"""Tests for generate_markdown.py — config parsing, path mapping, output cleaning."""

import json
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

AUTOHANDS_DIR = Path(__file__).parent.parent / "autohands"
sys.path.insert(0, str(AUTOHANDS_DIR))

import generate_markdown  # noqa: E402


def _write_config(workspace: Path, entries) -> None:
    config_path = workspace / generate_markdown.CONFIG_RELATIVE_PATH
    config_path.parent.mkdir(parents=True, exist_ok=True)
    config_path.write_text(yaml.safe_dump(entries))


def _make_script(workspace: Path, rel: str, docstring: str = "Title\n=====") -> None:
    script = workspace / rel
    script.parent.mkdir(parents=True, exist_ok=True)
    script.write_text(f'"""\n{docstring}\n"""\nprint("hi")\n')


class TestLoadExamples:
    def test_dict_and_string_entries(self, tmp_path):
        _make_script(tmp_path, "scripts/imaging/modeling.py")
        _make_script(tmp_path, "start_here.py")
        _write_config(
            tmp_path,
            [
                {"script": "scripts/imaging/modeling.py", "max_minutes": 120},
                "start_here.py",
            ],
        )
        examples = generate_markdown.load_examples(tmp_path)
        assert examples[0]["script"] == Path("scripts/imaging/modeling.py")
        assert examples[0]["max_minutes"] == 120
        assert examples[1]["script"] == Path("start_here.py")
        assert examples[1]["max_minutes"] == generate_markdown.DEFAULT_MAX_MINUTES

    def test_features_folder_rejected(self, tmp_path):
        _make_script(tmp_path, "scripts/imaging/features/no_lens_light/modeling.py")
        _write_config(
            tmp_path, ["scripts/imaging/features/no_lens_light/modeling.py"]
        )
        with pytest.raises(ValueError, match="features/"):
            generate_markdown.load_examples(tmp_path)

    def test_missing_script_rejected(self, tmp_path):
        _write_config(tmp_path, ["scripts/imaging/nope.py"])
        with pytest.raises(FileNotFoundError):
            generate_markdown.load_examples(tmp_path)

    def test_non_py_rejected(self, tmp_path):
        _make_script(tmp_path, "scripts/imaging/modeling.py")
        (tmp_path / "scripts/imaging/modeling.ipynb").write_text("{}")
        _write_config(tmp_path, ["scripts/imaging/modeling.ipynb"])
        with pytest.raises(ValueError, match="not a .py"):
            generate_markdown.load_examples(tmp_path)

    def test_missing_config_reported(self, tmp_path):
        with pytest.raises(FileNotFoundError, match="markdown_examples.yaml"):
            generate_markdown.load_examples(tmp_path)


class TestMarkdownDestination:
    def test_scripts_prefix_stripped(self):
        assert generate_markdown.markdown_destination(
            Path("scripts/imaging/modeling.py")
        ) == Path("markdown/imaging")

    def test_root_script(self):
        assert generate_markdown.markdown_destination(
            Path("start_here.py")
        ) == Path("markdown")

    def test_nested_guides(self):
        assert generate_markdown.markdown_destination(
            Path("scripts/guides/tracer.py")
        ) == Path("markdown/guides")


