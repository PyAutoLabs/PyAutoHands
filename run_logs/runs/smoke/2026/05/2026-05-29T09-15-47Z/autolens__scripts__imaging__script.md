# Test Report: autolens / scripts/imaging (script)

**79 scripts** | 64 passed | 15 skipped

| Status | Count |
|--------|-------|
| passed | 64 |
| skipped | 15 |

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

- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/double_einstein_ring/simulator.py` (10.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/los_halos/simulator.py` (31.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/los_halos/simulator_jax.py` (46.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/mass_stellar_dark/simulator.py` (12.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/operated_light_profile/simulator.py` (10.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/sky_background/simulator.py` (8.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/subhalo/simulator.py` (11.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/extra_galaxies/simulator.py` (12.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/multi_gaussian_expansion/simulator.py` (7.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/no_lens_light/simulator.py` (8.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/scaling_relation/simulator.py` (6.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/simulator_manual_signal_to_noise_ratio.py` (8.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/simulator.py` (7.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/simulator_sample.py` (12.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/data_preparation/start_here.py` (5.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/subhalo/detect/start_here.py` (24.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/start_here.py` (74.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/data_preparation/examples/data.py` (11.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/data_preparation/examples/noise_map.py` (9.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/data_preparation/examples/optional/extra_galaxies_centres.py` (7.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/data_preparation/examples/optional/info.py` (6.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/data_preparation/examples/optional/lens_light_centre.py` (7.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/data_preparation/examples/optional/mask.py` (7.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/data_preparation/examples/optional/mask_extra_galaxies.py` (7.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/data_preparation/examples/optional/positions.py` (7.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/data_preparation/examples/psf.py` (3.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/double_einstein_ring/chaining.py` (10.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/double_einstein_ring/fit.py` (8.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/double_einstein_ring/likelihood_function.py` (5.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/double_einstein_ring/modeling.py` (5.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/mass_stellar_dark/chaining.py` (4.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/mass_stellar_dark/fit.py` (5.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/mass_stellar_dark/likelihood_function.py` (4.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/operated_light_profile/modeling.py` (9.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/shapelets/fit.py` (10.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/shapelets/modeling.py` (19.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/sky_background/fit.py` (5.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/sky_background/modeling.py` (7.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/extra_galaxies/modeling.py` (6.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/extra_galaxies/slam.py` (13.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/linear_light_profiles/fit.py` (7.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/linear_light_profiles/likelihood_function.py` (5.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/linear_light_profiles/modeling.py` (5.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/linear_light_profiles/slam.py` (7.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/multi_gaussian_expansion/fit.py` (10.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/multi_gaussian_expansion/likelihood_function.py` (7.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/multi_gaussian_expansion/modeling.py` (23.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/multi_gaussian_expansion/slam.py` (7.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/multi_gaussian_expansion/source_science.py` (7.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/no_lens_light/modeling.py` (10.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/no_lens_light/slam.py` (12.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/pixelization/adaptive.py` (9.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/pixelization/cpu_fast_modeling.py` (10.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/pixelization/fit.py` (9.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/pixelization/likelihood_function.py` (6.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/pixelization/modeling.py` (8.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/pixelization/source_science.py` (7.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/scaling_relation/fit.py` (8.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/scaling_relation/likelihood_function.py` (4.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/scaling_relation/modeling.py` (13.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/fit.py` (12.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/likelihood_function.py` (4.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/modeling.py` (10.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/source_science.py` (3.6s)
