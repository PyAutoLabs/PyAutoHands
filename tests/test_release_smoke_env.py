"""Guard the release smoke job's env-aware shape (#272).

`run_smoke_tests` in release.yml used to run each `smoke_tests.txt` entry with
a bare `python "scripts/$script"` bash loop under blanket job-level PYAUTO_*
env. That loop never routed through `env_config.py`, so in-file `__Env__`
declarations were silently ignored — `witt_wynne.py` (`ENV: full_datasets`)
failed its verdict assertion deterministically under the job's
PYAUTO_SMALL_DATASETS=1 and turned every otherwise-green LIVE release red
(the 2026-08-29 release, run 33259478535).

The repaired shape routes the job through `autohands/run_python.py --list`,
the same entry point the workspace PR smoke gates and PyAutoHeart's
workspace-validation use, with the workspace's release profile
(`config/build/profile_release.yaml` — the profile pinned for exactly this
"workspace main against TestPyPI wheels" context). These tests hold that
shape so the loop cannot quietly regrow.
"""

from pathlib import Path

import yaml


RELEASE_WORKFLOW = (
    Path(__file__).resolve().parents[1] / ".github" / "workflows" / "release.yml"
)


def smoke_job():
    return yaml.safe_load(RELEASE_WORKFLOW.read_text())["jobs"]["run_smoke_tests"]


def smoke_run_step(job):
    (step,) = [s for s in job["steps"] if s.get("name") == "Run smoke tests"]
    return step


def test_smoke_job_checks_out_the_runner_repo():
    """The env-aware runner lives in this repo, so the job must check out
    PyAutoHands itself beside the workspace checkout (a checkout step with no
    `repository:` key defaults to the repo running the workflow)."""
    checkouts = [
        s
        for s in smoke_job()["steps"]
        if str(s.get("uses", "")).startswith("actions/checkout")
    ]

    self_checkouts = [s for s in checkouts if "repository" not in s.get("with", {})]
    assert [s["with"]["path"] for s in self_checkouts] == ["PyAutoHands"]


def test_smoke_step_routes_through_the_env_aware_runner():
    """The smoke run must go through run_python.py with the release profile:
    --list keeps the curated allowlist, --env-config pins the release-context
    profile (version-check skip included), and --report-dir is load-bearing —
    without a report the runner cannot propagate failures and exits 0."""
    run = smoke_run_step(smoke_job())["run"]

    assert "autohands/run_python.py" in run
    assert "--list smoke_tests.txt" in run
    assert "--env-config config/build/profile_release.yaml" in run
    assert "--report-dir" in run


def test_smoke_step_has_no_bare_script_loop():
    """The old loop ran scripts with the job's blanket env, ignoring `__Env__`
    declarations. It must not regrow beside (or instead of) the runner."""
    run = smoke_run_step(smoke_job())["run"]

    assert 'python "scripts/$script"' not in run
    assert "while IFS=" not in run


def test_smoke_job_env_owns_no_pyauto_vars():
    """PYAUTO_* behaviour now belongs to the workspace's release profile: a
    job-level PYAUTO_ var would be scrubbed by env_config's managed-prefix
    scrub on the runner path, so one reappearing here is dead-at-best and
    misleading-at-worst (it WOULD govern any future step that bypasses the
    runner — the exact drift #272 repaired)."""
    pyauto_keys = [k for k in smoke_job().get("env", {}) if k.startswith("PYAUTO_")]
    assert pyauto_keys == []


def test_smoke_step_fails_loudly_without_a_release_profile():
    """A workspace listing smoke tests but carrying no release profile has no
    env policy for this job; that is a config error to surface, never a
    silent fallback to the runner's ambient env."""
    run = smoke_run_step(smoke_job())["run"]

    assert "config/build/profile_release.yaml" in run
    assert "::error::" in run
