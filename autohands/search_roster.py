"""
Search rosters generated from the versioned ``autofit`` search manifest.

Every consumer that lists the non-linear searches -- a workspace's curated
``llms.txt``, a scripts README, an assistant's skill or wiki page -- used to
carry a hand-written roster, and several had gone stale (searches removed from
the library still listed, new ones missing). This module renders those rosters
from the one source of truth instead: the ``search-manifest@1`` document the
*installed* ``autofit`` prints with::

    python -m autofit search-manifest --json

A consumer opts in by placing a fenced block in its file::

    <!-- search-roster:begin style=list -->
    <!-- search-manifest@1 autofit 2026.10.12.1 -->
    ...generated...
    <!-- search-roster:end -->

Only the text between the markers is ever written; prose outside them is left
untouched. The begin marker carries the rendering options, so no per-consumer
configuration lives here:

``style=list``   one bullet per search family (the default)
``style=table``  one Markdown table row per search, with its capabilities
``indent=N``     prefix every rendered line with N spaces (nested lists)
``link=<repo>``  render example anchors that point into ``<repo>`` as
                 relative Markdown links (a workspace linking its own scripts);
                 anchors into any other repo render as ``repo:path`` citations

The second line inside the block is the stamp: the manifest schema and the
``autofit`` version that rendered it. ``--check`` re-renders against the
installed ``autofit``; a changed roster body is drift (failure), while a body
that is identical under a newer stamp is only reported, so an ``autofit``
release that adds no search does not redden every consumer. ``strict_version``
turns the stamp difference into a failure too.

Two further checks ride on the same manifest:

* :func:`resolve_anchors` -- each search's ``example`` and ``integration_test``
  anchor (``<repo>:<path>[#<Section>]``) must exist in the named checkout under
  a workspace root, and a ``#Section`` must appear as a ``__Section__`` heading.
  Repos not checked out are reported as skipped, never failed.
* :func:`named_searches` -- every search a script constructs as
  ``search = af.<Name>(...)`` must be in the manifest (the hand-written search
  guides keep their prose; only the names they use are checked).

Stdlib only, and nothing here imports ``autofit``: the manifest is read from a
JSON file or from a subprocess, so the module is testable without the science
stack.
"""

import ast
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Dict, Iterable, List, NamedTuple, Optional, Tuple

SCHEMA = "search-manifest@1"

BEGIN_RE = re.compile(r"^(?P<lead>[ \t]*)<!-- search-roster:begin(?P<opts>[^>]*?)-->\s*$")
END_RE = re.compile(r"^[ \t]*<!-- search-roster:end -->\s*$")
STAMP_RE = re.compile(
    r"^[ \t]*<!-- (?P<schema>search-manifest@\d+) autofit (?P<version>\S+) -->\s*$"
)

STYLES = ("list", "table")

# Files scanned for roster blocks when no explicit file list is given. Rosters
# live in prose and catalogue files, never in scripts.
SCAN_SUFFIXES = (".md", ".txt")
SKIP_DIRS = {".git", "notebooks", "output", "dataset", "node_modules", "__pycache__"}


class RosterError(Exception):
    """A malformed block or an unreadable manifest."""


# ---------------------------------------------------------------------------
# Manifest loading
# ---------------------------------------------------------------------------


