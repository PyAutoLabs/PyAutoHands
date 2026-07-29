# Test Report: autolens / scripts/group (script)

**55 scripts** | 51 passed | 4 skipped

| Status | Count |
|--------|-------|
| passed | 51 |
| skipped | 4 |

## Skipped

| Script | Reason |
|--------|--------|
| `slam.py` | NEEDS_FIX 2026-05-20 - same cascade as imaging variant — synthetic samples_summary lacks adapt_data; parking pattern of the imaging entry didn't cover this group/ twin |
| `modeling.py` | Requires CSE to be JAX enabled. |
| `slam.py` | Requires CSE to be JAX enabled. |
| `slam.py` | NEEDS_FIX 2026-04-10 - PriorException: upper limit must be greater than lower limit in group SLaM pipeline |

## Passed

- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/double_einstein_ring/simulator.py` (4.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/mass_stellar_dark/simulator.py` (6.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/operated_light_profile/simulator.py` (4.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/sky_background/simulator.py` (4.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/subhalo/simulator.py` (4.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/multi_gaussian_expansion/simulator.py` (4.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/no_lens_light/simulator.py` (4.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/scaling_relation/simulator.py` (4.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/simulator.py` (5.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/data_preparation/start_here.py` (3.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/subhalo/detect/start_here.py` (17.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/start_here.py` (60.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/double_einstein_ring/chaining.py` (6.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/double_einstein_ring/fit.py` (12.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/double_einstein_ring/likelihood_function.py` (5.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/double_einstein_ring/modeling.py` (6.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/mass_stellar_dark/chaining.py` (7.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/mass_stellar_dark/fit.py` (8.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/mass_stellar_dark/likelihood_function.py` (4.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/operated_light_profile/modeling.py` (12.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/shapelets/fit.py` (7.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/shapelets/modeling.py` (24.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/sky_background/fit.py` (6.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/sky_background/modeling.py` (16.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/linear_light_profiles/fit.py` (7.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/linear_light_profiles/likelihood_function.py` (6.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/linear_light_profiles/modeling.py` (13.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/linear_light_profiles/slam.py` (26.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/multi_gaussian_expansion/fit.py` (9.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/multi_gaussian_expansion/likelihood_function.py` (7.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/multi_gaussian_expansion/modeling.py` (13.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/multi_gaussian_expansion/slam.py` (13.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/multi_gaussian_expansion/source_science.py` (5.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/no_lens_light/modeling.py` (14.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/no_lens_light/slam.py` (13.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/pixelization/adaptive.py` (12.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/pixelization/cpu_fast_modeling.py` (8.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/pixelization/delaunay.py` (9.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/pixelization/fit.py` (8.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/pixelization/likelihood_function.py` (5.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/pixelization/modeling.py` (11.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/pixelization/slam.py` (18.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/pixelization/source_science.py` (5.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/scaling_relation/fit.py` (7.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/scaling_relation/likelihood_function.py` (4.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/scaling_relation/modeling.py` (11.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/scaling_relation/modeling_for_luminosities.py` (12.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/fit.py` (5.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/likelihood_function.py` (7.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/modeling.py` (12.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/source_science.py` (4.2s)
