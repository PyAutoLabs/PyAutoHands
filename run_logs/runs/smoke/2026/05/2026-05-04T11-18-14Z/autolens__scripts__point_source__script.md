# Test Report: autolens / scripts/point_source (script)

**11 scripts** | 1 failed | 7 passed | 3 skipped

| Status | Count |
|--------|-------|
| failed | 1 |
| passed | 7 |
| skipped | 3 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/point_source/fit.py` — FAILED (8.0s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/point_source/fit.py']' returned non-zero exit status 1.

```
                ^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/fit/fit_dataset.py", line 87, in chi_squared
    chi_squared_map=self.chi_squared_map.array, xp=self._xp
                    ^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/fit/fit_dataset.py", line 77, in chi_squared_map
    return fit_util.chi_squared_map_from(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/fit/fit_util.py", line 78, in chi_squared_map_from
    return (residual_map / noise_map) ** 2.0
            ~~~~~~~~~~~~~^~~~~~~~~~~
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/abstract_ndarray.py", line 35, in wrapper
    return self.with_new_array(func(self, *args, **kwargs))
                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/abstract_ndarray.py", line 57, in wrapper
    return func(self, other.array)
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/abstract_ndarray.py", line 326, in __truediv__
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

- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/point_source/features/deblending/simulator.py` (12.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/point_source/simulator.py` (10.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/point_source/simulator_sample.py` (17.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/point_source/start_here.py` (47.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/point_source/features/deblending/modeling.py` (16.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/point_source/features/fluxes.py` (30.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/point_source/modeling.py` (16.3s)
