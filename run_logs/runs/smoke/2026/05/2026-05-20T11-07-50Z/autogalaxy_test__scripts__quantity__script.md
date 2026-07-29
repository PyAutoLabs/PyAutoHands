# Test Report: autogalaxy_test / scripts/quantity (script)

**2 scripts** | 1 failed | 1 passed

| Status | Count |
|--------|-------|
| failed | 1 |
| passed | 1 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/quantity/visualization.py` — FAILED (27.1s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/quantity/visualization.py']' returned non-zero exit status 1.

```
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:173: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test matches the installed library version (2026.5.14.2): no `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/quantity/visualization.py", line 107, in <module>
    assert (image_path / "fit.png").exists(), "fit.png was not produced"
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: fit.png was not produced
```

## Passed

- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/quantity/visualization_jax.py` (19.1s)
