# Test Report: autofit / scripts/features (script)

**6 scripts** | 1 failed | 4 passed | 1 skipped

| Status | Count |
|--------|-------|
| failed | 1 |
| passed | 4 |
| skipped | 1 |

## Failures

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autofit_workspace/scripts/features/graphical_models.py` — FAILED (6.7s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autofit_workspace/scripts/features/graphical_models.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autofit_workspace/scripts/features/graphical_models.py", line 95, in <module>
    data = af.util.numpy_array_from_json(file_path=path.join(dataset_path, "data.json"))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoFit/autofit/tools/util.py", line 130, in numpy_array_from_json
    with open(file_path, "r") as f:
         ^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'dataset/example_1d/gaussian_x1__low_snr/dataset_0/data.json'
```

## Skipped

| Script | Reason |
|--------|--------|
| `interpolate.py` | NEEDS_FIX 2026-04-10 - IndexError in InstanceInterpolator.__getitem__ when querying time == 1.5; value_map lookup falls through to empty instances list |

## Passed

- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autofit_workspace/scripts/features/model_comparison.py` (2.6s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autofit_workspace/scripts/features/search_chaining.py` (3.0s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autofit_workspace/scripts/features/search_grid_search.py` (4.4s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autofit_workspace/scripts/features/sensitivity_mapping.py` (3.6s)
