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

- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/datacube/simulator.py` (8.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/extra_galaxies/simulator.py` (4.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/subhalo/simulator.py` (4.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/simulator.py` (7.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/datacube/start_here.py` (13.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/subhalo/detect/start_here.py` (18.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/subhalo/sensitivity/start_here.py` (0.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/start_here.py` (25.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/data_preparation.py` (12.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/advanced/shapelets/fit.py` (10.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/advanced/shapelets/modeling.py` (18.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/datacube/data_preparation.py` (4.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/datacube/delaunay.py` (11.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/datacube/likelihood_function.py` (10.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/datacube/modeling.py` (10.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/datacube/modeling_parametric.py` (7.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/extra_galaxies/modeling.py` (10.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/extra_galaxies/slam.py` (13.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/linear_light_profiles/fit.py` (7.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/linear_light_profiles/likelihood_function.py` (10.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/linear_light_profiles/modeling.py` (9.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/linear_light_profiles/slam.py` (11.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/multi_gaussian_expansion/fit.py` (9.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/multi_gaussian_expansion/likelihood_function.py` (7.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/multi_gaussian_expansion/modeling.py` (9.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/multi_gaussian_expansion/slam.py` (13.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/pixelization/fit.py` (12.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/pixelization/likelihood_function.py` (11.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/pixelization/many_visibilities_preparation.py` (7.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/pixelization/modeling.py` (10.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/pixelization/slam.py` (13.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/pixelization/source_science.py` (10.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/fit.py` (9.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/likelihood_function.py` (7.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/modeling.py` (16.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/source_science.py` (6.0s)
