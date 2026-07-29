# Triage notes — release-prep run 2026-04-29T14-48-47Z

Analytical clustering of the 48 failures, grouped by suspected root cause.
The auto-classifier in `report.md` only labels each failure individually
(`source_code_bug` vs `workspace_issue` vs `workspace_data` vs `timeout`)
based on traceback patterns. This file is human triage on top of that.

48 failures probably resolve to **~10 underlying causes**, not 48 separate
bugs.

## Cluster A — `autolens/group/features/pixelization/*` (5 scripts, 1 bug)

- `delaunay.py` — `AttributeError: 'NoneType' object has no attribute 'array'`
- `fit.py` — same
- `likelihood_function.py` — same
- `modeling.py` — `TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'`
- `slam.py` — `AttributeError: 'NoneType' object has no attribute 'positions'`

All five scripts in one folder, all None-dereferences in the same construction
path. Almost certainly one upstream API change (constructor returning `None`
where it used to return an object) cascading through every variant. Fix the
constructor or its caller; expect all five to recover.

## Cluster B — `autolens_workspace_test/jax_likelihood_functions/*` numerical drift (8 scripts)

- `imaging/delaunay.py`, `imaging/rectangular.py`, `imaging/rectangular_dspl.py`,
  `imaging/rectangular_mge.py`, `multi/delaunay.py`, `multi/delaunay_mge.py`,
  `multi/mge.py`, `multi/rectangular.py`, `multi/rectangular_mge.py`

All fail with `DESIRED: array(<value>)` — meaning the `np.testing.assert_allclose`
inside each benchmark hit a likelihood that no longer matches the recorded
expected value. Either:

- (a) a real numerical regression in PyAutoArray / PyAutoLens that affects
  rectangular + delaunay pixelizations under JAX; or
- (b) the recorded baseline is stale and needs refreshing.

Action: pick one script (e.g. `imaging/rectangular.py`), compute the expected
value by hand, decide which side moved. If (b), update all 8 baselines in one
sweep. If (a), file a bug against PyAutoArray.

## Cluster C — `modeling_visualization_jit*` JAX assertion (4 scripts)

- `autogalaxy_workspace_test/imaging/modeling_visualization_jit.py`
- `autolens_workspace_test/imaging/modeling_visualization_jit.py`
- `autolens_workspace_test/imaging/modeling_visualization_jit_delaunay.py`
- `autolens_workspace_test/imaging/modeling_visualization_jit_rectangular.py`

All fail `AssertionError: expected jax.Array, got <class 'numpy.float64'>`.

Looks like a single visualizer code path that asserts the input is a
JAX array but receives a numpy scalar. Almost certainly one missing
`jnp.asarray` or one upstream change that converted JAX→numpy. Fix once,
verify all four.

## Cluster D — `guides/results/aggregator/*` cascade (4 fails + 4 timeouts)

In both `autogalaxy_workspace` and `autolens_workspace`, the chain is:

1. `guides/results/start_here.py` — TIMEOUT (300s)  ← root cause
2. `guides/results/aggregator/galaxies_fit.py` / `galaxies_fits.py` — TIMEOUT (300s)
3. `guides/results/aggregator/samples.py` — TIMEOUT (300s)
4. `guides/results/aggregator/models.py` — `TypeError: 'NoneType' object is not subscriptable`
5. `guides/results/aggregator/queries.py` — `AttributeError: 'Model' object has no attribute 'sersic_index'`
6. `guides/results/aggregator/samples_via_aggregator.py` — `AttributeError: 'NoneType' object has no attribute 'parameter_lists'`

These scripts run real searches under `PYAUTO_TEST_MODE` unset. The ones
that depend on prior search output (the `models.py`, `queries.py`,
`samples_via_aggregator.py` fails) are downstream of the 300s timeouts —
no aggregator output exists, so the next script reads `None` and explodes.

Action: either bump the timeout further for this folder via an env override,
or mark them all as `# SLOW <date>` in the workspace `no_run.yaml`. (Many
peers in the same folder are already SLOW-marked.) The `start_here.py` SLOW
parking is what needs to come back; the rest cascade for free.

