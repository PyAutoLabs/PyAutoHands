# Test Report: autofit / scripts/searches (script)

**4 scripts** | 1 failed | 1 passed | 2 skipped

| Status | Count |
|--------|-------|
| failed | 1 |
| passed | 1 |
| skipped | 2 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autofit_workspace/scripts/searches/nest.py` — FAILED (5.3s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autofit_workspace/scripts/searches/nest.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autofit_workspace/scripts/searches/nest.py", line 348, in <module>
    search = af.NSS(
             ^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/nest/nss/search.py", line 254, in __init__
    raise ImportError(
ImportError: af.NSS requires the optional `nss` package and the matching `handley-lab/blackjax` fork. Install via:
    pip install autofit[nss]
The extra pins specific upstream commits — see PyAutoFit's pyproject.toml `[project.optional-dependencies] nss` entry.
```

## Skipped

| Script | Reason |
|--------|--------|
| `mcmc.py` | Zeus section in merged mcmc.py fails Test Model Initialization. |
| `start_point.py` | bug https://github.com/rhayes777/PyAutoFit/issues/1017 |

## Passed

- `/home/jammy/Code/PyAutoLabs/autofit_workspace/scripts/searches/mle.py` (5.3s)
