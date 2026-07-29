# Test Report: autolens / scripts/cluster (script)

**3 scripts** | 1 failed | 2 skipped

| Status | Count |
|--------|-------|
| failed | 1 |
| skipped | 2 |

## Failures

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/cluster/simulator.py` — FAILED (4.1s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/cluster/simulator.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/cluster/simulator.py", line 418, in <module>
    raw = np.asarray(jitted_solve(tracer, coord).array)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: function jitted_solve at /home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/cluster/simulator.py:405 traced for jit returned a value of type <class 'autoarray.structures.grids.irregular_2d.Grid2DIrregular'> at output component jit, which is not a valid JAX type
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
```

## Skipped

| Script | Reason |
|--------|--------|
| `start_here.py` | Cluster analysis is not maintained and test mode breaks it. |
| `modeling.py` | Cluster modeling is not maintained and test mode breaks it. |
