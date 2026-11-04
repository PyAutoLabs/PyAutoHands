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


# A project name no registry knows. This was "autocti" until CTI joined
# COLAB_PROJECTS (cti-upkeep phase 1, PyAutoHands#332); any unregistered name
# exercises the same validate-before-rmtree ordering.
UNKNOWN_PROJECT = "notaproject"


def test_unknown_project_exits_nonzero_without_touching_notebooks(tmp_path):
    workspace = _make_workspace(tmp_path)

    result = _run_generate(workspace, UNKNOWN_PROJECT)

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

    message = _run_generate(workspace, UNKNOWN_PROJECT).stderr

    assert UNKNOWN_PROJECT in message
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


def _path_without_converter(tmp_path: Path) -> str:
    """A PATH holding git but no ipynb-py-convert (PyAutoHands#330)."""
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    git = subprocess.run(["which", "git"], capture_output=True, text=True, check=True)
    (bin_dir / "git").symlink_to(git.stdout.strip())
    return str(bin_dir)


def test_missing_converter_exits_nonzero_without_touching_anything(tmp_path):
    workspace = _make_workspace(tmp_path / "ws")
    # A root start_here pair: generate removes start_here*.ipynb before it
    # converts, which is what a missing converter used to strand.
    (workspace / "start_here.py").write_text('"""\nStart\n=====\n"""\n\nvalue = 1\n')
    (workspace / "start_here.ipynb").write_text('{"cells": [], "nbformat": 4}\n')
    subprocess.run(["git", "add", "-A"], cwd=workspace, check=True)
    subprocess.run(
        ["git", "-c", "user.email=t@t", "-c", "user.name=t", "commit", "-qm", "start_here"],
        cwd=workspace,
        check=True,
    )

    env = dict(
        os.environ,
        PYTHONPATH=str(AUTOHANDS_DIR),
        PATH=_path_without_converter(tmp_path),
    )
    result = subprocess.run(
        [sys.executable, str(GENERATE), "autolens"],
        cwd=workspace,
        capture_output=True,
        text=True,
        env=env,
    )

    assert result.returncode != 0
    assert "ipynb-py-convert" in result.stderr
    assert "Nothing was modified" in result.stderr

    status = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=workspace,
        capture_output=True,
        text=True,
        check=True,
    )
    assert status.stdout == ""
    assert (workspace / "start_here.ipynb").exists()
    assert not (workspace / "temp.py").exists()


def _git(cwd, *args):
    subprocess.run(
        ["git", "-c", "user.email=t@t", "-c", "user.name=t", *args],
        cwd=cwd,
        check=True,
        capture_output=True,
    )


def test_assistant_behind_origin_counts_local_lag(tmp_path):
    origin = tmp_path / "origin"
    origin.mkdir()
    _git(origin, "init", "-q", "-b", "main")
    _git(origin, "commit", "-q", "--allow-empty", "-m", "one")
    clone = tmp_path / "clone"
    _git(tmp_path, "clone", "-q", str(origin), str(clone))

    assert build_util.assistant_behind_origin(clone) == 0

    _git(origin, "commit", "-q", "--allow-empty", "-m", "two")
    _git(origin, "commit", "-q", "--allow-empty", "-m", "three")
    _git(clone, "fetch", "-q")

    assert build_util.assistant_behind_origin(clone) == 2


def test_assistant_behind_origin_is_none_outside_git(tmp_path):
    assert build_util.assistant_behind_origin(tmp_path) is None
