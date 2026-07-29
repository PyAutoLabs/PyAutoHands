# Release Readiness Report

**Status: NOT READY**

**Run:** `2026-07-09T09-48-30Z`  •  **Path:** `/home/jammy/Code/PyAutoLabs/PyAutoBuild/test_results/runs/2026-07-09T09-48-30Z`  •  **Total duration:** 8980.4s

## Slow-Skipped Scripts (needs performance fix)

**23 script(s)** are being skipped because they exceed the 60s per-script timeout cap. These are NOT permanent skips — they need the underlying performance issue fixed and the `SLOW` marker removed from the workspace's `config/build/no_run.yaml`.

| Workspace | Script | Marked | Age | Reason |
|-----------|--------|--------|-----|--------|
| HowToGalaxy | `guides/results/database/start_here` | 2026-04-10 | 90d **STALE** | previously failed fast on a broken aggregator query; now runs the real aggregator and exceeds 60s |
| HowToGalaxy | `guides/results/examples/galaxies_fit` | 2026-04-10 | 90d **STALE** | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| HowToGalaxy | `guides/results/examples/models` | 2026-04-10 | 90d **STALE** | cascade from SLOW-skipped results/start_here.py; aggregator returns NoneType so instance.galaxies is None |
| HowToGalaxy | `guides/results/examples/samples` | 2026-04-10 | 90d **STALE** | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| HowToGalaxy | `guides/results/start_here` | 2026-04-10 | 90d **STALE** | exceeds 60s test timeout; unsets TEST_MODE to produce real samples for downstream examples |
| HowToGalaxy | `guides/results/workflow/csv_make` | 2026-04-10 | 90d **STALE** | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| HowToLens | `guides/results/database/start_here` | 2026-04-10 | 90d **STALE** | previously failed fast on a broken aggregator query; now runs the real aggregator and exceeds 60s |
| HowToLens | `guides/results/examples/queries` | 2026-04-10 | 90d **STALE** | cascade from SLOW-skipped results/start_here.py; stub Model lacks sersic_index attribute |
| HowToLens | `guides/results/examples/samples` | 2026-04-10 | 90d **STALE** | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| HowToLens | `guides/results/examples/samples_via_aggregator` | 2026-04-10 | 90d **STALE** | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| HowToLens | `howtolens/chapter_4_pixelizations/tutorial_10_brightness_adaption` | 2026-04-10 | 90d **STALE** | pixelization tutorial exceeds 60s test timeout |
| autogalaxy_workspace | `guides/results/database/start_here` | 2026-04-10 | 90d **STALE** | previously failed fast on a broken aggregator query; now runs the real aggregator and exceeds 60s |
| autogalaxy_workspace | `guides/results/workflow/csv_make` | 2026-04-10 | 90d **STALE** | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| autolens_workspace | `guides/results/database/start_here` | 2026-04-10 | 90d **STALE** | previously failed fast on a broken aggregator query; now runs the real aggregator and exceeds 60s |
| autolens_workspace_test | `database/scrape/multi_analysis` | 2026-04-10 | 90d **STALE** | exceeds 60s timeout; _test workspaces run full searches without test mode |
| autolens_workspace_test | `database/scrape/slam_general` | 2026-04-10 | 90d **STALE** | exceeds 60s timeout; _test workspaces run full searches without test mode |
| autolens_workspace_test | `database/scrape/slam_multi_one_by_one` | 2026-04-10 | 90d **STALE** | exceeds 60s timeout; _test workspaces run full searches without test mode |
| autolens_workspace_test | `database/scrape/slam_pix` | 2026-04-10 | 90d **STALE** | exceeds 60s timeout; _test workspaces run full searches without test mode |
| autolens_workspace_test | `imaging/modeling_visualization_jit` | 2026-05-07 | 63d **STALE** | JIT + full visualization pipeline exceeds 300s cap (autogalaxy variant ~90s); unblocked by PR #70 from prior `expected jax.Array, got numpy.float64` AssertionError, now hits perf wall |
| autolens_workspace_test | `imaging/modeling_visualization_jit_delaunay` | 2026-05-07 | 63d **STALE** | JIT + full visualization pipeline exceeds 300s cap; same root cause as modeling_visualization_jit |
| autolens_workspace_test | `imaging/modeling_visualization_jit_rectangular` | 2026-05-07 | 63d **STALE** | JIT + full visualization pipeline exceeds 301s cap; same root cause as modeling_visualization_jit |
| autolens_workspace_test | `interferometer/modeling_visualization_jit` | 2026-05-20 | 50d **STALE** | JIT + full visualization pipeline exceeds 300s cap; same root cause as imaging/modeling_visualization_jit family |
| autolens_workspace_test | `point_source/modeling_visualization_jit` | 2026-07-08 | 1d | JIT + Part-2 live Nautilus fit exceeds 300s cap; same family as imaging/interferometer modeling_visualization_jit (the zero_contour perf-assert false-positive was separately fixed to a cold/warm ratio, which now lets the script run past it into the slow fit) |

