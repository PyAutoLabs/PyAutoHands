# Test Report: autogalaxy / scripts/imaging (script)

**43 scripts** | 36 passed | 7 skipped

| Status | Count |
|--------|-------|
| passed | 36 |
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

- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/extra_galaxies/simulator.py` (10.3s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/multi_gaussian_expansion/simulator.py` (9.4s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/operated_light_profile/simulator.py` (7.0s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/simulator_manual_signal_to_noise.py` (5.2s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/sky_background/simulator.py` (7.1s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/simulator.py` (6.0s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/simulator_sample.py` (12.4s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/simulator_sersic.py` (11.2s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation/start_here.py` (6.1s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/start_here.py` (16.1s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation.py` (8.4s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation/examples/data.py` (9.0s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation/examples/noise_map.py` (6.3s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation/examples/optional/extra_galaxies_centres.py` (6.8s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation/examples/optional/info.py` (0.1s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation/examples/optional/light_centre.py` (8.0s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation/examples/optional/mask.py` (7.8s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation/examples/optional/mask_extra_galaxies.py` (9.2s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation/examples/psf.py` (4.1s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/extra_galaxies/modeling.py` (7.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/linear_light_profiles/fit.py` (7.5s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/linear_light_profiles/likelihood_function.py` (3.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/linear_light_profiles/modeling.py` (8.8s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/multi_gaussian_expansion/fit.py` (7.9s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/multi_gaussian_expansion/likelihood_function.py` (7.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/multi_gaussian_expansion/modeling.py` (40.4s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/operated_light_profile/modeling.py` (7.7s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/pixelization/fit.py` (7.2s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/pixelization/likelihood_function.py` (5.8s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/pixelization/source_science.py` (3.9s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/shapelets/fit.py` (8.8s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/shapelets/modeling.py` (25.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/sky_background/fit.py` (4.9s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/sky_background/modeling.py` (4.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/fit.py` (9.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/likelihood_function.py` (4.1s)
