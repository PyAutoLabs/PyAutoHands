# Test Report: autolens_test / scripts/jax_grad (script)

**7 scripts** | 1 failed | 3 passed | 3 skipped

| Status | Count |
|--------|-------|
| failed | 1 |
| passed | 3 |
| skipped | 3 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_grad/imaging_pixelization.py` — FAILED (10.5s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_grad/imaging_pixelization.py']' returned non-zero exit status 1.

```
    raise exc.ArrayException(
autoarray.exc.ArrayException: 
                The input array is a slim 1D array, but it does not have the same number of entries as pixels in
                the mask.

                This indicates that the number of unmaksed pixels in the mask  is different to the input slim array 
                shape.

                The shapes of the two arrays (which this exception is raised because they are different) are as follows:

                Input array_2d_slim.shape = 256
                Input mask_2d.pixels_in_mask = 441
                Input mask_2d.shape_native = (21, 21)
                
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_grad/imaging_pixelization.py", line 84, in <module>
    subprocess.run(
  File "/usr/lib/python3.12/subprocess.py", line 571, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/home/jammy/venv/PyAuto/bin/python3', 'scripts/jax_likelihood_functions/imaging/simulator.py']' returned non-zero exit status 1.
```

## Skipped

| Script | Reason |
|--------|--------|
| `imaging_lp.py` | NEEDS_FIX 2026-04-10 - JAX traceback in gradient computation for light profile |
| `imaging_mge.py` | NEEDS_FIX 2026-04-10 - AssertionError: Gradient is all zeros in MGE gradient computation |
| `interferometer.py` | SLOW 2026-07-14 - finite-difference JAX interferometer gradient; flakes at the 1800s cap (PyAutoHeart#74) |

## Passed

- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_grad/point_source.py` (40.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_grad/util.py` (0.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_grad/weak.py` (20.5s)
