# Test Report: autogalaxy / scripts/guides (script)

**36 scripts** | 1 failed | 30 passed | 5 skipped

| Status | Count |
|--------|-------|
| failed | 1 |
| passed | 30 |
| skipped | 5 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/start_here.py` — FAILED (4.7s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/start_here.py']' returned non-zero exit status 1.

```
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/start_here.py", line 231, in <module>
    dataset = ag.Imaging.from_fits(
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

## Skipped

| Script | Reason |
|--------|--------|
| `start_here.py` | SLOW 2026-04-10 - previously failed fast on a broken aggregator query; now runs the real aggregator and exceeds 60s |
| `searches.py` | Test mode breaks search visualization. |
| `csv_make.py` | SLOW 2026-04-10 - exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| `fits_make.py` | Test mode does not output .fits images. |
| `png_make.py` | Test mode does not output .png images. |

## Passed

- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/plot/simulator.py` (6.7s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/database/simulators/light_sersic_exp__0.py` (7.8s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/database/simulators/light_sersic_exp__1.py` (5.3s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/database/simulators/light_sersic_exp__2.py` (5.3s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/plot/start_here.py` (3.5s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/advanced/over_sampling.py` (4.1s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/data_structures.py` (3.2s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/galaxies.py` (5.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/hpc/example_cpu_and_gpu.py` (4.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/modeling/bug_fix.py` (6.4s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/modeling/chaining.py` (5.3s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/modeling/cookbook.py` (3.8s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/modeling/customize.py` (3.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/modeling/searches.py` (4.2s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/plot/advanced/plotters_pixelization.py` (10.4s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/plot/examples/mat_plot.py` (4.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/plot/examples/plotters.py` (6.3s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/plot/examples/visuals.py` (3.7s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/profiles/light.py` (5.4s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/_quick_fit.py` (0.1s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/data_fitting.py` (9.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/galaxies_fit.py` (6.5s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/interferometer.py` (0.0s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/models.py` (7.2s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/queries.py` (4.3s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/samples.py` (7.2s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/samples_via_aggregator.py` (3.8s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/latent_variables.py` (15.7s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/units/cosmology.py` (4.1s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/units/flux.py` (18.1s)
