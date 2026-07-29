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

- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/extra_galaxies/simulator.py` (4.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/multi_gaussian_expansion/simulator.py` (5.1s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/operated_light_profile/simulator.py` (8.5s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/simulator_manual_signal_to_noise.py` (5.2s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/sky_background/simulator.py` (4.9s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/simulator.py` (5.0s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/simulator_sample.py` (7.8s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/simulator_sersic.py` (4.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation/start_here.py` (4.0s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/start_here.py` (12.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation.py` (10.5s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation/examples/data.py` (12.1s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation/examples/noise_map.py` (8.5s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation/examples/optional/extra_galaxies_centres.py` (8.5s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation/examples/optional/info.py` (0.1s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation/examples/optional/light_centre.py` (8.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation/examples/optional/mask.py` (9.0s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation/examples/optional/mask_extra_galaxies.py` (8.7s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation/examples/psf.py` (4.3s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/extra_galaxies/modeling.py` (6.5s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/linear_light_profiles/fit.py` (7.1s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/linear_light_profiles/likelihood_function.py` (7.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/linear_light_profiles/modeling.py` (6.4s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/multi_gaussian_expansion/fit.py` (8.9s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/multi_gaussian_expansion/likelihood_function.py` (7.8s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/multi_gaussian_expansion/modeling.py` (41.4s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/operated_light_profile/modeling.py` (10.0s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/pixelization/fit.py` (9.3s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/pixelization/likelihood_function.py` (9.8s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/pixelization/source_science.py` (8.4s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/shapelets/fit.py` (17.1s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/shapelets/modeling.py` (91.0s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/sky_background/fit.py` (25.0s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/sky_background/modeling.py` (18.2s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/fit.py` (25.3s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/likelihood_function.py` (6.1s)
