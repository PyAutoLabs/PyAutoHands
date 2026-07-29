# Release Readiness Report

**Status: NOT READY**

**Run:** `2026-05-20T18-55-23Z`  •  **Path:** `/home/jammy/Code/PyAutoLabs/PyAutoBuild/test_results/runs/2026-05-20T18-55-23Z`  •  **Total duration:** 5709.2s

## Slow-Skipped Scripts (needs performance fix)

**10 script(s)** are being skipped because they exceed the 60s per-script timeout cap. These are NOT permanent skips — they need the underlying performance issue fixed and the `SLOW` marker removed from the workspace's `config/build/no_run.yaml`.

| Workspace | Script | Marked | Age | Reason |
|-----------|--------|--------|-----|--------|
| autogalaxy_workspace | `guides/results/database/start_here` | 2026-04-10 | 40d **STALE** | previously failed fast on a broken aggregator query; now runs the real aggregator and exceeds 60s |
| autogalaxy_workspace | `guides/results/workflow/csv_make` | 2026-04-10 | 40d **STALE** | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| autolens_workspace | `guides/results/database/start_here` | 2026-04-10 | 40d **STALE** | previously failed fast on a broken aggregator query; now runs the real aggregator and exceeds 60s |
| autolens_workspace_test | `database/scrape/multi_analysis` | 2026-04-10 | 40d **STALE** | exceeds 60s timeout; _test workspaces run full searches without test mode |
| autolens_workspace_test | `database/scrape/slam_general` | 2026-04-10 | 40d **STALE** | exceeds 60s timeout; _test workspaces run full searches without test mode |
| autolens_workspace_test | `database/scrape/slam_multi_one_by_one` | 2026-04-10 | 40d **STALE** | exceeds 60s timeout; _test workspaces run full searches without test mode |
| autolens_workspace_test | `database/scrape/slam_pix` | 2026-04-10 | 40d **STALE** | exceeds 60s timeout; _test workspaces run full searches without test mode |
| autolens_workspace_test | `imaging/modeling_visualization_jit` | 2026-05-07 | 13d | JIT + full visualization pipeline exceeds 300s cap (autogalaxy variant ~90s); unblocked by PR #70 from prior `expected jax.Array, got numpy.float64` AssertionError, now hits perf wall |
| autolens_workspace_test | `imaging/modeling_visualization_jit_delaunay` | 2026-05-07 | 13d | JIT + full visualization pipeline exceeds 300s cap; same root cause as modeling_visualization_jit |
| autolens_workspace_test | `imaging/modeling_visualization_jit_rectangular` | 2026-05-07 | 13d | JIT + full visualization pipeline exceeds 301s cap; same root cause as modeling_visualization_jit |

## Needs-Fix Scripts (parked for investigation)

**18 script(s)** are being skipped because they are broken and parked as a to-do list. These are NOT permanent skips — investigate the failure, fix the underlying bug, and remove the `NEEDS_FIX` marker from the workspace's `config/build/no_run.yaml`.

