# Release Readiness Report

**Status: NOT READY**

**Run:** `2026-05-07T15-42-17Z`  •  **Path:** `/home/jammy/Code/PyAutoLabs/PyAutoBuild/test_results/runs/2026-05-07T15-42-17Z`  •  **Total duration:** 3768.1s

## Slow-Skipped Scripts (needs performance fix)

**10 script(s)** are being skipped because they exceed the 60s per-script timeout cap. These are NOT permanent skips — they need the underlying performance issue fixed and the `SLOW` marker removed from the workspace's `config/build/no_run.yaml`.

| Workspace | Script | Marked | Age | Reason |
|-----------|--------|--------|-----|--------|
| autogalaxy_workspace | `guides/results/database/start_here` | 2026-04-10 | 27d | previously failed fast on a broken aggregator query; now runs the real aggregator and exceeds 60s |
| autogalaxy_workspace | `guides/results/workflow/csv_make` | 2026-04-10 | 27d | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| autolens_workspace | `guides/results/database/start_here` | 2026-04-10 | 27d | previously failed fast on a broken aggregator query; now runs the real aggregator and exceeds 60s |
| autolens_workspace_test | `database/scrape/multi_analysis` | 2026-04-10 | 27d | exceeds 60s timeout; _test workspaces run full searches without test mode |
| autolens_workspace_test | `database/scrape/slam_general` | 2026-04-10 | 27d | exceeds 60s timeout; _test workspaces run full searches without test mode |
| autolens_workspace_test | `database/scrape/slam_multi_one_by_one` | 2026-04-10 | 27d | exceeds 60s timeout; _test workspaces run full searches without test mode |
| autolens_workspace_test | `database/scrape/slam_pix` | 2026-04-10 | 27d | exceeds 60s timeout; _test workspaces run full searches without test mode |
| autolens_workspace_test | `imaging/modeling_visualization_jit` | 2026-05-07 | 0d | JIT + full visualization pipeline exceeds 300s cap (autogalaxy variant ~90s); unblocked by PR #70 from prior `expected jax.Array, got numpy.float64` AssertionError, now hits perf wall |
| autolens_workspace_test | `imaging/modeling_visualization_jit_delaunay` | 2026-05-07 | 0d | JIT + full visualization pipeline exceeds 300s cap; same root cause as modeling_visualization_jit |
| autolens_workspace_test | `imaging/modeling_visualization_jit_rectangular` | 2026-05-07 | 0d | JIT + full visualization pipeline exceeds 301s cap; same root cause as modeling_visualization_jit |

## Needs-Fix Scripts (parked for investigation)

**23 script(s)** are being skipped because they are broken and parked as a to-do list. These are NOT permanent skips — investigate the failure, fix the underlying bug, and remove the `NEEDS_FIX` marker from the workspace's `config/build/no_run.yaml`.

