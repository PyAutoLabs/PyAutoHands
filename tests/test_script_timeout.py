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

A third property, covered by ``TestTimeoutKillsProcessGroup``: the kill must
reach the child's whole process GROUP. ``subprocess.run(timeout=...)`` kills
only the direct child, so a grandchild outlives the cap and keeps running --
over a long mega-run those leak, each holding whatever memory and GPU it had.
``build_util.run_capped`` puts the child in its own session and SIGKILLs the
group instead.
"""

import os
import subprocess
import sys
import time
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


# A faulthandler dump as `kill_group`'s SIGABRT actually produces it: the
# `Fatal Python error` banner, the frames, then the loaded-extension list --
# which on the PyAuto stack is ~1900 characters, i.e. nearly the whole 2000-char
# tail budget. Before the dump-aware split, a hang's own stack was captured by
# the abort and then thrown away by the cap (autolens_workspace_test#287).
_FAULTHANDLER_DUMP = (
    "Fatal Python error: Aborted\n"
    "\n"
    "Current thread 0x00007f3a2c0b4740 (most recent call first):\n"
    '  File "/venv/lib/python3.12/site-packages/jax/_src/array.py", line 401 in _value\n'
    '  File "/venv/lib/python3.12/site-packages/jax/_src/api.py", line 2537 in block_until_ready\n'
    '  File "/work/scripts/multi_dataset/jax_likelihood/delaunay.py", line 208 in <module>\n'
)
_EXTENSION_MODULES = (
    "\nExtension modules: "
    + ", ".join(f"pyauto_ext_module_number_{i:02d}" for i in range(64))
    + " (total: 64)\n"
)


class TestTimeoutOutputKeepsTheAbortStack:
    """The stack the SIGABRT was sent to obtain must reach the report."""

    def test_the_dump_survives_a_noisy_stderr_and_loses_the_module_list(self):
        noise = "chatty library warning line\n" * 120  # >3000 chars of noise
        assert len(noise) > 3000
        assert len(_EXTENSION_MODULES) > 1800
        e = subprocess.TimeoutExpired(
            cmd="x", timeout=1, stderr=noise + _FAULTHANDLER_DUMP + _EXTENSION_MODULES
        )

        out = _timeout_output(e)

        # Every frame of the dump survives, banner included.
        assert "Fatal Python error: Aborted" in out
        assert "Current thread 0x00007f3a2c0b4740" in out
        assert "jax/_src/array.py" in out
        assert "block_until_ready" in out
        assert "delaunay.py" in out and "line 208" in out
        # The extension list -- the thing that used to eat the tail -- is gone.
        assert "Extension modules:" not in out
        assert "pyauto_ext_module_number_00" not in out
        # The noise ahead of the dump is still capped.
        assert "truncated" in out
        assert len(out) < len(noise)

    def test_a_dump_with_no_preceding_noise_is_returned_whole(self):
        e = subprocess.TimeoutExpired(
            cmd="x", timeout=1, stderr=_FAULTHANDLER_DUMP + _EXTENSION_MODULES
        )
        out = _timeout_output(e)
        assert "truncated" not in out
        assert "delaunay.py" in out
        assert "Extension modules:" not in out

    def test_plain_long_stderr_still_truncates_to_the_tail(self):
        # No dump means no change in behaviour: the cap applies as it always has.
        e = subprocess.TimeoutExpired(
            cmd="x", timeout=1, stderr="B" * 50_000 + "THE-LAST-STDERR-LINE"
        )
        out = _timeout_output(e)
        assert "THE-LAST-STDERR-LINE" in out
        assert "truncated" in out
        assert len(out) < 50_000


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


class TestTimeoutKillsProcessGroup:
    """The cap must reap the child's descendants, not just the child."""

    # A script that finishes its own work immediately but leaves a grandchild
    # running and holding the inherited stdout pipe. Under a plain
    # `subprocess.run(timeout=...)` the grandchild survives the cap.
    _SPAWNS_GRANDCHILD = (
        "import subprocess, sys\n"
        "subprocess.Popen([sys.executable, '-c',\n"
        "                  'import time; MARKER_{marker}=1; time.sleep(120)'])\n"
        "print('work done', flush=True)\n"
        "import time; time.sleep(120)\n"
    )

    @staticmethod
    def _alive(marker: str) -> int:
        found = subprocess.run(
            ["pgrep", "-f", f"MARKER_{marker}"], capture_output=True, text=True
        ).stdout
        return len([line for line in found.split() if line.strip()])

    def test_grandchild_is_reaped_at_the_cap(self, tmp_path, monkeypatch, real_interpreter):
        marker = "pyautohands_groupkill"
        monkeypatch.setattr(build_util, "TIMEOUT_SECS", 600)
        script = _write_script(tmp_path, self._SPAWNS_GRANDCHILD.format(marker=marker))

        report = RunReport(project="t", directory="d", run_type="script")
        try:
            execute_script(
                str(script),
                report=report,
                env={**dict(PATH=os.environ.get("PATH", "")), "BUILD_SCRIPT_TIMEOUT": "2"},
            )
            assert report.results[0].status == Status.TIMEOUT
            # The point of the group kill. Without it this is 1: the direct
            # child is dead but its descendant runs on for its full 120s.
            time.sleep(1)
            assert self._alive(marker) == 0
        finally:
            subprocess.run(["pkill", "-f", f"MARKER_{marker}"], capture_output=True)

    def test_run_capped_reports_the_output_captured_before_the_kill(self, tmp_path):
        # The drain after the group kill still has to yield what the child
        # printed -- killing the group is what lets that read reach EOF at all.
        script = _write_script(tmp_path, "print('before the hang', flush=True)\nimport time\ntime.sleep(60)\n")
        with pytest.raises(subprocess.TimeoutExpired) as excinfo:
            build_util.run_capped(
                [sys.executable, str(script)],
                timeout=2,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
        assert "before the hang" in (excinfo.value.output or "")


class TestCappedScriptLeavesAStack:
    """A script killed at its cap must say where it was.

    SIGKILL cannot be caught, so a group killed outright reports nothing --
    which is the whole problem a hang poses. `kill_group` SIGABRTs the child
    first, and with `PYTHONFAULTHANDLER` set (env_config's
    DIAGNOSTIC_ENV_DEFAULTS) that dumps every thread's Python stack to stderr.

    This is the general form of the fit library's `jax_compile.py` watchdog,
    which covers only the first JAX compile and is disarmed as soon as it
    returns -- so a script hanging afterwards leaves nothing at all. See the
    `jax-compile-stall` epic in PyAutoMind.
    """

    _HANGS_IN_A_NAMED_FUNCTION = (
        "import time\n"
        "def the_block_that_hangs():\n"
        "    time.sleep(120)\n"
        "the_block_that_hangs()\n"
    )

    def test_the_dump_names_the_function_the_script_was_parked_in(self, tmp_path):
        script = _write_script(tmp_path, self._HANGS_IN_A_NAMED_FUNCTION)

        with pytest.raises(subprocess.TimeoutExpired) as excinfo:
            build_util.run_capped(
                [sys.executable, str(script)],
                timeout=2,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                env={**os.environ, "PYTHONFAULTHANDLER": "1"},
            )

        output = excinfo.value.output or ""
        assert "the_block_that_hangs" in output

    def test_an_unflushed_print_survives_the_kill_when_unbuffered(self, tmp_path):
        # The real-world case the other tests in this file miss: every one of
        # them passes flush=True, but workspace scripts do not, and a PIPE is
        # block-buffered. Unbuffered, the last line printed survives the kill.
        script = _write_script(
            tmp_path, "print('reached the slow block')\nimport time\ntime.sleep(120)\n"
        )

        with pytest.raises(subprocess.TimeoutExpired) as excinfo:
            build_util.run_capped(
                [sys.executable, str(script)],
                timeout=2,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                env={**os.environ, "PYTHONUNBUFFERED": "1"},
            )

        assert "reached the slow block" in (excinfo.value.output or "")

    def test_without_unbuffered_the_same_print_is_lost(self, tmp_path):
        # Pins WHY the env default is needed rather than just that it is set.
        # If this ever starts passing, the buffering premise has changed and
        # the default can be reconsidered.
        script = _write_script(
            tmp_path, "print('reached the slow block')\nimport time\ntime.sleep(120)\n"
        )
        env = {k: v for k, v in os.environ.items() if k != "PYTHONFAULTHANDLER"}
        env["PYTHONUNBUFFERED"] = ""

        with pytest.raises(subprocess.TimeoutExpired) as excinfo:
            build_util.run_capped(
                [sys.executable, str(script)],
                timeout=2,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                env=env,
            )

        assert "reached the slow block" not in (excinfo.value.output or "")

    def test_the_group_still_dies_even_if_the_abort_is_ignored(self, tmp_path):
        # SIGABRT is best-effort; the SIGKILL after the grace period is not.
        script = _write_script(
            tmp_path,
            "import signal, time\n"
            "signal.signal(signal.SIGABRT, signal.SIG_IGN)\n"
            "time.sleep(120)\n",
        )
        started = time.time()

        with pytest.raises(subprocess.TimeoutExpired):
            build_util.run_capped(
                [sys.executable, str(script)],
                timeout=2,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
            )

        # Capped at 2s, plus at most the abort grace -- never the script's 120s.
        assert time.time() - started < 2 + build_util.ABORT_GRACE_SECS + 10

    def test_an_interrupt_does_not_wait_out_the_grace_period(self, tmp_path):
        # Ctrl-C wants the process gone now; there is no failure to diagnose.
        script = _write_script(
            tmp_path,
            "import signal, time\n"
            "signal.signal(signal.SIGABRT, signal.SIG_IGN)\n"
            "time.sleep(120)\n",
        )
        proc = subprocess.Popen(
            [sys.executable, str(script)],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            start_new_session=True,
        )
        try:
            started = time.time()
            build_util.kill_group(proc, dump_traceback_first=False)
            elapsed = time.time() - started
        finally:
            proc.communicate()

        assert elapsed < build_util.ABORT_GRACE_SECS


def test_the_abort_does_not_leave_a_core_dump(tmp_path, monkeypatch):
    # The SIGABRT kills the child with a core-dumping signal. The stack is
    # already on stderr, so a core adds nothing and a mega-run of them would
    # fill the runner's disk. build_util lowers RLIMIT_CORE at import and
    # children inherit it.
    import resource

    soft, _hard = resource.getrlimit(resource.RLIMIT_CORE)
    assert soft == 0

    script = _write_script(tmp_path, "import time\ntime.sleep(120)\n")
    monkeypatch.chdir(tmp_path)

    with pytest.raises(subprocess.TimeoutExpired):
        build_util.run_capped(
            [sys.executable, str(script)],
            timeout=2,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            env={**os.environ, "PYTHONFAULTHANDLER": "1"},
        )

    assert not list(tmp_path.glob("core*"))
