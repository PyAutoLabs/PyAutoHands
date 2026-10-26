"""Tests for the Colab Gemini instructions stamped into generated notebooks (#324).

A small fixture assistant (colab/contexts.yaml + skills/) is built per test, so
these pin the assembly, matching and metadata rules without any real assistant.
"""

import json
import sys
import uuid
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "autohands"))

import build_util
import gemini_context

CONTEXTS_YAML = """\
name: Test assistant
preface: |
  PREFACE written for a coding agent.
rules: |
  You are helping with {notebook} in {repo}.
never_map: [maintainer_skill]
default:
  skills: [skill_default]
contexts:
  - match: autolens_workspace/notebooks/imaging/features/*
    skills: [skill_feature]
  - match: autolens_workspace/notebooks/imaging/*
    skills: [skill_imaging, skill_default]
  - match: autolens_workspace/notebooks/big/*
    skills: [skill_big]
  - match: autolens_workspace/notebooks/broken/*
    skills: [skill_missing]
"""


@pytest.fixture
def assistant(tmp_path):
    root = tmp_path / "test_assistant"
    (root / "colab").mkdir(parents=True)
    (root / "colab" / "contexts.yaml").write_text(CONTEXTS_YAML)
    skills = root / "skills"
    skills.mkdir()
    for name in ("skill_default", "skill_feature", "skill_imaging", "maintainer_skill"):
        (skills / f"{name}.md").write_text(f"# {name}\n\nBody of {name}.\n")
    (skills / "skill_big.md").write_text("x" * (build_util.GEMINI_CONTEXT_CAP + 1))
    return root


def make_notebook(path, cells, metadata=None):
    path.parent.mkdir(parents=True, exist_ok=True)
    notebook = {
        "cells": cells,
        "metadata": metadata if metadata is not None else {},
        "nbformat": 4,
        "nbformat_minor": 4,
    }
    path.write_text(json.dumps(notebook, indent=1))
    return path


def code_cell(text):
    return {"cell_type": "code", "execution_count": None, "metadata": {},
            "outputs": [], "source": [text]}


def markdown_cell(text):
    return {"cell_type": "markdown", "metadata": {}, "source": [text]}


def colab_metadata(path):
    return json.loads(Path(path).read_text())["metadata"]["colab"]


def test_writes_selected_context_with_fixed_uuid5(tmp_path, assistant):
    nb = make_notebook(tmp_path / "modeling.ipynb", [code_cell("import autolens as al")])

    label = build_util.inject_gemini_instructions(
        nb, "autolens", assistant, "notebooks/imaging/modeling.ipynb"
    )

    expected_id = str(uuid.uuid5(
        uuid.NAMESPACE_URL, "https://github.com/PyAutoLabs/colab-gemini/autolens"
    ))
    assert build_util.gemini_context_id("autolens") == expected_id
    colab = colab_metadata(nb)
    assert colab["selectedAiContext"] == expected_id
    entry = colab["aiContexts"][expected_id]
    assert entry["id"] == expected_id
    assert entry["name"] == "Test assistant"
    assert label == "autolens_workspace/notebooks/imaging/*"
    assert "Body of skill_imaging." in entry["context"]
    assert "Body of skill_default." in entry["context"]
    assert entry["context"].index("PREFACE") < entry["context"].index("skill_imaging")


def test_ids_differ_per_project():
    assert build_util.gemini_context_id("autolens") != build_util.gemini_context_id("howtolens")


def test_notebook_path_and_repo_appear_in_text(tmp_path, assistant):
    nb = make_notebook(tmp_path / "modeling.ipynb", [code_cell("x = 1")])
    build_util.inject_gemini_instructions(nb, "autolens", assistant, "notebooks/imaging/modeling.ipynb")
    (entry,) = colab_metadata(nb)["aiContexts"].values()
    assert "notebooks/imaging/modeling.ipynb in autolens_workspace" in entry["context"]


