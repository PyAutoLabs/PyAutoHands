# Triage notes — release-prep run 2026-05-07T15-42-17Z

Analytical clustering of the 14 failures (14 FAIL + 0 TIMEOUT) from
this run, grouped by suspected root cause. Run took 3768s ≈ 63 min
(prior run was 160 min — the 3 `modeling_visualization_jit*` timeouts
that ate 900s last time are now SLOW-skipped per prior triage Cluster D,
plus broad fixes shaved unrelated paths).

The auto-classifier in `report.md` only labels each failure individually
(`source_code_bug` vs `workspace_issue` vs `workspace_data` vs `timeout`)
based on traceback patterns. This file is human triage on top of that.

**Headline:** 14 failures probably resolve to **7 underlying causes**
once Cluster A is set aside as non-reproducing (see below). Every one
of the 8 clusters from the previous (2026-05-04) triage is gone — A is
fully resolved by autogalaxy_workspace `e0de5f07` (mirror of PR #129),
B has morphed into a wider model-query family, C/E/F/G are fully fixed
via PR landings, and D/H are parked via SLOW / NEEDS_FIX markers. The
remaining 12 effective failures split as: **1 recurrence** (B-family),
**5 fresh issues** (C, E, F, G, H), and **1 truncated-traceback
unknown** (D).

Pass rate: **408 / 422 unskipped scripts (96.7%)** as recorded in
`report.md` — up from 96.3%. Effectively **410 / 422 (97.2%)** once
the 2 Cluster A scripts (verified non-reproducing 2026-05-08) are
discounted. Skip ledger has grown: 70 scripts skipped (10 SLOW +
23 NEEDS_FIX + 37 misc), reflecting last week's parking decisions on
the previously-failing slow/broken scripts.

## Cluster A — RESOLVED (2026-05-08)

`data_fitting.py` and `models.py` were flagged for the
`mask_header_from` NoneType crash, but verification on 2026-05-08
showed both scripts exit `0` against the current tree under the same
smoke env that produced the original failure. The mirror of PR #129
that the original action called for is already in
`autogalaxy_workspace/scripts/guides/results/_quick_fit.py:27–37`
(commit `e0de5f07`, 2026-05-07 10:59 UTC), and `image/dataset.fits`
is present on disk. The failures captured in this run snapshot were
produced before `e0de5f07` propagated to the runner; no further
action required. See plan `cuddly-booping-cat.md`.

## Cluster B — Aggregator KeyError on missing model parameter paths (4 scripts, new family — same root cause)

- `autogalaxy_workspace/scripts/guides/results/start_here.py` — `KeyError: ('galaxies','galaxy','bulge','ell_comps','ell_comps_0')`
- `autogalaxy_workspace/scripts/guides/results/aggregator/galaxies_fit.py` — same key
- `autogalaxy_workspace/scripts/guides/results/aggregator/samples.py` — same key
- `autogalaxy_workspace/scripts/guides/results/aggregator/samples_via_aggregator.py` — `KeyError: ('galaxies','galaxy','bulge','centre','centre_0'), ('galaxies','galaxy','disk','centre','centre_0')`

All four raise from
`PyAutoFit/autofit/non_linear/samples/sample.py:114`'s
`parameter_lists_for_paths` — meaning the consumer scripts query a
parameter path that doesn't exist in the model the new `_quick_fit`
helper builds. Three share the same `bulge.ell_comps` path; the fourth
queries `bulge.centre` / `disk.centre`. Same shape of bug as
**2026-05-04 Cluster B** (`Model.sersic_index` AttributeError) — the
`_quick_fit` helper (autogalaxy_workspace PR #55) appears to use a
profile that doesn't expose `ell_comps` (probably `SersicCore` with
fixed ellipticity, or a `Sersic` with `ell_comps` fixed).

**Action:** open `autogalaxy_workspace/scripts/guides/results/_quick_fit.py`,
read off the actual `Model` it builds, and update the four consumer
scripts to query the parameters that model exposes. This is the same
mechanical fix that PR #130 did for the autolens-side aggregator
queries. One workspace-script alignment pass; all 4 recover.

## Cluster C — JAX point_source likelihood baseline drift (3 scripts, new)

- `autolens_workspace_test/scripts/jax_likelihood_functions/point_source/image_plane.py` — `DESIRED: array(1.313508)` vs `ACTUAL: -83.380...`
- `autolens_workspace_test/scripts/jax_likelihood_functions/point_source/point.py` — same expected/actual
- `autolens_workspace_test/scripts/jax_likelihood_functions/point_source/source_plane.py` — `DESIRED: array(-199.155581)` vs `ACTUAL: -331481.26`

All three fail `np.testing.assert_allclose` against a recorded
likelihood baseline. `image_plane.py` and `point.py` share the **exact
same** expected-vs-actual numbers (1.313508 vs -83.38), strongly
suggesting they sample the same simulator output. Same family as
**2026-04-29 Cluster B** (rectangular/delaunay JAX baseline drift,
which was rebaselined and then stayed fixed for the next two runs).

The drift coincides with the autolens_workspace PR #132
(`fix: derive point_source/fit.py positions data from solver output`)
and PR #127 (realistic position/time-delay/flux noise in point source
simulators) — both touched the upstream simulator's positions/noise
generation. The recorded benchmarks here predate those simulator
changes.

