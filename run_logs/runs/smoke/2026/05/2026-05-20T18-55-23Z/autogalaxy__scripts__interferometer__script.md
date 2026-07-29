# Test Report: autogalaxy / scripts/interferometer (script)

**22 scripts** | 1 failed | 20 passed | 1 skipped

| Status | Count |
|--------|-------|
| failed | 1 |
| passed | 20 |
| skipped | 1 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/multi_gaussian_expansion/likelihood_function.py` — FAILED (5.6s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/multi_gaussian_expansion/likelihood_function.py']' returned non-zero exit status 1.

```
    s_chol[P] = lstsq((ZTZ)[P][:, P], (ZTx)[P])
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/util/fnnls.py", line 31, in <lambda>
    lstsq = lambda A, x: slg.solve(
                         ^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/scipy/linalg/_basic.py", line 253, in solve
    _solve_check(n, info)
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/scipy/linalg/_basic.py", line 40, in _solve_check
    raise LinAlgError('Matrix is singular.')
numpy.linalg.LinAlgError: Matrix is singular.

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/multi_gaussian_expansion/likelihood_function.py", line 309, in <module>
    reconstruction = ag.util.inversion.reconstruction_positive_only_from(
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/inversion/inversion/inversion_util.py", line 334, in reconstruction_positive_only_from
    raise exc.InversionException() from e
autoarray.exc.InversionException
```

## Skipped

| Script | Reason |
|--------|--------|
| `modeling.py` | NEEDS_FIX 2026-04-10 - LinAlgError: matrix not positive definite in interferometer pixelization modeling |

## Passed

- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/extra_galaxies/simulator.py` (3.3s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/simulator.py` (5.4s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/start_here.py` (12.5s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/casa_reduction.py` (3.0s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/data_preparation.py` (9.3s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/extra_galaxies/modeling.py` (7.0s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/linear_light_profiles/fit.py` (6.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/linear_light_profiles/likelihood_function.py` (6.2s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/linear_light_profiles/modeling.py` (7.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/multi_gaussian_expansion/fit.py` (6.7s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/multi_gaussian_expansion/modeling.py` (10.3s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/pixelization/fit.py` (5.7s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/pixelization/likelihood_function.py` (4.2s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/pixelization/many_visibilities_preparation.py` (3.8s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/pixelization/source_science.py` (5.7s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/shapelets/fit.py` (7.2s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/shapelets/modeling.py` (32.7s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/fit.py` (5.9s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/likelihood_function.py` (5.7s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/modeling.py` (6.7s)