def test_idempotent(tmp_path, assistant):
    nb = make_notebook(tmp_path / "modeling.ipynb", [code_cell("x = 1")])
    build_util.inject_gemini_instructions(nb, "autolens", assistant, "notebooks/imaging/modeling.ipynb")
    first = nb.read_text()
    build_util.inject_gemini_instructions(nb, "autolens", assistant, "notebooks/imaging/modeling.ipynb")
    assert nb.read_text() == first
    assert len(colab_metadata(nb)["aiContexts"]) == 1


def test_prose_only_notebook_gets_instructions(tmp_path, assistant):
    nb = make_notebook(tmp_path / "readme.ipynb", [markdown_cell("Just prose.")])
    assert build_util.inject_colab_setup(nb, "autolens") is False
    build_util.inject_gemini_instructions(nb, "autolens", assistant, "notebooks/imaging/readme.ipynb")
    assert "selectedAiContext" in colab_metadata(nb)


def test_hand_written_setup_notebook_gets_instructions(tmp_path, assistant):
    nb = make_notebook(tmp_path / "setup.ipynb", [code_cell('setup_colab.setup("autolens")')])
    assert build_util.inject_colab_setup(nb, "autolens") is False
    build_util.inject_gemini_instructions(nb, "autolens", assistant, "notebooks/imaging/setup.ipynb")
    assert "selectedAiContext" in colab_metadata(nb)


def test_most_specific_entry_wins(assistant):
    contexts = build_util.load_gemini_contexts(assistant)
    label, skills = build_util.match_gemini_context(
        contexts, "autolens_workspace/notebooks/imaging/features/pixelization/fit.ipynb"
    )
    assert label == "autolens_workspace/notebooks/imaging/features/*"
    assert skills == ["skill_feature"]


def test_default_fallback(tmp_path, assistant):
    nb = make_notebook(tmp_path / "other.ipynb", [code_cell("x = 1")])
    label = build_util.inject_gemini_instructions(nb, "autolens", assistant, "notebooks/weak/other.ipynb")
    assert label == "default"
    (entry,) = colab_metadata(nb)["aiContexts"].values()
    assert "Body of skill_default." in entry["context"]


def test_over_cap_raises_naming_the_entry(tmp_path, assistant):
    nb = make_notebook(tmp_path / "huge.ipynb", [code_cell("x = 1")])
    before = nb.read_text()
    with pytest.raises(ValueError, match=r"autolens_workspace/notebooks/big/\*.*over the 20000 cap"):
        build_util.inject_gemini_instructions(nb, "autolens", assistant, "notebooks/big/huge.ipynb")
    assert nb.read_text() == before


def test_missing_skill_raises(tmp_path, assistant):
    nb = make_notebook(tmp_path / "x.ipynb", [code_cell("x = 1")])
    with pytest.raises(FileNotFoundError, match="skill_missing"):
        build_util.inject_gemini_instructions(nb, "autolens", assistant, "notebooks/broken/x.ipynb")


def test_missing_mapping_raises(tmp_path):
    nb = make_notebook(tmp_path / "x.ipynb", [code_cell("x = 1")])
    (tmp_path / "bare_assistant").mkdir()
    with pytest.raises(FileNotFoundError, match="colab/contexts.yaml"):
        build_util.inject_gemini_instructions(nb, "autolens", tmp_path / "bare_assistant", "x.ipynb")


def test_unknown_project_raises(tmp_path, assistant):
    nb = make_notebook(tmp_path / "x.ipynb", [code_cell("x = 1")])
    with pytest.raises(ValueError, match="COLAB_ASSISTANTS"):
        build_util.inject_gemini_instructions(nb, "nonsense", assistant, "x.ipynb")


