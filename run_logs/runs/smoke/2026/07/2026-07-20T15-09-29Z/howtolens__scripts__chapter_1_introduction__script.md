# Test Report: howtolens / scripts/chapter_1_introduction (script)

**9 scripts** | 2 failed | 7 passed

| Status | Count |
|--------|-------|
| failed | 2 |
| passed | 7 |

## Failures

### `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_0_visualization.py` — FAILED (3.4s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_0_visualization.py']' returned non-zero exit status 1.

```
    array_2d = ndarray_via_fits_from(file_path=file_path, hdu=hdu)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoNerves/autonerves/fitsable.py", line 210, in ndarray_via_fits_from
    hdu_list = fits.open(file_path, do_not_scale_image_data=do_not_scale_image_data)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/astropy/io/fits/hdu/hdulist.py", line 227, in fitsopen
    return HDUList.fromfile(
           ^^^^^^^^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/astropy/io/fits/hdu/hdulist.py", line 491, in fromfile
    return cls._readfrom(
           ^^^^^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/astropy/io/fits/hdu/hdulist.py", line 1193, in _readfrom
    fileobj = _File(
              ^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/astropy/io/fits/file.py", line 239, in __init__
    self._open_filename(fileobj, mode, overwrite)
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/astropy/io/fits/file.py", line 711, in _open_filename
    self._file = open(self.name, IO_FITS_MODES[mode])
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'dataset/imaging/simple__no_lens_light/data.fits'
```

### `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_7_fitting.py` — FAILED (7.1s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_7_fitting.py']' returned non-zero exit status 1.

```
    array_2d = ndarray_via_fits_from(file_path=file_path, hdu=hdu)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoNerves/autonerves/fitsable.py", line 210, in ndarray_via_fits_from
    hdu_list = fits.open(file_path, do_not_scale_image_data=do_not_scale_image_data)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/astropy/io/fits/hdu/hdulist.py", line 227, in fitsopen
    return HDUList.fromfile(
           ^^^^^^^^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/astropy/io/fits/hdu/hdulist.py", line 491, in fromfile
    return cls._readfrom(
           ^^^^^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/astropy/io/fits/hdu/hdulist.py", line 1193, in _readfrom
    fileobj = _File(
              ^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/astropy/io/fits/file.py", line 239, in __init__
    self._open_filename(fileobj, mode, overwrite)
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/astropy/io/fits/file.py", line 711, in _open_filename
    self._file = open(self.name, IO_FITS_MODES[mode])
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'dataset/imaging/simple__no_lens_light__mass_sis/data.fits'
```

## Passed

- `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_1_grids_and_galaxies.py` (5.4s)
- `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_2_ray_tracing.py` (4.6s)
- `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_3_more_ray_tracing.py` (5.1s)
- `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_4_point_sources.py` (5.8s)
- `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_5_lensing_formalism.py` (6.0s)
- `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_6_data.py` (6.3s)
- `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_8_summary.py` (4.0s)
