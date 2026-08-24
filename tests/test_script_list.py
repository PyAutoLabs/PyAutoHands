"""
Cover the opt-in allowlist mode of the shared script runner.

`--list` exists so an opt-in workspace (one with a hand-maintained
`smoke_tests.txt`) can use the same runner as the opt-out HowTo repos, instead
of vendoring its own copy of the loop. These tests pin the four behaviours the
vendored copies relied on, so a collapsed workspace runner cannot lose them.
"""

import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).parent.parent
AUTOHANDS_DIR = PROJECT_ROOT / "autohands"
sys.path.insert(0, str(AUTOHANDS_DIR))

from build_util import execute_scripts_in_folder, files_from_list  # noqa: E402
from result_collector import RunReport, Status  # noqa: E402


@pytest.fixture
def workspace(tmp_path, monkeypatch):
    """A minimal workspace: scripts/ plus a place to write a script list."""
    scripts = tmp_path / "scripts"
    (scripts / "sub_directory").mkdir(parents=True)
    for rel in ("top_level.py", "a.py", "sub_directory/sub.py"):
        (scripts / rel).write_text("")
    (scripts / "simulators").mkdir()
    (scripts / "simulators" / "simulator_script.py").write_text("")
    monkeypatch.chdir(tmp_path)
    return tmp_path


def _rel(paths, root):
    return [str(Path(p).relative_to(root / "scripts")) for p in paths]


def test_allowlist_is_honoured(workspace):
    """Only listed scripts come back — the three unlisted ones do not."""
    listing = workspace / "smoke_tests.txt"
    listing.write_text("top_level.py\nsub_directory/sub.py\n")

    files = files_from_list("scripts", listing)

    assert _rel(files, workspace) == ["top_level.py", "sub_directory/sub.py"]


def test_allowlist_order_is_the_files_order(workspace):
    """
    The list's sequence survives, rather than being re-sorted.

    `find_scripts_in_folder` deliberately sorts simulators first; an allowlist
    must NOT, because a hand-maintained suite may depend on an earlier entry's
    output. Listing a simulator last therefore keeps it last.
    """
    listing = workspace / "smoke_tests.txt"
    listing.write_text("top_level.py\na.py\nsimulators/simulator_script.py\n")

    files = files_from_list("scripts", listing)

    assert _rel(files, workspace) == [
        "top_level.py",
        "a.py",
        "simulators/simulator_script.py",
    ]


def test_blank_lines_comments_and_duplicates_are_dropped(workspace):
    listing = workspace / "smoke_tests.txt"
    listing.write_text(
        "# a comment\n"
        "\n"
        "top_level.py\n"
        "   \n"
        "  a.py  \n"
        "# another comment\n"
        "top_level.py\n"  # duplicate: must not run twice
    )

    files = files_from_list("scripts", listing)

    assert _rel(files, workspace) == ["top_level.py", "a.py"]


def test_missing_list_file_is_an_error_not_an_empty_run(workspace):
    """
    A missing list must not resolve to "nothing to run".

    Returning an empty list would let the caller exit 0 having tested nothing —
    the vacuously-green-gate failure mode.
    """
    with pytest.raises(FileNotFoundError, match="no script list at"):
        files_from_list("scripts", workspace / "does_not_exist.txt")


def test_the_allowlist_wins_over_no_run(workspace):
    """
    An allowlisted script runs even when no_run.yaml also names it.

    The two files are policy for DIFFERENT runs: no_run.yaml governs the release
    mega-run and notebook generation, an allowlist governs the PR smoke gate. A
    script legitimately appears in both — excluded from the full build, required
    in smoke.

    This is measured, not theoretical. The vendored workspace runners read only
    smoke_tests.txt and never open no_run.yaml, and across the four repos that
    carry both files 13 allowlisted scripts are also no_run-listed. Filtering the
    list by no_run would silently delete every one of them from smoke coverage.
    """
    listing = workspace / "smoke_tests.txt"
    listing.write_text("top_level.py\na.py\n")
    report = RunReport(project="p", directory="scripts", run_type="script")

    execute_scripts_in_folder(
        directory="scripts",
        no_run_list=["a"],
        report=report,
        skip_reasons={"a": "excluded from the release build"},
        files=files_from_list("scripts", listing),
    )

    by_name = {Path(r.file).name: r for r in report.results}
    assert by_name["a.py"].status == Status.PASSED, (
        "an allowlisted script must run even when no_run.yaml names it"
    )
    assert by_name["top_level.py"].status == Status.PASSED


def test_no_run_still_filters_discovery(workspace):
    """The opt-out path is untouched: without a list, no_run.yaml still skips."""
    report = RunReport(project="p", directory="scripts", run_type="script")

    execute_scripts_in_folder(
        directory="scripts",
        no_run_list=["a"],
        report=report,
        skip_reasons={"a": "deliberately off"},
    )

    by_name = {Path(r.file).name: r for r in report.results}
    assert by_name["a.py"].status == Status.SKIPPED
    assert by_name["a.py"].skip_reason == "deliberately off"


def test_listed_but_missing_entry_fails_without_stopping_the_run(workspace):
    """
    A stale allowlist entry is one FAIL, not an abort.

    The runner's contract is to continue through failures; aborting would cost
    coverage of every entry after the stale one and print no summary.
    """
    listing = workspace / "smoke_tests.txt"
    listing.write_text("gone.py\ntop_level.py\n")
    report = RunReport(project="p", directory="scripts", run_type="script")

    execute_scripts_in_folder(
        directory="scripts",
        no_run_list=[],
        report=report,
        files=files_from_list("scripts", listing),
    )

    by_name = {Path(r.file).name: r for r in report.results}
    assert by_name["gone.py"].status == Status.FAILED
    assert "not found" in by_name["gone.py"].error_message
    # The entry AFTER the stale one still ran.
    assert "top_level.py" in by_name


def test_absent_flag_leaves_discovery_untouched(workspace):
    """The opt-out path is unchanged when no list is passed."""
    report = RunReport(project="p", directory="scripts", run_type="script")
    execute_scripts_in_folder(directory="scripts", no_run_list=[], report=report)

    assert len(report.results) == 4
    # Discovery's simulator-first ordering still applies here.
    assert Path(report.results[0].file).name == "simulator_script.py"


def test_a_listed_missing_file_fails_even_if_no_run_names_it(workspace):
    """
    With the list authoritative, a stale entry is a FAIL whatever no_run says.

    no_run.yaml cannot rescue it: the list is the smoke policy, so an entry
    naming a file that does not exist is a broken allowlist and must be visible.
    """
    listing = workspace / "smoke_tests.txt"
    listing.write_text("gone_and_excluded.py\ntop_level.py\n")
    report = RunReport(project="p", directory="scripts", run_type="script")

    execute_scripts_in_folder(
        directory="scripts",
        no_run_list=["gone_and_excluded"],
        report=report,
        skip_reasons={"gone_and_excluded": "retired"},
        files=files_from_list("scripts", listing),
    )

    by_name = {Path(r.file).name: r for r in report.results}
    assert by_name["gone_and_excluded.py"].status == Status.FAILED
    assert "top_level.py" in by_name
