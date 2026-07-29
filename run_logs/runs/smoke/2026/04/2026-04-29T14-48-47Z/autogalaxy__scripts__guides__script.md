# Test Report: autogalaxy / scripts/guides (script)

**33 scripts** | 4 failed | 20 passed | 7 skipped | 2 timeout

| Status | Count |
|--------|-------|
| failed | 4 |
| passed | 20 |
| skipped | 7 |
| timeout | 2 |

## Failures

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/plot/start_here.py` — FAILED (8.6s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/plot/start_here.py']' returned non-zero exit status 1.

```
    array_2d = ndarray_via_fits_from(file_path=file_path, hdu=hdu)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoConf/autoconf/fitsable.py", line 210, in ndarray_via_fits_from
    hdu_list = fits.open(file_path, do_not_scale_image_data=do_not_scale_image_data)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/astropy/io/fits/hdu/hdulist.py", line 223, in fitsopen
    return HDUList.fromfile(
           ^^^^^^^^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/astropy/io/fits/hdu/hdulist.py", line 487, in fromfile
    return cls._readfrom(
           ^^^^^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/astropy/io/fits/hdu/hdulist.py", line 1169, in _readfrom
    fileobj = _File(
              ^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/astropy/io/fits/file.py", line 218, in __init__
    self._open_filename(fileobj, mode, overwrite)
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/astropy/io/fits/file.py", line 651, in _open_filename
    self._file = open(self.name, IO_FITS_MODES[mode])
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'dataset/imaging/simple/data.fits'
```

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/advanced/over_sampling.py` — FAILED (2.6s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/advanced/over_sampling.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/advanced/over_sampling.py", line 111, in <module>
    aplt.plot_grid(
TypeError: plot_grid() got an unexpected keyword argument 'plot_over_sampled_grid'
```

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/results/aggregator/galaxies_fit.py` — TIMEOUT (300.0s)

Timed out after 300s

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/results/aggregator/models.py` — FAILED (1.6s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/results/aggregator/models.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/results/aggregator/models.py", line 102, in <module>
    for dataset_list, galaxies_list in zip(dataset_gen, galaxies_gen):
                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoGalaxy/autogalaxy/aggregator/imaging/imaging.py", line 63, in _imaging_from
    mask, header = agg_util.mask_header_from(fit=fit)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoGalaxy/autogalaxy/aggregator/agg_util.py", line 101, in mask_header_from
    header = aa.Header(header_sci_obj=fit.value(name=name)[0].header)
                                      ~~~~~~~~~~~~~~~~~~~~^^^
TypeError: 'NoneType' object is not subscriptable
```

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/results/aggregator/samples.py` — TIMEOUT (300.0s)

Timed out after 300s

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/results/aggregator/samples_via_aggregator.py` — FAILED (3.0s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/results/aggregator/samples_via_aggregator.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/results/aggregator/samples_via_aggregator.py", line 146, in <module>
    print(samples.parameter_lists[0])
          ^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'parameter_lists'
```

## Skipped

| Script | Reason |
|--------|--------|
| `start_here.py` | SLOW 2026-04-10 - previously failed fast on a broken aggregator query; now runs the real aggregator and exceeds 60s |
| `start_here.py` | SLOW 2026-04-10 - exceeds 60s test timeout; unsets TEST_MODE to produce real samples for downstream examples |
| `searches.py` | Test mode breaks search visualization. |
| `data_fitting.py` | Test mode breaks .fits file output |
| `csv_make.py` | SLOW 2026-04-10 - exceeds 60s test timeout; unsets TEST_MODE for downstream examples |
| `fits_make.py` | Test mode does not output .fits images. |
| `png_make.py` | Test mode does not output .png images. |

## Passed

- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/plot/simulator.py` (6.4s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/results/database/simulators/light_sersic_exp__0.py` (4.5s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/results/database/simulators/light_sersic_exp__1.py` (4.7s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/results/database/simulators/light_sersic_exp__2.py` (4.7s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/data_structures.py` (3.5s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/galaxies.py` (5.1s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/hpc/example_cpu_and_gpu.py` (10.6s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/modeling/bug_fix.py` (6.7s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/modeling/chaining.py` (5.8s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/modeling/cookbook.py` (3.6s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/modeling/customize.py` (8.3s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/modeling/searches.py` (2.2s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/plot/advanced/plotters_pixelization.py` (16.9s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/plot/examples/mat_plot.py` (3.0s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/plot/examples/plotters.py` (5.2s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/plot/examples/visuals.py` (2.8s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/results/aggregator/interferometer.py` (0.0s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/results/aggregator/queries.py` (2.2s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/units/cosmology.py` (3.4s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/guides/units/flux.py` (16.5s)
