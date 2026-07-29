# Test Report: autogalaxy_test / scripts/jax_likelihood_functions (script)

**30 scripts** | 18 failed | 12 passed

| Status | Count |
|--------|-------|
| failed | 18 |
| passed | 12 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/ellipse/fit.py` — FAILED (7.2s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/ellipse/fit.py']' returned non-zero exit status 1.

```
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:173: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test matches the installed library version (2026.5.21.1): no `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/ellipse/fit.py", line 138, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisEllipse.fit_from of <autogalaxy.ellipse.model.analysis.AnalysisEllipse object at 0x7fc18ea84410>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
```

### `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/ellipse/multipoles.py` — FAILED (6.4s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/ellipse/multipoles.py']' returned non-zero exit status 1.

```
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:173: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test matches the installed library version (2026.5.21.1): no `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/ellipse/multipoles.py", line 150, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisEllipse.fit_from of <autogalaxy.ellipse.model.analysis.AnalysisEllipse object at 0x7f6249efcec0>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
```

### `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/ellipse/multipoles_scaled.py` — FAILED (6.2s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/ellipse/multipoles_scaled.py']' returned non-zero exit status 1.

```
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:173: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test matches the installed library version (2026.5.21.1): no `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/ellipse/multipoles_scaled.py", line 152, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisEllipse.fit_from of <autogalaxy.ellipse.model.analysis.AnalysisEllipse object at 0x7f3929d87890>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
```

### `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/delaunay.py` — FAILED (13.7s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/delaunay.py']' returned non-zero exit status 1.

