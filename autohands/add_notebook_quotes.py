#!/usr/bin/env python
"""
Usage
./add_notebook_quotes.py /path/to/input /path/to/output
"""

import ast

from typing import Iterable, List, Tuple

from sys import argv


def _narrative_docstring_ranges(lines: List[str]) -> List[Tuple[int, int]]:
    """Locate the narrative docstring blocks of a script, by parsing it.

    Returns ``(start, end)`` 0-based line-index pairs, one per block, in source
    order — ``start`` is the opening-delimiter line, ``end`` the closing one.

    A narrative docstring is a **bare string expression statement at module
    level, written at column 0 with a triple-quote delimiter**. That is the shape
    the notebook generator turns into a markdown cell. Deriving it from the
    parsed source is what separates it from a string *bound to a name*::

        s = '''
        literal
        '''

    whose closing delimiter also sits at column 0. A line-prefix test cannot see
    that opener — it is indented behind ``s = `` — but does match the closer, so
    it reads the literal's end as a docstring boundary and inverts every cell
    boundary after it: the enclosing code cell becomes a ``SyntaxError`` and the
    code that follows is emitted as prose. ``ast`` tells the two apart by node
    type, so the confusion cannot arise.

    Two shapes raise rather than convert, because a wrong guess here silently
    ships a broken notebook — the same reasoning as the stray-``# %%`` guard in
    ``add_notebook_quotes``:

    * a script that does not parse, since there is then no parsed source to
      derive cell boundaries from;
    * a column-0 single-line docstring, whose opening and closing delimiters
      share a line and so cannot bracket a cell. Write them on their own lines.
    """
    try:
        module = ast.parse("".join(lines))
    except SyntaxError as exc:
        where = f"line {exc.lineno}" if exc.lineno else "unknown line"
        raise ValueError(
            f"source script does not parse as Python ({where}: {exc.msg}) — "
            f"notebook cell boundaries are derived from the parsed source, so a "
            f"script that does not compile cannot be converted."
        ) from exc

    ranges: List[Tuple[int, int]] = []
    for node in module.body:
        if not isinstance(node, ast.Expr):
            continue
        value = node.value
        if not (isinstance(value, ast.Constant) and isinstance(value.value, str)):
            continue
        if node.col_offset != 0:
            continue

        start = node.lineno - 1
        end = node.end_lineno - 1
        if not (lines[start].startswith('"""') or lines[start].startswith("'''")):
            # A column-0 string statement written with a single-quote delimiter
            # was never a cell boundary; leave it as code, as it always was.
            continue
        if start == end:
            raise ValueError(
                f"line {start + 1} is a single-line docstring "
                f"({lines[start].strip()!r}) — its opening and closing "
                f"delimiters share a line, so it cannot bracket a notebook "
                f"cell. Write the delimiters on their own lines."
            )
        ranges.append((start, end))
    return ranges


def strip_env_declarations(lines: List[str]) -> List[str]:
    """Remove in-file env declarations before notebook / markdown conversion.

    In-file env declarations are developer-only test-harness configuration
    (docs/env_profile_redesign.md §10) and must never appear in a generated
    notebook or markdown page. The stripped forms:

    * the ``__Env__`` docstring section — a column-0 ``__Env__`` header appended
      anywhere inside a docstring block (the canonical merged form) plus its one
      ``ENV:`` line, through the line before the block's closing delimiter. The
      docstring's earlier prose and its delimiters are PRESERVED; the blank /
      separator line(s) immediately before the header are trimmed. When the
      header is the block's only content (the standalone fallback), or when the
      strip would leave an empty docstring, the whole block is removed;
    * a ``# ENV: ...`` comment line anchored at column 0 — the comment form was
      removed at runtime (it now raises in ``read_env_declaration``), but a stray
      one is still stripped here defensively so it never reaches an artefact.

    Docstring blocks are located by :func:`_narrative_docstring_ranges`, the
    single shared segmentation this module exposes, so a code string literal can
    never be mistaken for one.

    This is the single shared strip layer: ``build_util.py_to_notebook`` routes
    both notebook generation (``generate.py``) and markdown generation
    (``generate_markdown.py``) through ``add_notebook_quotes``, and
    ``navigator.py`` reuses this same segmentation — it calls
    ``add_notebook_quotes`` and reads the delimiters back out — so stripping here
    drops the section from every generated artefact and keeps it out of the
    catalogue.
    """
    blocks = dict(_narrative_docstring_ranges(lines))

    out: List[str] = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        stripped = line.strip()

        # Comment form (removed at runtime): strip a column-0 `# ENV:` defensively.
        if stripped.startswith("# ENV:") and line[:1] == "#":
            i += 1
            continue

        # Docstring block: scan it for a column-0 `__Env__` header appended
        # anywhere inside.
        if i in blocks:
            close = blocks[i]  # closing-delimiter index
            header = None
            for k in range(i + 1, close):
                if lines[k].startswith("__Env__"):
                    header = k
                    break

            if header is not None:
                # Prose kept before the `__Env__` section, with the blank /
                # separator line(s) immediately preceding the header trimmed off.
                kept = list(lines[i + 1 : header])
                while kept and kept[-1].strip() == "":
                    kept.pop()
                if any(seg.strip() for seg in kept):
                    # Merged form: keep the opener, the earlier prose and the
                    # closing delimiter; drop the header through the closer's
                    # preceding line.
                    out.append(line)
                    out.extend(kept)
                    out.append(lines[close])
                # else: the block holds only the `__Env__` section (standalone
                # fallback) or is emptied by the strip — drop it whole.
                i = close + 1
                continue

            # A non-`__Env__` docstring block: emit it unchanged, delimiters too.
            out.extend(lines[i : close + 1])
            i = close + 1
            continue

        out.append(line)
        i += 1

    # A bottom-of-file `__Env__` block leaves dangling blank lines (its leading
    # separator); trim them so the generated artefact ends on real content.
    while out and out[-1].strip() == "":
        out.pop()
    if out and not out[-1].endswith("\n"):
        out[-1] = out[-1] + "\n"
    return out


