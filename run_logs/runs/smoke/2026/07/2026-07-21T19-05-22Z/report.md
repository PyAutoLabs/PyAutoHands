# Release Readiness Report

**Status: NOT READY**

**Run:** `2026-07-21T19-05-22Z`  •  **Path:** `/home/jammy/Code/PyAutoLabs/PyAutoHands/test_results/runs/2026-07-21T19-05-22Z`  •  **Total duration:** 9754.9s

## Slow-Skipped Scripts (needs performance fix)

**44 script(s)** are being skipped because they exceed the 60s per-script timeout cap. These are NOT permanent skips — they need the underlying performance issue fixed and the `SLOW` marker removed from the workspace's `config/build/no_run.yaml`.

| Workspace | Script | Marked | Age | Reason |
|-----------|--------|--------|-----|--------|
| HowToGalaxy | `guides/results/database/start_here` | 2026-04-10 | 102d **STALE** | previously failed fast on a broken aggregator query; now runs the real aggregator and exceeds 60s |
| HowToGalaxy | `guides/results/examples/galaxies_fit` | 2026-04-10 | 102d **STALE** | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| HowToGalaxy | `guides/results/examples/models` | 2026-04-10 | 102d **STALE** | cascade from SLOW-skipped results/start_here.py; aggregator returns NoneType so instance.galaxies is None |
| HowToGalaxy | `guides/results/examples/samples` | 2026-04-10 | 102d **STALE** | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| HowToGalaxy | `guides/results/start_here` | 2026-04-10 | 102d **STALE** | exceeds 60s test timeout; unsets TEST_MODE to produce real samples for downstream examples |
| HowToGalaxy | `guides/results/workflow/csv_make` | 2026-04-10 | 102d **STALE** | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| HowToLens | `guides/results/database/start_here` | 2026-04-10 | 102d **STALE** | previously failed fast on a broken aggregator query; now runs the real aggregator and exceeds 60s |
| HowToLens | `guides/results/examples/queries` | 2026-04-10 | 102d **STALE** | cascade from SLOW-skipped results/start_here.py; stub Model lacks sersic_index attribute |
| HowToLens | `guides/results/examples/samples` | 2026-04-10 | 102d **STALE** | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| HowToLens | `guides/results/examples/samples_via_aggregator` | 2026-04-10 | 102d **STALE** | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| HowToLens | `howtolens/chapter_4_pixelizations/tutorial_10_brightness_adaption` | 2026-04-10 | 102d **STALE** | pixelization tutorial exceeds 60s test timeout |
| autogalaxy_workspace | `guides/results/database/start_here` | 2026-04-10 | 102d **STALE** | previously failed fast on a broken aggregator query; now runs the real aggregator and exceeds 60s |
| autogalaxy_workspace | `guides/results/workflow/csv_make` | 2026-04-10 | 102d **STALE** | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| autogalaxy_workspace | `imaging/features/shapelets/modeling` | 2026-07-14 | 7d | real-search JAX shapelet fit exceeds the 1800s mode=release cap (>30min); speedup tracked by the Profiling Agent (PyAutoHeart#72). Not a bug. |
| autogalaxy_workspace_test | `jax_grad/interferometer/mge.py` | 2026-07-14 | 7d | finite-difference JAX interferometer MGE gradient; flakes at the 1800s cap (PyAutoHeart#74) |
| autogalaxy_workspace_test | `jax_grad/multi/mge.py` | 2026-07-14 | 7d | finite-difference JAX multi-band MGE gradient; flakes at the 1800s cap (PyAutoHeart#74) |
| autogalaxy_workspace_test | `jax_likelihood_functions/imaging/delaunay_mge.py` | 2026-07-14 | 7d | real-search JAX imaging Delaunay-MGE likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| autogalaxy_workspace_test | `jax_likelihood_functions/interferometer/delaunay.py` | 2026-07-14 | 7d | real-search JAX interferometer Delaunay likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| autogalaxy_workspace_test | `jax_likelihood_functions/interferometer/delaunay_mge.py` | 2026-07-14 | 7d | real-search JAX interferometer Delaunay-MGE likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| autogalaxy_workspace_test | `jax_likelihood_functions/interferometer/mge.py` | 2026-07-14 | 7d | real-search JAX interferometer MGE likelihood; flakes at the 1800s mode=release cap (PyAutoHeart#74) |
| autogalaxy_workspace_test | `jax_likelihood_functions/interferometer/mge_group.py` | 2026-07-14 | 7d | real-search JAX interferometer MGE-group likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| autogalaxy_workspace_test | `jax_likelihood_functions/interferometer/rectangular_mge.py` | 2026-07-14 | 7d | real-search JAX interferometer rectangular-MGE likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| autogalaxy_workspace_test | `jax_likelihood_functions/multi/delaunay_mge` | 2026-07-14 | 7d | real-search JAX Delaunay-MGE multi-band likelihood is borderline against the 1800s mode=release cap (its autolens_workspace_test sibling times out); skipped to keep release-validation deterministic. Speedup tracked by the Profiling Agent (PyAutoHeart#72). Not a bug. |
| autolens_workspace | `guides/results/database/start_here` | 2026-04-10 | 102d **STALE** | previously failed fast on a broken aggregator query; now runs the real aggregator and exceeds 60s |
| autolens_workspace_test | `cluster/visualization` | 2026-07-21 | 0d | per-plane critical-curve + caustic computation on the required full-extent 250x250 viz_grid (multi-plane marching squares) totals ~580s, over the 300s cap; same perf family as the modeling_visualization_jit scripts. Curves DO recover (plane-1 7 CC, plane-2 1 CC at full data) and the per-plane physics assertion passes — this is NOT the mislabelled "#1280 zero_contour algorithmic regression", which does not reproduce. env_vars.yaml unsets FAST_PLOTS/SMALL_DATASETS so it runs green in manual/full runs. |
| autolens_workspace_test | `database/scrape/multi_analysis` | 2026-04-10 | 102d **STALE** | exceeds 60s timeout; _test workspaces run full searches without test mode |
| autolens_workspace_test | `database/scrape/slam_general` | 2026-04-10 | 102d **STALE** | exceeds 60s timeout; _test workspaces run full searches without test mode |
| autolens_workspace_test | `database/scrape/slam_multi_one_by_one` | 2026-04-10 | 102d **STALE** | exceeds 60s timeout; _test workspaces run full searches without test mode |
| autolens_workspace_test | `database/scrape/slam_pix` | 2026-04-10 | 102d **STALE** | exceeds 60s timeout; _test workspaces run full searches without test mode |
| autolens_workspace_test | `imaging/modeling_visualization_jit` | 2026-05-07 | 75d **STALE** | JIT + full visualization pipeline exceeds 300s cap (autogalaxy variant ~90s); unblocked by PR #70 from prior `expected jax.Array, got numpy.float64` AssertionError, now hits perf wall |
| autolens_workspace_test | `imaging/modeling_visualization_jit_delaunay` | 2026-05-07 | 75d **STALE** | JIT + full visualization pipeline exceeds 300s cap; same root cause as modeling_visualization_jit |
| autolens_workspace_test | `imaging/modeling_visualization_jit_rectangular` | 2026-05-07 | 75d **STALE** | JIT + full visualization pipeline exceeds 301s cap; same root cause as modeling_visualization_jit |
| autolens_workspace_test | `interferometer/modeling_visualization_jit` | 2026-05-20 | 62d **STALE** | JIT + full visualization pipeline exceeds 300s cap; same root cause as imaging/modeling_visualization_jit family |
| autolens_workspace_test | `jax_grad/interferometer.py` | 2026-07-14 | 7d | finite-difference JAX interferometer gradient; flakes at the 1800s cap (PyAutoHeart#74) |
| autolens_workspace_test | `jax_likelihood_functions/datacube/delaunay.py` | 2026-07-14 | 7d | real-search JAX datacube Delaunay likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| autolens_workspace_test | `jax_likelihood_functions/datacube/shared_preloads.py` | 2026-07-14 | 7d | real-search JAX datacube shared-preloads likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| autolens_workspace_test | `jax_likelihood_functions/interferometer/delaunay.py` | 2026-07-14 | 7d | real-search JAX interferometer Delaunay likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| autolens_workspace_test | `jax_likelihood_functions/interferometer/delaunay_mge.py` | 2026-07-14 | 7d | real-search JAX interferometer Delaunay-MGE likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| autolens_workspace_test | `jax_likelihood_functions/interferometer/mge.py` | 2026-07-14 | 7d | real-search JAX interferometer MGE likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| autolens_workspace_test | `jax_likelihood_functions/interferometer/mge_group.py` | 2026-07-14 | 7d | real-search JAX interferometer MGE-group likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| autolens_workspace_test | `jax_likelihood_functions/interferometer/rectangular_mge.py` | 2026-07-14 | 7d | real-search JAX interferometer rectangular-MGE likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| autolens_workspace_test | `jax_likelihood_functions/multi/delaunay_mge` | 2026-07-14 | 7d | real-search JAX Delaunay-MGE multi-band likelihood exceeds the 1800s mode=release cap; speedup tracked by the Profiling Agent (PyAutoHeart#72). Not a bug. |
| autolens_workspace_test | `jax_likelihood_functions/multi/shared_preloads.py` | 2026-07-14 | 7d | real-search JAX multi-band shared-preloads likelihood; flakes at the 1800s mode=release cap (PyAutoHeart#74) |
| autolens_workspace_test | `point_source/modeling_visualization_jit` | 2026-07-08 | 13d | JIT + Part-2 live Nautilus fit exceeds 300s cap; same family as imaging/interferometer modeling_visualization_jit (the zero_contour perf-assert false-positive was separately fixed to a cold/warm ratio, which now lets the script run past it into the slow fit) |

## Needs-Fix Scripts (parked for investigation)

**11 script(s)** are being skipped because they are broken and parked as a to-do list. These are NOT permanent skips — investigate the failure, fix the underlying bug, and remove the `NEEDS_FIX` marker from the workspace's `config/build/no_run.yaml`.

| Workspace | Script | Marked | Age | Reason |
|-----------|--------|--------|-----|--------|
| HowToFit | `chapter_1_introduction/tutorial_5_results_and_samples` | 2026-04-10 | 102d **STALE** | IndexError in samples access, likely related to InstanceInterpolator bug in autofit features/interpolate |
| HowToGalaxy | `autogalaxy_workspace/scripts/imaging/modeling` | 2026-04-10 | 102d **STALE** | KeyError on ('galaxies','galaxy','bulge','ell_comps'...) kwargs after API drift in top-level imaging/modeling.py |
| HowToGalaxy | `ellipse/modeling` | 2026-04-10 | 102d **STALE** | KeyError on 'ellipses.0.centre_0' kwargs after API drift in ellipse model |
| HowToGalaxy | `guides/advanced/over_sampling` | 2026-04-10 | 102d **STALE** | plot_grid() got unexpected kwarg 'plot_grid_lines' after plotter API drift |
| HowToLens | `group/slam` | 2026-04-10 | 102d **STALE** | PriorException: upper limit must be greater than lower limit in group SLaM pipeline |
| autofit_workspace | `features/interpolate` | 2026-04-10 | 102d **STALE** | IndexError in InstanceInterpolator.__getitem__ when querying time == 1.5; value_map lookup falls through to empty instances list |
| autogalaxy_workspace | `autogalaxy_workspace/scripts/imaging/modeling` | 2026-04-10 | 102d **STALE** | KeyError on ('galaxies','galaxy','bulge','ell_comps'...) kwargs after API drift in top-level imaging/modeling.py |
| autolens_workspace | `group/slam` | 2026-04-10 | 102d **STALE** | PriorException: upper limit must be greater than lower limit in group SLaM pipeline |
| autolens_workspace_test | `database/scrape/general` | 2026-04-27 | 85d **STALE** | PyAutoGalaxy abstract_fit.linear_light_profile_intensity_dict raises "TypeError: __hash__ method should return an integer" during subplot_fit_imaging after the search completes (a light-profile object's __hash__ returns a non-int). Surfaced once the dataset_label="build" path fix let the script progress past Imaging.from_fits. |
| autolens_workspace_test | `jax_likelihood_functions/imaging/delaunay_mge` | 2026-04-10 | 102d **STALE** | timeout in JAX likelihood function benchmark |
| autolens_workspace_test | `jax_likelihood_functions/imaging/mge_group` | 2026-04-10 | 102d **STALE** | timeout in JAX likelihood function benchmark |

## Summary

| Passed | Failed | Skipped | Timeout |
|--------|--------|---------|---------|
| 646 | 13 | 78 | 5 |

## Per-Project Breakdown

| Project | Passed | Failed | Skipped | Timeout | Duration |
|---------|--------|--------|---------|---------|----------|
| autofit | 27 | 0 | 6 | 0 | 87.2s |
| autofit_test | 43 | 4 | 2 | 0 | 246.2s |
| autogalaxy | 110 | 1 | 11 | 0 | 889.8s |
| autogalaxy_test | 46 | 0 | 9 | 0 | 789.7s |
| autolens | 242 | 5 | 23 | 3 | 4081.0s |
| autolens_test | 95 | 3 | 23 | 2 | 2562.8s |
| euclid | 5 | 0 | 0 | 0 | 167.5s |
| howtofit | 15 | 0 | 1 | 0 | 58.8s |
| howtogalaxy | 25 | 0 | 1 | 0 | 315.0s |
| howtolens | 38 | 0 | 2 | 0 | 556.9s |

## Slowest scripts (top 25)

| Script | Project | Status | Duration | Share |
|--------|---------|--------|----------|-------|
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/advanced/potential_correction.py` | autolens | timeout | 300.4s | 3.1% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/potential_correction/subhalo_recovery.py` | autolens_test | timeout | 300.3s | 3.1% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_grad/imaging_pixelization.py` | autolens_test | timeout | 300.2s | 3.1% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/cluster/start_here.py` | autolens | timeout | 300.1s | 3.1% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/weak/features/strong_lensing/a2744.py` | autolens | timeout | 300.1s | 3.1% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/start_here.py` | autolens | passed | 146.1s | 1.5% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/cluster/lenstool/modeling.py` | autolens | passed | 132.8s | 1.4% |
| `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_4_pixelizations/tutorial_10_brightness_adaption.py` | howtolens | passed | 127.8s | 1.3% |
| `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_4_pixelizations/tutorial_4_bayesian_regularization.py` | howtogalaxy | passed | 97.2s | 1.0% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/units/flux.py` | autolens | passed | 88.0s | 0.9% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/visualization_jax.py` | autolens_test | passed | 86.5s | 0.9% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/profiles/light_and_mass_profiles.py` | autolens | passed | 84.1s | 0.9% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/multi_gaussian_expansion/modeling.py` | autolens | passed | 79.0s | 0.8% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/multi/mge_group.py` | autolens_test | passed | 78.3s | 0.8% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/multi/start_here.py` | autolens | passed | 75.1s | 0.8% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/subhalo.py` | autolens_test | passed | 70.6s | 0.7% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/start_here.py` | autolens | passed | 69.8s | 0.7% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_mge.py` | autolens_test | passed | 68.8s | 0.7% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/database/scrape/scaling_relation.py` | autolens_test | passed | 64.3s | 0.7% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/start_here.py` | autolens | passed | 62.0s | 0.6% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/visualization_jax.py` | autolens_test | passed | 60.2s | 0.6% |
| `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_dspl.py` | autolens_test | passed | 59.6s | 0.6% |
| `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/prior_correctness/emcee_gaussian_bias_check.py` | autofit_test | passed | 59.3s | 0.6% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/imaging/visualization.py` | autogalaxy_test | passed | 53.4s | 0.5% |
| `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/multi/mge_group.py` | autogalaxy_test | passed | 52.0s | 0.5% |

## Failures by Classification

### Source Code Bugs (9)

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
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation/manual/mask_irregular.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation/manual/mask_irregular.py']' returned non-zero exit status 1.
  - **Recently modified** in [chore: un-park mask_irregular no_run marker (bug already fixed)](https://github.com/PyAutoLabs/autolens_workspace/pull/304)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
                  the mask.

                This indicates that the number of unmaksed pixels in the mask  is different to the input slim array 
                shape.

                The shapes of the two arrays (which this exception is raised because they are different) are as follows:

                Input array_2d_slim.shape = 256
                Input mask_2d.pixels_in_mask = 961
                Input mask_2d.shape_native = (31, 31)
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/double_einstein_ring/slam.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/double_einstein_ring/slam.py']' returned non-zero exit status 1.
  - **Recently modified** in [chore: un-park group/slam (stale NEEDS_FIX, bug fixed)](https://github.com/PyAutoLabs/autolens_workspace/pull/312)
  - **Recently modified** in [fix: SLaM advanced-pipeline inversion + adapt-image cascade (#300)](https://github.com/PyAutoLabs/autolens_workspace/pull/302)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
    File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/inversion/regularization/adapt.py", line 210, in regularization_weights_from
    pixel_signals = linear_obj.pixel_signals_from(
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/inversion/mappers/abstract.py", line 469, in pixel_signals_from
    return mapper_util.adaptive_pixel_signals_from(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/inversion/mappers/mapper_util.py", line 62, in adaptive_pixel_signals_from
    flat_data_vals = xp.take(adapt_data[slim_index_for_sub_slim_index], I_sub, axis=0)
                             ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
IndexError: index 177 is out of bounds for axis 0 with size 177
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/data_preparation/manual/mask_irregular.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/data_preparation/manual/mask_irregular.py']' returned non-zero exit status 1.
  - **Recently modified** in [chore: un-park mask_irregular no_run marker (bug already fixed)](https://github.com/PyAutoLabs/autolens_workspace/pull/304)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
                  the mask.

                This indicates that the number of unmaksed pixels in the mask  is different to the input slim array 
                shape.

                The shapes of the two arrays (which this exception is raised because they are different) are as follows:

                Input array_2d_slim.shape = 256
                Input mask_2d.pixels_in_mask = 961
                Input mask_2d.shape_native = (31, 31)
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/double_einstein_ring/slam.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/double_einstein_ring/slam.py']' returned non-zero exit status 1.
  - **Recently modified** in [chore: un-park group/slam (stale NEEDS_FIX, bug fixed)](https://github.com/PyAutoLabs/autolens_workspace/pull/312)
  - **Recently modified** in [fix: SLaM advanced-pipeline inversion + adapt-image cascade (#300)](https://github.com/PyAutoLabs/autolens_workspace/pull/302)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
    File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/inversion/regularization/adapt.py", line 210, in regularization_weights_from
    pixel_signals = linear_obj.pixel_signals_from(
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/inversion/mappers/abstract.py", line 469, in pixel_signals_from
    return mapper_util.adaptive_pixel_signals_from(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/inversion/mappers/mapper_util.py", line 62, in adaptive_pixel_signals_from
    flat_data_vals = xp.take(adapt_data[slim_index_for_sub_slim_index], I_sub, axis=0)
                             ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
IndexError: index 177 is out of bounds for axis 0 with size 177
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/potential_correction/start_here.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/potential_correction/start_here.py']' returned non-zero exit status 1.
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
  - **Recently modified** in [fix: un-park pixelization/MGE scripts (stale NEEDS_FIX, now green)](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/141)
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
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/model_fit.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/model_fit.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/model_fit.py", line 256, in <module>
    aplt.corner_cornerpy(samples=result.samples)
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/plot/plot_util.py", line 18, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/plot/samples_plotters.py", line 35, in corner_cornerpy
    data = np.asarray(samples.parameter_lists)
                      ^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'parameter_lists'
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/latent/latent_variables_smoke.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/latent/latent_variables_smoke.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
    File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/latent/latent_variables_smoke.py", line 66, in <module>
    latent_samples = analysis.compute_latent_samples(result.samples)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/analysis/analysis.py", line 144, in compute_latent_samples
    return latent_samples_from(self, samples, batch_size=batch_size)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/analysis/latent.py", line 113, in latent_samples_from
    latent.variables, analysis, model=samples.model
                                      ^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'model'
  ```
  </details>

### Workspace Issues (4)

- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/jax_assertions/multi_start_gradient_auto_convergence.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/jax_assertions/multi_start_gradient_auto_convergence.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/jax_assertions/multi_start_gradient_auto_convergence.py", line 105, in <module>
    total_steps = int(result.samples.samples_info["total_steps"])
                      ~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^
KeyError: 'total_steps'
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/searches/MultiStartProdigy.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/searches/MultiStartProdigy.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/searches/MultiStartProdigy.py", line 113, in <module>
    assert abs(instance.normalization - 25.0) < 3.0, instance.normalization
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 1.0
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/searches/MultiStartResurrect.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/searches/MultiStartResurrect.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/searches/MultiStartResurrect.py", line 94, in <module>
    f"sigma={off[2]:.3f}  (n_resurrections={info_off['n_resurrections']})"
                                            ~~~~~~~~^^^^^^^^^^^^^^^^^^^
KeyError: 'n_resurrections'
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/latent/latent_nan_robustness.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/latent/latent_nan_robustness.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/latent/latent_nan_robustness.py", line 80, in <module>
    assert len(result.samples.sample_list) > LATENT_BATCH_SIZE, (
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'sample_list'
  ```
  </details>

### Timeouts (5)

- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/cluster/start_here.py`
  - Timed out after 300s
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/advanced/potential_correction.py`
  - Timed out after 300s
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/weak/features/strong_lensing/a2744.py`
  - Timed out after 300s
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_grad/imaging_pixelization.py`
  - Timed out after 300s
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/potential_correction/subhalo_recovery.py`
  - Timed out after 300s

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
| `modeling.py` | SLOW 2026-07-14 - real-search JAX shapelet fit exceeds the 1800s mode=release cap (>30min); speedup tracked by the Profiling Agent (PyAutoHeart#72). Not a bug. |
| `modeling.py` | NEEDS_FIX 2026-04-10 - KeyError on ('galaxies','galaxy','bulge','ell_comps'...) kwargs after API drift in top-level imaging/modeling.py |
| `mge.py` | SLOW 2026-07-14 - finite-difference JAX interferometer MGE gradient; flakes at the 1800s cap (PyAutoHeart#74) |
| `mge.py` | SLOW 2026-07-14 - finite-difference JAX multi-band MGE gradient; flakes at the 1800s cap (PyAutoHeart#74) |
| `delaunay_mge.py` | SLOW 2026-07-14 - real-search JAX imaging Delaunay-MGE likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| `delaunay.py` | SLOW 2026-07-14 - real-search JAX interferometer Delaunay likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| `delaunay_mge.py` | SLOW 2026-07-14 - real-search JAX interferometer Delaunay-MGE likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| `mge.py` | SLOW 2026-07-14 - real-search JAX interferometer MGE likelihood; flakes at the 1800s mode=release cap (PyAutoHeart#74) |
| `mge_group.py` | SLOW 2026-07-14 - real-search JAX interferometer MGE-group likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| `rectangular_mge.py` | SLOW 2026-07-14 - real-search JAX interferometer rectangular-MGE likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| `delaunay_mge.py` | SLOW 2026-07-14 - real-search JAX Delaunay-MGE multi-band likelihood is borderline against the 1800s mode=release cap (its autolens_workspace_test sibling times out); skipped to keep release-validation deterministic. Speedup tracked by the Profiling Agent (PyAutoHeart#72). Not a bug. |
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
| `modeling.py` | Requires CSE to be JAX enabled. |
| `slam.py` | Requires CSE to be JAX enabled. |
| `database.py` | Unsure but not a feature actively used currently. |
| `slam_source_parametric.py` | All sensitivity scripts need updating when visualization refactored. |
| `slam_source_pixelized.py` | All sensitivity scripts need updating when visualization refactored. |
| `casa_reduction.py` | Requires CASA MeasurementSet output, not runnable standalone |
| `simulator.py` | Blocked by PyAutoLens #480: solver finds 0 positions for intermediate-plane source |
| `modeling.py` | Blocked by PyAutoLens #480: same root cause as simulator above |
| `time_delays.py` | Test mode does not support cosmology ift |
| `visualization.py` | SLOW 2026-07-21 - per-plane critical-curve + caustic computation on the required full-extent 250x250 viz_grid (multi-plane marching squares) totals ~580s, over the 300s cap; same perf family as the modeling_visualization_jit scripts. Curves DO recover (plane-1 7 CC, plane-2 1 CC at full data) and the per-plane physics assertion passes — this is NOT the mislabelled "#1280 zero_contour algorithmic regression", which does not reproduce. env_vars.yaml unsets FAST_PLOTS/SMALL_DATASETS so it runs green in manual/full runs. |
| `general.py` | NEEDS_FIX 2026-04-27 - PyAutoGalaxy abstract_fit.linear_light_profile_intensity_dict raises "TypeError: __hash__ method should return an integer" during subplot_fit_imaging after the search completes (a light-profile object's __hash__ returns a non-int). Surfaced once the dataset_label="build" path fix let the script progress past Imaging.from_fits. |
| `multi_analysis.py` | SLOW 2026-04-10 - exceeds 60s timeout; _test workspaces run full searches without test mode |
| `slam_general.py` | SLOW 2026-04-10 - exceeds 60s timeout; _test workspaces run full searches without test mode |
| `slam_multi_one_by_one.py` | SLOW 2026-04-10 - exceeds 60s timeout; _test workspaces run full searches without test mode |
| `slam_pix.py` | SLOW 2026-04-10 - exceeds 60s timeout; _test workspaces run full searches without test mode |
| `modeling_visualization_jit.py` | SLOW 2026-05-07 - JIT + full visualization pipeline exceeds 300s cap (autogalaxy variant ~90s); unblocked by PR #70 from prior `expected jax.Array, got numpy.float64` AssertionError, now hits perf wall |
| `modeling_visualization_jit_delaunay.py` | SLOW 2026-05-07 - JIT + full visualization pipeline exceeds 300s cap (autogalaxy variant ~90s); unblocked by PR #70 from prior `expected jax.Array, got numpy.float64` AssertionError, now hits perf wall |
| `modeling_visualization_jit_rectangular.py` | SLOW 2026-05-07 - JIT + full visualization pipeline exceeds 300s cap (autogalaxy variant ~90s); unblocked by PR #70 from prior `expected jax.Array, got numpy.float64` AssertionError, now hits perf wall |
| `modeling_visualization_jit.py` | SLOW 2026-05-20 - JIT + full visualization pipeline exceeds 300s cap; same root cause as imaging/modeling_visualization_jit family |
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

### [feat(autofit): multi-start gradient convergence results contract (phase 2)](https://github.com/PyAutoLabs/PyAutoFit/pull/1410) (PyAutoLabs/PyAutoFit)
**API Changes:** Additive, plus one shared-`Samples` correctness fix. **Added:** `converged` / `stop_reason` / `convergence` / `fom_history` to the multi-start gradient `samples_info`; a `figure_of_merit_vs_iteration` MLE plotter (+ `plots_search.yaml` toggle) drawing the global-best figure-of-merit trace so the pla

### [fix: test-mode bypass tolerates a single-eval FitException (resample-equivalent)](https://github.com/PyAutoLabs/PyAutoFit/pull/1408) (PyAutoLabs/PyAutoFit)
**API Changes:** None. Behaviour change is confined to the `TEST_MODE=2` bypass path; public API, signatures, and normal-search behaviour are unchanged. No downstream workspace migration required.

### [feat(autofit): multi-start gradient auto-convergence (phase 1)](https://github.com/PyAutoLabs/PyAutoFit/pull/1407) (PyAutoLabs/PyAutoFit)
**API Changes:** Additive, plus one default-behaviour change. **Added:** `af.MultiStartGradientConvergence` settings object and a `convergence=` parameter on all four multi-start gradient searches (defaults to auto-convergence ON). **Changed behaviour:** the searches now stop early by default once the global-best fi

### [fix: Aggregator.from_directory test-mode-aware (interpolate tutorial IndexError)](https://github.com/PyAutoLabs/PyAutoFit/pull/1402) (PyAutoLabs/PyAutoFit)
**API Changes:** None affecting real runs — internal test-mode recovery only. The `from_directory` signature is unchanged and non-test-mode behaviour is byte-for-byte identical. In test mode only, an empty first scan now retries once against the `test_mode` sibling directory.
See full details below.

### [feat(autofit): restart-on-death (resurrection) for multi-start gradient search](https://github.com/PyAutoLabs/PyAutoFit/pull/1400) (PyAutoLabs/PyAutoFit)
**API Changes:** - **Added** a `resurrect: bool = False` constructor argument on `af.AbstractMultiStartGradient` (inherited by all `MultiStart*` searches). Default `False` → no behaviour change.
- **Added** an `n_resurrections` diagnostic to `search_internal` and `samples_info`.

No migration required — the new argu

### [feat(autofit): MultiStartProdigy + optax.contrib + per-start vmapped state](https://github.com/PyAutoLabs/PyAutoFit/pull/1398) (PyAutoLabs/PyAutoFit)
**API Changes:** - **Added** `af.MultiStartProdigy` — a learning-rate-free multi-start gradient MAP search (`optax.contrib.prodigy`).
- **Added** a `max_consecutive_nan: int = 8` constructor argument on `af.AbstractMultiStartGradient` (inherited by all `MultiStart*` searches) — the `apply_if_finite` per-start reject

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

### [fix: SersicCore.intensity_prime ZeroDivisionError on effective_radius=0 (#514)](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/515) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** No signature changes. One **behaviour** change:

<details>
<summary>Changed Behaviour</summary>

- `SersicCore.intensity_prime()` (and hence `SersicCore` / `SersicCoreSph` image evaluation) with `effective_radius <= 0` now returns a **non-finite** value (`inf`/`nan`) instead of raising `ZeroDivision

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

### [fix: analysis log_likelihood_function preserves the cause behind FitException](https://github.com/PyAutoLabs/PyAutoLens/pull/639) (PyAutoLabs/PyAutoLens)
**API Changes:** **Changed Behaviour**
- `AnalysisImaging` / `AnalysisInterferometer` / `AnalysisPoint`
  `log_likelihood_function` (numpy path): a fit failure is still re-raised as
  `af.exc.FitException`, but now with the original exception preserved as
  `__cause__` (`raise ... from e`). No change to when/whether

### [fix: interferometer LM objective double-counting + warm start (mid-tier certified)](https://github.com/PyAutoLabs/PyAutoLens/pull/629) (PyAutoLabs/PyAutoLens)
**API Changes:** Added `x0=` on `solve_joint_optimization`; behaviour fix in the LM objective (cold-start results change slightly — they were computed under the inconsistent objective).
See commit for detail.

### [chore: un-park features/interpolate (stale NEEDS_FIX, bug fixed)](https://github.com/PyAutoLabs/autofit_workspace/pull/103) (PyAutoLabs/autofit_workspace)
**Scripts Changed:** None (config-only edit to config/build/no_run.yaml). The following previously-skipped script returns to validation:
- `scripts/features/interpolate.py`

### [config: adopt version.minimum_library_version floor (2026.7.9.1)](https://github.com/PyAutoLabs/autofit_workspace/pull/97) (PyAutoLabs/autofit_workspace)
**API Changes:** None — workspace config only.

### [docs: note PYAUTO_TEST_MODE_SAMPLES in AGENTS.md](https://github.com/PyAutoLabs/autofit_workspace/pull/96) (PyAutoLabs/autofit_workspace)
**Scripts Changed:** None — AGENTS.md only.

Generated by the PyAutoLabs agent workflow.

### [chore: un-park imaging/modeling (stale NEEDS_FIX, bug fixed)](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/142) (PyAutoLabs/autogalaxy_workspace)
**Scripts Changed:** None (config-only edit to config/build/no_run.yaml). The following previously-skipped script returns to validation:
- `scripts/imaging/modeling.py`

### [fix: un-park pixelization/MGE scripts (stale NEEDS_FIX, now green)](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/141) (PyAutoLabs/autogalaxy_workspace)
**Scripts Changed:** No script edits -- `config/build/no_run.yaml` only. Markers removed (scripts now un-parked and verified green):
- `imaging/features/pixelization/modeling` -- was `LinAlgError: matrix not positive definite`
- `interferometer/features/pixelization/modeling` -- was `LinAlgError: matrix not positive def

### [config: adopt version.minimum_library_version floor (2026.7.9.1)](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/134) (PyAutoLabs/autogalaxy_workspace)
**API Changes:** None — workspace config only.

### [chore: un-park group/slam (stale NEEDS_FIX, bug fixed)](https://github.com/PyAutoLabs/autolens_workspace/pull/312) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** None (config-only edit to config/build/no_run.yaml). The following previously-skipped script returns to validation:
- `scripts/group/slam.py`

### [fix: multi-wavelength modeling green (auto-simulate + SersicCore effective_radius=0)](https://github.com/PyAutoLabs/autolens_workspace/pull/306) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/multi/features/wavelength_dependence/modeling.py` — add dataset auto-simulate block (mirrors `multi/modeling.py`)
- `config/build/no_run.yaml` — drop the `multi/features/wavelength_dependence/modeling` NEEDS_FIX marker
- `notebooks/multi/features/wavelength_dependence/modeling.ipynb` — re

### [chore: un-park mask_irregular no_run marker (bug already fixed)](https://github.com/PyAutoLabs/autolens_workspace/pull/304) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** No script edits -- `config/build/no_run.yaml` only. Marker removed:
- `imaging/data_preparation/manual/mask_irregular` -- was `NEEDS_FIX 2026-04-10 silent failure` (verified green)

### [fix: SLaM advanced-pipeline inversion + adapt-image cascade (#300)](https://github.com/PyAutoLabs/autolens_workspace/pull/302) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/imaging/features/advanced/double_einstein_ring/slam.py` — seed `source_1` adapt image in `source_pix_1_source_1` (+ docstring)
- `scripts/group/features/advanced/double_einstein_ring/slam.py` — same seed (+ docstring)
- `scripts/imaging/features/pixelization/slam.py` — `AdaptSplit` -> `Ad

### [fix(smoke): cap RXJ1131 data to 16x16 so modeling runs under SMALL_DATASETS](https://github.com/PyAutoLabs/autolens_workspace/pull/297) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/multi/features/imaging_and_point_source/modeling.py` — cap the downloaded data under `SMALL_DATASETS`.

_(Notebook regeneration will run in ship; config unchanged.)_
