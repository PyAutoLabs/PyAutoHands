# Test Report: autofit / scripts/overview (script)

**3 scripts** | 1 failed | 2 passed

| Status | Count |
|--------|-------|
| failed | 1 |
| passed | 2 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autofit_workspace/scripts/overview/overview_1_the_basics.py` — FAILED (3.7s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autofit_workspace/scripts/overview/overview_1_the_basics.py']' returned non-zero exit status 1.

```
  g(x, I, \sigma) = \frac{N}{\sigma\sqrt{2\pi}} \exp{(-0.5 (x / \sigma)^2)}
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autofit_workspace/scripts/overview/overview_1_the_basics.py", line 839, in <module>
    result = search.fit(model=model, analysis=analysis)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/abstract_search.py", line 521, in fit
    result = self.start_resume_fit(
             ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/abstract_search.py", line 105, in decorated
    return func(self, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/abstract_search.py", line 670, in start_resume_fit
    return self._fit_bypass_test_mode(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/abstract_search.py", line 857, in _fit_bypass_test_mode
    analysis.log_likelihood_function(instance)
  File "/home/jammy/Code/PyAutoLabs/autofit_workspace/scripts/overview/overview_1_the_basics.py", line 813, in log_likelihood_function
    [profile_1d.model_data_from(xvalues=xvalues) for profile_1d in instance]
     ^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'str' object has no attribute 'model_data_from'
```

## Passed

- `/home/jammy/Code/PyAutoLabs/autofit_workspace/scripts/overview/overview_2_scientific_workflow.py` (4.1s)
- `/home/jammy/Code/PyAutoLabs/autofit_workspace/scripts/overview/overview_3_statistical_methods.py` (0.1s)
