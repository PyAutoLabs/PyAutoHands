# Test Report: autolens / scripts/guides (script)

**46 scripts** | 1 failed | 39 passed | 5 skipped | 1 timeout

| Status | Count |
|--------|-------|
| failed | 1 |
| passed | 39 |
| skipped | 5 |
| timeout | 1 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/start_here.py` — FAILED (151.4s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/start_here.py']' returned non-zero exit status 1.

```
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/start_here.py", line 247, in <module>
    dataset = al.Imaging.from_fits(
              ^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/dataset/imaging/dataset.py", line 232, in from_fits
    return Imaging(
           ^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/dataset/imaging/dataset.py", line 108, in __init__
    raise exc.DatasetException(
autoarray.exc.DatasetException: 
                    A value in the noise-map of the dataset is 0.0. 

                    This is less than or equal to zero, and therefore an ill-defined value which must be corrected.
                    
                    The 2D indexes of the arrays in the native noise map array are [[ 0  0]
 [ 0  1]
 [ 0  2]
 ...
 [99 97]
 [99 98]
 [99 99]].
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

- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/plot/start_here.py` (12.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/advanced/add_a_profile.py` (4.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/advanced/custom_analysis.py` (5.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/advanced/multi_plane.py` (4.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/advanced/over_sampling.py` (5.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/advanced/over_sampling_chaining.py` (10.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/data_structures.py` (3.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/galaxies.py` (7.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/lens_calc.py` (8.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/advanced/expectation_propagation.py` (12.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/advanced/graphical.py` (33.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/advanced/hierarchical.py` (5.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/bug_fix.py` (18.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/chaining.py` (9.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/cookbook.py` (6.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/customize.py` (5.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/searches.py` (6.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/slam_start_here.py` (37.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/plot/advanced/plotters_double_einstein_ring.py` (8.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/plot/advanced/plotters_pixelization.py` (12.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/plot/examples/mat_plot.py` (4.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/plot/examples/plotters.py` (20.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/plot/examples/visuals.py` (5.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/profiles/light.py` (6.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/profiles/light_and_mass_profiles.py` (63.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/profiles/mass.py` (6.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/_quick_fit.py` (0.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/data_fitting.py` (25.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/galaxies_fits.py` (21.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/interferometer.py` (0.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/models.py` (9.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/queries.py` (6.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/samples.py` (31.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/samples_via_aggregator.py` (5.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/workflow/csv_make.py` (158.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/tracer.py` (8.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/units/cosmology.py` (7.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/units/flux.py` (53.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/units/mass_to_light_ratio_units.py` (5.6s)
