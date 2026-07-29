# Release Readiness Report

**Status: NOT READY**

**Run:** `2026-05-28T13-45-42Z`  •  **Path:** `/home/jammy/Code/PyAutoLabs/PyAutoBuild/test_results/runs/2026-05-28T13-45-42Z`  •  **Total duration:** 7908.7s

## Slow-Skipped Scripts (needs performance fix)

**22 script(s)** are being skipped because they exceed the 60s per-script timeout cap. These are NOT permanent skips — they need the underlying performance issue fixed and the `SLOW` marker removed from the workspace's `config/build/no_run.yaml`.

| Workspace | Script | Marked | Age | Reason |
|-----------|--------|--------|-----|--------|
| HowToGalaxy | `guides/results/database/start_here` | 2026-04-10 | 48d **STALE** | previously failed fast on a broken aggregator query; now runs the real aggregator and exceeds 60s |
| HowToGalaxy | `guides/results/examples/galaxies_fit` | 2026-04-10 | 48d **STALE** | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| HowToGalaxy | `guides/results/examples/models` | 2026-04-10 | 48d **STALE** | cascade from SLOW-skipped results/start_here.py; aggregator returns NoneType so instance.galaxies is None |
| HowToGalaxy | `guides/results/examples/samples` | 2026-04-10 | 48d **STALE** | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| HowToGalaxy | `guides/results/start_here` | 2026-04-10 | 48d **STALE** | exceeds 60s test timeout; unsets TEST_MODE to produce real samples for downstream examples |
| HowToGalaxy | `guides/results/workflow/csv_make` | 2026-04-10 | 48d **STALE** | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| HowToLens | `guides/results/database/start_here` | 2026-04-10 | 48d **STALE** | previously failed fast on a broken aggregator query; now runs the real aggregator and exceeds 60s |
| HowToLens | `guides/results/examples/queries` | 2026-04-10 | 48d **STALE** | cascade from SLOW-skipped results/start_here.py; stub Model lacks sersic_index attribute |
| HowToLens | `guides/results/examples/samples` | 2026-04-10 | 48d **STALE** | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| HowToLens | `guides/results/examples/samples_via_aggregator` | 2026-04-10 | 48d **STALE** | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| HowToLens | `howtolens/chapter_4_pixelizations/tutorial_10_brightness_adaption` | 2026-04-10 | 48d **STALE** | pixelization tutorial exceeds 60s test timeout |
| autogalaxy_workspace | `guides/results/database/start_here` | 2026-04-10 | 48d **STALE** | previously failed fast on a broken aggregator query; now runs the real aggregator and exceeds 60s |
| autogalaxy_workspace | `guides/results/workflow/csv_make` | 2026-04-10 | 48d **STALE** | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| autolens_workspace | `guides/results/database/start_here` | 2026-04-10 | 48d **STALE** | previously failed fast on a broken aggregator query; now runs the real aggregator and exceeds 60s |
| autolens_workspace_test | `database/scrape/multi_analysis` | 2026-04-10 | 48d **STALE** | exceeds 60s timeout; _test workspaces run full searches without test mode |
| autolens_workspace_test | `database/scrape/slam_general` | 2026-04-10 | 48d **STALE** | exceeds 60s timeout; _test workspaces run full searches without test mode |
| autolens_workspace_test | `database/scrape/slam_multi_one_by_one` | 2026-04-10 | 48d **STALE** | exceeds 60s timeout; _test workspaces run full searches without test mode |
| autolens_workspace_test | `database/scrape/slam_pix` | 2026-04-10 | 48d **STALE** | exceeds 60s timeout; _test workspaces run full searches without test mode |
| autolens_workspace_test | `imaging/modeling_visualization_jit` | 2026-05-07 | 21d | JIT + full visualization pipeline exceeds 300s cap (autogalaxy variant ~90s); unblocked by PR #70 from prior `expected jax.Array, got numpy.float64` AssertionError, now hits perf wall |
| autolens_workspace_test | `imaging/modeling_visualization_jit_delaunay` | 2026-05-07 | 21d | JIT + full visualization pipeline exceeds 300s cap; same root cause as modeling_visualization_jit |
| autolens_workspace_test | `imaging/modeling_visualization_jit_rectangular` | 2026-05-07 | 21d | JIT + full visualization pipeline exceeds 301s cap; same root cause as modeling_visualization_jit |
| autolens_workspace_test | `interferometer/modeling_visualization_jit` | 2026-05-20 | 8d | JIT + full visualization pipeline exceeds 300s cap; same root cause as imaging/modeling_visualization_jit family |

## Needs-Fix Scripts (parked for investigation)

**39 script(s)** are being skipped because they are broken and parked as a to-do list. These are NOT permanent skips — investigate the failure, fix the underlying bug, and remove the `NEEDS_FIX` marker from the workspace's `config/build/no_run.yaml`.

