# Triage notes — release-prep run 2026-05-04T11-18-14Z

Analytical clustering of the 15 failures (12 FAIL + 3 TIMEOUT) from
this run, grouped by suspected root cause. Run took 9618s ≈ 160 min
(prior run was 95 min — extra ~65 min came from real-execution paths
unblocked by PR #70 on `autolens_workspace_test`, which is also the
source of Cluster D below).

The auto-classifier in `report.md` only labels each failure individually
(`source_code_bug` vs `workspace_issue` vs `workspace_data` vs `timeout`)
based on traceback patterns. This file is human triage on top of that.

**Headline:** 15 failures probably resolve to **8 underlying causes**.
The previous run was 48 → 10; this run is 15 → 8 — every cluster from
the previous triage that was fixed (A, B, C, D, E, F, G) has stayed
fixed. The new failures are predominantly *new* clusters (4 of 8 are
fresh) plus *recurrences* of two prior root-causes in different consumer
scripts (Cluster C prior-bound, Cluster E 2-vs-4 positions).

Pass rate: **395 / 410 unskipped scripts (96.3%)**.

## Cluster A — Aggregator `mask_header_from` NoneType cascade (4 scripts, 1 bug)

- `autogalaxy_workspace/scripts/guides/results/aggregator/data_fitting.py` — `TypeError: 'NoneType' object is not subscriptable`
- `autogalaxy_workspace/scripts/guides/results/aggregator/models.py` — same
- `autolens_workspace/scripts/guides/results/aggregator/data_fitting.py` — same
- `autolens_workspace/scripts/guides/results/aggregator/models.py` — same

All four fail at the **same library line** —
`PyAutoGalaxy/autogalaxy/aggregator/agg_util.py:101`:

```python
header = aa.Header(header_sci_obj=fit.value(name=name)[0].header)
```

`fit.value(name=name)` is returning `None`, and `None[0]` blows up. Both
autogalaxy and autolens hit the same path (autolens's aggregator imports
the autogalaxy helper). All four were touched by the recent
`autogalaxy_workspace#55` / `autolens_workspace#118` "Refactor
guides/results aggregator to share quick-fit helper" PRs — the
refactored quick-fit helper presumably no longer persists the
`dataset_label="<name>"` artefact that `fit.value(name=name)` looks up,
so the lookup returns None.

**Action:** either guard `mask_header_from` to skip header construction
when `fit.value(name)` is None, **or** make the new `_quick_fit` helper
persist the same dataset entry the old per-script code did. One library
or one workspace-helper fix; expect all 4 to recover.

## Cluster B — Aggregator `Model.sersic_index` AttributeError (2 scripts)

- `autolens_workspace/scripts/guides/results/aggregator/queries.py` — `AttributeError: 'Model' object has no attribute 'sersic_index'`
- `autolens_workspace/scripts/guides/results/aggregator/samples_via_aggregator.py` — same

Both scripts query the model for `sersic_index`. The traceback comes
from `PyAutoFit/autofit/mapper/prior_model/prior_model.py:422`'s
`__getattr__` — meaning the prior model literally doesn't have a
`sersic_index` field. Most likely the new `_quick_fit` helper builds a
model with `Sersic` swapped for `SersicCore` (which uses `serjic_index`
internally but doesn't expose it as a free parameter), or the field has
been collapsed into a fixed value.

**Action:** open `notebooks/guides/results/_quick_fit.ipynb` (the new
shared helper that just landed on `main`) and check what model it
builds. Update both query scripts to ask for the actual parameter name
the new helper exposes. One workspace-script alignment; both recover.

## Cluster C — group SLaM `PriorException` recurrence (2 scripts)

- `autolens_workspace/scripts/group/features/linear_light_profiles/slam.py` — `PriorException: upper limit of a prior must be greater than its lower limit` (at `mass.einstein_radius = af.UniformPrior(...)`)
- `autolens_workspace/scripts/group/features/pixelization/slam.py` — same

This is the **same root cause** as Cluster F item 3 in the prior triage
(prior bound under zero-luminosity test mode), recurring in two more
group SLaM scripts. The fix that landed in PR #117 (Cluster F items 2/3/5/9)
narrowed the prior-bound clamp to specific scripts; these two share the
same upstream pattern but were not in the original PR's file list.

**Action:** apply the same prior-bound clamp pattern from PR #117 to
these two scripts. Mechanical port — identical 2–3 line change in each.
Both recover.

## Cluster D — `modeling_visualization_jit*` timeouts after PR #70 unblock (3 scripts)

- `autolens_workspace_test/scripts/imaging/modeling_visualization_jit.py` — TIMEOUT 300s
- `autolens_workspace_test/scripts/imaging/modeling_visualization_jit_delaunay.py` — TIMEOUT 300s
- `autolens_workspace_test/scripts/imaging/modeling_visualization_jit_rectangular.py` — TIMEOUT 301s

Background: in the prior triage these three (plus a 4th
`autogalaxy_workspace_test/imaging/modeling_visualization_jit.py`)
**failed fast** with `AssertionError: expected jax.Array, got numpy.float64`
(prior triage Cluster C). PR #24 / #70 (autogalaxy/autolens
`workspace_test`) — `fix(env): unblock modeling_visualization_jit
tests in CI defaults` — fixed that assertion. PR #70 was rebased into
this run mid-flight when the autolens_workspace_test pre-build push was
rejected and pulled.

