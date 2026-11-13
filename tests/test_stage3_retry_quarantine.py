"""
Stage 3's one script retry and the quarantine skip (PyAutoHeart#344).

Human ruling, 2026-11-12: a Stage 3 script that fails is re-run once; a pass
on the retry is recorded as flaky, not hidden; a second failure stays red. A
quarantined script (an ACTIVE entry Heart resolved: bug ref, expiry) is
skipped and recorded, never run. Heart owns the expiry / bug-ref / 3-entry
rules and the YELLOW; these tests pin the runner's half.
"""

import json
import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).parent.parent
AUTOHANDS_DIR = PROJECT_ROOT / "autohands"
sys.path.insert(0, str(AUTOHANDS_DIR))

import aggregate_results  # noqa: E402
from build_util import execute_scripts_in_folder  # noqa: E402
from result_collector import RunReport, Status  # noqa: E402

# Fails on its first run, passes on every later one (a marker file records
# that it ran) — a flake.
FLAKY = """
from pathlib import Path
marker = Path(__file__).with_suffix(".ran")
if not marker.exists():
    marker.write_text("1")
    raise SystemExit("first attempt: transient failure")
"""
BROKEN = 'raise RuntimeError("really broken")\n'


@pytest.fixture
def workspace(tmp_path, monkeypatch):
    scripts = tmp_path / "scripts"
    scripts.mkdir()
    (scripts / "flaky.py").write_text(FLAKY)
    (scripts / "broken.py").write_text(BROKEN)
    (scripts / "fine.py").write_text("")
    monkeypatch.chdir(tmp_path)
    return tmp_path


def _run(**kw):
    report = RunReport(project="demo", directory="scripts", run_type="script")
    execute_scripts_in_folder(directory="scripts", report=report, **kw)
    return {Path(r.file).name: r for r in report.results}, report


def test_witness_344_retry_pass_is_recorded_as_flaky(workspace):
    results, report = _run(retry_failed=True)
    r = results["flaky.py"]
    assert r.status == Status.PASSED
    assert r.flaky is True and r.attempts == 2
    assert "transient failure" in r.first_error
    d = r.to_dict()
    assert d["flaky"] is True and d["attempts"] == 2 and "first_error" in d
    assert "## Flaky" in report.to_markdown()
    # One entry per script: the first attempt is replaced, not double-counted.
    assert len(report.results) == 3


def test_witness_344_retry_fail_is_recorded_red(workspace):
    results, report = _run(retry_failed=True)
    r = results["broken.py"]
    assert r.status == Status.FAILED and r.attempts == 2 and r.flaky is False
    assert report.has_failures


def test_without_the_flag_nothing_is_retried(workspace):
    results, _ = _run()
    assert results["flaky.py"].status == Status.FAILED
    assert results["flaky.py"].attempts == 1
    # A passing entry carries none of the new keys: the per-run JSON is unchanged.
    assert set(results["fine.py"].to_dict()) == {"file", "status", "duration_seconds"}


def test_a_quarantined_script_is_skipped_and_recorded_not_run(workspace):
    q = [{"script": "scripts/broken.py", "bug": "PyAutoDemo#7", "expires": "2026-11-19"}]
    results, report = _run(retry_failed=True, quarantine=q)
    r = results["broken.py"]
    assert r.status == Status.SKIPPED and r.quarantined == "PyAutoDemo#7"
    assert "quarantined: PyAutoDemo#7" in r.skip_reason
    assert not report.has_failures


def test_aggregate_carries_flaky_and_quarantined(workspace, tmp_path, monkeypatch):
    monkeypatch.setattr(aggregate_results, "fetch_merged_prs", lambda: [])  # no network
    q = [{"script": "scripts/broken.py", "bug": "PyAutoDemo#7", "expires": "2026-11-19"}]
    _, report = _run(retry_failed=True, quarantine=q)
    out = tmp_path / "results"
    report.write(out)
    agg = aggregate_results.aggregate(out)
    assert agg["ready"] is True
    assert [Path(e["file"]).name for e in agg["flaky"]] == ["flaky.py"]
    assert [e["quarantined"] for e in agg["quarantined"]] == ["PyAutoDemo#7"]
    md = aggregate_results.generate_markdown(agg)
    assert "Flaky" in md and "Quarantined" in md
