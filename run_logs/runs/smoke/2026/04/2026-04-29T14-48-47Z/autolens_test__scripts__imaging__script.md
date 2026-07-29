# Test Report: autolens_test / scripts/imaging (script)

**9 scripts** | 4 failed | 3 passed | 2 skipped

| Status | Count |
|--------|-------|
| failed | 4 |
| passed | 3 |
| skipped | 2 |

## Failures

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/imaging/convolution.py` — FAILED (5.0s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/imaging/convolution.py']' returned non-zero exit status 1.

```
    res = fig.savefig(*args, **kwargs)  # type: ignore[func-returns-value]
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/matplotlib/figure.py", line 3395, in savefig
    self.canvas.print_figure(fname, **kwargs)
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/matplotlib/backend_bases.py", line 2204, in print_figure
    result = print_method(
             ^^^^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/matplotlib/backend_bases.py", line 2054, in <lambda>
    print_method = functools.wraps(meth)(lambda *args, **kwargs: meth(
                                                                 ^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/matplotlib/backends/backend_agg.py", line 496, in print_png
    self._print_pil(filename_or_obj, "png", pil_kwargs, metadata)
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/matplotlib/backends/backend_agg.py", line 445, in _print_pil
    mpl.image.imsave(
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/matplotlib/image.py", line 1676, in imsave
    image.save(fname, **pil_kwargs)
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/PIL/Image.py", line 2576, in save
    fp = builtins.open(filename, "w+b")
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'scripts/imaging/images/residuals.png'
```

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/imaging/modeling_visualization_jit.py` — FAILED (17.2s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/imaging/modeling_visualization_jit.py']' returned non-zero exit status 1.

```
/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/operators/convolver.py:925: UserWarning: No blurring_image provided. Only the direct image will be convolved. This may change the correctness of the PSF convolution.
  warnings.warn(
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/imaging/modeling_visualization_jit.py", line 149, in <module>
    assert isinstance(fit_1.log_likelihood, jnp.ndarray), (
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: expected jax.Array, got <class 'numpy.float64'>
```

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/imaging/modeling_visualization_jit_delaunay.py` — FAILED (9.1s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/imaging/modeling_visualization_jit_delaunay.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/imaging/modeling_visualization_jit_delaunay.py", line 191, in <module>
    assert isinstance(fit_1.log_likelihood, jnp.ndarray), (
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: expected jax.Array, got <class 'numpy.float64'>
```

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/imaging/modeling_visualization_jit_rectangular.py` — FAILED (9.3s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/imaging/modeling_visualization_jit_rectangular.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/imaging/modeling_visualization_jit_rectangular.py", line 175, in <module>
    assert isinstance(fit_1.log_likelihood, jnp.ndarray), (
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: expected jax.Array, got <class 'numpy.float64'>
```

## Skipped

| Script | Reason |
|--------|--------|
| `visualization.py` | NEEDS_FIX 2026-04-10 - AssertionError: dataset.png missing after visualization refactor |
| `visualization_jax.py` | NEEDS_FIX 2026-04-10 - AssertionError: dataset.png missing after visualization refactor |

## Passed

- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/imaging/simulator/no_lens_light.py` (5.2s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/imaging/simulator/with_lens_light.py` (3.4s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/imaging/model_fit.py` (130.1s)