```
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:173: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test matches the installed library version (2026.5.21.1): no `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/delaunay.py", line 175, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisImaging.fit_from of <autogalaxy.imaging.model.analysis.AnalysisImaging object at 0x7f033c2a4bc0>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
```

### `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/delaunay_mge.py` — FAILED (47.3s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/delaunay_mge.py']' returned non-zero exit status 1.

```
/home/jammy/venv/PyAuto/lib/python3.12/site-packages/google/protobuf/runtime_version.py:98: UserWarning: Protobuf gencode version 5.28.3 is exactly one major version older than the runtime version 6.31.1 at tensorflow/core/framework/cost_graph.proto. Please update the gencode to avoid compatibility violations in the next runtime release.
  warnings.warn(
/home/jammy/venv/PyAuto/lib/python3.12/site-packages/google/protobuf/runtime_version.py:98: UserWarning: Protobuf gencode version 5.28.3 is exactly one major version older than the runtime version 6.31.1 at tensorflow/core/framework/step_stats.proto. Please update the gencode to avoid compatibility violations in the next runtime release.
  warnings.warn(
/home/jammy/venv/PyAuto/lib/python3.12/site-packages/google/protobuf/runtime_version.py:98: UserWarning: Protobuf gencode version 5.28.3 is exactly one major version older than the runtime version 6.31.1 at tensorflow/core/framework/allocation_description.proto. Please update the gencode to avoid compatibility violations in the next runtime release.
  warnings.warn(
/home/jammy/venv/PyAuto/lib/python3.12/site-packages/google/protobuf/runtime_version.py:98: UserWarning: Protobuf gencode version 5.28.3 is exactly one major version older than the runtime version 6.31.1 at tensorflow/core/framework/tensor_description.proto. Please update the gencode to avoid compatibility violations in the next runtime release.
  warnings.warn(
/home/jammy/venv/PyAuto/lib/python3.12/site-packages/google/protobuf/runtime_version.py:98: UserWarning: Protobuf gencode version 5.28.3 is exactly one major version older than the runtime version 6.31.1 at tensorflow/core/protobuf/cluster.proto. Please update the gencode to avoid compatibility violations in the next runtime release.
  warnings.warn(
/home/jammy/venv/PyAuto/lib/python3.12/site-packages/google/protobuf/runtime_version.py:98: UserWarning: Protobuf gencode version 5.28.3 is exactly one major version older than the runtime version 6.31.1 at tensorflow/core/protobuf/debug.proto. Please update the gencode to avoid compatibility violations in the next runtime release.
  warnings.warn(
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/delaunay_mge.py", line 192, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisImaging.fit_from of <autogalaxy.imaging.model.analysis.AnalysisImaging object at 0x7fd45acccbf0>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
```

### `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/lp.py` — FAILED (5.5s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/lp.py']' returned non-zero exit status 1.

```
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:173: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test matches the installed library version (2026.5.21.1): no `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/lp.py", line 117, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisImaging.fit_from of <autogalaxy.imaging.model.analysis.AnalysisImaging object at 0x7f77e14450d0>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
```

### `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/mge.py` — FAILED (13.6s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/mge.py']' returned non-zero exit status 1.

```
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:173: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test matches the installed library version (2026.5.21.1): no `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/mge.py", line 130, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisImaging.fit_from of <autogalaxy.imaging.model.analysis.AnalysisImaging object at 0x7f2e777fb950>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
```

### `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/mge_group.py` — FAILED (38.5s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/mge_group.py']' returned non-zero exit status 1.

```
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:173: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test matches the installed library version (2026.5.21.1): no `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/mge_group.py", line 192, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisImaging.fit_from of <autogalaxy.imaging.model.analysis.AnalysisImaging object at 0x7fb20078ec60>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
```

### `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular.py` — FAILED (10.7s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular.py']' returned non-zero exit status 1.

```
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:173: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test matches the installed library version (2026.5.21.1): no `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular.py", line 158, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisImaging.fit_from of <autogalaxy.imaging.model.analysis.AnalysisImaging object at 0x7f06bf6333e0>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
```

### `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_mge.py` — FAILED (25.9s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_mge.py']' returned non-zero exit status 1.

```
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:173: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test matches the installed library version (2026.5.21.1): no `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/rectangular_mge.py", line 169, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisImaging.fit_from of <autogalaxy.imaging.model.analysis.AnalysisImaging object at 0x7fa1993110d0>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
```

### `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/delaunay.py` — FAILED (14.5s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/delaunay.py']' returned non-zero exit status 1.

```
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:173: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test matches the installed library version (2026.5.21.1): no `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/delaunay.py", line 182, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisInterferometer.fit_from of <autogalaxy.interferometer.model.analysis.AnalysisInterferometer object at 0x7f842028e090>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
```

### `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/delaunay_mge.py` — FAILED (38.4s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/delaunay_mge.py']' returned non-zero exit status 1.

```
/home/jammy/venv/PyAuto/lib/python3.12/site-packages/google/protobuf/runtime_version.py:98: UserWarning: Protobuf gencode version 5.28.3 is exactly one major version older than the runtime version 6.31.1 at tensorflow/core/framework/cost_graph.proto. Please update the gencode to avoid compatibility violations in the next runtime release.
  warnings.warn(
/home/jammy/venv/PyAuto/lib/python3.12/site-packages/google/protobuf/runtime_version.py:98: UserWarning: Protobuf gencode version 5.28.3 is exactly one major version older than the runtime version 6.31.1 at tensorflow/core/framework/step_stats.proto. Please update the gencode to avoid compatibility violations in the next runtime release.
  warnings.warn(
/home/jammy/venv/PyAuto/lib/python3.12/site-packages/google/protobuf/runtime_version.py:98: UserWarning: Protobuf gencode version 5.28.3 is exactly one major version older than the runtime version 6.31.1 at tensorflow/core/framework/allocation_description.proto. Please update the gencode to avoid compatibility violations in the next runtime release.
  warnings.warn(
/home/jammy/venv/PyAuto/lib/python3.12/site-packages/google/protobuf/runtime_version.py:98: UserWarning: Protobuf gencode version 5.28.3 is exactly one major version older than the runtime version 6.31.1 at tensorflow/core/framework/tensor_description.proto. Please update the gencode to avoid compatibility violations in the next runtime release.
  warnings.warn(
/home/jammy/venv/PyAuto/lib/python3.12/site-packages/google/protobuf/runtime_version.py:98: UserWarning: Protobuf gencode version 5.28.3 is exactly one major version older than the runtime version 6.31.1 at tensorflow/core/protobuf/cluster.proto. Please update the gencode to avoid compatibility violations in the next runtime release.
  warnings.warn(
/home/jammy/venv/PyAuto/lib/python3.12/site-packages/google/protobuf/runtime_version.py:98: UserWarning: Protobuf gencode version 5.28.3 is exactly one major version older than the runtime version 6.31.1 at tensorflow/core/protobuf/debug.proto. Please update the gencode to avoid compatibility violations in the next runtime release.
  warnings.warn(
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/delaunay_mge.py", line 192, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisInterferometer.fit_from of <autogalaxy.interferometer.model.analysis.AnalysisInterferometer object at 0x7f82f086f4a0>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
```

### `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/lp.py` — FAILED (8.1s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/lp.py']' returned non-zero exit status 1.

```
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:173: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test matches the installed library version (2026.5.21.1): no `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/lp.py", line 122, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisInterferometer.fit_from of <autogalaxy.interferometer.model.analysis.AnalysisInterferometer object at 0x7f4b5832de80>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
```

### `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/mge.py` — FAILED (16.6s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/mge.py']' returned non-zero exit status 1.

```
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:173: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test matches the installed library version (2026.5.21.1): no `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/mge.py", line 128, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisInterferometer.fit_from of <autogalaxy.interferometer.model.analysis.AnalysisInterferometer object at 0x7fea3c264a10>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
```

### `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/mge_group.py` — FAILED (36.7s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/mge_group.py']' returned non-zero exit status 1.

```
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:173: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test matches the installed library version (2026.5.21.1): no `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/mge_group.py", line 193, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisInterferometer.fit_from of <autogalaxy.interferometer.model.analysis.AnalysisInterferometer object at 0x7f45a0acc9b0>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
```

### `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular.py` — FAILED (12.3s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular.py']' returned non-zero exit status 1.

```
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:173: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test matches the installed library version (2026.5.21.1): no `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular.py", line 155, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisInterferometer.fit_from of <autogalaxy.interferometer.model.analysis.AnalysisInterferometer object at 0x7feaee6be720>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
```

### `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular_mge.py` — FAILED (22.4s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular_mge.py']' returned non-zero exit status 1.

```
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:173: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test matches the installed library version (2026.5.21.1): no `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/rectangular_mge.py", line 164, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisInterferometer.fit_from of <autogalaxy.interferometer.model.analysis.AnalysisInterferometer object at 0x7effa96f43b0>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
```

### `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/light_multipole/multipole.py` — FAILED (10.2s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/light_multipole/multipole.py']' returned non-zero exit status 1.

```
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:173: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test matches the installed library version (2026.5.21.1): no `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/light_multipole/multipole.py", line 132, in <module>
    fit = fit_jit_fn(instance)
          ^^^^^^^^^^^^^^^^^^^^
TypeError: Error interpreting argument to <bound method AnalysisImaging.fit_from of <autogalaxy.imaging.model.analysis.AnalysisImaging object at 0x7ff071f3f3e0>> as an abstract array. The problematic value is of type <class 'autofit.mapper.model.ModelInstance'> and was passed to the function at path instance.
This typically means that a jit-wrapped function was called with a non-array argument, and this argument was not marked as static using the static_argnums or static_argnames parameters of jax.jit.
--------------------
For simplicity, JAX has removed its internal frames from the traceback of the following exception. Set JAX_TRACEBACK_FILTERING=off to include these.
```

## Passed

- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/ellipse/simulator.py` (4.0s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/imaging/simulator.py` (8.8s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/interferometer/simulator.py` (13.3s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/multi/simulator.py` (8.5s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/multi/dataset_model.py` (9.9s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/multi/delaunay.py` (28.6s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/multi/delaunay_mge.py` (76.8s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/multi/lp.py` (10.1s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/multi/mge.py` (28.0s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/multi/mge_group.py` (55.9s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/multi/rectangular.py` (20.9s)
- `/home/jammy/Code/PyAutoLabs/autogalaxy_workspace_test/scripts/jax_likelihood_functions/multi/rectangular_mge.py` (43.2s)
