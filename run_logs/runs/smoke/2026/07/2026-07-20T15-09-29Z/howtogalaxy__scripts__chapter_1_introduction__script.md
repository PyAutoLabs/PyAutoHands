# Test Report: howtogalaxy / scripts/chapter_1_introduction (script)

**6 scripts** | 1 failed | 5 passed

| Status | Count |
|--------|-------|
| failed | 1 |
| passed | 5 |

## Failures

### `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_1_introduction/tutorial_3_fitting.py` — FAILED (4.7s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_1_introduction/tutorial_3_fitting.py']' returned non-zero exit status 1.

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
FileNotFoundError: [Errno 2] No such file or directory: 'dataset/imaging/simple/data.fits'
```

## Passed

- `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_1_introduction/tutorial_0_visualization.py` (6.9s)
- `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_1_introduction/tutorial_1_grids_and_galaxies.py` (3.7s)
- `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_1_introduction/tutorial_2_data.py` (4.2s)
- `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_1_introduction/tutorial_4_methods.py` (3.0s)
- `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_1_introduction/tutorial_5_summary.py` (3.3s)
