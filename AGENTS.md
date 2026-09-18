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

<!-- repos_sync:remote:begin -->
## Remote sessions (Claude Code on web and mobile)

Three facts, measured in a web/mobile container. A session holding several
organs is cwd'd at the repos' *parent*, where no project hook fires, so
nothing has set it up — this block is what does.

- **Bootstrap in the first turn, unconditionally** — before the first test
  command, not as a remedy: `bash PyAutoMind/scripts/session_bootstrap.sh`
  (`--check` reports only). It supplies pytest/PyYAML/xdist and **unshallows
  the clones**, without which `git merge-base --is-ancestor` calls a merged
  branch "not an ancestor" and the close-out acts on it.
- **Run the suite in parallel**: `python3 -m pytest -q -n auto` (4 cores,
  ~3.5x).
- **There is no `gh`, and installing one does not help** — it authenticates,
  then 403s every repo-scoped call through the egress proxy. GitHub is the
  `mcp__github__*` tools; `PyAutoBrain/skills/GITHUB_ACCESS.md` maps each
  `gh` operation onto its tool and is the one full page on the subject.
<!-- repos_sync:remote:end -->

<!-- repos_sync:history:begin -->
## Never rewrite history

Never rewrite pushed history on any repo with a remote — no `git init` over a
tracked repo, no force-push to `main`, no fresh-start "Initial commit", no
`filter-repo` / `filter-branch` / `rebase -i` on pushed branches. To get a
clean tree: `git fetch origin && git reset --hard origin/main && git clean -fd`.
<!-- repos_sync:history:end -->

<!-- repos_sync:deliverable:begin -->
## Sessions end at their deliverable

A session ends when it reports its deliverable — never arm anything that
outlives the turn to wait for CI, a review or a merge: no `send_later`, no
`subscribe_pr_activity`, no `CronCreate`, no `ScheduleWakeup`, no `/loop`, no
`RemoteTrigger` create/update/run. Judge once, report, stop; the human re-runs
`/prm` (or the batch review) when it is green. Measured: five batch members
armed hourly check-ins on 2026-08-31, and a mobile `/prm` re-armed a 60-minute
`send_later` hourly all night on 2026-09-03 with no task active, draining usage.
<!-- repos_sync:deliverable:end -->
