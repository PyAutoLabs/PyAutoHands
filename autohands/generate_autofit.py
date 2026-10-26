import glob
import os
from pathlib import Path

import build_util
import _workspace

WORKSPACE_PATH = str(_workspace.repo_path(_workspace.workspace_root(), "autofit_workspace"))
PROJECTS_ROOT_PATH = f"{WORKSPACE_PATH}/projects"

PROJECTS_FOLDERS_OMIT = ["config", "dataset", "src"]


def project_scripts():
    """The ``projects/<name>/*.py`` files ``generate_project_folders`` converts."""
    return [
        python_file
        for project_path in map(Path, glob.glob(f"{PROJECTS_ROOT_PATH}/*/"))
        for python_file in map(Path, glob.glob(f"{project_path}/*.py"))
        if python_file.name != "__init__.py"
    ]


def generate_project_folders(inject_gemini=None):
    """
    Convert each ``projects/<name>/*.py`` to a notebook beside it.

    ``inject_gemini(notebook, relpath)``, when given, stamps the notebook's
    Colab Gemini instructions; ``relpath`` is relative to the workspace root.
    """
    for project_path in map(Path, glob.glob(f"{PROJECTS_ROOT_PATH}/*/")):
        try:
            os.remove(project_path / "temp.py")
        except FileNotFoundError:
            pass

        for f in glob.glob(f"{project_path}/*.ipynb*"):
            os.remove(project_path / f)

        for python_file in map(Path, glob.glob(f"{project_path}/*.py")):
            if python_file.name == "__init__.py":
                continue

            new_filename = build_util.py_to_notebook(python_file)
            build_util.inject_colab_setup(new_filename, "autofit")
            if inject_gemini is not None:
                inject_gemini(new_filename, Path(new_filename).relative_to(WORKSPACE_PATH))
            os.system(f"git add -f {new_filename}")
