# Test Report: autolens_test / scripts/jax_substructure (script)

**3 scripts** | 2 failed | 1 passed

| Status | Count |
|--------|-------|
| failed | 2 |
| passed | 1 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_substructure/test_batched_simulate.py` — FAILED (7.7s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_substructure/test_batched_simulate.py']' returned non-zero exit status 1.

```
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:173: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autolens_workspace_test matches the installed library version (2026.5.21.1): no `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_substructure/test_batched_simulate.py", line 174, in <module>
    img = substructure_util.simulate_substructure(
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoLens/autolens/lens/substructure_util.py", line 168, in simulate_substructure
    image_2d = image_1d.reshape(image_shape)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/jax/_src/numpy/array_methods.py", line 316, in _reshape
    newshape = _compute_newshape(self, args[0] if len(args) == 1 else args)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/jax/_src/numpy/array_methods.py", line 481, in _compute_newshape
    raise TypeError(f"cannot reshape array of shape {arr.shape} (size {arr.size}) "
TypeError: cannot reshape array of shape (225,) (size 225) into shape (41, 41) (size 1681)
```

### `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_substructure/test_simulate_e2e.py` — FAILED (10.2s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_substructure/test_simulate_e2e.py']' returned non-zero exit status 1.

```
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:173: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autolens_workspace_test matches the installed library version (2026.5.21.1): no `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_substructure/test_simulate_e2e.py", line 169, in <module>
    image_scan = substructure_util.simulate_substructure(
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoLens/autolens/lens/substructure_util.py", line 168, in simulate_substructure
    image_2d = image_1d.reshape(image_shape)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/jax/_src/numpy/array_methods.py", line 316, in _reshape
    newshape = _compute_newshape(self, args[0] if len(args) == 1 else args)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/jax/_src/numpy/array_methods.py", line 481, in _compute_newshape
    raise TypeError(f"cannot reshape array of shape {arr.shape} (size {arr.size}) "
TypeError: cannot reshape array of shape (225,) (size 225) into shape (51, 51) (size 2601)
```

## Passed

- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/jax_substructure/test_scan_multiplane.py` (6.7s)
