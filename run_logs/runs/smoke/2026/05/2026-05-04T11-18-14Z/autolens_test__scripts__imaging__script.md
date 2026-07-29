# Test Report: autolens_test / scripts/imaging (script)

**9 scripts** | 4 passed | 2 skipped | 3 timeout

| Status | Count |
|--------|-------|
| passed | 4 |
| skipped | 2 |
| timeout | 3 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/modeling_visualization_jit.py` — TIMEOUT (300.3s)

Timed out after 300s

### `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/modeling_visualization_jit_delaunay.py` — TIMEOUT (300.2s)

Timed out after 300s

### `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/modeling_visualization_jit_rectangular.py` — TIMEOUT (300.6s)

Timed out after 301s

## Skipped

| Script | Reason |
|--------|--------|
| `visualization.py` | NEEDS_FIX 2026-04-10 - AssertionError: dataset.png missing after visualization refactor |
| `visualization_jax.py` | NEEDS_FIX 2026-04-10 - AssertionError: dataset.png missing after visualization refactor |

## Passed

- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/simulator/no_lens_light.py` (8.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/simulator/with_lens_light.py` (5.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/convolution.py` (13.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/model_fit.py` (12.9s)