def load_manifest(manifest_file: Optional[str] = None, source: Optional[str] = None) -> dict:
    """The search manifest.

    ``manifest_file`` reads a saved ``--json`` dump. Otherwise the manifest is
    printed by ``python -m autofit search-manifest --json`` in a subprocess of
    the current interpreter -- the installed ``autofit``, or, with ``source``,
    the checkout at that path put first on ``PYTHONPATH``.
    """
    if manifest_file:
        text = Path(manifest_file).read_text(encoding="utf-8")
    else:
        env = dict(os.environ)
        if source:
            env["PYTHONPATH"] = str(Path(source).resolve()) + (
                os.pathsep + env["PYTHONPATH"] if env.get("PYTHONPATH") else ""
            )
        proc = subprocess.run(
            [sys.executable, "-m", "autofit", "search-manifest", "--json"],
            capture_output=True,
            text=True,
            env=env,
        )
        if proc.returncode != 0:
            tail = "\n".join(proc.stderr.strip().splitlines()[-5:])
            raise RosterError(
                f"`python -m autofit search-manifest --json` failed "
                f"(exit {proc.returncode}):\n{tail}"
            )
        text = proc.stdout
    try:
        manifest = json.loads(text)
    except json.JSONDecodeError as exc:
        raise RosterError(f"search manifest is not JSON: {exc}") from exc
    if manifest.get("schema") != SCHEMA:
        raise RosterError(
            f"unsupported manifest schema {manifest.get('schema')!r} (expected {SCHEMA})"
        )
    return manifest


def stamp(manifest: dict) -> str:
    return f"<!-- {manifest['schema']} autofit {manifest['autofit_version']} -->"


def search_names(manifest: dict) -> List[str]:
    return [s["name"] for s in manifest["searches"]]


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------


def parse_anchor(anchor: str) -> Tuple[str, str, Optional[str]]:
    """``repo:path#Section`` -> (repo, path, section or None)."""
    repo, _, rest = anchor.partition(":")
    path, _, section = rest.partition("#")
    return repo, path, (section or None)


def parse_options(opts: str) -> Dict[str, str]:
    out = {}
    for token in opts.split():
        key, sep, value = token.partition("=")
        if not sep:
            raise RosterError(f"roster option {token!r} is not key=value")
        out[key] = value
    style = out.setdefault("style", "list")
    if style not in STYLES:
        raise RosterError(f"unknown roster style {style!r} (choose from {', '.join(STYLES)})")
    if "indent" in out and not out["indent"].isdigit():
        raise RosterError(f"roster indent {out['indent']!r} is not a number")
    return out


def _example_ref(anchor: Optional[str], link: Optional[str]) -> Optional[str]:
    if not anchor:
        return None
    repo, path, _ = parse_anchor(anchor)
    if link and repo == link:
        return f"[{path}]({path})"
    return f"`{repo}:{path}`"


def _families(manifest: dict) -> List[Tuple[str, str, List[dict]]]:
    """(key, label, searches) per family, in manifest order."""
    out = []
    for key, label in manifest["families"].items():
        members = [s for s in manifest["searches"] if s["family"] == key]
        if members:
            out.append((key, label, members))
    return out


def _render_list(manifest: dict, link: Optional[str]) -> List[str]:
    lines = []
    for key, label, members in _families(manifest):
        names = []
        for s in members:
            name = f"`af.{s['name']}`"
            if s["capabilities"].get("status") == "experimental":
                name += " (experimental)"
            names.append(name)
        line = f"- **{label}** (`{key}`): " + ", ".join(names)
        examples = []
        for s in members:
            ref = _example_ref((s.get("example") or "").partition("#")[0] or None, link)
            if ref and ref not in examples:
                examples.append(ref)
        if examples:
            line += " — example: " + ", ".join(examples)
        lines.append(line)
    return lines


def _yes_no(value) -> str:
    return "yes" if value else "no"