**Action:** rebaseline the three `DESIRED:` constants by running each
script once outside test mode and copying the new likelihood into the
script's `expected_likelihood = ...` literal. If after rebaselining the
new value still looks unphysical (e.g. extreme negative log-likelihood
suggesting the simulator/likelihood are out of sync), then it's a real
upstream regression — but baseline drift is the much more likely
explanation. Three two-line edits; all three recover.

## Cluster D — `autolens/guides/results/start_here.py` truncated traceback (1 script, unknown)

- `autolens_workspace/scripts/guides/results/start_here.py` — FAIL (52.7s); traceback truncated to a numpy printout of `[..., [14 14]].` pixel coordinates only.

The `report.md` capture only retains the tail ~2KB of stderr, and the
script's last action before failing was printing a 15×15-grid array of
pixel coords — so the actual exception line was clipped off. The
script is on the list of "Recently modified" by 7 different PRs
(autogalaxy_workspace #55 / #56 / #58, autolens_workspace #123 / #126
/ #127 / #133), so attribution is wide.

The 52.7s runtime is unusual for a small-dataset run — most failing
scripts in this cluster fail in <5s. This implies the script ran a
real fit to completion and then failed in post-fit visualisation /
inversion / aggregator-style code that emits a coordinate array.

**Action:** rerun in isolation with full stderr captured —
`python scripts/guides/results/start_here.py 2>&1 | tail -200` —
to see the actual exception, then classify. Likely either an
`AssertionError`/`ValueError` in mapper code (pixel coords are mapper
output) or a synthetic-test-mode boundary issue similar to the
double_einstein_ring class. One investigation; classification then
trivial.

## Cluster E — `multi/visualization_imaging.py` mask vs data shape mismatch (1 script, new)

- `autolens_workspace_test/scripts/multi/visualization_imaging.py` — `ValueError: operands could not be broadcast together with shapes (150,150) (15,15)` at `dataset.apply_mask(mask=mask)` (`PyAutoArray/.../imaging/dataset.py:263`).

The dataset is full-size (150×150) while the mask is small-dataset-cap
size (15×15). Either:

- (a) The mask is built with `PYAUTO_SMALL_DATASETS=1` honoured (15×15
  cap) but the dataset isn't because the script reads it from disk
  with no cap applied; or
- (b) Vice-versa.

The `_test` workspaces normally have `PYAUTO_TEST_MODE=0` and
`PYAUTO_SMALL_DATASETS` unset — except this script is in `multi/`
which may be importing helpers that flip the env flag.

**Action:** read the script's mask-construction block; ensure mask
shape is derived from `dataset.shape_native`, not from a hardcoded
constant or from a different dataset. One-line fix likely.

## Cluster F — `autofit_test/database/scrape/sensitivity.py` None dataset (1 script, new)

- `autofit_workspace_test/scripts/database/scrape/sensitivity.py` — `AttributeError: 'NoneType' object has no attribute 'data'` at line 241: `super().__init__(data=dataset.data, noise_map=dataset.noise_map)`

The sensitivity job in `PyAutoFit/.../grid/sensitivity/job.py:167`
calls `self.base_fit_cls(...)` which routes through the script's
`__call__` (line 390) and constructs `Analysis(dataset=dataset)` —
where `dataset` is `None`. The job machinery is failing to build /
forward the per-cell dataset.

**Action:** read `PyAutoFit/.../sensitivity/job.py` around lines
150-170 and check what builds the dataset for each grid cell.
Probably either:
- The script's `simulate_function` returns `None` under test mode (a
  workspace-script bug), or
- The job's dataset wiring was broken by a recent PyAutoFit refactor
  (library bug).

Brief investigation needed; expect a one-line fix on whichever side
broke.

## Cluster G — `BlackJAXNUTS.py` `info['ess_min']` KeyError (1 script, new)

