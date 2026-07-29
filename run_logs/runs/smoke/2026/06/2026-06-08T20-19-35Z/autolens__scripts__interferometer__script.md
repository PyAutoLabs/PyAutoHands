# Test Report: autolens / scripts/interferometer (script)

**38 scripts** | 36 passed | 2 skipped

| Status | Count |
|--------|-------|
| passed | 36 |
| skipped | 2 |

## Skipped

| Script | Reason |
|--------|--------|
| `casa_reduction.py` | Requires CASA MeasurementSet output, not runnable standalone |
| `delaunay.py` | NEEDS_FIX 2026-04-10 - broadcast shape mismatch (2,2) vs (1032,1032) in Delaunay interferometer |

## Passed

- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/datacube/simulator.py` (5.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/extra_galaxies/simulator.py` (6.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/subhalo/simulator.py` (5.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/simulator.py` (8.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/datacube/start_here.py` (11.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/subhalo/detect/start_here.py` (17.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/subhalo/sensitivity/start_here.py` (0.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/start_here.py` (25.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/data_preparation.py` (13.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/advanced/shapelets/fit.py` (11.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/advanced/shapelets/modeling.py` (18.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/datacube/data_preparation.py` (3.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/datacube/delaunay.py` (13.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/datacube/likelihood_function.py` (10.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/datacube/modeling.py` (12.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/datacube/modeling_parametric.py` (7.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/extra_galaxies/modeling.py` (10.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/extra_galaxies/slam.py` (13.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/linear_light_profiles/fit.py` (8.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/linear_light_profiles/likelihood_function.py` (10.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/linear_light_profiles/modeling.py` (8.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/linear_light_profiles/slam.py` (10.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/multi_gaussian_expansion/fit.py` (9.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/multi_gaussian_expansion/likelihood_function.py` (7.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/multi_gaussian_expansion/modeling.py` (9.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/multi_gaussian_expansion/slam.py` (14.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/pixelization/fit.py` (12.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/pixelization/likelihood_function.py` (12.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/pixelization/many_visibilities_preparation.py` (6.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/pixelization/modeling.py` (9.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/pixelization/slam.py` (10.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/pixelization/source_science.py` (13.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/fit.py` (10.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/likelihood_function.py` (7.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/modeling.py` (19.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/source_science.py` (5.9s)