def _render_table(manifest: dict, link: Optional[str]) -> List[str]:
    lines = [
        "| Search | Family | Status | JAX | Gradient | Evidence | Posterior | Example |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for key, _label, members in _families(manifest):
        for s in members:
            c = s["capabilities"]
            ref = _example_ref((s.get("example") or "").partition("#")[0] or None, link)
            lines.append(
                f"| `af.{s['name']}` | {key} | {c.get('status', '')} | "
                f"{c.get('jax_use', '')} | {c.get('gradient', '')} | "
                f"{_yes_no(c.get('produces_evidence'))} | {c.get('posterior_kind', '')} | "
                f"{ref or '—'} |"
            )
    return lines


def render_body(manifest: dict, options: Dict[str, str]) -> List[str]:
    """The generated lines between the stamp and the end marker."""
    link = options.get("link")
    if options["style"] == "table":
        lines = _render_table(manifest, link)
    else:
        lines = _render_list(manifest, link)
    pad = " " * int(options.get("indent", "0"))
    return [pad + line if line else line for line in lines]


# ---------------------------------------------------------------------------
# Blocks in a file
# ---------------------------------------------------------------------------


class Block(NamedTuple):
    begin: int  # index of the begin-marker line
    end: int  # index of the end-marker line
    options: Dict[str, str]
    lead: str  # whitespace before the begin marker, reused for stamp / end
    stamp_version: Optional[str]
    body: List[str]  # existing generated lines (after the stamp)


def find_blocks(lines: List[str], where: str = "<text>") -> List[Block]:
    blocks = []
    i = 0
    while i < len(lines):
        m = BEGIN_RE.match(lines[i])
        if not m:
            if END_RE.match(lines[i]):
                raise RosterError(f"{where}:{i + 1}: search-roster:end without a begin")
            i += 1
            continue
        options = parse_options(m.group("opts"))
        j = i + 1
        while j < len(lines) and not END_RE.match(lines[j]):
            if BEGIN_RE.match(lines[j]):
                raise RosterError(f"{where}:{j + 1}: nested search-roster:begin")
            j += 1
        if j == len(lines):
            raise RosterError(f"{where}:{i + 1}: search-roster:begin without an end")
        inner = lines[i + 1 : j]
        version = None
        body = inner
        if inner:
            sm = STAMP_RE.match(inner[0])
            if sm:
                version = sm.group("version")
                body = inner[1:]
        blocks.append(Block(i, j, options, m.group("lead"), version, list(body)))
        i = j + 1
    return blocks


def regenerate_text(text: str, manifest: dict, where: str = "<text>") -> Tuple[str, int]:
    """``text`` with every roster block re-rendered; (new text, block count)."""
    lines = text.split("\n")
    blocks = find_blocks(lines, where)
    for block in reversed(blocks):
        new_inner = [block.lead + stamp(manifest)] + render_body(manifest, block.options)
        lines[block.begin + 1 : block.end] = new_inner
    return "\n".join(lines), len(blocks)


class Drift(NamedTuple):
    path: str
    line: int
    kind: str  # "body" | "stamp" | "unstamped"
    detail: str


def check_text(text: str, manifest: dict, where: str = "<text>") -> List[Drift]:
    lines = text.split("\n")
    out = []
    installed = manifest["autofit_version"]
    for block in find_blocks(lines, where):
        expected = render_body(manifest, block.options)
        if block.body != expected:
            out.append(
                Drift(where, block.begin + 1, "body",
                      "roster differs from the installed manifest — regenerate")
            )
        elif block.stamp_version is None:
            out.append(Drift(where, block.begin + 1, "unstamped", "block has no manifest stamp"))
        elif block.stamp_version != installed:
            out.append(
                Drift(where, block.begin + 1, "stamp",
                      f"stamped autofit {block.stamp_version}, installed {installed}; "
                      f"roster identical")
            )
    return out


def discover_files(root: Path) -> List[Path]:
    """Every .md / .txt file under ``root`` that contains a roster block.

    Nested git checkouts (a directory holding its own ``.git``, e.g. the source
    clones an assistant's CI places under ``sources/``) are other repositories
    and are not descended into.
    """
    found = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(
            d
            for d in dirnames
            if d not in SKIP_DIRS
            and not d.startswith(".")
            and not (Path(dirpath) / d / ".git").exists()
        )
        for name in sorted(filenames):
            if not name.endswith(SCAN_SUFFIXES):
                continue
            path = Path(dirpath) / name
            try:
                text = path.read_text(encoding="utf-8")
            except (UnicodeDecodeError, OSError):
                continue
            if "<!-- search-roster:begin" in text:
                found.append(path)
    return found


def regenerate_files(paths: Iterable[Path], manifest: dict) -> List[Path]:
    """Re-render every block in ``paths``; returns the files whose text changed."""
    changed = []
    for path in paths:
        old = path.read_text(encoding="utf-8")
        new, _ = regenerate_text(old, manifest, str(path))
        if new != old:
            path.write_text(new, encoding="utf-8")
            changed.append(path)
    return changed


def check_files(paths: Iterable[Path], manifest: dict, root: Optional[Path] = None) -> List[Drift]:
    out = []
    for path in paths:
        where = str(path.relative_to(root)) if root and path.is_relative_to(root) else str(path)
        out.extend(check_text(path.read_text(encoding="utf-8"), manifest, where))
    return out


# ---------------------------------------------------------------------------
# Anchors and named searches
# ---------------------------------------------------------------------------


class AnchorResult(NamedTuple):
    search: str
    field: str  # "example" | "integration_test"
    anchor: str
    status: str  # "ok" | "missing" | "skipped"
    detail: str


def resolve_anchors(manifest: dict, workspace_root: Path) -> List[AnchorResult]:
    """Resolve each search's anchors against checkouts under ``workspace_root``."""
    out = []
    for s in manifest["searches"]:
        for field in ("example", "integration_test"):
            anchor = s.get(field)
            if not anchor:
                continue
            repo, path, section = parse_anchor(anchor)
            repo_dir = workspace_root / repo
            if not repo_dir.is_dir():
                out.append(AnchorResult(s["name"], field, anchor, "skipped",
                                        f"{repo} not checked out"))
                continue
            target = repo_dir / path
            if not target.is_file():
                out.append(AnchorResult(s["name"], field, anchor, "missing",
                                        f"{repo}/{path} does not exist"))
                continue
            if section:
                text = target.read_text(encoding="utf-8", errors="replace")
                if f"__{section}__" not in text:
                    out.append(AnchorResult(s["name"], field, anchor, "missing",
                                            f"no `__{section}__` section in {repo}/{path}"))
                    continue
            out.append(AnchorResult(s["name"], field, anchor, "ok", ""))
    return out


def _is_search_target(target: ast.expr) -> bool:
    return isinstance(target, ast.Name) and "search" in target.id.lower()


def named_searches(source: str) -> List[Tuple[int, str]]:
    """(line, Name) for every ``<…search…> = af.<Name>(...)`` in ``source``."""
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return []
    out = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign) or not isinstance(node.value, ast.Call):
            continue
        if not any(_is_search_target(t) for t in node.targets):
            continue
        func = node.value.func
        if (
            isinstance(func, ast.Attribute)
            and isinstance(func.value, ast.Name)
            and func.value.id == "af"
        ):
            out.append((node.lineno, func.attr))
    return sorted(out)


