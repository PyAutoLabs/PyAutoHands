# Test Report: autofit_test / scripts/features (script)

**5 scripts** | 1 failed | 4 passed

| Status | Count |
|--------|-------|
| failed | 1 |
| passed | 4 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/features/latent_nan_robustness.py` — FAILED (3.5s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/features/latent_nan_robustness.py']' returned non-zero exit status 1.

```
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:173: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autofit_workspace_test matches the installed library version (2026.5.29.4): no `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/features/latent_nan_robustness.py", line 94, in <module>
    assert len(result.samples.sample_list) > LATENT_BATCH_SIZE, (
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Need >3 samples for a multi-batch latent run; got 2.
```

## Passed

- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/features/assertion.py` (4.5s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/features/grid_search_parallel.py` (4.6s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/features/latent.py` (2.9s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/features/minimal_output.py` (2.9s)
