import json
import sys
import os
from pathlib import Path

# Add autohands to path so we can import result_collector
sys.path.insert(0, str(Path(__file__).parent.parent / "autohands"))

from result_collector import Status, ScriptResult, RunReport, parse_no_run_reasons


def test_test_result_to_dict_minimal():
    result = ScriptResult(file="test.py", status=Status.PASSED, duration_seconds=1.5)
    d = result.to_dict()
    assert d["file"] == "test.py"
    assert d["status"] == "passed"
    assert d["duration_seconds"] == 1.5
    assert "error_message" not in d
    assert "traceback" not in d
    assert "skip_reason" not in d


def test_test_result_to_dict_with_error():
    result = ScriptResult(
        file="fail.py",
        status=Status.FAILED,
        duration_seconds=2.3,
        error_message="Something broke",
        traceback="line 1\nline 2\nline 3",
    )
    d = result.to_dict()
    assert d["status"] == "failed"
    assert d["error_message"] == "Something broke"
    assert d["traceback"] == "line 1\nline 2\nline 3"


def test_test_result_traceback_truncation():
    long_tb = "\n".join(f"line {i}" for i in range(200))
    result = ScriptResult(
        file="fail.py",
        status=Status.FAILED,
        traceback=long_tb,
    )
    d = result.to_dict()
    tb_lines = d["traceback"].splitlines()
    assert len(tb_lines) == 100
    assert tb_lines[-1] == "line 199"


def test_test_result_skipped():
    result = ScriptResult(
        file="skip.py",
        status=Status.SKIPPED,
        skip_reason="GUI script",
    )
    d = result.to_dict()
    assert d["status"] == "skipped"
    assert d["skip_reason"] == "GUI script"


def test_run_report_summary():
    report = RunReport(project="autofit", directory="scripts/overview", run_type="script")
    report.results.append(ScriptResult(file="a.py", status=Status.PASSED))
    report.results.append(ScriptResult(file="b.py", status=Status.PASSED))
    report.results.append(ScriptResult(file="c.py", status=Status.FAILED))
    report.results.append(ScriptResult(file="d.py", status=Status.SKIPPED))

    assert report.summary == {"passed": 2, "failed": 1, "skipped": 1}
    assert report.has_failures is True


def test_run_report_no_failures():
    report = RunReport(project="autofit", directory="scripts/overview", run_type="script")
    report.results.append(ScriptResult(file="a.py", status=Status.PASSED))
    report.results.append(ScriptResult(file="b.py", status=Status.SKIPPED))

    assert report.has_failures is False


def test_run_report_write(tmp_path):
    report = RunReport(project="autofit", directory="scripts/overview", run_type="script")
    report.results.append(ScriptResult(file="a.py", status=Status.PASSED, duration_seconds=1.0))
    report.results.append(ScriptResult(file="b.py", status=Status.FAILED, error_message="oops"))

    path = report.write(tmp_path)
    assert path.exists()
    assert path.name == "autofit__scripts__overview__script.json"

    with open(path) as f:
        data = json.load(f)

    assert data["project"] == "autofit"
    assert data["directory"] == "scripts/overview"
    assert data["run_type"] == "script"
    assert data["completed_at"] is not None
    assert len(data["results"]) == 2
    assert data["summary"] == {"passed": 1, "failed": 1}


def test_parse_no_run_reasons():
    config_path = Path(__file__).parent.parent / "autohands" / "config" / "no_run.yaml"
    if not config_path.exists():
        return  # Skip if config not available

    reasons = parse_no_run_reasons(config_path, "autofit")
    assert "get_dist" in reasons
    assert "install" in reasons["get_dist"].lower()

    reasons_lens = parse_no_run_reasons(config_path, "autolens")
    assert "gui/mask" in reasons_lens
    assert "GUI" in reasons_lens["gui/mask"]


def test_parse_no_run_reasons_empty_project():
    config_path = Path(__file__).parent.parent / "autohands" / "config" / "no_run.yaml"
    if not config_path.exists():
        return

    reasons = parse_no_run_reasons(config_path, "autolens_test")
    assert reasons == {}


# --- surface recording (PyAutoHeart#83 §5.3) ----------------------------------

def test_run_report_records_env_profile():
    from result_collector import RunReport
    r = RunReport(
        project="autolens",
        directory="imaging",
        run_type="script",
        env_profile="profile_release.yaml",
    )
    assert r.to_dict()["env_profile"] == "profile_release.yaml"


