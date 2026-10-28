import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "autohands"))

import build_util


def make_notebook(path, cells):
    notebook = {
        "cells": cells,
        "metadata": {},
        "nbformat": 4,
        "nbformat_minor": 4,
    }
    path.write_text(json.dumps(notebook))
    return path


def markdown_cell(text):
    return {"cell_type": "markdown", "metadata": {}, "source": [text]}


def code_cell(text):
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [text],
    }


def test_injects_after_leading_markdown(tmp_path):
    nb_path = make_notebook(
        tmp_path / "example.ipynb",
        [markdown_cell("Title\n====="), code_cell("import autolens as al")],
    )

    assert build_util.inject_colab_setup(nb_path, "autolens") is True

    cells = json.loads(nb_path.read_text())["cells"]
    assert len(cells) == 4
    assert cells[0]["source"] == ["Title\n====="]
    assert cells[1]["cell_type"] == "markdown"
    assert "Google Colab Setup" in "".join(cells[1]["source"])
    assert cells[2]["cell_type"] == "code"
    assert '_setup_colab.setup("autolens")' in "".join(cells[2]["source"])
    assert cells[3]["source"] == ["import autolens as al"]


def test_injects_at_top_when_no_leading_markdown(tmp_path):
    nb_path = make_notebook(
        tmp_path / "example.ipynb", [code_cell("import autofit as af")]
    )

    assert build_util.inject_colab_setup(nb_path, "autofit") is True

    cells = json.loads(nb_path.read_text())["cells"]
    assert cells[0]["cell_type"] == "markdown"
    assert '_setup_colab.setup("autofit")' in "".join(cells[1]["source"])


def test_expands_notebook_with_hand_written_setup(tmp_path):
    original = [
        markdown_cell("Title"),
        code_cell("from autolens import setup_colab\nsetup_colab.for_autolens()"),
    ]
    nb_path = make_notebook(tmp_path / "start_here.ipynb", original)

    assert build_util.inject_colab_setup(nb_path, "autolens") is True
    cells = json.loads(nb_path.read_text())["cells"]
    assert '"pip", "install", "autonerves", "--no-deps"' in "".join(cells[2]["source"])
    assert "setup_colab.for_autolens()" in "".join(cells[2]["source"])
    assert cells[2]["metadata"]["cellView"] == "form"
    assert "locally or in HTML" in "".join(cells[1]["source"])


@pytest.mark.parametrize(
    "cells",
    [
        [],
        [markdown_cell("Scientific Workflow\nFollow the guide to continue.")],
        [markdown_cell("Scientific Workflow"), code_cell(" \n\t")],
    ],
    ids=["empty", "prose-only", "blank-code"],
)
def test_skips_notebooks_without_nonempty_code(tmp_path, cells):
    nb_path = make_notebook(tmp_path / "tutorial.ipynb", cells)
    original = nb_path.read_bytes()

    assert build_util.inject_colab_setup(nb_path, "howtofit") is False
    assert nb_path.read_bytes() == original


def test_injects_when_nonempty_code_follows_blank_code(tmp_path):
    nb_path = make_notebook(
        tmp_path / "tutorial.ipynb",
        [markdown_cell("Title"), code_cell("\n"), code_cell("print('ready')")],
    )

    assert build_util.inject_colab_setup(nb_path, "howtofit") is True
    cells = json.loads(nb_path.read_text())["cells"]
    assert '_setup_colab.setup("howtofit")' in "".join(cells[2]["source"])
    assert cells[-1]["source"] == ["print('ready')"]


def test_idempotent(tmp_path):
    nb_path = make_notebook(
        tmp_path / "example.ipynb", [markdown_cell("Title"), code_cell("x = 1")]
    )

    assert build_util.inject_colab_setup(nb_path, "howtolens") is True
    once = nb_path.read_text()
    assert build_util.inject_colab_setup(nb_path, "howtolens") is False
    assert nb_path.read_text() == once


def test_all_projects_accepted(tmp_path):
    expected_projects = {
        "autofit": "autofit",
        "autogalaxy": "autogalaxy",
        "autolens": "autolens",
        "howtofit": "autofit",
        "howtogalaxy": "autogalaxy",
        "howtolens": "autolens",
    }

    assert build_util.COLAB_PROJECTS == expected_projects

    for project, package in sorted(expected_projects.items()):
        nb_path = make_notebook(tmp_path / f"{project}.ipynb", [code_cell("x = 1")])
        assert build_util.inject_colab_setup(nb_path, project) is True
        cells = json.loads(nb_path.read_text())["cells"]
        source = "".join(cells[1]["source"])

        assert f"from {package} import setup_colab as _setup_colab" in source
        assert 'pip", "install", "autonerves", "--no-deps"' in source
        assert 'import_module("autonerves.setup_colab")' in source
        assert "from autonerves import setup_colab" not in source
        assert f'_setup_colab.setup("{project}")' in source


def test_unknown_project_raises(tmp_path):
    nb_path = make_notebook(tmp_path / "example.ipynb", [code_cell("x = 1")])
    with pytest.raises(ValueError, match="unknown project 'euclid'"):
        build_util.inject_colab_setup(nb_path, "euclid")


@pytest.mark.parametrize("heading", ["## Science", "__science__", "Science\n======="])
def test_keeps_following_markdown_sections(tmp_path, heading):
    following = heading + "\n\nKeep this scientific explanation.\n"
    path = make_notebook(
        tmp_path / "start_here.ipynb",
        [
            markdown_cell(
                "Title\n\n__Google Colab Setup__\n\nOld setup.\n\n" + following
            ),
            code_cell("from autolens import setup_colab\nsetup_colab.for_autolens()"),
        ],
    )
    build_util.inject_colab_setup(path, "autolens")
    text = "".join(json.loads(path.read_text())["cells"][0]["source"])
    assert following in text
    assert "Old setup." not in text


