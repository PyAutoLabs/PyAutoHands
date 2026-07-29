# Test Report: autolens_test / scripts/imaging (script)

**11 scripts** | 1 failed | 7 passed | 3 skipped

| Status | Count |
|--------|-------|
| failed | 1 |
| passed | 7 |
| skipped | 3 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/model_fit.py` — FAILED (8.6s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/model_fit.py']' returned non-zero exit status 1.

```
/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/mask/mask_2d_util.py:564: UserWarning: Mask padded from (16, 16) to (np.int64(26), np.int64(26)) (parity preserved) to support kernel footprint (11, 11).
  warnings.warn(
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/model_fit.py", line 256, in <module>
    aplt.corner_cornerpy(samples=result.samples)
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/plot/plot_util.py", line 18, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/plot/samples_plotters.py", line 35, in corner_cornerpy
    data = np.asarray(samples.parameter_lists)
                      ^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'parameter_lists'
```

## Skipped

| Script | Reason |
|--------|--------|
| `modeling_visualization_jit.py` | SLOW 2026-05-07 - JIT + full visualization pipeline exceeds 300s cap (autogalaxy variant ~90s); unblocked by PR #70 from prior `expected jax.Array, got numpy.float64` AssertionError, now hits perf wall |
| `modeling_visualization_jit_delaunay.py` | SLOW 2026-05-07 - JIT + full visualization pipeline exceeds 300s cap (autogalaxy variant ~90s); unblocked by PR #70 from prior `expected jax.Array, got numpy.float64` AssertionError, now hits perf wall |
| `modeling_visualization_jit_rectangular.py` | SLOW 2026-05-07 - JIT + full visualization pipeline exceeds 300s cap (autogalaxy variant ~90s); unblocked by PR #70 from prior `expected jax.Array, got numpy.float64` AssertionError, now hits perf wall |

## Passed

- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/simulator/no_lens_light.py` (5.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/simulator/with_lens_light.py` (4.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/simulator_use_jax_parity.py` (12.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/convolution.py` (8.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/convolution_over_sampled.py` (7.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/visualization.py` (28.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/visualization_jax.py` (86.5s)
