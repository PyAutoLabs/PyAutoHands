# Test Report: autofit_test / scripts/jax_assertions (script)

**9 scripts** | 1 failed | 8 passed

| Status | Count |
|--------|-------|
| failed | 1 |
| passed | 8 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/jax_assertions/multi_start_gradient_auto_convergence.py` — FAILED (4.8s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/jax_assertions/multi_start_gradient_auto_convergence.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/jax_assertions/multi_start_gradient_auto_convergence.py", line 105, in <module>
    total_steps = int(result.samples.samples_info["total_steps"])
                      ~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^
KeyError: 'total_steps'
```

## Passed

- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/jax_assertions/enable_pytrees.py` (3.3s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/jax_assertions/fitness_dispatch.py` (3.7s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/jax_assertions/fitness_nan_gradient_contract.py` (2.1s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/jax_assertions/nested.py` (2.8s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/jax_assertions/priors_xp_dispatch.py` (5.7s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/jax_assertions/pytree_leaf_registration.py` (2.7s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/jax_assertions/pytrees.py` (3.5s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/jax_assertions/shared_state.py` (4.2s)
