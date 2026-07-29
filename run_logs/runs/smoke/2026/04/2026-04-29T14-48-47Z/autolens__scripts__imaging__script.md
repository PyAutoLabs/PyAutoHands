# Test Report: autolens / scripts/imaging (script)

**71 scripts** | 1 failed | 56 passed | 14 skipped

| Status | Count |
|--------|-------|
| failed | 1 |
| passed | 56 |
| skipped | 14 |

## Failures

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/advanced/double_einstein_ring/slam.py` — FAILED (8.1s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/advanced/double_einstein_ring/slam.py']' returned non-zero exit status 1.

```
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/advanced/double_einstein_ring/slam.py", line 566, in <module>
    source_pix_result_1_source_1 = source_pix_1_source_1(
                                   ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/advanced/double_einstein_ring/slam.py", line 365, in source_pix_1_source_1
    return search.fit(model=model, analysis=analysis, **settings_search.fit_dict)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoFit/autofit/non_linear/search/abstract_search.py", line 512, in fit
    result = self.start_resume_fit(
             ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoFit/autofit/non_linear/search/abstract_search.py", line 117, in decorated
    return func(self, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoFit/autofit/non_linear/search/abstract_search.py", line 661, in start_resume_fit
    return self._fit_bypass_test_mode(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoFit/autofit/non_linear/search/abstract_search.py", line 848, in _fit_bypass_test_mode
    analysis.log_likelihood_function(instance)
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoLens/autolens/imaging/model/analysis.py", line 84, in log_likelihood_function
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
| `modeling.py` | Requires CSE to be JAX enabled. |
| `slam.py` | Requires CSE to be JAX enabled. |
| `database.py` | Unsure but not a feature actively used currently. |
| `slam_source_parametric.py` | All sensitivity scripts need updating when visualization refactored. |
| `slam_source_pixelized.py` | All sensitivity scripts need updating when visualization refactored. |
| `delaunay.py` | NEEDS_FIX 2026-04-10 - autofit.exc.FitException in Delaunay pixelization fit |
| `slam.py` | NEEDS_FIX 2026-04-10 - autofit.exc.FitException in SLaM pixelization pipeline |

## Passed

- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/advanced/double_einstein_ring/simulator.py` (4.7s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/advanced/los_halos/simulator.py` (40.1s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/advanced/mass_stellar_dark/simulator.py` (3.4s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/advanced/operated_light_profile/simulator.py` (3.3s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/advanced/sky_background/simulator.py` (3.3s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/advanced/subhalo/simulator.py` (4.0s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/extra_galaxies/simulator.py` (3.5s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/multi_gaussian_expansion/simulator.py` (3.5s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/no_lens_light/simulator.py` (3.6s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/simulator_manual_signal_to_noise_ratio.py` (3.4s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/simulator.py` (3.6s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/simulator_sample.py` (6.7s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/data_preparation/start_here.py` (2.1s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/advanced/subhalo/detect/start_here.py` (11.6s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/start_here.py` (39.7s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/data_preparation/examples/data.py` (9.3s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/data_preparation/examples/noise_map.py` (6.5s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/data_preparation/examples/optional/extra_galaxies_centres.py` (6.7s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/data_preparation/examples/optional/info.py` (5.9s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/data_preparation/examples/optional/lens_light_centre.py` (6.2s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/data_preparation/examples/optional/mask.py` (7.0s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/data_preparation/examples/optional/mask_extra_galaxies.py` (6.3s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/data_preparation/examples/optional/positions.py` (7.9s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/data_preparation/examples/psf.py` (2.6s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/advanced/double_einstein_ring/chaining.py` (11.6s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/advanced/double_einstein_ring/modeling.py` (6.4s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/advanced/mass_stellar_dark/chaining.py` (5.7s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/advanced/operated_light_profile/modeling.py` (6.4s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/advanced/shapelets/fit.py` (8.1s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/advanced/shapelets/modeling.py` (35.9s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/advanced/sky_background/fit.py` (4.7s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/advanced/sky_background/modeling.py` (6.4s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/extra_galaxies/modeling.py` (10.2s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/extra_galaxies/slam.py` (10.9s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/linear_light_profiles/fit.py` (4.4s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/linear_light_profiles/likelihood_function.py` (4.7s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/linear_light_profiles/modeling.py` (6.1s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/linear_light_profiles/slam.py` (11.1s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/multi_gaussian_expansion/fit.py` (12.7s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/multi_gaussian_expansion/likelihood_function.py` (6.0s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/multi_gaussian_expansion/modeling.py` (42.5s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/multi_gaussian_expansion/slam.py` (5.4s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/multi_gaussian_expansion/source_science.py` (5.5s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/no_lens_light/modeling.py` (6.7s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/no_lens_light/slam.py` (8.3s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/pixelization/adaptive.py` (7.7s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/pixelization/cpu_fast_modeling.py` (8.5s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/pixelization/fit.py` (7.8s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/pixelization/likelihood_function.py` (8.7s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/pixelization/modeling.py` (8.0s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/pixelization/source_science.py` (7.7s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/features/scaling_relation/modeling.py` (7.2s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/fit.py` (10.1s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/likelihood_function.py` (4.6s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/modeling.py` (11.8s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autolens_workspace/scripts/imaging/source_science.py` (3.2s)
