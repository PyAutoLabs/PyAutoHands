# Test Report: autolens / scripts/imaging (script)

**79 scripts** | 62 passed | 15 skipped | 2 timeout

| Status | Count |
|--------|-------|
| passed | 62 |
| skipped | 15 |
| timeout | 2 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/los_halos/simulator.py` — TIMEOUT (300.1s)

Timed out after 300s

### `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/los_halos/simulator_jax.py` — TIMEOUT (300.1s)

Timed out after 300s

## Skipped

| Script | Reason |
|--------|--------|
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

## Passed

- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/double_einstein_ring/simulator.py` (4.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/mass_stellar_dark/simulator.py` (8.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/operated_light_profile/simulator.py` (13.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/sky_background/simulator.py` (10.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/subhalo/simulator.py` (17.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/extra_galaxies/simulator.py` (12.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/multi_gaussian_expansion/simulator.py` (10.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/no_lens_light/simulator.py` (9.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/scaling_relation/simulator.py` (7.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/simulator_manual_signal_to_noise_ratio.py` (7.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/simulator.py` (6.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/simulator_sample.py` (10.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/data_preparation/start_here.py` (5.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/subhalo/detect/start_here.py` (23.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/start_here.py` (63.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/data_preparation/examples/data.py` (15.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/data_preparation/examples/noise_map.py` (20.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/data_preparation/examples/optional/extra_galaxies_centres.py` (15.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/data_preparation/examples/optional/info.py` (15.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/data_preparation/examples/optional/lens_light_centre.py` (16.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/data_preparation/examples/optional/mask.py` (12.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/data_preparation/examples/optional/mask_extra_galaxies.py` (10.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/data_preparation/examples/optional/positions.py` (12.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/data_preparation/examples/psf.py` (4.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/double_einstein_ring/chaining.py` (14.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/double_einstein_ring/fit.py` (10.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/double_einstein_ring/likelihood_function.py` (5.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/double_einstein_ring/modeling.py` (7.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/mass_stellar_dark/chaining.py` (6.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/mass_stellar_dark/fit.py` (8.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/mass_stellar_dark/likelihood_function.py` (5.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/operated_light_profile/modeling.py` (8.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/shapelets/fit.py` (11.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/shapelets/modeling.py` (29.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/sky_background/fit.py` (9.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/sky_background/modeling.py` (7.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/extra_galaxies/modeling.py` (8.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/extra_galaxies/slam.py` (15.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/linear_light_profiles/fit.py` (7.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/linear_light_profiles/likelihood_function.py` (7.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/linear_light_profiles/modeling.py` (9.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/linear_light_profiles/slam.py` (11.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/multi_gaussian_expansion/fit.py` (11.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/multi_gaussian_expansion/likelihood_function.py` (7.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/multi_gaussian_expansion/modeling.py` (28.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/multi_gaussian_expansion/slam.py` (9.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/multi_gaussian_expansion/source_science.py` (9.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/no_lens_light/modeling.py` (9.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/no_lens_light/slam.py` (14.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/pixelization/adaptive.py` (10.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/pixelization/cpu_fast_modeling.py` (12.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/pixelization/fit.py` (8.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/pixelization/likelihood_function.py` (6.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/pixelization/modeling.py` (7.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/pixelization/source_science.py` (8.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/scaling_relation/fit.py` (6.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/scaling_relation/likelihood_function.py` (6.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/scaling_relation/modeling.py` (14.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/fit.py` (13.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/likelihood_function.py` (8.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/modeling.py` (15.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/source_science.py` (8.0s)
