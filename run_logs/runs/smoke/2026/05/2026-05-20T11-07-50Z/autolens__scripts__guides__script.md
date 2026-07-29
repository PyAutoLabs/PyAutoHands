# Test Report: autolens / scripts/guides (script)

**45 scripts** | 40 passed | 5 skipped

| Status | Count |
|--------|-------|
| passed | 40 |
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

- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/plot/start_here.py` (13.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/start_here.py` (69.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/advanced/add_a_profile.py` (7.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/advanced/custom_analysis.py` (9.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/advanced/multi_plane.py` (4.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/advanced/over_sampling.py` (6.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/advanced/over_sampling_chaining.py` (8.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/data_structures.py` (6.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/galaxies.py` (8.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/lens_calc.py` (8.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/advanced/expectation_propagation.py` (32.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/advanced/graphical.py` (60.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/advanced/hierarchical.py` (10.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/bug_fix.py` (14.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/chaining.py` (15.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/cookbook.py` (7.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/customize.py` (8.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/searches.py` (6.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/slam_start_here.py` (26.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/plot/advanced/plotters_double_einstein_ring.py` (19.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/plot/advanced/plotters_pixelization.py` (12.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/plot/examples/mat_plot.py` (5.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/plot/examples/plotters.py` (30.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/plot/examples/visuals.py` (5.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/profiles/light.py` (6.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/profiles/light_and_mass_profiles.py` (64.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/profiles/mass.py` (6.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/_quick_fit.py` (0.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/data_fitting.py` (8.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/galaxies_fits.py` (8.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/interferometer.py` (0.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/models.py` (14.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/queries.py` (9.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/samples.py` (24.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/samples_via_aggregator.py` (9.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/workflow/csv_make.py` (77.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/tracer.py` (12.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/units/cosmology.py` (6.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/units/flux.py` (55.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/units/mass_to_light_ratio_units.py` (5.9s)