| Workspace | Script | Marked | Age | Reason |
|-----------|--------|--------|-----|--------|
| HowToFit | `chapter_1_introduction/tutorial_5_results_and_samples` | 2026-04-10 | 48d **STALE** | IndexError in samples access, likely related to InstanceInterpolator bug in autofit features/interpolate |
| HowToGalaxy | `autogalaxy_workspace/scripts/imaging/modeling` | 2026-04-10 | 48d **STALE** | KeyError on ('galaxies','galaxy','bulge','ell_comps'...) kwargs after API drift in top-level imaging/modeling.py |
| HowToGalaxy | `ellipse/modeling` | 2026-04-10 | 48d **STALE** | KeyError on 'ellipses.0.centre_0' kwargs after API drift in ellipse model |
| HowToGalaxy | `guides/advanced/over_sampling` | 2026-04-10 | 48d **STALE** | plot_grid() got unexpected kwarg 'plot_grid_lines' after plotter API drift |
| HowToGalaxy | `howtogalaxy/chapter_4_pixelizations/tutorial_2_mappers` | 2026-04-10 | 48d **STALE** | IndexError in mapper tutorial, likely empty mapping array |
| HowToGalaxy | `howtogalaxy/chapter_4_pixelizations/tutorial_5_model_fit` | 2026-04-10 | 48d **STALE** | LinAlgError: matrix not positive definite in pixelization fit |
| HowToGalaxy | `imaging/data_preparation/manual/mask_irregular` | 2026-04-10 | 48d **STALE** | silent failure, needs investigation |
| HowToGalaxy | `imaging/features/pixelization/modeling` | 2026-04-10 | 48d **STALE** | LinAlgError: matrix not positive definite in pixelization modeling |
| HowToGalaxy | `interferometer/features/pixelization/modeling` | 2026-04-10 | 48d **STALE** | LinAlgError: matrix not positive definite in interferometer pixelization modeling |
| HowToLens | `group/slam` | 2026-04-10 | 48d **STALE** | PriorException: upper limit must be greater than lower limit in group SLaM pipeline |
| HowToLens | `howtolens/chapter_1_introduction/tutorial_3_more_ray_tracing` | 2026-04-10 | 48d **STALE** | ValueError: Axis limits cannot be NaN or Inf in plotting |
| HowToLens | `howtolens/chapter_2_lens_modeling/tutorial_2_practicalities` | 2026-04-10 | 48d **STALE** | NameError: 'af' not defined; tutorial missing ~80 lines of imports + setup boilerplate (compare tutorial_1) |
| HowToLens | `howtolens/chapter_2_lens_modeling/tutorial_6_masking_and_positions` | 2026-04-10 | 48d **STALE** | ValueError: zero-size array reduction, empty mask after pre-computed positions load |
| HowToLens | `howtolens/chapter_4_pixelizations/tutorial_2_mappers` | 2026-04-10 | 48d **STALE** | ValueError: zero-size array reduction, empty mapper array |
| HowToLens | `imaging/data_preparation/manual/mask_irregular` | 2026-04-10 | 48d **STALE** | silent failure, needs investigation |
| HowToLens | `imaging/features/pixelization/delaunay` | 2026-04-10 | 48d **STALE** | autofit.exc.FitException in Delaunay pixelization fit |
| HowToLens | `imaging/features/pixelization/slam` | 2026-04-10 | 48d **STALE** | autofit.exc.FitException in SLaM pixelization pipeline |
| HowToLens | `interferometer/features/pixelization/delaunay` | 2026-04-10 | 48d **STALE** | broadcast shape mismatch (2,2) vs (1032,1032) in Delaunay interferometer |
| HowToLens | `multi/features/wavelength_dependence/modeling` | 2026-04-10 | 48d **STALE** | autofit.exc.FitException in multi-wavelength modeling |
| autofit_workspace | `features/interpolate` | 2026-04-10 | 48d **STALE** | IndexError in InstanceInterpolator.__getitem__ when querying time == 1.5; value_map lookup falls through to empty instances list |
| autogalaxy_workspace | `autogalaxy_workspace/scripts/imaging/modeling` | 2026-04-10 | 48d **STALE** | KeyError on ('galaxies','galaxy','bulge','ell_comps'...) kwargs after API drift in top-level imaging/modeling.py |
| autogalaxy_workspace | `imaging/data_preparation/manual/mask_irregular` | 2026-04-10 | 48d **STALE** | silent failure, needs investigation |
| autogalaxy_workspace | `imaging/features/pixelization/modeling` | 2026-04-10 | 48d **STALE** | LinAlgError: matrix not positive definite in pixelization modeling |
| autogalaxy_workspace | `interferometer/features/multi_gaussian_expansion/likelihood_function` | 2026-05-20 | 8d | LinAlgError: matrix singular in MGE inversion -> InversionException (known_numerical; same family as pixelization variants above) |
| autogalaxy_workspace | `interferometer/features/pixelization/modeling` | 2026-04-10 | 48d **STALE** | LinAlgError: matrix not positive definite in interferometer pixelization modeling |
| autolens_workspace | `group/features/advanced/double_einstein_ring/slam` | 2026-05-20 | 8d | same cascade as imaging variant — synthetic samples_summary lacks adapt_data; parking pattern of the imaging entry didn't cover this group/ twin |
| autolens_workspace | `group/slam` | 2026-04-10 | 48d **STALE** | PriorException: upper limit must be greater than lower limit in group SLaM pipeline |
| autolens_workspace | `imaging/data_preparation/manual/mask_irregular` | 2026-04-10 | 48d **STALE** | silent failure, needs investigation |
| autolens_workspace | `imaging/features/advanced/double_einstein_ring/slam` | 2026-05-07 | 21d | autofit.exc.FitException in SLaM bypass mode (same family as imaging/features/pixelization/slam — Adapt regularization needs adapt_data which the synthetic samples_summary doesn't carry; cascade goes deep, fixing in one PR isn't tractable) |
| autolens_workspace | `imaging/features/pixelization/delaunay` | 2026-04-10 | 48d **STALE** | autofit.exc.FitException in Delaunay pixelization fit |
| autolens_workspace | `imaging/features/pixelization/slam` | 2026-04-10 | 48d **STALE** | autofit.exc.FitException in SLaM pixelization pipeline |
| autolens_workspace | `interferometer/features/pixelization/delaunay` | 2026-04-10 | 48d **STALE** | broadcast shape mismatch (2,2) vs (1032,1032) in Delaunay interferometer |
| autolens_workspace | `multi/features/wavelength_dependence/modeling` | 2026-04-10 | 48d **STALE** | autofit.exc.FitException in multi-wavelength modeling |
| autolens_workspace_test | `database/scrape/general` | 2026-04-27 | 31d **STALE** | PyAutoGalaxy abstract_fit.linear_light_profile_intensity_dict raises "TypeError: __hash__ method should return an integer" during subplot_fit_imaging after the search completes (a light-profile object's __hash__ returns a non-int). Surfaced once the dataset_label="build" path fix let the script progress past Imaging.from_fits. |
| autolens_workspace_test | `imaging/visualization` | 2026-04-10 | 48d **STALE** | AssertionError: dataset.png missing after visualization refactor |
| autolens_workspace_test | `jax_grad/imaging_lp` | 2026-04-10 | 48d **STALE** | JAX traceback in gradient computation for light profile |
| autolens_workspace_test | `jax_grad/imaging_mge` | 2026-04-10 | 48d **STALE** | AssertionError: Gradient is all zeros in MGE gradient computation |
| autolens_workspace_test | `jax_likelihood_functions/imaging/delaunay_mge` | 2026-04-10 | 48d **STALE** | timeout in JAX likelihood function benchmark |
| autolens_workspace_test | `jax_likelihood_functions/imaging/mge_group` | 2026-04-10 | 48d **STALE** | timeout in JAX likelihood function benchmark |

## Summary

| Passed | Failed | Skipped | Timeout |
|--------|--------|---------|---------|
| 526 | 81 | 71 | 2 |

## Per-Project Breakdown

| Project | Passed | Failed | Skipped | Timeout | Duration |
|---------|--------|--------|---------|---------|----------|
| autofit | 24 | 1 | 6 | 0 | 149.3s |
| autofit_test | 31 | 1 | 2 | 0 | 210.6s |
| autogalaxy | 105 | 3 | 14 | 0 | 962.1s |
| autogalaxy_test | 33 | 20 | 0 | 0 | 1110.0s |
| autolens | 213 | 8 | 30 | 2 | 3286.4s |
| autolens_test | 63 | 25 | 15 | 0 | 1510.4s |
| euclid | 5 | 0 | 0 | 0 | 253.8s |
| howtofit | 14 | 1 | 1 | 0 | 102.7s |
| howtogalaxy | 12 | 11 | 1 | 0 | 97.3s |
| howtolens | 26 | 11 | 2 | 0 | 226.1s |

## Slowest scripts (top 25)

| Script | Project | Status | Duration | Share |
|--------|---------|--------|----------|-------|
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/los_halos/simulator.py` | autolens | timeout | 300.2s | 3.8% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/los_halos/simulator_jax.py` | autolens | timeout | 300.1s | 3.8% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/point_source/modeling_visualization_jit.py` | autolens_test | passed | 136.3s | 1.7% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/database/scrape/scaling_relation.py` | autolens_test | passed | 94.0s | 1.2% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/multi/start_here.py` | autolens | passed | 86.8s | 1.1% |
| `/home/jammy/Code/PyAutoLabs/euclid_strong_lens_modeling_pipeline/scripts/lens_model_waveband.py` | euclid | passed | 81.3s | 1.0% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/multi/delaunay_mge.py` | autogalaxy_test | passed | 76.8s | 1.0% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/visualization_jax.py` | autolens_test | passed | 74.2s | 0.9% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/start_here.py` | autolens | passed | 67.8s | 0.9% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/multi/mge_group.py` | autolens_test | passed | 66.6s | 0.8% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/advanced/graphical.py` | autolens | passed | 64.4s | 0.8% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/profiles/light_and_mass_profiles.py` | autolens | passed | 62.1s | 0.8% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/latent_variables.py` | autolens | passed | 61.4s | 0.8% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/multi/mge_group.py` | autogalaxy_test | passed | 55.9s | 0.7% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/imaging/modeling_visualization_jit.py` | autogalaxy_test | passed | 54.4s | 0.7% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/units/flux.py` | autolens | passed | 53.7s | 0.7% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/interferometer/modeling_visualization_jit.py` | autogalaxy_test | passed | 53.5s | 0.7% |
| `/home/jammy/Code/PyAutoLabs/euclid_strong_lens_modeling_pipeline/scripts/mge_lens_only.py` | euclid | passed | 53.1s | 0.7% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/imaging/visualization.py` | autogalaxy_test | passed | 53.0s | 0.7% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/visualization.py` | autolens_test | passed | 50.1s | 0.6% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/datacube/delaunay.py` | autolens_test | failed | 50.0s | 0.6% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/start_here.py` | autolens | passed | 48.1s | 0.6% |
| `/home/jammy/Code/PyAutoLabs/euclid_strong_lens_modeling_pipeline/scripts/sersic_lens_model.py` | euclid | passed | 48.0s | 0.6% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/delaunay_mge.py` | autogalaxy_test | failed | 47.3s | 0.6% |
| `/home/jammy/Code/PyAutoLabs/euclid_strong_lens_modeling_pipeline/scripts/full_model.py` | euclid | passed | 43.9s | 0.6% |

## Failures by Classification

### Source Code Bugs (61)

- `/home/jammy/Code/PyAutoLabs/autofit_workspace/scripts/overview/overview_1_the_basics.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autofit_workspace/scripts/overview/overview_1_the_basics.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/abstract_search.py", line 670, in start_resume_fit
    return self._fit_bypass_test_mode(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/abstract_search.py", line 857, in _fit_bypass_test_mode
    analysis.log_likelihood_function(instance)
  File "/home/jammy/Code/PyAutoLabs/autofit_workspace/scripts/overview/overview_1_the_basics.py", line 813, in log_likelihood_function
    [profile_1d.model_data_from(xvalues=xvalues) for profile_1d in instance]
     ^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'str' object has no attribute 'model_data_from'
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/jax_assertions/fitness_dispatch.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/jax_assertions/fitness_dispatch.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
    warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/jax_assertions/fitness_dispatch.py", line 159, in <module>
    assert_fit_for_visualization_dispatches_through_jit_when_flag_set()
  File "/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/jax_assertions/fitness_dispatch.py", line 85, in assert_fit_for_visualization_dispatches_through_jit_when_flag_set
    assert analysis._jitted_fit_from is not None
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/analysis/analysis.py", line 112, in __getattr__
    raise AttributeError(f"Analysis has no attribute {item}")
AttributeError: Analysis has no attribute _jitted_fit_from
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/start_here.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/start_here.py']' returned non-zero exit status 1.
  - **Recently modified** in [docs: __JAX__ in autogalaxy deferred (multi + guides mirror)](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/103)
  - **Recently modified** in [docs: __JAX__ sections in per-dataset scripts (imaging + interferometer)](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/101)
  - **Recently modified** in [docs: add __JAX__ section to top-level start_here.py](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/99)
  - **Recently modified** in [docs: __JAX__ in deferred datasets (multi + group + cluster) + cluster simulator migration](https://github.com/PyAutoLabs/autolens_workspace/pull/207)
  - **Recently modified** in [docs: __JAX__ sections in per-dataset scripts (imaging + interferometer + point_source)](https://github.com/PyAutoLabs/autolens_workspace/pull/203)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
      self.check_log_likelihood(fitness=self)
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/fitness.py", line 577, in check_log_likelihood
    raise exc.SearchException(
autofit.exc.SearchException: 
                Figure of merit sanity check failed. 

                This means that the existing results of a model fit used a different
                likelihood function compared to the one implemented now.
                Old Figure of Merit = -2516.7226211568395
                New Figure of Merit = -2494.699842478584
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/galaxies_fit.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/galaxies_fit.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
      self.check_log_likelihood(fitness=self)
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/fitness.py", line 577, in check_log_likelihood
    raise exc.SearchException(
autofit.exc.SearchException: 
                Figure of merit sanity check failed. 

                This means that the existing results of a model fit used a different
                likelihood function compared to the one implemented now.
                Old Figure of Merit = -2516.7226211568395
                New Figure of Merit = -2494.699842478584
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/samples.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/samples.py']' returned non-zero exit status 1.
  - **Recently modified** in [docs: raw-flux latent guide + workspace config updates](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/108)
  - **Recently modified** in [docs: workspace tutorial for latent variables in autogalaxy_workspace](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/97)
  - **Recently modified** in [docs: raw-flux latent guides + workspace config updates](https://github.com/PyAutoLabs/autolens_workspace/pull/214)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
      self.check_log_likelihood(fitness=self)
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/fitness.py", line 577, in check_log_likelihood
    raise exc.SearchException(
autofit.exc.SearchException: 
                Figure of merit sanity check failed. 

                This means that the existing results of a model fit used a different
                likelihood function compared to the one implemented now.
                Old Figure of Merit = -2516.7226211568395
                New Figure of Merit = -2494.699842478584
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/ellipse/modeling_visualization_jit.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/ellipse/modeling_visualization_jit.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  
You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/mask/mask_2d_util.py:564: UserWarning: Mask padded from (15, 15) to (np.int64(29), np.int64(29)) (parity preserved) to support kernel footprint (21, 21).
  warnings.warn(
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/ellipse/modeling_visualization_jit.py", line 107, in <module>
    assert isinstance(
           ^^^^^^^^^^^
AssertionError: expected jax.Array, got <class 'numpy.float64'>
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/ellipse/visualization_jax.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/ellipse/visualization_jax.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  
You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/mask/mask_2d_util.py:564: UserWarning: Mask padded from (15, 15) to (np.int64(29), np.int64(29)) (parity preserved) to support kernel footprint (21, 21).
  warnings.warn(
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/ellipse/visualization_jax.py", line 128, in <module>
    assert (
           ^
AssertionError: fit_ellipse.png was not produced by the JAX-backed visualizer
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/ellipse/fit.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/ellipse/fit.py']' returned non-zero exit status 1.
  - **Recently modified** in [docs(cookbooks/analysis): __Live Quick-Update Visualization__ section](https://github.com/PyAutoLabs/autofit_workspace/pull/62)
  - **Recently modified** in [feat: add af.NSS section to searches/nest.py tutorial (Phase 5)](https://github.com/PyAutoLabs/autofit_workspace/pull/60)
  - **Recently modified** in [docs: raw-flux latent guide + workspace config updates](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/108)
  - **Recently modified** in [interferometer: switch to TransformerNUFFT + apply_sparse_operator, reduce MGE to 5 Gaussians](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/106)
  - **Recently modified** in [docs: __JAX__ sections in per-dataset scripts (imaging + interferometer)](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/101)
  - **Recently modified** in [docs: workspace tutorial for latent variables in autogalaxy_workspace](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/97)
  - **Recently modified** in [docs: raw-flux latent guides + workspace config updates](https://github.com/PyAutoLabs/autolens_workspace/pull/214)
  - **Recently modified** in [docs: simplify weak/fit.py to load dataset via al.from_json](https://github.com/PyAutoLabs/autolens_workspace/pull/212)
  - **Recently modified** in [docs: remove Array2D.native jit-blocked caveats from JAX variant blocks](https://github.com/PyAutoLabs/autolens_workspace/pull/208)
  - **Recently modified** in [docs: __JAX__ in deferred datasets (multi + group + cluster) + cluster simulator migration](https://github.com/PyAutoLabs/autolens_workspace/pull/207)
  - **Recently modified** in [docs: __JAX__ sections in per-dataset scripts (imaging + interferometer + point_source)](https://github.com/PyAutoLabs/autolens_workspace/pull/203)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/ellipse/fit.py", line 138, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisEllipse.fit_from of <autogalaxy.ellipse.model.analysis.AnalysisEllipse object at 0x7fc18ea84410>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/ellipse/multipoles.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/ellipse/multipoles.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/ellipse/multipoles.py", line 150, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisEllipse.fit_from of <autogalaxy.ellipse.model.analysis.AnalysisEllipse object at 0x7f6249efcec0>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/ellipse/multipoles_scaled.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/ellipse/multipoles_scaled.py']' returned non-zero exit status 1
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/ellipse/multipoles_scaled.py", line 152, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisEllipse.fit_from of <autogalaxy.ellipse.model.analysis.AnalysisEllipse object at 0x7f3929d87890>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/delaunay.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/delaunay.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/delaunay.py", line 175, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisImaging.fit_from of <autogalaxy.imaging.model.analysis.AnalysisImaging object at 0x7f033c2a4bc0>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/delaunay_mge.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/delaunay_mge.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  /home/jammy/venv/PyAuto/lib/python3.12/site-packages/google/protobuf/runtime_version.py:98: UserWarning: Protobuf gencode version 5.28.3 is exactly one major version older than the runtime version 6.31.1 at tensorflow/core/protobuf/debug.proto. Please update the gencode to avoid compatibility violations in the next runtime release.
  warnings.warn(
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/delaunay_mge.py", line 192, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisImaging.fit_from of <autogalaxy.imaging.model.analysis.AnalysisImaging object at 0x7fd45acccbf0>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/lp.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/lp.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/lp.py", line 117, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisImaging.fit_from of <autogalaxy.imaging.model.analysis.AnalysisImaging object at 0x7f77e14450d0>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/mge.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/mge.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/mge.py", line 130, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisImaging.fit_from of <autogalaxy.imaging.model.analysis.AnalysisImaging object at 0x7f2e777fb950>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/mge_group.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/mge_group.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/mge_group.py", line 192, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisImaging.fit_from of <autogalaxy.imaging.model.analysis.AnalysisImaging object at 0x7fb20078ec60>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular.py", line 158, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisImaging.fit_from of <autogalaxy.imaging.model.analysis.AnalysisImaging object at 0x7f06bf6333e0>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_mge.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_mge.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_mge.py", line 169, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisImaging.fit_from of <autogalaxy.imaging.model.analysis.AnalysisImaging object at 0x7fa1993110d0>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/delaunay.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/delaunay.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/delaunay.py", line 182, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisInterferometer.fit_from of <autogalaxy.interferometer.model.analysis.AnalysisInterferometer object at 0x7f842028e090>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/delaunay_mge.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/delaunay_mge.py']' returned non-zero exit status
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  /home/jammy/venv/PyAuto/lib/python3.12/site-packages/google/protobuf/runtime_version.py:98: UserWarning: Protobuf gencode version 5.28.3 is exactly one major version older than the runtime version 6.31.1 at tensorflow/core/protobuf/debug.proto. Please update the gencode to avoid compatibility violations in the next runtime release.
  warnings.warn(
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/delaunay_mge.py", line 192, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisInterferometer.fit_from of <autogalaxy.interferometer.model.analysis.AnalysisInterferometer object at 0x7f82f086f4a0>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/lp.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/lp.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/lp.py", line 122, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisInterferometer.fit_from of <autogalaxy.interferometer.model.analysis.AnalysisInterferometer object at 0x7f4b5832de80>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/mge.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/mge.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/mge.py", line 128, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisInterferometer.fit_from of <autogalaxy.interferometer.model.analysis.AnalysisInterferometer object at 0x7fea3c264a10>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/mge_group.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/mge_group.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/mge_group.py", line 193, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisInterferometer.fit_from of <autogalaxy.interferometer.model.analysis.AnalysisInterferometer object at 0x7f45a0acc9b0>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular.py']' returned non-zero exit status 
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular.py", line 155, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisInterferometer.fit_from of <autogalaxy.interferometer.model.analysis.AnalysisInterferometer object at 0x7feaee6be720>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular_mge.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular_mge.py']' returned non-zero exit sta
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular_mge.py", line 164, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisInterferometer.fit_from of <autogalaxy.interferometer.model.analysis.AnalysisInterferometer object at 0x7effa96f43b0>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/light_multipole/multipole.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/light_multipole/multipole.py']' returned non-zero exit status 1
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/light_multipole/multipole.py", line 132, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisImaging.fit_from of <autogalaxy.imaging.model.analysis.AnalysisImaging object at 0x7ff071f3f3e0>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/cluster/simulator.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/cluster/simulator.py']' returned non-zero exit status 1.
  - **Recently modified** in [docs: remove Array2D.native jit-blocked caveats from JAX variant blocks](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/104)
  - **Recently modified** in [docs: __JAX__ sections in per-dataset scripts (imaging + interferometer)](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/101)
  - **Recently modified** in [docs: add __JAX__ section to top-level start_here.py](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/99)
  - **Recently modified** in [docs: remove Array2D.native jit-blocked caveats from JAX variant blocks](https://github.com/PyAutoLabs/autolens_workspace/pull/208)
  - **Recently modified** in [docs: __JAX__ in deferred datasets (multi + group + cluster) + cluster simulator migration](https://github.com/PyAutoLabs/autolens_workspace/pull/207)
  - **Recently modified** in [docs: __JAX__ sections in per-dataset scripts (imaging + interferometer + point_source)](https://github.com/PyAutoLabs/autolens_workspace/pull/203)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
      result = func(obj, grid, xp, *args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoGalaxy/autogalaxy/profiles/mass/abstract/mge.py", line 509, in potential_2d_via_mge_from
    amps, sigmas = self.decompose_convergence_via_mge(
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoGalaxy/autogalaxy/profiles/mass/abstract/mge.py", line 274, in decompose_convergence_via_mge
    self.mass_profile.convergence_func(
  File "/home/jammy/Code/PyAutoLabs/PyAutoGalaxy/autogalaxy/profiles/mass/abstract/abstract.py", line 174, in convergence_func
    raise NotImplementedError
NotImplementedError
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/cluster/start_here.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/cluster/start_here.py']' returned non-zero exit status 1.
  - **Recently modified** in [docs: __JAX__ in autogalaxy deferred (multi + guides mirror)](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/103)
  - **Recently modified** in [docs: __JAX__ sections in per-dataset scripts (imaging + interferometer)](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/101)
  - **Recently modified** in [docs: add __JAX__ section to top-level start_here.py](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/99)
  - **Recently modified** in [docs: __JAX__ in deferred datasets (multi + group + cluster) + cluster simulator migration](https://github.com/PyAutoLabs/autolens_workspace/pull/207)
  - **Recently modified** in [docs: __JAX__ sections in per-dataset scripts (imaging + interferometer + point_source)](https://github.com/PyAutoLabs/autolens_workspace/pull/203)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
      result = func(obj, grid, xp, *args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoGalaxy/autogalaxy/profiles/mass/abstract/mge.py", line 509, in potential_2d_via_mge_from
    amps, sigmas = self.decompose_convergence_via_mge(
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoGalaxy/autogalaxy/profiles/mass/abstract/mge.py", line 274, in decompose_convergence_via_mge
    self.mass_profile.convergence_func(
  File "/home/jammy/Code/PyAutoLabs/PyAutoGalaxy/autogalaxy/profiles/mass/abstract/abstract.py", line 174, in convergence_func
    raise NotImplementedError
NotImplementedError
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/cluster/modeling.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/cluster/modeling.py']' returned non-zero exit status 1.
  - **Recently modified** in [interferometer: switch to TransformerNUFFT + apply_sparse_operator, reduce MGE to 5 Gaussians](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/106)
  - **Recently modified** in [docs: __JAX__ in deferred datasets (multi + group + cluster) + cluster simulator migration](https://github.com/PyAutoLabs/autolens_workspace/pull/207)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
      result = func(obj, grid, xp, *args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoGalaxy/autogalaxy/profiles/mass/abstract/mge.py", line 509, in potential_2d_via_mge_from
    amps, sigmas = self.decompose_convergence_via_mge(
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoGalaxy/autogalaxy/profiles/mass/abstract/mge.py", line 274, in decompose_convergence_via_mge
    self.mass_profile.convergence_func(
  File "/home/jammy/Code/PyAutoLabs/PyAutoGalaxy/autogalaxy/profiles/mass/abstract/abstract.py", line 174, in convergence_func
    raise NotImplementedError
NotImplementedError
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/start_here.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/start_here.py']' returned non-zero exit status 1.
  - **Recently modified** in [docs: __JAX__ in autogalaxy deferred (multi + guides mirror)](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/103)
  - **Recently modified** in [docs: __JAX__ sections in per-dataset scripts (imaging + interferometer)](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/101)
  - **Recently modified** in [docs: add __JAX__ section to top-level start_here.py](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/99)
  - **Recently modified** in [docs: __JAX__ in deferred datasets (multi + group + cluster) + cluster simulator migration](https://github.com/PyAutoLabs/autolens_workspace/pull/207)
  - **Recently modified** in [docs: __JAX__ sections in per-dataset scripts (imaging + interferometer + point_source)](https://github.com/PyAutoLabs/autolens_workspace/pull/203)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
      self.check_log_likelihood(fitness=self)
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/fitness.py", line 577, in check_log_likelihood
    raise exc.SearchException(
autofit.exc.SearchException: 
                Figure of merit sanity check failed. 

                This means that the existing results of a model fit used a different
                likelihood function compared to the one implemented now.
                Old Figure of Merit = -1019.6430042720705
                New Figure of Merit = -1024.1860574458706
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/data_fitting.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/data_fitting.py']' returned non-zero exit status 1.
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
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/galaxies_fits.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/galaxies_fits.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
      self.check_log_likelihood(fitness=self)
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/fitness.py", line 577, in check_log_likelihood
    raise exc.SearchException(
autofit.exc.SearchException: 
                Figure of merit sanity check failed. 

                This means that the existing results of a model fit used a different
                likelihood function compared to the one implemented now.
                Old Figure of Merit = -1019.6430042720705
                New Figure of Merit = -1024.1860574458706
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/models.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/models.py']' returned non-zero exit status 1.
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
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/samples.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/samples.py']' returned non-zero exit status 1.
  - **Recently modified** in [docs: raw-flux latent guide + workspace config updates](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/108)
  - **Recently modified** in [docs: workspace tutorial for latent variables in autogalaxy_workspace](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/97)
  - **Recently modified** in [docs: raw-flux latent guides + workspace config updates](https://github.com/PyAutoLabs/autolens_workspace/pull/214)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
      self.check_log_likelihood(fitness=self)
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/fitness.py", line 577, in check_log_likelihood
    raise exc.SearchException(
autofit.exc.SearchException: 
                Figure of merit sanity check failed. 

                This means that the existing results of a model fit used a different
                likelihood function compared to the one implemented now.
                Old Figure of Merit = -1224.4306830405044
                New Figure of Merit = -1228.0670818130438
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/simulator.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/simulator.py']' returned non-zero exit status 1.
  - **Recently modified** in [docs: remove Array2D.native jit-blocked caveats from JAX variant blocks](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/104)
  - **Recently modified** in [docs: __JAX__ sections in per-dataset scripts (imaging + interferometer)](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/101)
  - **Recently modified** in [docs: add __JAX__ section to top-level start_here.py](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/99)
  - **Recently modified** in [docs: remove Array2D.native jit-blocked caveats from JAX variant blocks](https://github.com/PyAutoLabs/autolens_workspace/pull/208)
  - **Recently modified** in [docs: __JAX__ in deferred datasets (multi + group + cluster) + cluster simulator migration](https://github.com/PyAutoLabs/autolens_workspace/pull/207)
  - **Recently modified** in [docs: __JAX__ sections in per-dataset scripts (imaging + interferometer + point_source)](https://github.com/PyAutoLabs/autolens_workspace/pull/203)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/simulator.py", line 197, in <module>
    raw = np.asarray(jitted_solve(tracer, coord))
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <function jitted_solve at 0x7f2f54edd8a0> as an abstract array. The problematic value is of type <class 'autogalaxy.galaxy.galaxy.Galaxy'> and was passed to the function at path tracer[0][0].
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/simulator_use_jax_parity.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/simulator_use_jax_parity.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
    warnings.warn(_missing_version_warning(root, library_version))
/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/operators/convolver.py:951: UserWarning: No blurring_image provided. Only the direct image will be convolved. This may change the correctness of the PSF convolution.
  warnings.warn(
/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/operators/convolver.py:823: UserWarning: No blurring_image provided. Only the direct image will be convolved. This may change the correctness of the PSF convolution.
  warnings.warn(
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/simulator_use_jax_parity.py", line 100, in <module>
    al.util.register_tracer_classes(tracer)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: module 'autolens.util' has no attribute 'register_tracer_classes'
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/simulator_use_jax_parity.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/simulator_use_jax_parity.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  
If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/simulator_use_jax_parity.py", line 91, in <module>
    al.util.register_tracer_classes(tracer)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: module 'autolens.util' has no attribute 'register_tracer_classes'
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/datacube/delaunay.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/datacube/delaunay.py']' died with <Signals.SIGKILL: 9>.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  /home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:173: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autolens_workspace_test matches the installed library version (2026.5.21.1): no `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/delaunay.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/delaunay.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/delaunay.py", line 321, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisImaging.fit_from of <autolens.imaging.model.analysis.AnalysisImaging object at 0x7f62a1f99d30>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/lp.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/lp.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/lp.py", line 231, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisImaging.fit_from of <autolens.imaging.model.analysis.AnalysisImaging object at 0x7ff642ef3230>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/mge.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/mge.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/mge.py", line 264, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisImaging.fit_from of <autolens.imaging.model.analysis.AnalysisImaging object at 0x7f633bf0efc0>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular.py", line 301, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisImaging.fit_from of <autolens.imaging.model.analysis.AnalysisImaging object at 0x7fafe8720fb0>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_dspl.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_dspl.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_dspl.py", line 306, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisImaging.fit_from of <autolens.imaging.model.analysis.AnalysisImaging object at 0x7f457efd5fd0>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_mge.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_mge.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_mge.py", line 339, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisImaging.fit_from of <autolens.imaging.model.analysis.AnalysisImaging object at 0x7f0b9e7394c0>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/subhalo.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/subhalo.py']' returned non-zero exit status 1.
  - **Recently modified** in [interferometer: switch to TransformerNUFFT + apply_sparse_operator, MGE to 5 Gaussians](https://github.com/PyAutoLabs/autolens_workspace/pull/211)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/subhalo.py", line 278, in <module>
    run_scenario(
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/subhalo.py", line 264, in run_scenario
    fit = jax.jit(analysis_jit.fit_from)(instance)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisImaging.fit_from of <autolens.imaging.model.analysis.AnalysisImaging object at 0x7fee7c2bed50>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/delaunay.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/delaunay.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/delaunay.py", line 262, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisInterferometer.fit_from of <autolens.interferometer.model.analysis.AnalysisInterferometer object at 0x7fc4ced5b830>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/delaunay_mge.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/delaunay_mge.py']' returned non-zero exit status 1
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  /home/jammy/venv/PyAuto/lib/python3.12/site-packages/google/protobuf/runtime_version.py:98: UserWarning: Protobuf gencode version 5.28.3 is exactly one major version older than the runtime version 6.31.1 at tensorflow/core/protobuf/debug.proto. Please update the gencode to avoid compatibility violations in the next runtime release.
  warnings.warn(
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/delaunay_mge.py", line 280, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisInterferometer.fit_from of <autolens.interferometer.model.analysis.AnalysisInterferometer object at 0x7f27fbc37470>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/lp.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/lp.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/lp.py", line 207, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisInterferometer.fit_from of <autolens.interferometer.model.analysis.AnalysisInterferometer object at 0x7f9d72e81ee0>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/mge.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/mge.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/mge.py", line 223, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisInterferometer.fit_from of <autolens.interferometer.model.analysis.AnalysisInterferometer object at 0x7f4b8709d1f0>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/mge_group.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/mge_group.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/mge_group.py", line 152, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisInterferometer.fit_from of <autolens.interferometer.model.analysis.AnalysisInterferometer object at 0x7f96769edc70>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular.py", line 295, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisInterferometer.fit_from of <autolens.interferometer.model.analysis.AnalysisInterferometer object at 0x7f63d4d45370>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular_dspl.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular_dspl.py']' returned non-zero exit stat
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular_dspl.py", line 254, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisInterferometer.fit_from of <autolens.interferometer.model.analysis.AnalysisInterferometer object at 0x7f00942d1f40>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular_mge.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular_mge.py']' returned non-zero exit statu
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular_mge.py", line 264, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisInterferometer.fit_from of <autolens.interferometer.model.analysis.AnalysisInterferometer object at 0x7f063d6ad370>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular_sparse.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular_sparse.py']' returned non-zero exit st
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular_sparse.py", line 245, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisInterferometer.fit_from of <autolens.interferometer.model.analysis.AnalysisInterferometer object at 0x7f3950dee1e0>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/light_multipole/multipole.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/light_multipole/multipole.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/light_multipole/multipole.py", line 170, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisImaging.fit_from of <autolens.imaging.model.analysis.AnalysisImaging object at 0x7f83491df0e0>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/point_source/image_plane.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/point_source/image_plane.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/point_source/image_plane.py", line 170, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisPoint.fit_from of <autolens.point.model.analysis.AnalysisPoint object at 0x7f82e08bc500>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/point_source/point.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/point_source/point.py']' returned non-zero exit status 1.
  - **Recently modified** in [feat: add af.NSS section to searches/nest.py tutorial (Phase 5)](https://github.com/PyAutoLabs/autofit_workspace/pull/60)
  - **Recently modified** in [docs: raw-flux latent guide + workspace config updates](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/108)
  - **Recently modified** in [docs: raw-flux latent guides + workspace config updates](https://github.com/PyAutoLabs/autolens_workspace/pull/214)
  - **Recently modified** in [docs: remove Array2D.native jit-blocked caveats from JAX variant blocks](https://github.com/PyAutoLabs/autolens_workspace/pull/208)
  - **Recently modified** in [docs: __JAX__ sections in per-dataset scripts (imaging + interferometer + point_source)](https://github.com/PyAutoLabs/autolens_workspace/pull/203)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/point_source/point.py", line 273, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisPoint.fit_from of <autolens.point.model.analysis.AnalysisPoint object at 0x7fa03c173d40>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_substructure/test_batched_simulate.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_substructure/test_batched_simulate.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoLens/autolens/lens/substructure_util.py", line 168, in simulate_substructure
    image_2d = image_1d.reshape(image_shape)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/jax/_src/numpy/array_methods.py", line 316, in _reshape
    newshape = _compute_newshape(self, args[0] if len(args) == 1 else args)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/jax/_src/numpy/array_methods.py", line 481, in _compute_newshape
    raise TypeError(f"cannot reshape array of shape {arr.shape} (size {arr.size}) "
TypeError: cannot reshape array of shape (225,) (size 225) into shape (41, 41) (size 1681)
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_substructure/test_simulate_e2e.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_substructure/test_simulate_e2e.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoLens/autolens/lens/substructure_util.py", line 168, in simulate_substructure
    image_2d = image_1d.reshape(image_shape)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/jax/_src/numpy/array_methods.py", line 316, in _reshape
    newshape = _compute_newshape(self, args[0] if len(args) == 1 else args)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/jax/_src/numpy/array_methods.py", line 481, in _compute_newshape
    raise TypeError(f"cannot reshape array of shape {arr.shape} (size {arr.size}) "
TypeError: cannot reshape array of shape (225,) (size 225) into shape (51, 51) (size 2601)
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/HowToFit/scripts/chapter_1_introduction/tutorial_4_why_modeling_is_hard.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToFit/scripts/chapter_1_introduction/tutorial_4_why_modeling_is_hard.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/abstract_search.py", line 857, in _fit_bypass_test_mode
    analysis.log_likelihood_function(instance)
  File "/home/jammy/Code/PyAutoLabs/HowToFit/scripts/chapter_1_introduction/tutorial_4_why_modeling_is_hard.py", line 250, in log_likelihood_function
    model_data = self.model_data_from_instance(instance=instance)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/HowToFit/scripts/chapter_1_introduction/tutorial_4_why_modeling_is_hard.py", line 282, in model_data_from_instance
    return sum([profile.model_data_from(xvalues=xvalues) for profile in instance])
                ^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'str' object has no attribute 'model_data_from'
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_3_more_ray_tracing.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_3_more_ray_tracing.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
      ax.set_xlim(xmin, xmax)
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/matplotlib/axes/_base.py", line 3739, in set_xlim
    return self.xaxis._set_lim(left, right, emit=emit, auto=auto)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/matplotlib/axis.py", line 1236, in _set_lim
    v0 = self.axes._validate_converted_limits(v0, self.convert_units)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/matplotlib/axes/_base.py", line 3660, in _validate_converted_limits
    raise ValueError("Axis limits cannot be NaN or Inf")
ValueError: Axis limits cannot be NaN or Inf
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_2_lens_modeling/tutorial_6_masking_and_positions.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_2_lens_modeling/tutorial_6_masking_and_positions.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
    File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/dataset/imaging/dataset.py", line 128, in __init__
    state = ConvolverState(kernel=psf.kernel, mask=self.data.mask)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/operators/convolver.py", line 105, in __init__
    y_min, y_max = ys.min(), ys.max()
                   ^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/numpy/_core/_methods.py", line 48, in _amin
    return umr_minimum(a, axis, None, out, keepdims, initial, where)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: zero-size array to reduction operation minimum which has no identity
  ```
  </details>

### Workspace Issues (18)

- `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_1_introduction/tutorial_0_visualization.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_1_introduction/tutorial_0_visualization.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_1_introduction/tutorial_0_visualization.py", line 38, in <module>
    dataset_path = Path("dataset", "imaging", "simple__sersic")
                   ^^^^
NameError: name 'Path' is not defined
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_2_modeling/tutorial_3_realism_and_complexity.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_2_modeling/tutorial_3_realism_and_complexity.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  /home/jammy/venv/PyAuto/bin/python3: can't open file '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/imaging/simulator.py': [Errno 2] No such file or directory
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_2_modeling/tutorial_3_realism_and_complexity.py", line 57, in <module>
    subprocess.run(
  File "/usr/lib/python3.12/subprocess.py", line 571, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/home/jammy/venv/PyAuto/bin/python3', 'scripts/imaging/simulator.py']' returned non-zero exit status 2.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_2_modeling/tutorial_4_dealing_with_failure.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_2_modeling/tutorial_4_dealing_with_failure.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  /home/jammy/venv/PyAuto/bin/python3: can't open file '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/imaging/simulator.py': [Errno 2] No such file or directory
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_2_modeling/tutorial_4_dealing_with_failure.py", line 58, in <module>
    subprocess.run(
  File "/usr/lib/python3.12/subprocess.py", line 571, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/home/jammy/venv/PyAuto/bin/python3', 'scripts/imaging/simulator.py']' returned non-zero exit status 2.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_2_modeling/tutorial_5_linear_profiles.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_2_modeling/tutorial_5_linear_profiles.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  /home/jammy/venv/PyAuto/bin/python3: can't open file '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/imaging/simulator.py': [Errno 2] No such file or directory
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_2_modeling/tutorial_5_linear_profiles.py", line 72, in <module>
    subprocess.run(
  File "/usr/lib/python3.12/subprocess.py", line 571, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/home/jammy/venv/PyAuto/bin/python3', 'scripts/imaging/simulator.py']' returned non-zero exit status 2.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_3_search_chaining/tutorial_1_search_chaining.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_3_search_chaining/tutorial_1_search_chaining.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  /home/jammy/venv/PyAuto/bin/python3: can't open file '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/imaging/simulator.py': [Errno 2] No such file or directory
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_3_search_chaining/tutorial_1_search_chaining.py", line 78, in <module>
    subprocess.run(
  File "/usr/lib/python3.12/subprocess.py", line 571, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/home/jammy/venv/PyAuto/bin/python3', 'scripts/imaging/simulator.py']' returned non-zero exit status 2.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_3_search_chaining/tutorial_2_prior_passing.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_3_search_chaining/tutorial_2_prior_passing.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  /home/jammy/venv/PyAuto/bin/python3: can't open file '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/imaging/simulator.py': [Errno 2] No such file or directory
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_3_search_chaining/tutorial_2_prior_passing.py", line 57, in <module>
    subprocess.run(
  File "/usr/lib/python3.12/subprocess.py", line 571, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/home/jammy/venv/PyAuto/bin/python3', 'scripts/imaging/simulator.py']' returned non-zero exit status 2.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_3_search_chaining/tutorial_3_x2_galaxies.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_3_search_chaining/tutorial_3_x2_galaxies.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  /home/jammy/venv/PyAuto/bin/python3: can't open file '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/guides/plot/simulator.py': [Errno 2] No such file or directory
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_3_search_chaining/tutorial_3_x2_galaxies.py", line 60, in <module>
    subprocess.run(
  File "/usr/lib/python3.12/subprocess.py", line 571, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/home/jammy/venv/PyAuto/bin/python3', 'scripts/guides/plot/simulator.py']' returned non-zero exit status 2.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_4_pixelizations/tutorial_2_mappers.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_4_pixelizations/tutorial_2_mappers.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  /home/jammy/venv/PyAuto/bin/python3: can't open file '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/imaging/simulator.py': [Errno 2] No such file or directory
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_4_pixelizations/tutorial_2_mappers.py", line 47, in <module>
    subprocess.run(
  File "/usr/lib/python3.12/subprocess.py", line 571, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/home/jammy/venv/PyAuto/bin/python3', 'scripts/imaging/simulator.py']' returned non-zero exit status 2.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_4_pixelizations/tutorial_4_bayesian_regularization.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_4_pixelizations/tutorial_4_bayesian_regularization.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  /home/jammy/venv/PyAuto/bin/python3: can't open file '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/imaging/simulator.py': [Errno 2] No such file or directory
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_4_pixelizations/tutorial_4_bayesian_regularization.py", line 55, in <module>
    subprocess.run(
  File "/usr/lib/python3.12/subprocess.py", line 571, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/home/jammy/venv/PyAuto/bin/python3', 'scripts/imaging/simulator.py']' returned non-zero exit status 2.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_4_pixelizations/tutorial_5_model_fit.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_4_pixelizations/tutorial_5_model_fit.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  /home/jammy/venv/PyAuto/bin/python3: can't open file '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/imaging/simulator.py': [Errno 2] No such file or directory
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_4_pixelizations/tutorial_5_model_fit.py", line 61, in <module>
    subprocess.run(
  File "/usr/lib/python3.12/subprocess.py", line 571, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/home/jammy/venv/PyAuto/bin/python3', 'scripts/imaging/simulator.py']' returned non-zero exit status 2.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_0_visualization.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_0_visualization.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_0_visualization.py", line 41, in <module>
    dataset_path = Path("dataset") / "imaging" / "simple__no_lens_light"
                   ^^^^
NameError: name 'Path' is not defined
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_2_lens_modeling/tutorial_2_practicalities.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_2_lens_modeling/tutorial_2_practicalities.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_2_lens_modeling/tutorial_2_practicalities.py", line 77, in <module>
    search = af.Nautilus(
             ^^
NameError: name 'af' is not defined
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_4_pixelizations/tutorial_10_brightness_adaption.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_4_pixelizations/tutorial_10_brightness_adaption.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  /home/jammy/venv/PyAuto/bin/python3: can't open file '/home/jammy/Code/PyAutoLabs/HowToLens/scripts/imaging/features/no_lens_light/simulator.py': [Errno 2] No such file or directory
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_4_pixelizations/tutorial_10_brightness_adaption.py", line 60, in <module>
    subprocess.run(
  File "/usr/lib/python3.12/subprocess.py", line 571, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/home/jammy/venv/PyAuto/bin/python3', 'scripts/imaging/features/no_lens_light/simulator.py']' returned non-zero exit status 2.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_4_pixelizations/tutorial_11_adaptive_regularization.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_4_pixelizations/tutorial_11_adaptive_regularization.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  /home/jammy/venv/PyAuto/bin/python3: can't open file '/home/jammy/Code/PyAutoLabs/HowToLens/scripts/imaging/features/no_lens_light/simulator.py': [Errno 2] No such file or directory
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_4_pixelizations/tutorial_11_adaptive_regularization.py", line 52, in <module>
    subprocess.run(
  File "/usr/lib/python3.12/subprocess.py", line 571, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/home/jammy/venv/PyAuto/bin/python3', 'scripts/imaging/features/no_lens_light/simulator.py']' returned non-zero exit status 2.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_4_pixelizations/tutorial_2_mappers.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_4_pixelizations/tutorial_2_mappers.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  /home/jammy/venv/PyAuto/bin/python3: can't open file '/home/jammy/Code/PyAutoLabs/HowToLens/scripts/imaging/features/no_lens_light/simulator.py': [Errno 2] No such file or directory
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_4_pixelizations/tutorial_2_mappers.py", line 51, in <module>
    subprocess.run(
  File "/usr/lib/python3.12/subprocess.py", line 571, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/home/jammy/venv/PyAuto/bin/python3', 'scripts/imaging/features/no_lens_light/simulator.py']' returned non-zero exit status 2.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_4_pixelizations/tutorial_4_bayesian_regularization.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_4_pixelizations/tutorial_4_bayesian_regularization.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  /home/jammy/venv/PyAuto/bin/python3: can't open file '/home/jammy/Code/PyAutoLabs/HowToLens/scripts/imaging/features/no_lens_light/simulator.py': [Errno 2] No such file or directory
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_4_pixelizations/tutorial_4_bayesian_regularization.py", line 56, in <module>
    subprocess.run(
  File "/usr/lib/python3.12/subprocess.py", line 571, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/home/jammy/venv/PyAuto/bin/python3', 'scripts/imaging/features/no_lens_light/simulator.py']' returned non-zero exit status 2.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_4_pixelizations/tutorial_6_lens_modeling.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_4_pixelizations/tutorial_6_lens_modeling.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  /home/jammy/venv/PyAuto/bin/python3: can't open file '/home/jammy/Code/PyAutoLabs/HowToLens/scripts/imaging/features/no_lens_light/simulator.py': [Errno 2] No such file or directory
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_4_pixelizations/tutorial_6_lens_modeling.py", line 57, in <module>
    subprocess.run(
  File "/usr/lib/python3.12/subprocess.py", line 571, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/home/jammy/venv/PyAuto/bin/python3', 'scripts/imaging/features/no_lens_light/simulator.py']' returned non-zero exit status 2.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_4_pixelizations/tutorial_7_adaptive_pixelization.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_4_pixelizations/tutorial_7_adaptive_pixelization.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  /home/jammy/venv/PyAuto/bin/python3: can't open file '/home/jammy/Code/PyAutoLabs/HowToLens/scripts/imaging/features/no_lens_light/simulator.py': [Errno 2] No such file or directory
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_4_pixelizations/tutorial_7_adaptive_pixelization.py", line 52, in <module>
    subprocess.run(
  File "/usr/lib/python3.12/subprocess.py", line 571, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/home/jammy/venv/PyAuto/bin/python3', 'scripts/imaging/features/no_lens_light/simulator.py']' returned non-zero exit status 2.
  ```
  </details>

### Timeouts (2)

- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/los_halos/simulator.py`
  - Timed out after 300s
  - **Recently modified** in [docs: remove Array2D.native jit-blocked caveats from JAX variant blocks](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/104)
  - **Recently modified** in [docs: __JAX__ sections in per-dataset scripts (imaging + interferometer)](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/101)
  - **Recently modified** in [docs: add __JAX__ section to top-level start_here.py](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/99)
  - **Recently modified** in [docs: remove Array2D.native jit-blocked caveats from JAX variant blocks](https://github.com/PyAutoLabs/autolens_workspace/pull/208)
  - **Recently modified** in [docs: __JAX__ in deferred datasets (multi + group + cluster) + cluster simulator migration](https://github.com/PyAutoLabs/autolens_workspace/pull/207)
  - **Recently modified** in [docs: __JAX__ sections in per-dataset scripts (imaging + interferometer + point_source)](https://github.com/PyAutoLabs/autolens_workspace/pull/203)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/los_halos/simulator_jax.py`
  - Timed out after 300s

### Missing Data Files (2)

- `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_1_introduction/tutorial_3_fitting.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_1_introduction/tutorial_3_fitting.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
             ^^^^^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/astropy/io/fits/hdu/hdulist.py", line 1169, in _readfrom
    fileobj = _File(
              ^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/astropy/io/fits/file.py", line 218, in __init__
    self._open_filename(fileobj, mode, overwrite)
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/astropy/io/fits/file.py", line 651, in _open_filename
    self._file = open(self.name, IO_FITS_MODES[mode])
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'dataset/imaging/simple/data.fits'
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_7_fitting.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_7_fitting.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
             ^^^^^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/astropy/io/fits/hdu/hdulist.py", line 1169, in _readfrom
    fileobj = _File(
              ^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/astropy/io/fits/file.py", line 218, in __init__
    self._open_filename(fileobj, mode, overwrite)
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/astropy/io/fits/file.py", line 651, in _open_filename
    self._file = open(self.name, IO_FITS_MODES[mode])
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'dataset/imaging/simple__no_lens_light__mass_sis/data.fits'
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
| `likelihood_function.py` | NEEDS_FIX 2026-05-20 - LinAlgError: matrix singular in MGE inversion -> InversionException (known_numerical; same family as pixelization variants above) |
| `modeling.py` | NEEDS_FIX 2026-04-10 - LinAlgError: matrix not positive definite in interferometer pixelization modeling |
| `slam.py` | NEEDS_FIX 2026-05-20 - same cascade as imaging variant — synthetic samples_summary lacks adapt_data; parking pattern of the imaging entry didn't cover this group/ twin |
| `modeling.py` | Requires CSE to be JAX enabled. |
| `slam.py` | Requires CSE to be JAX enabled. |
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
| `visualization_jax.py` | NEEDS_FIX 2026-04-10 - AssertionError: dataset.png missing after visualization refactor |
| `modeling_visualization_jit.py` | SLOW 2026-05-20 - JIT + full visualization pipeline exceeds 300s cap; same root cause as imaging/modeling_visualization_jit family |
| `imaging_lp.py` | NEEDS_FIX 2026-04-10 - JAX traceback in gradient computation for light profile |
| `imaging_mge.py` | NEEDS_FIX 2026-04-10 - AssertionError: Gradient is all zeros in MGE gradient computation |
| `delaunay_mge.py` | NEEDS_FIX 2026-04-10 - timeout in JAX likelihood function benchmark |
| `mge_group.py` | NEEDS_FIX 2026-04-10 - timeout in JAX likelihood function benchmark |
| `tutorial_5_results_and_samples.py` | NEEDS_FIX 2026-04-10 - IndexError in samples access, likely related to InstanceInterpolator bug in autofit features/interpolate |
| `tutorial_searches.py` | No reason documented |
| `tutorial_5_borders.py` | Cant get right masks, need proper update. |
| `tutorial_searches.py` | No reason documented |

## Changes Since Last Release

### [Cache model.parameterization; try interactive matplotlib backends](https://github.com/PyAutoLabs/PyAutoFit/pull/1299) (PyAutoLabs/PyAutoFit)
**API Changes:** None — `parameterization` was already a `@property`, now `@functools.cached_property`. Same external interface. The live_viewer backend selection is internal.

### [Prefer fit_quick.png in quick-update display candidates](https://github.com/PyAutoLabs/PyAutoFit/pull/1298) (PyAutoLabs/PyAutoFit)
**API Changes:** None — internal constant change only.

### [Remove use_jax_for_visualization; add visualization warmup](https://github.com/PyAutoLabs/PyAutoFit/pull/1297) (PyAutoLabs/PyAutoFit)
**API Changes:** `Analysis.__init__` no longer accepts `use_jax_for_visualization`. Visualization now automatically follows `use_jax` — if the search uses JAX, visualization does too. The `_jitted_fit_from` lazy JIT cache on Analysis is removed; the warmup in `Fitness.__init__` is a better approach (pre-compiles bef

### [fix: skip _compute_latent_samples in PYAUTO_TEST_MODE (#1294)](https://github.com/PyAutoLabs/PyAutoFit/pull/1295) (PyAutoLabs/PyAutoFit)
**API Changes:** Public API: no change. Purely internal — adds `if skip_latents(): return None` at the top of the private `SearchUpdater._compute_latent_samples` method. The `PYAUTO_SKIP_LATENTS` env var is a new user-facing env knob but documented inline in `autoconf.test_mode.skip_latents()`'s docstring.

See full

### [Add live_visual_update flag for opt-in on-the-fly visualization](https://github.com/PyAutoLabs/PyAutoFit/pull/1293) (PyAutoLabs/PyAutoFit)
**API Changes:** `NonLinearSearch.__init__` gains optional `live_visual_update` kwarg (default `None`, falls back to `general.updates.live_visual_update` in config — defaults `false`). `Fitness.__init__` and `BackgroundQuickUpdate.__init__` gain the same flag. A new `LiveDisplay` helper class composes the display su

### [fix: PYAUTO_TEST_MODE should write to a separate output dir](https://github.com/PyAutoLabs/PyAutoFit/pull/1292) (PyAutoLabs/PyAutoFit)
**API Changes:** No public symbol additions, removals, or signature changes.

Behaviour change: when the `PYAUTO_TEST_MODE` environment variable is set (any truthy value), AutoFit search output paths get a `test_mode/` segment inserted directly after `conf.instance.output_path`. This affects every search-output path

### [feat(quick_update): IPython.display.update_display for live Jupyter cells](https://github.com/PyAutoLabs/PyAutoFit/pull/1290) (PyAutoLabs/PyAutoFit)
**API Changes:** One additive optional kwarg on `BackgroundQuickUpdate`: `display_id: str = "pyauto_fit_progress"`. Behavioural change: when running inside a Jupyter / Colab kernel, the worker additionally pushes the freshly-written `subplot_fit.png` to the active cell via `IPython.display.update_display`. Outside a

### [feat(analysis): LATENT_BATCH_MODE attribute (vmap default, jit option)](https://github.com/PyAutoLabs/PyAutoFit/pull/1288) (PyAutoLabs/PyAutoFit)
**API Changes:** New public class attribute `Analysis.LATENT_BATCH_MODE: str` (default `"vmap"`). Two values supported: `"vmap"` and `"jit"`. Other values raise `ValueError` at `compute_latent_samples` time with a clear message.

See full details below.

### [Fix Sample.kwargs mixed string/tuple key bug](https://github.com/PyAutoLabs/PyAutoFit/pull/1287) (PyAutoLabs/PyAutoFit)
**API Changes:** Internal in-memory representation of `Sample.kwargs` is now uniformly tuple-keyed — single-name keys become `('name',)` instead of staying as raw strings. All serialized forms (CSV headers, database JSON via `Sample.dict()`) are unchanged because they already join tuples back to dotted strings on se

### [fix: VectorYX2DIrregular from_dict round-trip (missing values property)](https://github.com/PyAutoLabs/PyAutoArray/pull/342) (PyAutoLabs/PyAutoArray)
**API Changes:** Added a new public read-only `values` property on `VectorYX2DIrregular` returning the underlying `(N, 2)` ndarray. Purely additive — no existing call sites read `vec.values`. See full details below.

### [perf: cache expensive @property on Fit classes](https://github.com/PyAutoLabs/PyAutoArray/pull/341) (PyAutoLabs/PyAutoArray)
**API Changes:** None — same properties, same return types. Now cached after first access.

### [fix: make Array2D.native jit-traceable for JAX simulator path](https://github.com/PyAutoLabs/PyAutoArray/pull/339) (PyAutoLabs/PyAutoArray)
**API Changes:** None — internal changes only. `array_2d_via_indexes_from` is a private utility; the simulator public interface is unchanged.

### [fix: raise ValueError on xp=np + jnp-backed-grid mismatch](https://github.com/PyAutoLabs/PyAutoArray/pull/337) (PyAutoLabs/PyAutoArray)
**API Changes:** - **Changed behaviour:** `AbstractMaker.__init__` now raises `ValueError` when `xp is np` and `grid.use_jax` is `True`. Pre-existing call sites are unaffected — all of PyAutoArray, PyAutoLens, PyAutoGalaxy continue to pass the tests (verified: 837 / 317 / 918 pass).

See full details below.

### [feat: SimulatorInterferometer(use_jax=True) + xp-aware preprocess Gaussian noise](https://github.com/PyAutoLabs/PyAutoArray/pull/336) (PyAutoLabs/PyAutoArray)
**API Changes:** - **Added:** `aa.SimulatorInterferometer(..., use_jax=False)` constructor flag.
- **Added:** `aa.SimulatorInterferometer._xp` property.
- **Changed signature:** `aa.SimulatorInterferometer.via_image_from(image, xp=None)` — fixed asymmetry with `SimulatorImaging` by adding the `xp` parameter. `xp=Non

### [feat: SimulatorImaging(use_jax=True) + xp-aware preprocess noise](https://github.com/PyAutoLabs/PyAutoArray/pull/335) (PyAutoLabs/PyAutoArray)
**API Changes:** - **Added:** `aa.SimulatorImaging(..., use_jax=False)` constructor flag.
- **Added:** `aa.SimulatorImaging._xp` property (returns `jnp` if `use_jax`, else `np`).
- **Changed signature:** `aa.SimulatorImaging.via_image_from(xp=None)` — defaults to `self._xp` when `None`.
- **Changed signature:** `pre

### [feat(grids): add respect_small_datasets kwarg to Grid2D.uniform](https://github.com/PyAutoLabs/PyAutoArray/pull/327) (PyAutoLabs/PyAutoArray)
**API Changes:** Adds one optional kwarg `respect_small_datasets: bool = True` to `aa.Grid2D.uniform`. No removed or renamed symbols; existing callers continue to work without change.
See full details below.

### [fix: soft-fail jax_zero_contour callers in lens_calc to NaN/[]](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/465) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** Behaviour change (no signature change): when `jax_zero_contour` is not installed, `einstein_radius_jit_from` now returns `float('nan')` (was: `ModuleNotFoundError`), and the public `tangential_critical_curve_list_via_zero_contour_from` / `radial_critical_curve_list_via_zero_contour_from` (via the pr

### [fix: raw-flux latent + soft-fail magzero-required µJy](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/463) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** - **Added** `total_galaxy_0_flux(fit, magzero=None, xp=np)` — raw integrated
  flux of galaxy 0 in the fit's image units; no instrument inputs required.
  Default-on in `autogalaxy/config/latent.yaml`.
- **Added** module-level helper `_maybe_magzero_warn(magzero, name) -> bool`
  to dedupe the new s

### [perf: cache expensive @property on Fit classes](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/462) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** None — same properties, same return types. Now cached after first access.

### [fix: elliptical MGE potential via deflection line integral](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/460) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** Changed internal implementation of `MGEDecomposer.potential_2d_via_mge_from`. Added `sigma_function` static method and `n_quad` parameter. No public API changes.

### [fix: add xp=np to convergence_func across all mass profiles](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/457) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** Added `xp=np` keyword to 5 `convergence_func` signatures. Default is `np` so existing callers are unaffected.

### [feat: vmapped_deflections_from for batched subhalo deflections](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/455) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** New methods on `MassProfile`:
- `MassProfile.vmapped_deflections_from(grid, params_batch, mask, xp=None)` — classmethod
- `MassProfile.radial_deflection_from(r, params, xp)` — static method (default raises `NotImplementedError`)

New static methods:
- `NFWTruncatedSph.radial_deflection_from(r, param

### [fix: cNFWSph deflection boundary bug and MCR validation (#451)](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/454) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** None — internal bug fix. The warning for invalid f_c is new user-visible behaviour.

### [docs: LaTeX docstrings for all mass profile classes](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/453) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** None — documentation only. No code logic changed.

### [fix: effective_einstein_radius falls back to NumPy when jax_zero_contour missing](https://github.com/PyAutoLabs/PyAutoLens/pull/558) (PyAutoLabs/PyAutoLens)
**API Changes:** Behaviour change (no signature change): on the JAX path (`xp is not np`), `effective_einstein_radius` now detects whether `jax_zero_contour` is importable. If yes — unchanged JIT path. If no — falls through to the existing NumPy `einstein_radius_from(grid)` branch with a one-time-per-process warning

### [fix: raw-flux latents + soft-fail magzero-required µJy](https://github.com/PyAutoLabs/PyAutoLens/pull/557) (PyAutoLabs/PyAutoLens)
**API Changes:** - **Added** three raw-flux latents (`total_lens_flux`, `total_lensed_source_flux`,
  `total_source_flux`), default-on. Same image-source and exception-handling
  contract as their `_mujy` siblings — they just skip the AB-mag → µJy step.
- **Added** module-level helper `_maybe_magzero_warn(magzero, n

### [test: lock down WeakDataset json round-trip (paired with PyAutoArray fix)](https://github.com/PyAutoLabs/PyAutoLens/pull/555) (PyAutoLabs/PyAutoLens)
**API Changes:** None — test-only change. See full details below.

### [Add placeholder subplot_fit_quick for weak lensing and combined fits](https://github.com/PyAutoLabs/PyAutoLens/pull/553) (PyAutoLabs/PyAutoLens)
**API Changes:** New functions: \`subplot_fit_quick\` (weak), \`subplot_fit_combined_quick\` (imaging combined).

🤖 Generated with [Claude Code](https://claude.com/claude-code)

### [Add subplot_fit_quick for point source quick updates](https://github.com/PyAutoLabs/PyAutoLens/pull/552) (PyAutoLabs/PyAutoLens)
**API Changes:** New function `autolens.point.plot.fit_point_plots.subplot_fit_quick`.

### [Simplify subplot_fit_quick: use fit properties directly](https://github.com/PyAutoLabs/PyAutoLens/pull/551) (PyAutoLabs/PyAutoLens)
**API Changes:** None — same function, same output.

### [Fix subplot_fit_quick styling: arcsecond axes, source plane, code reuse](https://github.com/PyAutoLabs/PyAutoLens/pull/550) (PyAutoLabs/PyAutoLens)
**API Changes:** None — same functions, same output filenames.

### [Add subplot_fit_quick for interferometer quick updates](https://github.com/PyAutoLabs/PyAutoLens/pull/549) (PyAutoLabs/PyAutoLens)
**API Changes:** New function `autolens.interferometer.plot.fit_interferometer_plots.subplot_fit_quick`. The plotter's quick-update branch now calls this instead of `subplot_fit_dirty_images`.

### [perf: cache expensive @property on Fit classes](https://github.com/PyAutoLabs/PyAutoLens/pull/548) (PyAutoLabs/PyAutoLens)
**API Changes:** None — same properties, same return types. Now cached after first access.

### [Fast subplot_fit_quick: sub-second rendering for quick updates](https://github.com/PyAutoLabs/PyAutoLens/pull/547) (PyAutoLabs/PyAutoLens)
**API Changes:** None — `subplot_fit_quick` has the same signature. Internal rendering pipeline is different but the output PNG is the same 6-panel layout.

### [docs: expand quick-update cookbook + add config flag defaults](https://github.com/PyAutoLabs/autofit_workspace/pull/67) (PyAutoLabs/autofit_workspace)
**Scripts Changed:** - `scripts/cookbooks/analysis.py` — rewrote the `__Live Quick-Update Visualization__` section: documents `live_visual_update` separately from `background_quick_update` (the two are independent), adds an Analysis API surface subsection (`perform_quick_update`, `supports_background_update`, `supports_

### [docs: foundational latent-variables cookbook in autofit_workspace](https://github.com/PyAutoLabs/autofit_workspace/pull/64) (PyAutoLabs/autofit_workspace)
**Scripts Changed:** - `scripts/cookbooks/latent_variables.py` (new, ~200 lines) — 10 sections in order: Model Fit, What is a Latent Variable, Why Latent Variables, How PyAutoFit Computes Latents, Two Output Modes, Errors on Latents, Posterior Draws Under the Hood, Loading Results Downstream, When To Add A Latent vs A S

### [docs(cookbooks/analysis): __Live Quick-Update Visualization__ section](https://github.com/PyAutoLabs/autofit_workspace/pull/62) (PyAutoLabs/autofit_workspace)
**Scripts Changed:** - `scripts/cookbooks/analysis.py` — new `__Live Quick-Update Visualization__` section (52 lines) covering `iterations_per_quick_update`, `background_quick_update=True`, the new IPython live-cell rendering when running in a Jupyter / Colab kernel, the script-mode fallback (PNGs on disk unchanged), an

### [chore(scripts): Phase 3 use_jax=True consistency in features/search_chaining](https://github.com/PyAutoLabs/autofit_workspace/pull/61) (PyAutoLabs/autofit_workspace)
**Scripts Changed:** - `scripts/features/search_chaining.py` — added `use_jax=True` to all 4 `af.ex.Analysis(...)` calls so the chained pipeline runs the same JAX path as the grid-search sibling

### [feat: add af.NSS section to searches/nest.py tutorial (Phase 5)](https://github.com/PyAutoLabs/autofit_workspace/pull/60) (PyAutoLabs/autofit_workspace)
**Scripts Changed:** - `scripts/searches/nest.py` — added a new **Search: NSS** section after the existing Nautilus section walking through the NSS-specific kwargs (`n_live`, `num_mcmc_steps`, `num_delete`, `termination`, `checkpoint_interval`, `iterations_per_quick_update`); extended the top docstring + Contents block 

### [Disable model.graph output by default](https://github.com/PyAutoLabs/autofit_workspace/pull/56) (PyAutoLabs/autofit_workspace)
**Scripts Changed:** - None — config-only change to `config/output.yaml`.

### [docs: raw-flux latent guide + workspace config updates](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/108) (PyAutoLabs/autogalaxy_workspace)
**Scripts Changed:** - `config/latent.yaml` — Add `total_galaxy_0_flux: true` explicitly alongside the existing `total_galaxy_0_flux_mujy: true`; reflow the comment block to explain the raw / µJy split.
- `scripts/guides/units/flux.py` — New "Latent Variables: Total Flux Directly from the Fit" section. Documents that `l

### [interferometer: switch to TransformerNUFFT + apply_sparse_operator, reduce MGE to 5 Gaussians](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/106) (PyAutoLabs/autogalaxy_workspace)
**API Changes:** None — pure workspace edits.
**Scripts Changed:** - `features/multi_gaussian_expansion/{modeling,fit,likelihood_function}.py`
- `features/pixelization/{modeling,fit,galaxy_reconstruction,many_visibilities_preparation,likelihood_function}.py`

### [config: add quick_update_background + live_visual_update defaults](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/105) (PyAutoLabs/autogalaxy_workspace)
**Scripts Changed:** - `config/general.yaml` — appends `quick_update_background: false` and `live_visual_update: false` under both `updates:` and `hpc:` with explanatory comments.

### [docs: remove Array2D.native jit-blocked caveats from JAX variant blocks](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/104) (PyAutoLabs/autogalaxy_workspace)
**Scripts Changed:** - `scripts/imaging/simulator.py` — removed jit-blocked caveat from JAX variant notes
- `scripts/interferometer/simulator.py` — removed jit-blocked caveat from JAX variant notes

### [docs: __JAX__ in autogalaxy deferred (multi + guides mirror)](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/103) (PyAutoLabs/autogalaxy_workspace)
**Scripts Changed:** - `scripts/multi/start_here.py` — refresh 2 stale `__JAX__` blocks per Phase 0 contract
- `scripts/guides/data_structures.py` — new `__JAX__` covering `.array` story, host transfer, the not-pytree rule + `.array` unwrap-rewrap workaround
- `scripts/guides/galaxies.py` — new `__JAX__` covering Galaxy

### [docs: __JAX__ sections in per-dataset scripts (imaging + interferometer)](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/101) (PyAutoLabs/autogalaxy_workspace)
**Scripts Changed:** - `scripts/imaging/start_here.py` — refresh 2 stale `__JAX__` blocks
- `scripts/imaging/simulator.py` — new `__JAX Variant__` (`SimulatorImaging(use_jax=True)`)
- `scripts/imaging/fit.py` — `__JAX__` prose
- `scripts/imaging/likelihood_function.py` — `__JAX__` section with `@jax.jit` recipe + `Fitne

### [docs: add __JAX__ section to top-level start_here.py](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/99) (PyAutoLabs/autogalaxy_workspace)
**Scripts Changed:** - `start_here.py` — new `__JAX__` section (~70 lines of prose + one illustrative `simulator.via_galaxies_from(use_jax=True)` snippet) inserted after `__Galaxies__`.

### [docs: workspace tutorial for latent variables in autogalaxy_workspace](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/97) (PyAutoLabs/autogalaxy_workspace)
**Scripts Changed:** - `scripts/guides/results/latent_variables.py` (new, ~180 lines) — sections in order: Galaxy Latents in PyAutoGalaxy (the curated catalogue), Toggling Latents (workspace yaml override pattern), Model Fit (quick Nautilus run on the simple dataset with `magzero=25.0`), Loading Latent Results (via `ana

### [docs: raw-flux latent guides + workspace config updates](https://github.com/PyAutoLabs/autolens_workspace/pull/214) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `config/latent.yaml` — Add `total_lens_flux`, `total_lensed_source_flux`, `total_source_flux` (all `true`) to the workspace overrides; reflow the comment block to explain the raw / µJy / dimensionless grouping; add `total_galaxy_0_flux: false` as an explicit cross-library silencer (the autogalaxy 

### [docs: simplify weak/fit.py to load dataset via al.from_json](https://github.com/PyAutoLabs/autolens_workspace/pull/212) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/weak/fit.py` — replaced inline `WeakDataset` reconstruction with `al.from_json(file_path=dataset_path / "dataset.json")`; revised the `__Dataset__` docstring accordingly. (−20 / +5 lines.)

### [interferometer: switch to TransformerNUFFT + apply_sparse_operator, MGE to 5 Gaussians](https://github.com/PyAutoLabs/autolens_workspace/pull/211) (PyAutoLabs/autolens_workspace)
**API Changes:** None — pure workspace edits.
**Scripts Changed:** 22 scripts across `features/{datacube,extra_galaxies,linear_light_profiles,multi_gaussian_expansion,pixelization,subhalo/detect}/` plus 2 READMEs.

### [config: add quick_update_background + live_visual_update defaults](https://github.com/PyAutoLabs/autolens_workspace/pull/210) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `config/general.yaml` — appends `quick_update_background: false` and `live_visual_update: false` under both `updates:` and `hpc:` with explanatory comments.

### [docs: remove Array2D.native jit-blocked caveats from JAX variant blocks](https://github.com/PyAutoLabs/autolens_workspace/pull/208) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/imaging/simulator.py` — removed jit-blocked caveat from JAX variant notes
- `scripts/interferometer/simulator.py` — removed jit-blocked caveat from JAX variant notes
- `scripts/group/simulator.py` — removed jit-blocked caveat from JAX variant notes
- `scripts/point_source/simulator.py` — 

### [docs: __JAX__ in deferred datasets (multi + group + cluster) + cluster simulator migration](https://github.com/PyAutoLabs/autolens_workspace/pull/207) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** **3c — multi (refresh):**
- `scripts/multi/start_here.py` — refresh 2 stale `__JAX__` blocks per Phase 0 contract.

**3e — group (full add):**
- `scripts/group/start_here.py` — refresh 2 stale `__JAX__` blocks
- `scripts/group/simulator.py` — `__JAX Variant__` reference (delegates to `imaging/simula

### [docs: __JAX__ sections in workspace guides (data_structures, galaxies, tracer, lens_calc)](https://github.com/PyAutoLabs/autolens_workspace/pull/205) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/guides/data_structures.py` — `__JAX__` section covering the `.array` story, when backing becomes `jax.Array`, host-transfer mechanics, the not-pytree rule + `.array` unwrap-rewrap workaround.
- `scripts/guides/galaxies.py` — pytree registration for `Galaxy` / `Galaxies` (implicit via Anal

### [docs: __JAX__ sections in per-dataset scripts (imaging + interferometer + point_source)](https://github.com/PyAutoLabs/autolens_workspace/pull/203) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/imaging/start_here.py` — refresh 2 stale `__JAX__` blocks
- `scripts/imaging/simulator.py` — new `__JAX Variant__` (`SimulatorImaging(use_jax=True)`)
- `scripts/imaging/fit.py` — `__JAX__` prose
- `scripts/imaging/likelihood_function.py` — `__JAX__` section with `@jax.jit` recipe + `Fitne
