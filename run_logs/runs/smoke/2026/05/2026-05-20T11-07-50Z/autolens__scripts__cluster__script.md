# Test Report: autolens / scripts/cluster (script)

**5 scripts** | 2 failed | 3 passed

| Status | Count |
|--------|-------|
| failed | 2 |
| passed | 3 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/cluster/start_here.py` — FAILED (10.1s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/cluster/start_here.py']' returned non-zero exit status 1.

```
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/mapper/prior_model/abstract.py", line 1418, in instance_for_arguments
    return self._instance_for_arguments(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/mapper/prior_model/collection.py", line 293, in _instance_for_arguments
    value = value.instance_for_arguments(
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/mapper/prior_model/abstract.py", line 1418, in instance_for_arguments
    return self._instance_for_arguments(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/mapper/prior_model/prior_model.py", line 462, in _instance_for_arguments
    ] = prior_model.instance_for_arguments(
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/mapper/prior_model/abstract.py", line 1418, in instance_for_arguments
    return self._instance_for_arguments(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/mapper/prior_model/prior_model.py", line 495, in _instance_for_arguments
    result = self.cls(**constructor_arguments)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: Point.__init__() got an unexpected keyword argument 'centre_0'
```

### `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/cluster/modeling.py` — FAILED (12.5s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/cluster/modeling.py']' returned non-zero exit status 1.

```
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/mapper/prior_model/abstract.py", line 1418, in instance_for_arguments
    return self._instance_for_arguments(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/mapper/prior_model/collection.py", line 293, in _instance_for_arguments
    value = value.instance_for_arguments(
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/mapper/prior_model/abstract.py", line 1418, in instance_for_arguments
    return self._instance_for_arguments(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/mapper/prior_model/prior_model.py", line 462, in _instance_for_arguments
    ] = prior_model.instance_for_arguments(
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/mapper/prior_model/abstract.py", line 1418, in instance_for_arguments
    return self._instance_for_arguments(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/mapper/prior_model/prior_model.py", line 495, in _instance_for_arguments
    result = self.cls(**constructor_arguments)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: Point.__init__() got an unexpected keyword argument 'centre_0'
```

## Passed

- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/cluster/simulator.py` (9.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/cluster/csv_api.py` (4.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/cluster/likelihood_function.py` (4.6s)
