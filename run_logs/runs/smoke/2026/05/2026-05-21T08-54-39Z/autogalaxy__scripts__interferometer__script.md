# Test Report: autogalaxy / scripts/interferometer (script)

**22 scripts** | 20 passed | 2 skipped

| Status | Count |
|--------|-------|
| passed | 20 |
| skipped | 2 |

## Skipped

| Script | Reason |
|--------|--------|
| `likelihood_function.py` | NEEDS_FIX 2026-05-20 - LinAlgError: matrix singular in MGE inversion -> InversionException (known_numerical; same family as pixelization variants above) |
| `modeling.py` | NEEDS_FIX 2026-04-10 - LinAlgError: matrix not positive definite in interferometer pixelization modeling |

## Passed

- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/extra_galaxies/simulator.py` (3.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/simulator.py` (5.8s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/start_here.py` (13.3s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/casa_reduction.py` (3.2s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/data_preparation.py` (9.2s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/extra_galaxies/modeling.py` (6.5s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/linear_light_profiles/fit.py` (5.9s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/linear_light_profiles/likelihood_function.py` (6.3s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/linear_light_profiles/modeling.py` (6.8s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/multi_gaussian_expansion/fit.py` (6.4s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/multi_gaussian_expansion/modeling.py` (10.4s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/pixelization/fit.py` (5.5s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/pixelization/likelihood_function.py` (4.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/pixelization/many_visibilities_preparation.py` (4.1s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/pixelization/source_science.py` (5.9s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/shapelets/fit.py` (7.0s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/shapelets/modeling.py` (32.5s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/fit.py` (6.2s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/likelihood_function.py` (5.7s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/modeling.py` (6.7s)
