"""Guard the release wiki-currency checks against PyPI index propagation (#334).

The 2026.11.6.1 and 2026.11.7.1 releases shipped completely but ended red:
autolens_assistant's wiki-currency check ran `pip install autolens==<version>`
about 3 minutes after the upload, before PyPI's simple index listed it. The drift
issue job then failed downloading a report that was never written, and its
fallback would have titled an install failure as "drift".

These tests hold the repaired shape: every wiki check waits for the released
stack on production PyPI, the wait is bounded and cache-free, and a drift job with
no report says the check could not complete instead of claiming drift.
"""

from pathlib import Path

import yaml

RELEASE_WORKFLOW = (
    Path(__file__).resolve().parents[1] / ".github" / "workflows" / "release.yml"
)

PACKAGES = ("autonerves", "autoarray", "autofit", "autogalaxy", "autolens", "autocti")


def jobs():
    return yaml.safe_load(RELEASE_WORKFLOW.read_text())["jobs"]


def wiki_checks(all_jobs):
    return {n: j for n, j in all_jobs.items() if n.startswith("wiki_currency_check")}


def drift_jobs(all_jobs):
    return {n: j for n, j in all_jobs.items() if n.startswith("wiki_drift_issue")}


def test_every_wiki_check_waits_for_the_released_stack():
    all_jobs = jobs()
    checks = wiki_checks(all_jobs)
    assert len(checks) == 4
    for name, job in checks.items():
        assert "wait_for_released_stack" in job["needs"], name


def test_the_wait_runs_after_publish_and_is_skipped_in_rehearsal():
    job = jobs()["wait_for_released_stack"]
    assert "release_workspaces" in job["needs"]
    assert "rehearsal != 'true'" in job["if"]


def test_the_wait_polls_production_pypi_for_every_package_without_cache_and_is_bounded():
    (step,) = [
        s for s in jobs()["wait_for_released_stack"]["steps"]
        if s.get("name", "").startswith("Wait")
    ]
    run = step["run"]
    assert "--index-url https://pypi.org/simple/" in run
    assert "--no-cache-dir" in run
    assert "--no-deps" in run
    for package in PACKAGES:
        assert package in run, package
    # bounded: the loop gives up and fails the job
    assert "-ge 60" in run
    assert "exit 1" in run


def test_drift_jobs_tolerate_a_missing_report_and_never_call_it_drift():
    all_jobs = drift_jobs(jobs())
    assert len(all_jobs) == 4
    for name, job in all_jobs.items():
        (download,) = [s for s in job["steps"] if s.get("name") == "Download drift report"]
        assert download.get("continue-on-error") is True, name
        (open_step,) = [s for s in job["steps"] if s.get("name", "").startswith("Open")]
        run = open_step["run"]
        assert 'if [ ! -f "$BODY" ]' in run, name
        assert "could not complete" in run, name
        assert '--title "$TITLE"' in run, name
