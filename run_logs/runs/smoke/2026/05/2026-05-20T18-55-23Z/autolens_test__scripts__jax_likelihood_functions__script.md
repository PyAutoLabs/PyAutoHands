# Test Report: autolens_test / scripts/jax_likelihood_functions (script)

**38 scripts** | 1 failed | 35 passed | 2 skipped

| Status | Count |
|--------|-------|
| failed | 1 |
| passed | 35 |
| skipped | 2 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_dspl.py` — FAILED (31.6s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_dspl.py']' returned non-zero exit status 1.

```

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_dspl.py", line 275, in <module>
    np.testing.assert_allclose(
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 1715, in assert_allclose
    assert_array_compare(compare, actual, desired, err_msg=str(err_msg),
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 921, in assert_array_compare
    raise AssertionError(msg)
AssertionError: 
Not equal to tolerance rtol=0.0001, atol=0
rectangular_dspl: JAX vmap likelihood mismatch
Mismatched elements: 1 / 1 (100%)
Max absolute difference among violations: 101.99460561
Max relative difference among violations: 0.02685672
 ACTUAL: array([-3695.737222])
 DESIRED: array(-3797.731828)
```

## Skipped

| Script | Reason |
|--------|--------|
| `delaunay_mge.py` | NEEDS_FIX 2026-04-10 - timeout in JAX likelihood function benchmark |
| `mge_group.py` | NEEDS_FIX 2026-04-10 - timeout in JAX likelihood function benchmark |

## Passed

- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/simulator.py` (8.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/simulator_dspl.py` (8.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/simulator.py` (8.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/simulator_dspl.py` (9.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/multi/simulator.py` (6.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/point_source/simulator.py` (3.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/datacube/delaunay.py` (163.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/datacube/rectangular.py` (27.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/delaunay.py` (37.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/lp.py` (16.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/mge.py` (36.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular.py` (37.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_mge.py` (63.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/subhalo.py` (90.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/delaunay.py` (33.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/delaunay_mge.py` (56.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/lp.py` (16.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/mge.py` (20.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/mge_group.py` (16.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular.py` (19.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular_dspl.py` (37.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular_mge.py` (40.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular_sparse.py` (22.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/light_multipole/multipole.py` (15.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/multi/dataset_model.py` (14.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/multi/delaunay.py` (19.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/multi/delaunay_mge.py` (24.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/multi/lp.py` (14.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/multi/mge.py` (17.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/multi/mge_group.py` (65.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/multi/rectangular.py` (22.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/multi/rectangular_mge.py` (29.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/point_source/image_plane.py` (34.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/point_source/point.py` (33.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/point_source/source_plane.py` (5.9s)
