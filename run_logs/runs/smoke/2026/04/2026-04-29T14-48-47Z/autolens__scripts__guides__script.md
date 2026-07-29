# Test Report: autolens / scripts/guides (script)

**41 scripts** | 7 failed | 25 passed | 6 skipped | 3 timeout

| Status | Count |
|--------|-------|
| failed | 7 |
| passed | 25 |
| skipped | 6 |
| timeout | 3 |

## Failures

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/results/start_here.py` — TIMEOUT (300.0s)

Timed out after 300s

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/data_structures.py` — FAILED (2.2s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/data_structures.py']' returned non-zero exit status 1.

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

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/modeling/bug_fix.py` — FAILED (2.5s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/modeling/bug_fix.py']' returned non-zero exit status 1.

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

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/modeling/chaining.py` — FAILED (1.8s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/modeling/chaining.py']' returned non-zero exit status 1.

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

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/plot/examples/plotters.py` — FAILED (16.3s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/plot/examples/plotters.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/plot/examples/plotters.py", line 351, in <module>
    dataset = al.from_json(
              ^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoConf/autoconf/dictable.py", line 364, in from_json
    with open(file_path, "r+") as f:
         ^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'dataset/point_source/simple/point_dataset_positions_only.json'
```

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/results/aggregator/galaxies_fits.py` — TIMEOUT (300.0s)

Timed out after 300s

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/results/aggregator/models.py` — FAILED (1.7s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/results/aggregator/models.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/results/aggregator/models.py", line 91, in <module>
    for dataset_list, tracer_list in zip(dataset_gen, tracer_gen):
                                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoGalaxy/autogalaxy/aggregator/imaging/imaging.py", line 63, in _imaging_from
    mask, header = agg_util.mask_header_from(fit=fit)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoGalaxy/autogalaxy/aggregator/agg_util.py", line 101, in mask_header_from
    header = aa.Header(header_sci_obj=fit.value(name=name)[0].header)
                                      ~~~~~~~~~~~~~~~~~~~~^^^
TypeError: 'NoneType' object is not subscriptable
```

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/results/aggregator/queries.py` — FAILED (2.9s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/results/aggregator/queries.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/results/aggregator/queries.py", line 119, in <module>
    agg_query = agg.query(bulge.sersic_index < 3.0)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoFit/autofit/aggregator/aggregator.py", line 271, in query
    search_outputs = list(search_outputs)
                     ^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoFit/autofit/aggregator/predicate.py", line 128, in <lambda>
    lambda search_output: self(search_output),
                          ^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoFit/autofit/aggregator/predicate.py", line 285, in __call__
    return self.attribute_predicate.value_for_search_output(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoFit/autofit/aggregator/predicate.py", line 35, in value_for_search_output
    value = getattr(
            ^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoFit/autofit/mapper/prior_model/prior_model.py", line 422, in __getattr__
    self.__getattribute__(item)
AttributeError: 'Model' object has no attribute 'sersic_index'
```

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/results/aggregator/samples.py` — TIMEOUT (300.0s)

Timed out after 300s

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/results/aggregator/samples_via_aggregator.py` — FAILED (3.2s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/results/aggregator/samples_via_aggregator.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/results/aggregator/samples_via_aggregator.py", line 143, in <module>
    print(samples.parameter_lists[0])
          ^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'parameter_lists'
```

## Skipped

| Script | Reason |
|--------|--------|
| `start_here.py` | SLOW 2026-04-10 - previously failed fast on a broken aggregator query; now runs the real aggregator and exceeds 60s |
| `example_cpu.py` | HPC paths dont exist locally. |
| `searches.py` | Test mode breaks search visualization. |
| `data_fitting.py` | Test mode breaks .fits file output |
| `fits_make.py` | Test mode does not output .fits images. |
| `png_make.py` | Test mode does not output .png images. |

## Passed

- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/plot/start_here.py` (10.9s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/advanced/add_a_profile.py` (3.3s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/advanced/custom_analysis.py` (4.1s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/advanced/multi_plane.py` (1.5s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/advanced/over_sampling.py` (3.4s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/advanced/over_sampling_chaining.py` (7.3s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/galaxies.py` (3.9s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/lens_calc.py` (5.7s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/modeling/advanced/expectation_propagation.py` (20.3s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/modeling/advanced/graphical.py` (45.7s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/modeling/advanced/hierarchical.py` (5.1s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/modeling/cookbook.py` (4.0s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/modeling/customize.py` (4.3s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/modeling/searches.py` (2.4s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/modeling/slam_start_here.py` (25.1s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/plot/advanced/plotters_double_einstein_ring.py` (14.0s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/plot/advanced/plotters_pixelization.py` (135.9s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/plot/examples/mat_plot.py` (3.0s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/plot/examples/visuals.py` (3.9s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/results/aggregator/interferometer.py` (0.0s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/results/workflow/csv_make.py` (144.8s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/tracer.py` (6.5s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/units/cosmology.py` (4.4s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/units/flux.py` (43.9s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/guides/units/mass_to_light_ratio_units.py` (4.1s)
