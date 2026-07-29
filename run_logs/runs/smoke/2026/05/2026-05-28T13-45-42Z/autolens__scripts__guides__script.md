# Test Report: autolens / scripts/guides (script)

**46 scripts** | 5 failed | 36 passed | 5 skipped

| Status | Count |
|--------|-------|
| failed | 5 |
| passed | 36 |
| skipped | 5 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/start_here.py` — FAILED (7.2s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/start_here.py']' returned non-zero exit status 1.

```
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/abstract_search.py", line 117, in decorated
    return func(self, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/abstract_search.py", line 677, in start_resume_fit
    search_internal, fitness = self._fit(
                               ^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/nest/nautilus/search.py", line 210, in _fit
    fitness = Fitness(
              ^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/fitness.py", line 164, in __init__
    self.check_log_likelihood(fitness=self)
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/fitness.py", line 577, in check_log_likelihood
    raise exc.SearchException(
autofit.exc.SearchException: 
                Figure of merit sanity check failed. 

                This means that the existing results of a model fit used a different
                likelihood function compared to the one implemented now.
                Old Figure of Merit = -1019.6430042720705
                New Figure of Merit = -1024.1860574458706
```

### `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/data_fitting.py` — FAILED (4.7s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/data_fitting.py']' returned non-zero exit status 1.

```
/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/data_fitting.py:153: SyntaxWarning: invalid escape sequence '\*'
  customize the plots using the `plot_yx` and `plot_array`/`subplot_\*` objects..
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/data_fitting.py", line 105, in <module>
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

### `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/galaxies_fits.py` — FAILED (6.4s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/galaxies_fits.py']' returned non-zero exit status 1.

```
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/abstract_search.py", line 117, in decorated
    return func(self, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/abstract_search.py", line 677, in start_resume_fit
    search_internal, fitness = self._fit(
                               ^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/nest/nautilus/search.py", line 210, in _fit
    fitness = Fitness(
              ^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/fitness.py", line 164, in __init__
    self.check_log_likelihood(fitness=self)
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/fitness.py", line 577, in check_log_likelihood
    raise exc.SearchException(
autofit.exc.SearchException: 
                Figure of merit sanity check failed. 

                This means that the existing results of a model fit used a different
                likelihood function compared to the one implemented now.
                Old Figure of Merit = -1019.6430042720705
                New Figure of Merit = -1024.1860574458706
```

### `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/models.py` — FAILED (7.5s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/models.py']' returned non-zero exit status 1.

```
/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/mask/mask_2d_util.py:564: UserWarning: Mask padded from (15, 15) to (np.int64(25), np.int64(25)) (parity preserved) to support kernel footprint (11, 11).
  warnings.warn(
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

### `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/samples.py` — FAILED (5.9s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/samples.py']' returned non-zero exit status 1.

```
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/abstract_search.py", line 117, in decorated
    return func(self, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/abstract_search.py", line 677, in start_resume_fit
    search_internal, fitness = self._fit(
                               ^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/nest/nautilus/search.py", line 210, in _fit
    fitness = Fitness(
              ^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/fitness.py", line 164, in __init__
    self.check_log_likelihood(fitness=self)
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/fitness.py", line 577, in check_log_likelihood
    raise exc.SearchException(
autofit.exc.SearchException: 
                Figure of merit sanity check failed. 

                This means that the existing results of a model fit used a different
                likelihood function compared to the one implemented now.
                Old Figure of Merit = -1224.4306830405044
                New Figure of Merit = -1228.0670818130438
```

## Skipped

| Script | Reason |
|--------|--------|
| `start_here.py` | SLOW 2026-04-10 - previously failed fast on a broken aggregator query; now runs the real aggregator and exceeds 60s |
| `example_cpu.py` | HPC paths dont exist locally. |
| `searches.py` | Test mode breaks search visualization. |
| `fits_make.py` | Test mode does not output .fits images. |
| `png_make.py` | Test mode does not output .png images. |

## Passed

- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/plot/start_here.py` (8.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/advanced/add_a_profile.py` (4.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/advanced/custom_analysis.py` (7.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/advanced/multi_plane.py` (4.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/advanced/over_sampling.py` (7.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/advanced/over_sampling_chaining.py` (7.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/data_structures.py` (4.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/galaxies.py` (8.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/lens_calc.py` (8.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/advanced/expectation_propagation.py` (14.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/advanced/graphical.py` (64.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/advanced/hierarchical.py` (6.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/bug_fix.py` (13.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/chaining.py` (24.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/cookbook.py` (7.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/customize.py` (9.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/searches.py` (5.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/modeling/slam_start_here.py` (27.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/plot/advanced/plotters_double_einstein_ring.py` (7.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/plot/advanced/plotters_pixelization.py` (10.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/plot/examples/mat_plot.py` (5.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/plot/examples/plotters.py` (17.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/plot/examples/visuals.py` (6.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/profiles/light.py` (7.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/profiles/light_and_mass_profiles.py` (62.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/profiles/mass.py` (6.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/_quick_fit.py` (0.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/interferometer.py` (0.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/queries.py` (6.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/aggregator/samples_via_aggregator.py` (8.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/latent_variables.py` (61.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/results/workflow/csv_make.py` (8.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/tracer.py` (9.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/units/cosmology.py` (10.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/units/flux.py` (53.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/guides/units/mass_to_light_ratio_units.py` (5.9s)
