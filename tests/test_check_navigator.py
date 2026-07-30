"""Tests for the navigator path check's relative-reference rule.

Workspace READMEs name packages relative to their own location ("The
``imaging/data_preparation`` package ..."), so those references never start at
``scripts/`` and were invisible to the original token regex. This is what let a
restructure rewrite a folder list while the gate stayed green.

The rule is deliberately narrow — it is a hard CI gate, so a false positive
turns a PR red over prose. These tests pin both directions: real drift is
caught, and the known-benign shapes are not.
"""

from pathlib import Path

from autohands.check_navigator import check_paths


def _workspace(tmp_path, readme_body, readme_at="scripts/imaging/data_preparation"):
    """A minimal workspace whose real tree is imaging/data_preparation/."""
    root = tmp_path / "demo_workspace"
    for folder in (
        "scripts/imaging/data_preparation/examples",
        "scripts/imaging/features",
        "scripts/guides/results/aggregator",
        "scripts/guides/advanced",
        "config/priors",
        "dataset/imaging",
    ):
        (root / folder).mkdir(parents=True)
    (root / "scripts/imaging/modeling.py").write_text("x = 1\n")
    (root / readme_at).mkdir(parents=True, exist_ok=True)
    (root / readme_at / "README.md").write_text(readme_body)
    return root


def _misses(root):
    return {token for _, _, token in check_paths(root, [])}


def test_reversed_relative_path_is_caught(tmp_path):
    # The real package is imaging/data_preparation; the README has it backwards.
    root = _workspace(tmp_path, "The `data_preparation/imaging` package prepares data.\n")

    assert "data_preparation/imaging" in _misses(root)


def test_typoed_leading_segment_is_caught(tmp_path):
    # `guides/advanced` exists; `guide/advanced` is the drift. The anchoring
    # guard must accept a real *tail* or this whole class is missed.
    root = _workspace(tmp_path, "The `guide/advanced` folder holds guides.\n")

    assert "guide/advanced" in _misses(root)


def test_tail_quoted_path_resolves(tmp_path):
    # Prose quotes the tail: `results/aggregator` for guides/results/aggregator.
    # Must resolve, or the gate contradicts documentation the hygiene audit
    # considers clean.
    root = _workspace(tmp_path, "See `results/aggregator` for the aggregator API.\n")

    assert _misses(root) == set()


def test_sibling_named_relative_to_the_readme_resolves(tmp_path):
    root = _workspace(tmp_path, "See `data_preparation/examples` for more.\n")

    assert _misses(root) == set()


def test_extensionless_file_reference_resolves(tmp_path):
    # Prose drops the .py: `imaging/modeling` is modeling.py.
    root = _workspace(tmp_path, "See `imaging/modeling` for the workflow.\n")

    assert _misses(root) == set()


def test_repo_name_prefix_is_stripped(tmp_path):
    root = _workspace(tmp_path, "See `demo_workspace/imaging/features` for features.\n")

    assert _misses(root) == set()


def test_prose_slash_is_not_a_reference(tmp_path):
    # "bulge/disk" is English, not a path. A hard gate must not fail on it.
    root = _workspace(tmp_path, "A `bulge/disk` decomposition is standard.\n")

    assert _misses(root) == set()


def test_runtime_directory_reference_is_ignored(tmp_path):
    # dataset/ is written by a simulator; absence proves nothing.
    root = _workspace(tmp_path, "The dataset is at `dataset/imaging/clumpy`.\n")

    assert _misses(root) == set()


def test_unbackticked_prose_is_not_scanned(tmp_path):
    root = _workspace(tmp_path, "Refer to data_preparation/imaging for details.\n")

    assert _misses(root) == set()


def test_bare_structure_list_names_are_out_of_scope(tmp_path):
    # Documented limitation: telling a folder list from a parameter glossary
    # needs the quorum heuristics that live in the hygiene audit, so a dead bare
    # name (the original `slam_pipeline` symptom) is NOT gated here.
    root = _workspace(tmp_path, "- `slam_pipeline`: the SLaM pipelines.\n")

    assert _misses(root) == set()