def test_run_report_env_profile_defaults_to_unknown():
    from result_collector import RunReport
    r = RunReport(project="p", directory="d", run_type="script")
    assert r.to_dict()["env_profile"] == "unknown"


# --- the timing dataset (PyAutoHands#264) -------------------------------------
#
# Repo/project names below are fabricated fixtures, not real workspaces.

import os

from result_collector import TIMINGS_FILENAME, TIMINGS_SCHEMA


def _report(**kwargs):
    defaults = dict(
        project="widgets",
        directory="scripts/demo",
        run_type="script",
        env_profile="profile_smoke.yaml",
    )
    defaults.update(kwargs)
    return RunReport(**defaults)


def test_timings_entry_carries_the_full_row():
    r = ScriptResult(
        file="scripts/demo/alpha.py",
        status=Status.PASSED,
        duration_seconds=12.345,
        cap_seconds=300,
        exit_code=0,
    )
    assert r.to_timings_entry() == {
        "entry": "scripts/demo/alpha.py",
        "kind": "script",
        "status": "passed",
        "seconds": 12.35,
        "cap_s": 300,
        "exit_code": 0,
    }


def test_timings_entry_kind_follows_the_suffix():
    nb = ScriptResult(file="notebooks/demo/alpha.ipynb", status=Status.PASSED,
                      duration_seconds=1.0, cap_seconds=60, exit_code=0)
    assert nb.to_timings_entry()["kind"] == "notebook"


