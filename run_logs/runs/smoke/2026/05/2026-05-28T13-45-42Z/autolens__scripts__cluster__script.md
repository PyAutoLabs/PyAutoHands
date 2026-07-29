# Test Report: autolens / scripts/cluster (script)

**5 scripts** | 3 failed | 2 passed

| Status | Count |
|--------|-------|
| failed | 3 |
| passed | 2 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/cluster/simulator.py` — FAILED (9.1s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/cluster/simulator.py']' returned non-zero exit status 1.

```
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/structures/decorators/to_array.py", line 47, in wrapper
    return ArrayMaker(func=func, obj=obj, grid=grid, xp=xp, *args, **kwargs).result
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/structures/decorators/abstract.py", line 112, in result
    return self.via_grid_2d_irr(self.evaluate_func)
                                ^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/structures/decorators/abstract.py", line 93, in evaluate_func
    return self.func(self.obj, self.grid, self._xp, *self.args, **self.kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/structures/decorators/transform.py", line 80, in wrapper
    result = func(obj, grid, xp, *args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoGalaxy/autogalaxy/profiles/mass/abstract/mge.py", line 509, in potential_2d_via_mge_from
    amps, sigmas = self.decompose_convergence_via_mge(
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoGalaxy/autogalaxy/profiles/mass/abstract/mge.py", line 274, in decompose_convergence_via_mge
    self.mass_profile.convergence_func(
  File "/home/jammy/Code/PyAutoLabs/PyAutoGalaxy/autogalaxy/profiles/mass/abstract/abstract.py", line 174, in convergence_func
    raise NotImplementedError
NotImplementedError
```

### `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/cluster/start_here.py` — FAILED (9.7s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/cluster/start_here.py']' returned non-zero exit status 1.

```
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/structures/decorators/to_array.py", line 47, in wrapper
    return ArrayMaker(func=func, obj=obj, grid=grid, xp=xp, *args, **kwargs).result
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/structures/decorators/abstract.py", line 112, in result
    return self.via_grid_2d_irr(self.evaluate_func)
                                ^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/structures/decorators/abstract.py", line 93, in evaluate_func
    return self.func(self.obj, self.grid, self._xp, *self.args, **self.kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/structures/decorators/transform.py", line 80, in wrapper
    result = func(obj, grid, xp, *args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoGalaxy/autogalaxy/profiles/mass/abstract/mge.py", line 509, in potential_2d_via_mge_from
    amps, sigmas = self.decompose_convergence_via_mge(
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoGalaxy/autogalaxy/profiles/mass/abstract/mge.py", line 274, in decompose_convergence_via_mge
    self.mass_profile.convergence_func(
  File "/home/jammy/Code/PyAutoLabs/PyAutoGalaxy/autogalaxy/profiles/mass/abstract/abstract.py", line 174, in convergence_func
    raise NotImplementedError
NotImplementedError
```

### `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/cluster/modeling.py` — FAILED (10.0s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/cluster/modeling.py']' returned non-zero exit status 1.

```
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/structures/decorators/to_array.py", line 47, in wrapper
    return ArrayMaker(func=func, obj=obj, grid=grid, xp=xp, *args, **kwargs).result
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/structures/decorators/abstract.py", line 112, in result
    return self.via_grid_2d_irr(self.evaluate_func)
                                ^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/structures/decorators/abstract.py", line 93, in evaluate_func
    return self.func(self.obj, self.grid, self._xp, *self.args, **self.kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoArray/autoarray/structures/decorators/transform.py", line 80, in wrapper
    result = func(obj, grid, xp, *args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoGalaxy/autogalaxy/profiles/mass/abstract/mge.py", line 509, in potential_2d_via_mge_from
    amps, sigmas = self.decompose_convergence_via_mge(
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoGalaxy/autogalaxy/profiles/mass/abstract/mge.py", line 274, in decompose_convergence_via_mge
    self.mass_profile.convergence_func(
  File "/home/jammy/Code/PyAutoLabs/PyAutoGalaxy/autogalaxy/profiles/mass/abstract/abstract.py", line 174, in convergence_func
    raise NotImplementedError
NotImplementedError
```

## Passed

- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/cluster/csv_api.py` (6.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/cluster/likelihood_function.py` (4.6s)
