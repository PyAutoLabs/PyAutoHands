# Release Readiness Report

**Status: NOT READY**

**Run:** `2026-05-04T11-18-14Z`  •  **Path:** `/home/jammy/Code/PyAutoLabs/PyAutoBuild/test_results/runs/2026-05-04T11-18-14Z`  •  **Total duration:** 9618.1s

## Slow-Skipped Scripts (needs performance fix)

**7 script(s)** are being skipped because they exceed the 60s per-script timeout cap. These are NOT permanent skips — they need the underlying performance issue fixed and the `SLOW` marker removed from the workspace's `config/build/no_run.yaml`.

| Workspace | Script | Marked | Age | Reason |
|-----------|--------|--------|-----|--------|
| autogalaxy_workspace | `guides/results/database/start_here` | 2026-04-10 | 24d | previously failed fast on a broken aggregator query; now runs the real aggregator and exceeds 60s |
| autogalaxy_workspace | `guides/results/workflow/csv_make` | 2026-04-10 | 24d | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| autolens_workspace | `guides/results/database/start_here` | 2026-04-10 | 24d | previously failed fast on a broken aggregator query; now runs the real aggregator and exceeds 60s |
| autolens_workspace_test | `database/scrape/multi_analysis` | 2026-04-10 | 24d | exceeds 60s timeout; _test workspaces run full searches without test mode |
| autolens_workspace_test | `database/scrape/slam_general` | 2026-04-10 | 24d | exceeds 60s timeout; _test workspaces run full searches without test mode |
| autolens_workspace_test | `database/scrape/slam_multi_one_by_one` | 2026-04-10 | 24d | exceeds 60s timeout; _test workspaces run full searches without test mode |
| autolens_workspace_test | `database/scrape/slam_pix` | 2026-04-10 | 24d | exceeds 60s timeout; _test workspaces run full searches without test mode |

## Needs-Fix Scripts (parked for investigation)

**22 script(s)** are being skipped because they are broken and parked as a to-do list. These are NOT permanent skips — investigate the failure, fix the underlying bug, and remove the `NEEDS_FIX` marker from the workspace's `config/build/no_run.yaml`.