class TestStreamCleaning:
    def test_ansi_stripped(self):
        assert generate_markdown._clean_stream_text("\x1b[1mBold\x1b[0m") == "Bold"

    def test_carriage_return_progress_resolved(self):
        assert (
            generate_markdown._clean_stream_text("it 1/100\rit 50/100\rit 100/100")
            == "it 100/100"
        )

    def test_long_output_truncated(self):
        text = "\n".join(f"line {i}" for i in range(200))
        cleaned = generate_markdown._clean_stream_text(text)
        lines = cleaned.split("\n")
        assert len(lines) == (
            generate_markdown.STREAM_HEAD_LINES
            + generate_markdown.STREAM_TAIL_LINES
            + 1
        )
        assert "truncated" in cleaned
        assert lines[0] == "line 0"
        assert lines[-1] == "line 199"

    def test_short_output_untouched(self):
        assert generate_markdown._clean_stream_text("a\nb") == "a\nb"

    def test_local_paths_redacted(self):
        redactions = generate_markdown._redactions_for(
            Path("/home/user/wt/autolens_workspace")
        )
        cleaned = generate_markdown._clean_stream_text(
            "Working Directory has been set to `/home/user/wt/autolens_workspace`\n"
            "/home/user/wt/PyAutoArray/autoarray/operators/convolver.py:1415: UserWarning",
            redactions=redactions,
        )
        assert "Working Directory has been set to `autolens_workspace`" in cleaned
        assert ".../PyAutoArray/autoarray/operators/convolver.py:1415" in cleaned
        assert "/home/user" not in cleaned

    def test_clean_notebook_outputs(self, tmp_path):
        notebook = {
            "cells": [
                {
                    "cell_type": "code",
                    "outputs": [
                        {"output_type": "stream", "text": ["a\r", "b\x1b[0m"]},
                        {"output_type": "display_data", "data": {}},
                    ],
                }
            ]
        }
        path = tmp_path / "nb.ipynb"
        path.write_text(json.dumps(notebook))
        generate_markdown.clean_notebook_outputs(path)
        cleaned = json.loads(path.read_text())
        assert cleaned["cells"][0]["outputs"][0]["text"] == "b"
        assert cleaned["cells"][0]["outputs"][1] == {
            "output_type": "display_data",
            "data": {},
        }

    def test_progress_runs_collapsed_to_final_state(self):
        text = "start\n" + "\n".join(
            f"{i}it [00:{i:02d}, bound: 3 | eff: 12%]" for i in range(50)
        ) + "\nend"
        cleaned = generate_markdown._clean_stream_text(text)
        assert cleaned == "start\n49it [00:49, bound: 3 | eff: 12%]\nend"

    def test_separate_progress_runs_kept_apart(self):
        text = "0it [a]\n1it [b]\nbetween\n0it [c]\n1it [d]"
        cleaned = generate_markdown._clean_stream_text(text)
        assert cleaned == "1it [b]\nbetween\n1it [d]"

    def test_blank_interleaved_progress_run_collapsed(self):
        # nbconvert renders each stream output as its own paragraph, so a
        # rendered page interleaves progress lines with blank lines.
        text = "    0it [00:00, ?it/s]\n\n    36it [00:00, nc: 3]\n\n    71it [00:00, nc: 1]\n\nafter"
        cleaned = generate_markdown._clean_stream_text(text)
        assert cleaned == "    71it [00:00, nc: 1]\n\nafter"

    def test_split_stream_outputs_merged_before_truncation(self, tmp_path):
        # Samplers emit each progress line as its OWN stream output; the
        # per-cell merge must let truncation fire on the concatenation.
        notebook = {
            "cells": [
                {
                    "cell_type": "code",
                    "outputs": [
                        {"output_type": "stream", "name": "stderr", "text": [f"line {i}\n"]}
                        for i in range(200)
                    ]
                    + [{"output_type": "display_data", "data": {}}],
                }
            ]
        }
        path = tmp_path / "nb.ipynb"
        path.write_text(json.dumps(notebook))
        generate_markdown.clean_notebook_outputs(path)
        cleaned = json.loads(path.read_text())
        outputs = cleaned["cells"][0]["outputs"]
        assert len(outputs) == 2
        assert outputs[0]["output_type"] == "stream"
        assert "truncated" in outputs[0]["text"]
        assert outputs[0]["text"].startswith("line 0\n")
        assert outputs[1]["output_type"] == "display_data"

    def test_split_progress_outputs_collapse_across_merge(self, tmp_path):
        notebook = {
            "cells": [
                {
                    "cell_type": "code",
                    "outputs": [
                        {"output_type": "stream", "name": "stderr", "text": [f"{i}it [00:27, nc: 5]\n"]}
                        for i in range(2480)
                    ],
                }
            ]
        }
        path = tmp_path / "nb.ipynb"
        path.write_text(json.dumps(notebook))
        generate_markdown.clean_notebook_outputs(path)
        cleaned = json.loads(path.read_text())
        outputs = cleaned["cells"][0]["outputs"]
        assert len(outputs) == 1
        assert outputs[0]["text"] == "2479it [00:27, nc: 5]\n"


class TestOptimizePngs:
    def test_quantizes_in_place_and_shrinks(self, tmp_path):
        from PIL import Image
        import random

        files_dir = tmp_path / "page_files"
        files_dir.mkdir()
        png = files_dir / "fig_0.png"
        random.seed(0)
        image = Image.new("RGB", (128, 128))
        image.putdata(
            [
                (random.randrange(50, 200), random.randrange(50, 200), 30)
                for _ in range(128 * 128)
            ]
        )
        image.save(png)
        before = png.stat().st_size
        generate_markdown.optimize_pngs(files_dir)
        after = png.stat().st_size
        assert after < before
        with Image.open(png) as reopened:
            assert reopened.size == (128, 128)
        assert not list(files_dir.glob("*.opt"))

    def test_missing_dir_is_noop(self, tmp_path):
        assert generate_markdown.optimize_pngs(tmp_path / "absent") == (0, 0)