def test_other_colab_metadata_preserved(tmp_path, assistant):
    nb = make_notebook(
        tmp_path / "x.ipynb",
        [code_cell("x = 1")],
        metadata={
            "kernelspec": {"name": "python3"},
            "colab": {"provenance": [{"file_id": "abc"}],
                      "aiContexts": {"user-own": {"id": "user-own", "name": "Mine", "context": "hi"}}},
        },
    )
    build_util.inject_gemini_instructions(nb, "autolens", assistant, "notebooks/imaging/x.ipynb")
    metadata = json.loads(nb.read_text())["metadata"]
    assert metadata["kernelspec"] == {"name": "python3"}
    assert metadata["colab"]["provenance"] == [{"file_id": "abc"}]
    assert "user-own" in metadata["colab"]["aiContexts"]
    assert metadata["colab"]["selectedAiContext"] == build_util.gemini_context_id("autolens")


def test_layout_preserved_so_cells_are_untouched(tmp_path, assistant):
    """A sorted-key, trailing-newline notebook (nbformat's layout) keeps its layout."""
    notebook = {"cells": [code_cell("x = 'é'")], "metadata": {"kernelspec": {}},
                "nbformat": 4, "nbformat_minor": 5}
    nb = tmp_path / "x.ipynb"
    nb.write_text(json.dumps(notebook, indent=1, sort_keys=True, ensure_ascii=False) + "\n")
    build_util.inject_gemini_instructions(nb, "autolens", assistant, "notebooks/imaging/x.ipynb")
    text = nb.read_text()
    assert text.endswith("}\n")
    assert "x = 'é'" in text
    rewritten = json.loads(text)
    assert rewritten["cells"] == notebook["cells"]


def test_resolve_assistant_root_explicit_and_env(tmp_path, monkeypatch):
    monkeypatch.delenv("PYAUTO_ASSISTANT_ROOT", raising=False)
    assert build_util.resolve_assistant_root("autolens", str(tmp_path)) == tmp_path.resolve()
    monkeypatch.setenv("PYAUTO_ASSISTANT_ROOT", str(tmp_path))
    assert build_util.resolve_assistant_root("autolens") == tmp_path.resolve()
    assert build_util.resolve_assistant_root("not_a_project") is None


def test_resolve_assistant_root_skips_workspace_checkout_without_mapping(tmp_path, monkeypatch, capsys):
    monkeypatch.delenv("PYAUTO_ASSISTANT_ROOT", raising=False)
    import _workspace

    monkeypatch.setattr(_workspace, "workspace_root", lambda: tmp_path)
    monkeypatch.setattr(_workspace, "repo_path", lambda root, name: Path(root) / name)
    (tmp_path / "autogalaxy_assistant").mkdir()
    assert build_util.resolve_assistant_root("autogalaxy") is None
    assert "skipped" in capsys.readouterr().err


def test_cli_apply_and_report(tmp_path, assistant, capsys):
    workspace = tmp_path / "autolens_workspace"
    make_notebook(workspace / "notebooks" / "imaging" / "modeling.ipynb", [code_cell("x = 1")])
    make_notebook(workspace / "notebooks" / "imaging" / "features" / "a.ipynb", [code_cell("x = 1")])
    make_notebook(workspace / "notebooks" / "weak" / "w.ipynb", [markdown_cell("prose")])
    make_notebook(workspace / "notebooks" / "imaging" / ".ipynb_checkpoints" / "c.ipynb", [])

    applied = gemini_context.apply(workspace / "notebooks", "autolens", assistant)
    assert applied == {
        "notebooks/imaging/features/a.ipynb": "autolens_workspace/notebooks/imaging/features/*",
        "notebooks/imaging/modeling.ipynb": "autolens_workspace/notebooks/imaging/*",
        "notebooks/weak/w.ipynb": "default",
    }

    report_path = tmp_path / "report.json"
    rc = gemini_context.main([
        "report", "--workspace", str(workspace), "--project", "autolens",
        "--assistant-root", str(assistant), "--json", str(report_path),
    ])
    result = json.loads(report_path.read_text())
    assert result["notebooks"] == 3
    assert result["default_notebooks"] == ["notebooks/weak/w.ipynb"]
    assert result["default_only_folders"] == ["notebooks/weak"]
    assert result["unused_entries"] == [
        "autolens_workspace/notebooks/big/*", "autolens_workspace/notebooks/broken/*",
    ]
    assert result["missing_skills"] == {"autolens_workspace/notebooks/broken/*": ["skill_missing"]}
    assert result["sizes"]["over_cap"] == []
    assert 0 < result["sizes"]["median"] <= result["sizes"]["max"] < build_util.GEMINI_CONTEXT_CAP
    # The fixture maps a missing skill, so the report fails.
    assert result["ok"] is False and rc == 1
    assert "MISSING skills" in capsys.readouterr().out


