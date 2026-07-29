# Test Report: howtolens / scripts/chapter_2_lens_modeling (script)

**8 scripts** | 2 failed | 6 passed

| Status | Count |
|--------|-------|
| failed | 2 |
| passed | 6 |

## Failures

### `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_2_lens_modeling/tutorial_2_practicalities.py` — FAILED (0.0s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_2_lens_modeling/tutorial_2_practicalities.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_2_lens_modeling/tutorial_2_practicalities.py", line 77, in <module>
    search = af.Nautilus(
             ^^
NameError: name 'af' is not defined
```

### `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_2_lens_modeling/tutorial_6_masking_and_positions.py` — FAILED (5.8s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_2_lens_modeling/tutorial_6_masking_and_positions.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_2_lens_modeling/tutorial_6_masking_and_positions.py", line 81, in <module>
    dataset = dataset.apply_mask(mask=mask)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/dataset/imaging/dataset.py", line 298, in apply_mask
    dataset = Imaging(
              ^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/dataset/imaging/dataset.py", line 128, in __init__
    state = ConvolverState(kernel=psf.kernel, mask=self.data.mask)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/operators/convolver.py", line 105, in __init__
    y_min, y_max = ys.min(), ys.max()
                   ^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/numpy/_core/_methods.py", line 48, in _amin
    return umr_minimum(a, axis, None, out, keepdims, initial, where)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: zero-size array to reduction operation minimum which has no identity
```

## Passed

- `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_2_lens_modeling/tutorial_1_non_linear_search.py` (16.3s)
- `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_2_lens_modeling/tutorial_3_realism_and_complexity.py` (12.0s)
- `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_2_lens_modeling/tutorial_4_dealing_with_failure.py` (6.1s)
- `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_2_lens_modeling/tutorial_5_linear_profiles.py` (16.0s)
- `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_2_lens_modeling/tutorial_7_results.py` (7.3s)
- `/home/jammy/Code/PyAutoLabs/HowToLens/scripts/chapter_2_lens_modeling/tutorial_8_need_for_speed.py` (0.0s)
