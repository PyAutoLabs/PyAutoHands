#!/usr/bin/env python3
"""Re-render every search-roster block from the installed ``autofit`` manifest.

Finds each ``<!-- search-roster:begin ... -->`` / ``<!-- search-roster:end -->``
block in the given files (default: every .md / .txt file under ``--root``
holding one) and rewrites only the text between the markers, stamped with the
manifest schema and the ``autofit`` version that rendered it. See
``search_roster.py`` for the block format.

Usage:
    python regenerate_search_roster.py --root <checkout> [--files F ...]
                                       [--manifest manifest.json]

``--manifest`` reads a saved ``python -m autofit search-manifest --json`` dump;
without it the manifest comes from the ``autofit`` importable by this
interpreter (the installed release in CI).

Exit codes: 0 done (changed or not) · 2 usage / manifest / block error.
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import search_roster  # noqa: E402


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", default=".", help="checkout to scan (default: cwd)")
    parser.add_argument("--files", nargs="+", help="explicit files (relative to --root)")
    parser.add_argument("--manifest", help="saved search-manifest --json dump")
    args = parser.parse_args(argv)

    root = Path(args.root)
    try:
        manifest = search_roster.load_manifest(args.manifest)
        paths = (
            [root / f for f in args.files] if args.files else search_roster.discover_files(root)
        )
        changed = search_roster.regenerate_files(paths, manifest, root)
    except (search_roster.RosterError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    print(
        f"Search roster: {len(paths)} file(s) with blocks, {len(changed)} rewritten "
        f"({search_roster.stamp(manifest)})"
    )
    for path in changed:
        print(f"  rewrote {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
