# Test Report: autogalaxy / scripts/interferometer (script)

**12 scripts** | 1 failed | 10 passed | 1 skipped

| Status | Count |
|--------|-------|
| failed | 1 |
| passed | 10 |
| skipped | 1 |

## Failures

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/interferometer/features/pixelization/fit.py` — FAILED (5.5s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/interferometer/features/pixelization/fit.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/interferometer/features/pixelization/fit.py", line 282, in <module>
    subplot_of_mapper(inversion=inversion, mapper_index=0)
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/inversion/plot/inversion_plots.py", line 63, in subplot_of_mapper
    plot_array(
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/plot/array.py", line 199, in plot_array
    h, w = array.shape[:2]
    ^^^^
ValueError: not enough values to unpack (expected 2, got 1)
```

## Skipped

| Script | Reason |
|--------|--------|
| `modeling.py` | NEEDS_FIX 2026-04-10 - LinAlgError: matrix not positive definite in interferometer pixelization modeling |

## Passed

- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/interferometer/simulator.py` (2.6s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/interferometer/start_here.py` (7.2s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/interferometer/casa_reduction.py` (1.3s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/interferometer/data_preparation.py` (5.5s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/interferometer/features/pixelization/likelihood_function.py` (4.2s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/interferometer/features/pixelization/many_visibilities_preparation.py` (3.7s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/interferometer/features/pixelization/source_science.py` (6.3s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/interferometer/fit.py` (2.8s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/interferometer/likelihood_function.py` (2.5s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/interferometer/modeling.py` (3.7s)
