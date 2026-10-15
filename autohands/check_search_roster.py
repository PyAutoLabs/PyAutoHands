#!/usr/bin/env python3
"""Fail when a search roster, anchor or named search drifts from the manifest.

Three checks against the search manifest of the installed ``autofit`` (or a
saved ``--manifest`` dump), runnable locally or in CI:

  (a) Roster blocks (HARD FAIL on a changed body)
      Every ``search-roster`` block under ``--root`` (or in ``--files``) is
      re-rendered and compared. A different body is drift. An identical body
      under an older/newer version stamp is reported only, unless
      ``--strict-version``.

  (b) Anchors (HARD FAIL on a missing target), with ``--workspace-root DIR``
      Each search's ``example`` / ``integration_test`` anchor
      (``<repo>:<path>[#<Section>]``) must resolve in ``DIR/<repo>``; a
      ``#Section`` must appear as ``__Section__``. Repos not checked out under
      DIR are listed as skipped.

  (c) Named searches (HARD FAIL), with ``--names-in GLOB`` (repeatable)
      Every ``<...search...> = af.<Name>(...)`` in the matching scripts must
      name a search the manifest lists. Globs are relative to ``--root``; a
      glob matching nothing is fine (one invocation serves every workspace).

``--against-source PATH`` additionally prints how the manifest of the source
checkout at PATH differs from the installed one. It is a report, never a
failure: the installed release is the source of truth.

Usage:
    python check_search_roster.py --root <checkout> [--files F ...]
        [--manifest manifest.json] [--strict-version]
        [--workspace-root DIR] [--names-in GLOB ...] [--against-source PATH]

Exit codes: 0 clean · 1 drift (details on stdout) · 2 usage / manifest error.
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import search_roster  # noqa: E402


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", default=".", help="checkout to check (default: cwd)")
    parser.add_argument("--files", nargs="+", help="explicit files (relative to --root)")
    parser.add_argument("--manifest", help="saved search-manifest --json dump")
    parser.add_argument("--strict-version", action="store_true",
                        help="a stale version stamp fails even when the roster is identical")
    parser.add_argument("--workspace-root", help="directory holding <repo>/ checkouts for anchors")
    parser.add_argument("--names-in", action="append", default=[], metavar="GLOB",
                        help="scripts whose constructed searches must be in the manifest")
    parser.add_argument("--against-source", metavar="PATH",
                        help="report (never fail on) source-checkout manifest differences")
    args = parser.parse_args(argv)

    root = Path(args.root)
    if not root.is_dir():
        print(f"error: root not found: {root}", file=sys.stderr)
        return 2
    try:
        manifest = search_roster.load_manifest(args.manifest)
        paths = (
            [root / f for f in args.files] if args.files else search_roster.discover_files(root)
        )
        drift = search_roster.check_files(paths, manifest, root)
    except (search_roster.RosterError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    failed = False
    print(f"Search roster check against {search_roster.stamp(manifest)}")

    print(f"\n(a) roster blocks: {len(paths)} file(s)")
    for d in drift:
        fatal = d.kind in ("body", "unstamped") or args.strict_version
        failed |= fatal
        print(f"  {'FAIL' if fatal else 'note'} {d.path}:{d.line}: {d.detail}")
    if not drift:
        print("  all blocks regenerate byte-identically")

    if args.workspace_root:
        results = search_roster.resolve_anchors(manifest, Path(args.workspace_root))
        ok = sum(r.status == "ok" for r in results)
        print(f"\n(b) anchors: {ok} resolved")
        for r in results:
            if r.status == "missing":
                failed = True
                print(f"  FAIL {r.search}.{r.field} {r.anchor}: {r.detail}")
        skipped = sorted({r.detail for r in results if r.status == "skipped"})
        for detail in skipped:
            print(f"  skip {detail}")

    if args.names_in:
        scripts = sorted({p for g in args.names_in for p in root.glob(g) if p.is_file()})
        unknown = search_roster.unknown_named_searches(scripts, manifest, root)
        print(f"\n(c) named searches: {len(scripts)} script(s)")
        for where, line, name in unknown:
            failed = True
            print(f"  FAIL {where}:{line}: af.{name} is not in the search manifest")

    if args.against_source:
        try:
            source = search_roster.load_manifest(source=args.against_source)
        except search_roster.RosterError as exc:
            print(f"\n(report) source manifest unavailable: {exc}")
        else:
            diff = search_roster.manifest_difference(manifest, source)
            print(f"\n(report) source {source['autofit_version']} vs installed "
                  f"{manifest['autofit_version']}: {len(diff)} difference(s)")
            for line in diff:
                print(f"  {line}")

    if failed:
        print("\nRegenerate with regenerate_search_roster.py (blocks) or fix the "
              "named script / anchor, then commit.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