def unknown_named_searches(paths: Iterable[Path], manifest: dict, root: Optional[Path] = None):
    """(where, line, Name) for every constructed search the manifest lacks."""
    known = set(search_names(manifest))
    out = []
    for path in paths:
        where = str(path.relative_to(root)) if root and path.is_relative_to(root) else str(path)
        for line, name in named_searches(path.read_text(encoding="utf-8", errors="replace")):
            if name not in known:
                out.append((where, line, name))
    return out


# ---------------------------------------------------------------------------
# Source-vs-installed report
# ---------------------------------------------------------------------------


def manifest_difference(installed: dict, source: dict) -> List[str]:
    """Human-readable roster differences between two manifests (report only)."""
    lines = []
    a = {s["name"]: s for s in installed["searches"]}
    b = {s["name"]: s for s in source["searches"]}
    for name in sorted(b.keys() - a.keys()):
        lines.append(f"+ {name} (in source {source['autofit_version']}, not installed)")
    for name in sorted(a.keys() - b.keys()):
        lines.append(f"- {name} (installed {installed['autofit_version']}, not in source)")
    for name in sorted(a.keys() & b.keys()):
        for style in STYLES:
            opts = {"style": style}
            one_a = dict(installed, searches=[a[name]])
            one_b = dict(source, searches=[b[name]])
            if render_body(one_a, opts) != render_body(one_b, opts):
                lines.append(f"~ {name}: rendered {style} row differs")
                break
    return lines
