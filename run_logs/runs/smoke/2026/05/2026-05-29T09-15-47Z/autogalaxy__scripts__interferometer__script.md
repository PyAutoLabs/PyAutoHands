# Test Report: autogalaxy / scripts/interferometer (script)

**23 scripts** | 21 passed | 2 skipped

| Status | Count |
|--------|-------|
| passed | 21 |
| skipped | 2 |

## Skipped

| Script | Reason |
|--------|--------|
| `likelihood_function.py` | NEEDS_FIX 2026-05-20 - LinAlgError: matrix singular in MGE inversion -> InversionException (known_numerical; same family as pixelization variants above) |
| `modeling.py` | NEEDS_FIX 2026-04-10 - LinAlgError: matrix not positive definite in interferometer pixelization modeling |

## Passed

- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/extra_galaxies/simulator.py` (3.5s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/pixelization/simulator.py` (6.2s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/simulator.py` (5.9s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/start_here.py` (13.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/casa_reduction.py` (2.8s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/data_preparation.py` (9.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/extra_galaxies/modeling.py` (8.0s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/linear_light_profiles/fit.py` (9.7s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/linear_light_profiles/likelihood_function.py` (7.2s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/linear_light_profiles/modeling.py` (8.1s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/multi_gaussian_expansion/fit.py` (10.0s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/multi_gaussian_expansion/modeling.py` (8.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/pixelization/fit.py` (10.9s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/pixelization/galaxy_reconstruction.py` (8.3s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/pixelization/likelihood_function.py` (13.1s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/pixelization/many_visibilities_preparation.py` (7.8s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/shapelets/fit.py` (6.5s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/shapelets/modeling.py` (31.8s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/fit.py` (9.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/likelihood_function.py` (10.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/modeling.py` (13.9s)
