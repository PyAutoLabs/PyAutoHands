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

- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/extra_galaxies/simulator.py` (9.7s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/multi_gaussian_expansion/simulator.py` (5.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/operated_light_profile/simulator.py` (5.9s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/simulator_manual_signal_to_noise.py` (5.8s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/sky_background/simulator.py` (6.4s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/simulator.py` (8.1s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/simulator_sample.py` (11.1s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/simulator_sersic.py` (7.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation/start_here.py` (3.4s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/start_here.py` (26.0s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation.py` (9.2s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation/examples/data.py` (8.8s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation/examples/noise_map.py` (10.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation/examples/optional/extra_galaxies_centres.py` (18.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation/examples/optional/info.py` (0.1s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation/examples/optional/light_centre.py` (18.1s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation/examples/optional/mask.py` (17.9s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation/examples/optional/mask_extra_galaxies.py` (11.1s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/data_preparation/examples/psf.py` (7.9s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/extra_galaxies/modeling.py` (10.5s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/linear_light_profiles/fit.py` (6.7s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/linear_light_profiles/likelihood_function.py` (5.3s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/linear_light_profiles/modeling.py` (12.2s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/multi_gaussian_expansion/fit.py` (13.3s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/multi_gaussian_expansion/likelihood_function.py` (7.8s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/multi_gaussian_expansion/modeling.py` (50.8s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/operated_light_profile/modeling.py` (9.8s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/pixelization/fit.py` (13.3s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/pixelization/likelihood_function.py` (12.4s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/pixelization/source_science.py` (9.5s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/shapelets/fit.py` (17.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/shapelets/modeling.py` (60.5s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/sky_background/fit.py` (8.9s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/features/sky_background/modeling.py` (6.7s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/fit.py` (13.7s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/imaging/likelihood_function.py` (7.5s)
