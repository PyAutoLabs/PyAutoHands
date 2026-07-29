# Test Report: autolens / scripts/point_source (script)

**11 scripts** | 3 failed | 5 passed | 3 skipped

| Status | Count |
|--------|-------|
| failed | 3 |
| passed | 5 |
| skipped | 3 |

## Failures

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/point_source/features/deblending/simulator.py` — FAILED (3.7s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/point_source/features/deblending/simulator.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/point_source/features/deblending/simulator.py", line 265, in <module>
    centre=positions[2], intensity=fluxes[2], sigma=psf_sigma
           ~~~~~~~~~^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/abstract_ndarray.py", line 391, in __getitem__
    result = self._array[item]
             ~~~~~~~~~~~^^^^^^
IndexError: index 2 is out of bounds for axis 0 with size 2
```

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/point_source/features/deblending/modeling.py` — FAILED (2.0s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/point_source/features/deblending/modeling.py']' returned non-zero exit status 1.

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
FileNotFoundError: [Errno 2] No such file or directory: 'dataset/point_source/deblending/data.fits'
```

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/point_source/fit.py` — FAILED (3.6s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/point_source/fit.py']' returned non-zero exit status 1.

```
                ^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/fit/fit_dataset.py", line 87, in chi_squared
    chi_squared_map=self.chi_squared_map.array, xp=self._xp
                    ^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/fit/fit_dataset.py", line 77, in chi_squared_map
    return fit_util.chi_squared_map_from(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/fit/fit_util.py", line 78, in chi_squared_map_from
    return (residual_map / noise_map) ** 2.0
            ~~~~~~~~~~~~~^~~~~~~~~~~
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/abstract_ndarray.py", line 35, in wrapper
    return self.with_new_array(func(self, *args, **kwargs))
                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/abstract_ndarray.py", line 57, in wrapper
    return func(self, other.array)
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/abstract_ndarray.py", line 326, in __truediv__
    return self._array / other
           ~~~~~~~~~~~~^~~~~~~
ValueError: operands could not be broadcast together with shapes (2,) (4,)
```

## Skipped

| Script | Reason |
|--------|--------|
| `simulator.py` | Blocked by PyAutoLens #480: solver finds 0 positions for intermediate-plane source |
| `modeling.py` | Blocked by PyAutoLens #480: same root cause as simulator above |
| `time_delays.py` | Test mode does not support cosmology ift |

## Passed

- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/point_source/simulator.py` (4.9s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/point_source/simulator_sample.py` (7.8s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/point_source/start_here.py` (14.3s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/point_source/features/fluxes.py` (10.7s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/point_source/modeling.py` (6.2s)
