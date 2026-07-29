# Test Report: autolens_test / scripts/cluster (script)

**5 scripts** | 1 failed | 4 passed

| Status | Count |
|--------|-------|
| failed | 1 |
| passed | 4 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/visualization.py` — FAILED (4.8s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/visualization.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/visualization.py", line 171, in <module>
    assert_png("visualization_overlaid_positions.png")
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/visualization.py", line 141, in assert_png
    assert path.exists(), f"{filename} missing"
           ^^^^^^^^^^^^^
AssertionError: visualization_overlaid_positions.png missing
```

## Passed

- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/simulator.py` (7.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/csv_api.py` (5.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/lenstool_parity.py` (6.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/likelihood_sanity.py` (9.5s)
