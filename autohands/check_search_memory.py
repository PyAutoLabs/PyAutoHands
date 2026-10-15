#!/usr/bin/env python
"""Fail when a workspace script leaves a gradient multi-start search unbatched.

Every ``af.MultiStart*`` search (``MultiStartProdigy``, ``MultiStartAdam``,
``MultiStartADABelief``, ``MultiStartLion``) defaults to ``n_starts=48`` and
``batch_size=None``. ``batch_size=None`` evaluates all 48 starts in a single
``jax.vmap``, materializing the whole batched ``value_and_grad`` at once. For a
memory-heavy likelihood that is enormous: a 48-start interferometer fit measured
~1.79 GB *per start*, wanted ~86 GB, and took down two nightly release-integrate
runs in 2026-07 (PyAutoLabs/PyAutoFit#1452).

Nothing at authoring time flagged it. Both workspaces' ``interferometer/
start_here.py`` adopted the search on the same day, inherited the default, and
the first anyone knew was ``RESOURCE_EXHAUSTED`` from inside XLA on the nightly
— once with the traceback filtered away, costing a second night.

The rule here is deliberately not "batch_size must be small". It is
**``batch_size`` must be explicit**: writing ``batch_size=None`` passes. The
point is that the memory decision is typed out where a reviewer sees it, rather
than arrived at by defaulting.

Which names are guarded: with ``--manifest`` (a saved
``python -m autofit search-manifest --json`` dump) the guarded set is exactly
the manifest's ``MultiStart*`` searches, read from the installed release rather
than hard-coded here. Without it -- the stdlib-only CI leg, which must not depend
on installing the science stack -- the ``MultiStart`` prefix rule below stands
in, which is a superset of every manifest to date.

Usage:
    python check_search_memory.py --root <workspace_dir> [--scripts-dir scripts]
                                  [--manifest manifest.json]

Exit codes:
    0  no unbatched multi-start searches found
    1  at least one found (details on stdout)
    2  usage error (root or scripts dir missing)
"""

import argparse
import ast
import json
import sys
from pathlib import Path
from typing import FrozenSet, List, NamedTuple, Optional

# Fallback when no manifest is given: any search whose name starts with this is
# a gradient multi-start search and carries the batch_size knob. Matched by
# prefix rather than an enumerated list so a new MultiStart* sibling in
# PyAutoFit is covered the day it lands.
SEARCH_PREFIX = "MultiStart"

# Not a search: the convergence-criteria object shares the prefix but takes no
# batch_size. Enumerated because it is the one known false positive.
NOT_A_SEARCH = {"MultiStartGradientConvergence"}


class Finding(NamedTuple):
    path: Path
    line: int
    search: str


def _called_name(node: ast.Call):
    """The bare callable name for ``Name(...)`` and ``a.b.Name(...)`` calls."""
    func = node.func
    if isinstance(func, ast.Attribute):
        return func.attr
    if isinstance(func, ast.Name):
        return func.id
    return None


def guarded_names(manifest: dict) -> FrozenSet[str]:
    """The manifest's multi-start searches -- the names carrying ``batch_size``."""
    return frozenset(
        s["name"] for s in manifest["searches"] if s["name"].startswith(SEARCH_PREFIX)
    )


def _guarded(name: str, names: Optional[FrozenSet[str]]) -> bool:
    if names is not None:
        return name in names
    return name.startswith(SEARCH_PREFIX) and name not in NOT_A_SEARCH


def findings_in_source(
    source: str, path: Path, names: Optional[FrozenSet[str]] = None
) -> List[Finding]:
    """Every multi-start search construction in ``source`` with no explicit
    ``batch_size``. ``names`` (from :func:`guarded_names`) replaces the prefix
    rule when given. A syntax error yields nothing — this check is not a linter
    and must not be the thing that reports a broken file."""
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return []

    found = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        name = _called_name(node)
        if name is None:
            continue
        if not _guarded(name, names):
            continue
        # **kwargs may carry batch_size; a splat keyword has arg=None. Treat
        # that as explicit rather than guess at the dict's contents.
        if any(kw.arg is None or kw.arg == "batch_size" for kw in node.keywords):
            continue
        found.append(Finding(path=path, line=node.lineno, search=name))
    return found


def check_root(
    root: Path, scripts_dir: str = "scripts", names: Optional[FrozenSet[str]] = None
) -> List[Finding]:
    scripts = root / scripts_dir
    if not scripts.is_dir():
        raise FileNotFoundError(f"scripts directory not found: {scripts}")

    found = []
    for file in sorted(scripts.rglob("*.py")):
        found.extend(
            findings_in_source(
                file.read_text(encoding="utf-8", errors="replace"), file, names
            )
        )
    return found


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", required=True, help="workspace root directory")
    parser.add_argument(
        "--scripts-dir",
        default="scripts",
        help="scripts directory relative to root (default: scripts)",
    )
    parser.add_argument(
        "--manifest",
        help="search-manifest --json dump; guards exactly its MultiStart* searches",
    )
    args = parser.parse_args(argv)

    root = Path(args.root)
    if not root.is_dir():
        print(f"error: root not found: {root}", file=sys.stderr)
        return 2

    names = None
    if args.manifest:
        try:
            names = guarded_names(json.loads(Path(args.manifest).read_text(encoding="utf-8")))
        except (OSError, ValueError, KeyError) as e:
            print(f"error: unreadable manifest {args.manifest}: {e}", file=sys.stderr)
            return 2

    try:
        found = check_root(root, args.scripts_dir, names)
    except FileNotFoundError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2

    if not found:
        print("Search memory check: no unbatched multi-start searches found.")
        return 0

    print(
        f"Search memory check: {len(found)} multi-start search(es) constructed "
        f"without an explicit `batch_size`.\n"
    )
    for f in found:
        rel = f.path.relative_to(root) if f.path.is_relative_to(root) else f.path
        print(f"  {rel}:{f.line}: {f.search}(...) has no `batch_size`")
    print(
        "\n`batch_size=None` (the default) vmaps every start into one "
        "value_and_grad and can allocate tens of GB — see PyAutoLabs/PyAutoFit#1452.\n"
        "Pass an explicit `batch_size` (e.g. `batch_size=4`). If the unbatched "
        "single-vmap really is what you want, write `batch_size=None` "
        "explicitly so the choice is visible in review."
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