def test_report_flags_never_map(tmp_path, assistant):
    yaml_path = assistant / "colab" / "contexts.yaml"
    yaml_path.write_text(
        yaml_path.read_text().replace("skills: [skill_feature]", "skills: [maintainer_skill]")
    )
    workspace = tmp_path / "autolens_workspace"
    make_notebook(workspace / "notebooks" / "imaging" / "m.ipynb", [code_cell("x = 1")])
    result = gemini_context.report(workspace, "autolens", assistant)
    assert result["never_map_violations"] == {
        "autolens_workspace/notebooks/imaging/features/*": ["maintainer_skill"]
    }


def test_never_map_enforced_at_load(assistant):
    yaml_path = assistant / "colab" / "contexts.yaml"
    yaml_path.write_text(
        yaml_path.read_text().replace("skills: [skill_feature]", "skills: [maintainer_skill]")
    )
    with pytest.raises(ValueError, match=r"imaging/features/\*.*never_map.*maintainer_skill"):
        build_util.load_gemini_contexts(assistant)
    # The coverage report still loads it, to list every violation.
    assert build_util.load_gemini_contexts(assistant, enforce_never_map=False)


def test_validate_lists_every_failing_notebook(assistant):
    with pytest.raises(ValueError) as info:
        build_util.validate_gemini_contexts(assistant, [
            "autolens_workspace/notebooks/imaging/ok.ipynb",
            "autolens_workspace/notebooks/big/a.ipynb",
            "autolens_workspace/notebooks/broken/b.ipynb",
        ])
    message = str(info.value)
    assert "2 notebook(s) would fail" in message
    assert "over the 20000 cap" in message and "skill_missing" in message


@pytest.mark.parametrize("folder", ["big", "broken"])
def test_generate_fails_before_touching_notebooks(tmp_path, assistant, folder):
    """An over-cap or missing-skill mapping stops generate.py before its rmtree."""
    import os
    import subprocess

    workspace = tmp_path / "ws"
    (workspace / "scripts" / folder).mkdir(parents=True)
    (workspace / "scripts" / folder / "modeling.py").write_text('"""\nT\n=\n"""\n\nvalue = 1\n')
    (workspace / "notebooks" / folder).mkdir(parents=True)
    (workspace / "notebooks" / folder / "modeling.ipynb").write_text('{"cells": [], "nbformat": 4}\n')
    subprocess.run(["git", "init", "-q"], cwd=workspace, check=True)
    subprocess.run(["git", "add", "-A"], cwd=workspace, check=True)
    subprocess.run(["git", "-c", "user.email=t@t", "-c", "user.name=t", "commit", "-qm", "seed"],
                   cwd=workspace, check=True)

    autohands = Path(__file__).resolve().parent.parent / "autohands"
    result = subprocess.run(
        [sys.executable, str(autohands / "generate.py"), "autolens", "--assistant-root", str(assistant)],
        cwd=workspace, capture_output=True, text=True,
        env=dict(os.environ, PYTHONPATH=str(autohands)),
    )

    assert result.returncode != 0
    assert "nothing was modified" in result.stderr
    status = subprocess.run(["git", "status", "--porcelain"], cwd=workspace,
                            capture_output=True, text=True, check=True)
    assert status.stdout == ""
    assert list(workspace.glob("scripts/**/*.ipynb")) == []
