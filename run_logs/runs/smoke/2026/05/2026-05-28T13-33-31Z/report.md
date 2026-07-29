# Release Readiness Report

**Status: READY**

**Run:** `2026-05-28T13-33-31Z`  •  **Path:** `/home/jammy/Code/PyAutoLabs/PyAutoBuild/test_results/runs/2026-05-28T13-33-31Z`  •  **Total duration:** 345.7s

## Summary

| Passed | Failed | Skipped | Timeout |
|--------|--------|---------|---------|
| 5 | 0 | 0 | 0 |

## Per-Project Breakdown

| Project | Passed | Failed | Skipped | Timeout | Duration |
|---------|--------|--------|---------|---------|----------|
| euclid | 5 | 0 | 0 | 0 | 345.7s |

## Slowest scripts (top 5)

| Script | Project | Status | Duration | Share |
|--------|---------|--------|----------|-------|
| `/home/jammy/Code/PyAutoLabs/euclid_strong_lens_modeling_pipeline/scripts/lens_model_waveband.py` | euclid | passed | 97.1s | 28.1% |
| `/home/jammy/Code/PyAutoLabs/euclid_strong_lens_modeling_pipeline/scripts/full_model.py` | euclid | passed | 77.2s | 22.3% |
| `/home/jammy/Code/PyAutoLabs/euclid_strong_lens_modeling_pipeline/scripts/mge_lens_only.py` | euclid | passed | 74.3s | 21.5% |
| `/home/jammy/Code/PyAutoLabs/euclid_strong_lens_modeling_pipeline/scripts/sersic_lens_model.py` | euclid | passed | 67.4s | 19.5% |
| `/home/jammy/Code/PyAutoLabs/euclid_strong_lens_modeling_pipeline/scripts/initial_lens_model.py` | euclid | passed | 29.8s | 8.6% |

## Changes Since Last Release

### [Cache model.parameterization; try interactive matplotlib backends](https://github.com/PyAutoLabs/PyAutoFit/pull/1299) (PyAutoLabs/PyAutoFit)
**API Changes:** None — `parameterization` was already a `@property`, now `@functools.cached_property`. Same external interface. The live_viewer backend selection is internal.

### [Prefer fit_quick.png in quick-update display candidates](https://github.com/PyAutoLabs/PyAutoFit/pull/1298) (PyAutoLabs/PyAutoFit)
**API Changes:** None — internal constant change only.

