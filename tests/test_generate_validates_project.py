"""Tests that generate.py validates the project before destroying anything.

`generate.py` clears the whole ``notebooks/`` tree, and until this was fixed the
only rejection of an unknown project happened inside the per-script loop that
runs *after* that rmtree — so running it on an unregistered project deleted 113
tracked notebooks in an unregistered workspace and then aborted. These tests pin the
ordering, since the failure is invisible in a passing run.

Driven as a subprocess: `generate.py` parses argv and does all its work at
module level under ``__main__``, so it cannot be exercised by import.
"""

import os
import subprocess
import sys
from pathlib import Path

AUTOHANDS_DIR = Path(__file__).parent.parent / "autohands"
GENERATE = AUTOHANDS_DIR / "generate.py"

sys.path.insert(0, str(AUTOHANDS_DIR))

import build_util  # noqa: E402


def _make_workspace(root: Path) -> Path:
    """A minimal workspace with a tracked notebooks/ tree, as a real git repo."""
    (root / "scripts" / "imaging").mkdir(parents=True)
    (root / "scripts" / "imaging" / "modeling.py").write_text(
        '"""\nModeling\n========\n\nIntro prose.\n"""\n\nvalue = 1\n'
    )

    notebooks = root / "notebooks" / "imaging"
    notebooks.mkdir(parents=True)
    (notebooks / "modeling.ipynb").write_text('{"cells": [], "nbformat": 4}\n')
    (root / "notebooks" / "README.rst").write_text("Existing index\n")

    subprocess.run(["git", "init", "-q"], cwd=root, check=True)
    subprocess.run(["git", "add", "-A"], cwd=root, check=True)
    subprocess.run(
        ["git", "-c", "user.email=t@t", "-c", "user.name=t", "commit", "-qm", "seed"],
        cwd=root,
        check=True,
    )
    return root


def _run_generate(workspace: Path, project: str):
    env = dict(os.environ, PYTHONPATH=str(AUTOHANDS_DIR))
    return subprocess.run(
        [sys.executable, str(GENERATE), project],
        cwd=workspace,
        capture_output=True,
        text=True,
        env=env,
    )


def test_unknown_project_exits_nonzero_without_touching_notebooks(tmp_path):
    workspace = _make_workspace(tmp_path)

    result = _run_generate(workspace, "autocti")

    assert result.returncode != 0

    # The tree is untouched — this is the regression. Before the fix, `git
    # status` showed every notebook deleted.
    status = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=workspace,
        capture_output=True,
        text=True,
        check=True,
    )
    assert status.stdout == ""
    assert (workspace / "notebooks" / "imaging" / "modeling.ipynb").exists()
    assert (workspace / "notebooks" / "README.rst").exists()

    # ... and no intermediate notebook is stranded beside a source script.
    assert list(workspace.glob("scripts/**/*.ipynb")) == []


def test_unknown_project_message_names_the_project_and_both_registries(tmp_path):
    workspace = _make_workspace(tmp_path)

    message = _run_generate(workspace, "autocti").stderr

    assert "autocti" in message
    assert "COLAB_PROJECTS" in message
    assert "setup_colab" in message
    assert "Nothing was modified" in message
    # The known set is listed, so the reader does not have to go find it.
    for project in build_util.COLAB_PROJECTS:
        assert project in message


def test_known_project_passes_validation_and_regenerates(tmp_path):
    workspace = _make_workspace(tmp_path)

    result = _run_generate(workspace, "autolens")

    assert result.returncode == 0, result.stderr
    assert "unknown project" not in result.stderr

    notebook = workspace / "notebooks" / "imaging" / "modeling.ipynb"
    assert notebook.exists()
    assert "Intro prose." in notebook.read_text()
    assert list(workspace.glob("scripts/**/*.ipynb")) == []
