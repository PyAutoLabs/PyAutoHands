# Adjusted Release Failure Report After Latent Refactor

Base report: `/home/jammy/Code/PyAutoLabs/PyAutoBuild/test_results/runs/2026-06-08T20-19-35Z/report.md`

The base report completed before the latent-class refactor merges:

- PyAutoFit `ff8ebd662` merged 2026-06-09 10:18:27 +0100
- PyAutoGalaxy `349bf8f5` merged 2026-06-09 10:18:52 +0100
- PyAutoLens `ae4a27afc` merged 2026-06-09 10:18:54 +0100
- autogalaxy_workspace `4b0b22db` merged 2026-06-09 10:19:22 +0100
- autolens_workspace `953726ba` merged 2026-06-09 10:19:19 +0100

Therefore, the base report remains useful as a release snapshot, but any latent/JAX
failure needed to be rechecked before being treated as still active.

## Targeted Rerun After Latent Refactor

Rerun completed 2026-06-09 against the current checkouts. Logs are under:

`/tmp/pyauto-latent-refactor-targeted/`

Result: all five latent/JAX-suspect failures still reproduce.

| Script | Status | Current failure |
|--------|--------|-----------------|
| `autofit_workspace_test/scripts/jax_assertions/fitness_dispatch.py` | FAIL | `Analysis has no attribute _jitted_fit_from` |
| `autogalaxy_workspace/scripts/guides/results/start_here.py` | FAIL | invalid/zero noise-map values |
| `autogalaxy_workspace_test/scripts/ellipse/modeling_visualization_jit.py` | FAIL | expected `jax.Array`, got `numpy.float64` |
| `autogalaxy_workspace_test/scripts/ellipse/visualization_jax.py` | FAIL | `fit_ellipse.png` not produced |
| `autogalaxy_workspace_test/scripts/interferometer/modeling_visualization_jit.py` | FAIL | `compute_latent_samples` empty stack |

## Current Grouping

### A. Active After Latent Refactor Rerun

These failures touch `Analysis`, latent computation, or workspace latent/JAX
examples and still fail after the latent refactor:

- `autofit_workspace_test/scripts/jax_assertions/fitness_dispatch.py`
  - `Analysis has no attribute _jitted_fit_from`
- `autogalaxy_workspace/scripts/guides/results/start_here.py`
  - invalid/ill-defined noise map values
- `autogalaxy_workspace_test/scripts/ellipse/modeling_visualization_jit.py`
  - expected `jax.Array`, got `numpy.float64`
- `autogalaxy_workspace_test/scripts/ellipse/visualization_jax.py`
  - `fit_ellipse.png` not produced
- `autogalaxy_workspace_test/scripts/interferometer/modeling_visualization_jit.py`
  - `compute_latent_samples` empty stack

### B. Likely Still Active: PyAutoFit Database Scrape Output

These have the same symptom: the script runs but the database aggregator is empty.

- `autofit_workspace_test/scripts/database/scrape/grid_search.py`
  - `assert len(agg) > 0`
- `autofit_workspace_test/scripts/database/scrape/sensitivity.py`
  - `assert len(agg) > 0`

### C. Likely Still Active: Autolens JAX Simulator API Drift

- `autolens_workspace_test/scripts/imaging/simulator_use_jax_parity.py`
  - `autolens.util.register_tracer_classes` missing
- `autolens_workspace_test/scripts/interferometer/simulator_use_jax_parity.py`
  - `autolens.util.register_tracer_classes` missing
- `autolens_workspace_test/scripts/cluster/simulator.py`
  - jitted function receives non-static `Galaxy` argument

### D. Likely Still Active: Heavy Datacube JAX Failure

- `autolens_workspace_test/scripts/jax_likelihood_functions/datacube/delaunay.py`
  - process killed by `SIGKILL`

### E. Likely Still Active: Tutorial / Workspace Script Issues

- `HowToGalaxy/scripts/chapter_4_pixelizations/tutorial_2_mappers.py`
  - mapper index out of range
- `HowToLens/scripts/chapter_1_introduction/tutorial_3_more_ray_tracing.py`
  - plot axis limits contain NaN/Inf
- `HowToLens/scripts/chapter_2_lens_modeling/tutorial_6_masking_and_positions.py`
  - zero-size mask/convolver array

## Fix Order

1. Fix Group A first because it still fails after the newly merged latent refactor and is closest to the changed code.
2. Within Group A, start with `autofit_workspace_test/scripts/jax_assertions/fitness_dispatch.py`, because it is the smallest PyAutoFit-level dispatch assertion and may explain downstream JAX visualization behaviour.
3. Then fix the autogalaxy visualization/latent failures.
4. After Group A clears, move to Group B (`autofit_workspace_test` database scrape output), because it is two failures with one likely root cause.