def _noisy_png(path: Path, seed: int = 0) -> None:
    """A 128x128 image that quantizes well — the shape matplotlib figures have."""
    from PIL import Image
    import random

    random.seed(seed)
    image = Image.new("RGB", (128, 128))
    image.putdata(
        [
            (random.randrange(50, 200), random.randrange(50, 200), 30)
            for _ in range(128 * 128)
        ]
    )
    image.save(path)


class TestOptimizeExisting:
    def test_walks_every_files_dir_and_shrinks(self, tmp_path):
        pages = [
            tmp_path / "markdown" / "start_here_files",
            tmp_path / "markdown" / "imaging" / "modeling_files",
        ]
        pngs = []
        for i, files_dir in enumerate(pages):
            files_dir.mkdir(parents=True)
            png = files_dir / "fig_0.png"
            _noisy_png(png, seed=i)
            pngs.append(png)
        before_sizes = [png.stat().st_size for png in pngs]

        total_before, total_after = generate_markdown.optimize_existing(tmp_path)

        assert total_after < total_before
        assert total_before == sum(before_sizes)
        for png in pngs:
            assert png.stat().st_size < before_sizes[pngs.index(png)]
        assert not list(tmp_path.rglob("*.opt"))

    def test_leaves_everything_outside_markdown_alone(self, tmp_path):
        outside = tmp_path / "dataset" / "imaging_files"
        outside.mkdir(parents=True)
        untouched = outside / "fig_0.png"
        _noisy_png(untouched)
        before = untouched.stat().st_size

        files_dir = tmp_path / "markdown" / "page_files"
        files_dir.mkdir(parents=True)
        _noisy_png(files_dir / "fig_0.png")

        generate_markdown.optimize_existing(tmp_path)

        assert untouched.stat().st_size == before

    def test_is_idempotent(self, tmp_path):
        files_dir = tmp_path / "markdown" / "page_files"
        files_dir.mkdir(parents=True)
        _noisy_png(files_dir / "fig_0.png")

        generate_markdown.optimize_existing(tmp_path)
        settled = (files_dir / "fig_0.png").read_bytes()
        second_before, second_after = generate_markdown.optimize_existing(tmp_path)

        assert (files_dir / "fig_0.png").read_bytes() == settled
        assert second_after == second_before

    def test_no_markdown_dir_is_noop(self, tmp_path):
        assert generate_markdown.optimize_existing(tmp_path) == (0, 0)

    def test_empty_markdown_dir_is_noop(self, tmp_path):
        (tmp_path / "markdown").mkdir()
        assert generate_markdown.optimize_existing(tmp_path) == (0, 0)


class TestMarkdownHeader:
    def test_scripts_page_links(self):
        header = generate_markdown._markdown_header(
            Path("scripts/imaging/modeling.py"), Path("markdown/imaging")
        )
        assert "../../scripts/imaging/modeling.py" in header
        assert "../../notebooks/imaging/modeling.ipynb" in header
        assert "auto-generated" in header

    def test_root_page_links(self):
        header = generate_markdown._markdown_header(
            Path("start_here.py"), Path("markdown")
        )
        assert "(../start_here.py)" in header
        assert "(../start_here.ipynb)" in header


class TestScriptTitle:
    def test_docstring_title(self, tmp_path):
        _make_script(tmp_path, "s.py", docstring="Modeling: Start Here\n====")
        assert generate_markdown.script_title(tmp_path / "s.py") == "Modeling: Start Here"

    def test_emphasis_markers_stripped(self, tmp_path):
        _make_script(tmp_path, "s.py", docstring="__Log Likelihood Function__")
        assert (
            generate_markdown.script_title(tmp_path / "s.py")
            == "Log Likelihood Function"
        )

    def test_no_docstring_falls_back_to_stem(self, tmp_path):
        script = tmp_path / "bare.py"
        script.write_text("print('hi')\n")
        assert generate_markdown.script_title(script) == "bare"