Now the assertion no longer fires, the autogalaxy script passes (88.6s,
visible in slowest-25 table), and the three autolens scripts run far
enough to hit the 300s per-script cap. So this is a real perf issue,
not a regression — JIT compilation + full visualization on imaging
takes >300s on the autolens variants but ~90s on the autogalaxy variant.

**Action options:**
- (a) Park as `# SLOW <date>` in `autolens_workspace_test/config/build/no_run.yaml` and file a perf issue.
- (b) Add a per-pattern `env_vars.yaml` override to set a longer timeout for these three (but `run.py`'s timeout is a CLI arg, not env-var driven — so this would need a small `run_python.py` change).
- (c) Investigate why the autolens variants are 3.5× slower than the autogalaxy one and fix at source.

Recommend (a) for now (matches how every other SLOW timeout is parked)
plus a follow-up issue for (c).

## Cluster E — `point_source/fit.py` 2-vs-4 positions broadcast (1 script)

- `autolens_workspace/scripts/point_source/fit.py` — `ValueError: operands could not be broadcast together with shapes (2,) (4,)` (at `_array / other` in `autoarray/abstract_ndarray.py:326`)

Same family as the prior triage's Cluster E (`PointSolver.solve()`
short-circuits to 2 positions under `PYAUTO_SMALL_DATASETS=1` while the
consumer expects 4). The deblending sweep in PR #119 fixed the
`deblending/simulator.py` and `deblending/modeling.py` consumers but
did not touch `point_source/fit.py`. This script presumably hardcodes
a 4-element positions array and divides it by `solver.solve()`'s
2-element output.

**Action:** apply the same `len(positions)` indexing pattern from PR
#119 to `point_source/fit.py`. One-line fix.

## Cluster F — `subhalo/detect/start_here.py` missed `source` → `source_lp` rename (1 script)

- `autolens_workspace/scripts/group/features/advanced/subhalo/detect/start_here.py` — `NameError: name 'source' is not defined. Did you mean: 'source_lp'?` (line 634, `source=source` in `af.Collection(...)`)

Python's NameError suggestion **literally tells us the fix**. A previous
sweep renamed the variable from `source` to `source_lp` everywhere
except this one usage in `subhalo_refine`'s lens_dict construction.
Trivial. The file appears in 4 "Recently modified" PRs but none of them
caught this stale reference.

**Action:** change `source=source` → `source=source_lp` on line 634.
One-line fix.

## Cluster G — `fitness_dispatch.py` private attribute drift (1 script)

- `autofit_workspace_test/scripts/jax_assertions/fitness_dispatch.py` — `AttributeError: Analysis has no attribute _jitted_fit_from` (at `analysis._jitted_fit_from is not None`)

The test asserts that after fitting, `Analysis._jitted_fit_from` is set.
But `PyAutoFit/autofit/non_linear/analysis/analysis.py:135`'s
`__getattr__` rejects the lookup — meaning the library either renamed
`_jitted_fit_from` to something else, or the JIT dispatch path no
longer caches the jitted callable on the analysis instance.

**Action:** read `PyAutoFit/autofit/non_linear/analysis/analysis.py`
around the JIT path. Either the assertion needs to look at the new
attribute name (test-side fix), or the library lost the cached
attribute (library-side fix). One small investigation — cheap.

## Cluster H — `double_einstein_ring/slam.py` FitException in test-mode bypass (1 script)

- `autolens_workspace/scripts/imaging/features/advanced/double_einstein_ring/slam.py` — `autofit.exc.FitException` (at `_fit_bypass_test_mode` → `analysis.log_likelihood_function(instance)` → `PyAutoLens/autolens/imaging/model/analysis.py:84` raises)

This is **different** from the prior Cluster F item 4 — that one was an
`IndexError` in `result.py:445` (fixed and merged via PR #491,
`source_plane_inversion_centre_from`). This new failure is in the same
script but in a different code path: the bypass instance from
`abstract_search.py:848` fails likelihood evaluation, and analysis.py:84
raises `FitException` rather than returning a finite logL.

**Action:** read `PyAutoLens/autolens/imaging/model/analysis.py`
around line 84 to see what triggers the raise (probably an inversion
solve that fails for the synthetic test-mode parameters). This may need
a real investigation — could be a library issue, could be a script-level
issue with how the test-mode parameters are constructed.

## Summary

| Cluster | Scripts | Hypothesised single fix? |
|---------|---------|--------------------------|
| A — aggregator mask_header NoneType | 4 | yes (1 library or workspace-helper line) |
| B — aggregator sersic_index | 2 | yes (workspace alignment with new _quick_fit helper) |
| C — group SLaM PriorException | 2 | yes (port PR #117 clamp pattern) |
| D — modeling_visualization_jit timeouts | 3 | yes (SLOW-mark for now; perf issue) |
| E — point_source/fit broadcast | 1 | yes (port PR #119 pattern) |
| F — subhalo source/source_lp rename | 1 | yes (one-line) |
| G — Analysis._jitted_fit_from | 1 | yes (small investigation) |
| H — double_einstein_ring FitException | 1 | needs investigation |
| **Total** | **15** | **8 clusters** |

Six of eight clusters are mechanical 1-line / 1-file fixes (or SLOW-marks).
Two (G, H) need a brief investigation to decide library-vs-script. None
look like they require deep redesign.