| Workspace | Script | Marked | Age | Reason |
|-----------|--------|--------|-----|--------|
| autofit_workspace | `features/interpolate` | 2026-04-10 | 27d | IndexError in InstanceInterpolator.__getitem__ when querying time == 1.5; value_map lookup falls through to empty instances list |
| autogalaxy_workspace | `autogalaxy_workspace/scripts/imaging/modeling` | 2026-04-10 | 27d | KeyError on ('galaxies','galaxy','bulge','ell_comps'...) kwargs after API drift in top-level imaging/modeling.py |
| autogalaxy_workspace | `ellipse/database` | 2026-04-24 | 13d | all ellipse examples parked pending JAX refactor; see PyAutoPrompt/autogalaxy/ellipse_no_run.md |
| autogalaxy_workspace | `ellipse/fit` | 2026-04-24 | 13d | all ellipse examples parked pending JAX refactor; see PyAutoPrompt/autogalaxy/ellipse_no_run.md |
| autogalaxy_workspace | `ellipse/modeling` | 2026-04-24 | 13d | all ellipse examples parked pending JAX refactor; see PyAutoPrompt/autogalaxy/ellipse_no_run.md |
| autogalaxy_workspace | `ellipse/multipoles` | 2026-04-24 | 13d | all ellipse examples parked pending JAX refactor; see PyAutoPrompt/autogalaxy/ellipse_no_run.md |
| autogalaxy_workspace | `ellipse/simulator` | 2026-04-24 | 13d | all ellipse examples parked pending JAX refactor; see PyAutoPrompt/autogalaxy/ellipse_no_run.md |
| autogalaxy_workspace | `imaging/data_preparation/manual/mask_irregular` | 2026-04-10 | 27d | silent failure, needs investigation |
| autogalaxy_workspace | `imaging/features/pixelization/modeling` | 2026-04-10 | 27d | LinAlgError: matrix not positive definite in pixelization modeling |
| autogalaxy_workspace | `interferometer/features/pixelization/modeling` | 2026-04-10 | 27d | LinAlgError: matrix not positive definite in interferometer pixelization modeling |
| autolens_workspace | `group/slam` | 2026-04-10 | 27d | PriorException: upper limit must be greater than lower limit in group SLaM pipeline |
| autolens_workspace | `imaging/data_preparation/manual/mask_irregular` | 2026-04-10 | 27d | silent failure, needs investigation |
| autolens_workspace | `imaging/features/advanced/double_einstein_ring/slam` | 2026-05-07 | 0d | autofit.exc.FitException in SLaM bypass mode (same family as imaging/features/pixelization/slam — Adapt regularization needs adapt_data which the synthetic samples_summary doesn't carry; cascade goes deep, fixing in one PR isn't tractable) |
| autolens_workspace | `imaging/features/pixelization/delaunay` | 2026-04-10 | 27d | autofit.exc.FitException in Delaunay pixelization fit |
| autolens_workspace | `imaging/features/pixelization/slam` | 2026-04-10 | 27d | autofit.exc.FitException in SLaM pixelization pipeline |
| autolens_workspace | `interferometer/features/pixelization/delaunay` | 2026-04-10 | 27d | broadcast shape mismatch (2,2) vs (1032,1032) in Delaunay interferometer |
| autolens_workspace | `multi/features/wavelength_dependence/modeling` | 2026-04-10 | 27d | autofit.exc.FitException in multi-wavelength modeling |
| autolens_workspace_test | `database/scrape/general` | 2026-04-27 | 10d | PyAutoGalaxy abstract_fit.linear_light_profile_intensity_dict raises "TypeError: __hash__ method should return an integer" during subplot_fit_imaging after the search completes (a light-profile object's __hash__ returns a non-int). Surfaced once the dataset_label="build" path fix let the script progress past Imaging.from_fits. |
| autolens_workspace_test | `imaging/visualization` | 2026-04-10 | 27d | AssertionError: dataset.png missing after visualization refactor |
| autolens_workspace_test | `jax_grad/imaging_lp` | 2026-04-10 | 27d | JAX traceback in gradient computation for light profile |
| autolens_workspace_test | `jax_grad/imaging_mge` | 2026-04-10 | 27d | AssertionError: Gradient is all zeros in MGE gradient computation |
| autolens_workspace_test | `jax_likelihood_functions/imaging/delaunay_mge` | 2026-04-10 | 27d | timeout in JAX likelihood function benchmark |
| autolens_workspace_test | `jax_likelihood_functions/imaging/mge_group` | 2026-04-10 | 27d | timeout in JAX likelihood function benchmark |

## Summary

| Passed | Failed | Skipped | Timeout |
|--------|--------|---------|---------|
| 408 | 14 | 70 | 0 |

## Per-Project Breakdown

| Project | Passed | Failed | Skipped | Timeout | Duration |
|---------|--------|--------|---------|---------|----------|
| autofit | 24 | 0 | 6 | 0 | 74.3s |
| autofit_test | 27 | 2 | 2 | 0 | 55.5s |
| autogalaxy | 83 | 7 | 18 | 0 | 621.7s |
| autogalaxy_test | 40 | 0 | 0 | 0 | 716.4s |
| autolens | 179 | 1 | 29 | 0 | 1451.8s |
| autolens_test | 55 | 4 | 15 | 0 | 848.4s |

## Slowest scripts (top 25)

| Script | Project | Status | Duration | Share |
|--------|---------|--------|----------|-------|
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_dspl.py` | autolens_test | passed | 71.0s | 1.9% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/multi/mge_group.py` | autolens_test | passed | 65.3s | 1.7% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/delaunay_mge.py` | autogalaxy_test | passed | 60.9s | 1.6% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/multi/mge_group.py` | autogalaxy_test | passed | 55.6s | 1.5% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_mge.py` | autolens_test | passed | 53.8s | 1.4% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/start_here.py` | autolens | failed | 52.8s | 1.4% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/workflow/csv_make.py` | autolens | passed | 44.6s | 1.2% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/multi/start_here.py` | autolens | passed | 44.1s | 1.2% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/units/flux.py` | autolens | passed | 41.5s | 1.1% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/multi_gaussian_expansion/modeling.py` | autogalaxy | passed | 40.4s | 1.1% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/delaunay_mge.py` | autogalaxy_test | passed | 39.1s | 1.0% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular_dspl.py` | autolens_test | passed | 38.4s | 1.0% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/database/scrape/scaling_relation.py` | autolens_test | passed | 38.2s | 1.0% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/los_halos/simulator.py` | autolens | passed | 37.6s | 1.0% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/delaunay_mge.py` | autolens_test | passed | 37.5s | 1.0% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/imaging/visualization.py` | autogalaxy_test | passed | 37.3s | 1.0% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/multi/delaunay_mge.py` | autogalaxy_test | passed | 36.8s | 1.0% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/advanced/graphical.py` | autolens | passed | 34.4s | 0.9% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/delaunay.py` | autolens_test | passed | 34.4s | 0.9% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/start_here.py` | autolens | passed | 33.9s | 0.9% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/multi_gaussian_expansion/modeling.py` | autolens | passed | 33.1s | 0.9% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/mge_group.py` | autogalaxy_test | passed | 31.4s | 0.8% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/multi/rectangular_mge.py` | autogalaxy_test | passed | 31.3s | 0.8% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/multi/delaunay_mge.py` | autolens_test | passed | 30.0s | 0.8% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/mge.py` | autolens_test | passed | 29.9s | 0.8% |

## Failures by Classification

### Source Code Bugs (11)

- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/database/scrape/sensitivity.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/database/scrape/sensitivity.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
    File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/grid/sensitivity/job.py", line 167, in perform
    result = self.base_fit_cls(
             ^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/database/scrape/sensitivity.py", line 390, in __call__
    analysis = self.analysis_cls(dataset=dataset)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/database/scrape/sensitivity.py", line 241, in __init__
    super().__init__(data=dataset.data, noise_map=dataset.noise_map)
                          ^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'data'
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/start_here.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/start_here.py']' returned non-zero exit status 1.
  - **Recently modified** in [docs: comprehensive output folder layout in modeling tutorials and use search.paths in results/start_here](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/58)
  - **Recently modified** in [Cluster E: fix guides/plot/start_here.py auto-simulate target](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/56)
  - **Recently modified** in [Refactor guides/results aggregator to share quick-fit helper](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/55)
  - **Recently modified** in [fix: restore missing source assignment in subhalo_refine (Cluster F)](https://github.com/PyAutoLabs/autolens_workspace/pull/133)
  - **Recently modified** in [docs: realistic position, time-delay, and flux noise in point source simulators](https://github.com/PyAutoLabs/autolens_workspace/pull/127)
  - **Recently modified** in [docs: comprehensive output folder layout in modeling tutorials and use search.paths in results/start_here](https://github.com/PyAutoLabs/autolens_workspace/pull/126)
  - **Recently modified** in [Add Delaunay datacube modeling + RectangularAdaptDensity + PositionsLH](https://github.com/PyAutoLabs/autolens_workspace/pull/123)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
      self.check_log_likelihood(fitness=self)
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/fitness.py", line 518, in check_log_likelihood
    parameters = max_log_likelihood_sample.parameter_lists_for_model(model=self.model)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/samples/sample.py", line 102, in parameter_lists_for_model
    return self.parameter_lists_for_paths(paths)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/samples/sample.py", line 114, in parameter_lists_for_paths
    raise KeyError(
KeyError: "Could not find any of the following keys in kwargs (('galaxies', 'galaxy', 'bulge', 'ell_comps', 'ell_comps_0'),)"
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/data_fitting.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/data_fitting.py']' returned non-zero exit status 1.
  - **Recently modified** in [Refactor guides/results aggregator to share quick-fit helper](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/55)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
    File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/data_fitting.py", line 115, in <module>
    for dataset_list in dataset_gen:
                        ^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoGalaxy/autogalaxy/aggregator/imaging/imaging.py", line 63, in _imaging_from
    mask, header = agg_util.mask_header_from(fit=fit)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoGalaxy/autogalaxy/aggregator/agg_util.py", line 101, in mask_header_from
    header = aa.Header(header_sci_obj=fit.value(name=name)[0].header)
                                      ~~~~~~~~~~~~~~~~~~~~^^^
TypeError: 'NoneType' object is not subscriptable
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/galaxies_fit.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/galaxies_fit.py']' returned non-zero exit status 1.
  - **Recently modified** in [Refactor guides/results aggregator to share quick-fit helper](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/55)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
      self.check_log_likelihood(fitness=self)
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/fitness.py", line 518, in check_log_likelihood
    parameters = max_log_likelihood_sample.parameter_lists_for_model(model=self.model)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/samples/sample.py", line 102, in parameter_lists_for_model
    return self.parameter_lists_for_paths(paths)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/samples/sample.py", line 114, in parameter_lists_for_paths
    raise KeyError(
KeyError: "Could not find any of the following keys in kwargs (('galaxies', 'galaxy', 'bulge', 'ell_comps', 'ell_comps_0'),)"
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/models.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/models.py']' returned non-zero exit status 1.
  - **Recently modified** in [Fix graphical_models.py auto-sim to call simulators_sample.py](https://github.com/PyAutoLabs/autofit_workspace/pull/50)
  - **Recently modified** in [Refactor guides/results aggregator to share quick-fit helper](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/55)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
    File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/models.py", line 102, in <module>
    for dataset_list, galaxies_list in zip(dataset_gen, galaxies_gen):
                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoGalaxy/autogalaxy/aggregator/imaging/imaging.py", line 63, in _imaging_from
    mask, header = agg_util.mask_header_from(fit=fit)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoGalaxy/autogalaxy/aggregator/agg_util.py", line 101, in mask_header_from
    header = aa.Header(header_sci_obj=fit.value(name=name)[0].header)
                                      ~~~~~~~~~~~~~~~~~~~~^^^
TypeError: 'NoneType' object is not subscriptable
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/samples.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/samples.py']' returned non-zero exit status 1.
  - **Recently modified** in [Refactor guides/results aggregator to share quick-fit helper](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/55)
  - **Recently modified** in [fix: align aggregator queries with MGE source bulge in autolens tutorials](https://github.com/PyAutoLabs/autolens_workspace/pull/130)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
      self.check_log_likelihood(fitness=self)
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/fitness.py", line 518, in check_log_likelihood
    parameters = max_log_likelihood_sample.parameter_lists_for_model(model=self.model)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/samples/sample.py", line 102, in parameter_lists_for_model
    return self.parameter_lists_for_paths(paths)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/samples/sample.py", line 114, in parameter_lists_for_paths
    raise KeyError(
KeyError: "Could not find any of the following keys in kwargs (('galaxies', 'galaxy', 'bulge', 'ell_comps', 'ell_comps_0'),)"
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/samples_via_aggregator.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/samples_via_aggregator.py']' returned non-zero exit status 1.
  - **Recently modified** in [Refactor guides/results aggregator to share quick-fit helper](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/55)
  - **Recently modified** in [fix: align aggregator queries with MGE source bulge in autolens tutorials](https://github.com/PyAutoLabs/autolens_workspace/pull/130)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/samples/interface.py", line 32, in wrapper
    vector = func(self, *args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/samples/interface.py", line 95, in max_log_likelihood
    return sample.parameter_lists_for_paths(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/samples/sample.py", line 114, in parameter_lists_for_paths
    raise KeyError(
KeyError: "Could not find any of the following keys in kwargs (('galaxies', 'galaxy', 'bulge', 'centre', 'centre_0'), ('galaxies', 'galaxy', 'disk', 'centre', 'centre_0'))"
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/point_source/image_plane.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/point_source/image_plane.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
    File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 921, in assert_array_compare
    raise AssertionError(msg)
AssertionError: 
Not equal to tolerance rtol=0.0001, atol=0
point_source/image_plane: JAX vmap likelihood mismatch
Mismatched elements: 1 / 1 (100%)
Max absolute difference among violations: 84.69400578
Max relative difference among violations: 64.47924625
 ACTUAL: array([-83.380498])
 DESIRED: array(1.313508)
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/point_source/point.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/point_source/point.py']' returned non-zero exit status 1.
  - **Recently modified** in [fix: derive point_source/fit.py positions data from solver output (Cluster E)](https://github.com/PyAutoLabs/autolens_workspace/pull/132)
  - **Recently modified** in [docs: realistic position, time-delay, and flux noise in point source simulators](https://github.com/PyAutoLabs/autolens_workspace/pull/127)
  - **Recently modified** in [docs: comprehensive output folder layout in modeling tutorials and use search.paths in results/start_here](https://github.com/PyAutoLabs/autolens_workspace/pull/126)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
    File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 921, in assert_array_compare
    raise AssertionError(msg)
AssertionError: 
Not equal to tolerance rtol=0.0001, atol=0
point: JAX vmap likelihood mismatch
Mismatched elements: 1 / 1 (100%)
Max absolute difference among violations: 84.69400578
Max relative difference among violations: 64.47924625
 ACTUAL: array([-83.380498])
 DESIRED: array(1.313508)
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/point_source/source_plane.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/point_source/source_plane.py']' returned non-zero exit status 1.
  - **Recently modified** in [docs: comprehensive output folder layout in modeling tutorials and use search.paths in results/start_here](https://github.com/PyAutoLabs/autolens_workspace/pull/126)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
    File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 921, in assert_array_compare
    raise AssertionError(msg)
AssertionError: 
Not equal to tolerance rtol=0.0001, atol=0
point_source/source_plane: JAX vmap likelihood mismatch
Mismatched elements: 1 / 1 (100%)
Max absolute difference among violations: 331282.10420019
Max relative difference among violations: 1663.43369359
 ACTUAL: array([-331481.259781])
 DESIRED: array(-199.155581)
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/multi/visualization_imaging.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/multi/visualization_imaging.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/multi/visualization_imaging.py", line 85, in <module>
    dataset = dataset.apply_mask(mask=mask)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/dataset/imaging/dataset.py", line 263, in apply_mask
    invalid = np.logical_and(self.data.mask, np.logical_not(mask))
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: operands could not be broadcast together with shapes (150,150) (15,15)
  ```
  </details>

## Skipped Tests

| Script | Reason |
|--------|--------|
| `interpolate.py` | NEEDS_FIX 2026-04-10 - IndexError in InstanceInterpolator.__getitem__ when querying time == 1.5; value_map lookup falls through to empty instances list |
| `dynesty_plotter.py` | Test Model Iniitalization no good. |
| `get_dist.py` | Cant get it to install, even in optional requirements. |
| `zeus_plotter.py` | Test Model Iniitalization no good. |
| `mcmc.py` | Zeus section in merged mcmc.py fails Test Model Initialization. |
| `start_point.py` | bug https://github.com/rhayes777/PyAutoFit/issues/1017 |
| `general.py` | Session mostly works but not maintaining currently. |
| `multi_analysis.py` | Session mostly works but not maintaining currently. |
| `simulator.py` | NEEDS_FIX 2026-04-24 - all ellipse examples parked pending JAX refactor; see PyAutoPrompt/autogalaxy/ellipse_no_run.md |
| `database.py` | NEEDS_FIX 2026-04-24 - all ellipse examples parked pending JAX refactor; see PyAutoPrompt/autogalaxy/ellipse_no_run.md |
| `fit.py` | NEEDS_FIX 2026-04-24 - all ellipse examples parked pending JAX refactor; see PyAutoPrompt/autogalaxy/ellipse_no_run.md |
| `modeling.py` | NEEDS_FIX 2026-04-24 - all ellipse examples parked pending JAX refactor; see PyAutoPrompt/autogalaxy/ellipse_no_run.md |
| `multipoles.py` | NEEDS_FIX 2026-04-24 - all ellipse examples parked pending JAX refactor; see PyAutoPrompt/autogalaxy/ellipse_no_run.md |
| `start_here.py` | SLOW 2026-04-10 - previously failed fast on a broken aggregator query; now runs the real aggregator and exceeds 60s |
| `searches.py` | Test mode breaks search visualization. |
| `csv_make.py` | SLOW 2026-04-10 - exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| `fits_make.py` | Test mode does not output .fits images. |
| `png_make.py` | Test mode does not output .png images. |
| `extra_galaxies_centres.py` | GUI scripts cannot be run |
| `light_centre.py` | GUI scripts cannot be run |
| `mask.py` | GUI scripts cannot be run |
| `mask_extra_galaxies.py` | GUI scripts cannot be run |
| `mask_irregular.py` | NEEDS_FIX 2026-04-10 - silent failure, needs investigation |
| `modeling.py` | NEEDS_FIX 2026-04-10 - LinAlgError: matrix not positive definite in pixelization modeling |
| `modeling.py` | NEEDS_FIX 2026-04-10 - KeyError on ('galaxies','galaxy','bulge','ell_comps'...) kwargs after API drift in top-level imaging/modeling.py |
| `modeling.py` | NEEDS_FIX 2026-04-10 - LinAlgError: matrix not positive definite in interferometer pixelization modeling |
| `start_here.py` | Cluster analysis is not maintained and test mode breaks it. |
| `modeling.py` | Cluster modeling is not maintained and test mode breaks it. |
| `slam.py` | NEEDS_FIX 2026-04-10 - PriorException: upper limit must be greater than lower limit in group SLaM pipeline |
| `start_here.py` | SLOW 2026-04-10 - previously failed fast on a broken aggregator query; now runs the real aggregator and exceeds 60s |
| `example_cpu.py` | HPC paths dont exist locally. |
| `searches.py` | Test mode breaks search visualization. |
| `fits_make.py` | Test mode does not output .fits images. |
| `png_make.py` | Test mode does not output .png images. |
| `start_here.py` | All sensitivity scripts need updating when visualization refactored. |
| `extra_galaxies_centres.py` | GUI scripts cannot be run |
| `lens_light_centre.py` | GUI scripts cannot be run |
| `mask.py` | GUI scripts cannot be run |
| `mask_extra_galaxies.py` | GUI scripts cannot be run |
| `positions.py` | GUI scripts cannot be run |
| `mask_irregular.py` | NEEDS_FIX 2026-04-10 - silent failure, needs investigation |
| `slam.py` | NEEDS_FIX 2026-05-07 - autofit.exc.FitException in SLaM bypass mode (same family as imaging/features/pixelization/slam — Adapt regularization needs adapt_data which the synthetic samples_summary doesn't carry; cascade goes deep, fixing in one PR isn't tractable) |
| `modeling.py` | Requires CSE to be JAX enabled. |
| `slam.py` | Requires CSE to be JAX enabled. |
| `database.py` | Unsure but not a feature actively used currently. |
| `slam_source_parametric.py` | All sensitivity scripts need updating when visualization refactored. |
| `slam_source_pixelized.py` | All sensitivity scripts need updating when visualization refactored. |
| `delaunay.py` | NEEDS_FIX 2026-04-10 - autofit.exc.FitException in Delaunay pixelization fit |
| `slam.py` | NEEDS_FIX 2026-04-10 - autofit.exc.FitException in SLaM pixelization pipeline |
| `casa_reduction.py` | Requires CASA MeasurementSet output, not runnable standalone |
| `delaunay.py` | NEEDS_FIX 2026-04-10 - broadcast shape mismatch (2,2) vs (1032,1032) in Delaunay interferometer |
| `modeling.py` | NEEDS_FIX 2026-04-10 - autofit.exc.FitException in multi-wavelength modeling |
| `simulator.py` | Blocked by PyAutoLens #480: solver finds 0 positions for intermediate-plane source |
| `modeling.py` | Blocked by PyAutoLens #480: same root cause as simulator above |
| `time_delays.py` | Test mode does not support cosmology ift |
| `general.py` | NEEDS_FIX 2026-04-27 - PyAutoGalaxy abstract_fit.linear_light_profile_intensity_dict raises "TypeError: __hash__ method should return an integer" during subplot_fit_imaging after the search completes (a light-profile object's __hash__ returns a non-int). Surfaced once the dataset_label="build" path fix let the script progress past Imaging.from_fits. |
| `multi_analysis.py` | SLOW 2026-04-10 - exceeds 60s timeout; _test workspaces run full searches without test mode |
| `slam_general.py` | SLOW 2026-04-10 - exceeds 60s timeout; _test workspaces run full searches without test mode |
| `slam_multi_one_by_one.py` | SLOW 2026-04-10 - exceeds 60s timeout; _test workspaces run full searches without test mode |
| `slam_pix.py` | SLOW 2026-04-10 - exceeds 60s timeout; _test workspaces run full searches without test mode |
| `modeling_visualization_jit.py` | SLOW 2026-05-07 - JIT + full visualization pipeline exceeds 300s cap (autogalaxy variant ~90s); unblocked by PR #70 from prior `expected jax.Array, got numpy.float64` AssertionError, now hits perf wall |
| `modeling_visualization_jit_delaunay.py` | SLOW 2026-05-07 - JIT + full visualization pipeline exceeds 300s cap (autogalaxy variant ~90s); unblocked by PR #70 from prior `expected jax.Array, got numpy.float64` AssertionError, now hits perf wall |
| `modeling_visualization_jit_rectangular.py` | SLOW 2026-05-07 - JIT + full visualization pipeline exceeds 300s cap (autogalaxy variant ~90s); unblocked by PR #70 from prior `expected jax.Array, got numpy.float64` AssertionError, now hits perf wall |
| `visualization.py` | NEEDS_FIX 2026-04-10 - AssertionError: dataset.png missing after visualization refactor |
| `visualization_cluster.py` | NEEDS_FIX 2026-04-10 - AssertionError: dataset.png missing after visualization refactor |
| `visualization_jax.py` | NEEDS_FIX 2026-04-10 - AssertionError: dataset.png missing after visualization refactor |
| `imaging_lp.py` | NEEDS_FIX 2026-04-10 - JAX traceback in gradient computation for light profile |
| `imaging_mge.py` | NEEDS_FIX 2026-04-10 - AssertionError: Gradient is all zeros in MGE gradient computation |
| `delaunay_mge.py` | NEEDS_FIX 2026-04-10 - timeout in JAX likelihood function benchmark |
| `mge_group.py` | NEEDS_FIX 2026-04-10 - timeout in JAX likelihood function benchmark |

## Changes Since Last Release

### [refactor: replace os.path with pathlib](https://github.com/PyAutoLabs/PyAutoFit/pull/1258) (PyAutoLabs/PyAutoFit)
**API Changes:** None — internal changes only. All public function signatures unchanged. Implementation switches from string-style joins to Path objects, but returned values, accepted argument types, and external behaviour are unchanged. Some test fixtures (`PlotPatch`) now stringify recorded paths to keep assertion

### [feat: add BlackJAXNUTS first-class non-linear search](https://github.com/PyAutoLabs/PyAutoFit/pull/1256) (PyAutoLabs/PyAutoFit)
**API Changes:** <details>
<summary>Full API change list</summary>

### Added

- `autofit.BlackJAXNUTS(name=None, path_prefix=None, unique_tag=None, num_warmup=500, num_samples=1000, num_chains=1, target_accept=0.8, max_num_doublings=10, seed=42, initializer=None, auto_correlation_settings=AutoCorrelationsSettings(c

### [Visualizer.visualize_combined: accept quick_update kwarg](https://github.com/PyAutoLabs/PyAutoFit/pull/1254) (PyAutoLabs/PyAutoFit)
**API Changes:** Tiny additive signature change on a single method. `Visualizer.visualize_combined` now declares `quick_update: bool = False` so callers may pass it (the factor-graph dispatch always does). Default no-op behaviour is preserved; subclasses that already override the method without `**kwargs` get unbloc

### [Fix AnalysisFactor.visualize_combined dispatch in FactorGraph](https://github.com/PyAutoLabs/PyAutoFit/pull/1253) (PyAutoLabs/PyAutoFit)
**API Changes:** <details>
<summary>API Changes</summary>

### Added
- `AnalysisFactor.visualize_combined(analyses, paths, instance, during_analysis, quick_update=False)` — forwards combined-visualization to the wrapped analysis's Visualizer.
- `AnalysisFactor.visualize_before_fit_combined(analyses, paths, model)` —

### [Refresh cached SearchUpdater when AbstractSearch.paths is reassigned](https://github.com/PyAutoLabs/PyAutoFit/pull/1252) (PyAutoLabs/PyAutoFit)
**API Changes:** None — internal change only. Existing callers see no behaviour difference unless they were affected by the bug. The `_updater` property remains a private cached lazily-initialised `SearchUpdater`; the only difference is that it now refreshes when the search's `paths` attribute has been reassigned to

### [Support fixed Array elements through the EP fitting pipeline](https://github.com/PyAutoLabs/PyAutoFit/pull/1250) (PyAutoLabs/PyAutoFit)
**API Changes:** Purely additive. New opt-in `EPAnalysisFactor.set_model_approx(model_approx)` hook called from `factor_step` if the factor implements it; default factors are unaffected. `factor_step` and `EPOptimiser.factor_step` now accept an additional keyword-only `model_approx=None` argument so the optimiser lo

### [Add EPAnalysisFactor for cavity-message injection](https://github.com/PyAutoLabs/PyAutoFit/pull/1248) (PyAutoLabs/PyAutoFit)
**API Changes:** Added `af.EPAnalysisFactor` — an `AnalysisFactor` subclass with a `set_cavity_dist(cavity_dist)` hook that the EP optimiser invokes before every fit, attaching the cavity `MeanField` to `analysis._cavity_mean_field` so the user's `log_likelihood_function` can read per-variable cavity messages (`.mea

### [refactor: replace os.path with pathlib](https://github.com/PyAutoLabs/PyAutoArray/pull/300) (PyAutoLabs/PyAutoArray)
**API Changes:** None — internal changes only. All public function signatures unchanged. Implementation switches from string-style joins to Path objects, but returned values, accepted argument types, and external behaviour are unchanged. Some test fixtures (`PlotPatch`) now stringify recorded paths to keep assertion

### [Fix subplot_of_mapper crash on interferometer data_subtracted](https://github.com/PyAutoLabs/PyAutoArray/pull/297) (PyAutoLabs/PyAutoArray)
**API Changes:** None — internal change to a plot helper. `subplot_of_mapper` / `subplot_mappings` signatures unchanged; behaviour for imaging fits is byte-identical. Interferometer fits previously crashed in panel 0; they now render a dirty data-subtracted image.

See full details below.

### [docs: convert index.rst to MyST .md](https://github.com/PyAutoLabs/PyAutoArray/pull/294) (PyAutoLabs/PyAutoArray)
**API Changes:** None — internal docs only.

### [Fix sign of poisson noise in preprocess.poisson_noise_via_data_eps_from](https://github.com/PyAutoLabs/PyAutoArray/pull/290) (PyAutoLabs/PyAutoArray)
**API Changes:** Behaviour-only change to two existing functions (signatures unchanged):
- `preprocess.poisson_noise_via_data_eps_from` now returns the true Poisson noise term (`noisy − data`) instead of its negation.
- `preprocess.data_eps_with_poisson_noise_added` and `SimulatorImaging.via_image_from(..., add_pois

### [refactor: replace os.path with pathlib](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/388) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** None — internal changes only. All public function signatures unchanged. Implementation switches from string-style joins to Path objects, but returned values, accepted argument types, and external behaviour are unchanged. Some test fixtures (`PlotPatch`) now stringify recorded paths to keep assertion

### [docs: convert prose .rst files to MyST .md](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/383) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** None — internal docs only.

### [feat: check workspace version on import](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/380) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** None to autogalaxy's public API. Importing `autogalaxy` now triggers a workspace-version check via `autoconf.workspace.check_version`, which may emit a warning (no version source found) or raise `autoconf.workspace.WorkspaceVersionMismatchError` (workspace and library versions disagree). Users on `m

### [docs: deprioritise numba in installation pages](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/379) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** None — docs-only.

### [refactor: replace os.path with pathlib](https://github.com/PyAutoLabs/PyAutoLens/pull/497) (PyAutoLabs/PyAutoLens)
**API Changes:** None — internal changes only. All public function signatures unchanged. Implementation switches from string-style joins to Path objects, but returned values, accepted argument types, and external behaviour are unchanged. Some test fixtures (`PlotPatch`) now stringify recorded paths to keep assertion

### [Add VisualizerInterferometer combined plotter for datacube fits](https://github.com/PyAutoLabs/PyAutoLens/pull/494) (PyAutoLabs/PyAutoLens)
**API Changes:** <details>
<summary>API Changes</summary>

### Added
- `autolens.interferometer.plot.fit_interferometer_plots.subplot_fit_interferometer_combined(fit_list, output_path=None, output_format=None, colormap=None, title_prefix=None)` — writes `fit_combined.png` for a list of `FitInterferometer` objects.
-

### [Fix mapper-index lookup in source_plane_inversion_centre_from](https://github.com/PyAutoLabs/PyAutoLens/pull/491) (PyAutoLabs/PyAutoLens)
**API Changes:** None — internal changes only.
See full details below.

### [fix: synthetic PositionsLH under skip_checks + test_mode](https://github.com/PyAutoLabs/PyAutoLens/pull/490) (PyAutoLabs/PyAutoLens)
**API Changes:** `autolens.analysis.result.Result.positions_likelihood_from` no longer returns `None` under the combination `PYAUTO_SKIP_CHECKS=1 + PYAUTO_TEST_MODE>0` — it now returns a synthetic `PositionsLH` with `positions=[(1.0, 0.0), (-1.0, 0.0)]` and `threshold=minimum_threshold or 0.5`. Behaviour is unchange

### [docs: convert prose .rst files to MyST .md](https://github.com/PyAutoLabs/PyAutoLens/pull/487) (PyAutoLabs/PyAutoLens)
**API Changes:** None — internal docs only.

### [Fix graphical_models.py auto-sim to call simulators_sample.py](https://github.com/PyAutoLabs/autofit_workspace/pull/50) (PyAutoLabs/autofit_workspace)
**Scripts Changed:** - `scripts/features/graphical_models.py` — auto-sim block

### [feat: embed workspace_version in config + drop welcome.py duplicate check](https://github.com/PyAutoLabs/autofit_workspace/pull/48) (PyAutoLabs/autofit_workspace)
**Scripts Changed:** - `config/general.yaml` — add a `version:` block with `workspace_version: 2026.4.13.6` and `workspace_version_check: True`
- `welcome.py` — remove the redundant `from autoconf import check_version` import and the `check_version(<lib>.__version__)` call (libraries now run the check on import via PyAu

### [feat: add notebook smoke tests](https://github.com/PyAutoLabs/autofit_workspace/pull/46) (PyAutoLabs/autofit_workspace)
**Scripts Changed:** - `.github/scripts/run_smoke.py` — extended with notebook execution loop, temp-dir output (so checked-in notebooks aren't dirtied), and regen-on-failure
- `.github/workflows/smoke_tests.yml` — added PyAutoBuild checkout, `jupyter`/`nbconvert`/`ipynb-py-convert` install, and `PYTHONPATH=PyAutoBuild/a

### [fix: make welcome.py self-contained instead of loading missing dataset](https://github.com/PyAutoLabs/autofit_workspace/pull/45) (PyAutoLabs/autofit_workspace)
**Scripts Changed:** - `welcome.py` — drop `from os import path` and the `af.util.numpy_array_from_json` calls; synthesise the demo gaussian + noise inline with `numpy.random.default_rng`

### [fix: neutralize smoke-mode env vars in _quick_fit.py helper](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/60) (PyAutoLabs/autogalaxy_workspace)
**Scripts Changed:** - `scripts/guides/results/_quick_fit.py` — pop `PYAUTO_SKIP_VISUALIZATION` and `PYAUTO_SKIP_FIT_OUTPUT`, downgrade `PYAUTO_TEST_MODE>=2` to `1`, before importing `autofit`. Ensures the helper always produces a complete `output/results_folder/` (including `image/dataset.fits`) regardless of how the p

### [refactor: replace os.path with pathlib in workspace scripts](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/59) (PyAutoLabs/autogalaxy_workspace)
**Scripts Changed:** See the diff against `main` for the full list (each modified script swaps one or more `os.path.*` / `path.*` calls for the equivalent `pathlib.Path` API). No script logic or behaviour changes — purely a syntactic conversion.

### [docs: comprehensive output folder layout in modeling tutorials and use search.paths in results/start_here](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/58) (PyAutoLabs/autogalaxy_workspace)
**Scripts Changed:** - `scripts/imaging/modeling.py` — replaced `__Output Folder__` flat-bullet with full directory-tree `__Output Folder Layout__` block (galaxies-not-tracer, no source-plane)
- `scripts/interferometer/modeling.py` — same treatment, adapted for visibility/uv-plane products (dirty_images.fits)
- `scripts

### [Cluster E: fix guides/plot/start_here.py auto-simulate target](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/56) (PyAutoLabs/autogalaxy_workspace)
**Scripts Changed:** - `scripts/guides/plot/start_here.py` — change auto-simulate subprocess target from `scripts/guides/plot/simulator.py` to `scripts/imaging/simulator.py`.

### [Refactor guides/results aggregator to share quick-fit helper](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/55) (PyAutoLabs/autogalaxy_workspace)
**API Changes:** None.
**Scripts Changed:** - `scripts/guides/results/_quick_fit.py` (new) - internal helper, capped Nautilus fit, idempotent (early-exits if `output/results_folder/` already exists).
- `scripts/guides/results/start_here.py` - drops the `test_mode_was_on` conditional gate on `n_like_max`; cap is now unconditional.
- `scripts/g

### [Drop removed plot_grid kwarg; emit extra_galaxies_centres.json from simulator](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/54) (PyAutoLabs/autogalaxy_workspace)
**Scripts Changed:** - `scripts/guides/advanced/over_sampling.py` — replace removed `plot_over_sampled_grid` kwarg with `.over_sampled` direct grid input (3 sites + prose)
- `scripts/imaging/features/extra_galaxies/simulator.py` — add `extra_galaxies_centres.json` output

### [feat: embed workspace_version in config + drop welcome.py duplicate check](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/51) (PyAutoLabs/autogalaxy_workspace)
**Scripts Changed:** - `config/general.yaml` — add a `version:` block with `workspace_version: 2026.4.13.6` and `workspace_version_check: True`
- `welcome.py` — remove the redundant `from autoconf import check_version` import and the `check_version(<lib>.__version__)` call (libraries now run the check on import via PyAu

### [fix: restore missing source assignment in subhalo_refine (Cluster F)](https://github.com/PyAutoLabs/autolens_workspace/pull/133) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/group/features/advanced/subhalo/detect/start_here.py` — function `subhalo_refine`. Add a single line `source = subhalo_grid_search_result.model.galaxies.source` between the existing `subhalo.mass.redshift_object = subhalo.redshift` (line 624) and the `lens_dict = {` literal (line 626). Re

### [fix: derive point_source/fit.py positions data from solver output (Cluster E)](https://github.com/PyAutoLabs/autolens_workspace/pull/132) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/point_source/fit.py` — replace the hardcoded 4-element `positions_data` and `positions_noise_map` lists with `al.Grid2DIrregular(positions)` and `al.ArrayIrregular([0.005] * len(positions))`. Same shape of fix as PR #119's `range(len(positions))` dict comprehension. Prose updated from "we

### [fix: clamp einstein_radius prior in two more group SLaM scripts](https://github.com/PyAutoLabs/autolens_workspace/pull/131) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/group/features/linear_light_profiles/slam.py` — function `mass_total` (the second SLaM phase). Adds the `luminosity_cap` / `upper_limit` clamp prefix before `mass.einstein_radius = af.UniformPrior(...)`. PR #117 already fixed `source_lp_1` in the same file; the SLaM pipeline was crashing 

### [fix: align aggregator queries with MGE source bulge in autolens tutorials](https://github.com/PyAutoLabs/autolens_workspace/pull/130) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/guides/results/aggregator/queries.py` — Model Queries section now demos `agg.query(lens.mass.einstein_radius < 1.5)` instead of `bulge.sersic_index < 3.0`. The Logic section already uses `mass.einstein_radius` with a `& mass == al.mp.Isothermal` composite, so the two sections continue to 

### [fix: neutralize smoke-mode env vars in _quick_fit.py helper](https://github.com/PyAutoLabs/autolens_workspace/pull/129) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/guides/results/_quick_fit.py` — pop `PYAUTO_SKIP_VISUALIZATION` and `PYAUTO_SKIP_FIT_OUTPUT`, downgrade `PYAUTO_TEST_MODE>=2` to `1`, before importing `autofit`. Ensures the helper always produces a complete `output/results_folder/` (including `image/dataset.fits`) regardless of how the p

### [refactor: replace os.path with pathlib in workspace scripts](https://github.com/PyAutoLabs/autolens_workspace/pull/128) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** See the diff against `main` for the full list (each modified script swaps one or more `os.path.*` / `path.*` calls for the equivalent `pathlib.Path` API). No script logic or behaviour changes — purely a syntactic conversion.

### [docs: realistic position, time-delay, and flux noise in point source simulators](https://github.com/PyAutoLabs/autolens_workspace/pull/127) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/point_source/simulator.py` — canonical simulator: full position/flux/time-delay docstring rewrites with literature citations (CASTLES, TDCOSMO, COSMOGRAIL)
- `scripts/point_source/simulator_sample.py` — sample-mode variant with the same constants and condensed docstrings referring back to

### [docs: comprehensive output folder layout in modeling tutorials and use search.paths in results/start_here](https://github.com/PyAutoLabs/autolens_workspace/pull/126) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/imaging/modeling.py` — replaced `__Output Folder__` flat-bullet with full directory-tree `__Output Folder Layout__` block (imaging-specific products: dataset.fits with PSF, fit.fits, tracer.fits, source_plane_images.fits)
- `scripts/interferometer/modeling.py` — same treatment, adapted fo

### [Add Delaunay datacube modeling + RectangularAdaptDensity + PositionsLH](https://github.com/PyAutoLabs/autolens_workspace/pull/123) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/interferometer/features/datacube/simulator.py` — add `PointSolver` block to compute and write `positions.json`. New `__Multiple Images__` section in the `__Contents__` TOC.
- `scripts/interferometer/features/datacube/start_here.py` — mesh swap + new `__Positions__` section, load positions
