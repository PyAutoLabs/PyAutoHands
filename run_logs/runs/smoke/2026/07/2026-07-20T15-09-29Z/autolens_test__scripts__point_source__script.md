# Test Report: autolens_test / scripts/point_source (script)

**4 scripts** | 3 passed | 1 skipped

| Status | Count |
|--------|-------|
| passed | 3 |
| skipped | 1 |

## Skipped

| Script | Reason |
|--------|--------|
| `modeling_visualization_jit.py` | SLOW 2026-07-08 - JIT + Part-2 live Nautilus fit exceeds 300s cap; same family as imaging/interferometer modeling_visualization_jit (the zero_contour perf-assert false-positive was separately fixed to a cold/warm ratio, which now lets the script run past it into the slow fit) |

## Passed

- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/point_source/simulators/point_source.py` (3.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/point_source/visualization.py` (13.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/point_source/visualization_jax.py` (43.6s)
