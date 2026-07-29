# Test Report: autolens / scripts/interferometer (script)

**40 scripts** | 2 failed | 37 passed | 1 skipped

| Status | Count |
|--------|-------|
| failed | 2 |
| passed | 37 |
| skipped | 1 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/potential_correction/start_here.py` — FAILED (12.9s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/potential_correction/start_here.py']' returned non-zero exit status 1.

```
  File "/home/jammy/Code/PyAutoLabs/PyAutoLens/autolens/potential_correction/fit_interferometer.py", line 274, in dpsi_response_matrix
    -1.0 * self.source_gradient_matrix @ self.dpsi_gradient_matrix
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoLens/autolens/potential_correction/fit_interferometer.py", line 246, in source_gradient_matrix
    traced = np.asarray(self.source_plane_data_grid)[self._dpsi_rows_in_full]
                                                     ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoLens/autolens/potential_correction/fit_interferometer.py", line 239, in _dpsi_rows_in_full
    self.pair_dpsi_data_obj.mask_data,
    ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoLens/autolens/potential_correction/fit_interferometer.py", line 221, in pair_dpsi_data_obj
    self._pair_dpsi_data_obj = self.dpsi_pixelization.pair_dpsi_data_mesh(
                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoLens/autolens/potential_correction/pixelization.py", line 90, in pair_dpsi_data_mesh
    return dpsi_mesh.PairRegularDpsiMesh(mask, pixel_scale, self.mesh.factor)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoLens/autolens/potential_correction/mesh.py", line 99, in __init__
    self.get_itp_box_ctr()
  File "/home/jammy/Code/PyAutoLabs/PyAutoLens/autolens/potential_correction/mesh.py", line 132, in get_itp_box_ctr
    raise ValueError(
ValueError: The dpsi grid is too sparse. Try decreasing the dpsi_factor to smaller values.
```

### `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/potential_correction/likelihood_function.py` — FAILED (7.8s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/potential_correction/likelihood_function.py']' returned non-zero exit status 1.

```
  As in the imaging walkthrough, a correction $\delta\psi$ perturbs the observed image via the source's brightness
/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/potential_correction/likelihood_function.py:242: SyntaxWarning: invalid escape sequence '\,'
  The joint real-space response stacks the two blocks, $A = [\, f \; | \; G \,]$, alongside the block-diagonal
/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/potential_correction/likelihood_function.py:293: SyntaxWarning: invalid escape sequence '\,'
  - the curvature is $F = A^T \, (T^H C^{-1} T) \, A$, where the operator $T^H C^{-1} T$ is a **convolution** in
/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/potential_correction/likelihood_function.py:317: SyntaxWarning: invalid escape sequence '\,'
  $(F + R) \, x = D$
/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/potential_correction/likelihood_function.py:330: SyntaxWarning: invalid escape sequence '\d'
  $\delta\kappa = \frac{1}{2}\nabla^2 \delta\psi$, via the mesh Laplacian. A dark subhalo missing from the smooth
/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/potential_correction/likelihood_function.py:357: SyntaxWarning: invalid escape sequence '\c'
  visibility-space specifics that the noise normalization and $\chi^2$ run over the real **and** imaginary parts:
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/potential_correction/likelihood_function.py", line 196, in <module>
    pair = al.pc.PairRegularDpsiMesh(dpsi_mask, pixel_scale=0.1, dpsi_factor=2)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoLens/autolens/potential_correction/mesh.py", line 99, in __init__
    self.get_itp_box_ctr()
  File "/home/jammy/Code/PyAutoLabs/PyAutoLens/autolens/potential_correction/mesh.py", line 132, in get_itp_box_ctr
    raise ValueError(
ValueError: The dpsi grid is too sparse. Try decreasing the dpsi_factor to smaller values.
```

## Skipped

| Script | Reason |
|--------|--------|
| `casa_reduction.py` | Requires CASA MeasurementSet output, not runnable standalone |

## Passed

- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/datacube/simulator.py` (8.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/extra_galaxies/simulator.py` (6.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/subhalo/simulator.py` (6.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/simulator.py` (10.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/datacube/start_here.py` (11.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/subhalo/detect/start_here.py` (12.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/subhalo/sensitivity/start_here.py` (0.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/start_here.py` (146.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/data_preparation.py` (11.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/advanced/shapelets/fit.py` (8.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/advanced/shapelets/modeling.py` (17.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/datacube/data_preparation.py` (4.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/datacube/delaunay.py` (7.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/datacube/likelihood_function.py` (10.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/datacube/modeling.py` (7.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/datacube/modeling_parametric.py` (6.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/extra_galaxies/modeling.py` (8.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/extra_galaxies/slam.py` (8.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/linear_light_profiles/fit.py` (7.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/linear_light_profiles/likelihood_function.py` (8.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/linear_light_profiles/modeling.py` (10.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/linear_light_profiles/slam.py` (10.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/multi_gaussian_expansion/fit.py` (10.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/multi_gaussian_expansion/likelihood_function.py` (9.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/multi_gaussian_expansion/modeling.py` (10.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/multi_gaussian_expansion/slam.py` (10.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/pixelization/delaunay.py` (20.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/pixelization/fit.py` (12.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/pixelization/likelihood_function.py` (14.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/pixelization/many_visibilities_preparation.py` (9.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/pixelization/modeling.py` (12.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/pixelization/slam.py` (9.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/features/pixelization/source_science.py` (11.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/fit.py` (9.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/likelihood_function.py` (9.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/modeling.py` (20.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/interferometer/source_science.py` (7.4s)
