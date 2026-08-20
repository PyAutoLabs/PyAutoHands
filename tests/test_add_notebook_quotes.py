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


# A triple-quoted string literal *assigned in code*. Its opener is indented
# behind `s = ` and so is invisible to a line-prefix test, but its closer sits at
# column 0 and does match one — flipping the docstring state and inverting every
# cell boundary that follows. The code cell became an unterminated-string
# SyntaxError and `print(s)` was emitted as narrative prose. Same failure class
# as the opener bug (#211), opposite trigger.
STRING_LITERAL_SCRIPT = (
    '"""\n'
    "__Intro__\n"
    '"""\n'
    "\n"
    "x = 1\n"
    's = """\n'
    "literal\n"
    '"""\n'
    "print(s)\n"
)


# The same shape as it occurs in the wild: a gallery-build script whose
# module-level `CSS` block is closed at column 0 and followed by real code.
GALLERY_STYLE_SCRIPT = (
    '"""\n'
    "__Intro__\n"
    '"""\n'
    "\n"
    'CSS = """\n'
    "body { margin: 0; }\n"
    '"""\n'
    "\n"
    "\n"
    "def build():\n"
    "    return CSS\n"
)


# The single-quote delimiter is equally affected; pin it so a fix that only
# handles `\"\"\"` cannot pass.
SINGLE_QUOTE_LITERAL_SCRIPT = (
    '"""\n'
    "__Intro__\n"
    '"""\n'
    "\n"
    "s = '''\n"
    "literal\n"
    "'''\n"
    "print(s)\n"
)


def test_code_string_literal_closer_is_not_a_cell_boundary():
    converted = "".join(add_notebook_quotes(_lines(STRING_LITERAL_SCRIPT)))

    # The literal must survive intact — delimiters unreplaced, no cell marker
    # injected between them.
    assert 's = """\nliteral\n"""\n' in converted
    assert "print(s)" in converted

    body = converted.split('s = """')[1]
    assert "# %%" not in body.split('"""')[1]


def test_code_string_literal_yields_markdown_then_intact_code_cell(
    tmp_path, monkeypatch
):
    notebook = _notebook_from(
        STRING_LITERAL_SCRIPT, tmp_path, monkeypatch, "string_literal.py"
    )

    assert [cell["cell_type"] for cell in notebook["cells"]] == ["markdown", "code"]

    code = "".join(notebook["cells"][1]["source"])
    assert 's = """\nliteral\n"""' in code
    assert "print(s)" in code

    for cell in notebook["cells"]:
        if cell["cell_type"] == "code":
            source = "".join(cell["source"])
            assert "# %%" not in source
            assert "'''" not in source


def test_code_string_literal_code_cell_is_valid_python(tmp_path, monkeypatch):
    """The regression's real symptom: the cell did not compile."""
    import ast

    notebook = _notebook_from(
        STRING_LITERAL_SCRIPT, tmp_path, monkeypatch, "string_literal_parse.py"
    )

    for cell in notebook["cells"]:
        if cell["cell_type"] == "code":
            ast.parse("".join(cell["source"]))


def test_gallery_style_css_block_is_not_a_cell_boundary(tmp_path, monkeypatch):
    notebook = _notebook_from(
        GALLERY_STYLE_SCRIPT, tmp_path, monkeypatch, "gallery_style.py"
    )

    assert [cell["cell_type"] for cell in notebook["cells"]] == ["markdown", "code"]

    code = "".join(notebook["cells"][1]["source"])
    assert 'CSS = """' in code
    assert "def build():" in code


def test_single_quoted_code_string_literal_is_not_a_cell_boundary():
    converted = "".join(add_notebook_quotes(_lines(SINGLE_QUOTE_LITERAL_SCRIPT)))

    assert "s = '''\nliteral\n'''\n" in converted
    assert "print(s)" in converted


def test_unparseable_source_raises():
    import pytest

    script = '"""\n__Intro__\n"""\n\ndef broken(:\n    pass\n'

    with pytest.raises(ValueError, match="does not parse as Python"):
        add_notebook_quotes(_lines(script))


def test_single_line_docstring_raises():
    import pytest

    script = '"""__Intro__"""\n\nx = 1\n'

    with pytest.raises(ValueError, match="single-line docstring"):
        add_notebook_quotes(_lines(script))


def test_indented_closing_delimiter_still_closes_the_block(tmp_path, monkeypatch):
    """The mirror defect the prefix test also carried.

    A closing delimiter written with leading whitespace did not match
    ``startswith``, so the block never closed and every following line was
    swallowed into the markdown cell. Deriving the span from the parsed source
    closes it regardless of indentation.
    """
    script = '"""\n' "__Intro__\n" ' """\n' "\n" "x = 1\n"

    notebook = _notebook_from(script, tmp_path, monkeypatch, "indented_closer.py")

    assert [cell["cell_type"] for cell in notebook["cells"]] == ["markdown", "code"]
    assert "x = 1" in "".join(notebook["cells"][1]["source"])
