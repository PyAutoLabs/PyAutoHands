# Test Report: autolens / scripts/group (script)

**55 scripts** | 3 failed | 49 passed | 3 skipped

| Status | Count |
|--------|-------|
| failed | 3 |
| passed | 49 |
| skipped | 3 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/double_einstein_ring/slam.py` — FAILED (13.3s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/double_einstein_ring/slam.py']' returned non-zero exit status 1.

```
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/double_einstein_ring/slam.py", line 689, in <module>
    source_pix_result_1_source_1 = source_pix_1_source_1(
                                   ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/double_einstein_ring/slam.py", line 474, in source_pix_1_source_1
    return search.fit(model=model, analysis=analysis, **settings_search.fit_dict)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/abstract_search.py", line 512, in fit
    result = self.start_resume_fit(
             ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/abstract_search.py", line 117, in decorated
    return func(self, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/abstract_search.py", line 661, in start_resume_fit
    return self._fit_bypass_test_mode(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/abstract_search.py", line 848, in _fit_bypass_test_mode
    analysis.log_likelihood_function(instance)
  File "/home/jammy/Code/PyAutoLabs/PyAutoLens/autolens/imaging/model/analysis.py", line 84, in log_likelihood_function
    raise af.exc.FitException
autofit.exc.FitException
```

### `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/linear_light_profiles/slam.py` — FAILED (8.2s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/linear_light_profiles/slam.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/linear_light_profiles/slam.py", line 921, in <module>
    source_pix_result_1, dataset, adapt_images = source_pix_1(
                                                 ^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/linear_light_profiles/slam.py", line 341, in source_pix_1
    image_plane_mesh_grid = image_mesh.image_plane_mesh_grid_from(
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/inversion/mesh/image_mesh/hilbert.py", line 267, in image_plane_mesh_grid_from
    raise exc.PixelizationException(
autoarray.exc.PixelizationException: 
                Hilbert image-mesh has been called but the input grid does not use a circular mask.
                
                Ensure that analysis is using a circular mask via the Mask2D.circular classmethod.
```

### `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/no_lens_light/slam.py` — FAILED (7.0s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/no_lens_light/slam.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/no_lens_light/slam.py", line 583, in <module>
    source_pix_result_1, dataset, adapt_images = source_pix_1(
                                                 ^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/no_lens_light/slam.py", line 183, in source_pix_1
    image_plane_mesh_grid = image_mesh.image_plane_mesh_grid_from(
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/inversion/mesh/image_mesh/hilbert.py", line 267, in image_plane_mesh_grid_from
    raise exc.PixelizationException(
autoarray.exc.PixelizationException: 
                Hilbert image-mesh has been called but the input grid does not use a circular mask.
                
                Ensure that analysis is using a circular mask via the Mask2D.circular classmethod.
```

## Skipped

| Script | Reason |
|--------|--------|
| `modeling.py` | Requires CSE to be JAX enabled. |
| `slam.py` | Requires CSE to be JAX enabled. |
| `slam.py` | NEEDS_FIX 2026-04-10 - PriorException: upper limit must be greater than lower limit in group SLaM pipeline |

## Passed

- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/double_einstein_ring/simulator.py` (5.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/mass_stellar_dark/simulator.py` (8.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/operated_light_profile/simulator.py` (6.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/sky_background/simulator.py` (4.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/subhalo/simulator.py` (5.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/multi_gaussian_expansion/simulator.py` (4.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/no_lens_light/simulator.py` (4.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/scaling_relation/simulator.py` (5.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/simulator.py` (5.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/data_preparation/start_here.py` (4.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/subhalo/detect/start_here.py` (16.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/start_here.py` (81.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/double_einstein_ring/chaining.py` (8.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/double_einstein_ring/fit.py` (15.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/double_einstein_ring/likelihood_function.py` (8.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/double_einstein_ring/modeling.py` (7.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/mass_stellar_dark/chaining.py` (11.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/mass_stellar_dark/fit.py` (12.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/mass_stellar_dark/likelihood_function.py` (10.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/operated_light_profile/modeling.py` (13.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/shapelets/fit.py` (11.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/shapelets/modeling.py` (37.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/sky_background/fit.py` (12.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/advanced/sky_background/modeling.py` (13.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/linear_light_profiles/fit.py` (6.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/linear_light_profiles/likelihood_function.py` (11.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/linear_light_profiles/modeling.py` (12.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/multi_gaussian_expansion/fit.py` (10.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/multi_gaussian_expansion/likelihood_function.py` (11.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/multi_gaussian_expansion/modeling.py` (13.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/multi_gaussian_expansion/slam.py` (22.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/multi_gaussian_expansion/source_science.py` (10.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/no_lens_light/modeling.py` (13.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/pixelization/adaptive.py` (22.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/pixelization/cpu_fast_modeling.py` (15.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/pixelization/delaunay.py` (15.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/pixelization/fit.py` (10.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/pixelization/likelihood_function.py` (9.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/pixelization/modeling.py` (13.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/pixelization/slam.py` (25.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/pixelization/source_science.py` (7.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/scaling_relation/fit.py` (15.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/scaling_relation/likelihood_function.py` (6.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/scaling_relation/modeling.py` (13.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/features/scaling_relation/modeling_for_luminosities.py` (16.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/fit.py` (9.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/likelihood_function.py` (10.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/modeling.py` (12.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/group/source_science.py` (4.8s)
