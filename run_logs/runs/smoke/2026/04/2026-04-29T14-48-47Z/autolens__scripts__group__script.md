# Test Report: autolens / scripts/group (script)

**38 scripts** | 7 failed | 30 passed | 1 skipped

| Status | Count |
|--------|-------|
| failed | 7 |
| passed | 30 |
| skipped | 1 |

## Failures

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/advanced/subhalo/detect/start_here.py` — FAILED (7.3s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/advanced/subhalo/detect/start_here.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/advanced/subhalo/detect/start_here.py", line 803, in <module>
    light_result = light_lp(
                   ^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/advanced/subhalo/detect/start_here.py", line 354, in light_lp
    galaxies=af.Collection(**lens_dict, source=source),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: autofit.mapper.prior_model.collection.Collection() got multiple values for keyword argument 'source'
```

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/linear_light_profiles/slam.py` — FAILED (3.7s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/linear_light_profiles/slam.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/linear_light_profiles/slam.py", line 891, in <module>
    source_lp_result_1 = source_lp_1(
                         ^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/linear_light_profiles/slam.py", line 235, in source_lp_1
    mass.einstein_radius = af.UniformPrior(
                           ^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoFit/autofit/mapper/prior/uniform.py", line 53, in __init__
    raise exc.PriorException(
autoconf.exc.PriorException: The upper limit of a prior must be greater than its lower limit
```

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/pixelization/delaunay.py` — FAILED (3.0s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/pixelization/delaunay.py']' returned non-zero exit status 1.

```
                         ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoConf/autoconf/tools/decorators.py", line 19, in __get__
    obj.__dict__[self.func.__name__] = self.func(obj)
                                       ^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoLens/autolens/lens/to_inversion.py", line 436, in mapper_galaxy_dict
    mapper = to_inversion.mapper_from(
             ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoGalaxy/autogalaxy/galaxy/to_inversion.py", line 489, in mapper_from
    interpolator = mesh.interpolator_from(
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/inversion/mesh/mesh/delaunay.py", line 158, in interpolator_from
    relocated_mesh_grid = self.relocated_mesh_grid_from(
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/inversion/mesh/mesh/abstract.py", line 91, in relocated_mesh_grid_from
    return border_relocator.relocated_mesh_grid_from(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/inversion/mesh/border_relocator.py", line 450, in relocated_mesh_grid_from
    grid=mesh_grid.array, origin=origin, a=a, b=b, phi=phi, xp=xp
         ^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'array'
```

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/pixelization/fit.py` — FAILED (3.1s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/pixelization/fit.py']' returned non-zero exit status 1.

```
                         ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoConf/autoconf/tools/decorators.py", line 19, in __get__
    obj.__dict__[self.func.__name__] = self.func(obj)
                                       ^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoLens/autolens/lens/to_inversion.py", line 436, in mapper_galaxy_dict
    mapper = to_inversion.mapper_from(
             ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoGalaxy/autogalaxy/galaxy/to_inversion.py", line 489, in mapper_from
    interpolator = mesh.interpolator_from(
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/inversion/mesh/mesh/delaunay.py", line 158, in interpolator_from
    relocated_mesh_grid = self.relocated_mesh_grid_from(
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/inversion/mesh/mesh/abstract.py", line 91, in relocated_mesh_grid_from
    return border_relocator.relocated_mesh_grid_from(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/inversion/mesh/border_relocator.py", line 450, in relocated_mesh_grid_from
    grid=mesh_grid.array, origin=origin, a=a, b=b, phi=phi, xp=xp
         ^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'array'
```

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/pixelization/likelihood_function.py` — FAILED (3.1s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/pixelization/likelihood_function.py']' returned non-zero exit status 1.

```
                         ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoConf/autoconf/tools/decorators.py", line 19, in __get__
    obj.__dict__[self.func.__name__] = self.func(obj)
                                       ^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoLens/autolens/lens/to_inversion.py", line 436, in mapper_galaxy_dict
    mapper = to_inversion.mapper_from(
             ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoGalaxy/autogalaxy/galaxy/to_inversion.py", line 489, in mapper_from
    interpolator = mesh.interpolator_from(
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/inversion/mesh/mesh/delaunay.py", line 158, in interpolator_from
    relocated_mesh_grid = self.relocated_mesh_grid_from(
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/inversion/mesh/mesh/abstract.py", line 91, in relocated_mesh_grid_from
    return border_relocator.relocated_mesh_grid_from(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/inversion/mesh/border_relocator.py", line 450, in relocated_mesh_grid_from
    grid=mesh_grid.array, origin=origin, a=a, b=b, phi=phi, xp=xp
         ^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'array'
```

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/pixelization/modeling.py` — FAILED (7.4s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/pixelization/modeling.py']' returned non-zero exit status 1.

```
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoFit/autofit/mapper/prior_model/prior_model.py", line 462, in _instance_for_arguments
    ] = prior_model.instance_for_arguments(
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoFit/autofit/mapper/prior_model/abstract.py", line 1403, in instance_for_arguments
    return self._instance_for_arguments(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoFit/autofit/mapper/prior_model/prior_model.py", line 462, in _instance_for_arguments
    ] = prior_model.instance_for_arguments(
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoFit/autofit/mapper/prior_model/abstract.py", line 1403, in instance_for_arguments
    return self._instance_for_arguments(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoFit/autofit/mapper/prior_model/prior_model.py", line 495, in _instance_for_arguments
    result = self.cls(**constructor_arguments)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/inversion/mesh/mesh/delaunay.py", line 58, in __init__
    pixels = int(pixels) + zeroed_pixels
             ~~~~~~~~~~~~^~~~~~~~~~~~~~~
TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
```

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/pixelization/slam.py` — FAILED (6.9s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/pixelization/slam.py']' returned non-zero exit status 1.

```
/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/operators/convolver.py:925: UserWarning: No blurring_image provided. Only the direct image will be convolved. This may change the correctness of the PSF convolution.
  warnings.warn(
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/pixelization/slam.py", line 751, in <module>
    ).positions
      ^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'positions'
```

## Skipped

| Script | Reason |
|--------|--------|
| `slam.py` | NEEDS_FIX 2026-04-10 - PriorException: upper limit must be greater than lower limit in group SLaM pipeline |

## Passed

- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/advanced/operated_light_profile/simulator.py` (4.1s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/advanced/sky_background/simulator.py` (3.6s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/advanced/subhalo/simulator.py` (3.8s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/multi_gaussian_expansion/simulator.py` (3.2s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/no_lens_light/simulator.py` (3.6s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/simulator.py` (3.6s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/data_preparation/start_here.py` (2.3s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/start_here.py` (34.3s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/advanced/operated_light_profile/modeling.py` (10.6s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/advanced/shapelets/fit.py` (4.5s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/advanced/shapelets/modeling.py` (28.6s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/advanced/sky_background/fit.py` (4.0s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/advanced/sky_background/modeling.py` (8.6s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/linear_light_profiles/fit.py` (3.6s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/linear_light_profiles/likelihood_function.py` (3.6s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/linear_light_profiles/modeling.py` (7.9s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/multi_gaussian_expansion/fit.py` (3.8s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/multi_gaussian_expansion/likelihood_function.py` (3.3s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/multi_gaussian_expansion/modeling.py` (8.0s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/multi_gaussian_expansion/slam.py` (7.9s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/multi_gaussian_expansion/source_science.py` (3.9s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/no_lens_light/modeling.py` (8.1s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/no_lens_light/slam.py` (8.7s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/pixelization/adaptive.py` (8.8s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/pixelization/cpu_fast_modeling.py` (10.7s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/features/pixelization/source_science.py` (3.8s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/fit.py` (4.1s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/likelihood_function.py` (3.5s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/modeling.py` (8.2s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/group/source_science.py` (2.9s)
