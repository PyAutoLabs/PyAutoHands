# Test Report: autolens / scripts/multi (script)

**18 scripts** | 1 failed | 16 passed | 1 skipped

| Status | Count |
|--------|-------|
| failed | 1 |
| passed | 16 |
| skipped | 1 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/multi/features/imaging_and_point_source/modeling.py` — FAILED (4.5s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/multi/features/imaging_and_point_source/modeling.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/multi/features/imaging_and_point_source/modeling.py", line 161, in <module>
    quasar_image_circles |= distances < quasar_mask_radius
ValueError: operands could not be broadcast together with shapes (200,200) (16,16) (200,200)
```

## Skipped

| Script | Reason |
|--------|--------|
| `modeling.py` | NEEDS_FIX 2026-04-10 - autofit.exc.FitException in multi-wavelength modeling |

## Passed

- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/multi/features/dataset_offsets/simulator.py` (6.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/multi/features/imaging_and_interferometer/simulator.py` (3.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/multi/features/pixelization/simulator.py` (5.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/multi/features/same_wavelength/simulator.py` (6.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/multi/features/wavelength_dependence/simulator.py` (6.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/multi/simulator.py` (6.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/multi/start_here.py` (69.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/multi/features/dataset_offsets/modeling.py` (7.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/multi/features/imaging_and_interferometer/modeling.py` (6.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/multi/features/one_by_one/modeling.py` (6.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/multi/features/pixelization/modeling.py` (8.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/multi/features/same_wavelength/modeling.py` (6.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/multi/features/slam/independent.py` (12.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/multi/features/slam/simultaneous.py` (26.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/multi/modeling.py` (14.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/multi/plot.py` (3.9s)
