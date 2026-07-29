# Test Report: howtogalaxy / scripts/chapter_4_pixelizations (script)

**5 scripts** | 3 failed | 2 passed

| Status | Count |
|--------|-------|
| failed | 3 |
| passed | 2 |

## Failures

### `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_4_pixelizations/tutorial_2_mappers.py` — FAILED (3.8s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_4_pixelizations/tutorial_2_mappers.py']' returned non-zero exit status 1.

```
/home/jammy/venv/PyAuto/bin/python3: can't open file '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/imaging/simulator.py': [Errno 2] No such file or directory
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_4_pixelizations/tutorial_2_mappers.py", line 47, in <module>
    subprocess.run(
  File "/usr/lib/python3.12/subprocess.py", line 571, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/home/jammy/venv/PyAuto/bin/python3', 'scripts/imaging/simulator.py']' returned non-zero exit status 2.
```

### `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_4_pixelizations/tutorial_4_bayesian_regularization.py` — FAILED (3.6s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_4_pixelizations/tutorial_4_bayesian_regularization.py']' returned non-zero exit status 1.

```
/home/jammy/venv/PyAuto/bin/python3: can't open file '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/imaging/simulator.py': [Errno 2] No such file or directory
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_4_pixelizations/tutorial_4_bayesian_regularization.py", line 55, in <module>
    subprocess.run(
  File "/usr/lib/python3.12/subprocess.py", line 571, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/home/jammy/venv/PyAuto/bin/python3', 'scripts/imaging/simulator.py']' returned non-zero exit status 2.
```

### `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_4_pixelizations/tutorial_5_model_fit.py` — FAILED (3.8s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_4_pixelizations/tutorial_5_model_fit.py']' returned non-zero exit status 1.

```
/home/jammy/venv/PyAuto/bin/python3: can't open file '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/imaging/simulator.py': [Errno 2] No such file or directory
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_4_pixelizations/tutorial_5_model_fit.py", line 61, in <module>
    subprocess.run(
  File "/usr/lib/python3.12/subprocess.py", line 571, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/home/jammy/venv/PyAuto/bin/python3', 'scripts/imaging/simulator.py']' returned non-zero exit status 2.
```

## Passed

- `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_4_pixelizations/tutorial_1_pixelizations.py` (3.7s)
- `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_4_pixelizations/tutorial_3_inversions.py` (3.5s)
