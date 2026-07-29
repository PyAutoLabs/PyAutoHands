# Test Report: autogalaxy / scripts/imaging (script)

**43 scripts** | 1 failed | 35 passed | 7 skipped

| Status | Count |
|--------|-------|
| failed | 1 |
| passed | 35 |
| skipped | 7 |

## Failures

### `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/imaging/features/extra_galaxies/modeling.py` — FAILED (4.2s)

Command '['/home/jammy/venv/PyAuto/bin/python3', '/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/imaging/features/extra_galaxies/modeling.py']' returned non-zero exit status 1.

```
Traceback (most recent call last):
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/imaging/features/extra_galaxies/modeling.py", line 272, in <module>
    ag.from_json(file_path=Path(dataset_path, "extra_galaxies_centres.json"))
  File "/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/PyAutoConf/autoconf/dictable.py", line 364, in from_json
    with open(file_path, "r+") as f:
         ^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'dataset/imaging/extra_galaxies/extra_galaxies_centres.json'
```

## Skipped

| Script | Reason |
|--------|--------|
| `extra_galaxies_centres.py` | GUI scripts cannot be run |
| `light_centre.py` | GUI scripts cannot be run |
| `mask.py` | GUI scripts cannot be run |
| `mask_extra_galaxies.py` | GUI scripts cannot be run |
| `mask_irregular.py` | NEEDS_FIX 2026-04-10 - silent failure, needs investigation |
| `modeling.py` | NEEDS_FIX 2026-04-10 - LinAlgError: matrix not positive definite in pixelization modeling |
| `modeling.py` | NEEDS_FIX 2026-04-10 - KeyError on ('galaxies','galaxy','bulge','ell_comps'...) kwargs after API drift in top-level imaging/modeling.py |

## Passed

- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/imaging/features/extra_galaxies/simulator.py` (3.8s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/imaging/features/multi_gaussian_expansion/simulator.py` (4.3s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/imaging/features/operated_light_profile/simulator.py` (3.7s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/imaging/features/simulator_manual_signal_to_noise.py` (4.0s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/imaging/features/sky_background/simulator.py` (4.0s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/imaging/simulator.py` (4.3s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/imaging/simulator_sample.py` (7.1s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/imaging/simulator_sersic.py` (3.5s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/imaging/data_preparation/start_here.py` (1.8s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/imaging/start_here.py` (11.6s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/imaging/data_preparation.py` (4.7s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/imaging/data_preparation/examples/data.py` (4.6s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/imaging/data_preparation/examples/noise_map.py` (4.4s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/imaging/data_preparation/examples/optional/extra_galaxies_centres.py` (4.7s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/imaging/data_preparation/examples/optional/info.py` (0.0s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/imaging/data_preparation/examples/optional/light_centre.py` (4.6s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/imaging/data_preparation/examples/optional/mask.py` (5.3s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/imaging/data_preparation/examples/optional/mask_extra_galaxies.py` (4.6s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/imaging/data_preparation/examples/psf.py` (1.6s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/imaging/features/linear_light_profiles/fit.py` (3.3s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/imaging/features/linear_light_profiles/likelihood_function.py` (2.8s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/imaging/features/linear_light_profiles/modeling.py` (4.3s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/imaging/features/multi_gaussian_expansion/fit.py` (8.4s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/imaging/features/multi_gaussian_expansion/likelihood_function.py` (4.0s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/imaging/features/multi_gaussian_expansion/modeling.py` (25.1s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/imaging/features/operated_light_profile/modeling.py` (4.5s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/imaging/features/pixelization/fit.py` (5.1s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/imaging/features/pixelization/likelihood_function.py` (4.4s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/imaging/features/pixelization/source_science.py` (3.7s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/imaging/features/shapelets/fit.py` (6.0s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/imaging/features/shapelets/modeling.py` (20.6s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/imaging/features/sky_background/fit.py` (3.1s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/imaging/features/sky_background/modeling.py` (4.1s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/imaging/fit.py` (6.2s)
- `/home/jammy/Code/PyAutoLabs-wt/autobuild-release-prep/autogalaxy_workspace/scripts/imaging/likelihood_function.py` (3.4s)
