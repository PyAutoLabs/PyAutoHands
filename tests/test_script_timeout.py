"""Unit tests for the per-script timeout budget.

``BUILD_SCRIPT_TIMEOUT`` used to be read once at import into
``build_util.TIMEOUT_SECS`` and applied directly as the
``subprocess.run(timeout=...)`` kill timer. The per-script environment built by
``env_config.build_env_for_script`` is handed to the CHILD, so a profile that
set ``BUILD_SCRIPT_TIMEOUT`` on an ``overrides`` pattern was silently ignored:
the parent's timer never saw it. ``build_util.timeout_for`` closes that gap by
resolving the value parent-side.

Two properties matter and are both covered end-to-end (a real subprocess that
sleeps past its cap), not just at the resolver:

1. a matching script is killed at its OWN cap, not the global one, and
2. a non-matching script is unaffected.

The timeout report also has to preserve the child's captured output. A killed
script cannot report its own progress, so without that tail a TIMEOUT cannot
say which block was executing — the reason the three jax_grad timeouts could
not be diagnosed from CI artefacts at all (PyAutoHands#226).
"""

import os
import subprocess
import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).parent.parent
AUTOHANDS_DIR = PROJECT_ROOT / "autohands"
sys.path.insert(0, str(AUTOHANDS_DIR))

import build_util  # noqa: E402
from build_util import _timeout_output, execute_script, timeout_for  # noqa: E402
from result_collector import RunReport, Status  # noqa: E402


class TestTimeoutFor:
    """Resolution of the effective per-run cap."""

    def test_no_env_uses_global(self):
        assert timeout_for(None) == build_util.TIMEOUT_SECS

    def test_empty_env_uses_global(self):
        assert timeout_for({}) == build_util.TIMEOUT_SECS

    def test_env_without_the_var_uses_global(self):
        assert timeout_for({"PYAUTO_TEST_MODE": "2"}) == build_util.TIMEOUT_SECS

    def test_profile_value_wins(self):
        assert timeout_for({"BUILD_SCRIPT_TIMEOUT": "1800"}) == 1800

    def test_profile_value_may_lower_the_cap(self):
        # Nothing special about raising: a profile may also tighten a cap.
        assert timeout_for({"BUILD_SCRIPT_TIMEOUT": "5"}) == 5

    @pytest.mark.parametrize("bad", ["", "abc", "12.5", "None", " "])
    def test_malformed_falls_back_to_global(self, bad):
        # A bad profile entry must never disable the cap entirely.
        assert timeout_for({"BUILD_SCRIPT_TIMEOUT": bad}) == build_util.TIMEOUT_SECS

    @pytest.mark.parametrize("bad", ["0", "-1", "-1800"])
    def test_zero_or_negative_falls_back_to_global(self, bad):
        # subprocess.run(timeout=0) would kill instantly and timeout<0 raises;
        # both must degrade to the global cap rather than break the run.
        assert timeout_for({"BUILD_SCRIPT_TIMEOUT": bad}) == build_util.TIMEOUT_SECS

    def test_precedence_profile_over_ambient_global(self, monkeypatch):
        # run_all exports BUILD_SCRIPT_TIMEOUT unconditionally, even when 300
        # was only its CLI default, so the parent cannot distinguish a
        # deliberate operator cap from the default. The profile value therefore
        # wins -- otherwise per-script budgets would work under CI and be
        # silently ignored under run_all.
        monkeypatch.setattr(build_util, "TIMEOUT_SECS", 300)
        assert timeout_for({"BUILD_SCRIPT_TIMEOUT": "1800"}) == 1800

    def test_release_global_applies_when_no_override_matches(self, monkeypatch):
        # mode=release exports 1800 globally; a script with no profile override
        # must still get 1800, not the 300 default.
        monkeypatch.setattr(build_util, "TIMEOUT_SECS", 1800)
        assert timeout_for({"PYAUTO_TEST_MODE": "0"}) == 1800


