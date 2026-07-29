# Release Readiness Report

**Status: NOT READY**

**Run:** `2026-07-08T11-25-50Z`  •  **Path:** `/home/jammy/Code/PyAutoLabs/PyAutoBuild/test_results/runs/2026-07-08T11-25-50Z`  •  **Total duration:** 11883.0s

## Slow-Skipped Scripts (needs performance fix)

**22 script(s)** are being skipped because they exceed the 60s per-script timeout cap. These are NOT permanent skips — they need the underlying performance issue fixed and the `SLOW` marker removed from the workspace's `config/build/no_run.yaml`.

| Workspace | Script | Marked | Age | Reason |
|-----------|--------|--------|-----|--------|
| HowToGalaxy | `guides/results/database/start_here` | 2026-04-10 | 89d **STALE** | previously failed fast on a broken aggregator query; now runs the real aggregator and exceeds 60s |
| HowToGalaxy | `guides/results/examples/galaxies_fit` | 2026-04-10 | 89d **STALE** | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| HowToGalaxy | `guides/results/examples/models` | 2026-04-10 | 89d **STALE** | cascade from SLOW-skipped results/start_here.py; aggregator returns NoneType so instance.galaxies is None |
| HowToGalaxy | `guides/results/examples/samples` | 2026-04-10 | 89d **STALE** | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| HowToGalaxy | `guides/results/start_here` | 2026-04-10 | 89d **STALE** | exceeds 60s test timeout; unsets TEST_MODE to produce real samples for downstream examples |
| HowToGalaxy | `guides/results/workflow/csv_make` | 2026-04-10 | 89d **STALE** | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| HowToLens | `guides/results/database/start_here` | 2026-04-10 | 89d **STALE** | previously failed fast on a broken aggregator query; now runs the real aggregator and exceeds 60s |
| HowToLens | `guides/results/examples/queries` | 2026-04-10 | 89d **STALE** | cascade from SLOW-skipped results/start_here.py; stub Model lacks sersic_index attribute |
| HowToLens | `guides/results/examples/samples` | 2026-04-10 | 89d **STALE** | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| HowToLens | `guides/results/examples/samples_via_aggregator` | 2026-04-10 | 89d **STALE** | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| HowToLens | `howtolens/chapter_4_pixelizations/tutorial_10_brightness_adaption` | 2026-04-10 | 89d **STALE** | pixelization tutorial exceeds 60s test timeout |
| autogalaxy_workspace | `guides/results/database/start_here` | 2026-04-10 | 89d **STALE** | previously failed fast on a broken aggregator query; now runs the real aggregator and exceeds 60s |
| autogalaxy_workspace | `guides/results/workflow/csv_make` | 2026-04-10 | 89d **STALE** | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| autolens_workspace | `guides/results/database/start_here` | 2026-04-10 | 89d **STALE** | previously failed fast on a broken aggregator query; now runs the real aggregator and exceeds 60s |
| autolens_workspace_test | `database/scrape/multi_analysis` | 2026-04-10 | 89d **STALE** | exceeds 60s timeout; _test workspaces run full searches without test mode |
| autolens_workspace_test | `database/scrape/slam_general` | 2026-04-10 | 89d **STALE** | exceeds 60s timeout; _test workspaces run full searches without test mode |
| autolens_workspace_test | `database/scrape/slam_multi_one_by_one` | 2026-04-10 | 89d **STALE** | exceeds 60s timeout; _test workspaces run full searches without test mode |
| autolens_workspace_test | `database/scrape/slam_pix` | 2026-04-10 | 89d **STALE** | exceeds 60s timeout; _test workspaces run full searches without test mode |
| autolens_workspace_test | `imaging/modeling_visualization_jit` | 2026-05-07 | 62d **STALE** | JIT + full visualization pipeline exceeds 300s cap (autogalaxy variant ~90s); unblocked by PR #70 from prior `expected jax.Array, got numpy.float64` AssertionError, now hits perf wall |
| autolens_workspace_test | `imaging/modeling_visualization_jit_delaunay` | 2026-05-07 | 62d **STALE** | JIT + full visualization pipeline exceeds 300s cap; same root cause as modeling_visualization_jit |
| autolens_workspace_test | `imaging/modeling_visualization_jit_rectangular` | 2026-05-07 | 62d **STALE** | JIT + full visualization pipeline exceeds 301s cap; same root cause as modeling_visualization_jit |
| autolens_workspace_test | `interferometer/modeling_visualization_jit` | 2026-05-20 | 49d **STALE** | JIT + full visualization pipeline exceeds 300s cap; same root cause as imaging/modeling_visualization_jit family |

