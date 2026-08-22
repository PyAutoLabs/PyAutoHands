"""Regression tests for leg 2 of the dataset-allowlist guard.

Leg 1 asserts nothing *generated* got committed. Leg 2 asserts nothing
*committed* gets deleted: ``should_simulate`` ends in ``shutil.rmtree``, so a
script that reaches a committed dataset while ``PYAUTO_SMALL_DATASETS=1`` is
still in force destroys data the allowlist exists to protect.

Two properties matter more than coverage, and both are locked in here:

- **No false positives.** This runs in ``pre_build``; a spurious failure blocks a
  release. The predicate is "rmtree would delete tracked files", NOT "the path
  sits under an allowlist prefix" — those differ, and the prefix form flagged six
  safe call sites in a real workspace (see the regression test below).
- **No silent under-reporting.** An argument the resolver cannot evaluate is
  reported and skipped, never guessed.
"""

import ast

from autohands.check_dataset_allowlist import (
    UNRESOLVED,
    _module_assignments,
    _names_before,
    _releasing_tokens,
    _resolve,
)


def _resolve_call_arg(src: str):
    """Resolve the first ``should_simulate`` argument in ``src``."""
    tree = ast.parse(src)
    assignments = _module_assignments(tree)
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            func = node.func
            name = func.attr if isinstance(func, ast.Attribute) else getattr(func, "id", "")
            if name == "should_simulate" and node.args:
                return _resolve(node.args[0], _names_before(assignments, node.lineno))
    raise AssertionError("no should_simulate call in source")


# --- resolver ---------------------------------------------------------------


def test_resolves_multi_argument_path():
    """`Path("dataset", "multi_galaxy", name)` is the dominant workspace idiom.

    Handling only the single-argument form left ~31% of the call sites in the
    largest workspace unresolved.
    """
    src = (
        'from pathlib import Path\n'
        'dataset_name = "simple"\n'
        'dataset_path = Path("dataset", "multi_galaxy", dataset_name)\n'
        'should_simulate(str(dataset_path))\n'
    )
    assert _resolve_call_arg(src) == "dataset/multi_galaxy/simple"


def test_resolves_truediv_chain_and_os_path_join():
    div = (
        'from pathlib import Path\n'
        'p = Path("dataset") / "point_source" / "simple"\n'
        'should_simulate(str(p))\n'
    )
    join = (
        'from os import path\n'
        'name = "simple"\n'
        'p = path.join("dataset", "point_source", name)\n'
        'should_simulate(p)\n'
    )
    assert _resolve_call_arg(div) == "dataset/point_source/simple"
    assert _resolve_call_arg(join) == "dataset/point_source/simple"


def test_reassignment_resolves_to_the_binding_in_force_at_the_call_site():
    """These scripts reassign `dataset_name` between sections; each call site
    must see the value above it, not the file's last one."""
    src = (
        'from pathlib import Path\n'
        'dataset_name = "first"\n'
        'should_simulate(str(Path("dataset", dataset_name)))\n'
        'dataset_name = "second"\n'
    )
    assert _resolve_call_arg(src) == "dataset/first"


def test_unknown_expression_is_unresolved_not_guessed():
    """A name the resolver cannot evaluate must yield UNRESOLVED — the caller
    reports and skips it rather than matching on a partial path."""
    src = (
        'from pathlib import Path\n'
        'dataset_name = compute_name()\n'
        'should_simulate(str(Path("dataset", dataset_name)))\n'
    )
    assert _resolve_call_arg(src) is UNRESOLVED


def test_assignment_inside_a_function_is_not_treated_as_module_scope():
    """Only top-level bindings are positionally knowable."""
    src = (
        'from pathlib import Path\n'
        'def f():\n'
        '    dataset_name = "inner"\n'
        'should_simulate(str(Path("dataset", dataset_name)))\n'
    )
    assert _resolve_call_arg(src) is UNRESOLVED


# --- releasing-token derivation ---------------------------------------------


