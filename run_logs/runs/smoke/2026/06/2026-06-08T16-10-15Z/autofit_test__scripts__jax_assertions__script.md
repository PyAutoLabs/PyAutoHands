# Test Report: autofit_test / scripts/jax_assertions (script)

**6 scripts** | 1 failed | 5 passed

| Status | Count |
|--------|-------|
| failed | 1 |
| passed | 5 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/jax_assertions/fitness_dispatch.py` — FAILED (2.0s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/jax_assertions/fitness_dispatch.py']' returned non-zero exit status 1.

```
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:173: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autofit_workspace_test matches the installed library version (2026.5.29.4): no `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/jax_assertions/fitness_dispatch.py", line 159, in <module>
    assert_fit_for_visualization_dispatches_through_jit_when_flag_set()
  File "/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/jax_assertions/fitness_dispatch.py", line 85, in assert_fit_for_visualization_dispatches_through_jit_when_flag_set
    assert analysis._jitted_fit_from is not None
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/analysis/analysis.py", line 112, in __getattr__
    raise AttributeError(f"Analysis has no attribute {item}")
AttributeError: Analysis has no attribute _jitted_fit_from
```

## Passed

- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/jax_assertions/enable_pytrees.py` (2.3s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/jax_assertions/nested.py` (1.9s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/jax_assertions/priors_xp_dispatch.py` (4.4s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/jax_assertions/pytrees.py` (3.4s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/jax_assertions/shared_state.py` (3.2s)
