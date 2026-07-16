# PyAutoBuild — Agent Guidance

PyAutoBuild is the **executor** of the PyAuto release ecosystem: packaging,
tagging, notebook generation, and PyPI publication via `release.yml`. It runs no
release-readiness checks of its own — that is PyAutoHeart's job.

## The boundary

The organs, boundaries and the `Brain → Heart (gate) → Build (execute)` call
chain are defined once in `PyAutoBrain/ORGANISM.md`. Build's side of it:
**pure executor** — it runs no readiness checks of its own and never
re-derives a gate decision; readiness is gated upstream by the Brain via
`pyauto-heart readiness`.

## What moved out of Build

Release-readiness checking is no longer Build's job. The version-skew gate, the
deep `verify_install` suite, and URL hygiene all live in PyAutoHeart now;
`autobuild verify_install` / `autobuild url_check` / `autobuild watch|status|
tick|fix` are thin shims that delegate to `pyauto-heart`. Build keeps only the
executor primitives (`pre_build`, `generate`, `run*`, `tag_and_merge`,
`bump_colab_urls`, `release.yml`).

See [`docs/internals.md`](docs/internals.md) for the build pipeline, workspace
folder structure, config files, and `release.yml` details. Read it when
changing the pipeline itself, not by default.

<!-- repos_sync:history:begin -->
## Never rewrite history

Never rewrite pushed history on any repo with a remote — no `git init` over a
tracked repo, no force-push to `main`, no fresh-start "Initial commit", no
`filter-repo` / `filter-branch` / `rebase -i` on pushed branches. To get a
clean tree: `git fetch origin && git reset --hard origin/main && git clean -fd`.
<!-- repos_sync:history:end -->