### [Remove use_jax_for_visualization; add visualization warmup](https://github.com/PyAutoLabs/PyAutoFit/pull/1297) (PyAutoLabs/PyAutoFit)
**API Changes:** `Analysis.__init__` no longer accepts `use_jax_for_visualization`. Visualization now automatically follows `use_jax` — if the search uses JAX, visualization does too. The `_jitted_fit_from` lazy JIT cache on Analysis is removed; the warmup in `Fitness.__init__` is a better approach (pre-compiles bef

### [fix: skip _compute_latent_samples in PYAUTO_TEST_MODE (#1294)](https://github.com/PyAutoLabs/PyAutoFit/pull/1295) (PyAutoLabs/PyAutoFit)
**API Changes:** Public API: no change. Purely internal — adds `if skip_latents(): return None` at the top of the private `SearchUpdater._compute_latent_samples` method. The `PYAUTO_SKIP_LATENTS` env var is a new user-facing env knob but documented inline in `autoconf.test_mode.skip_latents()`'s docstring.

See full

### [Add live_visual_update flag for opt-in on-the-fly visualization](https://github.com/PyAutoLabs/PyAutoFit/pull/1293) (PyAutoLabs/PyAutoFit)
**API Changes:** `NonLinearSearch.__init__` gains optional `live_visual_update` kwarg (default `None`, falls back to `general.updates.live_visual_update` in config — defaults `false`). `Fitness.__init__` and `BackgroundQuickUpdate.__init__` gain the same flag. A new `LiveDisplay` helper class composes the display su

### [fix: PYAUTO_TEST_MODE should write to a separate output dir](https://github.com/PyAutoLabs/PyAutoFit/pull/1292) (PyAutoLabs/PyAutoFit)
**API Changes:** No public symbol additions, removals, or signature changes.

Behaviour change: when the `PYAUTO_TEST_MODE` environment variable is set (any truthy value), AutoFit search output paths get a `test_mode/` segment inserted directly after `conf.instance.output_path`. This affects every search-output path

### [feat(quick_update): IPython.display.update_display for live Jupyter cells](https://github.com/PyAutoLabs/PyAutoFit/pull/1290) (PyAutoLabs/PyAutoFit)
**API Changes:** One additive optional kwarg on `BackgroundQuickUpdate`: `display_id: str = "pyauto_fit_progress"`. Behavioural change: when running inside a Jupyter / Colab kernel, the worker additionally pushes the freshly-written `subplot_fit.png` to the active cell via `IPython.display.update_display`. Outside a

### [feat(analysis): LATENT_BATCH_MODE attribute (vmap default, jit option)](https://github.com/PyAutoLabs/PyAutoFit/pull/1288) (PyAutoLabs/PyAutoFit)
**API Changes:** New public class attribute `Analysis.LATENT_BATCH_MODE: str` (default `"vmap"`). Two values supported: `"vmap"` and `"jit"`. Other values raise `ValueError` at `compute_latent_samples` time with a clear message.

See full details below.

### [Fix Sample.kwargs mixed string/tuple key bug](https://github.com/PyAutoLabs/PyAutoFit/pull/1287) (PyAutoLabs/PyAutoFit)
**API Changes:** Internal in-memory representation of `Sample.kwargs` is now uniformly tuple-keyed — single-name keys become `('name',)` instead of staying as raw strings. All serialized forms (CSV headers, database JSON via `Sample.dict()`) are unchanged because they already join tuples back to dotted strings on se

### [fix: VectorYX2DIrregular from_dict round-trip (missing values property)](https://github.com/PyAutoLabs/PyAutoArray/pull/342) (PyAutoLabs/PyAutoArray)
**API Changes:** Added a new public read-only `values` property on `VectorYX2DIrregular` returning the underlying `(N, 2)` ndarray. Purely additive — no existing call sites read `vec.values`. See full details below.

### [perf: cache expensive @property on Fit classes](https://github.com/PyAutoLabs/PyAutoArray/pull/341) (PyAutoLabs/PyAutoArray)
**API Changes:** None — same properties, same return types. Now cached after first access.

### [fix: make Array2D.native jit-traceable for JAX simulator path](https://github.com/PyAutoLabs/PyAutoArray/pull/339) (PyAutoLabs/PyAutoArray)
**API Changes:** None — internal changes only. `array_2d_via_indexes_from` is a private utility; the simulator public interface is unchanged.

### [fix: raise ValueError on xp=np + jnp-backed-grid mismatch](https://github.com/PyAutoLabs/PyAutoArray/pull/337) (PyAutoLabs/PyAutoArray)
**API Changes:** - **Changed behaviour:** `AbstractMaker.__init__` now raises `ValueError` when `xp is np` and `grid.use_jax` is `True`. Pre-existing call sites are unaffected — all of PyAutoArray, PyAutoLens, PyAutoGalaxy continue to pass the tests (verified: 837 / 317 / 918 pass).

See full details below.

### [feat: SimulatorInterferometer(use_jax=True) + xp-aware preprocess Gaussian noise](https://github.com/PyAutoLabs/PyAutoArray/pull/336) (PyAutoLabs/PyAutoArray)
**API Changes:** - **Added:** `aa.SimulatorInterferometer(..., use_jax=False)` constructor flag.
- **Added:** `aa.SimulatorInterferometer._xp` property.
- **Changed signature:** `aa.SimulatorInterferometer.via_image_from(image, xp=None)` — fixed asymmetry with `SimulatorImaging` by adding the `xp` parameter. `xp=Non

### [feat: SimulatorImaging(use_jax=True) + xp-aware preprocess noise](https://github.com/PyAutoLabs/PyAutoArray/pull/335) (PyAutoLabs/PyAutoArray)
**API Changes:** - **Added:** `aa.SimulatorImaging(..., use_jax=False)` constructor flag.
- **Added:** `aa.SimulatorImaging._xp` property (returns `jnp` if `use_jax`, else `np`).
- **Changed signature:** `aa.SimulatorImaging.via_image_from(xp=None)` — defaults to `self._xp` when `None`.
- **Changed signature:** `pre

### [feat(grids): add respect_small_datasets kwarg to Grid2D.uniform](https://github.com/PyAutoLabs/PyAutoArray/pull/327) (PyAutoLabs/PyAutoArray)
**API Changes:** Adds one optional kwarg `respect_small_datasets: bool = True` to `aa.Grid2D.uniform`. No removed or renamed symbols; existing callers continue to work without change.
See full details below.

### [fix: raw-flux latent + soft-fail magzero-required µJy](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/463) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** - **Added** `total_galaxy_0_flux(fit, magzero=None, xp=np)` — raw integrated
  flux of galaxy 0 in the fit's image units; no instrument inputs required.
  Default-on in `autogalaxy/config/latent.yaml`.
- **Added** module-level helper `_maybe_magzero_warn(magzero, name) -> bool`
  to dedupe the new s

### [perf: cache expensive @property on Fit classes](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/462) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** None — same properties, same return types. Now cached after first access.

### [fix: elliptical MGE potential via deflection line integral](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/460) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** Changed internal implementation of `MGEDecomposer.potential_2d_via_mge_from`. Added `sigma_function` static method and `n_quad` parameter. No public API changes.

### [fix: add xp=np to convergence_func across all mass profiles](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/457) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** Added `xp=np` keyword to 5 `convergence_func` signatures. Default is `np` so existing callers are unaffected.

### [feat: vmapped_deflections_from for batched subhalo deflections](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/455) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** New methods on `MassProfile`:
- `MassProfile.vmapped_deflections_from(grid, params_batch, mask, xp=None)` — classmethod
- `MassProfile.radial_deflection_from(r, params, xp)` — static method (default raises `NotImplementedError`)

New static methods:
- `NFWTruncatedSph.radial_deflection_from(r, param

### [fix: cNFWSph deflection boundary bug and MCR validation (#451)](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/454) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** None — internal bug fix. The warning for invalid f_c is new user-visible behaviour.

### [docs: LaTeX docstrings for all mass profile classes](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/453) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** None — documentation only. No code logic changed.

### [feat: MGE/CSE fallback for zero-returning mass profile potentials](https://github.com/PyAutoLabs/PyAutoGalaxy/pull/449) (PyAutoLabs/PyAutoGalaxy)
**API Changes:** Added `MGEDecomposer.potential_2d_via_mge_from()` — new public method computing lensing potential from MGE-decomposed convergence using the E1 exponential integral. Added helper methods `E1()` (Abramowitz & Stegun approximation, JAX-compatible) and `potential_func_gaussian()`. All existing zero-retu

### [fix: raw-flux latents + soft-fail magzero-required µJy](https://github.com/PyAutoLabs/PyAutoLens/pull/557) (PyAutoLabs/PyAutoLens)
**API Changes:** - **Added** three raw-flux latents (`total_lens_flux`, `total_lensed_source_flux`,
  `total_source_flux`), default-on. Same image-source and exception-handling
  contract as their `_mujy` siblings — they just skip the AB-mag → µJy step.
- **Added** module-level helper `_maybe_magzero_warn(magzero, n

### [test: lock down WeakDataset json round-trip (paired with PyAutoArray fix)](https://github.com/PyAutoLabs/PyAutoLens/pull/555) (PyAutoLabs/PyAutoLens)
**API Changes:** None — test-only change. See full details below.

### [Add placeholder subplot_fit_quick for weak lensing and combined fits](https://github.com/PyAutoLabs/PyAutoLens/pull/553) (PyAutoLabs/PyAutoLens)
**API Changes:** New functions: \`subplot_fit_quick\` (weak), \`subplot_fit_combined_quick\` (imaging combined).

🤖 Generated with [Claude Code](https://claude.com/claude-code)

### [Add subplot_fit_quick for point source quick updates](https://github.com/PyAutoLabs/PyAutoLens/pull/552) (PyAutoLabs/PyAutoLens)
**API Changes:** New function `autolens.point.plot.fit_point_plots.subplot_fit_quick`.

### [Simplify subplot_fit_quick: use fit properties directly](https://github.com/PyAutoLabs/PyAutoLens/pull/551) (PyAutoLabs/PyAutoLens)
**API Changes:** None — same function, same output.

### [Fix subplot_fit_quick styling: arcsecond axes, source plane, code reuse](https://github.com/PyAutoLabs/PyAutoLens/pull/550) (PyAutoLabs/PyAutoLens)
**API Changes:** None — same functions, same output filenames.

### [Add subplot_fit_quick for interferometer quick updates](https://github.com/PyAutoLabs/PyAutoLens/pull/549) (PyAutoLabs/PyAutoLens)
**API Changes:** New function `autolens.interferometer.plot.fit_interferometer_plots.subplot_fit_quick`. The plotter's quick-update branch now calls this instead of `subplot_fit_dirty_images`.

### [perf: cache expensive @property on Fit classes](https://github.com/PyAutoLabs/PyAutoLens/pull/548) (PyAutoLabs/PyAutoLens)
**API Changes:** None — same properties, same return types. Now cached after first access.

### [Fast subplot_fit_quick: sub-second rendering for quick updates](https://github.com/PyAutoLabs/PyAutoLens/pull/547) (PyAutoLabs/PyAutoLens)
**API Changes:** None — `subplot_fit_quick` has the same signature. Internal rendering pipeline is different but the output PNG is the same 6-panel layout.

### [Add subplot_fit_quick for faster quick-update rendering](https://github.com/PyAutoLabs/PyAutoLens/pull/546) (PyAutoLabs/PyAutoLens)
**API Changes:** New function `autolens.imaging.plot.fit_imaging_plots.subplot_fit_quick` — same signature as `subplot_fit` minus the `plane_index` arg. Saves as `fit_quick.png` at 200 DPI. The plotter's quick-update branch now calls this instead of `subplot_fit`.

### [docs: expand quick-update cookbook + add config flag defaults](https://github.com/PyAutoLabs/autofit_workspace/pull/67) (PyAutoLabs/autofit_workspace)
**Scripts Changed:** - `scripts/cookbooks/analysis.py` — rewrote the `__Live Quick-Update Visualization__` section: documents `live_visual_update` separately from `background_quick_update` (the two are independent), adds an Analysis API surface subsection (`perform_quick_update`, `supports_background_update`, `supports_

### [docs: foundational latent-variables cookbook in autofit_workspace](https://github.com/PyAutoLabs/autofit_workspace/pull/64) (PyAutoLabs/autofit_workspace)
**Scripts Changed:** - `scripts/cookbooks/latent_variables.py` (new, ~200 lines) — 10 sections in order: Model Fit, What is a Latent Variable, Why Latent Variables, How PyAutoFit Computes Latents, Two Output Modes, Errors on Latents, Posterior Draws Under the Hood, Loading Results Downstream, When To Add A Latent vs A S

### [docs(cookbooks/analysis): __Live Quick-Update Visualization__ section](https://github.com/PyAutoLabs/autofit_workspace/pull/62) (PyAutoLabs/autofit_workspace)
**Scripts Changed:** - `scripts/cookbooks/analysis.py` — new `__Live Quick-Update Visualization__` section (52 lines) covering `iterations_per_quick_update`, `background_quick_update=True`, the new IPython live-cell rendering when running in a Jupyter / Colab kernel, the script-mode fallback (PNGs on disk unchanged), an

### [chore(scripts): Phase 3 use_jax=True consistency in features/search_chaining](https://github.com/PyAutoLabs/autofit_workspace/pull/61) (PyAutoLabs/autofit_workspace)
**Scripts Changed:** - `scripts/features/search_chaining.py` — added `use_jax=True` to all 4 `af.ex.Analysis(...)` calls so the chained pipeline runs the same JAX path as the grid-search sibling

### [feat: add af.NSS section to searches/nest.py tutorial (Phase 5)](https://github.com/PyAutoLabs/autofit_workspace/pull/60) (PyAutoLabs/autofit_workspace)
**Scripts Changed:** - `scripts/searches/nest.py` — added a new **Search: NSS** section after the existing Nautilus section walking through the NSS-specific kwargs (`n_live`, `num_mcmc_steps`, `num_delete`, `termination`, `checkpoint_interval`, `iterations_per_quick_update`); extended the top docstring + Contents block 

### [Disable model.graph output by default](https://github.com/PyAutoLabs/autofit_workspace/pull/56) (PyAutoLabs/autofit_workspace)
**Scripts Changed:** - None — config-only change to `config/output.yaml`.

### [docs: raw-flux latent guide + workspace config updates](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/108) (PyAutoLabs/autogalaxy_workspace)
**Scripts Changed:** - `config/latent.yaml` — Add `total_galaxy_0_flux: true` explicitly alongside the existing `total_galaxy_0_flux_mujy: true`; reflow the comment block to explain the raw / µJy split.
- `scripts/guides/units/flux.py` — New "Latent Variables: Total Flux Directly from the Fit" section. Documents that `l

### [interferometer: switch to TransformerNUFFT + apply_sparse_operator, reduce MGE to 5 Gaussians](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/106) (PyAutoLabs/autogalaxy_workspace)
**API Changes:** None — pure workspace edits.
**Scripts Changed:** - `features/multi_gaussian_expansion/{modeling,fit,likelihood_function}.py`
- `features/pixelization/{modeling,fit,galaxy_reconstruction,many_visibilities_preparation,likelihood_function}.py`

### [config: add quick_update_background + live_visual_update defaults](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/105) (PyAutoLabs/autogalaxy_workspace)
**Scripts Changed:** - `config/general.yaml` — appends `quick_update_background: false` and `live_visual_update: false` under both `updates:` and `hpc:` with explanatory comments.

### [docs: remove Array2D.native jit-blocked caveats from JAX variant blocks](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/104) (PyAutoLabs/autogalaxy_workspace)
**Scripts Changed:** - `scripts/imaging/simulator.py` — removed jit-blocked caveat from JAX variant notes
- `scripts/interferometer/simulator.py` — removed jit-blocked caveat from JAX variant notes

### [docs: __JAX__ in autogalaxy deferred (multi + guides mirror)](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/103) (PyAutoLabs/autogalaxy_workspace)
**Scripts Changed:** - `scripts/multi/start_here.py` — refresh 2 stale `__JAX__` blocks per Phase 0 contract
- `scripts/guides/data_structures.py` — new `__JAX__` covering `.array` story, host transfer, the not-pytree rule + `.array` unwrap-rewrap workaround
- `scripts/guides/galaxies.py` — new `__JAX__` covering Galaxy

### [docs: __JAX__ sections in per-dataset scripts (imaging + interferometer)](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/101) (PyAutoLabs/autogalaxy_workspace)
**Scripts Changed:** - `scripts/imaging/start_here.py` — refresh 2 stale `__JAX__` blocks
- `scripts/imaging/simulator.py` — new `__JAX Variant__` (`SimulatorImaging(use_jax=True)`)
- `scripts/imaging/fit.py` — `__JAX__` prose
- `scripts/imaging/likelihood_function.py` — `__JAX__` section with `@jax.jit` recipe + `Fitne

### [docs: add __JAX__ section to top-level start_here.py](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/99) (PyAutoLabs/autogalaxy_workspace)
**Scripts Changed:** - `start_here.py` — new `__JAX__` section (~70 lines of prose + one illustrative `simulator.via_galaxies_from(use_jax=True)` snippet) inserted after `__Galaxies__`.

### [docs: workspace tutorial for latent variables in autogalaxy_workspace](https://github.com/PyAutoLabs/autogalaxy_workspace/pull/97) (PyAutoLabs/autogalaxy_workspace)
**Scripts Changed:** - `scripts/guides/results/latent_variables.py` (new, ~180 lines) — sections in order: Galaxy Latents in PyAutoGalaxy (the curated catalogue), Toggling Latents (workspace yaml override pattern), Model Fit (quick Nautilus run on the simple dataset with `magzero=25.0`), Loading Latent Results (via `ana

### [docs: raw-flux latent guides + workspace config updates](https://github.com/PyAutoLabs/autolens_workspace/pull/214) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `config/latent.yaml` — Add `total_lens_flux`, `total_lensed_source_flux`, `total_source_flux` (all `true`) to the workspace overrides; reflow the comment block to explain the raw / µJy / dimensionless grouping; add `total_galaxy_0_flux: false` as an explicit cross-library silencer (the autogalaxy 

### [docs: simplify weak/fit.py to load dataset via al.from_json](https://github.com/PyAutoLabs/autolens_workspace/pull/212) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/weak/fit.py` — replaced inline `WeakDataset` reconstruction with `al.from_json(file_path=dataset_path / "dataset.json")`; revised the `__Dataset__` docstring accordingly. (−20 / +5 lines.)

### [interferometer: switch to TransformerNUFFT + apply_sparse_operator, MGE to 5 Gaussians](https://github.com/PyAutoLabs/autolens_workspace/pull/211) (PyAutoLabs/autolens_workspace)
**API Changes:** None — pure workspace edits.
**Scripts Changed:** 22 scripts across `features/{datacube,extra_galaxies,linear_light_profiles,multi_gaussian_expansion,pixelization,subhalo/detect}/` plus 2 READMEs.

### [config: add quick_update_background + live_visual_update defaults](https://github.com/PyAutoLabs/autolens_workspace/pull/210) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `config/general.yaml` — appends `quick_update_background: false` and `live_visual_update: false` under both `updates:` and `hpc:` with explanatory comments.

### [docs: remove Array2D.native jit-blocked caveats from JAX variant blocks](https://github.com/PyAutoLabs/autolens_workspace/pull/208) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/imaging/simulator.py` — removed jit-blocked caveat from JAX variant notes
- `scripts/interferometer/simulator.py` — removed jit-blocked caveat from JAX variant notes
- `scripts/group/simulator.py` — removed jit-blocked caveat from JAX variant notes
- `scripts/point_source/simulator.py` — 

### [docs: __JAX__ in deferred datasets (multi + group + cluster) + cluster simulator migration](https://github.com/PyAutoLabs/autolens_workspace/pull/207) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** **3c — multi (refresh):**
- `scripts/multi/start_here.py` — refresh 2 stale `__JAX__` blocks per Phase 0 contract.

**3e — group (full add):**
- `scripts/group/start_here.py` — refresh 2 stale `__JAX__` blocks
- `scripts/group/simulator.py` — `__JAX Variant__` reference (delegates to `imaging/simula

### [docs: __JAX__ sections in workspace guides (data_structures, galaxies, tracer, lens_calc)](https://github.com/PyAutoLabs/autolens_workspace/pull/205) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/guides/data_structures.py` — `__JAX__` section covering the `.array` story, when backing becomes `jax.Array`, host-transfer mechanics, the not-pytree rule + `.array` unwrap-rewrap workaround.
- `scripts/guides/galaxies.py` — pytree registration for `Galaxy` / `Galaxies` (implicit via Anal

### [docs: __JAX__ sections in per-dataset scripts (imaging + interferometer + point_source)](https://github.com/PyAutoLabs/autolens_workspace/pull/203) (PyAutoLabs/autolens_workspace)
**Scripts Changed:** - `scripts/imaging/start_here.py` — refresh 2 stale `__JAX__` blocks
- `scripts/imaging/simulator.py` — new `__JAX Variant__` (`SimulatorImaging(use_jax=True)`)
- `scripts/imaging/fit.py` — `__JAX__` prose
- `scripts/imaging/likelihood_function.py` — `__JAX__` section with `@jax.jit` recipe + `Fitne