| Workspace | Script | Marked | Age | Reason |
|-----------|--------|--------|-----|--------|
| autofit_workspace | `features/interpolate` | 2026-04-10 | 24d | IndexError in InstanceInterpolator.__getitem__ when querying time == 1.5; value_map lookup falls through to empty instances list |
| autogalaxy_workspace | `autogalaxy_workspace/scripts/imaging/modeling` | 2026-04-10 | 24d | KeyError on ('galaxies','galaxy','bulge','ell_comps'...) kwargs after API drift in top-level imaging/modeling.py |
| autogalaxy_workspace | `ellipse/database` | 2026-04-24 | 10d | all ellipse examples parked pending JAX refactor; see PyAutoPrompt/autogalaxy/ellipse_no_run.md |
| autogalaxy_workspace | `ellipse/fit` | 2026-04-24 | 10d | all ellipse examples parked pending JAX refactor; see PyAutoPrompt/autogalaxy/ellipse_no_run.md |
| autogalaxy_workspace | `ellipse/modeling` | 2026-04-24 | 10d | all ellipse examples parked pending JAX refactor; see PyAutoPrompt/autogalaxy/ellipse_no_run.md |
| autogalaxy_workspace | `ellipse/multipoles` | 2026-04-24 | 10d | all ellipse examples parked pending JAX refactor; see PyAutoPrompt/autogalaxy/ellipse_no_run.md |
| autogalaxy_workspace | `ellipse/simulator` | 2026-04-24 | 10d | all ellipse examples parked pending JAX refactor; see PyAutoPrompt/autogalaxy/ellipse_no_run.md |
| autogalaxy_workspace | `imaging/data_preparation/manual/mask_irregular` | 2026-04-10 | 24d | silent failure, needs investigation |
| autogalaxy_workspace | `imaging/features/pixelization/modeling` | 2026-04-10 | 24d | LinAlgError: matrix not positive definite in pixelization modeling |
| autogalaxy_workspace | `interferometer/features/pixelization/modeling` | 2026-04-10 | 24d | LinAlgError: matrix not positive definite in interferometer pixelization modeling |
| autolens_workspace | `group/slam` | 2026-04-10 | 24d | PriorException: upper limit must be greater than lower limit in group SLaM pipeline |
| autolens_workspace | `imaging/data_preparation/manual/mask_irregular` | 2026-04-10 | 24d | silent failure, needs investigation |
| autolens_workspace | `imaging/features/pixelization/delaunay` | 2026-04-10 | 24d | autofit.exc.FitException in Delaunay pixelization fit |
| autolens_workspace | `imaging/features/pixelization/slam` | 2026-04-10 | 24d | autofit.exc.FitException in SLaM pixelization pipeline |
| autolens_workspace | `interferometer/features/pixelization/delaunay` | 2026-04-10 | 24d | broadcast shape mismatch (2,2) vs (1032,1032) in Delaunay interferometer |
| autolens_workspace | `multi/features/wavelength_dependence/modeling` | 2026-04-10 | 24d | autofit.exc.FitException in multi-wavelength modeling |
| autolens_workspace_test | `database/scrape/general` | 2026-04-27 | 7d | PyAutoGalaxy abstract_fit.linear_light_profile_intensity_dict raises "TypeError: __hash__ method should return an integer" during subplot_fit_imaging after the search completes (a light-profile object's __hash__ returns a non-int). Surfaced once the dataset_label="build" path fix let the script progress past Imaging.from_fits. |
| autolens_workspace_test | `imaging/visualization` | 2026-04-10 | 24d | AssertionError: dataset.png missing after visualization refactor |
| autolens_workspace_test | `jax_grad/imaging_lp` | 2026-04-10 | 24d | JAX traceback in gradient computation for light profile |
| autolens_workspace_test | `jax_grad/imaging_mge` | 2026-04-10 | 24d | AssertionError: Gradient is all zeros in MGE gradient computation |
| autolens_workspace_test | `jax_likelihood_functions/imaging/delaunay_mge` | 2026-04-10 | 24d | timeout in JAX likelihood function benchmark |
| autolens_workspace_test | `jax_likelihood_functions/imaging/mge_group` | 2026-04-10 | 24d | timeout in JAX likelihood function benchmark |

## Summary

| Passed | Failed | Skipped | Timeout |
|--------|--------|---------|---------|
| 395 | 12 | 65 | 3 |

## Per-Project Breakdown

| Project | Passed | Failed | Skipped | Timeout | Duration |
|---------|--------|--------|---------|---------|----------|
| autofit | 24 | 0 | 6 | 0 | 85.1s |
| autofit_test | 27 | 1 | 2 | 0 | 218.5s |
| autogalaxy | 88 | 2 | 18 | 0 | 865.1s |
| autogalaxy_test | 33 | 0 | 0 | 0 | 1682.5s |
| autolens | 166 | 9 | 28 | 0 | 3099.3s |
| autolens_test | 57 | 0 | 11 | 3 | 3667.6s |

## Slowest scripts (top 25)

| Script | Project | Status | Duration | Share |
|--------|---------|--------|----------|-------|
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/modeling_visualization_jit_rectangular.py` | autolens_test | timeout | 300.6s | 3.1% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/modeling_visualization_jit.py` | autolens_test | timeout | 300.3s | 3.1% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/modeling_visualization_jit_delaunay.py` | autolens_test | timeout | 300.2s | 3.1% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_dspl.py` | autolens_test | passed | 289.4s | 3.0% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/multi/mge_group.py` | autolens_test | passed | 218.8s | 2.3% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/units/flux.py` | autolens | passed | 181.8s | 1.9% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_mge.py` | autolens_test | passed | 177.0s | 1.8% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/multi/start_here.py` | autolens | passed | 172.3s | 1.8% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/delaunay_mge.py` | autogalaxy_test | passed | 171.6s | 1.8% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/los_halos/simulator.py` | autolens | passed | 168.1s | 1.7% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/delaunay_mge.py` | autogalaxy_test | passed | 119.7s | 1.2% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular_dspl.py` | autolens_test | passed | 118.8s | 1.2% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/point_source/image_plane.py` | autolens_test | passed | 118.3s | 1.2% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/delaunay_mge.py` | autolens_test | passed | 115.2s | 1.2% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/multi/mge_group.py` | autogalaxy_test | passed | 110.4s | 1.1% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/database/scrape/scaling_relation.py` | autolens_test | passed | 108.4s | 1.1% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/point_source/point.py` | autolens_test | passed | 106.8s | 1.1% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/multi/delaunay_mge.py` | autogalaxy_test | passed | 106.0s | 1.1% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/delaunay.py` | autolens_test | passed | 103.3s | 1.1% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/workflow/csv_make.py` | autolens | passed | 102.5s | 1.1% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/multi/rectangular_mge.py` | autolens_test | passed | 102.4s | 1.1% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/mge_group.py` | autogalaxy_test | passed | 93.2s | 1.0% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/imaging/visualization.py` | autogalaxy_test | passed | 88.6s | 0.9% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/mge.py` | autolens_test | passed | 88.0s | 0.9% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular.py` | autolens_test | passed | 88.0s | 0.9% |

## Failures by Classification

### Source Code Bugs (11)

- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/jax_assertions/fitness_dispatch.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/jax_assertions/fitness_dispatch.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
    warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/jax_assertions/fitness_dispatch.py", line 142, in <module>
    assert_fit_for_visualization_dispatches_through_jit_when_flag_set()
  File "/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/jax_assertions/fitness_dispatch.py", line 85, in assert_fit_for_visualization_dispatches_through_jit_when_flag_set
    assert analysis._jitted_fit_from is not None
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/analysis/analysis.py", line 135, in __getattr__
    raise AttributeError(f"Analysis has no attribute {item}")
AttributeError: Analysis has no attribute _jitted_fit_from
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/data_fitting.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/data_fitting.py']' returned non-zero exit status 1.
  - **Recently modified** in [Refactor guides/results aggregator to share quick-fit helper](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/55)
  - **Recently modified** in [Refactor guides/results aggregator to share quick-fit helper](https://github.com/PyAutoLabs/autolens_workspace/pull/118)
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
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/models.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/models.py']' returned non-zero exit status 1.
  - **Recently modified** in [Fix graphical_models.py auto-sim to call simulators_sample.py](https://github.com/PyAutoLabs/autofit_workspace/pull/50)
  - **Recently modified** in [Refactor guides/results aggregator to share quick-fit helper](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/55)
  - **Recently modified** in [Refactor guides/results aggregator to share quick-fit helper](https://github.com/PyAutoLabs/autolens_workspace/pull/118)
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
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/linear_light_profiles/slam.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/linear_light_profiles/slam.py']' returned non-zero exit status 1.
  - **Recently modified** in [Cluster F triage: 4 script fixes (items 2, 3, 5, 9)](https://github.com/PyAutoLabs/autolens_workspace/pull/117)
  - **Recently modified** in [fix: wire image-plane mesh grid + AdaptImages into group/features/pixelization scripts](https://github.com/PyAutoLabs/autolens_workspace/pull/116)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/linear_light_profiles/slam.py", line 950, in <module>
    mass_result = mass_total(
                  ^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/linear_light_profiles/slam.py", line 704, in mass_total
    mass.einstein_radius = af.UniformPrior(
                           ^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/mapper/prior/uniform.py", line 53, in __init__
    raise exc.PriorException(
autoconf.exc.PriorException: The upper limit of a prior must be greater than its lower limit
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/pixelization/slam.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/pixelization/slam.py']' returned non-zero exit status 1.
  - **Recently modified** in [Cluster F triage: 4 script fixes (items 2, 3, 5, 9)](https://github.com/PyAutoLabs/autolens_workspace/pull/117)
  - **Recently modified** in [fix: wire image-plane mesh grid + AdaptImages into group/features/pixelization scripts](https://github.com/PyAutoLabs/autolens_workspace/pull/116)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/pixelization/slam.py", line 741, in <module>
    source_lp_result_1 = source_lp_1(
                         ^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/pixelization/slam.py", line 234, in source_lp_1
    mass.einstein_radius = af.UniformPrior(
                           ^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/mapper/prior/uniform.py", line 53, in __init__
    raise exc.PriorException(
autoconf.exc.PriorException: The upper limit of a prior must be greater than its lower limit
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/data_fitting.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/data_fitting.py']' returned non-zero exit status 1.
  - **Recently modified** in [Refactor guides/results aggregator to share quick-fit helper](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/55)
  - **Recently modified** in [Refactor guides/results aggregator to share quick-fit helper](https://github.com/PyAutoLabs/autolens_workspace/pull/118)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
    File "/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/data_fitting.py", line 105, in <module>
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
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/models.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/models.py']' returned non-zero exit status 1.
  - **Recently modified** in [Fix graphical_models.py auto-sim to call simulators_sample.py](https://github.com/PyAutoLabs/autofit_workspace/pull/50)
  - **Recently modified** in [Refactor guides/results aggregator to share quick-fit helper](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/55)
  - **Recently modified** in [Refactor guides/results aggregator to share quick-fit helper](https://github.com/PyAutoLabs/autolens_workspace/pull/118)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
    File "/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/models.py", line 91, in <module>
    for dataset_list, tracer_list in zip(dataset_gen, tracer_gen):
                                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoGalaxy/autogalaxy/aggregator/imaging/imaging.py", line 63, in _imaging_from
    mask, header = agg_util.mask_header_from(fit=fit)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoGalaxy/autogalaxy/aggregator/agg_util.py", line 101, in mask_header_from
    header = aa.Header(header_sci_obj=fit.value(name=name)[0].header)
                                      ~~~~~~~~~~~~~~~~~~~~^^^
TypeError: 'NoneType' object is not subscriptable
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/queries.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/queries.py']' returned non-zero exit status 1.
  - **Recently modified** in [Refactor guides/results aggregator to share quick-fit helper](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/55)
  - **Recently modified** in [Refactor guides/results aggregator to share quick-fit helper](https://github.com/PyAutoLabs/autolens_workspace/pull/118)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
                            ^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/aggregator/predicate.py", line 285, in __call__
    return self.attribute_predicate.value_for_search_output(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/aggregator/predicate.py", line 35, in value_for_search_output
    value = getattr(
            ^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/mapper/prior_model/prior_model.py", line 422, in __getattr__
    self.__getattribute__(item)
AttributeError: 'Model' object has no attribute 'sersic_index'
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/samples_via_aggregator.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/samples_via_aggregator.py']' returned non-zero exit status 1.
  - **Recently modified** in [Refactor guides/results aggregator to share quick-fit helper](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/55)
  - **Recently modified** in [Refactor guides/results aggregator to share quick-fit helper](https://github.com/PyAutoLabs/autolens_workspace/pull/118)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/mapper/prior_model/abstract.py", line 328, in _with_paths
    new_value = new_value._with_paths(subtree)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/mapper/prior_model/abstract.py", line 320, in _with_paths
    new_value = getattr(self, name)
                ^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/mapper/prior_model/prior_model.py", line 422, in __getattr__
    self.__getattribute__(item)
AttributeError: 'Model' object has no attribute 'sersic_index'
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/double_einstein_ring/slam.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/double_einstein_ring/slam.py']' returned non-zero exit status 1.
  - **Recently modified** in [Cluster F triage: 4 script fixes (items 2, 3, 5, 9)](https://github.com/PyAutoLabs/autolens_workspace/pull/117)
  - **Recently modified** in [fix: wire image-plane mesh grid + AdaptImages into group/features/pixelization scripts](https://github.com/PyAutoLabs/autolens_workspace/pull/116)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
      return func(self, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/abstract_search.py", line 661, in start_resume_fit
    return self._fit_bypass_test_mode(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/abstract_search.py", line 848, in _fit_bypass_test_mode
    analysis.log_likelihood_function(instance)
  File "/home/jammy/Code/PyAutoLabs/PyAutoLens/autolens/imaging/model/analysis.py", line 84, in log_likelihood_function
    raise af.exc.FitException
autofit.exc.FitException
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/point_source/fit.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/point_source/fit.py']' returned non-zero exit status 1.
  - **Recently modified** in [Refactor guides/results aggregator to share quick-fit helper](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/55)
  - **Recently modified** in [Cluster E: fix deblending simulator + add auto-simulate snippets to 3 guides](https://github.com/PyAutoLabs/autolens_workspace/pull/119)
  - **Recently modified** in [Refactor guides/results aggregator to share quick-fit helper](https://github.com/PyAutoLabs/autolens_workspace/pull/118)
  - **Recently modified** in [fix: wire image-plane mesh grid + AdaptImages into group/features/pixelization scripts](https://github.com/PyAutoLabs/autolens_workspace/pull/116)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
    File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/abstract_ndarray.py", line 35, in wrapper
    return self.with_new_array(func(self, *args, **kwargs))
                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/abstract_ndarray.py", line 57, in wrapper
    return func(self, other.array)
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/abstract_ndarray.py", line 326, in __truediv__
    return self._array / other
           ~~~~~~~~~~~~^~~~~~~
ValueError: operands could not be broadcast together with shapes (2,) (4,)
  ```
  </details>

### Workspace Issues (1)

- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/subhalo/detect/start_here.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/subhalo/detect/start_here.py']' returned non-zero exit status 1.
  - **Recently modified** in [Cluster E: fix guides/plot/start_here.py auto-simulate target](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/56)
  - **Recently modified** in [Refactor guides/results aggregator to share quick-fit helper](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/55)
  - **Recently modified** in [Refactor guides/results aggregator to share quick-fit helper](https://github.com/PyAutoLabs/autolens_workspace/pull/118)
  - **Recently modified** in [Cluster F triage: 4 script fixes (items 2, 3, 5, 9)](https://github.com/PyAutoLabs/autolens_workspace/pull/117)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/subhalo/detect/start_here.py", line 827, in <module>
    result_with_subhalo = subhalo_refine(
                          ^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/subhalo/detect/start_here.py", line 634, in subhalo_refine
    galaxies=af.Collection(**lens_dict, source=source),
                                               ^^^^^^
NameError: name 'source' is not defined. Did you mean: 'source_lp'?
  ```
  </details>

### Timeouts (3)

- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/modeling_visualization_jit.py`
  - Timed out after 300s
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/modeling_visualization_jit_delaunay.py`
  - Timed out after 300s
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/modeling_visualization_jit_rectangular.py`
  - Timed out after 301s

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
| `visualization.py` | NEEDS_FIX 2026-04-10 - AssertionError: dataset.png missing after visualization refactor |
| `visualization_jax.py` | NEEDS_FIX 2026-04-10 - AssertionError: dataset.png missing after visualization refactor |
| `imaging_lp.py` | NEEDS_FIX 2026-04-10 - JAX traceback in gradient computation for light profile |
| `imaging_mge.py` | NEEDS_FIX 2026-04-10 - AssertionError: Gradient is all zeros in MGE gradient computation |
| `delaunay_mge.py` | NEEDS_FIX 2026-04-10 - timeout in JAX likelihood function benchmark |
| `mge_group.py` | NEEDS_FIX 2026-04-10 - timeout in JAX likelihood function benchmark |

## Changes Since Last Release

### [Add EPAnalysisFactor for cavity-message injection](https://github.com/PyAutoLabs/PyAutoFit/pull/1248) (PyAutoLabs/PyAutoFit)
**API Changes:** Added `af.EPAnalysisFactor` — an `AnalysisFactor` subclass with a `set_cavity_dist(cavity_dist)` hook that the EP optimiser invokes before every fit, attaching the cavity `MeanField` to `analysis._cavity_mean_field` so the user's `log_likelihood_function` can read per-variable cavity messages (`.mea

### [docs: convert prose .rst files to MyST .md](https://github.com/PyAutoLabs/PyAutoFit/pull/1246) (PyAutoLabs/PyAutoFit)
**API Changes:** None — internal docs only.

### [feat: check workspace version on import](https://github.com/PyAutoLabs/PyAutoFit/pull/1241) (PyAutoLabs/PyAutoFit)
**API Changes:** None to autofit's public API. Importing `autofit` now triggers a workspace-version check via `autoconf.workspace.check_version`, which may emit a warning (no version source found) or raise `autoconf.workspace.WorkspaceVersionMismatchError` (workspace and library versions disagree). Users on `main`-b

### [fix: af.ex.Analysis use_jax=True with bare af.Model fallback](https://github.com/PyAutoLabs/PyAutoFit/pull/1240) (PyAutoLabs/PyAutoFit)
**API Changes:** None — bug fix in example Analysis class. `af.ex.Analysis(use_jax=True)` now works with a bare `af.Model`; previously it silently degraded to numpy and crashed under JIT.

### [docs: update stale Python >= 3.9 claim to Python >= 3.12](https://github.com/PyAutoLabs/PyAutoFit/pull/1239) (PyAutoLabs/PyAutoFit)
**API Changes:** None — docs-only.

### [feat: implement gradient/Hessian for TruncatedNormalMessage](https://github.com/PyAutoLabs/PyAutoFit/pull/1238) (PyAutoLabs/PyAutoFit)
**API Changes:** `TruncatedNormalMessage.logpdf_gradient` and `.logpdf_gradient_hessian` now return real values instead of raising `NotImplementedError`. `TruncatedNaturalNormal` gets the same behaviour via an override that reconstructs the underlying Gaussian from its natural parameters. No public signatures change

### [Fix subplot_of_mapper crash on interferometer data_subtracted](https://github.com/PyAutoLabs/PyAutoArray/pull/297) (PyAutoLabs/PyAutoArray)
**API Changes:** None — internal change to a plot helper. `subplot_of_mapper` / `subplot_mappings` signatures unchanged; behaviour for imaging fits is byte-identical. Interferometer fits previously crashed in panel 0; they now render a dirty data-subtracted image.

See full details below.

### [docs: convert index.rst to MyST .md](https://github.com/PyAutoLabs/PyAutoArray/pull/294) (PyAutoLabs/PyAutoArray)
**API Changes:** None — internal docs only.

### [Fix sign of poisson noise in preprocess.poisson_noise_via_data_eps_from](https://github.com/PyAutoLabs/PyAutoArray/pull/290) (PyAutoLabs/PyAutoArray)
**API Changes:** Behaviour-only change to two existing functions (signatures unchanged):
- `preprocess.poisson_noise_via_data_eps_from` now returns the true Poisson noise term (`noisy − data`) instead of its negation.
- `preprocess.data_eps_with_poisson_noise_added` and `SimulatorImaging.via_image_from(..., add_pois

### [Add RectangularSplineAdapt{Density,Image} meshes for gradient-based samplers](https://github.com/PyAutoLabs/PyAutoArray/pull/289) (PyAutoLabs/PyAutoArray)
**Scripts Changed:** None in this repo. See `autolens_workspace_developer` PR (linked after that one is opened) for two new benchmark scripts.

### [jax: gated pytree registration for AbstractNDArray + generic helper](https://github.com/PyAutoLabs/PyAutoArray/pull/288) (PyAutoLabs/PyAutoArray)
**API Changes:** Two additions in `autoarray.abstract_ndarray`:

- `AbstractNDArray.__init__` now auto-registers its concrete subclass as a JAX pytree when `xp is not np`. Pure NumPy construction is unchanged.
- New public helper `register_instance_pytree(cls, no_flatten=...)` that registers arbitrary classes via `_

### [docs: convert prose .rst files to MyST .md](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/383) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** None — internal docs only.

### [feat: check workspace version on import](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/380) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** None to autogalaxy's public API. Importing `autogalaxy` now triggers a workspace-version check via `autoconf.workspace.check_version`, which may emit a warning (no version source found) or raise `autoconf.workspace.WorkspaceVersionMismatchError` (workspace and library versions disagree). Users on `m

### [docs: deprioritise numba in installation pages](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/379) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** None — docs-only.

### [docs: note Python 3.12+ requirement on pip install page](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/378) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** None — docs-only change.

### [feat: register pytrees for AnalysisInterferometer](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/376) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** - New: `autogalaxy.analysis.jax_pytrees.register_galaxies_pytree()` — shared helper that registers `Galaxies` (a `list` subclass) as a JAX pytree with custom flatten/unflatten. Idempotent.
- New: `AnalysisInterferometer._register_fit_interferometer_pytrees()` — static method registering `FitInterfer

### [Fix mapper-index lookup in source_plane_inversion_centre_from](https://github.com/PyAutoLabs/PyAutoLens/pull/491) (PyAutoLabs/PyAutoLens)
**API Changes:** None — internal changes only.
See full details below.

### [fix: synthetic PositionsLH under skip_checks + test_mode](https://github.com/PyAutoLabs/PyAutoLens/pull/490) (PyAutoLabs/PyAutoLens)
**API Changes:** `autolens.analysis.result.Result.positions_likelihood_from` no longer returns `None` under the combination `PYAUTO_SKIP_CHECKS=1 + PYAUTO_TEST_MODE>0` — it now returns a synthetic `PositionsLH` with `positions=[(1.0, 0.0), (-1.0, 0.0)]` and `threshold=minimum_threshold or 0.5`. Behaviour is unchange

### [docs: convert prose .rst files to MyST .md](https://github.com/PyAutoLabs/PyAutoLens/pull/487) (PyAutoLabs/PyAutoLens)
**API Changes:** None — internal docs only.

### [feat: check workspace version on import](https://github.com/PyAutoLabs/PyAutoLens/pull/484) (PyAutoLabs/PyAutoLens)
**API Changes:** None to autolens's public API. Importing `autolens` now triggers a workspace-version check via `autoconf.workspace.check_version`, which may emit a warning (no version source found) or raise `autoconf.workspace.WorkspaceVersionMismatchError` (workspace and library versions disagree). Users on `main`

### [docs: deprioritise numba in installation pages](https://github.com/PyAutoLabs/PyAutoLens/pull/483) (PyAutoLabs/PyAutoLens)
**API Changes:** None — docs-only.

### [docs: note Python 3.12+ requirement on pip install page](https://github.com/PyAutoLabs/PyAutoLens/pull/481) (PyAutoLabs/PyAutoLens)
**API Changes:** None — docs-only change.

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

### [feat: add CI smoke tests covering scripts and notebooks](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/50) (PyAutoLabs/autogalaxy_workspace)
**Scripts Changed:** - `.github/workflows/smoke_tests.yml` *(new)* — modeled on `autogalaxy_workspace_test`'s workflow; checks out PyAutoConf/Fit/Array/Galaxy + PyAutoBuild, installs jupyter + nbconvert + ipynb-py-convert
- `.github/scripts/run_smoke.py` *(new)* — runs scripts from `smoke_tests.txt` and notebooks from `

### [fix: replace removed aplt.LightProfile plotter in welcome.py](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/49) (PyAutoLabs/autogalaxy_workspace)
**Scripts Changed:** - `welcome.py` — replaced `aplt.LightProfile(...)` + `figures_2d(image=True)` with `aplt.plot_array(array=sersic_light_profile.image_2d_from(grid=grid), title="Image")`

### [Cluster E: fix deblending simulator + add auto-simulate snippets to 3 guides](https://github.com/PyAutoLabs/autolens_workspace/pull/119) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/point_source/features/deblending/simulator.py` — build `point_image_{i}` kwargs from `len(positions)` instead of hardcoding `[0..3]`. The `PointSolver` returns only 2 fixed positions under `PYAUTO_SMALL_DATASETS=1` (smoke-test short-circuit at `PyAutoLens/autolens/point/solver/point_solve

### [Refactor guides/results aggregator to share quick-fit helper](https://github.com/PyAutoLabs/autolens_workspace/pull/118) (PyAutoLabs/autolens_workspace)
**API Changes:** None.
**Scripts Changed:** - `scripts/guides/results/_quick_fit.py` (new) - internal helper, capped Nautilus fit, idempotent (early-exits if `output/results_folder/` already exists).
- `scripts/guides/results/start_here.py` - drops the `test_mode_was_on` conditional gate on `n_like_max`; cap is now unconditional.
- `scripts/g

### [Cluster F triage: 4 script fixes (items 2, 3, 5, 9)](https://github.com/PyAutoLabs/autolens_workspace/pull/117) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/cluster/simulator.py` — JAX `.array` unwrap inside `@jax.jit` boundary (item 5)
- `scripts/group/features/advanced/subhalo/detect/start_here.py` — remove duplicate `"source"` key from 5 `lens_dict` literals (item 2)
- `scripts/group/features/linear_light_profiles/slam.py` — guard prior `u

### [fix: wire image-plane mesh grid + AdaptImages into group/features/pixelization scripts](https://github.com/PyAutoLabs/autolens_workspace/pull/116) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/group/features/pixelization/fit.py` — concrete fit; added `Overlay` image-mesh + `AdaptImages(galaxy_image_plane_mesh_grid_dict=...)`
- `scripts/group/features/pixelization/likelihood_function.py` — same pattern (uses `masked_dataset` variable name)
- `scripts/group/features/pixelization/

### [feat: embed workspace_version in config + drop welcome.py duplicate check](https://github.com/PyAutoLabs/autolens_workspace/pull/112) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `config/general.yaml` — append `workspace_version: 2026.4.13.6` and `workspace_version_check: True` to the existing `version:` block (keeps existing `python_version_check`)
- `welcome.py` — remove the redundant `from autoconf import check_version` import and the `check_version(al.__version__)` cal

### [feat: add CI smoke tests covering scripts and notebooks](https://github.com/PyAutoLabs/autolens_workspace/pull/111) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `.github/workflows/smoke_tests.yml` *(new)* — modeled on `autolens_workspace_test`'s workflow; checks out PyAutoConf/Fit/Array/Galaxy/Lens + PyAutoBuild, installs jupyter + nbconvert + ipynb-py-convert
- `.github/scripts/run_smoke.py` *(new)* — runs scripts from `smoke_tests.txt` and notebooks fro

### [fix: replace undefined aa.Array2D with al.Array2D in welcome.py](https://github.com/PyAutoLabs/autolens_workspace/pull/109) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `welcome.py` — `aa.Array2D` → `al.Array2D` on lines 109 and 112
