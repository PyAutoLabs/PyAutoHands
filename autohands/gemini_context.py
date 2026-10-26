"""
Stamp or audit Colab Gemini instructions on a notebooks tree (PyAutoHands#324).

The release's ``generate.py`` stamps every notebook it generates. This is the
same injector for notebooks outside that path — the CTI workspace, which the
release does not generate — plus the coverage report that assistant upkeep and
PyAutoBroca read.

    autohands gemini_context apply <notebooks_dir> --project P --assistant-root A
        [--repo-name R] [--repo-root DIR]
    autohands gemini_context report --workspace W --project P --assistant-root A
        [--repo-name R] [--json FILE]

``apply`` names each notebook "<repo>/<path relative to the repo root>" for
matching. The repo root defaults to the parent of ``<notebooks_dir>`` when that
folder is called ``notebooks`` (the workspace layout), else the folder itself.

``report`` is deterministic: the notebooks only the ``default`` entry reaches
(and the folders made up entirely of them), mapping entries for this repo that
match nothing, mapped skills missing on disk, skills mapped against the
mapping's own ``never_map`` list, and the assembled sizes against the cap. It
writes JSON (``--json``, else stdout after the text summary) and exits 1 when a
skill is missing, a never_map skill is mapped, or any notebook is over the cap.
"""

import json
import statistics
import sys
from argparse import ArgumentParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import build_util

_SKIP_PARTS = {".git", ".ipynb_checkpoints", "output"}


def iter_notebooks(root):
    """Every ``*.ipynb`` under ``root`` in sorted order, minus checkpoints and outputs."""
    root = Path(root)
    return sorted(
        (
            p
            for p in root.rglob("*.ipynb")
            if not _SKIP_PARTS.intersection(p.relative_to(root).parts)
        ),
        key=lambda p: p.as_posix(),
    )


def _repo_name(project, repo_name):
    if repo_name:
        return repo_name
    if project not in build_util.COLAB_WORKSPACE_REPOS:
        raise SystemExit(f"gemini_context: pass --repo-name for project '{project}'.")
    return build_util.COLAB_WORKSPACE_REPOS[project]


def apply(notebooks_dir, project, assistant_root, repo_name=None, repo_root=None):
    """Stamp every notebook under ``notebooks_dir``; returns ``{relpath: entry}``."""
    notebooks_dir = Path(notebooks_dir).resolve()
    if repo_root is None:
        repo_root = notebooks_dir.parent if notebooks_dir.name == "notebooks" else notebooks_dir
    repo_root = Path(repo_root).resolve()
    repo_name = _repo_name(project, repo_name)
    contexts = build_util.load_gemini_contexts(assistant_root)

    applied = {}
    for notebook in iter_notebooks(notebooks_dir):
        relpath = notebook.relative_to(repo_root).as_posix()
        applied[relpath] = build_util.inject_gemini_instructions(
            notebook, project, assistant_root, relpath, repo_name=repo_name, contexts=contexts
        )
    return applied


