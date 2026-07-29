# Release Readiness Report

**Status: NOT READY**

**Run:** `2026-07-20T15-09-29Z`  •  **Path:** `/home/jammy/Code/PyAutoLabs/PyAutoHands/test_results/runs/2026-07-20T15-09-29Z`  •  **Total duration:** 8376.5s

## Slow-Skipped Scripts (needs performance fix)

**43 script(s)** are being skipped because they exceed the 60s per-script timeout cap. These are NOT permanent skips — they need the underlying performance issue fixed and the `SLOW` marker removed from the workspace's `config/build/no_run.yaml`.

| Workspace | Script | Marked | Age | Reason |
|-----------|--------|--------|-----|--------|
| HowToGalaxy | `guides/results/database/start_here` | 2026-04-10 | 101d **STALE** | previously failed fast on a broken aggregator query; now runs the real aggregator and exceeds 60s |
| HowToGalaxy | `guides/results/examples/galaxies_fit` | 2026-04-10 | 101d **STALE** | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| HowToGalaxy | `guides/results/examples/models` | 2026-04-10 | 101d **STALE** | cascade from SLOW-skipped results/start_here.py; aggregator returns NoneType so instance.galaxies is None |
| HowToGalaxy | `guides/results/examples/samples` | 2026-04-10 | 101d **STALE** | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| HowToGalaxy | `guides/results/start_here` | 2026-04-10 | 101d **STALE** | exceeds 60s test timeout; unsets TEST_MODE to produce real samples for downstream examples |
| HowToGalaxy | `guides/results/workflow/csv_make` | 2026-04-10 | 101d **STALE** | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| HowToLens | `guides/results/database/start_here` | 2026-04-10 | 101d **STALE** | previously failed fast on a broken aggregator query; now runs the real aggregator and exceeds 60s |
| HowToLens | `guides/results/examples/queries` | 2026-04-10 | 101d **STALE** | cascade from SLOW-skipped results/start_here.py; stub Model lacks sersic_index attribute |
| HowToLens | `guides/results/examples/samples` | 2026-04-10 | 101d **STALE** | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| HowToLens | `guides/results/examples/samples_via_aggregator` | 2026-04-10 | 101d **STALE** | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| HowToLens | `howtolens/chapter_4_pixelizations/tutorial_10_brightness_adaption` | 2026-04-10 | 101d **STALE** | pixelization tutorial exceeds 60s test timeout |
| autogalaxy_workspace | `guides/results/database/start_here` | 2026-04-10 | 101d **STALE** | previously failed fast on a broken aggregator query; now runs the real aggregator and exceeds 60s |
| autogalaxy_workspace | `guides/results/workflow/csv_make` | 2026-04-10 | 101d **STALE** | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| autogalaxy_workspace | `imaging/features/shapelets/modeling` | 2026-07-14 | 6d | real-search JAX shapelet fit exceeds the 1800s mode=release cap (>30min); speedup tracked by the Profiling Agent (PyAutoHeart#72). Not a bug. |
| autogalaxy_workspace_test | `jax_grad/interferometer/mge.py` | 2026-07-14 | 6d | finite-difference JAX interferometer MGE gradient; flakes at the 1800s cap (PyAutoHeart#74) |
| autogalaxy_workspace_test | `jax_grad/multi/mge.py` | 2026-07-14 | 6d | finite-difference JAX multi-band MGE gradient; flakes at the 1800s cap (PyAutoHeart#74) |
| autogalaxy_workspace_test | `jax_likelihood_functions/imaging/delaunay_mge.py` | 2026-07-14 | 6d | real-search JAX imaging Delaunay-MGE likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| autogalaxy_workspace_test | `jax_likelihood_functions/interferometer/delaunay.py` | 2026-07-14 | 6d | real-search JAX interferometer Delaunay likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| autogalaxy_workspace_test | `jax_likelihood_functions/interferometer/delaunay_mge.py` | 2026-07-14 | 6d | real-search JAX interferometer Delaunay-MGE likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| autogalaxy_workspace_test | `jax_likelihood_functions/interferometer/mge.py` | 2026-07-14 | 6d | real-search JAX interferometer MGE likelihood; flakes at the 1800s mode=release cap (PyAutoHeart#74) |
| autogalaxy_workspace_test | `jax_likelihood_functions/interferometer/mge_group.py` | 2026-07-14 | 6d | real-search JAX interferometer MGE-group likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| autogalaxy_workspace_test | `jax_likelihood_functions/interferometer/rectangular_mge.py` | 2026-07-14 | 6d | real-search JAX interferometer rectangular-MGE likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| autogalaxy_workspace_test | `jax_likelihood_functions/multi/delaunay_mge` | 2026-07-14 | 6d | real-search JAX Delaunay-MGE multi-band likelihood is borderline against the 1800s mode=release cap (its autolens_workspace_test sibling times out); skipped to keep release-validation deterministic. Speedup tracked by the Profiling Agent (PyAutoHeart#72). Not a bug. |
| autolens_workspace | `guides/results/database/start_here` | 2026-04-10 | 101d **STALE** | previously failed fast on a broken aggregator query; now runs the real aggregator and exceeds 60s |
| autolens_workspace_test | `database/scrape/multi_analysis` | 2026-04-10 | 101d **STALE** | exceeds 60s timeout; _test workspaces run full searches without test mode |
| autolens_workspace_test | `database/scrape/slam_general` | 2026-04-10 | 101d **STALE** | exceeds 60s timeout; _test workspaces run full searches without test mode |
| autolens_workspace_test | `database/scrape/slam_multi_one_by_one` | 2026-04-10 | 101d **STALE** | exceeds 60s timeout; _test workspaces run full searches without test mode |
| autolens_workspace_test | `database/scrape/slam_pix` | 2026-04-10 | 101d **STALE** | exceeds 60s timeout; _test workspaces run full searches without test mode |
| autolens_workspace_test | `imaging/modeling_visualization_jit` | 2026-05-07 | 74d **STALE** | JIT + full visualization pipeline exceeds 300s cap (autogalaxy variant ~90s); unblocked by PR #70 from prior `expected jax.Array, got numpy.float64` AssertionError, now hits perf wall |
| autolens_workspace_test | `imaging/modeling_visualization_jit_delaunay` | 2026-05-07 | 74d **STALE** | JIT + full visualization pipeline exceeds 300s cap; same root cause as modeling_visualization_jit |
| autolens_workspace_test | `imaging/modeling_visualization_jit_rectangular` | 2026-05-07 | 74d **STALE** | JIT + full visualization pipeline exceeds 301s cap; same root cause as modeling_visualization_jit |
| autolens_workspace_test | `interferometer/modeling_visualization_jit` | 2026-05-20 | 61d **STALE** | JIT + full visualization pipeline exceeds 300s cap; same root cause as imaging/modeling_visualization_jit family |
| autolens_workspace_test | `jax_grad/interferometer.py` | 2026-07-14 | 6d | finite-difference JAX interferometer gradient; flakes at the 1800s cap (PyAutoHeart#74) |
| autolens_workspace_test | `jax_likelihood_functions/datacube/delaunay.py` | 2026-07-14 | 6d | real-search JAX datacube Delaunay likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| autolens_workspace_test | `jax_likelihood_functions/datacube/shared_preloads.py` | 2026-07-14 | 6d | real-search JAX datacube shared-preloads likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| autolens_workspace_test | `jax_likelihood_functions/interferometer/delaunay.py` | 2026-07-14 | 6d | real-search JAX interferometer Delaunay likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| autolens_workspace_test | `jax_likelihood_functions/interferometer/delaunay_mge.py` | 2026-07-14 | 6d | real-search JAX interferometer Delaunay-MGE likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| autolens_workspace_test | `jax_likelihood_functions/interferometer/mge.py` | 2026-07-14 | 6d | real-search JAX interferometer MGE likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| autolens_workspace_test | `jax_likelihood_functions/interferometer/mge_group.py` | 2026-07-14 | 6d | real-search JAX interferometer MGE-group likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| autolens_workspace_test | `jax_likelihood_functions/interferometer/rectangular_mge.py` | 2026-07-14 | 6d | real-search JAX interferometer rectangular-MGE likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| autolens_workspace_test | `jax_likelihood_functions/multi/delaunay_mge` | 2026-07-14 | 6d | real-search JAX Delaunay-MGE multi-band likelihood exceeds the 1800s mode=release cap; speedup tracked by the Profiling Agent (PyAutoHeart#72). Not a bug. |
| autolens_workspace_test | `jax_likelihood_functions/multi/shared_preloads.py` | 2026-07-14 | 6d | real-search JAX multi-band shared-preloads likelihood; flakes at the 1800s mode=release cap (PyAutoHeart#74) |
| autolens_workspace_test | `point_source/modeling_visualization_jit` | 2026-07-08 | 12d | JIT + Part-2 live Nautilus fit exceeds 300s cap; same family as imaging/interferometer modeling_visualization_jit (the zero_contour perf-assert false-positive was separately fixed to a cold/warm ratio, which now lets the script run past it into the slow fit) |

## Needs-Fix Scripts (parked for investigation)

**36 script(s)** are being skipped because they are broken and parked as a to-do list. These are NOT permanent skips — investigate the failure, fix the underlying bug, and remove the `NEEDS_FIX` marker from the workspace's `config/build/no_run.yaml`.

| Workspace | Script | Marked | Age | Reason |
|-----------|--------|--------|-----|--------|
| HowToFit | `chapter_1_introduction/tutorial_5_results_and_samples` | 2026-04-10 | 101d **STALE** | IndexError in samples access, likely related to InstanceInterpolator bug in autofit features/interpolate |
| HowToGalaxy | `autogalaxy_workspace/scripts/imaging/modeling` | 2026-04-10 | 101d **STALE** | KeyError on ('galaxies','galaxy','bulge','ell_comps'...) kwargs after API drift in top-level imaging/modeling.py |
| HowToGalaxy | `ellipse/modeling` | 2026-04-10 | 101d **STALE** | KeyError on 'ellipses.0.centre_0' kwargs after API drift in ellipse model |
| HowToGalaxy | `guides/advanced/over_sampling` | 2026-04-10 | 101d **STALE** | plot_grid() got unexpected kwarg 'plot_grid_lines' after plotter API drift |
| HowToGalaxy | `howtogalaxy/chapter_4_pixelizations/tutorial_5_model_fit` | 2026-04-10 | 101d **STALE** | LinAlgError: matrix not positive definite in pixelization fit |
| HowToGalaxy | `imaging/data_preparation/manual/mask_irregular` | 2026-04-10 | 101d **STALE** | silent failure, needs investigation |
| HowToGalaxy | `imaging/features/pixelization/modeling` | 2026-04-10 | 101d **STALE** | LinAlgError: matrix not positive definite in pixelization modeling |
| HowToGalaxy | `interferometer/features/pixelization/modeling` | 2026-04-10 | 101d **STALE** | LinAlgError: matrix not positive definite in interferometer pixelization modeling |
| HowToLens | `group/slam` | 2026-04-10 | 101d **STALE** | PriorException: upper limit must be greater than lower limit in group SLaM pipeline |
| HowToLens | `howtolens/chapter_2_lens_modeling/tutorial_2_practicalities` | 2026-04-10 | 101d **STALE** | NameError: 'af' not defined; tutorial missing ~80 lines of imports + setup boilerplate (compare tutorial_1) |
| HowToLens | `howtolens/chapter_4_pixelizations/tutorial_2_mappers` | 2026-04-10 | 101d **STALE** | ValueError: zero-size array reduction, empty mapper array |
| HowToLens | `imaging/data_preparation/manual/mask_irregular` | 2026-04-10 | 101d **STALE** | silent failure, needs investigation |
| HowToLens | `imaging/features/pixelization/delaunay` | 2026-04-10 | 101d **STALE** | autofit.exc.FitException in Delaunay pixelization fit |
| HowToLens | `imaging/features/pixelization/slam` | 2026-04-10 | 101d **STALE** | autofit.exc.FitException in SLaM pixelization pipeline |
| HowToLens | `interferometer/features/pixelization/delaunay` | 2026-04-10 | 101d **STALE** | broadcast shape mismatch (2,2) vs (1032,1032) in Delaunay interferometer |
| HowToLens | `multi/features/wavelength_dependence/modeling` | 2026-04-10 | 101d **STALE** | autofit.exc.FitException in multi-wavelength modeling |
| autofit_workspace | `features/interpolate` | 2026-04-10 | 101d **STALE** | IndexError in InstanceInterpolator.__getitem__ when querying time == 1.5; value_map lookup falls through to empty instances list |
| autogalaxy_workspace | `autogalaxy_workspace/scripts/imaging/modeling` | 2026-04-10 | 101d **STALE** | KeyError on ('galaxies','galaxy','bulge','ell_comps'...) kwargs after API drift in top-level imaging/modeling.py |
| autogalaxy_workspace | `imaging/data_preparation/manual/mask_irregular` | 2026-04-10 | 101d **STALE** | silent failure, needs investigation |
| autogalaxy_workspace | `imaging/features/pixelization/modeling` | 2026-04-10 | 101d **STALE** | LinAlgError: matrix not positive definite in pixelization modeling |
| autogalaxy_workspace | `interferometer/features/multi_gaussian_expansion/likelihood_function` | 2026-05-20 | 61d **STALE** | LinAlgError: matrix singular in MGE inversion -> InversionException (known_numerical; same family as pixelization variants above) |
| autogalaxy_workspace | `interferometer/features/pixelization/modeling` | 2026-04-10 | 101d **STALE** | LinAlgError: matrix not positive definite in interferometer pixelization modeling |
| autolens_workspace | `group/features/advanced/double_einstein_ring/slam` | 2026-05-20 | 61d **STALE** | same cascade as imaging variant — synthetic samples_summary lacks adapt_data; parking pattern of the imaging entry didn't cover this group/ twin |
| autolens_workspace | `group/slam` | 2026-04-10 | 101d **STALE** | PriorException: upper limit must be greater than lower limit in group SLaM pipeline |
| autolens_workspace | `imaging/data_preparation/manual/mask_irregular` | 2026-04-10 | 101d **STALE** | silent failure, needs investigation |
| autolens_workspace | `imaging/features/advanced/double_einstein_ring/slam` | 2026-05-07 | 74d **STALE** | autofit.exc.FitException in SLaM bypass mode (same family as imaging/features/pixelization/slam — Adapt regularization needs adapt_data which the synthetic samples_summary doesn't carry; cascade goes deep, fixing in one PR isn't tractable) |
| autolens_workspace | `imaging/features/pixelization/delaunay` | 2026-04-10 | 101d **STALE** | autofit.exc.FitException in Delaunay pixelization fit |
| autolens_workspace | `imaging/features/pixelization/slam` | 2026-04-10 | 101d **STALE** | autofit.exc.FitException in SLaM pixelization pipeline |
| autolens_workspace | `interferometer/features/pixelization/delaunay` | 2026-04-10 | 101d **STALE** | broadcast shape mismatch (2,2) vs (1032,1032) in Delaunay interferometer |
| autolens_workspace | `multi/features/wavelength_dependence/modeling` | 2026-04-10 | 101d **STALE** | autofit.exc.FitException in multi-wavelength modeling |
| autolens_workspace_test | `database/scrape/general` | 2026-04-27 | 84d **STALE** | PyAutoGalaxy abstract_fit.linear_light_profile_intensity_dict raises "TypeError: __hash__ method should return an integer" during subplot_fit_imaging after the search completes (a light-profile object's __hash__ returns a non-int). Surfaced once the dataset_label="build" path fix let the script progress past Imaging.from_fits. |
| autolens_workspace_test | `imaging/visualization` | 2026-04-10 | 101d **STALE** | AssertionError: dataset.png missing after visualization refactor |
| autolens_workspace_test | `jax_grad/imaging_lp` | 2026-04-10 | 101d **STALE** | JAX traceback in gradient computation for light profile |
| autolens_workspace_test | `jax_grad/imaging_mge` | 2026-04-10 | 101d **STALE** | AssertionError: Gradient is all zeros in MGE gradient computation |
| autolens_workspace_test | `jax_likelihood_functions/imaging/delaunay_mge` | 2026-04-10 | 101d **STALE** | timeout in JAX likelihood function benchmark |
| autolens_workspace_test | `jax_likelihood_functions/imaging/mge_group` | 2026-04-10 | 101d **STALE** | timeout in JAX likelihood function benchmark |

## Summary

| Passed | Failed | Skipped | Timeout |
|--------|--------|---------|---------|
| 632 | 10 | 92 | 5 |

## Per-Project Breakdown

| Project | Passed | Failed | Skipped | Timeout | Duration |
|---------|--------|--------|---------|---------|----------|
| autofit | 27 | 0 | 6 | 0 | 163.4s |
| autofit_test | 43 | 1 | 2 | 0 | 203.0s |
| autogalaxy | 107 | 0 | 15 | 0 | 711.7s |
| autogalaxy_test | 45 | 0 | 9 | 1 | 1227.4s |
| autolens | 237 | 3 | 30 | 3 | 3327.5s |
| autolens_test | 93 | 3 | 26 | 1 | 1919.4s |
| euclid | 5 | 0 | 0 | 0 | 199.4s |
| howtofit | 15 | 0 | 1 | 0 | 51.2s |
| howtogalaxy | 24 | 1 | 1 | 0 | 195.2s |
| howtolens | 36 | 2 | 2 | 0 | 378.5s |

## Slowest scripts (top 25)

| Script | Project | Status | Duration | Share |
|--------|---------|--------|----------|-------|
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/aggregator/galaxies.py` | autogalaxy_test | timeout | 431.5s | 5.2% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/potential_correction/subhalo_recovery.py` | autolens_test | timeout | 300.2s | 3.6% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/advanced/potential_correction.py` | autolens | timeout | 300.2s | 3.6% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/weak/features/strong_lensing/a2744.py` | autolens | timeout | 300.1s | 3.6% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/cluster/start_here.py` | autolens | timeout | 300.0s | 3.6% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/cluster/lenstool/modeling.py` | autolens | passed | 114.9s | 1.4% |
| `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_4_pixelizations/tutorial_10_brightness_adaption.py` | howtolens | passed | 109.6s | 1.3% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/advanced/graphical.py` | autolens | passed | 94.6s | 1.1% |
| `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_4_pixelizations/tutorial_4_bayesian_regularization.py` | howtogalaxy | passed | 80.2s | 1.0% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/database/scrape/scaling_relation.py` | autolens_test | passed | 78.0s | 0.9% |
| `/home/jammy/Code/PyAutoLabs/euclid_strong_lens_modeling_pipeline/scripts/lens_model_waveband.py` | euclid | passed | 74.2s | 0.9% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/multi/start_here.py` | autolens | passed | 69.1s | 0.8% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/profiles/light_and_mass_profiles.py` | autolens | passed | 69.0s | 0.8% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_mge.py` | autolens_test | passed | 67.1s | 0.8% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/subhalo.py` | autolens_test | passed | 65.8s | 0.8% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/multi/mge_group.py` | autolens_test | passed | 64.9s | 0.8% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/units/flux.py` | autolens | passed | 61.1s | 0.7% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/visualization_jax.py` | autolens_test | passed | 60.7s | 0.7% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/start_here.py` | autolens | passed | 59.4s | 0.7% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/point_source/point.py` | autolens_test | passed | 50.8s | 0.6% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/imaging/modeling_visualization_jit.py` | autogalaxy_test | passed | 50.4s | 0.6% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/multi_gaussian_expansion/modeling.py` | autolens | passed | 48.6s | 0.6% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/start_here.py` | autolens | passed | 47.1s | 0.6% |
| `/home/jammy/Code/PyAutoLabs/euclid_strong_lens_modeling_pipeline/scripts/mge_lens_only.py` | euclid | passed | 45.1s | 0.5% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_dspl.py` | autolens_test | passed | 45.0s | 0.5% |

## Failures by Classification

### Source Code Bugs (5)

- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/profiling/aggregator/profile_database.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/profiling/aggregator/profile_database.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
    File "<string>", line 6, in __init__
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/sqlalchemy/orm/decl_base.py", line 2170, in _declarative_constructor
    setattr(self, k, kwargs[k])
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/database/model/array.py", line 188, in hdu
    self.array = hdu.data
    ^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/database/model/array.py", line 56, in array
    self._dtype = get_class_path(getattr(np, array.dtype.name))
                                             ^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'dtype'
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/potential_correction/start_here.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/potential_correction/start_here.py']' returned non-zero exit status 1.
  - **Recently modified** in [feat: cluster/group examples on Lenstool-native dPIE default + reference-anchored SLaM scaling](https://github.com/PyAutoLabs/autolens_workspace/pull/287)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
      self._pair_dpsi_data_obj = self.dpsi_pixelization.pair_dpsi_data_mesh(
                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoLens/autolens/potential_correction/pixelization.py", line 90, in pair_dpsi_data_mesh
    return dpsi_mesh.PairRegularDpsiMesh(mask, pixel_scale, self.mesh.factor)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoLens/autolens/potential_correction/mesh.py", line 99, in __init__
    self.get_itp_box_ctr()
  File "/home/jammy/Code/PyAutoLabs/PyAutoLens/autolens/potential_correction/mesh.py", line 132, in get_itp_box_ctr
    raise ValueError(
ValueError: The dpsi grid is too sparse. Try decreasing the dpsi_factor to smaller values.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/potential_correction/likelihood_function.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/potential_correction/likelihood_function.py']' returned non-zero exit s
  - **Recently modified** in [feat: cluster/group examples on Lenstool-native dPIE default + reference-anchored SLaM scaling](https://github.com/PyAutoLabs/autolens_workspace/pull/287)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
    visibility-space specifics that the noise normalization and $\chi^2$ run over the real **and** imaginary parts:
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/potential_correction/likelihood_function.py", line 196, in <module>
    pair = al.pc.PairRegularDpsiMesh(dpsi_mask, pixel_scale=0.1, dpsi_factor=2)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoLens/autolens/potential_correction/mesh.py", line 99, in __init__
    self.get_itp_box_ctr()
  File "/home/jammy/Code/PyAutoLabs/PyAutoLens/autolens/potential_correction/mesh.py", line 132, in get_itp_box_ctr
    raise ValueError(
ValueError: The dpsi grid is too sparse. Try decreasing the dpsi_factor to smaller values.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_grad/imaging_pixelization.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_grad/imaging_pixelization.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
                  Input array_2d_slim.shape = 256
                Input mask_2d.pixels_in_mask = 441
                Input mask_2d.shape_native = (21, 21)
                
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_grad/imaging_pixelization.py", line 84, in <module>
    subprocess.run(
  File "/usr/lib/python3.12/subprocess.py", line 571, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/home/jammy/venv/PyAuto/bin/python3', 'scripts/jax_likelihood_functions/imaging/simulator.py']' returned non-zero exit status 1.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/multi/dataset_model_parity_delaunay.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/multi/dataset_model_parity_delaunay.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
    File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 921, in assert_array_compare
    raise AssertionError(msg)
AssertionError: 
Not equal to tolerance rtol=1e-07, atol=0.2
Delaunay A0 != A1: profile-baked fits to two datasets of the same physical scene disagree by more than the pixel-sampling floor.
Mismatched elements: 1 / 1 (100%)
Max absolute difference among violations: 91.98521689
Max relative difference among violations: 0.32450508
 ACTUAL: array(-191.477885)
 DESIRED: array(-283.463101)
  ```
  </details>

### Workspace Issues (2)

- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/multi/features/imaging_and_point_source/modeling.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/multi/features/imaging_and_point_source/modeling.py']' returned non-zero exit status 1.
  - **Recently modified** in [Add MGE point-source example to multi_gaussian_expansion modeling](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/130)
  - **Recently modified** in [feat: cluster/group examples on Lenstool-native dPIE default + reference-anchored SLaM scaling](https://github.com/PyAutoLabs/autolens_workspace/pull/287)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/multi/features/imaging_and_point_source/modeling.py", line 161, in <module>
    quasar_image_circles |= distances < quasar_mask_radius
ValueError: operands could not be broadcast together with shapes (200,200) (16,16) (200,200)
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/visualization.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/visualization.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/visualization.py", line 171, in <module>
    assert_png("visualization_overlaid_positions.png")
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/visualization.py", line 141, in assert_png
    assert path.exists(), f"{filename} missing"
           ^^^^^^^^^^^^^
AssertionError: visualization_overlaid_positions.png missing
  ```
  </details>

### Timeouts (5)

- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/aggregator/galaxies.py`
  - Timed out after 431s
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/cluster/start_here.py`
  - Timed out after 300s
  - **Recently modified** in [feat: cluster/group examples on Lenstool-native dPIE default + reference-anchored SLaM scaling](https://github.com/PyAutoLabs/autolens_workspace/pull/287)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/advanced/potential_correction.py`
  - Timed out after 300s
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/weak/features/strong_lensing/a2744.py`
  - Timed out after 300s
  - **Recently modified** in [feat: cluster/group examples on Lenstool-native dPIE default + reference-anchored SLaM scaling](https://github.com/PyAutoLabs/autolens_workspace/pull/287)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/potential_correction/subhalo_recovery.py`
  - Timed out after 300s

### Missing Data Files (3)

- `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_1_introduction/tutorial_3_fitting.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_1_introduction/tutorial_3_fitting.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
             ^^^^^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/astropy/io/fits/hdu/hdulist.py", line 1193, in _readfrom
    fileobj = _File(
              ^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/astropy/io/fits/file.py", line 239, in __init__
    self._open_filename(fileobj, mode, overwrite)
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/astropy/io/fits/file.py", line 711, in _open_filename
    self._file = open(self.name, IO_FITS_MODES[mode])
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'dataset/imaging/simple/data.fits'
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_0_visualization.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_0_visualization.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
             ^^^^^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/astropy/io/fits/hdu/hdulist.py", line 1193, in _readfrom
    fileobj = _File(
              ^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/astropy/io/fits/file.py", line 239, in __init__
    self._open_filename(fileobj, mode, overwrite)
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/astropy/io/fits/file.py", line 711, in _open_filename
    self._file = open(self.name, IO_FITS_MODES[mode])
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'dataset/imaging/simple__no_lens_light/data.fits'
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_7_fitting.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_7_fitting.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
             ^^^^^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/astropy/io/fits/hdu/hdulist.py", line 1193, in _readfrom
    fileobj = _File(
              ^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/astropy/io/fits/file.py", line 239, in __init__
    self._open_filename(fileobj, mode, overwrite)
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/astropy/io/fits/file.py", line 711, in _open_filename
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
| `modeling.py` | SLOW 2026-07-14 - real-search JAX shapelet fit exceeds the 1800s mode=release cap (>30min); speedup tracked by the Profiling Agent (PyAutoHeart#72). Not a bug. |
| `modeling.py` | NEEDS_FIX 2026-04-10 - KeyError on ('galaxies','galaxy','bulge','ell_comps'...) kwargs after API drift in top-level imaging/modeling.py |
| `likelihood_function.py` | NEEDS_FIX 2026-05-20 - LinAlgError: matrix singular in MGE inversion -> InversionException (known_numerical; same family as pixelization variants above) |
| `modeling.py` | NEEDS_FIX 2026-04-10 - LinAlgError: matrix not positive definite in interferometer pixelization modeling |
| `mge.py` | SLOW 2026-07-14 - finite-difference JAX interferometer MGE gradient; flakes at the 1800s cap (PyAutoHeart#74) |
| `mge.py` | SLOW 2026-07-14 - finite-difference JAX multi-band MGE gradient; flakes at the 1800s cap (PyAutoHeart#74) |
| `delaunay_mge.py` | SLOW 2026-07-14 - real-search JAX imaging Delaunay-MGE likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| `delaunay.py` | SLOW 2026-07-14 - real-search JAX interferometer Delaunay likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| `delaunay_mge.py` | SLOW 2026-07-14 - real-search JAX interferometer Delaunay-MGE likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| `mge.py` | SLOW 2026-07-14 - real-search JAX interferometer MGE likelihood; flakes at the 1800s mode=release cap (PyAutoHeart#74) |
| `mge_group.py` | SLOW 2026-07-14 - real-search JAX interferometer MGE-group likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| `rectangular_mge.py` | SLOW 2026-07-14 - real-search JAX interferometer rectangular-MGE likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| `delaunay_mge.py` | SLOW 2026-07-14 - real-search JAX Delaunay-MGE multi-band likelihood is borderline against the 1800s mode=release cap (its autolens_workspace_test sibling times out); skipped to keep release-validation deterministic. Speedup tracked by the Profiling Agent (PyAutoHeart#72). Not a bug. |
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
| `interferometer.py` | SLOW 2026-07-14 - finite-difference JAX interferometer gradient; flakes at the 1800s cap (PyAutoHeart#74) |
| `delaunay.py` | SLOW 2026-07-14 - real-search JAX datacube Delaunay likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| `shared_preloads.py` | SLOW 2026-07-14 - real-search JAX datacube shared-preloads likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| `delaunay_mge.py` | NEEDS_FIX 2026-04-10 - timeout in JAX likelihood function benchmark |
| `mge_group.py` | NEEDS_FIX 2026-04-10 - timeout in JAX likelihood function benchmark |
| `delaunay.py` | SLOW 2026-07-14 - real-search JAX interferometer Delaunay likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| `delaunay_mge.py` | SLOW 2026-07-14 - real-search JAX interferometer Delaunay-MGE likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| `mge.py` | SLOW 2026-07-14 - real-search JAX interferometer MGE likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| `mge_group.py` | SLOW 2026-07-14 - real-search JAX interferometer MGE-group likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| `rectangular_mge.py` | SLOW 2026-07-14 - real-search JAX interferometer rectangular-MGE likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| `delaunay_mge.py` | SLOW 2026-07-14 - real-search JAX Delaunay-MGE multi-band likelihood exceeds the 1800s mode=release cap; speedup tracked by the Profiling Agent (PyAutoHeart#72). Not a bug. |
| `shared_preloads.py` | SLOW 2026-07-14 - real-search JAX multi-band shared-preloads likelihood; flakes at the 1800s mode=release cap (PyAutoHeart#74) |
| `modeling_visualization_jit.py` | SLOW 2026-07-08 - JIT + Part-2 live Nautilus fit exceeds 300s cap; same family as imaging/interferometer modeling_visualization_jit (the zero_contour perf-assert false-positive was separately fixed to a cold/warm ratio, which now lets the script run past it into the slow fit) |
| `tutorial_5_results_and_samples.py` | NEEDS_FIX 2026-04-10 - IndexError in samples access, likely related to InstanceInterpolator bug in autofit features/interpolate |
| `tutorial_searches.py` | No reason documented |
| `tutorial_5_borders.py` | Cant get right masks, need proper update. |
| `tutorial_searches.py` | No reason documented |

## Changes Since Last Release

### [docs: pin Fitness's NaN guard contract — value-only, never gradient](https://github.com/PyAutoLabs/PyAutoFit/pull/1392) (PyAutoLabs/PyAutoFit)
**API Changes:** **None.** Docstring and comment only; no signature, behaviour or public-surface change. Downstream workspaces need no migration.

<details>
<summary>Detail</summary>

- Removed: none
- Added: none
- Renamed: none
- Changed Signature: none
- Changed Behaviour: none — `Fitness.call` is byte-for-byte e

### [refactor: public AbstractPaths.preserve_in_zip for post-completion artifacts (#1389)](https://github.com/PyAutoLabs/PyAutoFit/pull/1390) (PyAutoLabs/PyAutoFit)
**API Changes:** Added `AbstractPaths.preserve_in_zip(file_path)`: no-op when the zip does not exist; idempotent on existing members; arcname relative to `output_path`. No existing behaviour changes.

### [fix: mark test-mode bypassed fits complete so they are resumable (#1387)](https://github.com/PyAutoLabs/PyAutoFit/pull/1388) (PyAutoLabs/PyAutoFit)
**API Changes:** None — behavioural fix only: a bypassed fit now leaves a `.completed` marker (zipped with the output), making test-mode pipelines resumable like production ones.

### [fix: AggregateFITS leaked one file handle per HDU per result (crash at ~500 results)](https://github.com/PyAutoLabs/PyAutoFit/pull/1386) (PyAutoLabs/PyAutoFit)
**API Changes:** None — bug fix only: no behaviour change other than handles being closed (and `extract_csv` tables being materialised rather than possibly memmap-backed).
See full details below.

### [fix: from_dict dropped dict entries with falsy values (0.0 parameters vanish on load)](https://github.com/PyAutoLabs/PyAutoFit/pull/1384) (PyAutoLabs/PyAutoFit)
**API Changes:** None — bug fix only: `from_dict` on a serialized dict now keeps entries whose value is `0.0`/`False`/`""` and drops only `None` (the original intent of the filter).
See full details below.

### [feat: opt-in gradient-safe log-det via Settings (default unchanged)](https://github.com/PyAutoLabs/PyAutoArray/pull/392) (PyAutoLabs/PyAutoArray)
**API Changes:** Additive only. New optional `Settings(log_det_method=...)` field, default `None` → config `"cholesky"` → current behaviour. No removed/renamed/changed symbols; no downstream migration.

<details>
<summary>Detail</summary>

- Added: `Settings.log_det_method` (optional kwarg + property); `AbstractInve

### [feat: masked-grid derivative operators + mask regularizations (potential correction phase 1)](https://github.com/PyAutoLabs/PyAutoArray/pull/390) (PyAutoLabs/PyAutoArray)
**API Changes:** Added only — nothing removed or changed. Two new regularization classes, `aa.reg.CurvatureMask` and `aa.reg.FourthOrderMask`, regularize linear objects defined on rectangular masked grids (the linear object must expose its `mask`). Two new util modules, `aa.util.derivative` (masked-grid sparse deriv

### [fix: pin tfp-nightly for JAX Matern-kernel path (tfp 0.25.0 × jax 0.10.2 crash)](https://github.com/PyAutoLabs/PyAutoArray/pull/386) (PyAutoLabs/PyAutoArray)
**API Changes:** None — public surface unchanged.

Fixes #385

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01TDCsgNCXacXqiWAPTswWCt

### [feat: make Lenstool-native parameterization the default dPIE profile](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/509) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** Breaking rename-swap of the dPIE family (no numerical/physics changes):
- `dPIEMass` / `dPIEMassSph` are now the Lenstool-native parameterized classes (formerly `dPIEMassLenstool` / `dPIEMassLenstoolSph`).
- The internal `(ra, rs, b0)` classes are renamed `dPIEMassB0` / `dPIEMassB0Sph`; `from_lensto

### [feat: zero-fill extrapolation for input pixelized mass profiles](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/508) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** Added only: the `fill` parameter on `ag.mp.LinearNDInterpolatorExt` and the `extrapolate` parameter on `ag.mp.InputPotential` / `ag.mp.InputDeflections` (defaults preserve existing behaviour).
See full details below.

### [refactor: use paths.preserve_in_zip for the galaxy-image cache (#1389 phase 2)](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/507) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** None public. Private `_append_to_search_zip` removed from `autogalaxy/analysis/adapt_images/adapt_images.py` (its one external consumer, PyAutoLens, switches in the companion PR).

### [feat: input pixelized mass profiles (potential correction phase 2)](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/505) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** Added only — nothing removed or changed. Three new mass profiles under `ag.mp`: `InputDeflections`, `InputPotential` and `GaussianRandomField` (data-holding profiles constructed from arrays/masks, not free-parameter model components), plus the `LinearNDInterpolatorExt` interpolation helper.
See full

### [feat: cache per-galaxy result images for SLaM resume fast-path (#502)](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/504) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** None — no public API changes. Behaviour of `galaxy_name_image_dict_via_result_from` is identical on first computation; later calls return equal values from disk. New side effect: two FITS cache files written into a result's `files/` folder (and its zip) when the result has on-disk output.

<details>

### [feat: PowerLawIntermediate — intermediate-axis (COOLEST) Einstein radius power-law](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/503) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** Added only — `ag.mp.PowerLawIntermediate`, the `einstein_radius_major_from` hook (identity for existing profiles), and an optional `intermediate` kwarg on `interop.coolest.mass_profile_from`. No existing symbol's behaviour changes (full suite is the regression net).
See full details below.

### [fix: interferometer LM objective double-counting + warm start (mid-tier certified)](https://github.com/PyAutoLabs/PyAutoLens/pull/629) (PyAutoLabs/PyAutoLens)
**API Changes:** Added `x0=` on `solve_joint_optimization`; behaviour fix in the LM objective (cold-start results change slightly — they were computed under the inconsistent objective).
See commit for detail.

### [feat: per-iteration evidence re-optimization for the interferometer LM engine](https://github.com/PyAutoLabs/PyAutoLens/pull/628) (PyAutoLabs/PyAutoLens)
**API Changes:** Added only: `reg_optimize_every` / `reg_optimize_grid` parameters (default off — behaviour unchanged) and the `reg_scales` attribute.
See full details below.

### [fix: Marquardt-scaled LM damping + zero-fill correction profiles](https://github.com/PyAutoLabs/PyAutoLens/pull/626) (PyAutoLabs/PyAutoLens)
**API Changes:** Behaviour change (internal numerics): the LM damping in `al.pc.dense_util.solve_lm_step_from` is now Marquardt-scaled; identical solutions at convergence, different damping trajectories. No signatures changed.
See full details below.

### [config: adopt version.minimum_library_version floor (2026.7.9.1)](https://github.com/PyAutoLabs/autofit_workspace/pull/97) (PyAutoLabs/autofit_workspace)
**API Changes:** None — workspace config only.

### [docs: note PYAUTO_TEST_MODE_SAMPLES in AGENTS.md](https://github.com/PyAutoLabs/autofit_workspace/pull/96) (PyAutoLabs/autofit_workspace)
**Scripts Changed:** None — AGENTS.md only.

Generated by the PyAutoLabs agent workflow.

### [config: adopt version.minimum_library_version floor (2026.7.9.1)](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/134) (PyAutoLabs/autogalaxy_workspace)
**API Changes:** None — workspace config only.

### [Add MGE point-source example to multi_gaussian_expansion modeling](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/130) (PyAutoLabs/autogalaxy_workspace)
**Scripts Changed:** - `scripts/imaging/features/multi_gaussian_expansion/modeling.py` (+ regenerated
  `notebooks/.../modeling.ipynb`, `llms-full.txt`, `workspace_index.json`)

Notebook regenerated via PyAutoBuild; unrelated pre-existing notebook drift on `main` was reverted
to keep this PR focused.

### [config: adopt version.minimum_library_version floor (2026.7.9.1)](https://github.com/PyAutoLabs/autolens_workspace/pull/288) (PyAutoLabs/autolens_workspace)
**API Changes:** None — workspace config only.

### [feat: cluster/group examples on Lenstool-native dPIE default + reference-anchored SLaM scaling](https://github.com/PyAutoLabs/autolens_workspace/pull/287) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** **Cluster suite — modeled in σ_LT-space (Lenstool `.par` parameters, priors in km/s / arcsec):**
- `cluster/simulator.py` — truths now `sigma` (330/210 km/s mains; `sigma_ref = 85` km/s tier), `r_core`/`r_cut`, `redshift_object`/`redshift_source` (final-plane anchored, same convention as `NFWMCRLudl
