# Test Report: howtogalaxy / scripts/chapter_4_pixelizations (script)

**5 scripts** | 1 failed | 4 passed

| Status | Count |
|--------|-------|
| failed | 1 |
| passed | 4 |

## Failures

### `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_4_pixelizations/tutorial_2_mappers.py` — FAILED (3.1s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_4_pixelizations/tutorial_2_mappers.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_4_pixelizations/tutorial_2_mappers.py", line 106, in <module>
    indexes = mapper.slim_indexes_for_pix_indexes(pix_indexes=pix_indexes)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/inversion/mappers/abstract.py", line 451, in slim_indexes_for_pix_indexes
    image_for_source[index]
    ~~~~~~~~~~~~~~~~^^^^^^^
IndexError: list index out of range
```

## Passed

- `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_4_pixelizations/tutorial_1_pixelizations.py` (3.3s)
- `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_4_pixelizations/tutorial_3_inversions.py` (3.2s)
- `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_4_pixelizations/tutorial_4_bayesian_regularization.py` (22.8s)
- `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_4_pixelizations/tutorial_5_model_fit.py` (5.6s)
