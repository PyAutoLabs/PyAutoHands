# Test Report: autolens_test / scripts/imaging (script)

**11 scripts** | 1 failed | 5 passed | 5 skipped

| Status | Count |
|--------|-------|
| failed | 1 |
| passed | 5 |
| skipped | 5 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/convolution_over_sampled.py` — FAILED (6.6s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/convolution_over_sampled.py']' returned non-zero exit status 1.

```
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:206: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autolens_workspace_test is compatible with the installed library version (2026.7.6.649): no `version.minimum_library_version` or `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
/home/jammy/Code/PyAutoLabs/PyAutoConf/autoconf/workspace.py:206: UserWarning: Cannot verify the workspace at /home/jammy/Code/PyAutoLabs/autolens_workspace_test is compatible with the installed library version (2026.7.6.649): no `version.minimum_library_version` or `version.workspace_version` key in config/general.yaml and no version.txt at the workspace root.

If you cloned the workspace from `main` rather than a release tag, set `version.workspace_version_check: False` in config/general.yaml to silence this warning. The `main` branch updates more frequently than library releases, so version mismatches are expected and not actionable for `main`-branch users.

You can also set the environment variable PYAUTO_SKIP_WORKSPACE_VERSION_CHECK=1 to disable temporarily.
  warnings.warn(_missing_version_warning(root, library_version))
/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/mask/mask_2d_util.py:564: UserWarning: Mask padded from (21, 21) to (np.int64(23), np.int64(23)) (parity preserved) to support kernel footprint (7, 7).
  warnings.warn(
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/convolution_over_sampled.py", line 384, in <module>
    assert raised == 3, f"expected 3 guard raises, got {raised}"
           ^^^^^^^^^^^
AssertionError: expected 3 guard raises, got 2
```

## Skipped

| Script | Reason |
|--------|--------|
| `modeling_visualization_jit.py` | SLOW 2026-05-07 - JIT + full visualization pipeline exceeds 300s cap (autogalaxy variant ~90s); unblocked by PR #70 from prior `expected jax.Array, got numpy.float64` AssertionError, now hits perf wall |
| `modeling_visualization_jit_delaunay.py` | SLOW 2026-05-07 - JIT + full visualization pipeline exceeds 300s cap (autogalaxy variant ~90s); unblocked by PR #70 from prior `expected jax.Array, got numpy.float64` AssertionError, now hits perf wall |
| `modeling_visualization_jit_rectangular.py` | SLOW 2026-05-07 - JIT + full visualization pipeline exceeds 300s cap (autogalaxy variant ~90s); unblocked by PR #70 from prior `expected jax.Array, got numpy.float64` AssertionError, now hits perf wall |
| `visualization.py` | NEEDS_FIX 2026-04-10 - AssertionError: dataset.png missing after visualization refactor |
| `visualization_jax.py` | NEEDS_FIX 2026-04-10 - AssertionError: dataset.png missing after visualization refactor |

## Passed

- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/simulator/no_lens_light.py` (5.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/simulator/with_lens_light.py` (6.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/simulator_use_jax_parity.py` (12.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/convolution.py` (9.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/imaging/model_fit.py` (10.3s)
