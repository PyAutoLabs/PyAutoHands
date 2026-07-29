# Test Report: autogalaxy / scripts/guides (script)

**34 scripts** | 7 failed | 22 passed | 5 skipped

| Status | Count |
|--------|-------|
| failed | 7 |
| passed | 22 |
| skipped | 5 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/start_here.py` — FAILED (4.9s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/start_here.py']' returned non-zero exit status 1.

```
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/abstract_search.py", line 117, in decorated
    return func(self, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/abstract_search.py", line 668, in start_resume_fit
    search_internal, fitness = self._fit(
                               ^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/nest/nautilus/search.py", line 209, in _fit
    fitness = Fitness(
              ^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/fitness.py", line 152, in __init__
    self.check_log_likelihood(fitness=self)
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/fitness.py", line 518, in check_log_likelihood
    parameters = max_log_likelihood_sample.parameter_lists_for_model(model=self.model)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/samples/sample.py", line 102, in parameter_lists_for_model
    return self.parameter_lists_for_paths(paths)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/samples/sample.py", line 114, in parameter_lists_for_paths
    raise KeyError(
KeyError: "Could not find any of the following keys in kwargs (('galaxies', 'galaxy', 'bulge', 'ell_comps', 'ell_comps_0'),)"
```

### `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/hpc/example_cpu_and_gpu.py` — FAILED (0.0s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/hpc/example_cpu_and_gpu.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/hpc/example_cpu_and_gpu.py", line 64, in <module>
    hpc_output_path = Path(path.sep) / "hpc" / "data" / "hpc_username" / "output"
                           ^^^^
NameError: name 'path' is not defined. Did you mean: 'Path'?
```

### `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/data_fitting.py` — FAILED (1.7s)

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

### `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/galaxies_fit.py` — FAILED (3.3s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/galaxies_fit.py']' returned non-zero exit status 1.

```
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/abstract_search.py", line 117, in decorated
    return func(self, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/abstract_search.py", line 668, in start_resume_fit
    search_internal, fitness = self._fit(
                               ^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/nest/nautilus/search.py", line 209, in _fit
    fitness = Fitness(
              ^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/fitness.py", line 152, in __init__
    self.check_log_likelihood(fitness=self)
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/fitness.py", line 518, in check_log_likelihood
    parameters = max_log_likelihood_sample.parameter_lists_for_model(model=self.model)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/samples/sample.py", line 102, in parameter_lists_for_model
    return self.parameter_lists_for_paths(paths)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/samples/sample.py", line 114, in parameter_lists_for_paths
    raise KeyError(
KeyError: "Could not find any of the following keys in kwargs (('galaxies', 'galaxy', 'bulge', 'ell_comps', 'ell_comps_0'),)"
```

### `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/models.py` — FAILED (1.7s)

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

### `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/samples.py` — FAILED (4.5s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/samples.py']' returned non-zero exit status 1.

```
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/abstract_search.py", line 117, in decorated
    return func(self, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/abstract_search.py", line 668, in start_resume_fit
    search_internal, fitness = self._fit(
                               ^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/nest/nautilus/search.py", line 209, in _fit
    fitness = Fitness(
              ^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/fitness.py", line 152, in __init__
    self.check_log_likelihood(fitness=self)
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/fitness.py", line 518, in check_log_likelihood
    parameters = max_log_likelihood_sample.parameter_lists_for_model(model=self.model)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/samples/sample.py", line 102, in parameter_lists_for_model
    return self.parameter_lists_for_paths(paths)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/samples/sample.py", line 114, in parameter_lists_for_paths
    raise KeyError(
KeyError: "Could not find any of the following keys in kwargs (('galaxies', 'galaxy', 'bulge', 'ell_comps', 'ell_comps_0'),)"
```

### `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/samples_via_aggregator.py` — FAILED (3.4s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/samples_via_aggregator.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/samples_via_aggregator.py", line 173, in <module>
    instance = samples_summary.max_log_likelihood()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/samples/interface.py", line 32, in wrapper
    vector = func(self, *args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/samples/interface.py", line 95, in max_log_likelihood
    return sample.parameter_lists_for_paths(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/samples/sample.py", line 114, in parameter_lists_for_paths
    raise KeyError(
KeyError: "Could not find any of the following keys in kwargs (('galaxies', 'galaxy', 'bulge', 'centre', 'centre_0'), ('galaxies', 'galaxy', 'disk', 'centre', 'centre_0'))"
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

- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/plot/simulator.py` (10.0s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/database/simulators/light_sersic_exp__0.py` (4.8s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/database/simulators/light_sersic_exp__1.py` (8.7s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/database/simulators/light_sersic_exp__2.py` (5.1s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/plot/start_here.py` (1.7s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/advanced/over_sampling.py` (4.0s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/data_structures.py` (2.2s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/galaxies.py` (3.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/modeling/bug_fix.py` (8.0s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/modeling/chaining.py` (3.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/modeling/cookbook.py` (2.3s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/modeling/customize.py` (3.3s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/modeling/searches.py` (5.5s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/plot/advanced/plotters_pixelization.py` (18.0s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/plot/examples/mat_plot.py` (3.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/plot/examples/plotters.py` (6.2s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/plot/examples/visuals.py` (3.3s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/_quick_fit.py` (0.1s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/interferometer.py` (0.0s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/results/aggregator/queries.py` (4.8s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/units/cosmology.py` (8.5s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/guides/units/flux.py` (21.5s)
