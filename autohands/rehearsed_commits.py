"""Resolve the library commits a release.yml run builds (M2.4, PyAutoHands#337).

Human ruling, 2026-11-12: a release publishes exactly the commits that passed
rehearsal, even if ``main`` has moved since. On 2026-11-09 the rehearsal built
one library at ``e2b05f004`` and the release leg, checking out ``main`` again
100 minutes later, published ``6ae33d433`` (four commits the rehearsal never
saw).

``release.yml``'s ``resolve_commits`` job runs this module once per run, before
anything is built, and every library checkout in the run uses its output:

- **rehearsal** (``rehearsal=true``): pin each library's ``main`` HEAD once, at
  the start of the run (or take an explicit ``commit_shas`` manifest), so every
  matrix leg builds the same set and the ``testpypi-rehearsal-version``
  artifact records exactly what was built (``rehearsal.json`` ``commit_shas``).
- **release** (live): take the commits from a rehearsal record (the
  ``testpypi-rehearsal-version`` artifact of a successful rehearsal run) and,
  when the caller also passes a ``commit_shas`` manifest, require the two to
  agree. No record, a record without ``commit_shas``, or a mismatch is a
  refusal: nothing is built, tagged or published.

``verify`` runs after each live checkout and prints the safeguard line the
decision sheet asked for: the rehearsed commit, the commit checked out, how far
``main`` has moved since, and ``identical``.

The library set is ``config/workspaces.yaml`` ``libraries`` (the released set,
release.yml's matrix order) and the owner is ``$GITHUB_REPOSITORY_OWNER`` or
``--owner``: organ code names no instance repo (tenant firewall). The GitHub
calls (run lookup, artifact download) stay in the workflow, so everything here
is testable offline; PyYAML is needed only to read the library set.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Callable, Iterable

CONFIG_PATH = Path(__file__).resolve().parent / "config" / "workspaces.yaml"


def libraries() -> tuple[str, ...]:
    """The published library set, as bare repo names, from Build config.

    These are the keys of commit_shas.json (Brain's nightly capture), of
    Heart's validation report and of release.yml's matrix ``path``, so one
    manifest addresses all three.
    """
    import yaml  # lazy: `verify` runs on a bare runner python without it

    cfg = yaml.safe_load(CONFIG_PATH.read_text()) or {}
    names = tuple(str(lib["name"]) for lib in cfg.get("libraries") or [])
    if not names:
        raise Refused(f"no libraries declared in {CONFIG_PATH}")
    return names

RECORD_FILENAME = "rehearsal.json"

_FULL_SHA = re.compile(r"^[0-9a-f]{40}$")


class Refused(Exception):
    """The release must not proceed; the message says why."""


# --------------------------------------------------------------------------
# Manifest + record parsing
# --------------------------------------------------------------------------


def _normalise(shas: object, where: str, libs: Iterable[str] | None = None) -> dict[str, str]:
    """Validate a {library: sha} mapping covering every library.

    Extra keys (e.g. ``PyAutoHands``, which Heart folds into its report) are
    ignored: only the published libraries are pinned. Full 40-hex SHAs only —
    a prefix cannot be checked out reliably and cannot be compared for
    ``identical`` without ambiguity.
    """
    if not isinstance(shas, dict):
        raise Refused(f"{where}: expected a JSON object of {{library: sha}}, got {type(shas).__name__}")
    out: dict[str, str] = {}
    missing = []
    for lib in libs if libs is not None else libraries():
        sha = shas.get(lib)
        if not sha:
            missing.append(lib)
            continue
        sha = str(sha).strip().lower()
        if not _FULL_SHA.match(sha):
            raise Refused(f"{where}: {lib} sha {sha!r} is not a full 40-character commit sha")
        out[lib] = sha
    if missing:
        raise Refused(f"{where}: no commit for {', '.join(missing)}")
    return out


def parse_manifest(text: str | None) -> dict[str, str] | None:
    """Parse a ``commit_shas`` manifest; empty/blank means "none given".

    Accepts the bare ``{library: sha}`` form (Brain's ``commit_shas.json``) or
    the wrapped ``{"commit_shas": {...}}`` form Heart also reads.
    """
    if text is None or not text.strip():
        return None
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        raise Refused(f"commit_shas manifest is not valid JSON: {exc}") from exc
    if isinstance(data, dict) and isinstance(data.get("commit_shas"), dict):
        data = data["commit_shas"]
    return _normalise(data, "commit_shas manifest")


def load_records(records_dir: Path) -> list[dict]:
    """Load every rehearsal record under ``records_dir``.

    The workflow downloads each candidate run's ``testpypi-rehearsal-version``
    artifact into ``<records_dir>/<run id>/``. The directory name is the run the
    artifact was downloaded FROM, so it — not the body's own ``run_id`` field —
    is the record's identity (``source_run_id``).
    """
    records = []
    if not records_dir.is_dir():
        return records
    for path in sorted(records_dir.rglob(RECORD_FILENAME)):
        try:
            data = json.loads(path.read_text())
        except (OSError, json.JSONDecodeError):
            continue
        if not isinstance(data, dict) or data.get("mode") != "rehearsal":
            continue
        rel = path.relative_to(records_dir)
        data["source_run_id"] = rel.parts[0] if len(rel.parts) > 1 else str(data.get("run_id", ""))
        records.append(data)
    return records


# --------------------------------------------------------------------------
# Resolution
# --------------------------------------------------------------------------


def _diff(manifest: dict[str, str], recorded: dict[str, str]) -> list[str]:
    return [
        f"  {lib}: manifest {manifest[lib][:12]} != rehearsed {recorded[lib][:12]}"
        for lib in manifest
        if manifest[lib] != recorded.get(lib)
    ]


def resolve_release(
    manifest: dict[str, str] | None,
    records: list[dict],
    rehearsal_run_id: str | None = None,
) -> tuple[dict[str, str], dict]:
    """Return ``(commits, record)`` for a live release, or raise ``Refused``.

    - ``rehearsal_run_id`` given: that run's record is the authority; a
      manifest, if also given, must match it exactly.
    - only a manifest given: some record must carry exactly those commits.
    - neither: refuse — there is nothing to say what was rehearsed.
    """
    run_id = (rehearsal_run_id or "").strip() or None
    if manifest is None and run_id is None:
        raise Refused(
            "no rehearsal named: pass rehearsal_run_id (the rehearsal run of release.yml) "
            "and/or commit_shas (the rehearsed commits). A live release builds only rehearsed commits."
        )

    candidates = records
    if run_id is not None:
        candidates = [r for r in records if str(r.get("source_run_id")) == run_id]
        if not candidates:
            raise Refused(
                f"no rehearsal record for run {run_id}: its testpypi-rehearsal-version artifact "
                "is missing (not a successful rehearsal run, or the artifact expired)."
            )

    usable = []
    unusable = []
    for record in candidates:
        try:
            usable.append((_normalise(record.get("commit_shas"), f"rehearsal run {record.get('source_run_id')}"), record))
        except Refused as exc:
            unusable.append(str(exc))
    if not usable:
        detail = "; ".join(unusable) or "no rehearsal records found"
        raise Refused(
            "no rehearsal record carries the commits it built (a rehearsal from before "
            f"PyAutoHands#337 does not record them — rehearse again): {detail}"
        )

    if manifest is None:
        # run_id is set here; one run has one artifact.
        commits, record = usable[0]
        return commits, record

    for commits, record in usable:
        if commits == manifest:
            return commits, record

    if run_id is not None:
        commits, _ = usable[0]
        raise Refused(
            f"the recorded commits of rehearsal run {run_id} do not match the commit_shas manifest:\n"
            + "\n".join(_diff(manifest, commits))
        )
    raise Refused(
        f"no rehearsal record matches the commit_shas manifest ({len(usable)} recent rehearsal "
        "record(s) checked): these exact commits were never rehearsed."
    )


def main_heads(
    owner: str = "",
    libs: Iterable[str] | None = None,
    ls_remote: Callable[[str], str] | None = None,
) -> dict[str, str]:
    """Each library's current ``main`` HEAD, read once (public repos, no token)."""
    libs = tuple(libs if libs is not None else libraries())

    def _default(lib: str) -> str:
        if not owner:
            raise Refused("no GitHub owner to read main HEADs from ($GITHUB_REPOSITORY_OWNER or --owner)")
        out = subprocess.run(
            ["git", "ls-remote", f"https://github.com/{owner}/{lib}.git", "refs/heads/main"],
            capture_output=True, text=True, check=True,
        ).stdout
        return out.split()[0] if out.strip() else ""

    fetch = ls_remote or _default
    heads = {lib: fetch(lib).strip().lower() for lib in libs}
    return _normalise(heads, "main HEADs", libs)


def resolve_rehearsal(
    manifest: dict[str, str] | None,
    heads: Callable[[], dict[str, str]],
) -> dict[str, str]:
    """The commits a rehearsal builds: the manifest if given, else main HEADs now."""
    return manifest if manifest is not None else heads()


# --------------------------------------------------------------------------
# Post-checkout safeguard
# --------------------------------------------------------------------------


def _git(repo_dir: Path, *args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(repo_dir), *args], capture_output=True, text=True, check=True
    ).stdout.strip()


def verify_checkout(repo_dir: Path, expected: str, main_ref: str = "origin/main") -> list[str]:
    """Assert HEAD is the pinned commit AND is on ``main``; return log lines.

    Runs in both modes: in each rehearsal leg (so a ``commit_shas`` input naming
    a PR head, a side branch or any other fetchable commit never becomes a
    rehearsal record) and in each live release leg (so it is never published).
    "On main" means ``git merge-base --is-ancestor HEAD <main_ref>``; a clone
    without ``<main_ref>`` cannot prove it and is refused.

    ``main`` having moved past the commit is reported, not refused: the ruling
    is to release the rehearsed commit; later merges wait for the next release.
    Because the commit is an ancestor of ``main``, ``HEAD..main`` counts exactly
    the commits merged since, so the number reported is the real lag.
    """
    expected = expected.strip().lower()
    head = _git(repo_dir, "rev-parse", "HEAD").lower()
    if head != expected:
        raise Refused(f"checked out {head} but the pinned commit is {expected}")
    try:
        main = _git(repo_dir, "rev-parse", "--verify", f"{main_ref}^{{commit}}").lower()
    except subprocess.CalledProcessError as exc:
        raise Refused(
            f"{main_ref} is not in this clone, so {head} cannot be shown to be on main "
            "(check out with full history)"
        ) from exc
    on_main = subprocess.run(
        ["git", "-C", str(repo_dir), "merge-base", "--is-ancestor", head, main],
        capture_output=True, text=True,
    )
    if on_main.returncode == 1:
        raise Refused(
            f"{head} is not on main ({main_ref} = {main}): only commits merged to main "
            "are rehearsed or released (a PR head or side-branch commit is refused)"
        )
    if on_main.returncode != 0:
        raise Refused(f"could not check whether {head} is on main: {on_main.stderr.strip()}")
    lines = [f"pinned commit:    {expected}", f"checked out:      {head}  (identical, on main)"]
    if main == head:
        lines.append(f"{main_ref}: {main}  (main has not moved past it)")
    else:
        ahead = _git(repo_dir, "rev-list", "--count", f"{head}..{main}")
        lines.append(
            f"{main_ref}: {main}  (main has {ahead} commit(s) merged after this one; "
            "they are not in this build and wait for the next release)"
        )
    return lines


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------


def _emit(commits: dict[str, str], out: Path | None) -> None:
    compact = json.dumps(commits, sort_keys=True, separators=(",", ":"))
    if out is not None:
        out.write_text(json.dumps(commits, indent=2, sort_keys=True) + "\n")
    gh_out = os.environ.get("GITHUB_OUTPUT")
    if gh_out:
        with open(gh_out, "a") as fh:
            fh.write(f"commit_shas={compact}\n")
    for lib, sha in commits.items():
        print(f"  {lib:<13} {sha}")


def _cmd_rehearsal(args: argparse.Namespace) -> int:
    manifest = parse_manifest(args.commit_shas)
    commits = resolve_rehearsal(manifest, heads=lambda: main_heads(args.owner))
    print("Rehearsal builds " + ("the commit_shas manifest:" if manifest else "main HEADs pinned now:"))
    _emit(commits, args.out)
    return 0


def _cmd_release(args: argparse.Namespace) -> int:
    manifest = parse_manifest(args.commit_shas)
    records = load_records(args.records_dir)
    commits, record = resolve_release(manifest, records, args.rehearsal_run_id)
    print(
        f"Release builds the commits rehearsed in run {record.get('source_run_id')} "
        f"(TestPyPI {record.get('version', '?')}):"
    )
    _emit(commits, args.out)
    return 0


def _cmd_verify(args: argparse.Namespace) -> int:
    for line in verify_checkout(args.repo_dir, args.expected, args.main_ref):
        print(line)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("rehearsal", help="pin the commits a rehearsal builds")
    p.add_argument("--commit-shas", default="", help="optional JSON manifest {library: sha}")
    p.add_argument("--owner", default=os.environ.get("GITHUB_REPOSITORY_OWNER", ""),
                   help="GitHub owner of the libraries (default: $GITHUB_REPOSITORY_OWNER)")
    p.add_argument("--out", type=Path)
    p.set_defaults(func=_cmd_rehearsal)

    p = sub.add_parser("release", help="resolve a live release's commits from a rehearsal record")
    p.add_argument("--records-dir", type=Path, required=True)
    p.add_argument("--rehearsal-run-id", default="")
    p.add_argument("--commit-shas", default="", help="optional JSON manifest {library: sha}")
    p.add_argument("--out", type=Path)
    p.set_defaults(func=_cmd_release)

    p = sub.add_parser("verify", help="assert a checkout is the rehearsed commit; report main drift")
    p.add_argument("--repo-dir", type=Path, required=True)
    p.add_argument("--expected", required=True)
    p.add_argument("--main-ref", default="origin/main")
    p.set_defaults(func=_cmd_verify)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        return args.func(args)
    except Refused as exc:
        print(f"::error::REFUSED — {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
