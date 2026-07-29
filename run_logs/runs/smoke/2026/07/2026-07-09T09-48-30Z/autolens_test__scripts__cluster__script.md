# Test Report: autolens_test / scripts/cluster (script)

**5 scripts** | 1 failed | 4 passed

| Status | Count |
|--------|-------|
| failed | 1 |
| passed | 4 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/visualization.py` — FAILED (4.7s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/visualization.py']' returned non-zero exit status 1.

```
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:206: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autolens_workspace_test is compatible with the installed library version (2026.7.6.649): no `version.minimum_library_version` or `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/visualization.py", line 171, in <module>
    assert_png("visualization_overlaid_positions.png")
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/visualization.py", line 141, in assert_png
    assert path.exists(), f"{filename} missing"
           ^^^^^^^^^^^^^
AssertionError: visualization_overlaid_positions.png missing
```

## Passed

- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/simulator.py` (6.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/csv_api.py` (4.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/lenstool_parity.py` (5.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/likelihood_sanity.py` (9.1s)
