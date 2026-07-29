# Test Report: autofit_test / scripts/searches (script)

**12 scripts** | 2 failed | 10 passed

| Status | Count |
|--------|-------|
| failed | 2 |
| passed | 10 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/searches/MultiStartProdigy.py` — FAILED (2.3s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/searches/MultiStartProdigy.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/searches/MultiStartProdigy.py", line 113, in <module>
    assert abs(instance.normalization - 25.0) < 3.0, instance.normalization
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 1.0
```

### `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/searches/MultiStartResurrect.py` — FAILED (2.4s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/searches/MultiStartResurrect.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/searches/MultiStartResurrect.py", line 94, in <module>
    f"sigma={off[2]:.3f}  (n_resurrections={info_off['n_resurrections']})"
                                            ~~~~~~~~^^^^^^^^^^^^^^^^^^^
KeyError: 'n_resurrections'
```

## Passed

- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/searches/BlackJAXNUTS.py` (20.0s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/searches/DynestyDynamic.py` (3.7s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/searches/DynestyStatic.py` (3.4s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/searches/Dynesty_jax.py` (2.6s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/searches/Emcee.py` (3.4s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/searches/LBFGS.py` (3.9s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/searches/MultiStartAdam.py` (21.5s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/searches/Nautilus.py` (2.8s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/searches/Nautilus_jax.py` (2.6s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace_test/scripts/searches/Zeus.py` (3.0s)