## Cluster E — Missing simulator output (5 scripts)

Files referenced but never produced:

- `dataset/imaging/simple/data.fits` — read by `autolens_workspace/guides/data_structures.py`,
  `guides/modeling/bug_fix.py`, `guides/modeling/chaining.py`,
  `autogalaxy_workspace/guides/plot/start_here.py`
- `dataset/point_source/deblending/data.fits` — read by
  `autolens_workspace/point_source/features/deblending/modeling.py`

The simulators that produce these failed too (e.g.
`point_source/features/deblending/simulator.py` failed with `IndexError: index 2
is out of bounds for axis 0 with size 2`). Fix the simulators first; the
downstream consumers will likely recover with no further work.

## Cluster F — API drift, isolated (probably 1-line fixes each)

- `autogalaxy_workspace/guides/advanced/over_sampling.py` —
  `TypeError: plot_grid() got an unexpected keyword argument 'plot_over_sampled_grid'`
- `autolens_workspace/group/features/advanced/subhalo/detect/start_here.py` —
  `Collection() got multiple values for keyword argument 'source'`
- `autolens_workspace/group/features/linear_light_profiles/slam.py` —
  `PriorException: upper limit must be greater than lower limit`
- `autolens_workspace/imaging/features/advanced/double_einstein_ring/slam.py` —
  `autofit.exc.FitException`
- `autolens_workspace/cluster/simulator.py` — JAX traceback (filtered)
- `autolens_workspace/point_source/fit.py` — broadcast shape (2,) vs (4,)
- `autofit_workspace/features/graphical_models.py` — missing
  `dataset/example_1d/gaussian_x1__low_snr/dataset_0/data.json`
- `autogalaxy_workspace/imaging/features/extra_galaxies/modeling.py` —
  missing `extra_galaxies_centres.json`
- `autolens_workspace/guides/plot/examples/plotters.py` — missing point-source data

Each looks isolated. None obviously share a cause with the clusters above.

## Cluster G — `pixelization/fit.py` shape unpack (2 workspaces)

- `autogalaxy_workspace/interferometer/features/pixelization/fit.py` —
  `ValueError: not enough values to unpack (expected 2, got 1)`
- `autolens_workspace/interferometer/features/pixelization/fit.py` — same

Same error in two workspaces, same script name. Likely one shared fixture
or helper that returns a different arity than the script expects. One fix.

## Cluster H — Other autolens_workspace_test failures

- `imaging/convolution.py` — `FileNotFoundError: scripts/imaging/images/residuals.png`
  (script tries to read its own output before producing it; ordering or env-var bug)
- `interferometer/model_fit.py` — `numpy.linalg.LinAlgError: Matrix is not positive definite`
  (numerical conditioning, possibly under small datasets — try without
  `PYAUTO_WORKSPACE_SMALL_DATASETS`)
- `interferometer/visualization.py` — `ValueError: not enough values to unpack`
  (same arity mismatch as Cluster G — possibly the same fix)

## Suggested triage order

1. **Cluster A** (group pixelization) — 5 scripts, 1 fix, easy win.
2. **Cluster C** (jit visualization) — 4 scripts, 1 fix.
3. **Cluster G + H** (pixelization/fit.py + visualization.py shape unpack) — 3 scripts, 1 fix.
4. **Cluster E** (simulators) — 2 simulator fixes recover 5 downstream consumers.
5. **Cluster B** (jax likelihood numerical drift) — investigate one, sweep eight.
6. **Cluster D** (aggregator cascade) — decide policy: bump timeout or extend SLOW skips.
7. **Cluster F** (isolated API drift) — pick off one at a time.

Plausible total developer effort: **~10 fixes**, not 48.

## Pointers

- Full per-failure tracebacks: `report.md` (this directory).
- Per-job markdowns (e.g. `autolens__scripts__group__script.md`) hold the
  short workspace-level summaries.
- Re-run the full set after fixes via `python autobuild/run_all.py` from
  PyAutoBuild root; the new run lands at `runs/<new-UTC>/` and `latest`
  flips automatically.
