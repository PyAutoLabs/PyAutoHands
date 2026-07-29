# Test Report: autogalaxy_test / scripts/jax_assertions (script)

**2 scripts** | 1 failed | 1 passed

| Status | Count |
|--------|-------|
| failed | 1 |
| passed | 1 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_assertions/convolver_mixed_precision.py` — FAILED (2.5s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_assertions/convolver_mixed_precision.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_assertions/convolver_mixed_precision.py", line 46, in <module>
    masked_image = aa.Array2D(values=image_values, mask=mask)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/structures/arrays/uniform_2d.py", line 243, in __init__
    values = array_2d_util.convert_array_2d(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/structures/arrays/array_2d_util.py", line 133, in convert_array_2d
    check_array_2d_and_mask_2d(array_2d=array_2d, mask_2d=mask_2d)
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/structures/arrays/array_2d_util.py", line 87, in check_array_2d_and_mask_2d
    raise exc.ArrayException(
autoarray.exc.ArrayException: 
                The input array is 2D but not the same dimensions as the mask.

                This indicates the mask's shape is different to the input array shape.

                The shapes of the two arrays (which this exception is raised because they are different) are as follows:

                Input array_2d shape = (80, 80)
                Input mask_2d shape_native = (15, 15)
```

## Passed

- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_assertions/hessian_parity.py` (8.8s)