## Needs-Fix Scripts (parked for investigation)

**36 script(s)** are being skipped because they are broken and parked as a to-do list. These are NOT permanent skips — investigate the failure, fix the underlying bug, and remove the `NEEDS_FIX` marker from the workspace's `config/build/no_run.yaml`.

| Workspace | Script | Marked | Age | Reason |
|-----------|--------|--------|-----|--------|
| HowToFit | `chapter_1_introduction/tutorial_5_results_and_samples` | 2026-04-10 | 90d **STALE** | IndexError in samples access, likely related to InstanceInterpolator bug in autofit features/interpolate |
| HowToGalaxy | `autogalaxy_workspace/scripts/imaging/modeling` | 2026-04-10 | 90d **STALE** | KeyError on ('galaxies','galaxy','bulge','ell_comps'...) kwargs after API drift in top-level imaging/modeling.py |
| HowToGalaxy | `ellipse/modeling` | 2026-04-10 | 90d **STALE** | KeyError on 'ellipses.0.centre_0' kwargs after API drift in ellipse model |
| HowToGalaxy | `guides/advanced/over_sampling` | 2026-04-10 | 90d **STALE** | plot_grid() got unexpected kwarg 'plot_grid_lines' after plotter API drift |
| HowToGalaxy | `howtogalaxy/chapter_4_pixelizations/tutorial_5_model_fit` | 2026-04-10 | 90d **STALE** | LinAlgError: matrix not positive definite in pixelization fit |
| HowToGalaxy | `imaging/data_preparation/manual/mask_irregular` | 2026-04-10 | 90d **STALE** | silent failure, needs investigation |
| HowToGalaxy | `imaging/features/pixelization/modeling` | 2026-04-10 | 90d **STALE** | LinAlgError: matrix not positive definite in pixelization modeling |
| HowToGalaxy | `interferometer/features/pixelization/modeling` | 2026-04-10 | 90d **STALE** | LinAlgError: matrix not positive definite in interferometer pixelization modeling |
| HowToLens | `group/slam` | 2026-04-10 | 90d **STALE** | PriorException: upper limit must be greater than lower limit in group SLaM pipeline |
| HowToLens | `howtolens/chapter_2_lens_modeling/tutorial_2_practicalities` | 2026-04-10 | 90d **STALE** | NameError: 'af' not defined; tutorial missing ~80 lines of imports + setup boilerplate (compare tutorial_1) |
| HowToLens | `howtolens/chapter_4_pixelizations/tutorial_2_mappers` | 2026-04-10 | 90d **STALE** | ValueError: zero-size array reduction, empty mapper array |
| HowToLens | `imaging/data_preparation/manual/mask_irregular` | 2026-04-10 | 90d **STALE** | silent failure, needs investigation |
| HowToLens | `imaging/features/pixelization/delaunay` | 2026-04-10 | 90d **STALE** | autofit.exc.FitException in Delaunay pixelization fit |
| HowToLens | `imaging/features/pixelization/slam` | 2026-04-10 | 90d **STALE** | autofit.exc.FitException in SLaM pixelization pipeline |
| HowToLens | `interferometer/features/pixelization/delaunay` | 2026-04-10 | 90d **STALE** | broadcast shape mismatch (2,2) vs (1032,1032) in Delaunay interferometer |
| HowToLens | `multi/features/wavelength_dependence/modeling` | 2026-04-10 | 90d **STALE** | autofit.exc.FitException in multi-wavelength modeling |
| autofit_workspace | `features/interpolate` | 2026-04-10 | 90d **STALE** | IndexError in InstanceInterpolator.__getitem__ when querying time == 1.5; value_map lookup falls through to empty instances list |
| autogalaxy_workspace | `autogalaxy_workspace/scripts/imaging/modeling` | 2026-04-10 | 90d **STALE** | KeyError on ('galaxies','galaxy','bulge','ell_comps'...) kwargs after API drift in top-level imaging/modeling.py |
| autogalaxy_workspace | `imaging/data_preparation/manual/mask_irregular` | 2026-04-10 | 90d **STALE** | silent failure, needs investigation |
| autogalaxy_workspace | `imaging/features/pixelization/modeling` | 2026-04-10 | 90d **STALE** | LinAlgError: matrix not positive definite in pixelization modeling |
| autogalaxy_workspace | `interferometer/features/multi_gaussian_expansion/likelihood_function` | 2026-05-20 | 50d **STALE** | LinAlgError: matrix singular in MGE inversion -> InversionException (known_numerical; same family as pixelization variants above) |
| autogalaxy_workspace | `interferometer/features/pixelization/modeling` | 2026-04-10 | 90d **STALE** | LinAlgError: matrix not positive definite in interferometer pixelization modeling |
| autolens_workspace | `group/features/advanced/double_einstein_ring/slam` | 2026-05-20 | 50d **STALE** | same cascade as imaging variant — synthetic samples_summary lacks adapt_data; parking pattern of the imaging entry didn't cover this group/ twin |
| autolens_workspace | `group/slam` | 2026-04-10 | 90d **STALE** | PriorException: upper limit must be greater than lower limit in group SLaM pipeline |
| autolens_workspace | `imaging/data_preparation/manual/mask_irregular` | 2026-04-10 | 90d **STALE** | silent failure, needs investigation |
| autolens_workspace | `imaging/features/advanced/double_einstein_ring/slam` | 2026-05-07 | 63d **STALE** | autofit.exc.FitException in SLaM bypass mode (same family as imaging/features/pixelization/slam — Adapt regularization needs adapt_data which the synthetic samples_summary doesn't carry; cascade goes deep, fixing in one PR isn't tractable) |
| autolens_workspace | `imaging/features/pixelization/delaunay` | 2026-04-10 | 90d **STALE** | autofit.exc.FitException in Delaunay pixelization fit |
| autolens_workspace | `imaging/features/pixelization/slam` | 2026-04-10 | 90d **STALE** | autofit.exc.FitException in SLaM pixelization pipeline |
| autolens_workspace | `interferometer/features/pixelization/delaunay` | 2026-04-10 | 90d **STALE** | broadcast shape mismatch (2,2) vs (1032,1032) in Delaunay interferometer |
| autolens_workspace | `multi/features/wavelength_dependence/modeling` | 2026-04-10 | 90d **STALE** | autofit.exc.FitException in multi-wavelength modeling |
| autolens_workspace_test | `database/scrape/general` | 2026-04-27 | 73d **STALE** | PyAutoGalaxy abstract_fit.linear_light_profile_intensity_dict raises "TypeError: __hash__ method should return an integer" during subplot_fit_imaging after the search completes (a light-profile object's __hash__ returns a non-int). Surfaced once the dataset_label="build" path fix let the script progress past Imaging.from_fits. |
| autolens_workspace_test | `imaging/visualization` | 2026-04-10 | 90d **STALE** | AssertionError: dataset.png missing after visualization refactor |
| autolens_workspace_test | `jax_grad/imaging_lp` | 2026-04-10 | 90d **STALE** | JAX traceback in gradient computation for light profile |
| autolens_workspace_test | `jax_grad/imaging_mge` | 2026-04-10 | 90d **STALE** | AssertionError: Gradient is all zeros in MGE gradient computation |
| autolens_workspace_test | `jax_likelihood_functions/imaging/delaunay_mge` | 2026-04-10 | 90d **STALE** | timeout in JAX likelihood function benchmark |
| autolens_workspace_test | `jax_likelihood_functions/imaging/mge_group` | 2026-04-10 | 90d **STALE** | timeout in JAX likelihood function benchmark |

## Summary

| Passed | Failed | Skipped | Timeout |
|--------|--------|---------|---------|
| 620 | 3 | 72 | 1 |

## Per-Project Breakdown

| Project | Passed | Failed | Skipped | Timeout | Duration |
|---------|--------|--------|---------|---------|----------|
| autofit | 26 | 0 | 6 | 0 | 104.5s |
| autofit_test | 35 | 0 | 2 | 0 | 218.9s |
| autogalaxy | 108 | 0 | 14 | 0 | 1094.5s |
| autogalaxy_test | 54 | 0 | 0 | 0 | 1233.8s |
| autolens | 226 | 0 | 30 | 1 | 3975.7s |
| autolens_test | 88 | 3 | 16 | 0 | 1661.4s |
| euclid | 5 | 0 | 0 | 0 | 202.8s |
| howtofit | 15 | 0 | 1 | 0 | 65.8s |
| howtogalaxy | 25 | 0 | 1 | 0 | 133.6s |
| howtolens | 38 | 0 | 2 | 0 | 289.3s |

## Slowest scripts (top 25)

| Script | Project | Status | Duration | Share |
|--------|---------|--------|----------|-------|
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/cluster/lenstool/modeling.py` | autolens | timeout | 300.1s | 3.3% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/multi/start_here.py` | autolens | passed | 102.3s | 1.1% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/profiles/light_and_mass_profiles.py` | autolens | passed | 85.5s | 1.0% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/start_here.py` | autolens | passed | 83.4s | 0.9% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/start_here.py` | autolens | passed | 81.7s | 0.9% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/delaunay_mge.py` | autogalaxy_test | passed | 77.9s | 0.9% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/visualization_jax.py` | autolens_test | passed | 73.9s | 0.8% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/multi/mge_group.py` | autolens_test | passed | 73.4s | 0.8% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/datacube/delaunay.py` | autolens_test | failed | 70.5s | 0.8% |
| `/home/jammy/Code/PyAutoLabs/euclid_strong_lens_modeling_pipeline/scripts/lens_model_waveband.py` | euclid | passed | 69.4s | 0.8% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/units/flux.py` | autolens | passed | 66.8s | 0.7% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/subhalo.py` | autolens_test | passed | 64.3s | 0.7% |
| `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_4_pixelizations/tutorial_10_brightness_adaption.py` | howtolens | passed | 62.9s | 0.7% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/delaunay_mge.py` | autolens_test | passed | 60.9s | 0.7% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/delaunay_mge.py` | autogalaxy_test | passed | 58.3s | 0.6% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_mge.py` | autolens_test | passed | 57.2s | 0.6% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/shapelets/modeling.py` | autogalaxy | passed | 57.0s | 0.6% |
| `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/prior_correctness/emcee_gaussian_bias_check.py` | autofit_test | passed | 56.3s | 0.6% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/multi/mge_group.py` | autogalaxy_test | passed | 56.2s | 0.6% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/imaging/visualization.py` | autogalaxy_test | passed | 55.0s | 0.6% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/multi_gaussian_expansion/modeling.py` | autolens | passed | 53.7s | 0.6% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/advanced/graphical.py` | autolens | passed | 53.4s | 0.6% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/modeling.py` | autolens | passed | 51.2s | 0.6% |
| `/home/jammy/Code/PyAutoLabs/euclid_strong_lens_modeling_pipeline/scripts/mge_lens_only.py` | euclid | passed | 50.4s | 0.6% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/multi/delaunay_mge.py` | autogalaxy_test | passed | 50.0s | 0.6% |

## Failures by Classification

### Source Code Bugs (3)

- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/visualization.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/visualization.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  
You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/visualization.py", line 171, in <module>
    assert_png("visualization_overlaid_positions.png")
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/visualization.py", line 141, in assert_png
    assert path.exists(), f"{filename} missing"
           ^^^^^^^^^^^^^
AssertionError: visualization_overlaid_positions.png missing
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/convolution_over_sampled.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/convolution_over_sampled.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  
You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/mask/mask_2d_util.py:564: UserWarning: Mask padded from (21, 21) to (np.int64(23), np.int64(23)) (parity preserved) to support kernel footprint (7, 7).
  warnings.warn(
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/convolution_over_sampled.py", line 384, in <module>
    assert raised == 3, f"expected 3 guard raises, got {raised}"
           ^^^^^^^^^^^
AssertionError: expected 3 guard raises, got 2
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/datacube/delaunay.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/datacube/delaunay.py']' died with <Signals.SIGKILL: 9>.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:206: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autolens_workspace_test is compatible with the installed library version (2026.7.6.649): no `version.minimum_library_version` or `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
  ```
  </details>

### Timeouts (1)

- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/cluster/lenstool/modeling.py`
  - Timed out after 300s
  - **Recently modified** in [feat: combined strong+weak lensing features example (weak series step 8)](https://github.com/PyAutoLabs/autolens_workspace/pull/251)
  - **Recently modified** in [feat: weak shear-profile + convergence-map demos; should_simulate adoption](https://github.com/PyAutoLabs/autolens_workspace/pull/244)
  - **Recently modified** in [feat: scripts/weak/modeling.py — weak lensing model-fit tutorial](https://github.com/PyAutoLabs/autolens_workspace/pull/241)
  - **Recently modified** in [docs: flagship 'PyAutoLens for Lenstool users' example — SMACS J0723 vs Mahler et al. 2023](https://github.com/PyAutoLabs/autolens_workspace/pull/240)
  - **Recently modified** in [feat: cluster + group scaling relations in Lenstool convention (reference-anchored, fixed exponent)](https://github.com/PyAutoLabs/autolens_workspace/pull/238)

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
| `modeling_visualization_jit.py` | SLOW 2026-07-08 - JIT + Part-2 live Nautilus fit exceeds 300s cap; same family as imaging/interferometer modeling_visualization_jit (the zero_contour perf-assert false-positive was separately fixed to a cold/warm ratio, which now lets the script run past it into the slow fit) |
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

### [feat: catalogue-size cap for PYAUTO_SMALL_DATASETS smoke mode](https://github.com/PyAutoLabs/PyAutoArray/pull/366) (PyAutoLabs/PyAutoArray)
**API Changes:** Added only: `aa.util.dataset.SMALL_DATASETS_N_CATALOGUE`, `aa.util.dataset.cap_catalogue_size_for_small_datasets(n)`.

### [fix: oversampled fine state when the blurring mask is padded](https://github.com/PyAutoLabs/PyAutoArray/pull/358) (PyAutoLabs/PyAutoArray)
**API Changes:** None — bug fix only, +62/−3 in `convolver.py` + tests.

### [feat: oversampled PSF inversion wiring — mapping formalism (phase 2b)](https://github.com/PyAutoLabs/PyAutoArray/pull/357) (PyAutoLabs/PyAutoArray)
**API Changes:** Additive; nothing changes while `convolve_over_sample_size == 1`.

- `Mapper.mapping_matrix_over_sampled` — sub-resolution mapping matrix, shape `[total_sub_pixels, source_pixels]` in per-pixel sub-block order (the 2a Convolver input format). Binning its rows by the mean of each sub-block reproduces

### [feat: oversampled PSF convolution core API (convolve_over_sample_size)](https://github.com/PyAutoLabs/PyAutoArray/pull/355) (PyAutoLabs/PyAutoArray)
**API Changes:** All changes are additive; `convolve_over_sample_size=1` (default) leaves every existing code path untouched.

- `Convolver(convolve_over_sample_size: int = 1)` — kernel supplied at the fine resolution when > 1; new `kernel_shape_image_resolution` property; convolution methods expect over-sampled (su

### [feat: Lenstool-native dPIE parameterization (from_lenstool + dPIEMassLenstool) and analytic potential](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/487) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** Added Lenstool-parameterized construction and fitting for the dPIE family: `from_lenstool(...)` classmethods on `dPIEMass` / `dPIEMassSph`, and new model-fittable wrapper profiles `dPIEMassLenstool` / `dPIEMassLenstoolSph` (with prior configs). `dPIEMass.potential_2d_from` values change (MGE approxi

### [feat: oversampled PSF blurred images — operate/image consumer (phase 2c)](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/481) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** None — behaviour is additive behind `convolve_over_sample_size=1` defaults; no signatures change. The three blurred-image methods (`blurred_image_2d_from`, `blurred_image_2d_list_from`, `galaxy_blurred_image_2d_dict_from`) gain the oversampled evaluation branch. `LightProfileOperated` images continu

### [fix: mixed-dataset factor graphs crash combined visualization](https://github.com/PyAutoLabs/PyAutoLens/pull/587) (PyAutoLabs/PyAutoLens)
**API Changes:** None — internal fix to visualization behaviour under mixed factor graphs.

### [feat: cap SimulatorShearYX catalogue size under PYAUTO_SMALL_DATASETS (weak series step 9)](https://github.com/PyAutoLabs/PyAutoLens/pull/584) (PyAutoLabs/PyAutoLens)
**API Changes:** None — internal behaviour of the simulator under a smoke-mode env var; public signatures unchanged.

### [feat: tangential/cross shear profiles + Kaiser-Squires map (weak series step 6)](https://github.com/PyAutoLabs/PyAutoLens/pull/582) (PyAutoLabs/PyAutoLens)
**API Changes:** Added only — no existing symbol removed, renamed or changed.
- `aplt.plot_shear_profile(obj, centre=, bins=, ax=, output_*)` — binned γ_t/γ_x profiles of a `WeakDataset` or `FitWeak`.
- `aplt.plot_convergence_map(shear_yx, shape_native=, smoothing_sigma_pixels=, ...)` — Kaiser-Squires E-mode map.
- 

### [feat: AnalysisWeak — weak lensing modeling (weak series step 4)](https://github.com/PyAutoLabs/PyAutoLens/pull/580) (PyAutoLabs/PyAutoLens)
**API Changes:** Added only — no existing symbol removed, renamed or changed.
- `al.AnalysisWeak(dataset, cosmology=, title_prefix=, use_jax=False)` — new Analysis class for `WeakDataset` fits. `use_jax` defaults to `False` (`FitWeak` is NumPy-only; JAX needs pytree registration — deliberate future work).
- New pack

### [feat: cluster-scale visualization — per-plane critical curves/caustics aplt helpers](https://github.com/PyAutoLabs/PyAutoLens/pull/578) (PyAutoLabs/PyAutoLens)
**API Changes:** Added five `aplt`-level plotting helpers (`plot_positions_overlay`, `plot_image_group_zooms`, `plot_critical_curves`, `plot_caustics`, `subplot_cluster_dataset`) plus the `WONG_PALETTE` / `CLUSTER_CMAP` constants in `autolens.cluster.plot.cluster_plots`. Purely additive — no existing symbol changes.

### [docs: add dPIEMassLenstool / dPIEMassLenstoolSph to mass API autosummary](https://github.com/PyAutoLabs/PyAutoLens/pull/576) (PyAutoLabs/PyAutoLens)
**API Changes:** None — internal changes only (documentation autosummary entries; the symbols themselves land via the PyAutoGalaxy PR).

### [docs(latent): migrate cookbooks to the Latent class API](https://github.com/PyAutoLabs/autofit_workspace/pull/72) (PyAutoLabs/autofit_workspace)
**Scripts Changed:** - `scripts/cookbooks/analysis.py` — defines `LatentFwhm(af.Latent)`, `Analysis.Latent = LatentFwhm`
- `scripts/cookbooks/latent_variables.py`, `samples.py` — prose migrated to the Latent API
- notebooks regenerated

### [fix: skip NSS example without optional dependency](https://github.com/PyAutoLabs/autofit_workspace/pull/71) (PyAutoLabs/autofit_workspace)
**Scripts Changed:** - `scripts/searches/nest.py` — catches the optional-dependency `ImportError` from `af.NSS(...)`, prints install guidance, and skips only the NSS fit when the extra is unavailable.

### [fix: preserve release result samples](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/122) (PyAutoLabs/autogalaxy_workspace)
**Scripts Changed:** - `scripts/guides/results/_quick_fit.py` — now creates two capped Nautilus fits in plain `output/results_folder`, retains all 300 samples, writes latent summaries, and disables fast-plot skipping so PNG/FITS workflow products exist.
- `scripts/guides/results/workflow/{csv_make,png_make,fits_make}.py

### [feat: combined strong+weak lensing features example (weak series step 8)](https://github.com/PyAutoLabs/autolens_workspace/pull/251) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/weak/features/strong_lensing/simulator.py` (new) — both datasets from one tracer.
- `scripts/weak/features/strong_lensing/fit.py` (new) — `FitImaging` + `FitWeak` with a shared tracer; joint LL = exact sum (6653.7 + 676.5 = 7330.2); shear profile demo.
- `scripts/weak/features/strong_lens

### [feat: weak shear-profile + convergence-map demos; should_simulate adoption](https://github.com/PyAutoLabs/autolens_workspace/pull/244) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/weak/fit.py` — new `__Shear Profile__` section (binned γ_t data-vs-model overlay + γ_x B-mode null test via `aplt.plot_shear_profile`); adopts the standard `__Dataset Auto-Simulation__` pattern (`al.util.dataset.should_simulate`) per user direction.
- `scripts/weak/simulator.py` — new `__

### [feat: scripts/weak/modeling.py — weak lensing model-fit tutorial](https://github.com/PyAutoLabs/autolens_workspace/pull/241) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/weak/modeling.py` (new) — Nautilus Isothermal fit to the simulated `WeakDataset` via `al.AnalysisWeak`; auto-simulates the dataset if missing; validated end-to-end (recovered `einstein_radius = 1.556 (1.476–1.631)` vs truth 1.6, ~7 min CPU; the search's own `VisualizerWeak` produced the o

### [docs: flagship 'PyAutoLens for Lenstool users' example — SMACS J0723 vs Mahler et al. 2023](https://github.com/PyAutoLabs/autolens_workspace/pull/240) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - **Added:** `scripts/cluster/lenstool/{data.py, modeling.py, README.md, __init__.py}`. No dataset files committed (all runtime-downloaded/derived).

### [feat: cluster + group scaling relations in Lenstool convention (reference-anchored, fixed exponent)](https://github.com/PyAutoLabs/autolens_workspace/pull/238) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/cluster/simulator.py` — truth relation → reference-anchored (b0_ref = 0.12, exponent 0.5, rs scaled); regenerates `dataset/cluster/simple/`.
- `scripts/cluster/modeling.py` — single free `b0_ref` (U(0,1)), fixed exponents, rewritten `__Scaling Relation__` prose (referee/Lenstool rationale
