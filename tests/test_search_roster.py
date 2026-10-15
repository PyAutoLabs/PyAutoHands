"""Tests for autohands/search_roster.py and its two CLI entrypoints.

Hermetic: a small fabricated ``search-manifest@1`` document stands in for
``python -m autofit search-manifest --json``, so nothing here imports the
science stack. Repo names in anchors are fake on purpose.
"""

import json
import sys
from pathlib import Path

import pytest

AUTOHANDS_DIR = Path(__file__).parent.parent / "autohands"
sys.path.insert(0, str(AUTOHANDS_DIR))

import check_search_roster  # noqa: E402
import regenerate_search_roster  # noqa: E402
import search_roster  # noqa: E402


def _search(name, family, status="stable", example=None, jax="none", evidence=False):
    return {
        "name": name,
        "class_path": f"pkg.{name}",
        "family": family,
        "lazy": False,
        "requires": [],
        "example": example,
        "integration_test": f"ws_test:scripts/searches/{name}.py",
        "capabilities": {
            "jax_use": jax,
            "gradient": "none",
            "produces_evidence": evidence,
            "posterior_kind": "weighted" if evidence else "point",
            "status": status,
        },
    }


def _manifest(version="1.0.0", extra=()):
    return {
        "schema": "search-manifest@1",
        "autofit_version": version,
        "families": {"nest": "Nested sampling", "mle": "Maximum likelihood"},
        "capability_attributes": [],
        "searches": [
            _search("Nautilus", "nest", example="ws:scripts/searches/nest.py#Search: Nautilus",
                    evidence=True),
            _search("NSS", "nest", status="experimental", jax="required", evidence=True),
            _search("LBFGS", "mle", example="ws:scripts/searches/mle.py#Search: LBFGS"),
            *extra,
        ],
    }


BLOCK = "intro\n<!-- search-roster:begin style=list -->\n<!-- search-roster:end -->\noutro\n"


def test_list_block_renders_families_in_manifest_order():
    text, n = search_roster.regenerate_text(BLOCK, _manifest())
    assert n == 1
    lines = text.split("\n")
    assert lines[0] == "intro" and lines[-2] == "outro"
    assert lines[2] == "<!-- search-manifest@1 autofit 1.0.0 -->"
    assert lines[3] == (
        "- **Nested sampling** (`nest`): `af.Nautilus`, `af.NSS` (experimental)"
        " — example: `ws:scripts/searches/nest.py`"
    )
    assert lines[4].startswith("- **Maximum likelihood** (`mle`): `af.LBFGS`")


def test_link_option_makes_own_repo_examples_relative_links():
    block = BLOCK.replace("style=list", "style=list link=ws indent=2")
    text, _ = search_roster.regenerate_text(block, _manifest())
    assert "  - **Nested sampling** (`nest`)" in text
    assert "[scripts/searches/nest.py](scripts/searches/nest.py)" in text


def test_table_block_has_one_row_per_search():
    block = BLOCK.replace("style=list", "style=table")
    text, _ = search_roster.regenerate_text(block, _manifest())
    rows = [l for l in text.split("\n") if l.startswith("| `af.")]
    assert [r.split("|")[1].strip() for r in rows] == ["`af.Nautilus`", "`af.NSS`", "`af.LBFGS`"]
    assert "| `af.NSS` | nest | experimental | required | none | yes | weighted | — |" in rows


def test_regeneration_is_idempotent_and_leaves_prose_alone():
    once, _ = search_roster.regenerate_text(BLOCK, _manifest())
    twice, _ = search_roster.regenerate_text(once, _manifest())
    assert once == twice
    assert once.startswith("intro\n") and once.endswith("outro\n")


def test_check_is_clean_after_regeneration():
    text, _ = search_roster.regenerate_text(BLOCK, _manifest())
    assert search_roster.check_text(text, _manifest()) == []


def test_check_flags_a_changed_roster_as_body_drift():
    text, _ = search_roster.regenerate_text(BLOCK, _manifest())
    grown = _manifest(extra=[_search("Drawer", "mle")])
    drift = search_roster.check_text(text, grown)
    assert [d.kind for d in drift] == ["body"]


def test_check_only_notes_a_new_version_with_the_same_roster():
    text, _ = search_roster.regenerate_text(BLOCK, _manifest("1.0.0"))
    drift = search_roster.check_text(text, _manifest("1.1.0"))
    assert [d.kind for d in drift] == ["stamp"]


def test_unstamped_block_is_reported():
    text, _ = search_roster.regenerate_text(BLOCK, _manifest())
    lines = [l for l in text.split("\n") if "search-manifest@1" not in l]
    drift = search_roster.check_text("\n".join(lines), _manifest())
    assert [d.kind for d in drift] == ["unstamped"]


@pytest.mark.parametrize(
    "text",
    [
        "<!-- search-roster:begin -->\nno end\n",
        "<!-- search-roster:end -->\n",
        "<!-- search-roster:begin style=bogus -->\n<!-- search-roster:end -->\n",
        "<!-- search-roster:begin -->\n<!-- search-roster:begin -->\n<!-- search-roster:end -->\n",
    ],
)
def test_malformed_blocks_raise(text):
    with pytest.raises(search_roster.RosterError):
        search_roster.regenerate_text(text, _manifest())


