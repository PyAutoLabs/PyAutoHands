# Test Report: autolens_test / scripts/jax_likelihood_functions (script)

**38 scripts** | 3 failed | 32 passed | 2 skipped | 1 timeout

| Status | Count |
|--------|-------|
| failed | 3 |
| passed | 32 |
| skipped | 2 |
| timeout | 1 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/datacube/delaunay.py` — FAILED (46.1s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/datacube/delaunay.py']' died with <Signals.SIGKILL: 9>.

```
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:173: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autolens_workspace_test matches the installed library version (2026.5.14.2): no `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
```

### `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_dspl.py` — FAILED (75.0s)

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

### `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/subhalo.py` — TIMEOUT (300.2s)

Timed out after 300s

### `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/delaunay.py` — FAILED (79.9s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/delaunay.py']' died with <Signals.SIGKILL: 9>.

```
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:173: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autolens_workspace_test matches the installed library version (2026.5.14.2): no `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
```

## Skipped

| Script | Reason |
|--------|--------|
| `delaunay_mge.py` | NEEDS_FIX 2026-04-10 - timeout in JAX likelihood function benchmark |
| `mge_group.py` | NEEDS_FIX 2026-04-10 - timeout in JAX likelihood function benchmark |

## Passed

- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/simulator.py` (11.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/simulator_dspl.py` (16.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/simulator.py` (17.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/simulator_dspl.py` (11.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/multi/simulator.py` (7.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/point_source/simulator.py` (4.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/datacube/rectangular.py` (34.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/delaunay.py` (45.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/lp.py` (19.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/mge.py` (49.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular.py` (85.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_mge.py` (241.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/delaunay_mge.py` (161.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/lp.py` (32.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/mge.py` (40.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/mge_group.py` (32.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular.py` (41.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular_dspl.py` (82.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular_mge.py` (85.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular_sparse.py` (49.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/light_multipole/multipole.py` (32.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/multi/dataset_model.py` (30.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/multi/delaunay.py` (39.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/multi/delaunay_mge.py` (52.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/multi/lp.py` (33.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/multi/mge.py` (36.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/multi/mge_group.py` (128.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/multi/rectangular.py` (41.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/multi/rectangular_mge.py` (51.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/point_source/image_plane.py` (60.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/point_source/point.py` (60.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/point_source/source_plane.py` (15.8s)
