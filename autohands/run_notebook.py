"""
Execute one notebook with the kernel's working directory pinned to the
workspace root.

Why this exists
---------------
``jupyter nbconvert --execute`` starts the kernel in the **notebook's own
directory**, not in the directory nbconvert was launched from. The workspaces
document the opposite convention (autolens_workspace/AGENTS.md: "Scripts are
run from the repository root so relative paths to ``dataset/`` and ``output/``
resolve correctly"), and the auto-simulate guards rely on it::

    if al.util.dataset.should_simulate(str(dataset_path)):
        subprocess.run([sys.executable, "scripts/imaging/simulator.py"], check=True)

That root-relative path resolves from a script run at the root and cannot
resolve from a notebook run in ``notebooks/<topic>/`` — the subprocess exits 2
("can't open file") and every auto-simulating notebook fails.

nbconvert exposes **no CLI flag** for the kernel's working directory. The knob
is ``resources['metadata']['path']``, which nbclient turns into the kernel's
``cwd`` (see ``nbclient/client.py``, ``_async_start_new_kernel``), and that is
reachable only from the Python API. Hence this module: ``build_util`` still
runs it as a **subprocess**, so process isolation, the ``BUILD_SCRIPT_TIMEOUT``
and the per-notebook environment are all unchanged — only the kernel's cwd
moves.

Failure contract
----------------
On a cell error the ``CellExecutionError`` is deliberately left **uncaught** so
Python prints its own traceback to stderr. That output contains the
``CellExecutionError`` marker and ends with the failing cell's terminal
``<ename>: <evalue>`` line, which is exactly what
``build_util.is_clean_skip_exit`` parses to tell an intentional
``sys.exit(0)`` skip from a genuine failure. Do not wrap it in a handler that
reformats the message, or that skip detection breaks.

Usage::

    python run_notebook.py <notebook-path> <workspace-root>
"""

import sys
from pathlib import Path

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor


def run(notebook_path: str, root: str) -> None:
    nb_path = Path(notebook_path)
    nb = nbformat.read(nb_path, as_version=4)

    ep = ExecutePreprocessor(timeout=None, kernel_name="python3")

    try:
        # The whole point: pin the kernel's cwd to the workspace root rather
        # than letting it default to the notebook's own directory.
        ep.preprocess(nb, {"metadata": {"path": str(root)}})
    finally:
        # Write back even on failure so a partially-executed notebook keeps its
        # outputs, matching `nbconvert --output <f> <f>` (which writes in place).
        nbformat.write(nb, nb_path)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"usage: {Path(__file__).name} <notebook-path> <workspace-root>",
              file=sys.stderr)
        sys.exit(2)
    run(sys.argv[1], sys.argv[2])
