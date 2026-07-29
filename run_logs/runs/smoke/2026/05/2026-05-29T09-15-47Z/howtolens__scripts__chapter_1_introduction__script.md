# Test Report: howtolens / scripts/chapter_1_introduction (script)

**9 scripts** | 1 failed | 8 passed

| Status | Count |
|--------|-------|
| failed | 1 |
| passed | 8 |

## Failures

### `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_3_more_ray_tracing.py` — FAILED (4.7s)

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

## Passed

- `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_0_visualization.py` (4.3s)
- `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_1_grids_and_galaxies.py` (3.1s)
- `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_2_ray_tracing.py` (4.8s)
- `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_4_point_sources.py` (2.7s)
- `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_5_lensing_formalism.py` (2.7s)
- `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_6_data.py` (3.8s)
- `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_7_fitting.py` (5.7s)
- `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_1_introduction/tutorial_8_summary.py` (3.2s)