| Workspace | Script | Marked | Age | Reason |
|-----------|--------|--------|-----|--------|
| autofit_workspace | `features/interpolate` | 2026-04-10 | 40d **STALE** | IndexError in InstanceInterpolator.__getitem__ when querying time == 1.5; value_map lookup falls through to empty instances list |
| autogalaxy_workspace | `autogalaxy_workspace/scripts/imaging/modeling` | 2026-04-10 | 40d **STALE** | KeyError on ('galaxies','galaxy','bulge','ell_comps'...) kwargs after API drift in top-level imaging/modeling.py |
| autogalaxy_workspace | `imaging/data_preparation/manual/mask_irregular` | 2026-04-10 | 40d **STALE** | silent failure, needs investigation |
| autogalaxy_workspace | `imaging/features/pixelization/modeling` | 2026-04-10 | 40d **STALE** | LinAlgError: matrix not positive definite in pixelization modeling |
| autogalaxy_workspace | `interferometer/features/pixelization/modeling` | 2026-04-10 | 40d **STALE** | LinAlgError: matrix not positive definite in interferometer pixelization modeling |
| autolens_workspace | `group/slam` | 2026-04-10 | 40d **STALE** | PriorException: upper limit must be greater than lower limit in group SLaM pipeline |
| autolens_workspace | `imaging/data_preparation/manual/mask_irregular` | 2026-04-10 | 40d **STALE** | silent failure, needs investigation |
| autolens_workspace | `imaging/features/advanced/double_einstein_ring/slam` | 2026-05-07 | 13d | autofit.exc.FitException in SLaM bypass mode (same family as imaging/features/pixelization/slam — Adapt regularization needs adapt_data which the synthetic samples_summary doesn't carry; cascade goes deep, fixing in one PR isn't tractable) |
| autolens_workspace | `imaging/features/pixelization/delaunay` | 2026-04-10 | 40d **STALE** | autofit.exc.FitException in Delaunay pixelization fit |
| autolens_workspace | `imaging/features/pixelization/slam` | 2026-04-10 | 40d **STALE** | autofit.exc.FitException in SLaM pixelization pipeline |
| autolens_workspace | `interferometer/features/pixelization/delaunay` | 2026-04-10 | 40d **STALE** | broadcast shape mismatch (2,2) vs (1032,1032) in Delaunay interferometer |
| autolens_workspace | `multi/features/wavelength_dependence/modeling` | 2026-04-10 | 40d **STALE** | autofit.exc.FitException in multi-wavelength modeling |
| autolens_workspace_test | `database/scrape/general` | 2026-04-27 | 23d | PyAutoGalaxy abstract_fit.linear_light_profile_intensity_dict raises "TypeError: __hash__ method should return an integer" during subplot_fit_imaging after the search completes (a light-profile object's __hash__ returns a non-int). Surfaced once the dataset_label="build" path fix let the script progress past Imaging.from_fits. |
| autolens_workspace_test | `imaging/visualization` | 2026-04-10 | 40d **STALE** | AssertionError: dataset.png missing after visualization refactor |
| autolens_workspace_test | `jax_grad/imaging_lp` | 2026-04-10 | 40d **STALE** | JAX traceback in gradient computation for light profile |
| autolens_workspace_test | `jax_grad/imaging_mge` | 2026-04-10 | 40d **STALE** | AssertionError: Gradient is all zeros in MGE gradient computation |
| autolens_workspace_test | `jax_likelihood_functions/imaging/delaunay_mge` | 2026-04-10 | 40d **STALE** | timeout in JAX likelihood function benchmark |
| autolens_workspace_test | `jax_likelihood_functions/imaging/mge_group` | 2026-04-10 | 40d **STALE** | timeout in JAX likelihood function benchmark |

## Summary

| Passed | Failed | Skipped | Timeout |
|--------|--------|---------|---------|
| 504 | 8 | 64 | 2 |

## Per-Project Breakdown

| Project | Passed | Failed | Skipped | Timeout | Duration |
|---------|--------|--------|---------|---------|----------|
| autofit | 24 | 0 | 6 | 0 | 80.2s |
| autofit_test | 30 | 1 | 2 | 1 | 439.4s |
| autogalaxy | 105 | 1 | 13 | 0 | 643.4s |
| autogalaxy_test | 52 | 1 | 0 | 0 | 888.6s |
| autolens | 219 | 3 | 29 | 0 | 1828.0s |
| autolens_test | 74 | 2 | 14 | 1 | 1829.7s |

## Slowest scripts (top 25)

| Script | Project | Status | Duration | Share |
|--------|---------|--------|----------|-------|
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/modeling_visualization_jit.py` | autolens_test | timeout | 300.1s | 5.3% |
| `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/features/grid_search_parallel.py` | autofit_test | timeout | 300.0s | 5.3% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/datacube/delaunay.py` | autolens_test | passed | 163.8s | 2.9% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/point_source/modeling_visualization_jit.py` | autolens_test | passed | 103.4s | 1.8% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/subhalo.py` | autolens_test | passed | 90.6s | 1.6% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/multi/mge_group.py` | autolens_test | passed | 65.8s | 1.2% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_mge.py` | autolens_test | passed | 63.5s | 1.1% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/multi/start_here.py` | autolens | passed | 58.6s | 1.0% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/delaunay_mge.py` | autolens_test | passed | 56.6s | 1.0% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/delaunay_mge.py` | autogalaxy_test | passed | 54.7s | 1.0% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/profiles/light_and_mass_profiles.py` | autolens | passed | 52.3s | 0.9% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/start_here.py` | autolens | passed | 51.7s | 0.9% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/start_here.py` | autolens | passed | 49.7s | 0.9% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/imaging/visualization.py` | autogalaxy_test | passed | 47.1s | 0.8% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/delaunay_mge.py` | autogalaxy_test | passed | 47.1s | 0.8% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/multi/mge_group.py` | autogalaxy_test | passed | 45.4s | 0.8% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/units/flux.py` | autolens | passed | 45.3s | 0.8% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/visualization_jax.py` | autolens_test | passed | 42.3s | 0.7% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/multi/delaunay_mge.py` | autogalaxy_test | passed | 40.6s | 0.7% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular_mge.py` | autolens_test | passed | 40.4s | 0.7% |
| `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/prior_correctness/emcee_gaussian_bias_check.py` | autofit_test | passed | 40.2s | 0.7% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/los_halos/simulator.py` | autolens | passed | 38.3s | 0.7% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular_dspl.py` | autolens_test | passed | 37.7s | 0.7% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular.py` | autolens_test | passed | 37.2s | 0.7% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/delaunay.py` | autolens_test | passed | 37.2s | 0.7% |

## Failures by Classification

### Source Code Bugs (7)

- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/searches/BlackJAXNUTS.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/searches/BlackJAXNUTS.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  /home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:173: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autofit_workspace_test matches the installed library version (2026.5.14.2): no `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/searches/BlackJAXNUTS.py", line 120, in <module>
    abs(mp.normalization - 25.0) < 5.0
AssertionError: normalization off by too much: 1.0
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_assertions/convolver_mixed_precision.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_assertions/convolver_mixed_precision.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
      raise exc.ArrayException(
autoarray.exc.ArrayException: 
                The input array is 2D but not the same dimensions as the mask.

                This indicates the mask's shape is different to the input array shape.

                The shapes of the two arrays (which this exception is raised because they are different) are as follows:

                Input array_2d shape = (80, 80)
                Input mask_2d shape_native = (15, 15)
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/double_einstein_ring/slam.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/double_einstein_ring/slam.py']' returned non-zero exit status 1.
  - **Recently modified** in [feat: add interferometer extra_galaxies feature scripts](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/82)
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
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/models.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/models.py']' returned non-zero exit status 1.
  - **Recently modified** in [feat(cluster): adopt named-galaxy CSV API across all cluster scripts](https://github.com/PyAutoLabs/autolens_workspace/pull/189)
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
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/nufft.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/nufft.py']' returned non-zero exit status 1.
  - **Recently modified** in [fix(interferometer): correct sparse curvature for Pmax > 1 (Delaunay)](https://github.com/PyAutoLabs/PyAutoArray/pull/316)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/nufft.py:352: UserWarning: Data has no positive values, and therefore cannot be log-scaled.
  axes[2].set_yscale("log")
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/nufft.py", line 493, in <module>
    distance < 5.0
AssertionError: Round-trip dirty-image peak too far from original peak: 5.00 px
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_dspl.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_dspl.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
    File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 921, in assert_array_compare
    raise AssertionError(msg)
AssertionError: 
Not equal to tolerance rtol=0.0001, atol=0
rectangular_dspl: JAX vmap likelihood mismatch
Mismatched elements: 1 / 1 (100%)
Max absolute difference among violations: 101.99460561
Max relative difference among violations: 0.02685672
 ACTUAL: array([-3695.737222])
 DESIRED: array(-3797.731828)
  ```
  </details>

### Timeouts (2)

- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/features/grid_search_parallel.py`
  - Timed out after 300s
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/modeling_visualization_jit.py`
  - Timed out after 300s

### Known Numerical Issues (1)

- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/multi_gaussian_expansion/likelihood_function.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/multi_gaussian_expansion/likelihood_function.py']' returned non-zero 
  - **Recently modified** in [fix(interferometer): correct sparse curvature for Pmax > 1 (Delaunay)](https://github.com/PyAutoLabs/PyAutoArray/pull/316)
  - **Recently modified** in [fix(mass_stellar_dark): drop assertions, rename alpha→deflections](https://github.com/PyAutoLabs/autolens_workspace/pull/192)
  - **Recently modified** in [feat(cluster): step-by-step likelihood_function.py walkthrough](https://github.com/PyAutoLabs/autolens_workspace/pull/191)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  
The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/multi_gaussian_expansion/likelihood_function.py", line 309, in <module>
    reconstruction = ag.util.inversion.reconstruction_positive_only_from(
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/inversion/inversion/inversion_util.py", line 334, in reconstruction_positive_only_from
    raise exc.InversionException() from e
autoarray.exc.InversionException
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
| `modeling.py` | NEEDS_FIX 2026-04-10 - LinAlgError: matrix not positive definite in interferometer pixelization modeling |
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
| `imaging_lp.py` | NEEDS_FIX 2026-04-10 - JAX traceback in gradient computation for light profile |
| `imaging_mge.py` | NEEDS_FIX 2026-04-10 - AssertionError: Gradient is all zeros in MGE gradient computation |
| `delaunay_mge.py` | NEEDS_FIX 2026-04-10 - timeout in JAX likelihood function benchmark |
| `mge_group.py` | NEEDS_FIX 2026-04-10 - timeout in JAX likelihood function benchmark |

## Changes Since Last Release

### [perf: direct-ndtr fast path for TruncatedGaussianPrior.value_for](https://github.com/PyAutoLabs/PyAutoFit/pull/1285) (PyAutoLabs/PyAutoFit)
**API Changes:** None — internal implementation change only. `TruncatedGaussianPrior.value_for`
and `TruncatedNormalMessage.value_for` retain identical signatures and
docstring behaviour. Their bodies now delegate to the new private helper
`autofit.mapper.prior._erf_helpers.truncated_normal_value_for`, which is
not 

### [fix: coerce figure_of_metric return to Python float for Drawer + JAX](https://github.com/PyAutoLabs/PyAutoFit/pull/1283) (PyAutoLabs/PyAutoFit)
**API Changes:** None — internal bugfix only.
See full details below.

### [revert: default use_jax_for_visualization to False (reverts #1278)](https://github.com/PyAutoLabs/PyAutoFit/pull/1280) (PyAutoLabs/PyAutoFit)
**API Changes:** `Analysis.__init__(use_jax_for_visualization)` default flips back from `Optional[bool] = None` (follow `use_jax`) to `bool = False`. The sentinel-resolution block is dropped. Users wanting JIT visualization must pass `use_jax_for_visualization=True` explicitly. The existing `use_jax_for_visualizatio

### [feat: default use_jax_for_visualization to follow use_jax in Analysis.__init__](https://github.com/PyAutoLabs/PyAutoFit/pull/1278) (PyAutoLabs/PyAutoFit)
**API Changes:** - `Analysis.__init__(use_jax_for_visualization=...)` default changes from
  `False` → `None`. Type annotation widens from `bool` to `Optional[bool]`.
- When `use_jax=True` and no explicit visualization flag is given, the JIT
  visualization path is now ON by default (previously had to be opted into)

### [feat: autofit[nss] install extra (Phase 4 of nss_first_class_sampler)](https://github.com/PyAutoLabs/PyAutoFit/pull/1277) (PyAutoLabs/PyAutoFit)
**API Changes:** Pure additive at the install layer (`autofit[nss]` extra). The af.NSS `ImportError` message changes to reference the new install command. No code-API changes.
See full details below.

<details>
<summary>Full API Changes (for automation & release notes)</summary>

### Added
- `autofit[nss]` install e

### [feat: af.NSS checkpoint/resume + on-the-fly visualization (Phases 2-3)](https://github.com/PyAutoLabs/PyAutoFit/pull/1274) (PyAutoLabs/PyAutoFit)
**API Changes:** Pure additive at the kwarg level (`checkpoint_interval=100`); `iterations_per_quick_update` was already accepted in Phase 1 and is now functional. New module-level helpers `_save_checkpoint` / `_load_checkpoint` and a new `_NSSInternal` repackaging step. No existing API touched.
See full details bel

### [feat: af.NSS NonLinearSearch wrapper for Nested Slice Sampling (Phase 1 of nss_first_class_sampler)](https://github.com/PyAutoLabs/PyAutoFit/pull/1272) (PyAutoLabs/PyAutoFit)
**API Changes:** Added `af.NSS` (Nested Slice Sampling) as a new public sampler at the top level, plus `NSSamples` as the corresponding posterior-samples class. Pure addition — no existing classes / signatures / behaviours change. The `nss` import is optional and guarded; `import autofit` continues to work without i

### [fix: dedupe number_of_cores in Drawer for from_dict round-trip](https://github.com/PyAutoLabs/PyAutoFit/pull/1270) (PyAutoLabs/PyAutoFit)
**API Changes:** None — internal bugfix only.

### [fix: log_prior_from_value sign convention — density form across Prior subclasses](https://github.com/PyAutoLabs/PyAutoFit/pull/1269) (PyAutoLabs/PyAutoFit)
**API Changes:** `Prior.log_prior_from_value` is a behaviour change, not a signature change. The kwarg surface is unchanged (`(value, xp=np)`). Returned values are sign-flipped on the JAX-family priors and replaced with the correct density-form expression on `LogUniformPrior`. The normalisation constants `-log(σ · √

### [feat(grids): add respect_small_datasets kwarg to Grid2D.uniform](https://github.com/PyAutoLabs/PyAutoArray/pull/327) (PyAutoLabs/PyAutoArray)
**API Changes:** Adds one optional kwarg `respect_small_datasets: bool = True` to `aa.Grid2D.uniform`. No removed or renamed symbols; existing callers continue to work without change.
See full details below.

### [fix(mask): cap radius under PYAUTO_SMALL_DATASETS](https://github.com/PyAutoLabs/PyAutoArray/pull/325) (PyAutoLabs/PyAutoArray)
**API Changes:** None — internal behaviour change only. Under `PYAUTO_SMALL_DATASETS=1`, `Mask2D.circular` now also clamps `radius` to `min(shape_native) * pixel_scales / 2.0`. Outside that env var the function is unchanged.

See full details below.

### [feat: add zoom_extent_scale to Mapper.extent_from for Mid Zoom panel](https://github.com/PyAutoLabs/PyAutoArray/pull/324) (PyAutoLabs/PyAutoArray)
**API Changes:** - `Mapper.extent_from(...)` gains an optional `zoom_extent_scale: float = 1.0` argument. Default behaviour is unchanged.
- `plot_inversion_reconstruction(...)` and `plot_mapper(...)` gain the same passthrough kwarg.
- When `zoom_extent_scale > 1.0`, the returned extent is the brightest-region extent

### [feat: RectangularRotatedAdaptImage — PCA rotation fixes multi-source ghost-peak failure](https://github.com/PyAutoLabs/PyAutoArray/pull/323) (PyAutoLabs/PyAutoArray)
**API Changes:** Purely additive — no existing class, function, or signature changed:

- New mesh class `aa.mesh.RectangularRotatedAdaptImage(shape, weight_power, weight_floor, spline_deg)` — opt-in subclass of `RectangularSplineAdaptImage`.
- New module `autoarray.inversion.mesh.interpolator.density_components` wit

### [fix(inversion): make AbstractMeshGeometry picklable (xp module → _use_jax bool + property)](https://github.com/PyAutoLabs/PyAutoArray/pull/321) (PyAutoLabs/PyAutoArray)
**API Changes:** - `AbstractMeshGeometry.__init__(xp=np)` continues to accept the same `xp=` kwarg — no caller changes needed.
- The instance no longer holds `_xp` as a module attribute; it holds `_use_jax: bool` and exposes `_xp` as a `@property` that returns `numpy` or `jax.numpy` on demand.
- All existing `self._

### [Reduce critical curves and caustics overlay linewidth from 2 to 1](https://github.com/PyAutoLabs/PyAutoArray/pull/319) (PyAutoLabs/PyAutoArray)
**API Changes:** None — internal styling tweak only. No public symbols added, removed, renamed, or re-signatured; the `lines=` parameter and all call sites in PyAutoGalaxy / PyAutoLens are unchanged. Behaviour change is limited to rendered line thickness.
See full details below.

### [Add KNNBarycentric mesh: JAX-native Delaunay-class interpolator](https://github.com/PyAutoLabs/PyAutoArray/pull/318) (PyAutoLabs/PyAutoArray)
**API Changes:** Purely additive:

- New `aa.mesh.KNNBarycentric(pixels=...)` mesh class, inherits from
  `KNearestNeighbor` (so all the existing kNN regularization-spacing
  knobs work) but selects the new interpolator.
- New `InterpolatorKNNBarycentric` (not exported at `aa.` top level,
  same as `InterpolatorKNea

### [fix(interferometer): correct sparse curvature for Pmax > 1 (Delaunay)](https://github.com/PyAutoLabs/PyAutoArray/pull/316) (PyAutoLabs/PyAutoArray)
**API Changes:** The interferometer sparse operator now exposes the same API surface as the imaging operator: `apply_operator(F)` + `curvature_matrix_diag_from(rows, cols, vals, *, S)`. The old `curvature_matrix_via_sparse_operator_from(pix_indexes, pix_weights, pix_pixels, fft_index)` shape-array signature is gone.
**Scripts Changed:** None in this library PR. Workspace follow-up coming in a separate `/ship_workspace` PR for `autolens_workspace_test`:

- `scripts/jax_assertions/sparse_operators.py` — switch the Pmax=1 call to the new `curvature_matrix_diag_from(rows, cols, vals, S)` API.
- `scripts/jax_likelihood_functions/interfe

### [fix(interferometer-sparse): guard against Delaunay mappers (issue #314)](https://github.com/PyAutoLabs/PyAutoArray/pull/315) (PyAutoLabs/PyAutoArray)
**API Changes:** `InversionInterferometerSparse.curvature_matrix_diag` (and therefore `curvature_matrix`, `data_vector`, and any downstream method that materialises the curvature) now raises `NotImplementedError` when constructed with a Delaunay-mesh mapper. Users running `Interferometer.apply_sparse_operator(...)` 

### [fix(lens_calc): preserve evaluation_grid extent under PYAUTO_SMALL_DATASETS=1](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/431) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** None — internal change only. Public `LensCalc.tangential_critical_curve_list_from`, `radial_critical_curve_list_from`, caustic and area variants now correctly return curves under `PYAUTO_SMALL_DATASETS=1` (previously returned `[]`).
See full details below.

### [fix: handle r=0 in NFWSph deflections](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/430) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** None. `NFWSph.deflections_yx_2d_from(grid)` signature and return type unchanged; only the behaviour at r=0 changes (NaN → 0).

### [fix(csv): preserve TuplePrior on af.Model built from tuple-param rows](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/429) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** None — internal change to the construction logic inside
`galaxy_af_models_from_csv_tables`. Existing callers that don't override
tuple-component priors after construction see no behaviour difference; callers
that *do* (the cluster modeling scripts) now succeed instead of raising
`TypeError` at sampl

### [feat(galaxy): named-galaxy CSV reader/writer for full model round-trips](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/428) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** Two new public dataclasses (`GalaxyModelRow`, `GalaxyModelTable`) and four public functions (`galaxy_models_to_csv`, `galaxy_models_from_csv`, `galaxies_from_csv_tables`, `galaxy_af_models_from_csv_tables`). One CSV per profile family (`mass` / `light` / `point`); profile classes dispatch via `getat

### [fix: EllipseMultipoleScaled JAX-traceable via deferred derivation](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/427) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** `EllipseMultipoleScaled.__init__` no longer pre-computes or stores `self.specific_multipole_comps`; the attribute is gone. `super().__init__` is no longer called, so `self.multipole_comps` is also no longer set. `get_shape_angle` is now overridden (was inherited) to derive from `scaled_multipole_com

### [fix: Basis.image_2d_from and dPIEPotential.convergence_2d_from return wrong wrapper types](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/425) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** None — return-type fix only. `Basis.image_2d_from` and
`dPIEPotential.convergence_2d_from` already advertised `aa.Array2D` return types in their
annotations; this PR makes the runtime behaviour match. Any caller that already relies on
the (incorrect) `numpy.ndarray` / `VectorYX2D` returns will see a

### [config: add prior defaults for ExternalPotential](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/423) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** None — config-only addition. See full details below.

### [feat(mass): add ExternalPotential mass profile (Powell 2022 Eq 4)](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/422) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** Single additive class: `ag.mp.ExternalPotential` (sibling of `ExternalShear` in `autogalaxy/profiles/mass/sheets/`). Six free parameters (`gamma_1/2`, `tau_1/2`, `delta_1/2`) plus a free `centre` (unlike `ExternalShear`'s fixed `(0, 0)` — the τ and δ deflections are radial so the centre matters). Pl

### [refactor(light): split multipole module + add ag.lp_linear variants](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/421) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** Two new public classes added to ``ag.lp_linear``:

- ``ag.lp_linear.SersicMultipole`` — linear elliptical Sersic with m=3/m=4 multipole perturbations
- ``ag.lp_linear.GaussianMultipole`` — linear elliptical Gaussian with m=3/m=4 multipole perturbations

Standard classes (``ag.lp.SersicMultipole`` / 

### [feat: re-export galaxy_model_csv helpers under al.*](https://github.com/PyAutoLabs/PyAutoLens/pull/526) (PyAutoLabs/PyAutoLens)
**API Changes:** Six new re-exports: `al.GalaxyModelRow`, `al.GalaxyModelTable`, `al.galaxy_models_from_csv`, `al.galaxy_models_to_csv`, `al.galaxies_from_csv_tables`, `al.galaxy_af_models_from_csv_tables`. All point to the corresponding `autogalaxy.galaxy.galaxy_model_csv` symbols. See the upstream PyAutoGalaxy PR 

### [feat(weak): FitWeak class + plotters (#524)](https://github.com/PyAutoLabs/PyAutoLens/pull/525) (PyAutoLabs/PyAutoLens)
**API Changes:** Pure additions. One new class (`autolens.weak.FitWeak`) and four new module-level plot helpers (`plot_data_vs_model`, `plot_residuals`, `plot_chi_squared_map`, `subplot_fit_weak`), all re-exported into `autolens.plot` and accessible at the top level as `al.FitWeak`. See full details below.

### [feat(weak): aplt plotters for WeakDataset shear catalogues (#496)](https://github.com/PyAutoLabs/PyAutoLens/pull/523) (PyAutoLabs/PyAutoLens)
**API Changes:** Pure additions — no removals, no signature changes. Five new public functions on the `aplt` namespace for weak-lensing shear-catalogue visualisation. See full details below.

### [docs(api): sync mass.rst with full al.mp namespace + lmp / lmp_linear](https://github.com/PyAutoLabs/PyAutoLens/pull/520) (PyAutoLabs/PyAutoLens)
**API Changes:** None — docs-only change. No Python code is modified, no symbols added or removed. The new
autosummary entries point at classes that already exist in `autogalaxy.profiles.mass.*`,
`autogalaxy.profiles.light_and_mass_profiles`, and
`autogalaxy.profiles.light_linear_and_mass_profiles`, and are already 

### [feat: redesign subplot_fit panels — add Source Plane (Mid Zoom)](https://github.com/PyAutoLabs/PyAutoLens/pull/518) (PyAutoLabs/PyAutoLens)
**API Changes:** - `_plot_source_plane(...)` and `plane_image_from(...)` gain a `zoom_extent_scale` kwarg. `plane_image_from` also gains a `zoom_extent_bounds` kwarg.
- `subplot_fit` and `subplot_fit_log10` produce the new 12-panel layout — same panel count, different ordering, one renamed panel ("Source Plane (Zoom

### [docs(api): sync light profile reference with PyAutoGalaxy](https://github.com/PyAutoLabs/PyAutoLens/pull/516) (PyAutoLabs/PyAutoLens)
**API Changes:** None — docs-only change. No Python code is modified, no symbols added or removed. The
new autosummary entries point at classes that already exist in
`autogalaxy.profiles.light.*` and are already re-exported by `autolens` as
`al.lp_linear`, `al.lp_operated`, `al.lp_basis`.
See full details below.

### [docs(api): list SersicMultipole and GaussianMultipole in autosummary](https://github.com/PyAutoLabs/PyAutoLens/pull/515) (PyAutoLabs/PyAutoLens)
**API Changes:** None — pure documentation entries.

### [feat(AnalysisImaging): plumb dataset_model into adapt_images_via_instance_from](https://github.com/PyAutoLabs/PyAutoLens/pull/512) (PyAutoLabs/PyAutoLens)
**Scripts Changed:** None beyond the test file.

### [chore(scripts): Phase 3 use_jax=True consistency in features/search_chaining](https://github.com/PyAutoLabs/autofit_workspace/pull/61) (PyAutoLabs/autofit_workspace)
**Scripts Changed:** - `scripts/features/search_chaining.py` — added `use_jax=True` to all 4 `af.ex.Analysis(...)` calls so the chained pipeline runs the same JAX path as the grid-search sibling

### [feat: add af.NSS section to searches/nest.py tutorial (Phase 5)](https://github.com/PyAutoLabs/autofit_workspace/pull/60) (PyAutoLabs/autofit_workspace)
**Scripts Changed:** - `scripts/searches/nest.py` — added a new **Search: NSS** section after the existing Nautilus section walking through the NSS-specific kwargs (`n_live`, `num_mcmc_steps`, `num_delete`, `termination`, `checkpoint_interval`, `iterations_per_quick_update`); extended the top docstring + Contents block 

### [Disable model.graph output by default](https://github.com/PyAutoLabs/autofit_workspace/pull/56) (PyAutoLabs/autofit_workspace)
**Scripts Changed:** - None — config-only change to `config/output.yaml`.

### [docs: render __Contents__ blocks as Markdown lists](https://github.com/PyAutoLabs/autofit_workspace/pull/54) (PyAutoLabs/autofit_workspace)
**Scripts Changed:** 1 script — `scripts/cookbooks/model.py` had a single un-bulleted `**Models:**` heading inside its `__Contents__` block. Most of this repo's tutorial scripts were already bulleted (28 files); only this one needed the fix.

### [fix(interferometer): use TransformerDFT for sparse-operator preparation script](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/90) (PyAutoLabs/autogalaxy_workspace)
**Scripts Changed:** - `scripts/interferometer/features/pixelization/many_visibilities_preparation.py` — `transformer_class=ag.TransformerNUFFT` → `ag.TransformerDFT` to unblock `apply_sparse_operator`.

### [Remove basis regularization section from MGE + shapelets modeling.py](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/89) (PyAutoLabs/autogalaxy_workspace)
**Scripts Changed:** - `scripts/imaging/features/multi_gaussian_expansion/modeling.py` — removed the regularization section, replaced with a 7-line pointer paragraph to `autolens_workspace_developer/basis_regularization/mge_galaxy.py`
- `scripts/imaging/features/shapelets/modeling.py` — removed the regularization sectio

### [docs: refresh Basis demo in profiles/light.py after #425](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/88) (PyAutoLabs/autogalaxy_workspace)
**Scripts Changed:** - `scripts/guides/profiles/light.py` — Basis section: swap four `ag.lp_linear.Gaussian`
  constituents for four `ag.lp.Gaussian` with explicit decreasing intensities; drop the
  `basis_galaxy = ag.Galaxy(...)` wrap; plot `basis.image_2d_from(grid=grid)` directly;
  rewrite the surrounding prose for 

### [docs: reorder Multipole section in light profiles guide](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/87) (PyAutoLabs/autogalaxy_workspace)
**Scripts Changed:** - `scripts/guides/profiles/light.py` — Multipole section moved to follow Model Instance; `__Contents__` reordered; small wording tweaks to forward-references
- `.script_sizes.json` — refreshed snapshot

### [docs: add light profiles guide at scripts/guides/profiles/light.py](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/86) (PyAutoLabs/autogalaxy_workspace)
**Scripts Changed:** - `scripts/guides/profiles/__init__.py` — new, empty package marker
- `scripts/guides/profiles/light.py` — new guide (~530 lines, full 10-section walk-through)
- `.script_sizes.json` — refreshed to record the new files

### [feat: add interferometer extra_galaxies feature scripts](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/82) (PyAutoLabs/autogalaxy_workspace)
**Scripts Changed:** New scripts in `scripts/interferometer/features/extra_galaxies/`:

- `__init__.py`, `README.md` — package + folder docs. README explains the autogalaxy-vs-autolens role split (autogalaxy fits *light* of extras; autolens fits their *mass*).
- `simulator.py` — `ag.SimulatorInterferometer` produces a d

### [feat: add interferometer shapelets feature scripts (+ pad imaging)](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/79) (PyAutoLabs/autogalaxy_workspace)
**Scripts Changed:** New scripts in `scripts/interferometer/features/shapelets/`:

- `__init__.py`, `README.md` — package + folder docs (including a section on why the positive-negative solver is required).
- `modeling.py` — full Nautilus model-fit. Single galaxy with a polar shapelet bulge built from `ag.lp_linear.Shap

### [Remove basis regularization section from MGE + shapelets modeling.py](https://github.com/PyAutoLabs/autolens_workspace/pull/193) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/imaging/features/multi_gaussian_expansion/modeling.py` — removed the regularization section, replaced with a 7-line pointer paragraph to `autolens_workspace_developer/basis_regularization/mge_lens.py`
- `scripts/imaging/features/advanced/shapelets/modeling.py` — removed the regularization

### [fix(mass_stellar_dark): drop assertions, rename alpha→deflections](https://github.com/PyAutoLabs/autolens_workspace/pull/192) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/imaging/features/advanced/mass_stellar_dark/fit.py` — 5 `alpha_*` → `deflections_*`, 5 prints updated, 1 assert removed.
- `scripts/imaging/features/advanced/mass_stellar_dark/likelihood_function.py` — 4 `alpha_*` → `deflections_*`, 4 prints updated, 1 assert removed.

### [feat(cluster): step-by-step likelihood_function.py walkthrough](https://github.com/PyAutoLabs/autolens_workspace/pull/191) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/cluster/likelihood_function.py` — **NEW**, ~780 lines. Walks through every step of the cluster point-source log-likelihood, then validates each piece against `al.FitPositionsSource` and `al.FitPositionsImagePair`. Both validations match exactly. Per-section breakdown:
  - **Setup**: load 

### [feat(cluster): adopt named-galaxy CSV API across all cluster scripts](https://github.com/PyAutoLabs/autolens_workspace/pull/189) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/cluster/csv_api.py` — **NEW** pedagogical guide. Builds a cluster model in plain Python, writes it to family CSVs via `al.galaxy_models_to_csv`, reads it back, prints the round-trip, and constructs `af.Model[Galaxy]` instances ready for non-linear search. Also documents `point_datasets.cs

### [feat: scaling-relation members as default in cluster scripts](https://github.com/PyAutoLabs/autolens_workspace/pull/185) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/cluster/simulator.py` — added 10 scaling members with truth values `scaling_factor = 0.3` and `scaling_exponent = 1.0`; emits `scaling_galaxies.csv` via `al.galaxy_table_to_csv`. Adaptive over-sampling now covers all scaling-member centres.
- `scripts/cluster/modeling.py` — loads `scaling

### [docs: refresh Basis + dPIEPotential examples after #425](https://github.com/PyAutoLabs/autolens_workspace/pull/183) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/guides/profiles/light.py` — Basis section: swap four `al.lp_linear.Gaussian`
  constituents for four `al.lp.Gaussian` with explicit decreasing intensities; drop the
  `basis_galaxy = al.Galaxy(...)` wrap; plot `basis.image_2d_from(grid=grid)` directly;
  rewrite the surrounding prose for 

### [docs: add stellar + dark + lmp light-and-mass profiles guide](https://github.com/PyAutoLabs/autolens_workspace/pull/181) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/guides/profiles/light_and_mass_profiles.py` — new ~751-line guide (11 sections
  mirroring `light.py` / `mass.py` flow)
- `.script_sizes.json` — refreshed to record the new file

### [docs: add mass profiles guide at scripts/guides/profiles/mass.py](https://github.com/PyAutoLabs/autolens_workspace/pull/179) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/guides/profiles/mass.py` — new ~620-line guide (10-section walk-through mirrored
  with `light.py`; uses `convergence_2d_from` / `deflections_yx_2d_from` /
  `potential_2d_from` rather than `image_2d_from`)
- `.script_sizes.json` — refreshed to record the new file
