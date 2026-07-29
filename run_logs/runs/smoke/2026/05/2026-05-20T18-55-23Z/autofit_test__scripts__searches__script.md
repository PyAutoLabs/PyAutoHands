# Test Report: autofit_test / scripts/searches (script)

**9 scripts** | 1 failed | 8 passed

| Status | Count |
|--------|-------|
| failed | 1 |
| passed | 8 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/searches/BlackJAXNUTS.py` — FAILED (3.2s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/searches/BlackJAXNUTS.py']' returned non-zero exit status 1.

```
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:173: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autofit_workspace_test matches the installed library version (2026.5.14.2): no `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/searches/BlackJAXNUTS.py", line 120, in <module>
    abs(mp.normalization - 25.0) < 5.0
AssertionError: normalization off by too much: 1.0
```

## Passed

- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/searches/DynestyDynamic.py` (3.5s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/searches/DynestyStatic.py` (3.6s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/searches/Dynesty_jax.py` (5.3s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/searches/Emcee.py` (4.5s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/searches/LBFGS.py` (4.3s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/searches/Nautilus.py` (3.5s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/searches/Nautilus_jax.py` (2.9s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/searches/Zeus.py` (3.2s)
