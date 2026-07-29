# Test Report: autolens_test / scripts/multi (script)

**4 scripts** | 1 failed | 3 passed

| Status | Count |
|--------|-------|
| failed | 1 |
| passed | 3 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/multi/dataset_model_parity_delaunay.py` — FAILED (6.6s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/multi/dataset_model_parity_delaunay.py']' returned non-zero exit status 1.

```
/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/operators/convolver.py:1415: UserWarning: No blurring_image provided. Only the direct image will be convolved. This may change the correctness of the PSF convolution.
  warnings.warn(
/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/mask/mask_2d_util.py:564: UserWarning: Mask padded from (16, 16) to (np.int64(18), np.int64(18)) (parity preserved) to support kernel footprint (3, 3).
  warnings.warn(
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/multi/dataset_model_parity_delaunay.py", line 277, in <module>
    np.testing.assert_allclose(
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 1715, in assert_allclose
    assert_array_compare(compare, actual, desired, err_msg=str(err_msg),
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 921, in assert_array_compare
    raise AssertionError(msg)
AssertionError: 
Not equal to tolerance rtol=1e-07, atol=0.2
Delaunay A0 != A1: profile-baked fits to two datasets of the same physical scene disagree by more than the pixel-sampling floor.
Mismatched elements: 1 / 1 (100%)
Max absolute difference among violations: 91.98521689
Max relative difference among violations: 0.32450508
 ACTUAL: array(-191.477885)
 DESIRED: array(-283.463101)
```

## Passed

- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/multi/dataset_model_parity_lp_linear.py` (5.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/multi/visualization_imaging.py` (38.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/multi/visualization_interferometer.py` (4.7s)
