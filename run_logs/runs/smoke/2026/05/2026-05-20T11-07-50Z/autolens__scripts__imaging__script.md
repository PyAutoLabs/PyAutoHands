# Test Report: autolens / scripts/imaging (script)

**78 scripts** | 3 failed | 60 passed | 15 skipped

| Status | Count |
|--------|-------|
| failed | 3 |
| passed | 60 |
| skipped | 15 |

## Failures

### `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/mass_stellar_dark/fit.py` — FAILED (5.3s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/mass_stellar_dark/fit.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/mass_stellar_dark/fit.py", line 255, in <module>
    assert np.allclose(np.asarray(alpha_total_summed), np.asarray(alpha_total_lens))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
```

### `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/mass_stellar_dark/likelihood_function.py` — FAILED (6.7s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/mass_stellar_dark/likelihood_function.py']' returned non-zero exit status 1.

```
/home/jammy/Code/PyAutoLabs/PyAutoGalaxy/autogalaxy/profiles/mass/dark/nfw.py:321: RuntimeWarning: divide by zero encountered in divide
  (4.0 * self.kappa_s * self.scale_radius / eta),
/home/jammy/Code/PyAutoLabs/PyAutoGalaxy/autogalaxy/profiles/mass/dark/abstract.py:156: RuntimeWarning: divide by zero encountered in log
  return xp.log(grid_radius / 2.0) + self.coord_func_f(
/home/jammy/Code/PyAutoLabs/PyAutoGalaxy/autogalaxy/profiles/mass/dark/abstract.py:101: RuntimeWarning: divide by zero encountered in divide
  inv_r = 1.0 / r
/home/jammy/Code/PyAutoLabs/PyAutoGalaxy/autogalaxy/profiles/mass/dark/abstract.py:101: RuntimeWarning: invalid value encountered in divide
  inv_r = 1.0 / r
/home/jammy/Code/PyAutoLabs/PyAutoGalaxy/autogalaxy/profiles/mass/dark/abstract.py:107: RuntimeWarning: invalid value encountered in multiply
  out_lt = (1.0 / xp.sqrt(1.0 - r**2)) * xp.arccosh(inv_r)
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/mass_stellar_dark/likelihood_function.py", line 195, in <module>
    assert np.allclose(np.asarray(grid_source_manual), np.asarray(grid_source_tracer))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
```

### `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/multi_gaussian_expansion/modeling.py` — FAILED (53.5s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/multi_gaussian_expansion/modeling.py']' returned non-zero exit status 1.

```
During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/multi_gaussian_expansion/modeling.py", line 579, in <module>
    result = search.fit(model=model, analysis=analysis)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/abstract_search.py", line 512, in fit
    result = self.start_resume_fit(
             ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/abstract_search.py", line 117, in decorated
    return func(self, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/abstract_search.py", line 661, in start_resume_fit
    return self._fit_bypass_test_mode(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs/PyAutoFit/autofit/non_linear/search/abstract_search.py", line 848, in _fit_bypass_test_mode
    analysis.log_likelihood_function(instance)
  File "/home/jammy/Code/PyAutoLabs/PyAutoLens/autolens/imaging/model/analysis.py", line 84, in log_likelihood_function
    raise af.exc.FitException
autofit.exc.FitException
```

## Skipped

| Script | Reason |
|--------|--------|
| `start_here.py` | All sensitivity scripts need updating when visualization refactored. |
| `extra_galaxies_centres.py` | GUI scripts cannot be run |
| `lens_light_centre.py` | GUI scripts cannot be run |
| `mask.py` | GUI scripts cannot be run |
| `mask_extra_galaxies.py` | GUI scripts cannot be run |
| `positions.py` | GUI scripts cannot be run |
| `mask_irregular.py` | NEEDS_FIX 2026-04-10 - silent failure, needs investigation |
| `slam.py` | NEEDS_FIX 2026-05-07 - autofit.exc.FitException in SLaM bypass mode (same family as imaging/features/pixelization/slam — Adapt regularization needs adapt_data which the synthetic samples_summary doesn't carry; cascade goes deep, fixing in one PR isn't tractable) |
| `modeling.py` | Requires CSE to be JAX enabled. |
| `slam.py` | Requires CSE to be JAX enabled. |
| `database.py` | Unsure but not a feature actively used currently. |
| `slam_source_parametric.py` | All sensitivity scripts need updating when visualization refactored. |
| `slam_source_pixelized.py` | All sensitivity scripts need updating when visualization refactored. |
| `delaunay.py` | NEEDS_FIX 2026-04-10 - autofit.exc.FitException in Delaunay pixelization fit |
| `slam.py` | NEEDS_FIX 2026-04-10 - autofit.exc.FitException in SLaM pixelization pipeline |

## Passed

- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/double_einstein_ring/simulator.py` (5.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/los_halos/simulator.py` (56.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/mass_stellar_dark/simulator.py` (4.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/operated_light_profile/simulator.py` (5.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/sky_background/simulator.py` (5.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/subhalo/simulator.py` (6.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/extra_galaxies/simulator.py` (6.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/multi_gaussian_expansion/simulator.py` (5.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/no_lens_light/simulator.py` (5.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/scaling_relation/simulator.py` (5.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/simulator_manual_signal_to_noise_ratio.py` (6.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/simulator.py` (6.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/simulator_sample.py` (10.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/data_preparation/start_here.py` (4.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/subhalo/detect/start_here.py` (17.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/start_here.py` (56.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/data_preparation/examples/data.py` (9.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/data_preparation/examples/noise_map.py` (9.2s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/data_preparation/examples/optional/extra_galaxies_centres.py` (9.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/data_preparation/examples/optional/info.py` (10.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/data_preparation/examples/optional/lens_light_centre.py` (8.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/data_preparation/examples/optional/mask.py` (9.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/data_preparation/examples/optional/mask_extra_galaxies.py` (9.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/data_preparation/examples/optional/positions.py` (9.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/data_preparation/examples/psf.py` (3.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/double_einstein_ring/chaining.py` (13.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/double_einstein_ring/fit.py` (10.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/double_einstein_ring/likelihood_function.py` (8.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/double_einstein_ring/modeling.py` (7.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/mass_stellar_dark/chaining.py` (9.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/operated_light_profile/modeling.py` (9.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/shapelets/fit.py` (13.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/shapelets/modeling.py` (54.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/sky_background/fit.py` (7.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/advanced/sky_background/modeling.py` (8.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/extra_galaxies/modeling.py` (9.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/extra_galaxies/slam.py` (15.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/linear_light_profiles/fit.py` (7.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/linear_light_profiles/likelihood_function.py` (7.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/linear_light_profiles/modeling.py` (7.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/linear_light_profiles/slam.py` (13.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/multi_gaussian_expansion/fit.py` (13.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/multi_gaussian_expansion/likelihood_function.py` (5.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/multi_gaussian_expansion/slam.py` (6.7s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/multi_gaussian_expansion/source_science.py` (10.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/no_lens_light/modeling.py` (9.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/no_lens_light/slam.py` (8.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/pixelization/adaptive.py` (11.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/pixelization/cpu_fast_modeling.py` (13.9s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/pixelization/fit.py` (9.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/pixelization/likelihood_function.py` (8.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/pixelization/modeling.py` (6.6s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/pixelization/source_science.py` (6.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/scaling_relation/fit.py` (8.3s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/scaling_relation/likelihood_function.py` (7.4s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/features/scaling_relation/modeling.py` (12.1s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/fit.py` (15.0s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/likelihood_function.py` (6.8s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/modeling.py` (12.5s)
- `/home/jammy/Code/PyAutoLabs/autolens_workspace/scripts/imaging/source_science.py` (6.2s)