class TestTimeoutOutput:
    """The captured tail rendered into the TIMEOUT report."""

    def test_none_streams_render_empty(self):
        e = subprocess.TimeoutExpired(cmd="x", timeout=1)
        assert _timeout_output(e) == ""

    def test_stdout_is_labelled(self):
        e = subprocess.TimeoutExpired(cmd="x", timeout=1, output="=== variant 3 ===")
        out = _timeout_output(e)
        assert "last stdout before timeout" in out
        assert "=== variant 3 ===" in out

    def test_bytes_are_decoded(self):
        e = subprocess.TimeoutExpired(cmd="x", timeout=1, output=b"block C")
        assert "block C" in _timeout_output(e)

    def test_undecodable_bytes_do_not_raise(self):
        e = subprocess.TimeoutExpired(cmd="x", timeout=1, output=b"\xff\xfeblock C")
        assert "block C" in _timeout_output(e)

    def test_long_output_is_truncated_keeping_the_tail(self):
        # The TAIL is what identifies the block that was running when killed.
        e = subprocess.TimeoutExpired(
            cmd="x",
            timeout=1,
            output="A" * 50_000 + "THE-LAST-BLOCK",
        )
        out = _timeout_output(e)
        assert "THE-LAST-BLOCK" in out
        assert "truncated" in out
        assert len(out) < 50_000

    def test_both_streams_present(self):
        e = subprocess.TimeoutExpired(
            cmd="x", timeout=1, output="on stdout", stderr="on stderr"
        )
        out = _timeout_output(e)
        assert "on stdout" in out
        assert "on stderr" in out


def _write_script(tmp_path: Path, body: str) -> Path:
    script = tmp_path / "script.py"
    script.write_text(body)
    return script


@pytest.fixture
def real_interpreter(monkeypatch):
    """Run children with THIS interpreter.

    ``execute_script`` shells out to ``BUILD_PYTHON_INTERPRETER`` ("python3"),
    which is resolved via PATH -- and these tests pass a deliberately minimal
    env. Pin the absolute interpreter so the subprocess is found regardless.
    """
    monkeypatch.setattr(build_util, "BUILD_PYTHON_INTERPRETER", sys.executable)


class TestExecuteScriptTimeout:
    """End-to-end: a real subprocess killed at the resolved cap."""

    def test_per_script_env_overrides_the_global_cap(self, tmp_path, monkeypatch, real_interpreter):
        # Global cap is generous; the profile tightens it to 1s. If the parent
        # ignored the per-script value (the bug), this script would run to
        # completion and PASS instead of timing out.
        monkeypatch.setattr(build_util, "TIMEOUT_SECS", 600)
        script = _write_script(tmp_path, "import time\ntime.sleep(30)\n")

        report = RunReport(project="t", directory="d", run_type="script")
        execute_script(
            str(script),
            report=report,
            env={**dict(PATH=os.environ.get("PATH", "")), "BUILD_SCRIPT_TIMEOUT": "1"},
        )

        assert len(report.results) == 1
        assert report.results[0].status == Status.TIMEOUT

    def test_non_matching_script_keeps_the_global_cap(self, tmp_path, monkeypatch, real_interpreter):
        # The mirror of the test above: with no per-script value the generous
        # global applies and a quick script simply passes.
        monkeypatch.setattr(build_util, "TIMEOUT_SECS", 600)
        script = _write_script(tmp_path, "print('done')\n")

        report = RunReport(project="t", directory="d", run_type="script")
        execute_script(str(script), report=report, env=dict(PATH=os.environ.get("PATH", "")))

        assert len(report.results) == 1
        assert report.results[0].status == Status.PASSED

    def test_timeout_message_records_the_cap_in_force(self, tmp_path, monkeypatch, real_interpreter):
        # Which cap was enforced must be self-describing in the artefact --
        # otherwise a future TIMEOUT is as ambiguous as the ones that prompted
        # this change.
        monkeypatch.setattr(build_util, "TIMEOUT_SECS", 600)
        script = _write_script(tmp_path, "import time\ntime.sleep(30)\n")

        report = RunReport(project="t", directory="d", run_type="script")
        execute_script(
            str(script),
            report=report,
            env={**dict(PATH=os.environ.get("PATH", "")), "BUILD_SCRIPT_TIMEOUT": "1"},
        )

        assert "cap 1s" in report.results[0].error_message

    def test_timeout_preserves_child_stdout(self, tmp_path, monkeypatch, real_interpreter):
        # The whole point: the tail names the block that was running.
        monkeypatch.setattr(build_util, "TIMEOUT_SECS", 600)
        script = _write_script(
            tmp_path,
            "import time\nprint('=== variant 3 ===', flush=True)\ntime.sleep(30)\n",
        )

        report = RunReport(project="t", directory="d", run_type="script")
        execute_script(
            str(script),
            report=report,
            env={**dict(PATH=os.environ.get("PATH", "")), "BUILD_SCRIPT_TIMEOUT": "2"},
        )

        message = report.results[0].error_message
        assert report.results[0].status == Status.TIMEOUT
        assert "=== variant 3 ===" in message
