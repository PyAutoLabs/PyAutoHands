# Test Report: autofit_test / scripts/database (script)

**8 scripts** | 1 failed | 5 passed | 2 skipped

| Status | Count |
|--------|-------|
| failed | 1 |
| passed | 5 |
| skipped | 2 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/database/scrape/sensitivity.py` — FAILED (2.2s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/database/scrape/sensitivity.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/database/scrape/sensitivity.py", line 502, in <module>
    sensitivity_result = sensitivity.run()
                         ^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/grid/sensitivity/__init__.py", line 171, in run
    for result in process_class.run_jobs(
                  ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/grid/grid_search/__init__.py", line 22, in run_jobs
    yield job_.perform()
          ^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/grid/sensitivity/job.py", line 167, in perform
    result = self.base_fit_cls(
             ^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/database/scrape/sensitivity.py", line 390, in __call__
    analysis = self.analysis_cls(dataset=dataset)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/database/scrape/sensitivity.py", line 241, in __init__
    super().__init__(data=dataset.data, noise_map=dataset.noise_map)
                          ^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'data'
```

## Skipped

| Script | Reason |
|--------|--------|
| `general.py` | Session mostly works but not maintaining currently. |
| `multi_analysis.py` | Session mostly works but not maintaining currently. |

## Passed

- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/database/directory/general.py` (2.2s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/database/directory/multi_analysis.py` (1.8s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/database/scrape/general.py` (1.8s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/database/scrape/grid_search.py` (2.7s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/database/scrape/multi_analysis.py` (1.8s)
