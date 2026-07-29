# Test Report: autofit_test / scripts/database (script)

**8 scripts** | 2 failed | 4 passed | 2 skipped

| Status | Count |
|--------|-------|
| failed | 2 |
| passed | 4 |
| skipped | 2 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/database/scrape/grid_search.py` — FAILED (3.6s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/database/scrape/grid_search.py']' returned non-zero exit status 1.

```
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:173: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autofit_workspace_test matches the installed library version (2026.5.29.4): no `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/database/aggregator/info.py:31: SAWarning: relationship 'Fit.arrays' will copy column fit.id to column array.fit_id, which conflicts with relationship(s): 'HDU.fit' (copies fit.id to array.fit_id). If this is not the intention, consider if these relationships should be linked with back_populates, or if viewonly=True should be applied to one or more if they are read-only. For the less common case that foreign key constraints are partially overlapping, the orm.foreign() annotation can be used to isolate the columns that should be written towards.   To silence this warning, add the parameter 'overlaps="fit"' to the 'Fit.arrays' relationship. (Background on this warning at: https://sqlalche.me/e/20/qzyx) (This warning originated from the `configure_mappers()` process, which was invoked automatically in response to a user-initiated operation.)
  return self.session.query(Fit).all()
/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/database/aggregator/info.py:31: SAWarning: relationship 'Fit.hdus' will copy column fit.id to column array.fit_id, which conflicts with relationship(s): 'Array.fit' (copies fit.id to array.fit_id), 'Fit.arrays' (copies fit.id to array.fit_id). If this is not the intention, consider if these relationships should be linked with back_populates, or if viewonly=True should be applied to one or more if they are read-only. For the less common case that foreign key constraints are partially overlapping, the orm.foreign() annotation can be used to isolate the columns that should be written towards.   To silence this warning, add the parameter 'overlaps="arrays,fit"' to the 'Fit.hdus' relationship. (Background on this warning at: https://sqlalche.me/e/20/qzyx) (This warning originated from the `configure_mappers()` process, which was invoked automatically in response to a user-initiated operation.)
  return self.session.query(Fit).all()
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/database/scrape/grid_search.py", line 132, in <module>
    assert len(agg) > 0
           ^^^^^^^^^^^^
AssertionError
```

### `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/database/scrape/sensitivity.py` — FAILED (5.0s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/database/scrape/sensitivity.py']' returned non-zero exit status 1.

```
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:173: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autofit_workspace_test matches the installed library version (2026.5.29.4): no `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/database/aggregator/info.py:31: SAWarning: relationship 'Fit.arrays' will copy column fit.id to column array.fit_id, which conflicts with relationship(s): 'HDU.fit' (copies fit.id to array.fit_id). If this is not the intention, consider if these relationships should be linked with back_populates, or if viewonly=True should be applied to one or more if they are read-only. For the less common case that foreign key constraints are partially overlapping, the orm.foreign() annotation can be used to isolate the columns that should be written towards.   To silence this warning, add the parameter 'overlaps="fit"' to the 'Fit.arrays' relationship. (Background on this warning at: https://sqlalche.me/e/20/qzyx) (This warning originated from the `configure_mappers()` process, which was invoked automatically in response to a user-initiated operation.)
  return self.session.query(Fit).all()
/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/database/aggregator/info.py:31: SAWarning: relationship 'Fit.hdus' will copy column fit.id to column array.fit_id, which conflicts with relationship(s): 'Array.fit' (copies fit.id to array.fit_id), 'Fit.arrays' (copies fit.id to array.fit_id). If this is not the intention, consider if these relationships should be linked with back_populates, or if viewonly=True should be applied to one or more if they are read-only. For the less common case that foreign key constraints are partially overlapping, the orm.foreign() annotation can be used to isolate the columns that should be written towards.   To silence this warning, add the parameter 'overlaps="arrays,fit"' to the 'Fit.hdus' relationship. (Background on this warning at: https://sqlalche.me/e/20/qzyx) (This warning originated from the `configure_mappers()` process, which was invoked automatically in response to a user-initiated operation.)
  return self.session.query(Fit).all()
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/database/scrape/sensitivity.py", line 547, in <module>
    assert len(agg) > 0
           ^^^^^^^^^^^^
AssertionError
```

## Skipped

| Script | Reason |
|--------|--------|
| `general.py` | Session mostly works but not maintaining currently. |
| `multi_analysis.py` | Session mostly works but not maintaining currently. |

## Passed

- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/database/directory/general.py` (4.6s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/database/directory/multi_analysis.py` (4.9s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/database/scrape/general.py` (5.7s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/database/scrape/multi_analysis.py` (5.5s)