## Needs-Fix Scripts (parked for investigation)

**36 script(s)** are being skipped because they are broken and parked as a to-do list. These are NOT permanent skips — investigate the failure, fix the underlying bug, and remove the `NEEDS_FIX` marker from the workspace's `config/build/no_run.yaml`.

| Workspace | Script | Marked | Age | Reason |
|-----------|--------|--------|-----|--------|
| HowToFit | `chapter_1_introduction/tutorial_5_results_and_samples` | 2026-04-10 | 89d **STALE** | IndexError in samples access, likely related to InstanceInterpolator bug in autofit features/interpolate |
| HowToGalaxy | `autogalaxy_workspace/scripts/imaging/modeling` | 2026-04-10 | 89d **STALE** | KeyError on ('galaxies','galaxy','bulge','ell_comps'...) kwargs after API drift in top-level imaging/modeling.py |
| HowToGalaxy | `ellipse/modeling` | 2026-04-10 | 89d **STALE** | KeyError on 'ellipses.0.centre_0' kwargs after API drift in ellipse model |
| HowToGalaxy | `guides/advanced/over_sampling` | 2026-04-10 | 89d **STALE** | plot_grid() got unexpected kwarg 'plot_grid_lines' after plotter API drift |
| HowToGalaxy | `howtogalaxy/chapter_4_pixelizations/tutorial_5_model_fit` | 2026-04-10 | 89d **STALE** | LinAlgError: matrix not positive definite in pixelization fit |
| HowToGalaxy | `imaging/data_preparation/manual/mask_irregular` | 2026-04-10 | 89d **STALE** | silent failure, needs investigation |
| HowToGalaxy | `imaging/features/pixelization/modeling` | 2026-04-10 | 89d **STALE** | LinAlgError: matrix not positive definite in pixelization modeling |
| HowToGalaxy | `interferometer/features/pixelization/modeling` | 2026-04-10 | 89d **STALE** | LinAlgError: matrix not positive definite in interferometer pixelization modeling |
| HowToLens | `group/slam` | 2026-04-10 | 89d **STALE** | PriorException: upper limit must be greater than lower limit in group SLaM pipeline |
| HowToLens | `howtolens/chapter_2_lens_modeling/tutorial_2_practicalities` | 2026-04-10 | 89d **STALE** | NameError: 'af' not defined; tutorial missing ~80 lines of imports + setup boilerplate (compare tutorial_1) |
| HowToLens | `howtolens/chapter_4_pixelizations/tutorial_2_mappers` | 2026-04-10 | 89d **STALE** | ValueError: zero-size array reduction, empty mapper array |
| HowToLens | `imaging/data_preparation/manual/mask_irregular` | 2026-04-10 | 89d **STALE** | silent failure, needs investigation |
| HowToLens | `imaging/features/pixelization/delaunay` | 2026-04-10 | 89d **STALE** | autofit.exc.FitException in Delaunay pixelization fit |
| HowToLens | `imaging/features/pixelization/slam` | 2026-04-10 | 89d **STALE** | autofit.exc.FitException in SLaM pixelization pipeline |
| HowToLens | `interferometer/features/pixelization/delaunay` | 2026-04-10 | 89d **STALE** | broadcast shape mismatch (2,2) vs (1032,1032) in Delaunay interferometer |
| HowToLens | `multi/features/wavelength_dependence/modeling` | 2026-04-10 | 89d **STALE** | autofit.exc.FitException in multi-wavelength modeling |
| autofit_workspace | `features/interpolate` | 2026-04-10 | 89d **STALE** | IndexError in InstanceInterpolator.__getitem__ when querying time == 1.5; value_map lookup falls through to empty instances list |
| autogalaxy_workspace | `autogalaxy_workspace/scripts/imaging/modeling` | 2026-04-10 | 89d **STALE** | KeyError on ('galaxies','galaxy','bulge','ell_comps'...) kwargs after API drift in top-level imaging/modeling.py |
| autogalaxy_workspace | `imaging/data_preparation/manual/mask_irregular` | 2026-04-10 | 89d **STALE** | silent failure, needs investigation |
| autogalaxy_workspace | `imaging/features/pixelization/modeling` | 2026-04-10 | 89d **STALE** | LinAlgError: matrix not positive definite in pixelization modeling |
| autogalaxy_workspace | `interferometer/features/multi_gaussian_expansion/likelihood_function` | 2026-05-20 | 49d **STALE** | LinAlgError: matrix singular in MGE inversion -> InversionException (known_numerical; same family as pixelization variants above) |
| autogalaxy_workspace | `interferometer/features/pixelization/modeling` | 2026-04-10 | 89d **STALE** | LinAlgError: matrix not positive definite in interferometer pixelization modeling |
| autolens_workspace | `group/features/advanced/double_einstein_ring/slam` | 2026-05-20 | 49d **STALE** | same cascade as imaging variant — synthetic samples_summary lacks adapt_data; parking pattern of the imaging entry didn't cover this group/ twin |
| autolens_workspace | `group/slam` | 2026-04-10 | 89d **STALE** | PriorException: upper limit must be greater than lower limit in group SLaM pipeline |
| autolens_workspace | `imaging/data_preparation/manual/mask_irregular` | 2026-04-10 | 89d **STALE** | silent failure, needs investigation |
| autolens_workspace | `imaging/features/advanced/double_einstein_ring/slam` | 2026-05-07 | 62d **STALE** | autofit.exc.FitException in SLaM bypass mode (same family as imaging/features/pixelization/slam — Adapt regularization needs adapt_data which the synthetic samples_summary doesn't carry; cascade goes deep, fixing in one PR isn't tractable) |
| autolens_workspace | `imaging/features/pixelization/delaunay` | 2026-04-10 | 89d **STALE** | autofit.exc.FitException in Delaunay pixelization fit |
| autolens_workspace | `imaging/features/pixelization/slam` | 2026-04-10 | 89d **STALE** | autofit.exc.FitException in SLaM pixelization pipeline |
| autolens_workspace | `interferometer/features/pixelization/delaunay` | 2026-04-10 | 89d **STALE** | broadcast shape mismatch (2,2) vs (1032,1032) in Delaunay interferometer |
| autolens_workspace | `multi/features/wavelength_dependence/modeling` | 2026-04-10 | 89d **STALE** | autofit.exc.FitException in multi-wavelength modeling |
| autolens_workspace_test | `database/scrape/general` | 2026-04-27 | 72d **STALE** | PyAutoGalaxy abstract_fit.linear_light_profile_intensity_dict raises "TypeError: __hash__ method should return an integer" during subplot_fit_imaging after the search completes (a light-profile object's __hash__ returns a non-int). Surfaced once the dataset_label="build" path fix let the script progress past Imaging.from_fits. |
| autolens_workspace_test | `imaging/visualization` | 2026-04-10 | 89d **STALE** | AssertionError: dataset.png missing after visualization refactor |
| autolens_workspace_test | `jax_grad/imaging_lp` | 2026-04-10 | 89d **STALE** | JAX traceback in gradient computation for light profile |
| autolens_workspace_test | `jax_grad/imaging_mge` | 2026-04-10 | 89d **STALE** | AssertionError: Gradient is all zeros in MGE gradient computation |
| autolens_workspace_test | `jax_likelihood_functions/imaging/delaunay_mge` | 2026-04-10 | 89d **STALE** | timeout in JAX likelihood function benchmark |
| autolens_workspace_test | `jax_likelihood_functions/imaging/mge_group` | 2026-04-10 | 89d **STALE** | timeout in JAX likelihood function benchmark |

## Summary

| Passed | Failed | Skipped | Timeout |
|--------|--------|---------|---------|
| 613 | 5 | 71 | 1 |

## Per-Project Breakdown

| Project | Passed | Failed | Skipped | Timeout | Duration |
|---------|--------|--------|---------|---------|----------|
| autofit | 26 | 0 | 6 | 0 | 112.6s |
| autofit_test | 35 | 0 | 2 | 0 | 189.7s |
| autogalaxy | 107 | 1 | 14 | 0 | 1079.7s |
| autogalaxy_test | 54 | 0 | 0 | 0 | 1798.7s |
| autolens | 221 | 1 | 30 | 1 | 3469.1s |
| autolens_test | 87 | 3 | 15 | 0 | 3640.7s |
| euclid | 5 | 0 | 0 | 0 | 393.3s |
| howtofit | 15 | 0 | 1 | 0 | 164.6s |
| howtogalaxy | 25 | 0 | 1 | 0 | 298.5s |
| howtolens | 38 | 0 | 2 | 0 | 736.3s |

## Slowest scripts (top 25)

| Script | Project | Status | Duration | Share |
|--------|---------|--------|----------|-------|
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/latent_variables.py` | autolens | timeout | 300.0s | 2.5% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/multi/mge_group.py` | autolens_test | passed | 298.8s | 2.5% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/_quick_fit.py` | autolens | passed | 202.7s | 1.7% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/galaxies_fits.py` | autolens | passed | 185.9s | 1.6% |
| `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_4_pixelizations/tutorial_10_brightness_adaption.py` | howtolens | passed | 184.4s | 1.6% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/visualization_jax.py` | autolens_test | failed | 163.8s | 1.4% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/subhalo.py` | autolens_test | passed | 143.6s | 1.2% |
| `/home/jammy/Code/PyAutoLabs/euclid_strong_lens_modeling_pipeline/scripts/lens_model_waveband.py` | euclid | passed | 138.3s | 1.2% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_dspl.py` | autolens_test | passed | 136.7s | 1.1% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_mge.py` | autolens_test | passed | 136.4s | 1.1% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/delaunay_mge.py` | autogalaxy_test | passed | 135.4s | 1.1% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/visualization.py` | autolens_test | passed | 130.9s | 1.1% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/multi/mge_group.py` | autogalaxy_test | passed | 128.5s | 1.1% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/multi/delaunay_mge.py` | autogalaxy_test | passed | 122.0s | 1.0% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/delaunay_mge.py` | autolens_test | passed | 107.5s | 0.9% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/delaunay_mge.py` | autogalaxy_test | passed | 102.0s | 0.9% |
| `/home/jammy/Code/PyAutoLabs/euclid_strong_lens_modeling_pipeline/scripts/mge_lens_only.py` | euclid | passed | 100.0s | 0.8% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular.py` | autolens_test | passed | 99.5s | 0.8% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/point_source/image_plane.py` | autolens_test | passed | 96.5s | 0.8% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/multi/start_here.py` | autolens | passed | 89.5s | 0.8% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/datacube/shared_preloads.py` | autolens_test | passed | 85.3s | 0.7% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/point_source/point.py` | autolens_test | passed | 85.0s | 0.7% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/delaunay.py` | autolens_test | passed | 82.7s | 0.7% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/visualization.py` | autolens_test | passed | 82.6s | 0.7% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular_mge.py` | autolens_test | passed | 81.3s | 0.7% |

## Failures by Classification

### Source Code Bugs (5)

- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/models.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/models.py']' returned non-zero exit status 1.
  - **Recently modified** in [fix: ensure aggregator helper results include datasets](https://github.com/PyAutoLabs/autolens_workspace/pull/221)
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
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/models.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/models.py']' returned non-zero exit status 1.
  - **Recently modified** in [fix: ensure aggregator helper results include datasets](https://github.com/PyAutoLabs/autolens_workspace/pull/221)
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
AssertionError: zero_contour warm call took 119.8 ms (> 100 ms) — closure cache-busting bug from PyAutoGalaxy #433 may have regressed
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/point_source/modeling_visualization_jit.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/point_source/modeling_visualization_jit.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  
If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/point_source/modeling_visualization_jit.py", line 182, in <module>
    assert _warm_dt < 0.1, (
           ^^^^^^^^^^^^^^
AssertionError: zero_contour warm call took 145.2 ms (> 100 ms) — closure cache-busting bug from PyAutoGalaxy #433 may have regressed
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/point_source/visualization_jax.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/point_source/visualization_jax.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  
If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/point_source/visualization_jax.py", line 173, in <module>
    assert _warm_dt < 0.1, (
           ^^^^^^^^^^^^^^
AssertionError: zero_contour warm call took 135.1 ms (> 100 ms) — closure cache-busting bug from PyAutoGalaxy #433 may have regressed
  ```
  </details>

### Timeouts (1)

- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/latent_variables.py`
  - Timed out after 300s
  - **Recently modified** in [docs(latent): migrate cookbooks to the Latent class API](https://github.com/PyAutoLabs/autofit_workspace/pull/72)
  - **Recently modified** in [docs(latent): migrate custom-latent examples to the Latent class (Phase 2)](https://github.com/PyAutoLabs/autolens_workspace/pull/219)

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

### [fix: LogUniform NumPy log-prior returns -inf for value<=0 (emcee NaN crash)](https://github.com/PyAutoLabs/PyAutoFit/pull/1329) (PyAutoLabs/PyAutoFit)
**API Changes:** Behaviour-only: `LogUniformPrior.log_prior_from_value(value)` now returns `-inf`
(was `NaN`/`+inf`) for `value <= 0` on the NumPy path. No signatures, symbols, or
defaults change; positive-value behaviour is identical. The only direct callers are
the `autofit_workspace_test` prior parity/regression 

### [docs: add signpost llms.txt + consolidate agent instructions into AGENTS.md](https://github.com/PyAutoLabs/PyAutoFit/pull/1320) (PyAutoLabs/PyAutoFit)
**API Changes:** None.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
**Scripts Changed:** None — docs only.

### [fix: skip latent computation without keys](https://github.com/PyAutoLabs/PyAutoFit/pull/1317) (PyAutoLabs/PyAutoFit)
**API Changes:** `Analysis.compute_latent_samples(...)` now returns `None` immediately when the analysis has no enabled latent keys, matching the existing no-latent contract instead of attempting an empty latent batch.
See full details below.

### [refactor(latent): first-class Latent class + engine extraction (Phase 1)](https://github.com/PyAutoLabs/PyAutoFit/pull/1315) (PyAutoLabs/PyAutoFit)
**API Changes:** No signature changes. New extension point `af.Latent` (declare `Analysis.Latent = ...`, override `keys`/`variables`). The legacy `Analysis.LATENT_KEYS` / `LATENT_BATCH_MODE` / `compute_latent_variables` still work — the default `Latent` delegates to them (back-compat shim).
See full details below.

### [Add optional arcsecond double-prime tick labels](https://github.com/PyAutoLabs/PyAutoArray/pull/350) (PyAutoLabs/PyAutoArray)
**API Changes:** Adds one optional config key, `visualize.general.ticks.symbol_over_decimal`, defaulting to `false`.
When enabled, 2D arcsecond tick labels use the double-prime symbol over the decimal point, e.g. `3.″8`; when disabled, labels remain unchanged, e.g. `3.8"`.
See full details below.

### [docs: add signpost llms.txt + consolidate agent instructions into AGENTS.md](https://github.com/PyAutoLabs/PyAutoArray/pull/347) (PyAutoLabs/PyAutoArray)
**API Changes:** None.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
**Scripts Changed:** None — docs only.

### [feat: Preloads API for reusing channel-invariant inversion quantities](https://github.com/PyAutoLabs/PyAutoArray/pull/344) (PyAutoLabs/PyAutoArray)
**API Changes:** All additive and backward compatible — no removals or renames.

- Added `aa.AbstractPreloads` and `aa.PreloadsInterferometer(curvature_matrix=None)` — containers for preloaded inversion quantities (new `autoarray/preloads/` package).
- `AbstractInversion`, the interferometer inversions, and the `inv

### [fix: VectorYX2DIrregular from_dict round-trip (missing values property)](https://github.com/PyAutoLabs/PyAutoArray/pull/342) (PyAutoLabs/PyAutoArray)
**API Changes:** Added a new public read-only `values` property on `VectorYX2DIrregular` returning the underlying `(N, 2)` ndarray. Purely additive — no existing call sites read `vec.values`. See full details below.

### [docs: add signpost llms.txt + consolidate agent instructions into AGENTS.md](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/474) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** None.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
**Scripts Changed:** None — docs only.

### [Lensing potential for elliptical/spherical dark-matter profiles (NFW/gNFW) + NFWSph fix](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/470) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** Adds a working `potential_2d_from` to the elliptical/spherical dark-matter profiles (via a single MGE-decomposition method on `gNFW`, inherited by `NFW`, `gNFWSph`, and all MCR/Virial variants). Corrects `NFWSph.potential_2d_from` (it returned values a factor of `r_s` too small). No public signature

### [fix(mass): convergence_func on PowerLawBroken, PowerLawMultipole, cNFW family](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/467) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** Added `convergence_func` overrides on `PowerLawBroken`, `PowerLawBrokenSph` (inherited), `PowerLawMultipole`, and the `cNFW` family (`cNFWSph` + MCR variants inherit). `PowerLawBroken._convergence` is a new private radial helper. `PowerLawBroken.potential_2d_from` now raises `NotImplementedError` ex

### [docs: add signpost llms.txt + consolidate agent instructions into AGENTS.md](https://github.com/PyAutoLabs/PyAutoLens/pull/570) (PyAutoLabs/PyAutoLens)
**API Changes:** None.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
**Scripts Changed:** None — docs only.

### [feat: datacube shared-state for AnalysisInterferometer via curvature preloads](https://github.com/PyAutoLabs/PyAutoLens/pull/566) (PyAutoLabs/PyAutoLens)
**API Changes:** All additive and backward compatible — no removals or renames.

- `AnalysisInterferometer.__init__` gains an opt-in `shared_preloads=False` flag.
- New method `AnalysisInterferometer.shared_state_from(instance)` — returns a `PreloadsInterferometer` with the channel-invariant `curvature_matrix` (or `

### [test: regression guard for HowToLens tutorial_3 NaN axis-limits crash](https://github.com/PyAutoLabs/PyAutoLens/pull/560) (PyAutoLabs/PyAutoLens)
**API Changes:** None — test-only.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

### [Honour PYAUTO_TEST_MODE in LOSSampler to fix los_halos simulator timeouts](https://github.com/PyAutoLabs/PyAutoLens/pull/559) (PyAutoLabs/PyAutoLens)
**API Changes:** `autolens.lens.los.negative_kappa_from` gains two optional keyword arguments, `quad_limit=50` and `quad_epsrel=1.49e-8` (both scipy's own `quad` defaults), threaded into its inner and outer integrals. Existing callers are unaffected. `LOSSampler.galaxies_from` now reads `autoconf.test_mode.is_test_m

### [docs(latent): migrate cookbooks to the Latent class API](https://github.com/PyAutoLabs/autofit_workspace/pull/72) (PyAutoLabs/autofit_workspace)
**Scripts Changed:** - `scripts/cookbooks/analysis.py` — defines `LatentFwhm(af.Latent)`, `Analysis.Latent = LatentFwhm`
- `scripts/cookbooks/latent_variables.py`, `samples.py` — prose migrated to the Latent API
- notebooks regenerated

### [fix: skip NSS example without optional dependency](https://github.com/PyAutoLabs/autofit_workspace/pull/71) (PyAutoLabs/autofit_workspace)
**Scripts Changed:** - `scripts/searches/nest.py` — catches the optional-dependency `ImportError` from `af.NSS(...)`, prints install guidance, and skips only the NSS fit when the extra is unavailable.

### [fix: preserve release result samples](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/122) (PyAutoLabs/autogalaxy_workspace)
**Scripts Changed:** - `scripts/guides/results/_quick_fit.py` — now creates two capped Nautilus fits in plain `output/results_folder`, retains all 300 samples, writes latent summaries, and disables fast-plot skipping so PNG/FITS workflow products exist.
- `scripts/guides/results/workflow/{csv_make,png_make,fits_make}.py

### [fix: reload saved result dataset with unchecked noise map](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/112) (PyAutoLabs/autogalaxy_workspace)
**Scripts Changed:** - `scripts/guides/results/start_here.py` — passes `check_noise_map=False` when reloading `image/dataset.fits` from the script output.

### [fix: restore release result contracts](https://github.com/PyAutoLabs/autolens_workspace/pull/229) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/guides/results/_quick_fit.py` — now creates two capped Nautilus fits in plain `output/results_folder`, retains all 300 samples, writes latent summaries, and disables fast-plot skipping so PNG/FITS workflow products exist.
- `scripts/guides/results/workflow/{csv_make,png_make,fits_make}.py

### [ci: validate navigator paths + catalogue staleness (+ banner-comment lint)](https://github.com/PyAutoLabs/autolens_workspace/pull/224) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** None — additive CI + tooling only.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

### [docs: add generated llms-full.txt catalogue + workspace_index.json](https://github.com/PyAutoLabs/autolens_workspace/pull/223) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** None. This is additive — generated artefacts plus a skill doc update.

### [fix: ensure aggregator helper results include datasets](https://github.com/PyAutoLabs/autolens_workspace/pull/221) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/guides/results/_quick_fit.py` — validates reusable helper output by checking for `**/image/dataset.fits`; removes incompatible helper output before regenerating.
- `scripts/guides/results/aggregator/data_fitting.py` — checks for a valid helper dataset and scrapes `results_path`.
- `script

### [docs(latent): migrate custom-latent examples to the Latent class (Phase 2)](https://github.com/PyAutoLabs/autolens_workspace/pull/219) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/guides/results/latent_variables.py` — 'Extending with a Custom Latent' rewritten to subclass `al.LatentLens` + `Latent = ...`
- `scripts/guides/results/workflow/{csv,png,fits}_make.py` — `AnalysisLatent` migrated to subclass `al.Latent` + `Latent = ...`
- notebooks regenerated

🤖 Generate
