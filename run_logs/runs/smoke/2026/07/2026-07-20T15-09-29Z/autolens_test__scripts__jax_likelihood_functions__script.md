# Test Report: autolens_test / scripts/jax_likelihood_functions (script)

**45 scripts** | 34 passed | 11 skipped

| Status | Count |
|--------|-------|
| passed | 34 |
| skipped | 11 |

## Skipped

| Script | Reason |
|--------|--------|
| `delaunay.py` | SLOW 2026-07-14 - real-search JAX datacube Delaunay likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| `shared_preloads.py` | SLOW 2026-07-14 - real-search JAX datacube shared-preloads likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| `delaunay_mge.py` | NEEDS_FIX 2026-04-10 - timeout in JAX likelihood function benchmark |
| `mge_group.py` | NEEDS_FIX 2026-04-10 - timeout in JAX likelihood function benchmark |
| `delaunay.py` | SLOW 2026-07-14 - real-search JAX interferometer Delaunay likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| `delaunay_mge.py` | SLOW 2026-07-14 - real-search JAX interferometer Delaunay-MGE likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| `mge.py` | SLOW 2026-07-14 - real-search JAX interferometer MGE likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| `mge_group.py` | SLOW 2026-07-14 - real-search JAX interferometer MGE-group likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| `rectangular_mge.py` | SLOW 2026-07-14 - real-search JAX interferometer rectangular-MGE likelihood; flakes at the 1800s cap (PyAutoHeart#74) |
| `delaunay_mge.py` | SLOW 2026-07-14 - real-search JAX Delaunay-MGE multi-band likelihood exceeds the 1800s mode=release cap; speedup tracked by the Profiling Agent (PyAutoHeart#72). Not a bug. |
| `shared_preloads.py` | SLOW 2026-07-14 - real-search JAX multi-band shared-preloads likelihood; flakes at the 1800s mode=release cap (PyAutoHeart#74) |

## Passed

- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/simulator.py` (12.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/simulator_dspl.py` (10.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/simulator.py` (9.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/simulator_dspl.py` (10.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/multi/simulator.py` (6.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/point_source/simulator.py` (2.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/weak/simulator.py` (2.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/datacube/rectangular.py` (20.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/delaunay.py` (40.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/delaunay_near_caustic.py` (37.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/lp.py` (16.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/mge.py` (37.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/potential_correction.py` (7.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular.py` (30.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_dspl.py` (45.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_mge.py` (67.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/imaging/subhalo.py` (65.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/lp.py` (22.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/potential_correction.py` (14.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular.py` (27.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular_dspl.py` (38.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular_sparse.py` (28.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/light_multipole/multipole.py` (18.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/multi/dataset_model.py` (13.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/multi/delaunay.py` (32.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/multi/lp.py` (13.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/multi/mge.py` (16.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/multi/mge_group.py` (64.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/multi/rectangular.py` (25.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/multi/rectangular_mge.py` (34.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/point_source/image_plane.py` (36.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/point_source/point.py` (50.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/point_source/source_plane.py` (7.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_likelihood_functions/weak/shear.py` (7.9s)
