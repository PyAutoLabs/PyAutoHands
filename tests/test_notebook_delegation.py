"""
Cover the notebook-leg behaviours promoted out of the workspace `run_smoke.py`.

These are the behaviours the vendored 356-line workspace runner held that
`build_util` did not, and that a collapsed delegator must not lose:

* the committed `notebooks/` tree stays clean when a smoke gate runs it;
* a genuine failure gets ONE regenerate-from-source retry (stale-notebook
  recovery), and the retry's verdict replaces the first attempt's;
* a TIMEOUT is never retried;
* a clean skip-guard exit is a PASS and never reaches the retry.
"""

import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).parent.parent
AUTOHANDS_DIR = PROJECT_ROOT / "autohands"
sys.path.insert(0, str(AUTOHANDS_DIR))

import build_util  # noqa: E402
from build_util import execute_notebook  # noqa: E402
from result_collector import RunReport, Status  # noqa: E402

nbformat = pytest.importorskip("nbformat")
pytest.importorskip("nbconvert")


def _write_notebook(path: Path, source: str) -> Path:
    nb = nbformat.v4.new_notebook()
    nb.cells = [nbformat.v4.new_code_cell(source)]
    path.parent.mkdir(parents=True, exist_ok=True)
    nbformat.write(nb, path)
    return path


@pytest.fixture
def workspace(tmp_path, monkeypatch):
    (tmp_path / "notebooks").mkdir()
    (tmp_path / "scripts").mkdir()
    monkeypatch.chdir(tmp_path)
    return tmp_path


def _report():
    return RunReport(project="p", directory="notebooks", run_type="notebook")


class TestWriteBack:
    """`write_back` decides whether the committed notebook is modified."""

    def test_write_back_false_leaves_the_notebook_untouched(self, workspace):
        """
        A PR smoke gate must not dirty the tree it is testing.

        run_notebook.py writes executed outputs back in place, which is right
        for generation but wrong for a gate — an unchanged worktree after a
        smoke run is the invariant the workspace copy protected by executing a
        throwaway copy.
        """
        nb = _write_notebook(workspace / "notebooks" / "n.ipynb", "x = 1 + 1")
        before = nb.read_bytes()

        status = execute_notebook(nb, report=_report(), write_back=False)

        assert status == "passed"
        assert nb.read_bytes() == before

    def test_write_back_true_records_outputs(self, workspace):
        """The generation/release contract is unchanged: outputs are kept."""
        nb = _write_notebook(workspace / "notebooks" / "n.ipynb", "print('hi')")
        before = nb.read_bytes()

        status = execute_notebook(nb, report=_report(), write_back=True)

        assert status == "passed"
        assert nb.read_bytes() != before


class TestRegenerateAndRetry:
    """One retry from the source script, and only where it can help."""

    def test_stale_notebook_is_regenerated_and_passes(self, workspace):
        """
        The recovery case: the script moved on, the committed notebook did not.

        The notebook fails; its source script is healthy; regenerating and
        retrying turns the entry green with exactly one recorded result.
        """
        _write_notebook(workspace / "notebooks" / "n.ipynb", "raise RuntimeError('stale')")
        (workspace / "scripts" / "n.py").write_text("x = 1 + 1\n")
        report = _report()

        status = execute_notebook(
            workspace / "notebooks" / "n.ipynb",
            report=report,
            write_back=False,
            retry_from_scripts=workspace / "scripts",
        )

        assert status == "passed"
        # The retry REPLACES the first attempt — one notebook, one result.
        assert len(report.results) == 1
        assert report.results[0].status == Status.PASSED
        # A temp path never leaks into the report.
        assert report.results[0].file.endswith("notebooks/n.ipynb")

    def test_genuinely_broken_notebook_still_fails_after_the_retry(self, workspace):
        """A real bug survives regeneration, and stays one FAIL."""
        _write_notebook(workspace / "notebooks" / "n.ipynb", "raise RuntimeError('boom')")
        (workspace / "scripts" / "n.py").write_text("raise RuntimeError('boom')\n")
        report = _report()

        status = execute_notebook(
            workspace / "notebooks" / "n.ipynb",
            report=report,
            write_back=False,
            retry_from_scripts=workspace / "scripts",
        )

        assert status == "failed"
        assert len(report.results) == 1
        assert report.results[0].status == Status.FAILED

    def test_missing_source_script_leaves_the_first_failure_standing(self, workspace):
        """
        No source to regenerate from: the recovery was unavailable, not the
        notebook fixed. The original FAIL must stand rather than vanish.
        """
        _write_notebook(workspace / "notebooks" / "n.ipynb", "raise RuntimeError('boom')")
        report = _report()

        status = execute_notebook(
            workspace / "notebooks" / "n.ipynb",
            report=report,
            write_back=False,
            retry_from_scripts=workspace / "scripts",
        )

        assert status == "failed"
        assert len(report.results) == 1
        assert report.results[0].status == Status.FAILED

    def test_no_retry_when_not_asked(self, workspace):
        """Without retry_from_scripts the behaviour is exactly as before."""
        _write_notebook(workspace / "notebooks" / "n.ipynb", "raise RuntimeError('boom')")
        (workspace / "scripts" / "n.py").write_text("x = 1\n")
        report = _report()

        status = execute_notebook(
            workspace / "notebooks" / "n.ipynb", report=report, write_back=False
        )

        assert status == "failed"


class TestRetryIsNarrow:
    """A retry is only ever spent where it can change the answer."""

    def test_timeout_is_never_retried(self, workspace, monkeypatch):
        """
        Retrying a timeout burns a second full cap for the same result,
        doubling the slowest entry's cost.
        """
        _write_notebook(workspace / "notebooks" / "n.ipynb", "x = 1")
        (workspace / "scripts" / "n.py").write_text("x = 1\n")
        monkeypatch.setenv("BUILD_SCRIPT_TIMEOUT", "0")

        calls = []
        real = build_util._run_notebook_once

        def counting(*args, **kwargs):
            calls.append(args[0])
            return "timeout"

        monkeypatch.setattr(build_util, "_run_notebook_once", counting)
        status = execute_notebook(
            workspace / "notebooks" / "n.ipynb",
            report=_report(),
            write_back=False,
            retry_from_scripts=workspace / "scripts",
        )

        assert status == "timeout"
        assert len(calls) == 1, "a timeout must not trigger the regenerate-and-retry"
        assert real is not None  # the real implementation is still importable

    def test_clean_skip_exit_passes_without_a_retry(self, workspace, monkeypatch):
        """
        The optional-dependency skip guard is already a PASS, so it must never
        reach the retry path — regenerating it would be pure waste.
        """
        _write_notebook(
            workspace / "notebooks" / "n.ipynb",
            "import sys\nprint('skipping')\nsys.exit(0)",
        )
        (workspace / "scripts" / "n.py").write_text("x = 1\n")
        report = _report()

        calls = []
        real = build_util._run_notebook_once

        def counting(*args, **kwargs):
            calls.append(args[0])
            return real(*args, **kwargs)

        monkeypatch.setattr(build_util, "_run_notebook_once", counting)
        status = execute_notebook(
            workspace / "notebooks" / "n.ipynb",
            report=report,
            write_back=False,
            retry_from_scripts=workspace / "scripts",
        )

        assert status == "passed"
        assert len(calls) == 1
        assert report.results[0].status == Status.PASSED
