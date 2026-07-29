# Test Report: autogalaxy / scripts/imaging (script)

**44 scripts** | 37 passed | 7 skipped

| Status | Count |
|--------|-------|
| passed | 37 |
| skipped | 7 |

## Skipped

| Script | Reason |
|--------|--------|
| `extra_galaxies_centres.py` | GUI scripts cannot be run |
| `light_centre.py` | GUI scripts cannot be run |
| `mask.py` | GUI scripts cannot be run |
| `mask_extra_galaxies.py` | GUI scripts cannot be run |
| `mask_irregular.py` | NEEDS_FIX 2026-04-10 - silent failure, needs investigation |
| `modeling.py` | NEEDS_FIX 2026-04-10 - LinAlgError: matrix not positive definite in pixelization modeling |
| `modeling.py` | NEEDS_FIX 2026-04-10 - KeyError on ('galaxies','galaxy','bulge','ell_comps'...) kwargs after API drift in top-level imaging/modeling.py |

## Passed

- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/extra_galaxies/simulator.py` (15.2s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/multi_gaussian_expansion/simulator.py` (18.2s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/operated_light_profile/simulator.py` (18.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/pixelization/simulator.py` (18.4s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/simulator_manual_signal_to_noise.py` (12.3s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/sky_background/simulator.py` (10.1s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/simulator.py` (9.7s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/simulator_sample.py` (12.2s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/simulator_sersic.py` (7.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation/start_here.py` (8.8s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/start_here.py` (28.9s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation.py` (20.7s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation/examples/data.py` (15.3s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation/examples/noise_map.py` (15.9s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation/examples/optional/extra_galaxies_centres.py` (15.7s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation/examples/optional/info.py` (0.1s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation/examples/optional/light_centre.py` (16.4s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation/examples/optional/mask.py` (16.0s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation/examples/optional/mask_extra_galaxies.py` (16.5s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation/examples/psf.py` (7.7s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/extra_galaxies/modeling.py` (12.0s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/linear_light_profiles/fit.py` (8.9s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/linear_light_profiles/likelihood_function.py` (9.3s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/linear_light_profiles/modeling.py` (13.3s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/multi_gaussian_expansion/fit.py` (21.8s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/multi_gaussian_expansion/likelihood_function.py` (14.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/multi_gaussian_expansion/modeling.py` (33.5s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/operated_light_profile/modeling.py` (15.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/pixelization/fit.py` (19.1s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/pixelization/galaxy_reconstruction.py` (16.9s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/pixelization/likelihood_function.py` (17.4s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/shapelets/fit.py` (21.0s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/shapelets/modeling.py` (88.4s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/sky_background/fit.py` (14.1s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/sky_background/modeling.py` (16.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/fit.py` (37.5s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/likelihood_function.py` (17.7s)
