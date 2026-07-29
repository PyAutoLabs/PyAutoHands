# Test Report: howtogalaxy / scripts/chapter_3_search_chaining (script)

**3 scripts** | 3 failed

| Status | Count |
|--------|-------|
| failed | 3 |

## Failures

### `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_3_search_chaining/tutorial_1_search_chaining.py` — FAILED (3.7s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_3_search_chaining/tutorial_1_search_chaining.py']' returned non-zero exit status 1.

```
/home/jammy/venv/PyAuto/bin/python3: can't open file '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/imaging/simulator.py': [Errno 2] No such file or directory
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_3_search_chaining/tutorial_1_search_chaining.py", line 78, in <module>
    subprocess.run(
  File "/usr/lib/python3.12/subprocess.py", line 571, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/home/jammy/venv/PyAuto/bin/python3', 'scripts/imaging/simulator.py']' returned non-zero exit status 2.
```

### `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_3_search_chaining/tutorial_2_prior_passing.py` — FAILED (3.7s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_3_search_chaining/tutorial_2_prior_passing.py']' returned non-zero exit status 1.

```
/home/jammy/venv/PyAuto/bin/python3: can't open file '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/imaging/simulator.py': [Errno 2] No such file or directory
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_3_search_chaining/tutorial_2_prior_passing.py", line 57, in <module>
    subprocess.run(
  File "/usr/lib/python3.12/subprocess.py", line 571, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/home/jammy/venv/PyAuto/bin/python3', 'scripts/imaging/simulator.py']' returned non-zero exit status 2.
```

### `/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_3_search_chaining/tutorial_3_x2_galaxies.py` — FAILED (3.6s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_3_search_chaining/tutorial_3_x2_galaxies.py']' returned non-zero exit status 1.

```
/home/jammy/venv/PyAuto/bin/python3: can't open file '/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/guides/plot/simulator.py': [Errno 2] No such file or directory
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/HowToGalaxy/scripts/chapter_3_search_chaining/tutorial_3_x2_galaxies.py", line 60, in <module>
    subprocess.run(
  File "/usr/lib/python3.12/subprocess.py", line 571, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/home/jammy/venv/PyAuto/bin/python3', 'scripts/guides/plot/simulator.py']' returned non-zero exit status 2.
```
