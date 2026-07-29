# Test Report: autolens_test / scripts/interferometer (script)

**8 scripts** | 7 passed | 1 skipped

| Status | Count |
|--------|-------|
| passed | 7 |
| skipped | 1 |

## Skipped

| Script | Reason |
|--------|--------|
| `modeling_visualization_jit.py` | SLOW 2026-05-20 - JIT + full visualization pipeline exceeds 300s cap; same root cause as imaging/modeling_visualization_jit family |

## Passed

- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/simulator/no_lens_light.py` (4.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/simulator/with_lens_light.py` (4.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/simulator_use_jax_parity.py` (10.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/model_fit.py` (7.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/nufft.py` (14.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/visualization.py` (45.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/visualization_jax.py` (60.2s)