def report(workspace, project, assistant_root, repo_name=None):
    """The coverage report for one workspace against one assistant mapping."""
    workspace = Path(workspace).resolve()
    assistant_root = Path(assistant_root).resolve()
    repo_name = _repo_name(project, repo_name)
    contexts = build_util.load_gemini_contexts(assistant_root, enforce_never_map=False)
    cap = build_util.GEMINI_CONTEXT_CAP

    rows = []
    for notebook in iter_notebooks(workspace):
        relpath = notebook.relative_to(workspace).as_posix()
        label, skills, text, missing = build_util.assemble_gemini_context(
            assistant_root, f"{repo_name}/{relpath}", contexts
        )
        rows.append({"notebook": relpath, "entry": label, "chars": len(text), "missing": missing})

    entries = [("default", contexts["default"]["skills"])] + [
        (e["match"], e["skills"]) for e in contexts["contexts"]
    ]
    missing_skills = {
        label: [s for s in skills if not (assistant_root / "skills" / f"{s}.md").is_file()]
        for label, skills in entries
    }
    missing_skills = {k: v for k, v in missing_skills.items() if v}
    never_map = set(contexts.get("never_map") or [])
    never_mapped = {
        label: sorted(never_map.intersection(skills))
        for label, skills in entries
        if never_map.intersection(skills)
    }

    matched = {r["entry"] for r in rows}
    unused_entries = [
        e["match"]
        for e in contexts["contexts"]
        if e["match"].startswith(f"{repo_name}/") and e["match"] not in matched
    ]

    default_notebooks = [r["notebook"] for r in rows if r["entry"] == "default"]
    folders = {}
    for r in rows:
        folders.setdefault(str(Path(r["notebook"]).parent.as_posix()), []).append(r["entry"])
    default_only_folders = sorted(
        folder for folder, labels in folders.items() if set(labels) == {"default"}
    )

    sizes = [r["chars"] for r in rows]
    per_entry = {}
    for r in rows:
        stats = per_entry.setdefault(r["entry"], {"notebooks": 0, "max_chars": 0})
        stats["notebooks"] += 1
        stats["max_chars"] = max(stats["max_chars"], r["chars"])

    result = {
        "workspace": repo_name,
        "project": project,
        "assistant": assistant_root.name,
        "cap": cap,
        "notebooks": len(rows),
        "default_notebooks": default_notebooks,
        "default_only_folders": default_only_folders,
        "unused_entries": unused_entries,
        "missing_skills": missing_skills,
        "never_map_violations": never_mapped,
        "sizes": {
            "max": max(sizes) if sizes else 0,
            "median": int(statistics.median(sizes)) if sizes else 0,
            "over_cap": [
                {"notebook": r["notebook"], "entry": r["entry"], "chars": r["chars"]}
                for r in rows
                if r["chars"] > cap
            ],
            "largest": [
                {"notebook": r["notebook"], "entry": r["entry"], "chars": r["chars"]}
                for r in sorted(rows, key=lambda r: (-r["chars"], r["notebook"]))[:5]
            ],
        },
        "entries": dict(sorted(per_entry.items())),
    }
    result["ok"] = not (missing_skills or never_mapped or result["sizes"]["over_cap"])
    return result


def format_report(result):
    """A short human summary of ``report``'s result."""
    sizes = result["sizes"]
    lines = [
        f"{result['workspace']} vs {result['assistant']}: {result['notebooks']} notebooks, "
        f"{len(result['entries'])} mapping entries used",
        f"  sizes: max {sizes['max']}, median {sizes['median']}, cap {result['cap']}, "
        f"over cap {len(sizes['over_cap'])}",
        f"  default only: {len(result['default_notebooks'])} notebooks, "
        f"{len(result['default_only_folders'])} folders",
    ]
    for folder in result["default_only_folders"]:
        lines.append(f"    {folder}/")
    if result["unused_entries"]:
        lines.append(f"  entries matching nothing: {', '.join(result['unused_entries'])}")
    for label, skills in result["missing_skills"].items():
        lines.append(f"  MISSING skills in '{label}': {', '.join(skills)}")
    for label, skills in result["never_map_violations"].items():
        lines.append(f"  NEVER_MAP skills in '{label}': {', '.join(skills)}")
    for row in sizes["over_cap"]:
        lines.append(f"  OVER CAP: {row['notebook']} ({row['entry']}, {row['chars']})")
    lines.append("  OK" if result["ok"] else "  FAILED")
    return "\n".join(lines)


def main(argv=None):
    parser = ArgumentParser(prog="autohands gemini_context", description=__doc__.split("\n\n")[1])
    sub = parser.add_subparsers(dest="command", required=True)

    p_apply = sub.add_parser("apply", help="Stamp every notebook under a folder")
    p_apply.add_argument("notebooks_dir")
    p_apply.add_argument("--project", required=True)
    p_apply.add_argument("--assistant-root", required=True)
    p_apply.add_argument("--repo-name", default=None)
    p_apply.add_argument("--repo-root", default=None)

    p_report = sub.add_parser("report", help="Coverage report for a workspace")
    p_report.add_argument("--workspace", required=True)
    p_report.add_argument("--project", required=True)
    p_report.add_argument("--assistant-root", required=True)
    p_report.add_argument("--repo-name", default=None)
    p_report.add_argument("--json", default=None, help="Write the JSON report here")

    args = parser.parse_args(argv)

    if args.command == "apply":
        applied = apply(
            args.notebooks_dir, args.project, args.assistant_root,
            repo_name=args.repo_name, repo_root=args.repo_root,
        )
        counts = {}
        for label in applied.values():
            counts[label] = counts.get(label, 0) + 1
        print(f"Stamped {len(applied)} notebooks:")
        for label, count in sorted(counts.items()):
            print(f"  {count:4d}  {label}")
        return 0

    result = report(args.workspace, args.project, args.assistant_root, repo_name=args.repo_name)
    print(format_report(result))
    payload = json.dumps(result, indent=2) + "\n"
    if args.json:
        Path(args.json).write_text(payload)
    else:
        print(payload)
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
