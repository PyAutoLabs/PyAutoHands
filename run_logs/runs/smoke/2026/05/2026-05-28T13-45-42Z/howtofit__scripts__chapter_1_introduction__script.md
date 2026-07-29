# Test Report: howtofit / scripts/chapter_1_introduction (script)

**6 scripts** | 1 failed | 4 passed | 1 skipped

| Status | Count |
|--------|-------|
| failed | 1 |
| passed | 4 |
| skipped | 1 |

## Failures

### `/home/jammy/Code/PyAutoLabs/HowToFit/scripts/chapter_1_introduction/tutorial_4_why_modeling_is_hard.py` — FAILED (5.5s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToFit/scripts/chapter_1_introduction/tutorial_4_why_modeling_is_hard.py']' returned non-zero exit status 1.

```
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
  File "/home/jammy/Code/PyAutoLabs/HowToFit/scripts/chapter_1_introduction/tutorial_4_why_modeling_is_hard.py", line 250, in log_likelihood_function
    model_data = self.model_data_from_instance(instance=instance)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/HowToFit/scripts/chapter_1_introduction/tutorial_4_why_modeling_is_hard.py", line 282, in model_data_from_instance
    return sum([profile.model_data_from(xvalues=xvalues) for profile in instance])
                ^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'str' object has no attribute 'model_data_from'
```

## Skipped

| Script | Reason |
|--------|--------|
| `tutorial_5_results_and_samples.py` | NEEDS_FIX 2026-04-10 - IndexError in samples access, likely related to InstanceInterpolator bug in autofit features/interpolate |

## Passed

- `/home/jammy/Code/PyAutoLabs/HowToFit/scripts/chapter_1_introduction/start_here.py` (0.0s)
- `/home/jammy/Code/PyAutoLabs/HowToFit/scripts/chapter_1_introduction/tutorial_1_models.py` (2.8s)
- `/home/jammy/Code/PyAutoLabs/HowToFit/scripts/chapter_1_introduction/tutorial_2_fitting_data.py` (24.5s)
- `/home/jammy/Code/PyAutoLabs/HowToFit/scripts/chapter_1_introduction/tutorial_3_non_linear_search.py` (5.2s)