def test_load_manifest_rejects_another_schema(tmp_path):
    f = tmp_path / "m.json"
    f.write_text(json.dumps(dict(_manifest(), schema="search-manifest@9")))
    with pytest.raises(search_roster.RosterError):
        search_roster.load_manifest(str(f))


def test_anchors_resolve_skip_and_fail(tmp_path):
    ws = tmp_path / "ws" / "scripts" / "searches"
    ws.mkdir(parents=True)
    (ws / "nest.py").write_text('"""\n__Search: Nautilus__\n"""\n')
    (ws / "mle.py").write_text('"""\n__Search: Something Else__\n"""\n')
    results = search_roster.resolve_anchors(_manifest(), tmp_path)
    by = {(r.search, r.field): r.status for r in results}
    assert by[("Nautilus", "example")] == "ok"
    assert by[("LBFGS", "example")] == "missing"  # section absent
    assert by[("Nautilus", "integration_test")] == "skipped"  # ws_test not checked out


def test_named_searches_only_reads_search_assignments():
    source = (
        "search = af.Nautilus(n_live=100)\n"
        "search_mle = af.Gone()\n"
        "model = af.Model(Thing)\n"
        '"""prose naming af.UltraNest"""\n'
    )
    assert search_roster.named_searches(source) == [(1, "Nautilus"), (2, "Gone")]


def test_manifest_difference_reports_added_and_changed():
    source = _manifest("2.0.0", extra=[_search("Drawer", "mle")])
    source["searches"][1]["capabilities"]["status"] = "stable"
    diff = search_roster.manifest_difference(_manifest(), source)
    assert any(l.startswith("+ Drawer") for l in diff)
    assert any(l.startswith("~ NSS") for l in diff)


# --- the CLIs ----------------------------------------------------------------


def _tree(tmp_path):
    root = tmp_path / "ws"
    (root / "scripts" / "searches").mkdir(parents=True)
    (root / "llms.txt").write_text(BLOCK)
    (root / "notes.md").write_text("no block here\n")
    (root / "scripts" / "searches" / "nest.py").write_text(
        '"""\n__Search: Nautilus__\n"""\nsearch = af.Nautilus()\n'
    )
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps(_manifest()))
    return root, manifest


def test_cli_regenerate_then_check(tmp_path, capsys):
    root, manifest = _tree(tmp_path)
    args = ["--root", str(root), "--manifest", str(manifest)]
    assert check_search_roster.main(args) == 1  # unrendered block = body drift
    assert regenerate_search_roster.main(args) == 0
    assert check_search_roster.main(args + ["--names-in", "scripts/**/*.py"]) == 0
    out = capsys.readouterr().out
    assert "regenerate byte-identically" in out


def test_cli_stamp_is_a_note_unless_strict(tmp_path):
    root, manifest = _tree(tmp_path)
    regenerate_search_roster.main(["--root", str(root), "--manifest", str(manifest)])
    newer = tmp_path / "newer.json"
    newer.write_text(json.dumps(_manifest("9.9.9")))
    args = ["--root", str(root), "--manifest", str(newer)]
    assert check_search_roster.main(args) == 0
    assert check_search_roster.main(args + ["--strict-version"]) == 1


def test_cli_unknown_named_search_fails(tmp_path, capsys):
    root, manifest = _tree(tmp_path)
    regenerate_search_roster.main(["--root", str(root), "--manifest", str(manifest)])
    (root / "scripts" / "searches" / "old.py").write_text("search = af.UltraNest()\n")
    args = ["--root", str(root), "--manifest", str(manifest), "--names-in", "scripts/**/*.py"]
    assert check_search_roster.main(args) == 1
    assert "af.UltraNest is not in the search manifest" in capsys.readouterr().out


def test_cli_missing_anchor_fails(tmp_path):
    root, manifest = _tree(tmp_path)
    regenerate_search_roster.main(["--root", str(root), "--manifest", str(manifest)])
    args = ["--root", str(root), "--manifest", str(manifest), "--workspace-root", str(tmp_path)]
    assert check_search_roster.main(args) == 1  # LBFGS example file absent


def test_cli_usage_errors(tmp_path):
    assert check_search_roster.main(["--root", str(tmp_path / "absent")]) == 2
    root, _ = _tree(tmp_path)
    bad = tmp_path / "bad.json"
    bad.write_text("not json")
    assert check_search_roster.main(["--root", str(root), "--manifest", str(bad)]) == 2


def test_navigator_roster_mode_rewrites_only_the_block(tmp_path):
    root, manifest = _tree(tmp_path)
    sys.argv = ["generate.py", "autofit"]
    import navigator

    changed = navigator.write_roster(root, str(manifest))
    assert changed == [root / "llms.txt"]
    text = (root / "llms.txt").read_text()
    assert text.startswith("intro\n") and text.endswith("outro\n")
    assert "<!-- search-manifest@1 autofit 1.0.0 -->" in text
    assert navigator.write_roster(root, str(manifest)) == []  # idempotent
