# Test Report: howtogalaxy / scripts/chapter_2_modeling (script)

**8 scripts** | 3 failed | 5 passed

| Status | Count |
|--------|-------|
| failed | 3 |
| passed | 5 |

## Failures

### `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_2_modeling/tutorial_3_realism_and_complexity.py` — FAILED (3.5s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_2_modeling/tutorial_3_realism_and_complexity.py']' returned non-zero exit status 1.

```
/home/jammy/venv/PyAuto/bin/python3: can't open file '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/imaging/simulator.py': [Errno 2] No such file or directory
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_2_modeling/tutorial_3_realism_and_complexity.py", line 57, in <module>
    subprocess.run(
  File "/usr/lib/python3.12/subprocess.py", line 571, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/home/jammy/venv/PyAuto/bin/python3', 'scripts/imaging/simulator.py']' returned non-zero exit status 2.
```

### `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_2_modeling/tutorial_4_dealing_with_failure.py` — FAILED (3.5s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_2_modeling/tutorial_4_dealing_with_failure.py']' returned non-zero exit status 1.

```
/home/jammy/venv/PyAuto/bin/python3: can't open file '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/imaging/simulator.py': [Errno 2] No such file or directory
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_2_modeling/tutorial_4_dealing_with_failure.py", line 58, in <module>
    subprocess.run(
  File "/usr/lib/python3.12/subprocess.py", line 571, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/home/jammy/venv/PyAuto/bin/python3', 'scripts/imaging/simulator.py']' returned non-zero exit status 2.
```

### `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_2_modeling/tutorial_5_linear_profiles.py` — FAILED (3.9s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_2_modeling/tutorial_5_linear_profiles.py']' returned non-zero exit status 1.

```
/home/jammy/venv/PyAuto/bin/python3: can't open file '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/imaging/simulator.py': [Errno 2] No such file or directory
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_2_modeling/tutorial_5_linear_profiles.py", line 72, in <module>
    subprocess.run(
  File "/usr/lib/python3.12/subprocess.py", line 571, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/home/jammy/venv/PyAuto/bin/python3', 'scripts/imaging/simulator.py']' returned non-zero exit status 2.
```

## Passed

- `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_2_modeling/tutorial_1_non_linear_search.py` (10.7s)
- `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_2_modeling/tutorial_2_practicalities.py` (5.4s)
- `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_2_modeling/tutorial_6_masking.py` (5.0s)
- `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_2_modeling/tutorial_7_results.py` (5.0s)
- `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_2_modeling/tutorial_8_need_for_speed.py` (0.0s)
