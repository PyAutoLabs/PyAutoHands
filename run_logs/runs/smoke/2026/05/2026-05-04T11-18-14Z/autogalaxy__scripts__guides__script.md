# Test Report: autogalaxy / scripts/guides (script)

**34 scripts** | 2 failed | 27 passed | 5 skipped

| Status | Count |
|--------|-------|
| failed | 2 |
| passed | 27 |
| skipped | 5 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/data_fitting.py` — FAILED (2.9s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/data_fitting.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/data_fitting.py", line 115, in <module>
    for dataset_list in dataset_gen:
                        ^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoGalaxy/autogalaxy/aggregator/imaging/imaging.py", line 63, in _imaging_from
    mask, header = agg_util.mask_header_from(fit=fit)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoGalaxy/autogalaxy/aggregator/agg_util.py", line 101, in mask_header_from
    header = aa.Header(header_sci_obj=fit.value(name=name)[0].header)
                                      ~~~~~~~~~~~~~~~~~~~~^^^
TypeError: 'NoneType' object is not subscriptable
```

### `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/models.py` — FAILED (3.1s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/models.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/models.py", line 102, in <module>
    for dataset_list, galaxies_list in zip(dataset_gen, galaxies_gen):
                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoGalaxy/autogalaxy/aggregator/imaging/imaging.py", line 63, in _imaging_from
    mask, header = agg_util.mask_header_from(fit=fit)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoGalaxy/autogalaxy/aggregator/agg_util.py", line 101, in mask_header_from
    header = aa.Header(header_sci_obj=fit.value(name=name)[0].header)
                                      ~~~~~~~~~~~~~~~~~~~~^^^
TypeError: 'NoneType' object is not subscriptable
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

- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/plot/simulator.py` (9.5s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/database/simulators/light_sersic_exp__0.py` (5.9s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/database/simulators/light_sersic_exp__1.py` (7.1s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/database/simulators/light_sersic_exp__2.py` (5.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/plot/start_here.py` (2.3s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/start_here.py` (13.3s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/advanced/over_sampling.py` (11.8s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/data_structures.py` (3.3s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/galaxies.py` (7.2s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/hpc/example_cpu_and_gpu.py` (6.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/modeling/bug_fix.py` (8.9s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/modeling/chaining.py` (5.3s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/modeling/cookbook.py` (4.0s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/modeling/customize.py` (10.1s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/modeling/searches.py` (4.9s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/plot/advanced/plotters_pixelization.py` (28.9s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/plot/examples/mat_plot.py` (7.1s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/plot/examples/plotters.py` (10.9s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/plot/examples/visuals.py` (5.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/_quick_fit.py` (0.1s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/galaxies_fit.py` (8.2s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/interferometer.py` (0.1s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/queries.py` (3.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/samples.py` (9.4s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/samples_via_aggregator.py` (4.0s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/units/cosmology.py` (4.7s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/units/flux.py` (32.2s)
