# Test Report: autolens_test / scripts/cluster (script)

**5 scripts** | 4 passed | 1 skipped

| Status | Count |
|--------|-------|
| passed | 4 |
| skipped | 1 |

## Skipped

| Script | Reason |
|--------|--------|
| `visualization.py` | SLOW 2026-07-21 - per-plane critical-curve + caustic computation on the required full-extent 250x250 viz_grid (multi-plane marching squares) totals ~580s, over the 300s cap; same perf family as the modeling_visualization_jit scripts. Curves DO recover (plane-1 7 CC, plane-2 1 CC at full data) and the per-plane physics assertion passes — this is NOT the mislabelled "#1280 zero_contour algorithmic regression", which does not reproduce. env_vars.yaml unsets FAST_PLOTS/SMALL_DATASETS so it runs green in manual/full runs. |

## Passed

- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/simulator.py` (7.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/csv_api.py` (4.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/lenstool_parity.py` (4.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/cluster/likelihood_sanity.py` (10.7s)