- `autofit_workspace_test/scripts/searches/BlackJAXNUTS.py` — `KeyError: 'ess_min'` at line 109: `print(f"ESS (min over dims): {info['ess_min']:.1f}")`

`BlackJAXNUTS` is a brand-new search added in PyAutoFit PR #1256. The
test script accesses `info['ess_min']` but the search's info dict
doesn't expose that key (it likely uses `min_ess` or `effective_sample_size_min`
or similar — common naming variations).

**Action:** print `list(info.keys())` once to discover the actual key
name, then either:
- (a) update the script's lookup to match, or
- (b) add an `ess_min` alias inside the BlackJAXNUTS implementation if
  this naming was a contract — a quick `git log -p PyAutoFit -- '*BlackJAX*'`
  on the PR will tell us which side intended which.

One-line fix on whichever side.

## Cluster H — `autogalaxy/guides/hpc/example_cpu_and_gpu.py` pathlib-refactor leftover (1 script, new)

- `autogalaxy_workspace/scripts/guides/hpc/example_cpu_and_gpu.py` — `NameError: name 'path' is not defined. Did you mean: 'Path'?` at line 64: `Path(path.sep) / "hpc" / "data" / "hpc_username" / "output"`

This is a leftover from autogalaxy_workspace PR #59
(`refactor: replace os.path with pathlib in workspace scripts`).
The blanket conversion replaced `from os import path` with
`from pathlib import Path` but missed `path.sep` on line 64 — that
specific reference was relying on `os.path.sep` (a string) not on
the `os.path` module per se.

**Action:** replace `Path(path.sep)` with `Path("/")` (or
`Path(os.sep)` after adding `import os`). The intent is to seed an
absolute root path; either form does that. One-line fix.

The autolens-workspace twin (`autolens_workspace/scripts/guides/hpc/example_cpu_and_gpu.py`,
PR #128) is **not** in the failure list — it's `SKIPPED` with reason
`"HPC paths dont exist locally."`. The autogalaxy variant should
either be skipped the same way (add to autogalaxy `no_run.yaml`) or
fixed and kept runnable. Recommend fix-and-keep, since the bug is a
trivial typo that would fail loudly for any user who tried to follow
the HPC example.

## Summary

| Cluster | Scripts | Hypothesised single fix? | Status vs prior |
|---------|---------|--------------------------|-----------------|
| ~~A — aggregator mask_header NoneType~~ | ~~2~~ | RESOLVED 2026-05-08 — verified non-reproducing against current tree (see Cluster A note above) | n/a |
| B — aggregator KeyError on missing model paths | 4 | yes (workspace queries align with new `_quick_fit`, mirror PR #130) | morphed from prior Cluster B (sersic_index → ell_comps/centre) |
| C — JAX point_source baseline drift | 3 | yes (rebaseline 3 `DESIRED:` constants) | new family (same shape as 2026-04-29 Cluster B) |
| D — autolens guides/results/start_here truncated | 1 | unknown (rerun for stderr) | new — needs investigation |
| E — multi/visualization_imaging shape mismatch | 1 | yes (one-line mask shape derive) | new |
| F — sensitivity.py None dataset | 1 | needs investigation (workspace vs library) | new |
| G — BlackJAXNUTS ess_min | 1 | yes (one-line key rename) | new (PR #1256 follow-up) |
| H — HPC `path.sep` NameError | 1 | yes (one-line typo fix) | new (PR #59 leftover) |
| **Total (open)** | **12** | **5 mechanical + 2 investigation** | |

Five of seven open clusters are mechanical fixes (≤ a handful of lines
each). Two (D, F) need a brief investigation. None look like deep
redesign.

### Compared to 2026-05-04

Every one of the prior 8 clusters is gone:
- A (mask_header): **fully resolved** 2026-05-08 — autogalaxy_workspace `e0de5f07` (mirror of PR #129) closes the autogalaxy half; verification confirmed both scripts pass against current tree
- B (sersic_index): morphed into Cluster B above
- C (group SLaM PriorException): **fixed** by PR #131
- D (modeling_visualization_jit timeouts): **parked** as SLOW (prior triage's recommended action (a))
- E (point_source/fit broadcast): **fixed** by PR #132
- F (subhalo source/source_lp rename): **fixed** by PR #133
- G (Analysis._jitted_fit_from): **fixed** (no longer surfaces)
- H (double_einstein_ring/slam.py FitException): **parked** as NEEDS_FIX

We are very close to all-green. With A already resolved, if B is fixed
in a `_quick_fit`-aligned follow-up (one autogalaxy_workspace PR) and
C is rebaselined, that takes us from 12 → 4 effective failures with
one more pass.
