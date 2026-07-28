"""Regression tests for the notebook kernel's working directory.

`jupyter nbconvert --execute` starts the kernel in the **notebook's own
directory**, but the workspaces document execution from the repo root and their
auto-simulate guards shell out to root-relative simulator paths::

    if al.util.dataset.should_simulate(str(dataset_path)):
        subprocess.run([sys.executable, "scripts/imaging/simulator.py"], check=True)

Under nbconvert that subprocess exits 2 ("can't open file") and every
auto-simulating notebook fails. `autohands/run_notebook.py` fixes this by
pinning the kernel cwd to the workspace root via
`resources['metadata']['path']`.

These tests lock in the two properties that matter: the kernel really runs at
the given root (not the notebook's directory), and a root-relative subprocess
therefore resolves. They are skipped when a Jupyter kernel is unavailable.
"""

import json
import subprocess
import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).parent.parent
RUNNER = PROJECT_ROOT / "autohands" / "run_notebook.py"

jupyter = pytest.importorskip("nbformat")
pytest.importorskip("nbconvert")


def _write_nb(path: Path, source: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    nb = {
        "cells": [{
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": source,
        }],
        "metadata": {"kernelspec": {
            "display_name": "Python 3", "language": "python", "name": "python3",
        }},
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    path.write_text(json.dumps(nb))


def _outputs(path: Path) -> str:
    nb = json.loads(path.read_text())
    return "".join(
        "".join(o.get("text", "")) for o in nb["cells"][0].get("outputs", [])
    )


def _run(nb_path: Path, root: Path):
    return subprocess.run(
        [sys.executable, str(RUNNER), str(nb_path), str(root)],
        capture_output=True, text=True, timeout=300,
    )


def test_kernel_cwd_is_the_given_root_not_the_notebook_dir(tmp_path):
    """The whole point of the runner: cwd is the root, not notebooks/sub/."""
    nb = tmp_path / "notebooks" / "sub" / "cwd.ipynb"
    _write_nb(nb, 'import os\nprint("CWD:", os.getcwd())')

    result = _run(nb, tmp_path)

    assert result.returncode == 0, result.stderr
    out = _outputs(nb)
    assert f"CWD: {tmp_path}" in out
    # the failure mode this exists to prevent
    assert str(nb.parent) not in out


def test_root_relative_subprocess_resolves(tmp_path):
    """The auto-simulate guard shape: a root-relative script path must run."""
    (tmp_path / "scripts").mkdir(parents=True, exist_ok=True)
    (tmp_path / "scripts" / "sim.py").write_text('print("simulated")')

    nb = tmp_path / "notebooks" / "deep" / "guard.ipynb"
    _write_nb(
        nb,
        "import subprocess, sys\n"
        'r = subprocess.run([sys.executable, "scripts/sim.py"], check=True)\n'
        'print("GUARD_OK")',
    )

    result = _run(nb, tmp_path)

    assert result.returncode == 0, result.stderr
    assert "GUARD_OK" in _outputs(nb)
