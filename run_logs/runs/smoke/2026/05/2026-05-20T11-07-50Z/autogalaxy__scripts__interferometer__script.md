# Test Report: autogalaxy / scripts/interferometer (script)

**22 scripts** | 2 failed | 19 passed | 1 skipped

| Status | Count |
|--------|-------|
| failed | 2 |
| passed | 19 |
| skipped | 1 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/multi_gaussian_expansion/likelihood_function.py` — FAILED (10.2s)

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

### `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/pixelization/many_visibilities_preparation.py` — FAILED (4.0s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/pixelization/many_visibilities_preparation.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/pixelization/many_visibilities_preparation.py", line 165, in <module>
    dataset = dataset.apply_sparse_operator(
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/dataset/interferometer/dataset.py", line 262, in apply_sparse_operator
    raise NotImplementedError(
NotImplementedError: 
--------------------
`apply_sparse_operator` is not yet supported with the default `TransformerNUFFT` (nufftax-backed) transformer.

The sparse-operator path consumes the dirty image returned by `transformer.image_from(use_adjoint_scaling=True)` together with the NUFFT precision operator; their relative scale matters. The new `TransformerNUFFT` returns the strict mathematical adjoint (matching `TransformerDFT`), whereas the legacy pynufft adjoint applies an internal Kaiser-Bessel kernel deconvolution. The two scales differ by a non-constant factor, so feeding the new dirty image into the existing sparse-operator solver would silently give wrong answers.

Workarounds:
  - Build the dataset with `transformer_class=TransformerDFT` (the JAX-likelihood scripts do this today), or
  - Build the dataset with `transformer_class=TransformerNUFFTPyNUFFT` to keep the legacy pynufft adjoint scale (requires `pip install pynufft`).
----------------------
```

## Skipped

| Script | Reason |
|--------|--------|
| `modeling.py` | NEEDS_FIX 2026-04-10 - LinAlgError: matrix not positive definite in interferometer pixelization modeling |

## Passed

- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/extra_galaxies/simulator.py` (5.1s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/simulator.py` (9.2s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/start_here.py` (22.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/casa_reduction.py` (4.9s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/data_preparation.py` (16.2s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/extra_galaxies/modeling.py` (8.3s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/linear_light_profiles/fit.py` (10.9s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/linear_light_profiles/likelihood_function.py` (9.4s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/linear_light_profiles/modeling.py` (8.8s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/multi_gaussian_expansion/fit.py` (12.8s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/multi_gaussian_expansion/modeling.py` (19.3s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/pixelization/fit.py` (13.9s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/pixelization/likelihood_function.py` (9.0s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/pixelization/source_science.py` (6.8s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/shapelets/fit.py` (12.9s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/features/shapelets/modeling.py` (48.8s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/fit.py` (12.2s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/likelihood_function.py` (7.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace/scripts/interferometer/modeling.py` (8.5s)