def add_notebook_quotes(lines: Iterable[str]):
    """
    Add %% above and below docs quotes with triple quotes.

    Cell boundaries are the delimiter lines of the narrative docstring blocks
    found by :func:`_narrative_docstring_ranges`, which parses the script rather
    than testing line prefixes — so a triple-quoted string *assigned in code*,
    whose closing delimiter also sits at column 0, is never mistaken for a
    docstring boundary.

    A closing docstring does not emit its following code-cell marker until a
    non-blank code line is seen. This prevents adjacent docstrings from
    producing an empty code segment whose duplicate ``# %%`` markers are
    interpreted as literal code by ``ipynb-py-convert``.

    ``ipynb-py-convert``'s ``py2nb`` splits cells on the literal
    ``"\n\n# %%\n"`` — the marker must be preceded by a *blank* line. A
    docstring opened on the line immediately after code has only a single
    newline before it, so the split never fires and the marker plus both
    ``'''`` delimiters end up inside the preceding code cell as literal text
    (a ``SyntaxError`` for anyone who runs it). The separator is therefore
    emitted here when it is missing, subject to two constraints: never when
    ``out`` is empty, because ``py2nb`` strips a *leading* ``# %%\n`` header
    and a leading blank line would defeat that strip and yield a spurious
    empty first code cell; and never when the output already ends blank,
    because emitting it unconditionally would append a trailing blank line to
    every code cell in every generated notebook.

    Used for conversion to ipynb notebooks

    Parameters
    ----------
    lines
        An iterable of lines loaded from a notebook file

    Returns
    -------
    Lines with %% inserted before and after docs
    """
    lines = strip_env_declarations(list(lines))

    # A column-0 `# %%` in a *source* script is always a defect: this function
    # is what inserts the cell markers, so a hand-written one collides with the
    # generated marker and `py2nb` silently folds the following docstring into
    # the preceding code cell. Two workspace scripts carried these for years,
    # shipping notebooks whose first code cell was a SyntaxError. Fail loudly
    # rather than laundering it into a broken artefact.
    stray = [n + 1 for n, line in enumerate(lines) if line.rstrip("\r\n") == "# %%"]
    if stray:
        raise ValueError(
            f"source script contains hand-written '# %%' cell marker(s) at "
            f"line(s) {stray} — notebook cell markers are generated, not "
            f"authored. Delete them; the docstring blocks alone define the cells."
        )

    # Re-derived on the stripped lines: dropping an `__Env__` block shifts every
    # line number after it.
    boundaries = set()
    for start, end in _narrative_docstring_ranges(lines):
        boundaries.add(start)
        boundaries.add(end)

    out = list()
    is_in_quotes = False
    pending_code_boundary = False
    pending_lines: List[str] = []

    for index, line in enumerate(lines):
        if index in boundaries:
            if is_in_quotes:
                out.extend(["'''", "\n\n"])
                pending_code_boundary = True
            else:
                if pending_code_boundary:
                    out.extend(pending_lines)
                    pending_lines = []
                    pending_code_boundary = False
                if out and not "".join(out[-3:]).endswith("\n\n"):
                    out.append("\n")
                out.extend(["# %%", "\n", "'''\n"])

            is_in_quotes = not is_in_quotes
        elif pending_code_boundary:
            if line.strip():
                out.append("# %%\n")
                out.extend(pending_lines)
                pending_lines = []
                pending_code_boundary = False
                out.append(line)
            else:
                pending_lines.append(line)
        else:
            out.append(line)

    out.extend(pending_lines)
    return out


if __name__ == "__main__":
    _, in_filename, out_filename = argv

    with open(in_filename) as f:
        lines = f.readlines()

    with open(out_filename, "w+") as f:
        f.writelines(add_notebook_quotes(lines))
