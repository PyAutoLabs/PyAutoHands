#!/usr/bin/env python
"""
Build the workspace-validation script matrix.

By default a project is sharded by directory: one entry per
``<project>/scripts/<subdir>/``, each run as its own job.

A project named with ``--ordered`` is instead emitted as ONE entry that carries
its ordered smoke list (``smoke_tests.txt``), to be run in a single job via
``run_python.py --list``. This is for projects whose smoke scripts depend on
each other's output (the Euclid pipeline: ``scripts/tools/diagnose_latent.py``
replays fits that ``start_here.py`` and the top-level ``scripts/*.py`` produce
earlier in the list), so per-directory sharding would run a consumer without
its producers. The opt-in is explicit and owned by the caller (the workflow),
not inferred from ``smoke_tests.txt`` being present — every workspace has one.
"""
import json
from argparse import ArgumentParser
from pathlib import Path

SMOKE_LIST = "smoke_tests.txt"


def make_script_matrix(project):
    return [
        {
            "name": project,
            "directory": path.name,
        }
        for path in (Path(project) / "scripts").glob("*/")
        if path.is_dir()
    ]


def make_ordered_entry(project):
    """
    The single matrix entry for a project whose smoke list is order-dependent.

    ``directory`` is ``"."`` because the list's entries are paths relative to
    the project root (``start_here.py``, ``scripts/<name>.py``); the runner
    resolves them against ``<cwd>/<directory>`` with the project root as cwd.
    """
    return {
        "name": project,
        "directory": ".",
        "script_list": SMOKE_LIST,
    }


def make_combined_script_matrix(projects, ordered=()):
    ordered = set(ordered)
    unknown = ordered - set(projects)
    if unknown:
        raise ValueError(
            f"--ordered names project(s) not in the matrix: {sorted(unknown)}"
        )
    matrix = []
    for project in projects:
        if project in ordered:
            matrix.append(make_ordered_entry(project))
        else:
            matrix.extend(make_script_matrix(project))
    return matrix


def main(argv=None):
    parser = ArgumentParser(description=__doc__.strip().splitlines()[0])
    parser.add_argument("projects", nargs="*", help="Project directories to shard")
    parser.add_argument(
        "--ordered",
        action="append",
        default=[],
        metavar="PROJECT",
        help=(
            f"Run PROJECT's ordered {SMOKE_LIST} as one shard instead of one "
            "shard per scripts/<subdir>. Repeatable."
        ),
    )
    args = parser.parse_args(argv)
    return make_combined_script_matrix(args.projects, ordered=args.ordered)


if __name__ == "__main__":
    print(json.dumps(main()))
