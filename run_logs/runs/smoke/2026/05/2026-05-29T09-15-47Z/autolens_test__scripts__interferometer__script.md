# Test Report: autolens_test / scripts/interferometer (script)

**8 scripts** | 2 failed | 5 passed | 1 skipped

| Status | Count |
|--------|-------|
| failed | 2 |
| passed | 5 |
| skipped | 1 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/simulator_use_jax_parity.py` — FAILED (9.2s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/simulator_use_jax_parity.py']' returned non-zero exit status 1.

```
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:173: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autolens_workspace_test matches the installed library version (2026.5.21.1): no `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:173: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autolens_workspace_test matches the installed library version (2026.5.21.1): no `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/simulator_use_jax_parity.py", line 91, in <module>
    al.util.register_tracer_classes(tracer)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: module 'autolens.util' has no attribute 'register_tracer_classes'
```

### `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/visualization_jax.py` — FAILED (121.7s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/visualization_jax.py']' returned non-zero exit status 1.

```
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:173: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autolens_workspace_test matches the installed library version (2026.5.21.1): no `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:173: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autolens_workspace_test matches the installed library version (2026.5.21.1): no `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/visualization_jax.py", line 179, in <module>
    assert _warm_dt < 0.1, (
           ^^^^^^^^^^^^^^
AssertionError: zero_contour warm call took 155.3 ms (> 100 ms) — closure cache-busting bug from PyAutoGalaxy #433 may have regressed
```

## Skipped

| Script | Reason |
|--------|--------|
| `modeling_visualization_jit.py` | SLOW 2026-05-20 - JIT + full visualization pipeline exceeds 300s cap; same root cause as imaging/modeling_visualization_jit family |

## Passed

- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/simulator/no_lens_light.py` (4.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/simulator/with_lens_light.py` (5.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/model_fit.py` (8.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/nufft.py` (13.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/interferometer/visualization.py` (65.4s)
