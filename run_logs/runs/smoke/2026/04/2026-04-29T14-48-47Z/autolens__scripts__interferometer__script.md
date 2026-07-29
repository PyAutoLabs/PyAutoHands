# Test Report: autolens / scripts/interferometer (script)

**21 scripts** | 1 failed | 18 passed | 2 skipped

| Status | Count |
|--------|-------|
| failed | 1 |
| passed | 18 |
| skipped | 2 |

## Failures

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/interferometer/features/pixelization/fit.py` — FAILED (4.8s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/interferometer/features/pixelization/fit.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/interferometer/features/pixelization/fit.py", line 288, in <module>
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
| `casa_reduction.py` | Requires CASA MeasurementSet output, not runnable standalone |
| `delaunay.py` | NEEDS_FIX 2026-04-10 - broadcast shape mismatch (2,2) vs (1032,1032) in Delaunay interferometer |

## Passed

- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/interferometer/features/extra_galaxies/simulator.py` (3.2s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/interferometer/features/subhalo/simulator.py` (2.9s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/interferometer/simulator.py` (3.6s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/interferometer/features/subhalo/detect/start_here.py` (11.1s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/interferometer/features/subhalo/sensitivity/start_here.py` (0.0s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/interferometer/start_here.py` (20.8s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/interferometer/data_preparation.py` (5.2s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/interferometer/features/extra_galaxies/modeling.py` (4.2s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/interferometer/features/extra_galaxies/slam.py` (6.3s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/interferometer/features/pixelization/likelihood_function.py` (3.6s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/interferometer/features/pixelization/many_visibilities_preparation.py` (3.1s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/interferometer/features/pixelization/modeling.py` (7.3s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/interferometer/features/pixelization/slam.py` (7.6s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/interferometer/features/pixelization/source_science.py` (7.6s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/interferometer/fit.py` (4.3s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/interferometer/likelihood_function.py` (3.7s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/interferometer/modeling.py` (9.8s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/interferometer/source_science.py` (2.9s)