class TestTrackedFileProtection:
    def _git_workspace(self, tmp_path):
        subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
        subprocess.run(
            ["git", "config", "user.email", "t@t"], cwd=tmp_path, check=True
        )
        subprocess.run(["git", "config", "user.name", "t"], cwd=tmp_path, check=True)
        (tmp_path / "dataset.txt").write_text("original")
        subprocess.run(["git", "add", "dataset.txt"], cwd=tmp_path, check=True)
        subprocess.run(
            ["git", "commit", "-qm", "init"], cwd=tmp_path, check=True
        )
        return tmp_path

    def test_modified_tracked_file_restored(self, tmp_path):
        workspace = self._git_workspace(tmp_path)
        (workspace / "dataset.txt").write_text("clobbered by simulator")
        restored = generate_markdown.restore_tracked_files(workspace)
        assert restored == ["dataset.txt"]
        assert (workspace / "dataset.txt").read_text() == "original"

    def test_pre_dirty_files_excluded(self, tmp_path):
        workspace = self._git_workspace(tmp_path)
        (workspace / "dataset.txt").write_text("hand edit before build")
        restored = generate_markdown.restore_tracked_files(
            workspace, exclude=frozenset(["dataset.txt"])
        )
        assert restored == []
        assert (workspace / "dataset.txt").read_text() == "hand edit before build"

    def test_markdown_and_untracked_left_alone(self, tmp_path):
        workspace = self._git_workspace(tmp_path)
        md = workspace / "markdown"
        md.mkdir()
        (md / "page.md").write_text("new page")
        (workspace / "output.log").write_text("untracked")
        assert generate_markdown.restore_tracked_files(workspace) == []
        assert (md / "page.md").read_text() == "new page"
        assert (workspace / "output.log").exists()


