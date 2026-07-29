# Test Report: autolens_test / scripts/database (script)

**6 scripts** | 1 passed | 5 skipped

| Status | Count |
|--------|-------|
| passed | 1 |
| skipped | 5 |

## Skipped

| Script | Reason |
|--------|--------|
| `general.py` | NEEDS_FIX 2026-04-27 - PyAutoGalaxy abstract_fit.linear_light_profile_intensity_dict raises "TypeError: __hash__ method should return an integer" during subplot_fit_imaging after the search completes (a light-profile object's __hash__ returns a non-int). Surfaced once the dataset_label="build" path fix let the script progress past Imaging.from_fits. |
| `multi_analysis.py` | SLOW 2026-04-10 - exceeds 60s timeout; _test workspaces run full searches without test mode |
| `slam_general.py` | SLOW 2026-04-10 - exceeds 60s timeout; _test workspaces run full searches without test mode |
| `slam_multi_one_by_one.py` | SLOW 2026-04-10 - exceeds 60s timeout; _test workspaces run full searches without test mode |
| `slam_pix.py` | SLOW 2026-04-10 - exceeds 60s timeout; _test workspaces run full searches without test mode |

## Passed

- `/home/jammy/Code/PyAutoLabs/autolens_workspace_test/scripts/database/scrape/scaling_relation.py` (93.9s)
