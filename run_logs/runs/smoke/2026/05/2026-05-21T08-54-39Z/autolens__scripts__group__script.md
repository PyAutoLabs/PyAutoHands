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

- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/double_einstein_ring/simulator.py` (3.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/mass_stellar_dark/simulator.py` (4.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/operated_light_profile/simulator.py` (4.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/sky_background/simulator.py` (5.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/subhalo/simulator.py` (4.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/multi_gaussian_expansion/simulator.py` (4.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/no_lens_light/simulator.py` (3.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/scaling_relation/simulator.py` (5.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/simulator.py` (4.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/data_preparation/start_here.py` (3.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/subhalo/detect/start_here.py` (12.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/start_here.py` (43.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/double_einstein_ring/chaining.py` (5.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/double_einstein_ring/fit.py` (7.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/double_einstein_ring/likelihood_function.py` (4.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/double_einstein_ring/modeling.py` (5.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/mass_stellar_dark/chaining.py` (5.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/mass_stellar_dark/fit.py` (5.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/mass_stellar_dark/likelihood_function.py` (3.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/operated_light_profile/modeling.py` (9.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/shapelets/fit.py` (5.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/shapelets/modeling.py` (24.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/sky_background/fit.py` (4.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/sky_background/modeling.py` (9.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/linear_light_profiles/fit.py` (4.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/linear_light_profiles/likelihood_function.py` (4.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/linear_light_profiles/modeling.py` (9.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/linear_light_profiles/slam.py` (15.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/multi_gaussian_expansion/fit.py` (5.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/multi_gaussian_expansion/likelihood_function.py` (4.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/multi_gaussian_expansion/modeling.py` (10.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/multi_gaussian_expansion/slam.py` (9.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/multi_gaussian_expansion/source_science.py` (4.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/no_lens_light/modeling.py` (9.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/no_lens_light/slam.py` (8.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/pixelization/adaptive.py` (8.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/pixelization/cpu_fast_modeling.py` (7.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/pixelization/delaunay.py` (6.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/pixelization/fit.py` (5.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/pixelization/likelihood_function.py` (4.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/pixelization/modeling.py` (10.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/pixelization/slam.py` (12.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/pixelization/source_science.py` (4.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/scaling_relation/fit.py` (5.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/scaling_relation/likelihood_function.py` (3.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/scaling_relation/modeling.py` (9.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/scaling_relation/modeling_for_luminosities.py` (8.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/fit.py` (4.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/likelihood_function.py` (4.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/modeling.py` (9.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/source_science.py` (3.6s)
