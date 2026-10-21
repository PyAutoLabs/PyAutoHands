"""
Cover the two shapes of the workspace-validation script matrix.

Per-directory (the default): one entry per ``<project>/scripts/<subdir>/``.
Ordered (``--ordered PROJECT``): one entry carrying the project's
``smoke_tests.txt``, so an order-dependent suite (the Euclid pipeline, whose
``scripts/tools/diagnose_latent.py`` replays fits run earlier in the list) runs
in one job instead of a consumer shard without its producers (PyAutoHands#317).
"""

import json
import subprocess
import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).parent.parent
AUTOHANDS_DIR = PROJECT_ROOT / "autohands"
sys.path.insert(0, str(AUTOHANDS_DIR))

from script_matrix import (  # noqa: E402
    main,
    make_combined_script_matrix,
    make_script_matrix,
)


@pytest.fixture
def projects(tmp_path, monkeypatch):
    """A sharded workspace and an order-dependent pipeline, side by side."""
    for sub in ("imaging", "interferometer"):
        (tmp_path / "ws" / "scripts" / sub).mkdir(parents=True)
    (tmp_path / "ws" / "smoke_tests.txt").write_text("imaging/a.py\n")
    (tmp_path / "pipe" / "scripts" / "tools").mkdir(parents=True)
    (tmp_path / "pipe" / "scripts" / "full_model.py").write_text("")
    (tmp_path / "pipe" / "start_here.py").write_text("")
    (tmp_path / "pipe" / "smoke_tests.txt").write_text(
        "start_here.py\nscripts/full_model.py\nscripts/tools/diagnose_latent.py\n"
    )
    monkeypatch.chdir(tmp_path)
    return tmp_path


def _sorted(entries):
    return sorted(entries, key=lambda e: (e["name"], e["directory"]))


def test_default_shape_is_one_entry_per_scripts_subdir(projects):
    assert _sorted(make_script_matrix("ws")) == [
        {"name": "ws", "directory": "imaging"},
        {"name": "ws", "directory": "interferometer"},
    ]


def test_smoke_list_presence_alone_does_not_opt_in(projects):
    """Every workspace has a smoke_tests.txt; only --ordered changes the shape."""
    matrix = make_combined_script_matrix(["ws", "pipe"])
    assert all("script_list" not in e for e in matrix)
    assert {"name": "pipe", "directory": "tools"} in matrix


def test_ordered_project_is_one_entry_carrying_its_list(projects):
    matrix = make_combined_script_matrix(["ws", "pipe"], ordered=["pipe"])
    pipe = [e for e in matrix if e["name"] == "pipe"]
    assert pipe == [
        {"name": "pipe", "directory": ".", "script_list": "smoke_tests.txt"}
    ]


def test_ordering_one_project_leaves_the_others_byte_identical(projects):
    before = [e for e in make_combined_script_matrix(["ws", "pipe"]) if e["name"] == "ws"]
    after = [
        e
        for e in make_combined_script_matrix(["ws", "pipe"], ordered=["pipe"])
        if e["name"] == "ws"
    ]
    assert json.dumps(before) == json.dumps(after)


def test_ordered_name_outside_the_matrix_is_an_error(projects):
    """A typo in the opt-in must not silently fall back to per-dir shards."""
    with pytest.raises(ValueError, match="not in the matrix"):
        make_combined_script_matrix(["ws"], ordered=["pipe"])


def test_cli_without_flag_matches_the_historical_positional_call(projects):
    assert main(["ws", "pipe"]) == make_combined_script_matrix(["ws", "pipe"])


def test_cli_ordered_flag_after_positionals(projects):
    """The workflow appends the flag after the project list; both orders parse."""
    out = subprocess.run(
        [sys.executable, str(AUTOHANDS_DIR / "script_matrix.py"),
         "ws", "pipe", "--ordered", "pipe"],
        cwd=projects, capture_output=True, text=True, check=True,
    ).stdout
    matrix = json.loads(out)
    assert {"name": "pipe", "directory": ".", "script_list": "smoke_tests.txt"} in matrix
    assert sum(e["name"] == "pipe" for e in matrix) == 1
    assert sum(e["name"] == "ws" for e in matrix) == 2


def test_ordered_entry_feeds_the_list_runner_and_keeps_per_script_overrides(
    projects, monkeypatch
):
    """The entry's (directory, script_list) resolve every list line from the
    project root, in order, and a profile override keyed on a path pattern
    (euclid's diagnose_latent PYAUTO_OUTPUT_DIR) still matches the resolved path
    — the `.` directory must not leak into the path the pattern is tested on."""
    from build_util import files_from_list
    from env_config import apply_profile

    (entry,) = make_combined_script_matrix(["pipe"], ordered=["pipe"])
    root = projects / "pipe"
    monkeypatch.chdir(root)
    files = files_from_list(entry["directory"], entry["script_list"])
    assert [str(f.relative_to(root)) for f in files] == [
        "start_here.py",
        "scripts/full_model.py",
        "scripts/tools/diagnose_latent.py",
    ]
    profile = {
        "defaults": {"PYAUTO_TEST_MODE": "2"},
        "overrides": [
            {
                "pattern": "scripts/tools/diagnose_latent.py",
                "set": {"PYAUTO_OUTPUT_DIR": "output/test_mode"},
            }
        ],
    }
    assert apply_profile({}, files[-1], profile)["PYAUTO_OUTPUT_DIR"] == "output/test_mode"
    assert "PYAUTO_OUTPUT_DIR" not in apply_profile({}, files[0], profile)
