# Release Readiness Report

**Status: NOT READY**

**Run:** `2026-04-29T14-48-47Z`  •  **Path:** `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoBuild/test_results/runs/2026-04-29T14-48-47Z`  •  **Total duration:** 5725.3s

## Slow-Skipped Scripts (needs performance fix)

**14 script(s)** are being skipped because they exceed the 60s per-script timeout cap. These are NOT permanent skips — they need the underlying performance issue fixed and the `SLOW` marker removed from the workspace's `config/build/no_run.yaml`.

| Workspace | Script | Marked | Age | Reason |
|-----------|--------|--------|-----|--------|
| autogalaxy_workspace | `guides/results/database/start_here` | 2026-04-10 | 19d | previously failed fast on a broken aggregator query; now runs the real aggregator and exceeds 60s |
| autogalaxy_workspace | `guides/results/examples/galaxies_fit` | 2026-04-10 | 19d | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| autogalaxy_workspace | `guides/results/examples/models` | 2026-04-10 | 19d | cascade from SLOW-skipped results/start_here.py; aggregator returns NoneType so instance.galaxies is None |
| autogalaxy_workspace | `guides/results/examples/samples` | 2026-04-10 | 19d | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| autogalaxy_workspace | `guides/results/start_here` | 2026-04-10 | 19d | exceeds 60s test timeout; unsets TEST_MODE to produce real samples for downstream examples |
| autogalaxy_workspace | `guides/results/workflow/csv_make` | 2026-04-10 | 19d | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| autolens_workspace | `guides/results/database/start_here` | 2026-04-10 | 19d | previously failed fast on a broken aggregator query; now runs the real aggregator and exceeds 60s |
| autolens_workspace | `guides/results/examples/queries` | 2026-04-10 | 19d | cascade from SLOW-skipped results/start_here.py; stub Model lacks sersic_index attribute |
| autolens_workspace | `guides/results/examples/samples` | 2026-04-10 | 19d | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| autolens_workspace | `guides/results/examples/samples_via_aggregator` | 2026-04-10 | 19d | exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| autolens_workspace_test | `database/scrape/multi_analysis` | 2026-04-10 | 19d | exceeds 60s timeout; _test workspaces run full searches without test mode |
| autolens_workspace_test | `database/scrape/slam_general` | 2026-04-10 | 19d | exceeds 60s timeout; _test workspaces run full searches without test mode |
| autolens_workspace_test | `database/scrape/slam_multi_one_by_one` | 2026-04-10 | 19d | exceeds 60s timeout; _test workspaces run full searches without test mode |
| autolens_workspace_test | `database/scrape/slam_pix` | 2026-04-10 | 19d | exceeds 60s timeout; _test workspaces run full searches without test mode |

## Needs-Fix Scripts (parked for investigation)

**22 script(s)** are being skipped because they are broken and parked as a to-do list. These are NOT permanent skips — investigate the failure, fix the underlying bug, and remove the `NEEDS_FIX` marker from the workspace's `config/build/no_run.yaml`.

