# Test Report: autolens_test / scripts/imaging (script)

**10 scripts** | 5 passed | 5 skipped

| Status | Count |
|--------|-------|
| passed | 5 |
| skipped | 5 |

## Skipped

| Script | Reason |
|--------|--------|
| `modeling_visualization_jit.py` | SLOW 2026-05-07 - JIT + full visualization pipeline exceeds 300s cap (autogalaxy variant ~90s); unblocked by PR #70 from prior `expected jax.Array, got numpy.float64` AssertionError, now hits perf wall |
| `modeling_visualization_jit_delaunay.py` | SLOW 2026-05-07 - JIT + full visualization pipeline exceeds 300s cap (autogalaxy variant ~90s); unblocked by PR #70 from prior `expected jax.Array, got numpy.float64` AssertionError, now hits perf wall |
| `modeling_visualization_jit_rectangular.py` | SLOW 2026-05-07 - JIT + full visualization pipeline exceeds 300s cap (autogalaxy variant ~90s); unblocked by PR #70 from prior `expected jax.Array, got numpy.float64` AssertionError, now hits perf wall |
| `visualization.py` | NEEDS_FIX 2026-04-10 - AssertionError: dataset.png missing after visualization refactor |
| `visualization_jax.py` | NEEDS_FIX 2026-04-10 - AssertionError: dataset.png missing after visualization refactor |

## Passed

- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/simulator/no_lens_light.py` (3.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/simulator/with_lens_light.py` (3.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/simulator_use_jax_parity.py` (8.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/convolution.py` (5.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/model_fit.py` (7.0s)
