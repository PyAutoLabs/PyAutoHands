# Test Report: autogalaxy_test / scripts/jax_likelihood_functions (script)

**30 scripts** | 23 passed | 7 skipped

| Status | Count |
|--------|-------|
| passed | 23 |
| skipped | 7 |

## Skipped

| Script | Reason |
|--------|--------|
| `delaunay_mge.py` | SLOW 2026-07-14 - real-search JAX imaging Delaunay-MGE likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| `delaunay.py` | SLOW 2026-07-14 - real-search JAX interferometer Delaunay likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| `delaunay_mge.py` | SLOW 2026-07-14 - real-search JAX interferometer Delaunay-MGE likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| `mge.py` | SLOW 2026-07-14 - real-search JAX interferometer MGE likelihood; flakes at the 1800s mode=release cap (PyAutoHeart#74) |
| `mge_group.py` | SLOW 2026-07-14 - real-search JAX interferometer MGE-group likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| `rectangular_mge.py` | SLOW 2026-07-14 - real-search JAX interferometer rectangular-MGE likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| `delaunay_mge.py` | SLOW 2026-07-14 - real-search JAX Delaunay-MGE multi-band likelihood is borderline against the 1800s mode=release cap (its autolens_workspace_test sibling times out); skipped to keep release-validation deterministic. Speedup tracked by the Profiling Agent (PyAutoHeart#72). Not a bug. |

## Passed

- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/ellipse/simulator.py` (4.7s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/simulator.py` (6.7s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/simulator.py` (11.0s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/multi/simulator.py` (8.4s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/ellipse/fit.py` (7.4s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/ellipse/multipoles.py` (7.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/ellipse/multipoles_scaled.py` (7.5s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/delaunay.py` (40.7s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/lp.py` (9.4s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/mge.py` (23.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/mge_group.py` (38.5s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular.py` (25.0s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_mge.py` (26.7s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/lp.py` (8.0s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular.py` (15.5s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/light_multipole/multipole.py` (9.9s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/multi/dataset_model.py` (7.3s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/multi/delaunay.py` (19.5s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/multi/lp.py` (7.0s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/multi/mge.py` (23.3s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/multi/mge_group.py` (44.3s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/multi/rectangular.py` (28.5s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/multi/rectangular_mge.py` (42.8s)
