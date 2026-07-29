# Test Report: autolens_test / scripts/cluster (script)

**4 scripts** | 1 failed | 3 passed

| Status | Count |
|--------|-------|
| failed | 1 |
| passed | 3 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/simulator.py` — FAILED (5.6s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/simulator.py']' returned non-zero exit status 1.

```
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:173: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autolens_workspace_test matches the installed library version (2026.5.29.4): no `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:173: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autolens_workspace_test matches the installed library version (2026.5.29.4): no `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/simulator.py", line 197, in <module>
    raw = np.asarray(jitted_solve(tracer, coord))
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <function jitted_solve at 0x7fb8297c59e0> as an abstract array. The problematic value is of type <class 'autogalaxy.galaxy.galaxy.Galaxy'> and was passed to the function at path tracer[0][0].
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
```

## Passed

- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/csv_api.py` (3.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/likelihood_sanity.py` (6.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/visualization.py` (24.3s)
