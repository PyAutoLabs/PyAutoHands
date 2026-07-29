# Test Report: autolens_test / scripts/interferometer (script)

**7 scripts** | 2 failed | 4 passed | 1 timeout

| Status | Count |
|--------|-------|
| failed | 2 |
| passed | 4 |
| timeout | 1 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/modeling_visualization_jit.py` — TIMEOUT (300.1s)

Timed out after 300s

### `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/nufft.py` — FAILED (14.8s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/nufft.py']' returned non-zero exit status 1.

```
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:173: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autolens_workspace_test matches the installed library version (2026.5.14.2): no `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:173: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autolens_workspace_test matches the installed library version (2026.5.14.2): no `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/nufft.py:352: UserWarning: Data has no positive values, and therefore cannot be log-scaled.
  axes[2].set_yscale("log")
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/nufft.py", line 493, in <module>
    distance < 5.0
AssertionError: Round-trip dirty-image peak too far from original peak: 5.00 px
```

### `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/visualization.py` — FAILED (11.7s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/visualization.py']' returned non-zero exit status 1.

```
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:173: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autolens_workspace_test matches the installed library version (2026.5.14.2): no `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/visualization.py", line 263, in <module>
    assert (image_path / "dataset.png").exists(), "dataset.png missing"
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: dataset.png missing
```

## Passed

- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/simulator/no_lens_light.py` (6.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/simulator/with_lens_light.py` (6.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/model_fit.py` (8.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/visualization_jax.py` (76.7s)
