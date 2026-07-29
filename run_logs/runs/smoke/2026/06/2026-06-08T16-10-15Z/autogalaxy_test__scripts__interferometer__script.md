# Test Report: autogalaxy_test / scripts/interferometer (script)

**3 scripts** | 1 failed | 2 passed

| Status | Count |
|--------|-------|
| failed | 1 |
| passed | 2 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/interferometer/modeling_visualization_jit.py` — FAILED (38.4s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/interferometer/modeling_visualization_jit.py']' returned non-zero exit status 1.

```
    return func(self, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/abstract_search.py", line 685, in start_resume_fit
    samples = self.perform_update(
              ^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/abstract_search.py", line 1006, in perform_update
    return self._updater.update(
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/updater.py", line 93, in update
    latent_samples = self._compute_latent_samples(
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/updater.py", line 268, in _compute_latent_samples
    latent_samples = analysis.compute_latent_samples(
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/analysis/analysis.py", line 259, in compute_latent_samples
    latent_values_batch = jnp.stack(latent_values_batch, axis=-1)  # (batch, n_latents)
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/jax/_src/numpy/lax_numpy.py", line 4451, in stack
    raise ValueError("Need at least one array to stack.")
ValueError: Need at least one array to stack.
```

## Passed

- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/interferometer/visualization.py` (8.2s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/interferometer/visualization_jax.py` (13.5s)