def test_output_is_valid_notebook_json(tmp_path):
    nb_path = make_notebook(
        tmp_path / "example.ipynb", [markdown_cell("Title"), code_cell("x = 1")]
    )
    build_util.inject_colab_setup(nb_path, "autogalaxy")

    notebook = json.loads(nb_path.read_text())
    assert notebook["nbformat"] == 4
    for cell in notebook["cells"]:
        assert isinstance(cell["source"], list)
        assert all(isinstance(line, str) for line in cell["source"])
    code = notebook["cells"][2]
    assert code["outputs"] == []
    assert code["execution_count"] is None


@pytest.mark.parametrize("project", build_util.COLAB_PROJECTS)
def test_intro_and_advanced_copy(tmp_path, project):
    intro = (
        tmp_path / build_util._COLAB_INTRO_NOTEBOOKS[project].split("/blob/main/")[1]
    )
    intro.parent.mkdir(parents=True, exist_ok=True)
    make_notebook(intro, [code_cell("x = 1")])
    build_util.inject_colab_setup(intro, project)
    cells = json.loads(intro.read_text())["cells"]
    assert "locally or in HTML" in "".join(cells[0]["source"])
    assert cells[1]["metadata"]["jupyter"]["source_hidden"] is True
    advanced = make_notebook(tmp_path / "advanced.ipynb", [code_cell("x = 1")])
    build_util.inject_colab_setup(advanced, project)
    text = "".join(json.loads(advanced.read_text())["cells"][0]["source"])
    assert "as in [the introductory notebook]" in text
    assert "locally" not in text


@pytest.mark.parametrize("legacy", [True, False])
def test_existing_options_preserved_and_science_visible(tmp_path, legacy):
    if legacy:
        source = build_util.COLAB_SETUP_CODE.format(
            project="autolens", package="autolens"
        )
        source = source.replace(
            'setup("autolens")', 'setup("autolens", raise_error_if_not_gpu=False)'
        )
    else:
        source = "from autolens import setup_colab\nsetup_colab.for_autolens(raise_error_if_not_gpu=False)"
    source += "\nresult = 42\nprint(result)\n"
    path = make_notebook(
        tmp_path / "start_here.ipynb",
        [
            markdown_cell(
                "Title\n\n__Google Colab Setup__\n\nOld lengthy explanation."
            ),
            code_cell(source),
        ],
    )
    assert build_util.inject_colab_setup(path, "autolens")
    cells = json.loads(path.read_text())["cells"]
    assert "Title" in "".join(cells[0]["source"])
    assert "Old lengthy" not in "".join(cells[0]["source"])
    assert "raise_error_if_not_gpu=False" in "".join(cells[1]["source"])
    assert "result = 42" not in "".join(cells[1]["source"])
    assert "result = 42" in "".join(cells[2]["source"])
    assert "cellView" not in cells[2]["metadata"]
    once = path.read_bytes()
    assert not build_util.inject_colab_setup(path, "autolens")
    assert path.read_bytes() == once


@pytest.mark.parametrize(
    "source",
    [
        "custom_setup_colab()\nscience()",
        "from autolens import setup_colab; setup_colab.for_autolens(); science()",
    ],
)
def test_unknown_custom_setup_is_not_hidden_or_rewritten(tmp_path, source):
    path = make_notebook(tmp_path / "custom.ipynb", [code_cell(source)])
    original = path.read_bytes()
    assert not build_util.inject_colab_setup(path, "autolens")
    assert path.read_bytes() == original


@pytest.mark.parametrize("colab", [True, False])
@pytest.mark.parametrize("gpu_required", [True, False])
def test_bootstrap_runs_before_library_import_and_preserves_options(
    tmp_path, monkeypatch, colab, gpu_required
):
    import builtins
    import importlib
    import subprocess
    from types import SimpleNamespace

    events = []
    setup = SimpleNamespace(
        for_autolens=lambda **kwargs: events.append(("setup", kwargs))
    )
    original_import = builtins.__import__

    def guarded_import(name, *args, **kwargs):
        if name == "google.colab":
            if not colab:
                raise ImportError("not Colab")
            return SimpleNamespace()
        if name == "autolens":
            if colab:
                pytest.fail("Fresh Colab must bootstrap before importing autolens")
            return SimpleNamespace(setup_colab=setup)
        return original_import(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", guarded_import)
    monkeypatch.setattr(
        subprocess, "check_call", lambda command: events.append(("install", command))
    )
    original_import_module = importlib.import_module

    def import_module(name, *args):
        if name == "autonerves.setup_colab":
            assert events[0][0] == "install"
            return setup
        return original_import_module(name, *args)

    monkeypatch.setattr(importlib, "import_module", import_module)
    path = make_notebook(
        tmp_path / "start_here.ipynb",
        [
            code_cell(
                "from autolens import setup_colab\n"
                f"setup_colab.for_autolens(raise_error_if_not_gpu={gpu_required})"
            )
        ],
    )
    build_util.inject_colab_setup(path, "autolens")
    cells = json.loads(path.read_text())["cells"]
    exec("".join(cells[1]["source"]), {})
    assert events[-1] == ("setup", {"raise_error_if_not_gpu": gpu_required})
    assert len(events) == (2 if colab else 1)
