# Test Report: autolens / scripts/guides (script)

**46 scripts** | 1 failed | 39 passed | 5 skipped | 1 timeout

| Status | Count |
|--------|-------|
| failed | 1 |
| passed | 39 |
| skipped | 5 |
| timeout | 1 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/models.py` — FAILED (11.7s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/models.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/models.py", line 91, in <module>
    for dataset_list, tracer_list in zip(dataset_gen, tracer_gen):
                                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoGalaxy/autogalaxy/aggregator/imaging/imaging.py", line 63, in _imaging_from
    mask, header = agg_util.mask_header_from(fit=fit)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoGalaxy/autogalaxy/aggregator/agg_util.py", line 101, in mask_header_from
    header = aa.Header(header_sci_obj=fit.value(name=name)[0].header)
                                      ~~~~~~~~~~~~~~~~~~~~^^^
TypeError: 'NoneType' object is not subscriptable
```

### `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/latent_variables.py` — TIMEOUT (300.0s)

Timed out after 300s

## Skipped

| Script | Reason |
|--------|--------|
| `start_here.py` | SLOW 2026-04-10 - previously failed fast on a broken aggregator query; now runs the real aggregator and exceeds 60s |
| `example_cpu.py` | HPC paths dont exist locally. |
| `searches.py` | Test mode breaks search visualization. |
| `fits_make.py` | Test mode does not output .fits images. |
| `png_make.py` | Test mode does not output .png images. |

## Passed

- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/plot/start_here.py` (15.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/start_here.py` (13.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/advanced/add_a_profile.py` (5.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/advanced/custom_analysis.py` (7.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/advanced/multi_plane.py` (3.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/advanced/over_sampling.py` (6.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/advanced/over_sampling_chaining.py` (11.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/data_structures.py` (4.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/galaxies.py` (7.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/lens_calc.py` (8.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/advanced/expectation_propagation.py` (11.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/advanced/graphical.py` (35.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/advanced/hierarchical.py` (6.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/bug_fix.py` (18.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/chaining.py` (11.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/cookbook.py` (5.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/customize.py` (6.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/searches.py` (4.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/slam_start_here.py` (32.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/plot/advanced/plotters_double_einstein_ring.py` (7.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/plot/advanced/plotters_pixelization.py` (13.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/plot/examples/mat_plot.py` (5.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/plot/examples/plotters.py` (23.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/plot/examples/visuals.py` (6.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/profiles/light.py` (7.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/profiles/light_and_mass_profiles.py` (69.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/profiles/mass.py` (7.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/_quick_fit.py` (202.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/data_fitting.py` (60.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/galaxies_fits.py` (185.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/interferometer.py` (0.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/queries.py` (7.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/samples.py` (38.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/samples_via_aggregator.py` (9.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/workflow/csv_make.py` (7.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/tracer.py` (11.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/units/cosmology.py` (7.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/units/flux.py` (79.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/units/mass_to_light_ratio_units.py` (6.7s)
