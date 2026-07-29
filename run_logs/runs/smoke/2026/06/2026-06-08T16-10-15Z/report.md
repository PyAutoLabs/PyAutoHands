# Release Readiness Report

**Status: NOT READY**

**Run:** `2026-06-08T16-10-15Z`  •  **Path:** `/home/jammy/Code/PyAutoLabs/PyAutoBuild/test_results/runs/2026-06-08T16-10-15Z`  •  **Total duration:** 7798.3s

## Slow-Skipped Scripts (needs performance fix)

**22 script(s)** are being skipped because they exceed the 60s per-script timeout cap. These are NOT permanent skips — they need the underlying performance issue fixed and the `SLOW` marker removed from the workspace's `config/build/no_run.yaml`.

| Workspace | Script | Marked | Age | Reason |
|-----------|--------|--------|-----|--------|
| HowToGalaxy | `guides/results/database/start_here` | 2026-04-10 | 59d **STALE** | previously failed fast on a broken aggregator query; now runs the real aggregator and exceeds 60s |
| HowToGalaxy | `guides/results/examples/galaxies_fit` | 2026-04-10 | 59d **STALE** | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| HowToGalaxy | `guides/results/examples/models` | 2026-04-10 | 59d **STALE** | cascade from SLOW-skipped results/start_here.py; aggregator returns NoneType so instance.galaxies is None |
| HowToGalaxy | `guides/results/examples/samples` | 2026-04-10 | 59d **STALE** | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| HowToGalaxy | `guides/results/start_here` | 2026-04-10 | 59d **STALE** | exceeds 60s test timeout; unsets TEST_MODE to produce real samples for downstream examples |
| HowToGalaxy | `guides/results/workflow/csv_make` | 2026-04-10 | 59d **STALE** | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| HowToLens | `guides/results/database/start_here` | 2026-04-10 | 59d **STALE** | previously failed fast on a broken aggregator query; now runs the real aggregator and exceeds 60s |
| HowToLens | `guides/results/examples/queries` | 2026-04-10 | 59d **STALE** | cascade from SLOW-skipped results/start_here.py; stub Model lacks sersic_index attribute |
| HowToLens | `guides/results/examples/samples` | 2026-04-10 | 59d **STALE** | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| HowToLens | `guides/results/examples/samples_via_aggregator` | 2026-04-10 | 59d **STALE** | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| HowToLens | `howtolens/chapter_4_pixelizations/tutorial_10_brightness_adaption` | 2026-04-10 | 59d **STALE** | pixelization tutorial exceeds 60s test timeout |
| autogalaxy_workspace | `guides/results/database/start_here` | 2026-04-10 | 59d **STALE** | previously failed fast on a broken aggregator query; now runs the real aggregator and exceeds 60s |
| autogalaxy_workspace | `guides/results/workflow/csv_make` | 2026-04-10 | 59d **STALE** | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| autolens_workspace | `guides/results/database/start_here` | 2026-04-10 | 59d **STALE** | previously failed fast on a broken aggregator query; now runs the real aggregator and exceeds 60s |
| autolens_workspace_test | `database/scrape/multi_analysis` | 2026-04-10 | 59d **STALE** | exceeds 60s timeout; _test workspaces run full searches without test mode |
| autolens_workspace_test | `database/scrape/slam_general` | 2026-04-10 | 59d **STALE** | exceeds 60s timeout; _test workspaces run full searches without test mode |
| autolens_workspace_test | `database/scrape/slam_multi_one_by_one` | 2026-04-10 | 59d **STALE** | exceeds 60s timeout; _test workspaces run full searches without test mode |
| autolens_workspace_test | `database/scrape/slam_pix` | 2026-04-10 | 59d **STALE** | exceeds 60s timeout; _test workspaces run full searches without test mode |
| autolens_workspace_test | `imaging/modeling_visualization_jit` | 2026-05-07 | 32d **STALE** | JIT + full visualization pipeline exceeds 300s cap (autogalaxy variant ~90s); unblocked by PR #70 from prior `expected jax.Array, got numpy.float64` AssertionError, now hits perf wall |
| autolens_workspace_test | `imaging/modeling_visualization_jit_delaunay` | 2026-05-07 | 32d **STALE** | JIT + full visualization pipeline exceeds 300s cap; same root cause as modeling_visualization_jit |
| autolens_workspace_test | `imaging/modeling_visualization_jit_rectangular` | 2026-05-07 | 32d **STALE** | JIT + full visualization pipeline exceeds 301s cap; same root cause as modeling_visualization_jit |
| autolens_workspace_test | `interferometer/modeling_visualization_jit` | 2026-05-20 | 19d | JIT + full visualization pipeline exceeds 300s cap; same root cause as imaging/modeling_visualization_jit family |

