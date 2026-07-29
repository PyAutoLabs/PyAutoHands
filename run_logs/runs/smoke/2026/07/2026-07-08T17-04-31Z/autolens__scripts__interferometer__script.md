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

- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/datacube/simulator.py` (10.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/extra_galaxies/simulator.py` (7.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/subhalo/simulator.py` (10.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/simulator.py` (15.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/datacube/start_here.py` (23.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/subhalo/detect/start_here.py` (32.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/subhalo/sensitivity/start_here.py` (0.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/start_here.py` (46.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/data_preparation.py` (20.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/advanced/shapelets/fit.py` (15.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/advanced/shapelets/modeling.py` (31.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/datacube/data_preparation.py` (7.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/datacube/delaunay.py` (21.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/datacube/likelihood_function.py` (19.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/datacube/modeling.py` (20.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/datacube/modeling_parametric.py` (20.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/extra_galaxies/modeling.py` (25.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/extra_galaxies/slam.py` (29.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/linear_light_profiles/fit.py` (20.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/linear_light_profiles/likelihood_function.py` (14.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/linear_light_profiles/modeling.py` (20.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/linear_light_profiles/slam.py` (43.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/multi_gaussian_expansion/fit.py` (22.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/multi_gaussian_expansion/likelihood_function.py` (21.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/multi_gaussian_expansion/modeling.py` (28.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/multi_gaussian_expansion/slam.py` (36.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/pixelization/fit.py` (34.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/pixelization/likelihood_function.py` (49.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/pixelization/many_visibilities_preparation.py` (20.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/pixelization/modeling.py` (32.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/pixelization/slam.py` (31.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/pixelization/source_science.py` (20.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/fit.py` (24.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/likelihood_function.py` (18.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/modeling.py` (54.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/source_science.py` (17.7s)
