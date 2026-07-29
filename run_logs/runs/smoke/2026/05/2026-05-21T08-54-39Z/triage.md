# Triage notes — release-prep run 2026-05-21T08-54-39Z

Analytical clustering of the 3 failures from this run, grouped by suspected
root cause. Run took 6195s ≈ 103 min, up from 95 min in the prior run
(2026-05-20T18-55-23Z) — duration growth is mostly the previously-failing
scripts now running to completion (BlackJAXNUTS +10s real-sampler, NUFFT +1s,
rectangular_dspl +60s vmap+JIT, double_einstein_ring/slam +90s before parking
kicks in next run, etc.).

**Headline:** Cycle of 5 PRs (autolens_workspace_test #110, autolens_workspace
#194, autogalaxy_workspace #91, autogalaxy_workspace_test #53,
autofit_workspace_test #30) cleared **8 of 10 prior failures**, including
the H-grid `grid_search_parallel` timeout that I couldn't reproduce locally
(confirmed transient — passed this run). Two of the prior 10 failures
persisted (autolens aggregator NoneType ×2 — my "self-resolves on clean
run" theory was wrong; this is a real bug requiring code work) and one
brand-new failure surfaced (`jax_likelihood_functions/datacube/delaunay.py`
— but with a truncated traceback that gives no signal).

Pass rate: **508 / 511 unskipped scripts (99.4%)** — up from 98.1%. Skip
ledger grew by 4 (10→11 SLOW, 18→20 NEEDS_FIX): the H-jit interferometer
SLOW + the D group/ double_einstein_ring NEEDS_FIX + the G MGE singular
NEEDS_FIX all landed and are now suppressing those failures.

Library pre-flight before this run: 3531 unit tests passing across all 5
libraries (unchanged).

## Cluster A — autolens aggregator `mask_header_from` NoneType (2 scripts, **PERSISTING — real bug, not stale output**)

- `autolens_workspace/scripts/guides/results/aggregator/data_fitting.py` — `TypeError: 'NoneType' object is not subscriptable` at `agg_util.mask_header_from`
  - **Repro:** `(cd autolens_workspace && env PYAUTO_SKIP_VISUALIZATION=1 PYAUTO_SKIP_CHECKS=1 PYAUTO_DISABLE_JAX=1 PYAUTO_FAST_PLOTS=1 JAX_ENABLE_X64=True NUMBA_CACHE_DIR=/tmp/numba_cache MPLCONFIGDIR=/tmp/matplotlib python3 scripts/guides/results/aggregator/data_fitting.py)`
- `autolens_workspace/scripts/guides/results/aggregator/models.py` — same
  - **Repro:** `(cd autolens_workspace && env PYAUTO_SKIP_VISUALIZATION=1 PYAUTO_SKIP_CHECKS=1 PYAUTO_DISABLE_JAX=1 PYAUTO_FAST_PLOTS=1 JAX_ENABLE_X64=True NUMBA_CACHE_DIR=/tmp/numba_cache MPLCONFIGDIR=/tmp/matplotlib python3 scripts/guides/results/aggregator/models.py)`

The previous triage (2026-05-20T18-55-23Z) hypothesized this was a stale-output
cascade that would self-heal on the next clean `run_all`. **That was wrong.**
Both scripts ran fresh (after `start_here.py` succeeded in this run) and still
failed with the same `agg_util.mask_header_from` NoneType.

Diagnostic comparison vs the working autogalaxy side:

| | autolens | autogalaxy |
|---|---|---|
| `output/results_folder/<dataset>/results/<hash>/` exists? | yes | yes |
| `image/dataset.fits` exists in that dir? | **yes** | yes |
| `files/{model,samples,…}.json` exist? | yes | yes |
| `agg.values("dataset.mask")` returns | **`[None]`** | `[Mask2D(...)]` |
| Aggregator query `fit.value(name="dataset")` returns | **`None`** | non-None |

Both have a `dataset.fits` on disk; both have an aggregator that finds 1
search output. The difference is that for autogalaxy the aggregator can
resolve `name="dataset"` to the on-disk fits file, but for autolens it
returns `None`.

The autolens `start_here.py` already has the same HDU-index shift
(`data_hdu=1, noise_map_hdu=2, psf_hdu=3`) that fixed the autogalaxy side
in commit `c2902672` (2026-05-08), so the upstream "Simple-Loading" path is
correct on both. The bug is elsewhere in the autolens output-write or
aggregator-name-registration path.

Two candidate root causes worth investigating first:

1. **The `_quick_fit.py` script (subprocess invoked when `output/results_folder`
   doesn't exist) writes a different output layout than `start_here.py`.**
   `data_fitting.py`'s bootstrap explicitly calls `_quick_fit.py`, not
   `start_here.py`. If `_quick_fit.py` saves the dataset under a different
   name (or doesn't register it at all), the aggregator query fails. The
   autogalaxy `_quick_fit.py` and the autolens one differ in the model setup
   (lens + MGE source vs single-galaxy Sersic+Exponential) but their structure
   looks analogous on the surface — the difference must be in some subtler
   `name=` argument to `analysis.save_attributes` or similar.

2. **The `image/dataset.fits` file is being written by the visualization
   pipeline (after the fit finishes) under a `name` key that doesn't match
   what the aggregator queries.** Check whether the autolens results saving
   path registers `dataset` as a name in `files/` (the `files/*.json`
   manifest is what the aggregator probably consumes).

**Action:** the right next step is a focused investigation:
- Open the autolens `_quick_fit.py` and the analogous autogalaxy one
  side-by-side; find the `save_attributes` / output-registration calls that
  differ.
- Or open `PyAutoLens` `AnalysisImaging` vs `PyAutoGalaxy` `AnalysisImaging`
  and look for a `visualize` / `save_results_to_aggregator` hook that
  registers `dataset` on the autogalaxy side but not autolens.

Likely a one-line fix once the divergence is identified. The aggregator
query API itself is the same.

## Cluster B — `jax_likelihood_functions/datacube/delaunay.py` (1 script, **new — but truncated traceback**)

- `autolens_workspace_test/scripts/jax_likelihood_functions/datacube/delaunay.py` — failure with no captured traceback (only the workspace-version-warning preamble visible)
  - **Repro:** `(cd autolens_workspace_test && env PYAUTO_TEST_MODE=2 PYAUTO_FAST_PLOTS=1 JAX_ENABLE_X64=True NUMBA_CACHE_DIR=/tmp/numba_cache MPLCONFIGDIR=/tmp/matplotlib python3 scripts/jax_likelihood_functions/datacube/delaunay.py)`

This script was on the failure list in the 2026-05-20T11-07-50Z run (as a
SIGKILL — probably OOM under JIT compilation of the datacube path) and got
RECOVERED in the 2026-05-20T18-55-23Z run. Now it's failing again in
2026-05-21T08-54-39Z — and the report's traceback capture is the trailing
2 KB of stderr, which here is entirely the
`PYAUTO_SKIP_WORKSPACE_VERSION_CHECK` warning preamble. No actual exception
line is visible in the captured tail.

The flip-flop between recoveries and failures on this script across the
last three runs (FAIL → PASS → FAIL) suggests a non-deterministic root
cause — likely memory pressure on the laptop GPU (6 GB RTX 2060 Max-Q,
documented in `feedback_jax_gpu_prealloc`) interacting with whatever JAX
state is left over from earlier scripts in the run_all queue. The new
datacube branch is the most memory-hungry corner of the JAX corpus, so
small changes in upstream allocation behaviour push it over or under the
OOM cliff.

**Action:** rerun in isolation with verbose output capture
(`python3 -u <script> 2>&1 | tail -200`) to see the actual exception. If
SIGKILL again → confirm OOM, park as NEEDS_FIX with a "laptop-GPU
prohibitive; revisit on bigger machine" reason matching the
`feedback_jax_gpu_prealloc` note. If a different error → investigate. Don't
trust the report-classified `source_code_bug` label; the auto-classifier
fell back to that when the traceback was unparseable.

## Summary

| Cluster | Scripts | Action | Status |
|---------|--------:|--------|--------|
| A — autolens aggregator NoneType | 2 | investigate `_quick_fit.py` vs `start_here.py` output-name divergence | persists from prior run; NOT a stale-output cascade — real bug |
| B — datacube/delaunay (truncated traceback) | 1 | rerun in isolation to surface the exception, then either park (OOM) or fix | flaky across last 3 runs |
| **Total** | **3** | **1 investigation + 1 diagnostic rerun** | |

### Compared to 2026-05-20T18-55-23Z

| Status | Count | Notes |
|--------|------:|-------|
| Failures cleared | 8 | B (BlackJAXNUTS env override), C (convolver env override), D (group/double_einstein_ring park), E (NUFFT tolerance 5→6), F (rectangular_dspl rebaseline), G (MGE singular park), H-jit (interferometer modeling_visualization_jit SLOW park), H-grid (grid_search_parallel transient, recovered without intervention) |
| Persisting | 2 | A (autolens aggregator NoneType ×2 — real bug, my prior self-resolve theory was wrong) |
| New regressions | 1 | datacube/delaunay (flaky — was failing on 2026-05-20T11-07-50Z as SIGKILL, passing on 2026-05-20T18-55-23Z, failing again here with truncated traceback) |

**Net delta: −7 failures (10 → 3).** Pass rate 98.1% → 99.4%. Total run
wall-clock 95 min → 103 min (the formerly-failing scripts that recovered
contribute their full runtime now instead of failing-fast).

### Path to release-ready

- **Cluster A** is the only real-code blocker. One focused investigation
  → likely one-line fix once the divergence between autolens and autogalaxy
  output-registration is identified.
- **Cluster B (datacube/delaunay)** is a diagnostic-then-decide entry. Most
  likely outcome: park as NEEDS_FIX with the GPU-memory rationale; the
  next run on a bigger machine (CI, not laptop) demonstrates whether it's
  actually a code bug or just a hardware constraint.

If both land in one more pass, we hit **0–1 failures** (depending on
datacube outcome), and the release-readiness gate becomes "ready" for the
first time in this triage thread.
