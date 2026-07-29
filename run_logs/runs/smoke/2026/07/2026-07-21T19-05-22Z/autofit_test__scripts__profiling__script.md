# Test Report: autofit_test / scripts/profiling (script)

**3 scripts** | 1 failed | 2 passed

| Status | Count |
|--------|-------|
| failed | 1 |
| passed | 2 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/profiling/aggregator/profile_database.py` — FAILED (5.4s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/profiling/aggregator/profile_database.py']' returned non-zero exit status 1.

```
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/sqlalchemy/orm/state.py", line 571, in _initialize_instance
    with util.safe_reraise():
         ^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/sqlalchemy/util/langhelpers.py", line 146, in __exit__
    raise exc_value.with_traceback(exc_tb)
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/sqlalchemy/orm/state.py", line 569, in _initialize_instance
    manager.original_init(*mixed[1:], **kwargs)
  File "<string>", line 6, in __init__
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/database/model/array.py", line 16, in __init__
    super().__init__(**kwargs)
  File "<string>", line 6, in __init__
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/sqlalchemy/orm/decl_base.py", line 2170, in _declarative_constructor
    setattr(self, k, kwargs[k])
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/database/model/array.py", line 188, in hdu
    self.array = hdu.data
    ^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/database/model/array.py", line 56, in array
    self._dtype = get_class_path(getattr(np, array.dtype.name))
                                             ^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'dtype'
```

## Passed

- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/profiling/aggregator/mock_results.py` (4.7s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/profiling/aggregator/profile_aggregator.py` (2.7s)