class TestRedactionRoots:
    """
    Where the sibling checkouts live — the assumption that broke in worktrees.

    A canonical checkout has the libraries in ``workspace_path.parent``; a task
    worktree does not (the libraries stay in the canonical tree), so a page
    rendered from a worktree used to publish the developer's home directory.
    """

    LIBRARY_WARNING = (
        "{root}/PyAutoArray/autoarray/operators/convolver.py:1415: UserWarning"
    )

    def _git(self, repo, *args):
        subprocess.run(["git", *args], cwd=repo, check=True, capture_output=True)

    def _canonical_workspace(self, tmp_path):
        """``<tmp>/checkouts/example_workspace``, a real checkout with a commit."""
        workspace = tmp_path / "checkouts" / "example_workspace"
        workspace.mkdir(parents=True)
        self._git(workspace, "init", "-q")
        self._git(workspace, "config", "user.email", "t@t")
        self._git(workspace, "config", "user.name", "t")
        (workspace / "start_here.py").write_text("print('hi')\n")
        self._git(workspace, "add", "start_here.py")
        self._git(workspace, "commit", "-qm", "init")
        return workspace

    def _worktree_workspace(self, tmp_path, canonical):
        """``<tmp>/checkouts-wt/<task>/example_workspace``, a worktree of it."""
        dest = tmp_path / "checkouts-wt" / "a-task" / "example_workspace"
        self._git(canonical, "worktree", "add", "-q", "-b", "a-task", str(dest))
        return dest

    def _render(self, workspace, warning_root):
        return generate_markdown._clean_stream_text(
            self.LIBRARY_WARNING.format(root=warning_root),
            redactions=generate_markdown._redactions_for(workspace),
        )

    def test_canonical_checkout_redacts_sibling_library(self, tmp_path, monkeypatch):
        monkeypatch.delenv("PYAUTO_MAIN", raising=False)
        canonical = self._canonical_workspace(tmp_path)
        cleaned = self._render(canonical, canonical.parent)
        assert cleaned == (
            ".../PyAutoArray/autoarray/operators/convolver.py:1415: UserWarning"
        )

    def test_worktree_redacts_canonical_sibling_library(self, tmp_path, monkeypatch):
        # The bug: the libraries resolve to the CANONICAL tree while the
        # workspace is in the worktree, so `workspace_path.parent` matches
        # nothing and the home path used to be published verbatim.
        monkeypatch.delenv("PYAUTO_MAIN", raising=False)
        canonical = self._canonical_workspace(tmp_path)
        worktree = self._worktree_workspace(tmp_path, canonical)
        cleaned = self._render(worktree, canonical.parent)
        assert cleaned == (
            ".../PyAutoArray/autoarray/operators/convolver.py:1415: UserWarning"
        )
        assert str(tmp_path) not in cleaned

    def test_worktree_and_canonical_publish_the_same_page(self, tmp_path, monkeypatch):
        monkeypatch.delenv("PYAUTO_MAIN", raising=False)
        canonical = self._canonical_workspace(tmp_path)
        worktree = self._worktree_workspace(tmp_path, canonical)
        assert self._render(worktree, canonical.parent) == self._render(
            canonical, canonical.parent
        )

    def test_worktree_own_siblings_still_redacted(self, tmp_path, monkeypatch):
        # A worktree render legitimately sees paths from BOTH trees: sibling
        # library worktrees live next to the workspace worktree.
        monkeypatch.delenv("PYAUTO_MAIN", raising=False)
        canonical = self._canonical_workspace(tmp_path)
        worktree = self._worktree_workspace(tmp_path, canonical)
        assert self._render(worktree, worktree.parent) == (
            ".../PyAutoArray/autoarray/operators/convolver.py:1415: UserWarning"
        )

    def test_workspace_path_itself_wins_over_its_root(self, tmp_path, monkeypatch):
        # Order matters: the checkout root is a prefix of the workspace path,
        # so redacting it first would mangle the workspace path to `.../name`.
        monkeypatch.delenv("PYAUTO_MAIN", raising=False)
        canonical = self._canonical_workspace(tmp_path)
        cleaned = generate_markdown._clean_stream_text(
            f"Working Directory has been set to `{canonical}`",
            redactions=generate_markdown._redactions_for(canonical),
        )
        assert cleaned == "Working Directory has been set to `example_workspace`"

    def test_redactions_ordered_longest_first(self, tmp_path, monkeypatch):
        monkeypatch.delenv("PYAUTO_MAIN", raising=False)
        canonical = self._canonical_workspace(tmp_path)
        worktree = self._worktree_workspace(tmp_path, canonical)
        lengths = [len(old) for old, _ in generate_markdown._redactions_for(worktree)]
        assert lengths == sorted(lengths, reverse=True)

    def test_pyauto_main_redacted_when_set(self, tmp_path, monkeypatch):
        # No git repo here at all: PYAUTO_MAIN is the workspace's own answer to
        # "where is the canonical checkout" and must still be scrubbed.
        monkeypatch.setenv("PYAUTO_MAIN", str(tmp_path / "checkouts"))
        workspace = tmp_path / "elsewhere" / "example_workspace"
        workspace.mkdir(parents=True)
        assert self._render(workspace, tmp_path / "checkouts") == (
            ".../PyAutoArray/autoarray/operators/convolver.py:1415: UserWarning"
        )

    def test_root_at_or_above_home_never_redacted(self, tmp_path, monkeypatch):
        # A root that is the home directory (or above it) would rewrite the
        # home prefix to `...` and mangle paths that should render as `~`.
        home = tmp_path / "home" / "dev"
        home.mkdir(parents=True)
        monkeypatch.setenv("HOME", str(home))
        monkeypatch.setenv("PYAUTO_MAIN", str(home))
        workspace = home / "example_workspace"
        workspace.mkdir()
        cleaned = generate_markdown._clean_stream_text(
            f"cache at {home}/.cache/x",
            redactions=generate_markdown._redactions_for(workspace),
        )
        assert cleaned == "cache at ~/.cache/x"


class TestLocalPathGuard:
    def test_clean_page_passes(self, tmp_path):
        page = tmp_path / "page.md"
        page.write_text("Working Directory has been set to `example_workspace`\n")
        generate_markdown.check_no_local_paths(page)

    def test_leaked_home_path_fails_the_build(self, tmp_path):
        page = tmp_path / "page.md"
        page.write_text(
            "/home/dev/Code/checkouts/PyAutoArray/autoarray/convolver.py:1: Warning\n"
        )
        with pytest.raises(RuntimeError, match="absolute local paths"):
            generate_markdown.check_no_local_paths(page)

    def test_leaked_macos_path_fails_the_build(self, tmp_path):
        page = tmp_path / "page.md"
        page.write_text("loaded /Users/dev/Code/checkouts/PyAutoArray/x.py\n")
        with pytest.raises(RuntimeError, match="/Users/dev"):
            generate_markdown.check_no_local_paths(page)

    def test_leaked_non_standard_home_fails_the_build(self, tmp_path, monkeypatch):
        home = tmp_path / "mnt" / "ral" / "dev"
        home.mkdir(parents=True)
        monkeypatch.setenv("HOME", str(home))
        page = tmp_path / "page.md"
        page.write_text(f"output written to {home}/checkouts/output\n")
        with pytest.raises(RuntimeError, match="absolute local paths"):
            generate_markdown.check_no_local_paths(page)
