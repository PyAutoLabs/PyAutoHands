# Test Report: autogalaxy / scripts/guides (script)

**36 scripts** | 31 passed | 5 skipped

| Status | Count |
|--------|-------|
| passed | 31 |
| skipped | 5 |

## Skipped

| Script | Reason |
|--------|--------|
| `start_here.py` | SLOW 2026-04-10 - previously failed fast on a broken aggregator query; now runs the real aggregator and exceeds 60s |
| `searches.py` | Test mode breaks search visualization. |
| `csv_make.py` | SLOW 2026-04-10 - exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| `fits_make.py` | Test mode does not output .fits images. |
| `png_make.py` | Test mode does not output .png images. |

## Passed

- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/plot/simulator.py` (11.3s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/database/simulators/light_sersic_exp__0.py` (9.3s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/database/simulators/light_sersic_exp__1.py` (9.9s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/database/simulators/light_sersic_exp__2.py` (12.0s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/plot/start_here.py` (7.4s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/start_here.py` (20.8s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/advanced/over_sampling.py` (7.9s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/data_structures.py` (6.8s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/galaxies.py` (8.9s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/hpc/example_cpu_and_gpu.py` (8.8s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/modeling/bug_fix.py` (9.7s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/modeling/chaining.py` (9.5s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/modeling/cookbook.py` (6.5s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/modeling/customize.py` (7.9s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/modeling/searches.py` (6.1s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/plot/advanced/plotters_pixelization.py` (18.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/plot/examples/mat_plot.py` (7.7s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/plot/examples/plotters.py` (8.4s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/plot/examples/visuals.py` (4.7s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/profiles/light.py` (6.5s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/_quick_fit.py` (0.0s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/data_fitting.py` (12.8s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/galaxies_fit.py` (5.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/interferometer.py` (0.0s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/models.py` (9.4s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/queries.py` (5.2s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/samples.py` (8.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/samples_via_aggregator.py` (6.7s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/latent_variables.py` (7.7s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/units/cosmology.py` (5.0s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/units/flux.py` (26.7s)
