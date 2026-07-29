# Test Report: autolens_test / scripts/multi (script)

**4 scripts** | 1 failed | 3 passed

| Status | Count |
|--------|-------|
| failed | 1 |
| passed | 3 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/multi/dataset_model_parity_delaunay.py` — FAILED (16.3s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/multi/dataset_model_parity_delaunay.py']' returned non-zero exit status 1.

```
  warnings.warn(_missing_version_warning(root, library_version))
/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/operators/convolver.py:951: UserWarning: No blurring_image provided. Only the direct image will be convolved. This may change the correctness of the PSF convolution.
  warnings.warn(
/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/mask/mask_2d_util.py:564: UserWarning: Mask padded from (15, 15) to (np.int64(17), np.int64(17)) (parity preserved) to support kernel footprint (3, 3).
  warnings.warn(
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/multi/dataset_model_parity_delaunay.py", line 294, in <module>
    np.testing.assert_allclose(
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 1715, in assert_allclose
    assert_array_compare(compare, actual, desired, err_msg=str(err_msg),
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 921, in assert_array_compare
    raise AssertionError(msg)
AssertionError: 
Not equal to tolerance rtol=1e-07, atol=0.005
Delaunay A1 != B1: DatasetModel rotation+shift fit differs from profile-baked fit (THIS IS THE BUG THE FIX TARGETS).
Mismatched elements: 1 / 1 (100%)
Max absolute difference among violations: 0.00706624
Max relative difference among violations: 3.41283736e-05
 ACTUAL: array(-207.055781)
 DESIRED: array(-207.048715)
```

## Passed

- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/multi/dataset_model_parity_lp_linear.py` (13.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/multi/visualization_imaging.py` (79.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/multi/visualization_interferometer.py` (12.3s)
