# Test Report: autolens / scripts/guides (script)

**46 scripts** | 41 passed | 5 skipped

| Status | Count |
|--------|-------|
| passed | 41 |
| skipped | 5 |

## Skipped

| Script | Reason |
|--------|--------|
| `start_here.py` | SLOW 2026-04-10 - previously failed fast on a broken aggregator query; now runs the real aggregator and exceeds 60s |
| `example_cpu.py` | HPC paths dont exist locally. |
| `searches.py` | Test mode breaks search visualization. |
| `fits_make.py` | Test mode does not output .fits images. |
| `png_make.py` | Test mode does not output .png images. |

## Passed

- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/plot/start_here.py` (6.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/start_here.py` (70.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/advanced/add_a_profile.py` (11.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/advanced/custom_analysis.py` (5.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/advanced/multi_plane.py` (3.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/advanced/over_sampling.py` (8.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/advanced/over_sampling_chaining.py` (9.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/data_structures.py` (4.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/galaxies.py` (6.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/lens_calc.py` (12.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/advanced/expectation_propagation.py` (15.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/advanced/graphical.py` (44.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/advanced/hierarchical.py` (10.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/bug_fix.py` (15.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/chaining.py` (11.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/cookbook.py` (10.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/customize.py` (16.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/searches.py` (6.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/slam_start_here.py` (44.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/plot/advanced/plotters_double_einstein_ring.py` (6.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/plot/advanced/plotters_pixelization.py` (12.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/plot/examples/mat_plot.py` (4.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/plot/examples/plotters.py` (18.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/plot/examples/visuals.py` (5.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/profiles/light.py` (6.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/profiles/light_and_mass_profiles.py` (82.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/profiles/mass.py` (6.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/_quick_fit.py` (0.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/data_fitting.py` (8.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/galaxies_fits.py` (11.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/interferometer.py` (0.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/models.py` (7.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/queries.py` (6.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/samples.py` (18.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/samples_via_aggregator.py` (5.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/latent_variables.py` (123.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/workflow/csv_make.py` (68.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/tracer.py` (11.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/units/cosmology.py` (6.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/units/flux.py` (58.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/units/mass_to_light_ratio_units.py` (7.2s)
