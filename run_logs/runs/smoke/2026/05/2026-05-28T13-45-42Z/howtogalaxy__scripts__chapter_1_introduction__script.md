# Test Report: howtogalaxy / scripts/chapter_1_introduction (script)

**6 scripts** | 2 failed | 4 passed

| Status | Count |
|--------|-------|
| failed | 2 |
| passed | 4 |

## Failures

### `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_1_introduction/tutorial_0_visualization.py` — FAILED (0.0s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_1_introduction/tutorial_0_visualization.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_1_introduction/tutorial_0_visualization.py", line 38, in <module>
    dataset_path = Path("dataset", "imaging", "simple__sersic")
                   ^^^^
NameError: name 'Path' is not defined
```

### `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_1_introduction/tutorial_3_fitting.py` — FAILED (9.9s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_1_introduction/tutorial_3_fitting.py']' returned non-zero exit status 1.

```
    array_2d = ndarray_via_fits_from(file_path=file_path, hdu=hdu)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/fitsable.py", line 210, in ndarray_via_fits_from
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

## Passed

- `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_1_introduction/tutorial_1_grids_and_galaxies.py` (4.9s)
- `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_1_introduction/tutorial_2_data.py` (6.6s)
- `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_1_introduction/tutorial_4_methods.py` (0.2s)
- `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_1_introduction/tutorial_5_summary.py` (5.3s)
