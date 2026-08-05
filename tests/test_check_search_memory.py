"""Tests for autohands/check_search_memory.py.

Same tmp_path pattern as the other checker tests — build a fake workspace
tree, run the checker, assert on the findings.
"""

import sys
from pathlib import Path

AUTOHANDS_DIR = Path(__file__).parent.parent / "autohands"
sys.path.insert(0, str(AUTOHANDS_DIR))

import check_search_memory  # noqa: E402
from check_search_memory import check_root, findings_in_source, main  # noqa: E402


def _names(source):
    return [f.search for f in findings_in_source(source, Path("x.py"))]


# --- what must be flagged ----------------------------------------------------


def test_flags_the_real_incident():
    # autogalaxy_workspace/scripts/interferometer/start_here.py as it stood
    # when it OOMed the nightly.
    source = (
        "search = af.MultiStartProdigy(\n"
        "    name='start_here',\n"
        "    n_starts=48,\n"
        "    n_steps=300,\n"
        ")\n"
    )
    assert _names(source) == ["MultiStartProdigy"]


def test_flags_every_multi_start_sibling():
    # Matched by prefix, so a new MultiStart* in PyAutoFit is covered on day one.
    for name in (
        "MultiStartProdigy",
        "MultiStartAdam",
        "MultiStartADABelief",
        "MultiStartLion",
        "MultiStartSomethingNotYetWritten",
    ):
        assert _names(f"s = af.{name}(n_starts=48)") == [name]


def test_flags_a_bare_name_call():
    assert _names("s = MultiStartProdigy(n_starts=48)") == ["MultiStartProdigy"]


def test_flags_each_occurrence_separately():
    source = "a = af.MultiStartProdigy()\nb = af.MultiStartAdam()\n"
    assert _names(source) == ["MultiStartProdigy", "MultiStartAdam"]


def test_reports_the_line_number():
    source = "x = 1\n\ns = af.MultiStartProdigy(n_starts=48)\n"
    assert findings_in_source(source, Path("x.py"))[0].line == 3


# --- what must NOT be flagged ------------------------------------------------


def test_explicit_batch_size_passes():
    assert _names("s = af.MultiStartProdigy(n_starts=48, batch_size=4)") == []


def test_explicit_none_passes():
    # The rule is "explicit", not "small" — an intentional single vmap is fine
    # so long as it is typed out where a reviewer sees it.
    assert _names("s = af.MultiStartProdigy(n_starts=48, batch_size=None)") == []


def test_kwargs_splat_passes():
    # batch_size may be inside the dict; do not guess at its contents.
    assert _names("s = af.MultiStartProdigy(**settings)") == []


def test_nautilus_is_not_a_multi_start_search():
    assert _names("s = af.Nautilus(n_live=200)") == []


def test_convergence_object_is_not_a_search():
    # Shares the MultiStart prefix but takes no batch_size.
    assert _names("c = af.MultiStartGradientConvergence(n_stall=20)") == []


def test_prose_mentioning_the_search_is_not_a_call():
    # A naive grep flags this; the AST does not. This exact false positive
    # cost a wrong answer during the #1452 triage, hence the test.
    source = '"""The folder\'s start_here.py instead fits with af.MultiStartProdigy."""\n'
    assert _names(source) == []


def test_syntax_error_is_ignored_not_raised():
    # This checker is not a linter; a broken file is someone else's error.
    assert _names("def (:\n") == []


# --- end to end over a tree --------------------------------------------------


def _workspace(tmp_path, **files):
    ws = tmp_path / "ws"
    for rel, text in files.items():
        p = ws / "scripts" / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)
    (ws / "scripts").mkdir(parents=True, exist_ok=True)
    return ws


def test_check_root_walks_nested_scripts(tmp_path):
    ws = _workspace(
        tmp_path,
        **{
            "interferometer/start_here.py": "s = af.MultiStartProdigy(n_starts=48)\n",
            "interferometer/modeling.py": "s = af.Nautilus()\n",
            "imaging/features/deep/x.py": "s = af.MultiStartAdam()\n",
        },
    )
    found = check_root(ws)
    assert [f.search for f in found] == ["MultiStartAdam", "MultiStartProdigy"]


def test_check_root_clean_workspace(tmp_path):
    ws = _workspace(
        tmp_path,
        **{"interferometer/start_here.py": "s = af.MultiStartProdigy(batch_size=4)\n"},
    )
    assert check_root(ws) == []


def test_main_exit_codes(tmp_path, capsys):
    dirty = _workspace(tmp_path / "a", **{"x.py": "s = af.MultiStartProdigy()\n"})
    assert main(["--root", str(dirty)]) == 1
    assert "no `batch_size`" in capsys.readouterr().out

    clean = _workspace(tmp_path / "b", **{"x.py": "s = af.MultiStartProdigy(batch_size=1)\n"})
    assert main(["--root", str(clean)]) == 0

    assert main(["--root", str(tmp_path / "does_not_exist")]) == 2
