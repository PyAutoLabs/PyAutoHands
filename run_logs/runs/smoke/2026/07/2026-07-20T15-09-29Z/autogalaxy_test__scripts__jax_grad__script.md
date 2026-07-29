# Test Report: autogalaxy_test / scripts/jax_grad (script)

**6 scripts** | 4 passed | 2 skipped

| Status | Count |
|--------|-------|
| passed | 4 |
| skipped | 2 |

## Skipped

| Script | Reason |
|--------|--------|
| `mge.py` | SLOW 2026-07-14 - finite-difference JAX interferometer MGE gradient; flakes at the 1800s cap (PyAutoHeart#74) |
| `mge.py` | SLOW 2026-07-14 - finite-difference JAX multi-band MGE gradient; flakes at the 1800s cap (PyAutoHeart#74) |

## Passed

- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_grad/imaging/lp.py` (18.1s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_grad/imaging/mge.py` (20.3s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_grad/interferometer/lp.py` (8.9s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_grad/multi/lp.py` (12.0s)
