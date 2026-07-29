# Test Report: autolens_test / scripts/jax_likelihood_functions (script)

**33 scripts** | 9 failed | 22 passed | 2 skipped

| Status | Count |
|--------|-------|
| failed | 9 |
| passed | 22 |
| skipped | 2 |

## Failures

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/delaunay.py` — FAILED (16.4s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/delaunay.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/delaunay.py", line 290, in <module>
    np.testing.assert_allclose(
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 1715, in assert_allclose
    assert_array_compare(compare, actual, desired, err_msg=str(err_msg),
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 921, in assert_array_compare
    raise AssertionError(msg)
AssertionError: 
Not equal to tolerance rtol=0.0001, atol=0
delaunay: JAX vmap likelihood mismatch
Mismatched elements: 3 / 3 (100%)
Max absolute difference among violations: 1456.97072316
Max relative difference among violations: 0.06157208
 ACTUAL: array([-22205.878181, -22205.878181, -22205.878181])
 DESIRED: array(-23662.848904)
```

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular.py` — FAILED (14.2s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular.py", line 260, in <module>
    np.testing.assert_allclose(
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 1715, in assert_allclose
    assert_array_compare(compare, actual, desired, err_msg=str(err_msg),
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 921, in assert_array_compare
    raise AssertionError(msg)
AssertionError: 
Not equal to tolerance rtol=0.0001, atol=0
rectangular: JAX vmap likelihood mismatch
Mismatched elements: 3 / 3 (100%)
Max absolute difference among violations: 1059.94076761
Max relative difference among violations: 0.00162909
 ACTUAL: array([-651692.997799, -651692.997799, -651692.997799])
 DESIRED: array(-650633.057031)
```

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_dspl.py` — FAILED (39.3s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_dspl.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_dspl.py", line 275, in <module>
    np.testing.assert_allclose(
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 1715, in assert_allclose
    assert_array_compare(compare, actual, desired, err_msg=str(err_msg),
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 921, in assert_array_compare
    raise AssertionError(msg)
AssertionError: 
Not equal to tolerance rtol=0.0001, atol=0
rectangular_dspl: JAX vmap likelihood mismatch
Mismatched elements: 1 / 1 (100%)
Max absolute difference among violations: 35.12946094
Max relative difference among violations: 0.03095257
 ACTUAL: array([1170.074391])
 DESIRED: array(1134.94493)
```

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_mge.py` — FAILED (56.1s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_mge.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_mge.py", line 298, in <module>
    np.testing.assert_allclose(
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 1715, in assert_allclose
    assert_array_compare(compare, actual, desired, err_msg=str(err_msg),
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 921, in assert_array_compare
    raise AssertionError(msg)
AssertionError: 
Not equal to tolerance rtol=0.0001, atol=0
rectangular_mge: JAX vmap likelihood mismatch
Mismatched elements: 6 / 6 (100%)
Max absolute difference among violations: 28.41880723
Max relative difference among violations: 0.25517883
 ACTUAL: array([-82.949395, -82.949395, -82.949395, -82.949395, -82.949395,
       -82.949395])
 DESIRED: array(-111.368202)
```

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/multi/delaunay.py` — FAILED (16.9s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/multi/delaunay.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/multi/delaunay.py", line 207, in <module>
    np.testing.assert_allclose(
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 1715, in assert_allclose
    assert_array_compare(compare, actual, desired, err_msg=str(err_msg),
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 921, in assert_array_compare
    raise AssertionError(msg)
AssertionError: 
Not equal to tolerance rtol=0.0001, atol=0
multi/delaunay: JAX vmap likelihood mismatch
Mismatched elements: 3 / 3 (100%)
Max absolute difference among violations: 2500.39460237
Max relative difference among violations: 0.39359731
 ACTUAL: array([-8853.066593, -8853.066593, -8853.066593])
 DESIRED: array(-6352.671991)
```

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/multi/delaunay_mge.py` — FAILED (19.6s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/multi/delaunay_mge.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/multi/delaunay_mge.py", line 205, in <module>
    np.testing.assert_allclose(
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 1715, in assert_allclose
    assert_array_compare(compare, actual, desired, err_msg=str(err_msg),
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 921, in assert_array_compare
    raise AssertionError(msg)
AssertionError: 
Not equal to tolerance rtol=0.0001, atol=0
multi/delaunay_mge: JAX vmap likelihood mismatch
Mismatched elements: 3 / 3 (100%)
Max absolute difference among violations: 420.92603587
Max relative difference among violations: 3.38562991
 ACTUAL: array([-545.25328, -545.25328, -545.25328])
 DESIRED: array(-124.327244)
```

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/multi/mge.py` — FAILED (19.1s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/multi/mge.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/multi/mge.py", line 154, in <module>
    np.testing.assert_allclose(
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 1715, in assert_allclose
    assert_array_compare(compare, actual, desired, err_msg=str(err_msg),
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 921, in assert_array_compare
    raise AssertionError(msg)
AssertionError: 
Not equal to tolerance rtol=0.0001, atol=0
multi/mge: JAX vmap likelihood mismatch
Mismatched elements: 3 / 3 (100%)
Max absolute difference among violations: 1114.52822173
Max relative difference among violations: 0.00051258
 ACTUAL: array([-2173221.436859, -2173221.436859, -2173221.436859])
 DESIRED: array(-2174335.96508)
```

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/multi/rectangular.py` — FAILED (19.2s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/multi/rectangular.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/multi/rectangular.py", line 203, in <module>
    np.testing.assert_allclose(
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 1715, in assert_allclose
    assert_array_compare(compare, actual, desired, err_msg=str(err_msg),
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 921, in assert_array_compare
    raise AssertionError(msg)
AssertionError: 
Not equal to tolerance rtol=0.0001, atol=0
multi/rectangular: JAX vmap likelihood mismatch
Mismatched elements: 3 / 3 (100%)
Max absolute difference among violations: 258.50636197
Max relative difference among violations: 0.02040271
 ACTUAL: array([-12928.700871, -12928.700871, -12928.700871])
 DESIRED: array(-12670.194509)
```

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/multi/rectangular_mge.py` — FAILED (24.8s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/multi/rectangular_mge.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/multi/rectangular_mge.py", line 188, in <module>
    np.testing.assert_allclose(
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 1715, in assert_allclose
    assert_array_compare(compare, actual, desired, err_msg=str(err_msg),
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 921, in assert_array_compare
    raise AssertionError(msg)
AssertionError: 
Not equal to tolerance rtol=0.0001, atol=0
multi/rectangular_mge: JAX vmap likelihood mismatch
Mismatched elements: 3 / 3 (100%)
Max absolute difference among violations: 52.77866625
Max relative difference among violations: 0.00866102
 ACTUAL: array([-6146.592113, -6146.592113, -6146.592113])
 DESIRED: array(-6093.813447)
```

## Skipped

| Script | Reason |
|--------|--------|
| `delaunay_mge.py` | NEEDS_FIX 2026-04-10 - timeout in JAX likelihood function benchmark |
| `mge_group.py` | NEEDS_FIX 2026-04-10 - timeout in JAX likelihood function benchmark |

## Passed

- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/simulator.py` (15.3s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/simulator_dspl.py` (12.8s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/simulator.py` (12.5s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/simulator_dspl.py` (12.8s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/multi/simulator.py` (10.2s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/point_source/simulator.py` (2.9s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/lp.py` (20.3s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/mge.py` (37.4s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/delaunay.py` (46.8s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/delaunay_mge.py` (48.8s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/lp.py` (14.2s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/mge.py` (18.0s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/mge_group.py` (23.3s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular.py` (17.7s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular_dspl.py` (40.7s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular_mge.py` (35.6s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular_sparse.py` (22.3s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/multi/lp.py` (14.1s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/multi/mge_group.py` (73.5s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/point_source/image_plane.py` (40.7s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/point_source/point.py` (39.5s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/jax_likelihood_functions/point_source/source_plane.py` (6.7s)
