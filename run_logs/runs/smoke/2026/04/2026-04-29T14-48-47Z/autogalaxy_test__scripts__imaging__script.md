# Test Report: autogalaxy_test / scripts/imaging (script)

**4 scripts** | 1 failed | 3 passed

| Status | Count |
|--------|-------|
| failed | 1 |
| passed | 3 |

## Failures

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace_test/scripts/imaging/modeling_visualization_jit.py` — FAILED (4.6s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace_test/scripts/imaging/modeling_visualization_jit.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace_test/scripts/imaging/modeling_visualization_jit.py", line 128, in <module>
    assert isinstance(fit_1.log_likelihood, jnp.ndarray), (
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: expected jax.Array, got <class 'numpy.float64'>
```

## Passed

- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace_test/scripts/imaging/model_fit.py` (31.5s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace_test/scripts/imaging/visualization.py` (44.3s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace_test/scripts/imaging/visualization_jax.py` (10.5s)
