# Test Report: autolens_test / scripts/cluster (script)

**4 scripts** | 2 failed | 2 passed

| Status | Count |
|--------|-------|
| failed | 2 |
| passed | 2 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/simulator.py` — FAILED (6.2s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/simulator.py']' returned non-zero exit status 1.

```
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:173: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autolens_workspace_test matches the installed library version (2026.5.14.2): no `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/simulator.py", line 48, in <module>
    mass_table = al.galaxy_models_from_csv(dataset_path / "mass.csv", family="mass")
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoGalaxy/autogalaxy/galaxy/galaxy_model_csv.py", line 232, in galaxy_models_from_csv
    raw_rows = csvable.list_from_csv(file_path)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/csvable.py", line 103, in list_from_csv
    with open(file_path, newline="") as f:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'dataset/cluster/test/mass.csv'
```

### `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/visualization.py` — FAILED (5.8s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/visualization.py']' returned non-zero exit status 1.

```
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:173: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autolens_workspace_test matches the installed library version (2026.5.14.2): no `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/visualization.py", line 467, in <module>
    len(tangential_curves) > 0
AssertionError: no tangential critical curves recovered (expected at least one for a 10^15.3 M_sun host)
```

## Passed

- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/csv_api.py` (5.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/likelihood_sanity.py` (22.8s)