## Needs-Fix Scripts (parked for investigation)

**39 script(s)** are being skipped because they are broken and parked as a to-do list. These are NOT permanent skips — investigate the failure, fix the underlying bug, and remove the `NEEDS_FIX` marker from the workspace's `config/build/no_run.yaml`.

| Workspace | Script | Marked | Age | Reason |
|-----------|--------|--------|-----|--------|
| HowToFit | `chapter_1_introduction/tutorial_5_results_and_samples` | 2026-04-10 | 59d **STALE** | IndexError in samples access, likely related to InstanceInterpolator bug in autofit features/interpolate |
| HowToGalaxy | `autogalaxy_workspace/scripts/imaging/modeling` | 2026-04-10 | 59d **STALE** | KeyError on ('galaxies','galaxy','bulge','ell_comps'...) kwargs after API drift in top-level imaging/modeling.py |
| HowToGalaxy | `ellipse/modeling` | 2026-04-10 | 59d **STALE** | KeyError on 'ellipses.0.centre_0' kwargs after API drift in ellipse model |
| HowToGalaxy | `guides/advanced/over_sampling` | 2026-04-10 | 59d **STALE** | plot_grid() got unexpected kwarg 'plot_grid_lines' after plotter API drift |
| HowToGalaxy | `howtogalaxy/chapter_4_pixelizations/tutorial_2_mappers` | 2026-04-10 | 59d **STALE** | IndexError in mapper tutorial, likely empty mapping array |
| HowToGalaxy | `howtogalaxy/chapter_4_pixelizations/tutorial_5_model_fit` | 2026-04-10 | 59d **STALE** | LinAlgError: matrix not positive definite in pixelization fit |
| HowToGalaxy | `imaging/data_preparation/manual/mask_irregular` | 2026-04-10 | 59d **STALE** | silent failure, needs investigation |
| HowToGalaxy | `imaging/features/pixelization/modeling` | 2026-04-10 | 59d **STALE** | LinAlgError: matrix not positive definite in pixelization modeling |
| HowToGalaxy | `interferometer/features/pixelization/modeling` | 2026-04-10 | 59d **STALE** | LinAlgError: matrix not positive definite in interferometer pixelization modeling |
| HowToLens | `group/slam` | 2026-04-10 | 59d **STALE** | PriorException: upper limit must be greater than lower limit in group SLaM pipeline |
| HowToLens | `howtolens/chapter_1_introduction/tutorial_3_more_ray_tracing` | 2026-04-10 | 59d **STALE** | ValueError: Axis limits cannot be NaN or Inf in plotting |
| HowToLens | `howtolens/chapter_2_lens_modeling/tutorial_2_practicalities` | 2026-04-10 | 59d **STALE** | NameError: 'af' not defined; tutorial missing ~80 lines of imports + setup boilerplate (compare tutorial_1) |
| HowToLens | `howtolens/chapter_2_lens_modeling/tutorial_6_masking_and_positions` | 2026-04-10 | 59d **STALE** | ValueError: zero-size array reduction, empty mask after pre-computed positions load |
| HowToLens | `howtolens/chapter_4_pixelizations/tutorial_2_mappers` | 2026-04-10 | 59d **STALE** | ValueError: zero-size array reduction, empty mapper array |
| HowToLens | `imaging/data_preparation/manual/mask_irregular` | 2026-04-10 | 59d **STALE** | silent failure, needs investigation |
| HowToLens | `imaging/features/pixelization/delaunay` | 2026-04-10 | 59d **STALE** | autofit.exc.FitException in Delaunay pixelization fit |
| HowToLens | `imaging/features/pixelization/slam` | 2026-04-10 | 59d **STALE** | autofit.exc.FitException in SLaM pixelization pipeline |
| HowToLens | `interferometer/features/pixelization/delaunay` | 2026-04-10 | 59d **STALE** | broadcast shape mismatch (2,2) vs (1032,1032) in Delaunay interferometer |
| HowToLens | `multi/features/wavelength_dependence/modeling` | 2026-04-10 | 59d **STALE** | autofit.exc.FitException in multi-wavelength modeling |
| autofit_workspace | `features/interpolate` | 2026-04-10 | 59d **STALE** | IndexError in InstanceInterpolator.__getitem__ when querying time == 1.5; value_map lookup falls through to empty instances list |
| autogalaxy_workspace | `autogalaxy_workspace/scripts/imaging/modeling` | 2026-04-10 | 59d **STALE** | KeyError on ('galaxies','galaxy','bulge','ell_comps'...) kwargs after API drift in top-level imaging/modeling.py |
| autogalaxy_workspace | `imaging/data_preparation/manual/mask_irregular` | 2026-04-10 | 59d **STALE** | silent failure, needs investigation |
| autogalaxy_workspace | `imaging/features/pixelization/modeling` | 2026-04-10 | 59d **STALE** | LinAlgError: matrix not positive definite in pixelization modeling |
| autogalaxy_workspace | `interferometer/features/multi_gaussian_expansion/likelihood_function` | 2026-05-20 | 19d | LinAlgError: matrix singular in MGE inversion -> InversionException (known_numerical; same family as pixelization variants above) |
| autogalaxy_workspace | `interferometer/features/pixelization/modeling` | 2026-04-10 | 59d **STALE** | LinAlgError: matrix not positive definite in interferometer pixelization modeling |
| autolens_workspace | `group/features/advanced/double_einstein_ring/slam` | 2026-05-20 | 19d | same cascade as imaging variant — synthetic samples_summary lacks adapt_data; parking pattern of the imaging entry didn't cover this group/ twin |
| autolens_workspace | `group/slam` | 2026-04-10 | 59d **STALE** | PriorException: upper limit must be greater than lower limit in group SLaM pipeline |
| autolens_workspace | `imaging/data_preparation/manual/mask_irregular` | 2026-04-10 | 59d **STALE** | silent failure, needs investigation |
| autolens_workspace | `imaging/features/advanced/double_einstein_ring/slam` | 2026-05-07 | 32d **STALE** | autofit.exc.FitException in SLaM bypass mode (same family as imaging/features/pixelization/slam — Adapt regularization needs adapt_data which the synthetic samples_summary doesn't carry; cascade goes deep, fixing in one PR isn't tractable) |
| autolens_workspace | `imaging/features/pixelization/delaunay` | 2026-04-10 | 59d **STALE** | autofit.exc.FitException in Delaunay pixelization fit |
| autolens_workspace | `imaging/features/pixelization/slam` | 2026-04-10 | 59d **STALE** | autofit.exc.FitException in SLaM pixelization pipeline |
| autolens_workspace | `interferometer/features/pixelization/delaunay` | 2026-04-10 | 59d **STALE** | broadcast shape mismatch (2,2) vs (1032,1032) in Delaunay interferometer |
| autolens_workspace | `multi/features/wavelength_dependence/modeling` | 2026-04-10 | 59d **STALE** | autofit.exc.FitException in multi-wavelength modeling |
| autolens_workspace_test | `database/scrape/general` | 2026-04-27 | 42d **STALE** | PyAutoGalaxy abstract_fit.linear_light_profile_intensity_dict raises "TypeError: __hash__ method should return an integer" during subplot_fit_imaging after the search completes (a light-profile object's __hash__ returns a non-int). Surfaced once the dataset_label="build" path fix let the script progress past Imaging.from_fits. |
| autolens_workspace_test | `imaging/visualization` | 2026-04-10 | 59d **STALE** | AssertionError: dataset.png missing after visualization refactor |
| autolens_workspace_test | `jax_grad/imaging_lp` | 2026-04-10 | 59d **STALE** | JAX traceback in gradient computation for light profile |
| autolens_workspace_test | `jax_grad/imaging_mge` | 2026-04-10 | 59d **STALE** | AssertionError: Gradient is all zeros in MGE gradient computation |
| autolens_workspace_test | `jax_likelihood_functions/imaging/delaunay_mge` | 2026-04-10 | 59d **STALE** | timeout in JAX likelihood function benchmark |
| autolens_workspace_test | `jax_likelihood_functions/imaging/mge_group` | 2026-04-10 | 59d **STALE** | timeout in JAX likelihood function benchmark |

## Summary

| Passed | Failed | Skipped | Timeout |
|--------|--------|---------|---------|
| 598 | 20 | 71 | 1 |

## Per-Project Breakdown

| Project | Passed | Failed | Skipped | Timeout | Duration |
|---------|--------|--------|---------|---------|----------|
| autofit | 25 | 1 | 6 | 0 | 136.2s |
| autofit_test | 31 | 4 | 2 | 0 | 171.8s |
| autogalaxy | 107 | 1 | 14 | 0 | 877.7s |
| autogalaxy_test | 50 | 4 | 0 | 0 | 1016.3s |
| autolens | 221 | 1 | 30 | 1 | 2977.9s |
| autolens_test | 84 | 6 | 15 | 0 | 1903.5s |
| euclid | 5 | 0 | 0 | 0 | 202.5s |
| howtofit | 15 | 0 | 1 | 0 | 69.0s |
| howtogalaxy | 24 | 1 | 1 | 0 | 141.5s |
| howtolens | 36 | 2 | 2 | 0 | 301.9s |

## Slowest scripts (top 25)

| Script | Project | Status | Duration | Share |
|--------|---------|--------|----------|-------|
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/latent_variables.py` | autolens | timeout | 300.0s | 3.8% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/workflow/csv_make.py` | autolens | passed | 158.6s | 2.0% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/start_here.py` | autolens | failed | 151.4s | 1.9% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/point_source/modeling_visualization_jit.py` | autolens_test | passed | 139.3s | 1.8% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/database/scrape/scaling_relation.py` | autolens_test | passed | 82.7s | 1.1% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/multi/mge_group.py` | autolens_test | passed | 78.9s | 1.0% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/multi/start_here.py` | autolens | passed | 77.8s | 1.0% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/subhalo.py` | autolens_test | passed | 71.5s | 0.9% |
| `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_4_pixelizations/tutorial_10_brightness_adaption.py` | howtolens | passed | 71.3s | 0.9% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/delaunay_mge.py` | autolens_test | passed | 70.8s | 0.9% |
| `/home/jammy/Code/PyAutoLabs/euclid_strong_lens_modeling_pipeline/scripts/lens_model_waveband.py` | euclid | passed | 69.7s | 0.9% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/visualization_jax.py` | autolens_test | failed | 66.6s | 0.9% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/delaunay_mge.py` | autogalaxy_test | passed | 65.6s | 0.8% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_mge.py` | autolens_test | passed | 64.7s | 0.8% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/profiles/light_and_mass_profiles.py` | autolens | passed | 63.4s | 0.8% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/start_here.py` | autolens | passed | 60.3s | 0.8% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/start_here.py` | autolens | passed | 54.0s | 0.7% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/units/flux.py` | autolens | passed | 53.6s | 0.7% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_dspl.py` | autolens_test | passed | 51.9s | 0.7% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/multi/mge_group.py` | autogalaxy_test | passed | 50.8s | 0.7% |
| `/home/jammy/Code/PyAutoLabs/euclid_strong_lens_modeling_pipeline/scripts/mge_lens_only.py` | euclid | passed | 50.1s | 0.6% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular_mge.py` | autolens_test | passed | 49.8s | 0.6% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/delaunay_mge.py` | autogalaxy_test | passed | 49.3s | 0.6% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/multi/delaunay_mge.py` | autogalaxy_test | passed | 48.5s | 0.6% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/datacube/delaunay.py` | autolens_test | failed | 48.5s | 0.6% |

## Failures by Classification

### Source Code Bugs (19)

- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/database/scrape/grid_search.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/database/scrape/grid_search.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
    File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/sqlalchemy/engine/base.py", line 2355, in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/sqlalchemy/engine/base.py", line 1967, in _exec_single_context
    self.dialect.do_execute(
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/sqlalchemy/engine/default.py", line 941, in do_execute
    cursor.execute(statement, parameters)
sqlalchemy.exc.IntegrityError: (sqlite3.IntegrityError) UNIQUE constraint failed: fit.id
[SQL: INSERT INTO fit (id, is_complete, max_log_likelihood, parent_id, is_grid_search, unique_tag, name, path_prefix, model_id, instance_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)]
[parameters: ('gaussian_x1', 1, None, None, 1, 'gaussian_x1', None, None, None, None)]
(Background on this error at: https://sqlalche.me/e/20/gkpj)
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/database/scrape/sensitivity.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/database/scrape/sensitivity.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
    File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/sqlalchemy/engine/base.py", line 2355, in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/sqlalchemy/engine/base.py", line 1967, in _exec_single_context
    self.dialect.do_execute(
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/sqlalchemy/engine/default.py", line 941, in do_execute
    cursor.execute(statement, parameters)
sqlalchemy.exc.IntegrityError: (sqlite3.IntegrityError) UNIQUE constraint failed: fit.id
[SQL: INSERT INTO fit (id, is_complete, max_log_likelihood, parent_id, is_grid_search, unique_tag, name, path_prefix, model_id, instance_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)]
[parameters: ('', 0, None, None, 1, '', None, None, None, None)]
(Background on this error at: https://sqlalche.me/e/20/gkpj)
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/features/latent_nan_robustness.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/features/latent_nan_robustness.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  
If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/features/latent_nan_robustness.py", line 94, in <module>
    assert len(result.samples.sample_list) > LATENT_BATCH_SIZE, (
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Need >3 samples for a multi-batch latent run; got 2.
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
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  
                    This is less than or equal to zero, and therefore an ill-defined value which must be corrected.
                    
                    The 2D indexes of the arrays in the native noise map array are [[ 0  0]
 [ 0  1]
 [ 0  2]
 ...
 [99 97]
 [99 98]
 [99 99]].
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
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/interferometer/modeling_visualization_jit.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/interferometer/modeling_visualization_jit.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/updater.py", line 268, in _compute_latent_samples
    latent_samples = analysis.compute_latent_samples(
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/analysis/analysis.py", line 259, in compute_latent_samples
    latent_values_batch = jnp.stack(latent_values_batch, axis=-1)  # (batch, n_latents)
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/jax/_src/numpy/lax_numpy.py", line 4451, in stack
    raise ValueError("Need at least one array to stack.")
ValueError: Need at least one array to stack.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/latent/latent_nan_robustness.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/latent/latent_nan_robustness.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  
If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/latent/latent_nan_robustness.py", line 65, in <module>
    assert len(result.samples.sample_list) > LATENT_BATCH_SIZE, (
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Need >3 samples for a multi-batch latent run; got 2. Increase n_live / n_like_max.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/start_here.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/start_here.py']' returned non-zero exit status 1.
  - **Recently modified** in [docs: __JAX__ in autogalaxy deferred (multi + guides mirror)](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/103)
  - **Recently modified** in [docs: __JAX__ sections in per-dataset scripts (imaging + interferometer)](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/101)
  - **Recently modified** in [docs: add __JAX__ section to top-level start_here.py](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/99)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  
                    This is less than or equal to zero, and therefore an ill-defined value which must be corrected.
                    
                    The 2D indexes of the arrays in the native noise map array are [[ 0  0]
 [ 0  1]
 [ 0  2]
 ...
 [99 97]
 [99 98]
 [99 99]].
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/simulator.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/simulator.py']' returned non-zero exit status 1.
  - **Recently modified** in [docs: remove Array2D.native jit-blocked caveats from JAX variant blocks](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/104)
  - **Recently modified** in [docs: __JAX__ sections in per-dataset scripts (imaging + interferometer)](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/101)
  - **Recently modified** in [docs: add __JAX__ section to top-level start_here.py](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/99)
  - **Recently modified** in [docs: remove Array2D.native jit-blocked caveats from JAX variant blocks](https://github.com/PyAutoLabs/autolens_workspace/pull/208)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/simulator.py", line 197, in <module>
    raw = np.asarray(jitted_solve(tracer, coord))
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <function jitted_solve at 0x7fb8297c59e0> as an abstract array. The problematic value is of type <class 'autogalaxy.galaxy.galaxy.Galaxy'> and was passed to the function at path tracer[0][0].
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
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/visualization_jax.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/visualization_jax.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  
If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/visualization_jax.py", line 179, in <module>
    assert _warm_dt < 0.1, (
           ^^^^^^^^^^^^^^
AssertionError: zero_contour warm call took 163.7 ms (> 100 ms) — closure cache-busting bug from PyAutoGalaxy #433 may have regressed
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/datacube/delaunay.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/datacube/delaunay.py']' died with <Signals.SIGKILL: 9>.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:173: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autolens_workspace_test matches the installed library version (2026.5.29.4): no `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/latent/latent_nan_robustness.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/latent/latent_nan_robustness.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  
If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/latent/latent_nan_robustness.py", line 80, in <module>
    assert len(result.samples.sample_list) > LATENT_BATCH_SIZE, (
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Need >3 samples for a multi-batch latent run; got 2. Increase n_live / n_like_max.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_4_pixelizations/tutorial_2_mappers.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_4_pixelizations/tutorial_2_mappers.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_4_pixelizations/tutorial_2_mappers.py", line 106, in <module>
    indexes = mapper.slim_indexes_for_pix_indexes(pix_indexes=pix_indexes)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/inversion/mappers/abstract.py", line 451, in slim_indexes_for_pix_indexes
    image_for_source[index]
    ~~~~~~~~~~~~~~~~^^^^^^^
IndexError: list index out of range
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

### Environment Issues (1)

- `/home/jammy/Code/PyAutoLabs/autofit_workspace/scripts/searches/nest.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autofit_workspace/scripts/searches/nest.py']' returned non-zero exit status 1.
  - **Recently modified** in [feat: add af.NSS section to searches/nest.py tutorial (Phase 5)](https://github.com/PyAutoLabs/autofit_workspace/pull/60)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autofit_workspace/scripts/searches/nest.py", line 348, in <module>
    search = af.NSS(
             ^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/nest/nss/search.py", line 254, in __init__
    raise ImportError(
ImportError: af.NSS requires the optional `nss` package and the matching `handley-lab/blackjax` fork. Install via:
    pip install autofit[nss]
The extra pins specific upstream commits — see PyAutoFit's pyproject.toml `[project.optional-dependencies] nss` entry.
  ```
  </details>

### Timeouts (1)

- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/latent_variables.py`
  - Timed out after 300s
  - **Recently modified** in [docs: foundational latent-variables cookbook in autofit_workspace](https://github.com/PyAutoLabs/autofit_workspace/pull/64)
  - **Recently modified** in [docs: raw-flux latent guide + workspace config updates](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/108)
  - **Recently modified** in [docs: raw-flux latent guides + workspace config updates](https://github.com/PyAutoLabs/autolens_workspace/pull/214)

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

### [test: skip NSS tests without optional dependency](https://github.com/PyAutoLabs/PyAutoFit/pull/1312) (PyAutoLabs/PyAutoFit)
**API Changes:** None — test-only changes.

### [fix(latent): degenerate latent edge cases (quantile n=1, latent exceptions, anti-correlated NaNs)](https://github.com/PyAutoLabs/PyAutoFit/pull/1311) (PyAutoLabs/PyAutoFit)
**API Changes:** No signature changes. Behaviour: `quantile()` now handles a single sample; `compute_latent_samples` tolerates latent functions that raise (any exception → dropped sample) and salvages anti-correlated-NaN cases instead of returning `None`.
See full details below.

### [fix(latent): global masking in compute_latent_samples to prevent KeyError on per-batch NaN drops](https://github.com/PyAutoLabs/PyAutoFit/pull/1310) (PyAutoLabs/PyAutoFit)
**API Changes:** No signature changes. Behaviour change to `Analysis.compute_latent_samples`: latent finite-masking is now global instead of per-batch, and a fully-degenerate latent set returns `None` rather than raising.
See full details below.

### [feat: cross-Analysis shared per-evaluation state in FactorGraphModel](https://github.com/PyAutoLabs/PyAutoFit/pull/1308) (PyAutoLabs/PyAutoFit)
**API Changes:** All changes are additive and backward compatible — no removals or renames.

- Added `Analysis.shared_state_from(instance) -> None`: an opt-in hook (default returns `None`) that computes a per-evaluation object shared across a `FactorGraphModel`'s factors. The per-evaluation, cross-factor sibling of 

### [fix(nss): chunked algo.init follow-up to #1303](https://github.com/PyAutoLabs/PyAutoFit/pull/1305) (PyAutoLabs/PyAutoFit)
**API Changes:** No public-API changes. The existing `af.NSS(chunk_size=...)` kwarg (added by #1303) gains coverage of the init path that previously OOMed before reaching the configuration log line. New private module `autofit.non_linear.search.nest.nss._chunked_nss` is an implementation detail (`_`-prefixed); only 

### [feat(nss): chunk_size kwarg for inversion-heavy A100 likelihoods](https://github.com/PyAutoLabs/PyAutoFit/pull/1303) (PyAutoLabs/PyAutoFit)
**API Changes:** `af.NSS.__init__` gains an optional `chunk_size: Optional[int] = None` kwarg. When unset, behaviour is bit-identical to the previous version. When set and below `num_delete`, the internal `blackjax.nss(update_strategy=...)` is swapped to a chunked variant that uses `jax.lax.map(batch_size=chunk_size

### [Cache model.parameterization; try interactive matplotlib backends](https://github.com/PyAutoLabs/PyAutoFit/pull/1299) (PyAutoLabs/PyAutoFit)
**API Changes:** None — `parameterization` was already a `@property`, now `@functools.cached_property`. Same external interface. The live_viewer backend selection is internal.

### [feat: Preloads API for reusing channel-invariant inversion quantities](https://github.com/PyAutoLabs/PyAutoArray/pull/344) (PyAutoLabs/PyAutoArray)
**API Changes:** All additive and backward compatible — no removals or renames.

- Added `aa.AbstractPreloads` and `aa.PreloadsInterferometer(curvature_matrix=None)` — containers for preloaded inversion quantities (new `autoarray/preloads/` package).
- `AbstractInversion`, the interferometer inversions, and the `inv

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

### [Lensing potential for elliptical/spherical dark-matter profiles (NFW/gNFW) + NFWSph fix](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/470) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** Adds a working `potential_2d_from` to the elliptical/spherical dark-matter profiles (via a single MGE-decomposition method on `gNFW`, inherited by `NFW`, `gNFWSph`, and all MCR/Virial variants). Corrects `NFWSph.potential_2d_from` (it returned values a factor of `r_s` too small). No public signature

### [fix(mass): convergence_func on PowerLawBroken, PowerLawMultipole, cNFW family](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/467) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** Added `convergence_func` overrides on `PowerLawBroken`, `PowerLawBrokenSph` (inherited), `PowerLawMultipole`, and the `cNFW` family (`cNFWSph` + MCR variants inherit). `PowerLawBroken._convergence` is a new private radial helper. `PowerLawBroken.potential_2d_from` now raises `NotImplementedError` ex

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

### [feat: datacube shared-state for AnalysisInterferometer via curvature preloads](https://github.com/PyAutoLabs/PyAutoLens/pull/566) (PyAutoLabs/PyAutoLens)
**API Changes:** All additive and backward compatible — no removals or renames.

- `AnalysisInterferometer.__init__` gains an opt-in `shared_preloads=False` flag.
- New method `AnalysisInterferometer.shared_state_from(instance)` — returns a `PreloadsInterferometer` with the channel-invariant `curvature_matrix` (or `

### [test: regression guard for HowToLens tutorial_3 NaN axis-limits crash](https://github.com/PyAutoLabs/PyAutoLens/pull/560) (PyAutoLabs/PyAutoLens)
**API Changes:** None — test-only.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

### [Honour PYAUTO_TEST_MODE in LOSSampler to fix los_halos simulator timeouts](https://github.com/PyAutoLabs/PyAutoLens/pull/559) (PyAutoLabs/PyAutoLens)
**API Changes:** `autolens.lens.los.negative_kappa_from` gains two optional keyword arguments, `quad_limit=50` and `quad_epsrel=1.49e-8` (both scipy's own `quad` defaults), threaded into its inner and outer integrals. Existing callers are unaffected. `LOSSampler.galaxies_from` now reads `autoconf.test_mode.is_test_m

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

### [feat: shared_analysis_state feature example for FactorGraphModel shared state](https://github.com/PyAutoLabs/autofit_workspace/pull/69) (PyAutoLabs/autofit_workspace)
**Scripts Changed:** - `scripts/features/shared_analysis_state.py` — new feature tutorial: builds a fully-shared 3-Gaussian factor graph, opts into `Analysis.share_model_data` / `shared_state_from`, and explains when sharing is valid (contrasting with `graphical_models.py`, which shares only `centre`).
- `scripts/featur

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

### [feat: datacube modeling opts into shared_preloads](https://github.com/PyAutoLabs/autolens_workspace/pull/218) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/interferometer/features/datacube/modeling.py` — set `shared_preloads=True` on each per-channel `AnalysisInterferometer`; added a "Shared Preloads" prose section (mechanism, validity precondition, speed-up, cross-reference to the parity test).

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
