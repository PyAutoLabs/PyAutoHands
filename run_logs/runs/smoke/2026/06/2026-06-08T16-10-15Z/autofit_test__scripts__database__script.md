# Test Report: autofit_test / scripts/database (script)

**8 scripts** | 2 failed | 4 passed | 2 skipped

| Status | Count |
|--------|-------|
| failed | 2 |
| passed | 4 |
| skipped | 2 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/database/scrape/grid_search.py` — FAILED (5.8s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/database/scrape/grid_search.py']' returned non-zero exit status 1.

```
    return connection._execute_clauseelement(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/sqlalchemy/engine/base.py", line 1640, in _execute_clauseelement
    ret = self._execute_context(
          ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/sqlalchemy/engine/base.py", line 1846, in _execute_context
    return self._exec_single_context(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/sqlalchemy/engine/base.py", line 1986, in _exec_single_context
    self._handle_dbapi_exception(
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/sqlalchemy/engine/base.py", line 2355, in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/sqlalchemy/engine/base.py", line 1967, in _exec_single_context
    self.dialect.do_execute(
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/sqlalchemy/engine/default.py", line 941, in do_execute
    cursor.execute(statement, parameters)
sqlalchemy.exc.IntegrityError: (sqlite3.IntegrityError) UNIQUE constraint failed: fit.id
[SQL: INSERT INTO fit (id, is_complete, max_log_likelihood, parent_id, is_grid_search, unique_tag, name, path_prefix, model_id, instance_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)]
[parameters: ('gaussian_x1', 1, None, None, 1, 'gaussian_x1', None, None, None, None)]
(Background on this error at: https://sqlalche.me/e/20/gkpj)
```

### `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/database/scrape/sensitivity.py` — FAILED (4.6s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/database/scrape/sensitivity.py']' returned non-zero exit status 1.

```
    return connection._execute_clauseelement(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/sqlalchemy/engine/base.py", line 1640, in _execute_clauseelement
    ret = self._execute_context(
          ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/sqlalchemy/engine/base.py", line 1846, in _execute_context
    return self._exec_single_context(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/sqlalchemy/engine/base.py", line 1986, in _exec_single_context
    self._handle_dbapi_exception(
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/sqlalchemy/engine/base.py", line 2355, in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/sqlalchemy/engine/base.py", line 1967, in _exec_single_context
    self.dialect.do_execute(
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/sqlalchemy/engine/default.py", line 941, in do_execute
    cursor.execute(statement, parameters)
sqlalchemy.exc.IntegrityError: (sqlite3.IntegrityError) UNIQUE constraint failed: fit.id
[SQL: INSERT INTO fit (id, is_complete, max_log_likelihood, parent_id, is_grid_search, unique_tag, name, path_prefix, model_id, instance_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)]
[parameters: ('', 0, None, None, 1, '', None, None, None, None)]
(Background on this error at: https://sqlalche.me/e/20/gkpj)
```

## Skipped

| Script | Reason |
|--------|--------|
| `general.py` | Session mostly works but not maintaining currently. |
| `multi_analysis.py` | Session mostly works but not maintaining currently. |

## Passed

- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/database/directory/general.py` (2.8s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/database/directory/multi_analysis.py` (3.6s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/database/scrape/general.py` (3.5s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/database/scrape/multi_analysis.py` (3.5s)