def test_releasing_tokens_derived_from_the_token_map_not_hardcoded():
    """Must include the superset token `real_output`, which releases all four
    managed vars — miscounting it as non-releasing is the easy error."""
    from autohands.env_config import ENV_DECLARATION_TOKENS

    releasing = _releasing_tokens()

    assert "full_datasets" in releasing
    assert "real_output" in releasing
    assert "real_plots" not in releasing
    assert releasing == {
        tok
        for tok, vars_ in ENV_DECLARATION_TOKENS.items()
        if "PYAUTO_SMALL_DATASETS" in vars_
    }


# --- the containment predicate (end-to-end) ---------------------------------


def _run_check(tmp_path, monkeypatch, script_src, tracked, capsys):
    """Drive check_capped_deletion over one synthetic script."""
    from autohands import check_dataset_allowlist as guard

    script = tmp_path / "script.py"
    script.write_text(script_src)
    monkeypatch.setattr(guard, "tracked_python_files", lambda: [str(script)])
    monkeypatch.chdir(tmp_path)

    code = guard.check_capped_deletion(["dataset/overview"], tracked)
    return code, capsys.readouterr()


def test_sibling_dir_holding_no_tracked_files_is_not_a_violation(
    tmp_path, monkeypatch, capsys
):
    """The real shape that exposed the bad predicate: a workspace commits doc
    images directly in `dataset/<section>/`, while its scripts regenerate a
    sibling `dataset/<section>/<generated>/` that holds nothing tracked.

    Deleting that destroys nothing. Prefix matching against the allowlist called
    all six such call sites release-blocking failures; containment does not.
    """
    src = (
        'from pathlib import Path\n'
        'p = Path("dataset", "overview", "imaging_ci", "uniform")\n'
        'should_simulate(str(p))\n'
    )
    tracked = ["dataset/overview/ccd.gif", "dataset/overview/what_is_cti.png"]

    code, captured = _run_check(tmp_path, monkeypatch, src, tracked, capsys)

    assert code == 0
    assert "FAIL" not in captured.out + captured.err


def test_path_holding_tracked_files_without_a_releasing_token_fails(
    tmp_path, monkeypatch, capsys
):
    """The originating bug's shape: the resolved path itself holds tracked files."""
    src = (
        '"""\n__Env__\n\nENV: real_plots\n"""\n'
        'from pathlib import Path\n'
        'p = Path("dataset", "overview")\n'
        'should_simulate(str(p))\n'
    )
    tracked = ["dataset/overview/ccd.gif"]

    code, captured = _run_check(tmp_path, monkeypatch, src, tracked, capsys)

    assert code == 1
    assert "FAIL" in captured.err
    assert "dataset/overview" in captured.err


def test_releasing_token_exempts_an_otherwise_failing_call_site(
    tmp_path, monkeypatch, capsys
):
    """Same script, plus `full_datasets` — the shape of the shipped fix."""
    src = (
        '"""\n__Env__\n\nENV: full_datasets real_plots\n"""\n'
        'from pathlib import Path\n'
        'p = Path("dataset", "overview")\n'
        'should_simulate(str(p))\n'
    )
    tracked = ["dataset/overview/ccd.gif"]

    code, captured = _run_check(tmp_path, monkeypatch, src, tracked, capsys)

    assert code == 0
    assert "FAIL" not in captured.out + captured.err


def test_unresolvable_call_site_is_reported_and_skipped(
    tmp_path, monkeypatch, capsys
):
    """Under-reporting is acceptable; a SILENT partial sweep is not."""
    src = (
        'from pathlib import Path\n'
        'p = Path("dataset", compute())\n'
        'should_simulate(str(p))\n'
    )
    tracked = ["dataset/overview/ccd.gif"]

    code, captured = _run_check(tmp_path, monkeypatch, src, tracked, capsys)

    assert code == 0
    assert "skipped" in captured.out
    assert "script.py:3" in captured.out