| Workspace | Script | Marked | Age | Reason |
|-----------|--------|--------|-----|--------|
| autofit_workspace | `features/interpolate` | 2026-04-10 | 19d | IndexError in InstanceInterpolator.__getitem__ when querying time == 1.5; value_map lookup falls through to empty instances list |
| autogalaxy_workspace | `autogalaxy_workspace/scripts/imaging/modeling` | 2026-04-10 | 19d | KeyError on ('galaxies','galaxy','bulge','ell_comps'...) kwargs after API drift in top-level imaging/modeling.py |
| autogalaxy_workspace | `ellipse/database` | 2026-04-24 | 5d | all ellipse examples parked pending JAX refactor; see PyAutoPrompt/autogalaxy/ellipse_no_run.md |
| autogalaxy_workspace | `ellipse/fit` | 2026-04-24 | 5d | all ellipse examples parked pending JAX refactor; see PyAutoPrompt/autogalaxy/ellipse_no_run.md |
| autogalaxy_workspace | `ellipse/modeling` | 2026-04-24 | 5d | all ellipse examples parked pending JAX refactor; see PyAutoPrompt/autogalaxy/ellipse_no_run.md |
| autogalaxy_workspace | `ellipse/multipoles` | 2026-04-24 | 5d | all ellipse examples parked pending JAX refactor; see PyAutoPrompt/autogalaxy/ellipse_no_run.md |
| autogalaxy_workspace | `ellipse/simulator` | 2026-04-24 | 5d | all ellipse examples parked pending JAX refactor; see PyAutoPrompt/autogalaxy/ellipse_no_run.md |
| autogalaxy_workspace | `imaging/data_preparation/manual/mask_irregular` | 2026-04-10 | 19d | silent failure, needs investigation |
| autogalaxy_workspace | `imaging/features/pixelization/modeling` | 2026-04-10 | 19d | LinAlgError: matrix not positive definite in pixelization modeling |
| autogalaxy_workspace | `interferometer/features/pixelization/modeling` | 2026-04-10 | 19d | LinAlgError: matrix not positive definite in interferometer pixelization modeling |
| autolens_workspace | `group/slam` | 2026-04-10 | 19d | PriorException: upper limit must be greater than lower limit in group SLaM pipeline |
| autolens_workspace | `imaging/data_preparation/manual/mask_irregular` | 2026-04-10 | 19d | silent failure, needs investigation |
| autolens_workspace | `imaging/features/pixelization/delaunay` | 2026-04-10 | 19d | autofit.exc.FitException in Delaunay pixelization fit |
| autolens_workspace | `imaging/features/pixelization/slam` | 2026-04-10 | 19d | autofit.exc.FitException in SLaM pixelization pipeline |
| autolens_workspace | `interferometer/features/pixelization/delaunay` | 2026-04-10 | 19d | broadcast shape mismatch (2,2) vs (1032,1032) in Delaunay interferometer |
| autolens_workspace | `multi/features/wavelength_dependence/modeling` | 2026-04-10 | 19d | autofit.exc.FitException in multi-wavelength modeling |
| autolens_workspace_test | `database/scrape/general` | 2026-04-27 | 2d | PyAutoGalaxy abstract_fit.linear_light_profile_intensity_dict raises "TypeError: __hash__ method should return an integer" during subplot_fit_imaging after the search completes (a light-profile object's __hash__ returns a non-int). Surfaced once the dataset_label="build" path fix let the script progress past Imaging.from_fits. |
| autolens_workspace_test | `imaging/visualization` | 2026-04-10 | 19d | AssertionError: dataset.png missing after visualization refactor |
| autolens_workspace_test | `jax_grad/imaging_lp` | 2026-04-10 | 19d | JAX traceback in gradient computation for light profile |
| autolens_workspace_test | `jax_grad/imaging_mge` | 2026-04-10 | 19d | AssertionError: Gradient is all zeros in MGE gradient computation |
| autolens_workspace_test | `jax_likelihood_functions/imaging/delaunay_mge` | 2026-04-10 | 19d | timeout in JAX likelihood function benchmark |
| autolens_workspace_test | `jax_likelihood_functions/imaging/mge_group` | 2026-04-10 | 19d | timeout in JAX likelihood function benchmark |

## Summary

| Passed | Failed | Skipped | Timeout |
|--------|--------|---------|---------|
| 344 | 43 | 68 | 5 |

## Per-Project Breakdown

| Project | Passed | Failed | Skipped | Timeout | Duration |
|---------|--------|--------|---------|---------|----------|
| autofit | 23 | 1 | 6 | 0 | 99.2s |
| autofit_test | 22 | 0 | 2 | 0 | 105.6s |
| autogalaxy | 79 | 6 | 20 | 2 | 1044.3s |
| autogalaxy_test | 31 | 1 | 0 | 0 | 742.2s |
| autolens | 150 | 20 | 29 | 3 | 2566.6s |
| autolens_test | 39 | 15 | 11 | 0 | 1167.5s |

## Slowest scripts (top 25)

| Script | Project | Status | Duration | Share |
|--------|---------|--------|----------|-------|
| `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/results/aggregator/samples.py` | autogalaxy | timeout | 300.0s | 5.2% |
| `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/results/aggregator/galaxies_fit.py` | autogalaxy | timeout | 300.0s | 5.2% |
| `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/results/start_here.py` | autolens | timeout | 300.0s | 5.2% |
| `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/results/aggregator/galaxies_fits.py` | autolens | timeout | 300.0s | 5.2% |
| `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/results/aggregator/samples.py` | autolens | timeout | 300.0s | 5.2% |
| `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/results/workflow/csv_make.py` | autolens | passed | 144.8s | 2.5% |
| `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/plot/advanced/plotters_pixelization.py` | autolens | passed | 135.9s | 2.4% |
| `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/imaging/model_fit.py` | autolens_test | passed | 130.1s | 2.3% |
| `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/multi/start_here.py` | autolens | passed | 74.4s | 1.3% |
| `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/multi/mge_group.py` | autolens_test | passed | 73.5s | 1.3% |
| `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/delaunay_mge.py` | autogalaxy_test | passed | 59.8s | 1.0% |
| `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_mge.py` | autolens_test | failed | 56.1s | 1.0% |
| `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/database/scrape/scaling_relation.py` | autolens_test | passed | 55.4s | 1.0% |
| `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace_test/scripts/jax_likelihood_functions/multi/mge_group.py` | autogalaxy_test | passed | 55.2s | 1.0% |
| `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/delaunay_mge.py` | autolens_test | passed | 48.8s | 0.9% |
| `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/interferometer/visualization.py` | autolens_test | failed | 48.4s | 0.8% |
| `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/delaunay.py` | autolens_test | passed | 46.8s | 0.8% |
| `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/modeling/advanced/graphical.py` | autolens | passed | 45.7s | 0.8% |
| `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/delaunay_mge.py` | autogalaxy_test | passed | 45.1s | 0.8% |
| `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace_test/scripts/imaging/visualization.py` | autogalaxy_test | passed | 44.4s | 0.8% |
| `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/units/flux.py` | autolens | passed | 43.9s | 0.8% |
| `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_mge.py` | autogalaxy_test | passed | 42.8s | 0.7% |
| `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/multi_gaussian_expansion/modeling.py` | autolens | passed | 42.5s | 0.7% |
| `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace_test/scripts/jax_likelihood_functions/multi/delaunay_mge.py` | autogalaxy_test | passed | 42.1s | 0.7% |
| `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/mge_group.py` | autogalaxy_test | passed | 42.0s | 0.7% |

## Failures by Classification

### Source Code Bugs (21)

- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autofit_workspace/scripts/features/graphical_models.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autofit_workspace/scripts/features/graphical_models.py']' returned non-zero exit status 1.
  - **Recently modified** in [refactor: remove howtofit/ from autofit_workspace (sub-2 of howtofit extraction)](https://github.com/PyAutoLabs/autofit_workspace/pull/39)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autofit_workspace/scripts/features/graphical_models.py", line 95, in <module>
    data = af.util.numpy_array_from_json(file_path=path.join(dataset_path, "data.json"))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoFit/autofit/tools/util.py", line 130, in numpy_array_from_json
    with open(file_path, "r") as f:
         ^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'dataset/example_1d/gaussian_x1__low_snr/dataset_0/data.json'
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/results/aggregator/models.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/results/aggregator/models.py']' returned non-zero exit statu
  - **Recently modified** in [refactor: remove howtofit/ from autofit_workspace (sub-2 of howtofit extraction)](https://github.com/PyAutoLabs/autofit_workspace/pull/39)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
    File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/results/aggregator/models.py", line 102, in <module>
    for dataset_list, galaxies_list in zip(dataset_gen, galaxies_gen):
                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoGalaxy/autogalaxy/aggregator/imaging/imaging.py", line 63, in _imaging_from
    mask, header = agg_util.mask_header_from(fit=fit)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoGalaxy/autogalaxy/aggregator/agg_util.py", line 101, in mask_header_from
    header = aa.Header(header_sci_obj=fit.value(name=name)[0].header)
                                      ~~~~~~~~~~~~~~~~~~~~^^^
TypeError: 'NoneType' object is not subscriptable
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/imaging/features/extra_galaxies/modeling.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/imaging/features/extra_galaxies/modeling.py']' returned non-zero ex
  - **Recently modified** in [Add version.txt and check_version() in welcome.py](https://github.com/PyAutoLabs/autofit_workspace/pull/33)
  - **Recently modified** in [docs: merge guides/results start_here.py files (simple + aggregator)](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/46)
  - **Recently modified** in [Auto-generate mask_extra_galaxies.fits in simulators](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/41)
  - **Recently modified** in [feat(point_source): rename to multiple_sources and add multi-source modeling](https://github.com/PyAutoLabs/autolens_workspace/pull/100)
  - **Recently modified** in [docs: merge guides/results start_here.py files (simple + aggregator)](https://github.com/PyAutoLabs/autolens_workspace/pull/98)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/imaging/features/extra_galaxies/modeling.py", line 272, in <module>
    ag.from_json(file_path=Path(dataset_path, "extra_galaxies_centres.json"))
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoConf/autoconf/dictable.py", line 364, in from_json
    with open(file_path, "r+") as f:
         ^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'dataset/imaging/extra_galaxies/extra_galaxies_centres.json'
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/interferometer/features/pixelization/fit.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/interferometer/features/pixelization/fit.py']' returned non-zero ex
  - **Recently modified** in [refactor: remove howtofit/ from autofit_workspace (sub-2 of howtofit extraction)](https://github.com/PyAutoLabs/autofit_workspace/pull/39)
  - **Recently modified** in [Auto-generate mask_extra_galaxies.fits in simulators](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/41)
  - **Recently modified** in [fix: enable fits_make / png_make smoke tests](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/39)
  - **Recently modified** in [feat(point_source): rename to multiple_sources and add multi-source modeling](https://github.com/PyAutoLabs/autolens_workspace/pull/100)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/interferometer/features/pixelization/fit.py", line 282, in <module>
    subplot_of_mapper(inversion=inversion, mapper_index=0)
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/inversion/plot/inversion_plots.py", line 63, in subplot_of_mapper
    plot_array(
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/plot/array.py", line 199, in plot_array
    h, w = array.shape[:2]
    ^^^^
ValueError: not enough values to unpack (expected 2, got 1)
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/linear_light_profiles/slam.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/linear_light_profiles/slam.py']' returned non-zero exi
  - **Recently modified** in [fix(interferometer): strip lens light from pixelization SLaM scripts](https://github.com/PyAutoLabs/autolens_workspace/pull/106)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/linear_light_profiles/slam.py", line 891, in <module>
    source_lp_result_1 = source_lp_1(
                         ^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/linear_light_profiles/slam.py", line 235, in source_lp_1
    mass.einstein_radius = af.UniformPrior(
                           ^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoFit/autofit/mapper/prior/uniform.py", line 53, in __init__
    raise exc.PriorException(
autoconf.exc.PriorException: The upper limit of a prior must be greater than its lower limit
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/pixelization/delaunay.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/pixelization/delaunay.py']' returned non-zero exit sta
  - **Recently modified** in [fix(interferometer): strip lens light from pixelization SLaM scripts](https://github.com/PyAutoLabs/autolens_workspace/pull/106)
  - **Recently modified** in [fix: chain image_plane_mesh_grid through light_lp / mass_total in delaunay SLaM](https://github.com/PyAutoLabs/autolens_workspace/pull/104)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
    File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/inversion/mesh/mesh/delaunay.py", line 158, in interpolator_from
    relocated_mesh_grid = self.relocated_mesh_grid_from(
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/inversion/mesh/mesh/abstract.py", line 91, in relocated_mesh_grid_from
    return border_relocator.relocated_mesh_grid_from(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/inversion/mesh/border_relocator.py", line 450, in relocated_mesh_grid_from
    grid=mesh_grid.array, origin=origin, a=a, b=b, phi=phi, xp=xp
         ^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'array'
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/pixelization/fit.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/pixelization/fit.py']' returned non-zero exit status 1
  - **Recently modified** in [refactor: remove howtofit/ from autofit_workspace (sub-2 of howtofit extraction)](https://github.com/PyAutoLabs/autofit_workspace/pull/39)
  - **Recently modified** in [Auto-generate mask_extra_galaxies.fits in simulators](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/41)
  - **Recently modified** in [fix: enable fits_make / png_make smoke tests](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/39)
  - **Recently modified** in [feat(point_source): rename to multiple_sources and add multi-source modeling](https://github.com/PyAutoLabs/autolens_workspace/pull/100)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
    File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/inversion/mesh/mesh/delaunay.py", line 158, in interpolator_from
    relocated_mesh_grid = self.relocated_mesh_grid_from(
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/inversion/mesh/mesh/abstract.py", line 91, in relocated_mesh_grid_from
    return border_relocator.relocated_mesh_grid_from(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/inversion/mesh/border_relocator.py", line 450, in relocated_mesh_grid_from
    grid=mesh_grid.array, origin=origin, a=a, b=b, phi=phi, xp=xp
         ^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'array'
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/pixelization/likelihood_function.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/pixelization/likelihood_function.py']' returned non-ze
  <details><summary>Traceback (last 10 lines)</summary>

  ```
    File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/inversion/mesh/mesh/delaunay.py", line 158, in interpolator_from
    relocated_mesh_grid = self.relocated_mesh_grid_from(
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/inversion/mesh/mesh/abstract.py", line 91, in relocated_mesh_grid_from
    return border_relocator.relocated_mesh_grid_from(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/inversion/mesh/border_relocator.py", line 450, in relocated_mesh_grid_from
    grid=mesh_grid.array, origin=origin, a=a, b=b, phi=phi, xp=xp
         ^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'array'
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/pixelization/modeling.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/pixelization/modeling.py']' returned non-zero exit sta
  - **Recently modified** in [Add version.txt and check_version() in welcome.py](https://github.com/PyAutoLabs/autofit_workspace/pull/33)
  - **Recently modified** in [docs: merge guides/results start_here.py files (simple + aggregator)](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/46)
  - **Recently modified** in [Auto-generate mask_extra_galaxies.fits in simulators](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/41)
  - **Recently modified** in [feat(point_source): rename to multiple_sources and add multi-source modeling](https://github.com/PyAutoLabs/autolens_workspace/pull/100)
  - **Recently modified** in [docs: merge guides/results start_here.py files (simple + aggregator)](https://github.com/PyAutoLabs/autolens_workspace/pull/98)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
    File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoFit/autofit/mapper/prior_model/abstract.py", line 1403, in instance_for_arguments
    return self._instance_for_arguments(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoFit/autofit/mapper/prior_model/prior_model.py", line 495, in _instance_for_arguments
    result = self.cls(**constructor_arguments)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/inversion/mesh/mesh/delaunay.py", line 58, in __init__
    pixels = int(pixels) + zeroed_pixels
             ~~~~~~~~~~~~^~~~~~~~~~~~~~~
TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/pixelization/slam.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/pixelization/slam.py']' returned non-zero exit status 
  - **Recently modified** in [fix(interferometer): strip lens light from pixelization SLaM scripts](https://github.com/PyAutoLabs/autolens_workspace/pull/106)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  /home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/operators/convolver.py:925: UserWarning: No blurring_image provided. Only the direct image will be convolved. This may change the correctness of the PSF convolution.
  warnings.warn(
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/pixelization/slam.py", line 751, in <module>
    ).positions
      ^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'positions'
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/plot/examples/plotters.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/plot/examples/plotters.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/plot/examples/plotters.py", line 351, in <module>
    dataset = al.from_json(
              ^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoConf/autoconf/dictable.py", line 364, in from_json
    with open(file_path, "r+") as f:
         ^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'dataset/point_source/simple/point_dataset_positions_only.json'
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/results/aggregator/models.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/results/aggregator/models.py']' returned non-zero exit status 
  - **Recently modified** in [refactor: remove howtofit/ from autofit_workspace (sub-2 of howtofit extraction)](https://github.com/PyAutoLabs/autofit_workspace/pull/39)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
    File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/results/aggregator/models.py", line 91, in <module>
    for dataset_list, tracer_list in zip(dataset_gen, tracer_gen):
                                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoGalaxy/autogalaxy/aggregator/imaging/imaging.py", line 63, in _imaging_from
    mask, header = agg_util.mask_header_from(fit=fit)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoGalaxy/autogalaxy/aggregator/agg_util.py", line 101, in mask_header_from
    header = aa.Header(header_sci_obj=fit.value(name=name)[0].header)
                                      ~~~~~~~~~~~~~~~~~~~~^^^
TypeError: 'NoneType' object is not subscriptable
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/results/aggregator/queries.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/results/aggregator/queries.py']' returned non-zero exit status
  <details><summary>Traceback (last 10 lines)</summary>

  ```
                            ^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoFit/autofit/aggregator/predicate.py", line 285, in __call__
    return self.attribute_predicate.value_for_search_output(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoFit/autofit/aggregator/predicate.py", line 35, in value_for_search_output
    value = getattr(
            ^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoFit/autofit/mapper/prior_model/prior_model.py", line 422, in __getattr__
    self.__getattribute__(item)
AttributeError: 'Model' object has no attribute 'sersic_index'
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/advanced/double_einstein_ring/slam.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/advanced/double_einstein_ring/slam.py']' returned no
  - **Recently modified** in [fix(interferometer): strip lens light from pixelization SLaM scripts](https://github.com/PyAutoLabs/autolens_workspace/pull/106)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
      return func(self, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoFit/autofit/non_linear/search/abstract_search.py", line 661, in start_resume_fit
    return self._fit_bypass_test_mode(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoFit/autofit/non_linear/search/abstract_search.py", line 848, in _fit_bypass_test_mode
    analysis.log_likelihood_function(instance)
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoLens/autolens/imaging/model/analysis.py", line 84, in log_likelihood_function
    raise af.exc.FitException
autofit.exc.FitException
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/interferometer/features/pixelization/fit.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/interferometer/features/pixelization/fit.py']' returned non-zero exit
  - **Recently modified** in [refactor: remove howtofit/ from autofit_workspace (sub-2 of howtofit extraction)](https://github.com/PyAutoLabs/autofit_workspace/pull/39)
  - **Recently modified** in [Auto-generate mask_extra_galaxies.fits in simulators](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/41)
  - **Recently modified** in [fix: enable fits_make / png_make smoke tests](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/39)
  - **Recently modified** in [feat(point_source): rename to multiple_sources and add multi-source modeling](https://github.com/PyAutoLabs/autolens_workspace/pull/100)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/interferometer/features/pixelization/fit.py", line 288, in <module>
    subplot_of_mapper(inversion=inversion, mapper_index=0)
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/inversion/plot/inversion_plots.py", line 63, in subplot_of_mapper
    plot_array(
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/plot/array.py", line 199, in plot_array
    h, w = array.shape[:2]
    ^^^^
ValueError: not enough values to unpack (expected 2, got 1)
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/point_source/features/deblending/simulator.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/point_source/features/deblending/simulator.py']' returned non-zero ex
  - **Recently modified** in [Auto-generate mask_extra_galaxies.fits in simulators](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/41)
  - **Recently modified** in [fix: restore truncated data_preparation scripts (#85)](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/40)
  - **Recently modified** in [fix: drop PYAUTO_SMALL_DATASETS workaround in group simulators](https://github.com/PyAutoLabs/autolens_workspace/pull/102)
  - **Recently modified** in [feat(point_source): rename to multiple_sources and add multi-source modeling](https://github.com/PyAutoLabs/autolens_workspace/pull/100)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/point_source/features/deblending/simulator.py", line 265, in <module>
    centre=positions[2], intensity=fluxes[2], sigma=psf_sigma
           ~~~~~~~~~^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/abstract_ndarray.py", line 391, in __getitem__
    result = self._array[item]
             ~~~~~~~~~~~^^^^^^
IndexError: index 2 is out of bounds for axis 0 with size 2
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/point_source/fit.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/point_source/fit.py']' returned non-zero exit status 1.
  - **Recently modified** in [refactor: remove howtofit/ from autofit_workspace (sub-2 of howtofit extraction)](https://github.com/PyAutoLabs/autofit_workspace/pull/39)
  - **Recently modified** in [Auto-generate mask_extra_galaxies.fits in simulators](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/41)
  - **Recently modified** in [fix: enable fits_make / png_make smoke tests](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/39)
  - **Recently modified** in [feat(point_source): rename to multiple_sources and add multi-source modeling](https://github.com/PyAutoLabs/autolens_workspace/pull/100)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
    File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/abstract_ndarray.py", line 35, in wrapper
    return self.with_new_array(func(self, *args, **kwargs))
                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/abstract_ndarray.py", line 57, in wrapper
    return func(self, other.array)
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/abstract_ndarray.py", line 326, in __truediv__
    return self._array / other
           ~~~~~~~~~~~~^~~~~~~
ValueError: operands could not be broadcast together with shapes (2,) (4,)
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/imaging/convolution.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/imaging/convolution.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
    File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/matplotlib/backends/backend_agg.py", line 496, in print_png
    self._print_pil(filename_or_obj, "png", pil_kwargs, metadata)
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/matplotlib/backends/backend_agg.py", line 445, in _print_pil
    mpl.image.imsave(
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/matplotlib/image.py", line 1676, in imsave
    image.save(fname, **pil_kwargs)
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/PIL/Image.py", line 2576, in save
    fp = builtins.open(filename, "w+b")
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'scripts/imaging/images/residuals.png'
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/imaging/modeling_visualization_jit.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/imaging/modeling_visualization_jit.py']' returned non-zero exit 
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  /home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/operators/convolver.py:925: UserWarning: No blurring_image provided. Only the direct image will be convolved. This may change the correctness of the PSF convolution.
  warnings.warn(
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/imaging/modeling_visualization_jit.py", line 149, in <module>
    assert isinstance(fit_1.log_likelihood, jnp.ndarray), (
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: expected jax.Array, got <class 'numpy.float64'>
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/interferometer/model_fit.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/interferometer/model_fit.py']' returned non-zero exit status 1.
  <details><summary>Traceback (last 10 lines)</summary>

  ```
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/nautilus/pool.py", line 85, in map
    return list(self.pool.map(func, iterable))
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/multiprocessing/pool.py", line 367, in map
    return self._map_async(func, iterable, mapstar, chunksize).get()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/multiprocessing/pool.py", line 774, in get
    raise self._value
numpy.linalg.LinAlgError: Matrix is not positive definite
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/interferometer/visualization.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/interferometer/visualization.py']' returned non-zero exit status
  <details><summary>Traceback (last 10 lines)</summary>

  ```
    File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoLens/autolens/interferometer/model/visualizer.py", line 159, in visualize
    plotter.inversion(
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoGalaxy/autogalaxy/analysis/plotter.py", line 150, in inversion
    subplot_of_mapper(
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/inversion/plot/inversion_plots.py", line 63, in subplot_of_mapper
    plot_array(
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/plot/array.py", line 199, in plot_array
    h, w = array.shape[:2]
    ^^^^
ValueError: not enough values to unpack (expected 2, got 1)
  ```
  </details>

### Workspace Issues (17)

- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/advanced/over_sampling.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/advanced/over_sampling.py']' returned non-zero exit status 1
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/advanced/over_sampling.py", line 111, in <module>
    aplt.plot_grid(
TypeError: plot_grid() got an unexpected keyword argument 'plot_over_sampled_grid'
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/results/aggregator/samples_via_aggregator.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/results/aggregator/samples_via_aggregator.py']' returned non
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/results/aggregator/samples_via_aggregator.py", line 146, in <module>
    print(samples.parameter_lists[0])
          ^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'parameter_lists'
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace_test/scripts/imaging/modeling_visualization_jit.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace_test/scripts/imaging/modeling_visualization_jit.py']' returned non-zero exi
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace_test/scripts/imaging/modeling_visualization_jit.py", line 128, in <module>
    assert isinstance(fit_1.log_likelihood, jnp.ndarray), (
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: expected jax.Array, got <class 'numpy.float64'>
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/cluster/simulator.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/cluster/simulator.py']' returned non-zero exit status 1.
  - **Recently modified** in [Auto-generate mask_extra_galaxies.fits in simulators](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/41)
  - **Recently modified** in [fix: restore truncated data_preparation scripts (#85)](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/40)
  - **Recently modified** in [fix: drop PYAUTO_SMALL_DATASETS workaround in group simulators](https://github.com/PyAutoLabs/autolens_workspace/pull/102)
  - **Recently modified** in [feat(point_source): rename to multiple_sources and add multi-source modeling](https://github.com/PyAutoLabs/autolens_workspace/pull/100)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/cluster/simulator.py", line 418, in <module>
    raw = np.asarray(jitted_solve(tracer, coord).array)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: function jitted_solve at /home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/cluster/simulator.py:405 traced for jit returned a value of type <class 'autoarray.structures.grids.irregular_2d.Grid2DIrregular'> at output component jit, which is not a valid JAX type
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/advanced/subhalo/detect/start_here.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/advanced/subhalo/detect/start_here.py']' returned non-
  - **Recently modified** in [docs: merge guides/results start_here.py files (simple + aggregator)](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/46)
  - **Recently modified** in [Auto-generate mask_extra_galaxies.fits in simulators](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/41)
  - **Recently modified** in [fix(interferometer): strip lens light from pixelization SLaM scripts](https://github.com/PyAutoLabs/autolens_workspace/pull/106)
  - **Recently modified** in [docs: merge guides/results start_here.py files (simple + aggregator)](https://github.com/PyAutoLabs/autolens_workspace/pull/98)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/advanced/subhalo/detect/start_here.py", line 803, in <module>
    light_result = light_lp(
                   ^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/advanced/subhalo/detect/start_here.py", line 354, in light_lp
    galaxies=af.Collection(**lens_dict, source=source),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: autofit.mapper.prior_model.collection.Collection() got multiple values for keyword argument 'source'
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/results/aggregator/samples_via_aggregator.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/results/aggregator/samples_via_aggregator.py']' returned non-z
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/results/aggregator/samples_via_aggregator.py", line 143, in <module>
    print(samples.parameter_lists[0])
          ^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'parameter_lists'
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/imaging/modeling_visualization_jit_delaunay.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/imaging/modeling_visualization_jit_delaunay.py']' returned non-z
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/imaging/modeling_visualization_jit_delaunay.py", line 191, in <module>
    assert isinstance(fit_1.log_likelihood, jnp.ndarray), (
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: expected jax.Array, got <class 'numpy.float64'>
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/imaging/modeling_visualization_jit_rectangular.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/imaging/modeling_visualization_jit_rectangular.py']' returned no
  <details><summary>Traceback (last 10 lines)</summary>

  ```
  Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/imaging/modeling_visualization_jit_rectangular.py", line 175, in <module>
    assert isinstance(fit_1.log_likelihood, jnp.ndarray), (
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: expected jax.Array, got <class 'numpy.float64'>
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/delaunay.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/delaunay.py']' returned non-zer
  - **Recently modified** in [fix(interferometer): strip lens light from pixelization SLaM scripts](https://github.com/PyAutoLabs/autolens_workspace/pull/106)
  - **Recently modified** in [fix: chain image_plane_mesh_grid through light_lp / mass_total in delaunay SLaM](https://github.com/PyAutoLabs/autolens_workspace/pull/104)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
    File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 921, in assert_array_compare
    raise AssertionError(msg)
AssertionError: 
Not equal to tolerance rtol=0.0001, atol=0
delaunay: JAX vmap likelihood mismatch
Mismatched elements: 3 / 3 (100%)
Max absolute difference among violations: 1456.97072316
Max relative difference among violations: 0.06157208
 ACTUAL: array([-22205.878181, -22205.878181, -22205.878181])
 DESIRED: array(-23662.848904)
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular.py']' returned non-
  <details><summary>Traceback (last 10 lines)</summary>

  ```
    File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 921, in assert_array_compare
    raise AssertionError(msg)
AssertionError: 
Not equal to tolerance rtol=0.0001, atol=0
rectangular: JAX vmap likelihood mismatch
Mismatched elements: 3 / 3 (100%)
Max absolute difference among violations: 1059.94076761
Max relative difference among violations: 0.00162909
 ACTUAL: array([-651692.997799, -651692.997799, -651692.997799])
 DESIRED: array(-650633.057031)
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_dspl.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_dspl.py']' returned
  <details><summary>Traceback (last 10 lines)</summary>

  ```
    File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 921, in assert_array_compare
    raise AssertionError(msg)
AssertionError: 
Not equal to tolerance rtol=0.0001, atol=0
rectangular_dspl: JAX vmap likelihood mismatch
Mismatched elements: 1 / 1 (100%)
Max absolute difference among violations: 35.12946094
Max relative difference among violations: 0.03095257
 ACTUAL: array([1170.074391])
 DESIRED: array(1134.94493)
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_mge.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_mge.py']' returned 
  <details><summary>Traceback (last 10 lines)</summary>

  ```
      raise AssertionError(msg)
AssertionError: 
Not equal to tolerance rtol=0.0001, atol=0
rectangular_mge: JAX vmap likelihood mismatch
Mismatched elements: 6 / 6 (100%)
Max absolute difference among violations: 28.41880723
Max relative difference among violations: 0.25517883
 ACTUAL: array([-82.949395, -82.949395, -82.949395, -82.949395, -82.949395,
       -82.949395])
 DESIRED: array(-111.368202)
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/multi/delaunay.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/multi/delaunay.py']' returned non-zero 
  - **Recently modified** in [fix(interferometer): strip lens light from pixelization SLaM scripts](https://github.com/PyAutoLabs/autolens_workspace/pull/106)
  - **Recently modified** in [fix: chain image_plane_mesh_grid through light_lp / mass_total in delaunay SLaM](https://github.com/PyAutoLabs/autolens_workspace/pull/104)
  <details><summary>Traceback (last 10 lines)</summary>

  ```
    File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 921, in assert_array_compare
    raise AssertionError(msg)
AssertionError: 
Not equal to tolerance rtol=0.0001, atol=0
multi/delaunay: JAX vmap likelihood mismatch
Mismatched elements: 3 / 3 (100%)
Max absolute difference among violations: 2500.39460237
Max relative difference among violations: 0.39359731
 ACTUAL: array([-8853.066593, -8853.066593, -8853.066593])
 DESIRED: array(-6352.671991)
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/multi/delaunay_mge.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/multi/delaunay_mge.py']' returned non-z
  <details><summary>Traceback (last 10 lines)</summary>

  ```
    File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 921, in assert_array_compare
    raise AssertionError(msg)
AssertionError: 
Not equal to tolerance rtol=0.0001, atol=0
multi/delaunay_mge: JAX vmap likelihood mismatch
Mismatched elements: 3 / 3 (100%)
Max absolute difference among violations: 420.92603587
Max relative difference among violations: 3.38562991
 ACTUAL: array([-545.25328, -545.25328, -545.25328])
 DESIRED: array(-124.327244)
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/multi/mge.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/multi/mge.py']' returned non-zero exit 
  <details><summary>Traceback (last 10 lines)</summary>

  ```
    File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 921, in assert_array_compare
    raise AssertionError(msg)
AssertionError: 
Not equal to tolerance rtol=0.0001, atol=0
multi/mge: JAX vmap likelihood mismatch
Mismatched elements: 3 / 3 (100%)
Max absolute difference among violations: 1114.52822173
Max relative difference among violations: 0.00051258
 ACTUAL: array([-2173221.436859, -2173221.436859, -2173221.436859])
 DESIRED: array(-2174335.96508)
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/multi/rectangular.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/multi/rectangular.py']' returned non-ze
  <details><summary>Traceback (last 10 lines)</summary>

  ```
    File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 921, in assert_array_compare
    raise AssertionError(msg)
AssertionError: 
Not equal to tolerance rtol=0.0001, atol=0
multi/rectangular: JAX vmap likelihood mismatch
Mismatched elements: 3 / 3 (100%)
Max absolute difference among violations: 258.50636197
Max relative difference among violations: 0.02040271
 ACTUAL: array([-12928.700871, -12928.700871, -12928.700871])
 DESIRED: array(-12670.194509)
  ```
  </details>
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/multi/rectangular_mge.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/multi/rectangular_mge.py']' returned no
  <details><summary>Traceback (last 10 lines)</summary>

  ```
    File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 921, in assert_array_compare
    raise AssertionError(msg)
AssertionError: 
Not equal to tolerance rtol=0.0001, atol=0
multi/rectangular_mge: JAX vmap likelihood mismatch
Mismatched elements: 3 / 3 (100%)
Max absolute difference among violations: 52.77866625
Max relative difference among violations: 0.00866102
 ACTUAL: array([-6146.592113, -6146.592113, -6146.592113])
 DESIRED: array(-6093.813447)
  ```
  </details>

### Timeouts (5)

- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/results/aggregator/galaxies_fit.py`
  - Timed out after 300s
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/results/aggregator/samples.py`
  - Timed out after 300s
  - **Recently modified** in [refactor: remove howtofit/ from autofit_workspace (sub-2 of howtofit extraction)](https://github.com/PyAutoLabs/autofit_workspace/pull/39)
  - **Recently modified** in [docs: merge guides/results start_here.py files (simple + aggregator)](https://github.com/PyAutoLabs/autolens_workspace/pull/98)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/results/start_here.py`
  - Timed out after 300s
  - **Recently modified** in [docs: merge guides/results start_here.py files (simple + aggregator)](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/46)
  - **Recently modified** in [Auto-generate mask_extra_galaxies.fits in simulators](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/41)
  - **Recently modified** in [fix(interferometer): strip lens light from pixelization SLaM scripts](https://github.com/PyAutoLabs/autolens_workspace/pull/106)
  - **Recently modified** in [docs: merge guides/results start_here.py files (simple + aggregator)](https://github.com/PyAutoLabs/autolens_workspace/pull/98)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/results/aggregator/galaxies_fits.py`
  - Timed out after 300s
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/results/aggregator/samples.py`
  - Timed out after 300s
  - **Recently modified** in [refactor: remove howtofit/ from autofit_workspace (sub-2 of howtofit extraction)](https://github.com/PyAutoLabs/autofit_workspace/pull/39)
  - **Recently modified** in [docs: merge guides/results start_here.py files (simple + aggregator)](https://github.com/PyAutoLabs/autolens_workspace/pull/98)

### Missing Data Files (5)

- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/plot/start_here.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/plot/start_here.py']' returned non-zero exit status 1.
  - **Recently modified** in [docs: merge guides/results start_here.py files (simple + aggregator)](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/46)
  - **Recently modified** in [Auto-generate mask_extra_galaxies.fits in simulators](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/41)
  - **Recently modified** in [fix(interferometer): strip lens light from pixelization SLaM scripts](https://github.com/PyAutoLabs/autolens_workspace/pull/106)
  - **Recently modified** in [docs: merge guides/results start_here.py files (simple + aggregator)](https://github.com/PyAutoLabs/autolens_workspace/pull/98)
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
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/data_structures.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/data_structures.py']' returned non-zero exit status 1.
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
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/modeling/bug_fix.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/modeling/bug_fix.py']' returned non-zero exit status 1.
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
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/modeling/chaining.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/modeling/chaining.py']' returned non-zero exit status 1.
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
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/point_source/features/deblending/modeling.py`
  - Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/point_source/features/deblending/modeling.py']' returned non-zero exi
  - **Recently modified** in [Add version.txt and check_version() in welcome.py](https://github.com/PyAutoLabs/autofit_workspace/pull/33)
  - **Recently modified** in [docs: merge guides/results start_here.py files (simple + aggregator)](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/46)
  - **Recently modified** in [Auto-generate mask_extra_galaxies.fits in simulators](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/41)
  - **Recently modified** in [feat(point_source): rename to multiple_sources and add multi-source modeling](https://github.com/PyAutoLabs/autolens_workspace/pull/100)
  - **Recently modified** in [docs: merge guides/results start_here.py files (simple + aggregator)](https://github.com/PyAutoLabs/autolens_workspace/pull/98)
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
FileNotFoundError: [Errno 2] No such file or directory: 'dataset/point_source/deblending/data.fits'
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
| `start_here.py` | SLOW 2026-04-10 - exceeds 60s test timeout; unsets TEST_MODE to produce real samples for downstream examples |
| `searches.py` | Test mode breaks search visualization. |
| `data_fitting.py` | Test mode breaks .fits file output |
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
| `data_fitting.py` | Test mode breaks .fits file output |
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

### [docs: remove howtofit/ tree and point tutorials to standalone repo](https://github.com/PyAutoLabs/PyAutoFit/pull/1231) (PyAutoLabs/PyAutoFit)
**API Changes:** None — documentation and prose only. No Python source, tests, or config files touched.
See full details below.

### [feat: lazily JIT-cache fit_for_visualization when flag set](https://github.com/PyAutoLabs/PyAutoFit/pull/1229) (PyAutoLabs/PyAutoFit)
**API Changes:** `Analysis.fit_for_visualization` now lazily constructs and caches `jax.jit(self.fit_from)` on the instance when `use_jax_for_visualization=True`. Flag-off behaviour and all public signatures are unchanged. See full details below.

### [feat: add use_jax_for_visualization flag and fit_for_visualization dispatch](https://github.com/PyAutoLabs/PyAutoFit/pull/1228) (PyAutoLabs/PyAutoFit)
**API Changes:** `Analysis.__init__` gains a `use_jax_for_visualization: bool = False` kwarg. It requires `use_jax=True` (otherwise it's coerced to `False` with a warning), and is cleared by `PYAUTO_DISABLE_JAX=1` alongside `use_jax`. Two new public members: `Analysis.fit_for_visualization(instance)` (dispatch seam)

### [docs(install): clone workspace at tag matching library version](https://github.com/PyAutoLabs/PyAutoFit/pull/1225) (PyAutoLabs/PyAutoFit)
**API Changes:** None — documentation only.

See full details below.

### [Guard corner_cornerpy against samples < dims](https://github.com/PyAutoLabs/PyAutoFit/pull/1224) (PyAutoLabs/PyAutoFit)
**API Changes:** None — internal behaviour of `corner_cornerpy` now gracefully skips when samples are insufficient. Callers see an INFO log line and a `None` return instead of an `AssertionError`.
See full details below.

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

### [Propagate xp through Grid2DIrregular.grid_2d_via_deflection_grid_from](https://github.com/PyAutoLabs/PyAutoArray/pull/287) (PyAutoLabs/PyAutoArray)
**API Changes:** None — internal change only. Public signature unchanged; behaviour is only affected when the receiver's `_xp` is not numpy (in which case previously the result silently downgraded to numpy).
See full details below.

### [fix: stop creating root.log on autoarray import](https://github.com/PyAutoLabs/PyAutoArray/pull/285) (PyAutoLabs/PyAutoArray)
**API Changes:** None — internal configuration change only. No public Python symbols are affected.
See full details below.

### [fix: align hardcoded nnls_target_kappa fallback with yaml default](https://github.com/PyAutoLabs/PyAutoArray/pull/284) (PyAutoLabs/PyAutoArray)
**API Changes:** No public API changes. Config fallback default only.

### [fix: lower nnls_target_kappa default to 1e-11](https://github.com/PyAutoLabs/PyAutoArray/pull/283) (PyAutoLabs/PyAutoArray)
**API Changes:** No API changes. Config default only.

### [fix(jax): bump default NNLS target_kappa to 1e-2 for finite backward gradients](https://github.com/PyAutoLabs/PyAutoArray/pull/282) (PyAutoLabs/PyAutoArray)
**API Changes:** None - internal numerical fix. New `nnls_target_kappa` config entry has a sensible default; no call signatures or public symbols changed.
See full details below.

### [feat: register pytrees for AnalysisInterferometer](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/376) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** - New: `autogalaxy.analysis.jax_pytrees.register_galaxies_pytree()` — shared helper that registers `Galaxies` (a `list` subclass) as a JAX pytree with custom flatten/unflatten. Idempotent.
- New: `AnalysisInterferometer._register_fit_interferometer_pytrees()` — static method registering `FitInterfer

### [fix: AdaptImages galaxy-identity mismatch across jax.jit boundary](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/370) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** `AdaptImages` gained a `galaxy_path_list` attribute and two new lookup helpers (`image_for_galaxy`, `image_plane_mesh_grid_for_galaxy`). `updated_via_instance_from` accepts an optional `galaxies` arg used to align the path list with the analysis-time galaxy ordering. `GalaxiesToInversion` accepts an

### [test: widen no-PSF SNR upper bound from 11.5 to 12.5](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/368) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** None — internal test tolerance only.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

### [fix: forward **kwargs through AnalysisImaging.__init__](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/367) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** `ag.AnalysisImaging.__init__` now accepts arbitrary additional keyword arguments and forwards them through `AnalysisDataset.__init__` → `Analysis.__init__` → `af.Analysis.__init__`. No existing call sites are broken — this is a strict superset of the previous signature.

See full details below.

### [docs(weak-lensing): document shear API across LensCalc, Isothermal, ExternalShear](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/366) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** None — internal documentation changes plus a new unit test. No public symbol added, removed, renamed, or behaviourally changed. The `[gamma_2, gamma_1]` storage convention used by `LensCalc.shear_yx_2d_via_hessian_from`, `Isothermal.shear_yx_2d_from`, `ExternalShear`, and `ShearYX2D` / `ShearYX2DIrr

### [feat: register FitImaging, DatasetModel, Galaxies as pytrees in AnalysisImaging](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/364) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** None — internal changes only. `_register_fit_imaging_pytrees` is a new private staticmethod on `AnalysisImaging`; `fit_from` now calls it when `use_jax=True` (no behaviour change on the NumPy path). See full details below.

### [fix: synthetic positions fallback in test mode and PYAUTO_SMALL_DATASETS](https://github.com/PyAutoLabs/PyAutoLens/pull/479) (PyAutoLabs/PyAutoLens)
**API Changes:** No public API signature changes. Two test-mode-only behavior additions, both gated on env vars and inert in production:

- `Result.positions_likelihood_from` now substitutes `[(1.0, 0.0), (-1.0, 0.0)]` when `PYAUTO_TEST_MODE` is set and the resolved positions are empty / NaN / inf.
- `PointSolver.so

### [fix: drop AdaptImages single-pixelated-galaxy fallback in lens.to_inversion](https://github.com/PyAutoLabs/PyAutoLens/pull/474) (PyAutoLabs/PyAutoLens)
**API Changes:** `Analysis.fit_from` (imaging + interferometer) passes `galaxies=tracer.galaxies` into `adapt_images_via_instance_from`. No public symbols added or removed in autolens. Internal change. See full details below.

### [Short-circuit set_snr_of_snr_light_profiles when no SNR profiles present](https://github.com/PyAutoLabs/PyAutoLens/pull/471) (PyAutoLabs/PyAutoLens)
**API Changes:** None. Public signature unchanged; early-return is a pure optimisation.

### [refactor(point): make PointSolver stateless w.r.t. xp](https://github.com/PyAutoLabs/PyAutoLens/pull/469) (PyAutoLabs/PyAutoLens)
**API Changes:** `PointSolver.for_grid` and `PointSolver.for_limits_and_scale` no longer accept `xp=`. The array module is now passed per-call to `solver.solve(xp=...)` / `solver.solve_triangles(xp=...)`. Most user code never calls `.solve()` directly — `AnalysisPoint` threads `xp` through internally based on `use_j

### [feat: add optional redshift to PointDataset](https://github.com/PyAutoLabs/PyAutoLens/pull/465) (PyAutoLabs/PyAutoLens)
**API Changes:** - `PointDataset.__init__` gains optional `redshift: Optional[float] = None` kwarg; new `redshift` attribute on the instance (float or `None`).
- CSV I/O (`output_to_csv`, `list_from_csv`, `to_csv`, `from_csv`) now round-trips a `redshift` column, emitted when any dataset supplies one.
- Validation: 

### [register FitPointDataset pytrees for jit(fit_from)](https://github.com/PyAutoLabs/PyAutoLens/pull/458) (PyAutoLabs/PyAutoLens)
**API Changes:** Adds a private `_register_fit_point_pytrees` classmethod on `AnalysisPoint` that registers `FitPointDataset`, `Tracer`, and the three `FitPositions*` classes as JAX pytrees. Called once from `fit_from` when `use_jax=True`. No public surface change.
See full details below.

### [feat: JAX pytree registration for FitInterferometer + MGE source](https://github.com/PyAutoLabs/PyAutoLens/pull/456) (PyAutoLabs/PyAutoLens)
**API Changes:** Adds ``_register_fit_interferometer_pytrees`` to ``AnalysisInterferometer`` and calls
it at the top of ``fit_from`` when ``use_jax=True``. Registers ``FitInterferometer``,
``Tracer`` and ``DatasetModel`` as pytrees with the appropriate ``no_flatten`` aux
fields. No public signature changes.

See ful

### [refactor: remove howtofit/ from autofit_workspace (sub-2 of howtofit extraction)](https://github.com/PyAutoLabs/autofit_workspace/pull/39) (PyAutoLabs/autofit_workspace)
**Scripts Changed:** **Deletions**
- `scripts/howtofit/` — 38 files removed (`chapter_1_introduction`, `chapter_2_scientific_workflow` stub, `chapter_3_graphical_models`, `intro/`, `plan/`, READMEs, `__init__.py`s)
- `notebooks/howtofit/` — 17 files removed (matching notebook tree)

**Cross-reference updates** (scripts 

### [ci: remove defunct api-update.yml workflow](https://github.com/PyAutoLabs/autofit_workspace/pull/35) (PyAutoLabs/autofit_workspace)
**Scripts Changed:** - .github/workflows/api-update.yml — deleted (defunct Copilot integration)

### [Add version.txt and check_version() in welcome.py](https://github.com/PyAutoLabs/autofit_workspace/pull/33) (PyAutoLabs/autofit_workspace)
**Scripts Changed:** - `welcome.py` — adds `from autoconf import check_version` and calls `check_version(af.__version__)` at startup so a mismatched workspace/library pair fails loudly before any modeling code runs.
- `version.txt` (new) — pins the workspace to the library version it was generated against.

### [docs: merge guides/results start_here.py files (simple + aggregator)](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/46) (PyAutoLabs/autogalaxy_workspace)
**Scripts Changed:** - `scripts/guides/results/start_here.py` — rewritten as a single tutorial in two halves: simple loading (Galaxies, Model, Samples, FITS) followed by the aggregator (Model Fit, Generators, Database, Workflow, Result, Samples, Linear Light Profiles, Galaxies, Fits, Units, Pixelization). Existing `test

### [Auto-generate mask_extra_galaxies.fits in simulators](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/41) (PyAutoLabs/autogalaxy_workspace)
**Scripts Changed:** - `scripts/imaging/features/extra_galaxies/simulator.py` — added `__Mask Extra Galaxies__` section that writes `mask_extra_galaxies.fits` from a union of `Mask2D.circular` regions around each extra-galaxy centre.
- `scripts/imaging/simulator_sersic.py` — added a no-op (all-False) `mask_extra_galaxie

### [fix: restore truncated data_preparation scripts (#85)](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/40) (PyAutoLabs/autogalaxy_workspace)
**Scripts Changed:** - `scripts/imaging/data_preparation.py` — restored body (15k restored from 2k stub); now uses `simple` dataset + auto-simulate.
- `scripts/imaging/data_preparation/examples/data.py` — restored body; uses `simple`; resize demo now reuses the loaded `data` (was: `simple__big_stamp` which is not genera

### [fix: enable fits_make / png_make smoke tests](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/39) (PyAutoLabs/autogalaxy_workspace)
**Scripts Changed:** - `config/build/env_vars.yaml` — add overrides for `fits_make` / `png_make` patterns that `unset: [PYAUTO_SKIP_VISUALIZATION, PYAUTO_FAST_PLOTS]`
- `scripts/guides/results/workflow/csv_make.py` — add `n_like_max=300` (with inline comment + `__N Like Max__` docstring section)
- `scripts/guides/result

### [fix(interferometer): strip lens light from pixelization SLaM scripts](https://github.com/PyAutoLabs/autolens_workspace/pull/106) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/interferometer/features/pixelization/delaunay.py` — `source_lp`: dropped the `lens_bulge` MGE definition and set `bulge=None, disk=None`. `source_pix_2`: replaced the forwarded `bulge=source_lp_result.instance.galaxies.lens.bulge` / `disk=...` with explicit `bulge=None, disk=None`. **This

### [fix: chain image_plane_mesh_grid through light_lp / mass_total in delaunay SLaM](https://github.com/PyAutoLabs/autolens_workspace/pull/104) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/imaging/features/pixelization/delaunay.py` — `light_lp` and `mass_total` SLaM helpers now propagate `galaxy_name_image_plane_mesh_grid_dict` from `source_result_for_source` into their `AdaptImages` constructor.
- `scripts/interferometer/features/pixelization/delaunay.py` — `mass_total` he

### [fix: drop PYAUTO_SMALL_DATASETS workaround in group simulators](https://github.com/PyAutoLabs/autolens_workspace/pull/102) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/group/simulator.py` — removed `import os`, `small_datasets = os.environ.pop(...)`, and the restore block around `solver.solve`.
- `scripts/group/features/multi_gaussian_expansion/simulator.py` — same cleanup.
- `scripts/group/features/no_lens_light/simulator.py` — same cleanup.

Net chang

### [feat(point_source): rename to multiple_sources and add multi-source modeling](https://github.com/PyAutoLabs/autolens_workspace/pull/100) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/point_source/features/multiple_sources/simulator.py` — renamed from `double_einstein_cross/simulator.py`; `dataset_name` updated to `multiple_sources`; `positions_1` noise-shape bug fixed (was `size=positions_0.shape`); docstring rewritten with PyAutoLens #480 notice; source_0's `Isotherm

### [docs: merge guides/results start_here.py files (simple + aggregator)](https://github.com/PyAutoLabs/autolens_workspace/pull/98) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/guides/results/start_here.py` — rewritten as a single tutorial in two halves: simple loading (Tracer, Model, Samples, FITS) followed by the aggregator (Model Fit, Generators, Database, Workflow, Result, Samples, Linear Light Profiles, Tracer, Fits, Galaxies, Units, Pixelization). Added `t