def test_timings_entry_is_workspace_relative(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    absolute = tmp_path / "scripts" / "demo" / "alpha.py"
    r = ScriptResult(file=str(absolute), status=Status.PASSED,
                     duration_seconds=2.0, cap_seconds=300, exit_code=0)
    assert r.to_timings_entry()["entry"] == "scripts/demo/alpha.py"


def test_timeout_entry_records_the_cap_it_hit():
    r = ScriptResult(
        file="scripts/demo/slow.py",
        status=Status.TIMEOUT,
        duration_seconds=300.4,
        cap_seconds=300,
    )
    entry = r.to_timings_entry()
    assert entry["status"] == "timeout"
    assert entry["cap_s"] == 300
    assert entry["seconds"] == 300.4
    # A killed process group chose no exit code.
    assert entry["exit_code"] is None


def test_skipped_entry_is_never_fabricated_as_zero_seconds():
    r = ScriptResult(file="scripts/demo/gui.py", status=Status.SKIPPED,
                     skip_reason="GUI script")
    entry = r.to_timings_entry()
    assert entry["status"] == "skipped"
    assert entry["seconds"] is None
    assert entry["cap_s"] is None


def test_listed_but_missing_entry_is_untimed():
    # Never entered an execution, so its 0.0 duration is the dataclass default,
    # not a measurement.
    r = ScriptResult(file="scripts/demo/gone.py", status=Status.FAILED,
                     error_message="Listed in the script list but not found")
    assert r.to_timings_entry()["seconds"] is None


def test_write_emits_the_timings_file(tmp_path):
    report = _report()
    report.results.append(ScriptResult(file="scripts/demo/alpha.py",
                                       status=Status.PASSED,
                                       duration_seconds=3.0, cap_seconds=300,
                                       exit_code=0))
    report.write(tmp_path)

    data = json.loads((tmp_path / TIMINGS_FILENAME).read_text())
    assert data["schema"] == TIMINGS_SCHEMA
    assert data["project"] == "widgets"
    assert data["directory"] == "scripts/demo"
    assert data["run_type"] == "script"
    assert data["env_profile"] == "profile_smoke.yaml"
    assert data["python"] == f"{sys.version_info.major}.{sys.version_info.minor}"
    assert data["ts"]
    assert [e["entry"] for e in data["entries"]] == ["scripts/demo/alpha.py"]
    assert [leg["run_type"] for leg in data["legs"]] == ["script"]


def test_notebook_leg_does_not_clobber_the_script_leg(tmp_path):
    scripts = _report()
    scripts.results.append(ScriptResult(file="scripts/demo/alpha.py",
                                        status=Status.PASSED,
                                        duration_seconds=3.0, cap_seconds=300,
                                        exit_code=0))
    scripts.write(tmp_path)

    notebooks = _report(directory="notebooks/demo", run_type="notebook")
    notebooks.results.append(ScriptResult(file="notebooks/demo/alpha.ipynb",
                                          status=Status.PASSED,
                                          duration_seconds=9.0, cap_seconds=300,
                                          exit_code=0))
    notebooks.write(tmp_path)

    data = json.loads((tmp_path / TIMINGS_FILENAME).read_text())
    assert [e["entry"] for e in data["entries"]] == [
        "scripts/demo/alpha.py",
        "notebooks/demo/alpha.ipynb",
    ]
    assert [e["kind"] for e in data["entries"]] == ["script", "notebook"]
    assert {leg["run_type"] for leg in data["legs"]} == {"script", "notebook"}


def test_rerunning_one_leg_replaces_its_own_rows(tmp_path):
    first = _report()
    first.results.append(ScriptResult(file="scripts/demo/alpha.py",
                                      status=Status.PASSED,
                                      duration_seconds=3.0, cap_seconds=300,
                                      exit_code=0))
    first.write(tmp_path)

    second = _report()
    second.results.append(ScriptResult(file="scripts/demo/alpha.py",
                                       status=Status.PASSED,
                                       duration_seconds=8.0, cap_seconds=300,
                                       exit_code=0))
    second.write(tmp_path)

    data = json.loads((tmp_path / TIMINGS_FILENAME).read_text())
    assert len(data["entries"]) == 1
    assert data["entries"][0]["seconds"] == 8.0
    assert len(data["legs"]) == 1


def test_corrupt_timings_file_is_replaced_not_fatal(tmp_path):
    (tmp_path).mkdir(parents=True, exist_ok=True)
    (tmp_path / TIMINGS_FILENAME).write_text("{ not json")

    report = _report()
    report.results.append(ScriptResult(file="scripts/demo/alpha.py",
                                       status=Status.PASSED,
                                       duration_seconds=1.0, cap_seconds=300,
                                       exit_code=0))
    report.write(tmp_path)

    data = json.loads((tmp_path / TIMINGS_FILENAME).read_text())
    assert len(data["entries"]) == 1


def test_per_run_json_shape_is_untouched(tmp_path):
    # The published interface PyAutoHeart's script_timing/test_run read.
    report = _report()
    report.results.append(ScriptResult(file="scripts/demo/alpha.py",
                                       status=Status.PASSED,
                                       duration_seconds=3.0, cap_seconds=300,
                                       exit_code=0))
    path = report.write(tmp_path)
    result = json.loads(path.read_text())["results"][0]
    assert set(result) == {"file", "status", "duration_seconds"}


def test_aggregate_ignores_the_timings_file(tmp_path):
    from aggregate_results import aggregate

    report = _report()
    report.results.append(ScriptResult(file="scripts/demo/alpha.py",
                                       status=Status.PASSED,
                                       duration_seconds=3.0, cap_seconds=300,
                                       exit_code=0))
    report.write(tmp_path)

    out = aggregate(tmp_path)
    assert len(out["runs"]) == 1
    assert out["runs"][0]["project"] == "widgets"


# --- the step summary ---------------------------------------------------------


def test_step_summary_table_is_slowest_first(tmp_path, monkeypatch):
    summary = tmp_path / "summary.md"
    monkeypatch.setenv("GITHUB_STEP_SUMMARY", str(summary))

    report = _report()
    report.results.append(ScriptResult(file="scripts/demo/quick.py",
                                       status=Status.PASSED,
                                       duration_seconds=1.5, cap_seconds=300,
                                       exit_code=0))
    report.results.append(ScriptResult(file="scripts/demo/slow.py",
                                       status=Status.TIMEOUT,
                                       duration_seconds=300.4, cap_seconds=300))
    report.results.append(ScriptResult(file="scripts/demo/gui.py",
                                       status=Status.SKIPPED,
                                       skip_reason="GUI script"))
    report.write(tmp_path / "reports")

    text = summary.read_text()
    rows = [line for line in text.splitlines() if line.startswith("| `")]
    assert "slow.py" in rows[0]
    assert "quick.py" in rows[1]
    # Untimed entries sort last and show no fabricated duration.
    assert "gui.py" in rows[2]
    assert "| — |" in rows[2]
    # The cap is shown for the entry it bound, not on every row.
    assert rows[0].endswith("| 300s |")
    assert rows[1].endswith("|  |")
    assert "3 entries" in text
    assert "301.9s total" in text


def test_step_summary_is_appended_by_each_leg(tmp_path, monkeypatch):
    summary = tmp_path / "summary.md"
    monkeypatch.setenv("GITHUB_STEP_SUMMARY", str(summary))

    scripts = _report()
    scripts.results.append(ScriptResult(file="scripts/demo/alpha.py",
                                        status=Status.PASSED,
                                        duration_seconds=1.0, cap_seconds=300,
                                        exit_code=0))
    scripts.write(tmp_path / "reports")

    notebooks = _report(directory="notebooks/demo", run_type="notebook")
    notebooks.results.append(ScriptResult(file="notebooks/demo/alpha.ipynb",
                                          status=Status.PASSED,
                                          duration_seconds=2.0, cap_seconds=300,
                                          exit_code=0))
    notebooks.write(tmp_path / "reports")

    text = summary.read_text()
    assert text.count("### Smoke timings") == 2
    assert "scripts/demo" in text and "notebooks/demo" in text


def test_no_step_summary_off_ci(tmp_path, monkeypatch):
    monkeypatch.delenv("GITHUB_STEP_SUMMARY", raising=False)
    report = _report()
    report.results.append(ScriptResult(file="scripts/demo/alpha.py",
                                       status=Status.PASSED,
                                       duration_seconds=1.0, cap_seconds=300,
                                       exit_code=0))
    assert report.append_step_summary() is False


def test_unwritable_step_summary_does_not_fail_the_run(tmp_path, monkeypatch):
    monkeypatch.setenv("GITHUB_STEP_SUMMARY", str(tmp_path / "nope" / "s.md"))
    report = _report()
    assert report.append_step_summary() is False


# --- the runner records the cap and exit code (build_util) --------------------


def test_execute_script_records_cap_and_exit_code(tmp_path, monkeypatch):
    import build_util

    monkeypatch.chdir(tmp_path)
    script = tmp_path / "ok.py"
    script.write_text("print('hi')\n")

    report = _report()
    env = dict(os.environ, BUILD_SCRIPT_TIMEOUT="77")
    build_util.execute_script(str(script), report=report, env=env)

    result = report.results[0]
    assert result.status == Status.PASSED
    assert result.cap_seconds == 77
    assert result.exit_code == 0
    assert result.to_timings_entry()["cap_s"] == 77


def test_execute_script_records_the_failing_exit_code(tmp_path, monkeypatch):
    import build_util

    monkeypatch.chdir(tmp_path)
    script = tmp_path / "bad.py"
    script.write_text("import sys; sys.exit(3)\n")

    report = _report()
    build_util.execute_script(str(script), report=report, env=dict(os.environ))

    result = report.results[0]
    assert result.status == Status.FAILED
    assert result.exit_code == 3
    assert result.cap_seconds == build_util.timeout_for(None)


# --- both report legs reach the same emission --------------------------------


AUTOHANDS_DIR = Path(__file__).parent.parent / "autohands"


def _fake_workspace(tmp_path):
    """A minimal workspace: an empty exclusion policy and a smoke profile."""
    build = tmp_path / "config" / "build"
    build.mkdir(parents=True)
    (build / "no_run.yaml").write_text("")
    (build / "profile_smoke.yaml").write_text("defaults: {}\noverrides: []\n")
    (tmp_path / "notebooks").mkdir()
    (tmp_path / "scripts").mkdir()
    return tmp_path


def _run_leg(workspace, script, directory):
    import subprocess

    env = dict(os.environ, PYTHONPATH=str(AUTOHANDS_DIR))
    return subprocess.run(
        [sys.executable, str(AUTOHANDS_DIR / script), "widgets", directory,
         "--report-dir", "test-results"],
        cwd=str(workspace), env=env, capture_output=True, text=True,
    )


def test_both_legs_emit_the_timings_file(tmp_path):
    ws = _fake_workspace(tmp_path)

    scripts_leg = _run_leg(ws, "run_python.py", "scripts")
    assert scripts_leg.returncode == 0, scripts_leg.stderr
    notebooks_leg = _run_leg(ws, "run.py", "notebooks")
    assert notebooks_leg.returncode == 0, notebooks_leg.stderr

    data = json.loads((ws / "test-results" / TIMINGS_FILENAME).read_text())
    assert {leg["run_type"] for leg in data["legs"]} == {"script", "notebook"}
    # Both legs state the surface they measured, not "unknown".
    assert {leg["env_profile"] for leg in data["legs"]} == {"profile_smoke.yaml"}
