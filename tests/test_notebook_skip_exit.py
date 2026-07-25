"""Unit tests for the notebook optional-dependency skip guard.

The workspaces guard optional-dependency examples with

    if importlib.util.find_spec("<dep>") is None:
        print("Skipping ...")
        sys.exit(0)

which is a clean exit 0 as a `.py` script but raises `SystemExit` in a Jupyter
kernel, so `jupyter nbconvert --execute` exits non-zero and the notebook is
reported as a failure. `build_util.is_clean_skip_exit` classifies that one case
as a pass; every other exception — including a non-zero `sys.exit` — stays a
failure.

The classifier tests are pure string matching (fast, no kernel). The
end-to-end tests actually execute a one-cell notebook through
`build_util.execute_notebook` and are skipped when `jupyter` is unavailable.
"""

import json
import shutil
import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).parent.parent
AUTOHANDS_DIR = PROJECT_ROOT / "autohands"
sys.path.insert(0, str(AUTOHANDS_DIR))

from build_util import execute_notebook, is_clean_skip_exit  # noqa: E402
from result_collector import Status  # noqa: E402


def _nbconvert_error(cell_source: str, ename: str, evalue: str, ansi: bool = True) -> str:
    """A realistic `jupyter nbconvert --execute` failure message."""
    if ansi:
        terminal = f"\x1b[31m{ename}\x1b[39m\x1b[31m:\x1b[39m {evalue}"
    else:
        terminal = f"{ename}: {evalue}"
    return (
        "[NbConvertApp] Converting notebook example.ipynb to notebook\n"
        "Traceback (most recent call last):\n"
        '  File "nbclient/client.py", line 918, in _check_raise_for_error\n'
        "    raise CellExecutionError.from_cell_and_msg(cell, exec_reply_content)\n"
        "nbclient.exceptions.CellExecutionError: An error occurred while "
        "executing the following cell:\n"
        "------------------\n"
        f"{cell_source}\n"
        "------------------\n\n"
        "An exception has occurred, use %tb to see the full traceback.\n\n"
        f"{terminal}\n\n"
    )


SKIP_CELL = 'import sys\nprint("Skipping BlackJAXNUTS example")\nsys.exit(0)'


# --- classifier ------------------------------------------------------------


@pytest.mark.parametrize("ansi", [True, False])
def test_system_exit_zero_is_a_clean_skip(ansi):
    # The IPython traceback is ANSI-coloured, so escapes must be stripped
    # before the ename line can be matched.
    assert is_clean_skip_exit(_nbconvert_error(SKIP_CELL, "SystemExit", "0", ansi=ansi))


def test_system_exit_nonzero_is_a_failure():
    assert not is_clean_skip_exit(
        _nbconvert_error("import sys\nsys.exit(1)", "SystemExit", "1")
    )


def test_other_exception_is_a_failure():
    assert not is_clean_skip_exit(
        _nbconvert_error("raise ValueError('boom')", "ValueError", "boom")
    )


def test_empty_output_is_a_failure():
    assert not is_clean_skip_exit("")


def test_output_without_a_cell_error_is_a_failure():
    # e.g. nbconvert itself dying before execution — not a skip guard.
    assert not is_clean_skip_exit("[NbConvertApp] ERROR | Notebook not found\n")


def test_skip_guard_followed_by_a_later_real_error_is_a_failure():
    # Defensive: the terminal line must be the SystemExit: 0, so a message
    # that merely mentions it somewhere is not enough.
    output = _nbconvert_error(SKIP_CELL, "SystemExit", "0")
    output += "\nnbclient.exceptions.CellExecutionError: later cell\nValueError: boom\n"
    assert not is_clean_skip_exit(output)


# --- end to end through execute_notebook ------------------------------------


class _Report:
    def __init__(self):
        self.results = []


def _write_notebook(path: Path, source: str) -> None:
    notebook = {
        "cells": [
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": source,
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    path.write_text(json.dumps(notebook), encoding="utf-8")


needs_jupyter = pytest.mark.skipif(
    shutil.which("jupyter") is None, reason="jupyter not installed"
)


@needs_jupyter
def test_execute_notebook_passes_on_system_exit_zero(tmp_path):
    nb = tmp_path / "skip.ipynb"
    _write_notebook(nb, SKIP_CELL)
    report = _Report()
    execute_notebook(str(nb), report=report)
    assert [r.status for r in report.results] == [Status.PASSED]


@needs_jupyter
def test_execute_notebook_fails_on_system_exit_one(tmp_path):
    nb = tmp_path / "fail.ipynb"
    _write_notebook(nb, "import sys\nsys.exit(1)")
    report = _Report()
    execute_notebook(str(nb), report=report)
    assert [r.status for r in report.results] == [Status.FAILED]
