"""Regression tests for narrative-docstring notebook cell boundaries."""

import json
import sys
from pathlib import Path


AUTOHANDS_DIR = Path(__file__).parent.parent / "autohands"
sys.path.insert(0, str(AUTOHANDS_DIR))

from add_notebook_quotes import add_notebook_quotes  # noqa: E402


ADJACENT_SCRIPT = (
    '"""\n'
    "__First__\n"
    '"""\n'
    "\n"
    '"""\n'
    "__Second__\n"
    '"""\n'
    "\n"
    "value = 1\n"
    "\n"
    '"""\n'
    "__Third__\n"
    '"""\n'
)


# A docstring opened on the line *immediately* after code, with no blank line
# between. ``py2nb`` splits on "\n\n# %%\n", so without a separator the marker
# and both delimiters are swallowed into the preceding code cell.
DOCSTRING_AFTER_CODE_SCRIPT = (
    '"""\n'
    "__Intro__\n"
    '"""\n'
    "\n"
    "value = 1\n"
    '"""\n'
    "__Swallowed__\n"
    '"""\n'
    "\n"
    "other = 2\n"
)


# A script whose final segment is code, not a docstring. Workspace examples used
# to append a trailing ``"""\nFinish.\n"""`` block in the belief that this shape
# converted badly; it does not, and this test pins that so the crutch cannot be
# reintroduced.
ENDS_WITH_CODE_SCRIPT = (
    '"""\n'
    "__Intro__\n"
    '"""\n'
    "\n"
    "first = 1\n"
    "\n"
    '"""\n'
    "__Section__\n"
    '"""\n'
    "\n"
    "last = 2\n"
    "print(last)\n"
)


def _lines(text: str):
    return text.splitlines(keepends=True)


def _notebook_from(script_text: str, tmp_path, monkeypatch, name):
    """Convert *script_text* through the real generation chain."""
    import build_util

    script = tmp_path / name
    script.write_text(script_text)
    monkeypatch.chdir(tmp_path)

    return json.loads(build_util.py_to_notebook(script).read_text())


def test_adjacent_docstrings_do_not_emit_an_empty_code_cell_boundary():
    converted = "".join(add_notebook_quotes(_lines(ADJACENT_SCRIPT)))

    assert "# %%\n\n# %%" not in converted
    assert converted.count("# %%") == 4


def test_adjacent_docstrings_generate_separate_markdown_cells(tmp_path, monkeypatch):
    import build_util

    script = tmp_path / "adjacent.py"
    script.write_text(ADJACENT_SCRIPT)
    monkeypatch.chdir(tmp_path)

    notebook_path = build_util.py_to_notebook(script)
    notebook = json.loads(notebook_path.read_text())

    assert [cell["cell_type"] for cell in notebook["cells"]] == [
        "markdown",
        "markdown",
        "code",
        "markdown",
    ]
    assert "__First__" in "".join(notebook["cells"][0]["source"])
    assert "__Second__" in "".join(notebook["cells"][1]["source"])
    assert "value = 1" in "".join(notebook["cells"][2]["source"])

    for cell in notebook["cells"]:
        if cell["cell_type"] == "code":
            source = "".join(cell["source"])
            assert "# %%" not in source
            assert "'''" not in source


def test_docstring_immediately_after_code_is_its_own_markdown_cell(
    tmp_path, monkeypatch
):
    notebook = _notebook_from(
        DOCSTRING_AFTER_CODE_SCRIPT, tmp_path, monkeypatch, "after_code.py"
    )

    assert [cell["cell_type"] for cell in notebook["cells"]] == [
        "markdown",
        "code",
        "markdown",
        "code",
    ]
    assert "__Swallowed__" in "".join(notebook["cells"][2]["source"])

    for cell in notebook["cells"]:
        if cell["cell_type"] == "code":
            source = "".join(cell["source"])
            assert "# %%" not in source
            assert "'''" not in source


def test_script_ending_in_code_keeps_a_complete_final_code_cell(
    tmp_path, monkeypatch
):
    notebook = _notebook_from(
        ENDS_WITH_CODE_SCRIPT, tmp_path, monkeypatch, "ends_with_code.py"
    )

    assert notebook["cells"][-1]["cell_type"] == "code"

    final = "".join(notebook["cells"][-1]["source"])
    assert "last = 2" in final
    assert "print(last)" in final


def test_hand_written_cell_marker_in_source_raises():
    import pytest

    script = "# %%\n" + ENDS_WITH_CODE_SCRIPT

    with pytest.raises(ValueError, match="hand-written '# %%'"):
        add_notebook_quotes(_lines(script))


def test_leading_docstring_does_not_produce_an_empty_first_code_cell(
    tmp_path, monkeypatch
):
    notebook = _notebook_from(
        ENDS_WITH_CODE_SCRIPT, tmp_path, monkeypatch, "leading.py"
    )

    first = notebook["cells"][0]
    assert first["cell_type"] == "markdown"
    assert "__Intro__" in "".join(first["source"])
    assert [cell["cell_type"] for cell in notebook["cells"]].count("markdown") == 2
