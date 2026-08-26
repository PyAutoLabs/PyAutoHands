# PyAutoHands — Agent Guidance

(The repo was renamed PyAutoBuild → PyAutoHands in 2026-07; the `autohands`
CLI/package name and the *Build* call-chain shorthand were kept — see
[MIGRATION.md](MIGRATION.md) and `PyAutoBrain/ORGANISM.md`.)

PyAutoHands is the **executor** (the Hands) of the PyAuto release ecosystem:
packaging, tagging, notebook generation, and PyPI publication via `release.yml`.
**PyAutoHands executes work on behalf of PyAutoBrain.** It runs no
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
`autohands verify_install` / `autohands url_check` / `autohands watch|status|
tick|fix` are thin shims that delegate to `pyauto-heart`. Build keeps only the
executor primitives: the build/notebook pipeline (`pre_build`, `generate*`,
`run_all` / `run*`), the navigator catalogue and the workspace guards, tagging +
release (`tag_and_merge`, `bump_colab_urls`, `release.yml`), the release-notes
and Slack tooling (`generate_release_notes`, `slack_release_notes`), the release
board (`board`, published by `release_board.yml`), assistant seeding
(`clone_seed`), and `repro_command`. `bin/autohands help` is the **complete**
registry of `autohands/` — every module there is a CLI verb or an
`INTERNAL_MODULES` entry, enforced by `tests/test_autohands_registry.py`, so
read `help` rather than listing verbs here. See `docs/internals.md` for the
pipeline detail.

See [`docs/internals.md`](docs/internals.md) for the build pipeline, workspace
folder structure, config files, and `release.yml` details. Read it when
changing the pipeline itself, not by default.

## Remote sessions: knock on the door first

Measured in a web/mobile container, where this file is loaded and little else is.

- **A session holding several organs registers no SessionStart hook.** Claude
  Code reads project hooks from the project directory, which in that layout is
  the repos' *parent*, not a repo — so none of the Python-3.12 setup runs and
  the session uses the container's 3.11. Knock on the door yourself in the first
  turn:

  ```
  bash PyAutoMind/scripts/session_bootstrap.sh          # fix it
  bash PyAutoMind/scripts/session_bootstrap.sh --check  # report only
  ```

  The symptom of skipping it: collection `ImportError`s naming `yaml`, or
  `No module named pytest`. Both are the session resolving a pytest that is not
  this workspace's — never a broken test module.

- **This repo declares extra deps.** `.claude/session-python.txt` names
  `ipynb-py-convert` and `Pillow` — the same set `tests.yml` installs. The
  bootstrap installs them; without it 14 tests fail on a missing module or a
  missing binary while CI on the same commit is green.

- **Run the suite in parallel.** `pytest-xdist` is a base dep of that bootstrap:
  `python3 -m pytest -q -n auto`. This repo's 406 tests are 27s on one
  core and 13s on four.

<!-- repos_sync:history:begin -->
## Never rewrite history

Never rewrite pushed history on any repo with a remote — no `git init` over a
tracked repo, no force-push to `main`, no fresh-start "Initial commit", no
`filter-repo` / `filter-branch` / `rebase -i` on pushed branches. To get a
clean tree: `git fetch origin && git reset --hard origin/main && git clean -fd`.
<!-- repos_sync:history:end -->
