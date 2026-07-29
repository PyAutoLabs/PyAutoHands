# Test Report: autolens_test / scripts/latent (script)

**2 scripts** | 2 failed

| Status | Count |
|--------|-------|
| failed | 2 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/latent/latent_nan_robustness.py` — FAILED (6.5s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/latent/latent_nan_robustness.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/latent/latent_nan_robustness.py", line 80, in <module>
    assert len(result.samples.sample_list) > LATENT_BATCH_SIZE, (
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'sample_list'
```

### `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/latent/latent_variables_smoke.py` — FAILED (5.5s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/latent/latent_variables_smoke.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/latent/latent_variables_smoke.py", line 66, in <module>
    latent_samples = analysis.compute_latent_samples(result.samples)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/analysis/analysis.py", line 144, in compute_latent_samples
    return latent_samples_from(self, samples, batch_size=batch_size)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/analysis/latent.py", line 113, in latent_samples_from
    latent.variables, analysis, model=samples.model
                                      ^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'model'
```
