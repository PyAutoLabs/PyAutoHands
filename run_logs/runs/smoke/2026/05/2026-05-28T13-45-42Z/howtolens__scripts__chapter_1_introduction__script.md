# Test Report: howtolens / scripts/chapter_1_introduction (script)

**9 scripts** | 3 failed | 6 passed

| Status | Count |
|--------|-------|
| failed | 3 |
| passed | 6 |

## Failures

### `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_0_visualization.py` — FAILED (0.2s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_0_visualization.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_0_visualization.py", line 41, in <module>
    dataset_path = Path("dataset") / "imaging" / "simple__no_lens_light"
                   ^^^^
NameError: name 'Path' is not defined
```

### `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_3_more_ray_tracing.py` — FAILED (3.8s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_3_more_ray_tracing.py']' returned non-zero exit status 1.

```
/home/jammy/Code/PyAutoLabs/PyAutoGalaxy/autogalaxy/profiles/mass/total/power_law.py:232: RuntimeWarning: invalid value encountered in divide
  * xp.divide(
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_3_more_ray_tracing.py", line 151, in <module>
    aplt.plot_grid(grid=tracer.traced_grid_2d_list_from(grid=grid)[1], title="Plane 1 Grid")
  File "/home/jammy/Code/PyAutoLabs/PyAutoGalaxy/autogalaxy/util/plot_utils.py", line 322, in plot_grid
    _aa_plot_grid(
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/plot/grid.py", line 181, in plot_grid
    apply_extent(ax, extent)
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/plot/utils.py", line 921, in apply_extent
    ax.set_xlim(xmin, xmax)
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/matplotlib/axes/_base.py", line 3739, in set_xlim
    return self.xaxis._set_lim(left, right, emit=emit, auto=auto)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/matplotlib/axis.py", line 1236, in _set_lim
    v0 = self.axes._validate_converted_limits(v0, self.convert_units)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/matplotlib/axes/_base.py", line 3660, in _validate_converted_limits
    raise ValueError("Axis limits cannot be NaN or Inf")
ValueError: Axis limits cannot be NaN or Inf
```

### `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_7_fitting.py` — FAILED (5.9s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_7_fitting.py']' returned non-zero exit status 1.

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
FileNotFoundError: [Errno 2] No such file or directory: 'dataset/imaging/simple__no_lens_light__mass_sis/data.fits'
```

## Passed

- `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_1_grids_and_galaxies.py` (4.3s)
- `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_2_ray_tracing.py` (3.8s)
- `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_4_point_sources.py` (3.4s)
- `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_5_lensing_formalism.py` (4.0s)
- `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_6_data.py` (5.3s)
- `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_8_summary.py` (6.9s)
