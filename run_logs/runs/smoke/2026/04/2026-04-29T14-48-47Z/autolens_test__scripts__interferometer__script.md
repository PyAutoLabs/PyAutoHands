# Test Report: autolens_test / scripts/interferometer (script)

**4 scripts** | 2 failed | 2 passed

| Status | Count |
|--------|-------|
| failed | 2 |
| passed | 2 |

## Failures

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/interferometer/model_fit.py` — FAILED (17.2s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/interferometer/model_fit.py']' returned non-zero exit status 1.

```
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoFit/autofit/non_linear/search/nest/nautilus/search.py", line 413, in call_search
    search_internal.run(
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/nautilus/sampler.py", line 441, in run
    self.n_update_iter += self.add_samples(-1, verbose=verbose)
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/nautilus/sampler.py", line 1119, in add_samples
    log_l, blobs = self.evaluate_likelihood(points)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/nautilus/sampler.py", line 869, in evaluate_likelihood
    result = list(self.pool_l.map(self.likelihood, args))
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/venv/PyAuto/lib/python3.12/site-packages/nautilus/pool.py", line 85, in map
    return list(self.pool.map(func, iterable))
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/multiprocessing/pool.py", line 367, in map
    return self._map_async(func, iterable, mapstar, chunksize).get()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/multiprocessing/pool.py", line 774, in get
    raise self._value
numpy.linalg.LinAlgError: Matrix is not positive definite
```

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/interferometer/visualization.py` — FAILED (48.4s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/interferometer/visualization.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/interferometer/visualization.py", line 341, in <module>
    VisualizerInterferometer.visualize(
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoLens/autolens/interferometer/model/visualizer.py", line 159, in visualize
    plotter.inversion(
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoGalaxy/autogalaxy/analysis/plotter.py", line 150, in inversion
    subplot_of_mapper(
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/inversion/plot/inversion_plots.py", line 63, in subplot_of_mapper
    plot_array(
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoArray/autoarray/plot/array.py", line 199, in plot_array
    h, w = array.shape[:2]
    ^^^^
ValueError: not enough values to unpack (expected 2, got 1)
```

## Passed

- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/interferometer/simulator/no_lens_light.py` (4.7s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace_test/scripts/interferometer/simulator/with_lens_light.py` (6.3s)
