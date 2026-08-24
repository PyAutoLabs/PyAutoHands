"""autohands/board.py — the PyAutoHands Dashboard.

A phone-readable record of **what the Hands shipped**: the released library
versions (from git tags — the authoritative record; version stamps are
build-tree-only and never committed), their PyPI liveness, the release train's
recent runs, and the nightly driver's outcomes. Every actionable item carries
a one-tap 📋 copy block holding the Claude Code command that drives it
(``/release``, ``/release rehearse``, ``/release validate``, ``/build``; a
failed train run copies a ``/bug`` prompt with its run URL).

**Boundary.** Hands is a pure executor, so this board is a *past-tense record
of execution* — never a verdict, a score, or a gate. "Is it safe to release?"
lives with the Heart, whose board this page links.

**Shape.** ``collect()`` is the only I/O (GitHub REST via ``gh api`` + the
PyPI JSON API) and degrades per-section: a source that cannot be fetched
renders as "unavailable", never as fabricated data. ``render(snapshot, fmt)``
is pure — ``fmt = md | md-brief | html | json | badge`` — mirroring the
Heart's ``dashboard.py`` (one renderer, many surfaces). The GitHub owner is
derived from ``git remote`` and the library set from
``config/workspaces.yaml`` — organ code carries no instance facts (the
tenant firewall).

Published by ``.github/workflows/release_board.yml``: the Pages page +
``badge.json`` after every "PyAuto Release" run and daily, plus the README
strip between the ``hands:begin/end`` markers.

Usage:
    python -m autohands.board --collect snapshot.json   # gather, write, exit
    python -m autohands.board [--snapshot F] --md|--md-brief|--html|--json|--badge
"""

from __future__ import annotations

import datetime
import html as _html
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

HANDS_HOME = Path(__file__).resolve().parents[1]

# The family look lives once, in the Brain (``board/_theme.py``): the
# stylesheet, the hero that redraws this organ's logo as a mark, and the
# cross-board footer. Imported rather than copied, so the look moves for the
# whole family at once — release_board.yml checks PyAutoBrain out beside this
# repo, and a local run finds the sibling checkout the way the other PyAuto
# tools resolve each other.
BOARD_KEY = "hands"  # this board's entry in the Brain's palette table


def _workspace_root() -> Path:
    """Where the sibling PyAuto checkouts live: `$PYAUTO_ROOT`, else `~/Code`.

    The org's own directory name is an instance fact, so it is never written
    here — a workspace that does not follow the default sets `$PYAUTO_ROOT`
    (the same variable the dev-flow doors read).
    """
    return Path(os.environ.get("PYAUTO_ROOT") or Path.home() / "Code")


def theme():
    """The shared theme module, or a RuntimeError naming the fix.

    Only the html path needs it; ``--md``/``--badge``/``--json`` never call
    here, so the digest keeps working with no PyAutoBrain in reach.
    """
    for cand in (os.environ.get("PYAUTO_BRAIN"), HANDS_HOME / "PyAutoBrain",
                 HANDS_HOME.parent / "PyAutoBrain",
                 _workspace_root() / "PyAutoBrain"):
        if not cand:
            continue
        board = Path(cand) / "board"
        if (board / "_theme.py").is_file():
            if str(board) not in sys.path:
                sys.path.insert(0, str(board))
            import _theme
            return _theme
    raise RuntimeError(
        "the shared board theme (PyAutoBrain/board/_theme.py) is not in reach "
        "— check PyAutoBrain out beside this repo or set PYAUTO_BRAIN")
CONFIG_PATH = Path(__file__).resolve().parent / "config" / "workspaces.yaml"

SCHEMA_VERSION = 1
TRAIN_RUNS_SHOWN = 14
NIGHTLY_RUNS_SHOWN = 10

# The one-tap chips: the Claude Code doors that drive the Hands. Payload is
# what 📋 copies into the clipboard, ready to paste into a Claude chat.
ACTION_CHIPS = (
    ("release", "/release"),
    ("rehearse", "/release rehearse"),
    ("validate", "/release validate"),
    ("build", "/build"),
)


# --- identity (derived, never hardcoded — tenant firewall) -------------------
def _owner_repo() -> tuple[str, str]:
    """(owner, repo) from this checkout's origin URL (https or ssh)."""
    out = subprocess.run(
        ["git", "-C", str(HANDS_HOME), "remote", "get-url", "origin"],
        capture_output=True, text=True,
    ).stdout.strip()
    return parse_owner_repo(out)


def parse_owner_repo(url: str) -> tuple[str, str]:
    m = re.search(r"[:/]([^/:]+)/([^/]+?)(?:\.git)?/?$", url)
    if not m:
        return "", ""
    return m.group(1), m.group(2)


def _libraries() -> list[dict]:
    """The released library set from the declared config surface."""
    import yaml

    cfg = yaml.safe_load(CONFIG_PATH.read_text()) or {}
    libs = cfg.get("libraries") or []
    return [
        {"name": str(l["name"]), "package": str(l["package"])}
        for l in libs
        if isinstance(l, dict) and l.get("name") and l.get("package")
    ]


# --- collect (the only I/O) ---------------------------------------------------
def _gh_api(path: str) -> object:
    res = subprocess.run(["gh", "api", path], capture_output=True, text=True,
                         timeout=60)
    if res.returncode != 0:
        raise RuntimeError(res.stderr.strip().splitlines()[-1] if res.stderr else "gh api failed")
    return json.loads(res.stdout)


def _pypi_status(package: str, version: str) -> str:
    """'live' | 'yanked' | 'missing' for one released version on PyPI."""
    try:
        with urllib.request.urlopen(
            f"https://pypi.org/pypi/{package}/json", timeout=30
        ) as resp:
            data = json.load(resp)
    except (urllib.error.URLError, TimeoutError, ValueError) as e:
        raise RuntimeError(f"pypi {package}: {e}") from e
    files = (data.get("releases") or {}).get(version)
    if not files:
        return "missing"
    if all(f.get("yanked") for f in files):
        return "yanked"
    return "live"


# The release version scheme: YYYY.M.D.minor (+ optional .attempt). The tags
# API is NOT date-ordered, and the tagged commit's date is the last commit
# before the release, not the release itself — the version string is the
# authoritative ship date, so both come from parsing it.
_VERSION_RE = re.compile(r"^(\d{4})\.(\d{1,2})\.(\d{1,2})\.(\d+)(?:\.(\d+))?$")


def _version_key(tag_name: str) -> tuple | None:
    m = _VERSION_RE.match(tag_name)
    if not m:
        return None
    return tuple(int(g) if g else 0 for g in m.groups())


def version_date(version: str) -> str | None:
    """The ship date a YYYY.M.D.* version encodes, as ISO, else None."""
    key = _version_key(version)
    if not key:
        return None
    try:
        return datetime.date(key[0], key[1], key[2]).isoformat()
    except ValueError:
        return None


def _collect_library(owner: str, lib: dict) -> dict:
    name, package = lib["name"], lib["package"]
    entry = {"name": name, "package": package, "version": None, "date": None,
             "pypi": "unavailable", "tag_url": None}
    tags = _gh_api(f"repos/{owner}/{name}/tags?per_page=100")
    versioned = [(k, str(t["name"])) for t in tags or []
                 if (k := _version_key(str(t.get("name") or ""))) is not None]
    if not versioned:
        return entry
    _, version = max(versioned)
    entry["version"] = version
    entry["date"] = version_date(version)
    entry["tag_url"] = f"https://github.com/{owner}/{name}/releases/tag/{version}"
    try:
        entry["pypi"] = _pypi_status(package, version)
    except RuntimeError:
        entry["pypi"] = "unavailable"
    return entry


def _collect_runs(owner: str, repo: str, workflow: str, limit: int) -> list[dict]:
    data = _gh_api(
        f"repos/{owner}/{repo}/actions/workflows/{workflow}/runs?per_page={limit}"
    )
    runs = []
    for r in data.get("workflow_runs") or []:
        created = str(r.get("created_at") or "")
        updated = str(r.get("updated_at") or "")
        # run_started_at restarts on re-attempts, so the duration stays the
        # attempt's own, not created→updated across a multi-day gap.
        started = str(r.get("run_started_at") or created)
        duration = None
        t0, t1 = _parse_ts(started), _parse_ts(updated)
        if t0 and t1:
            duration = int((t1 - t0).total_seconds())
        runs.append({
            "date": created,
            "status": str(r.get("status") or ""),
            "conclusion": str(r.get("conclusion") or ""),
            "event": str(r.get("event") or ""),
            "attempt": int(r.get("run_attempt") or 1),
            "duration_s": duration,
            "url": str(r.get("html_url") or ""),
        })
    return runs


def collect() -> dict:
    """Gather the snapshot. Degrades per-section; never raises."""
    owner, repo = _owner_repo()
    snapshot: dict = {
        "schema_version": SCHEMA_VERSION,
        "generated": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "owner": owner,
        "repo": repo,
        "libraries": [],
        "train": [],
        "nightly": [],
        "errors": [],
    }
    if not owner:
        snapshot["errors"].append("could not derive owner from git remote")
        return snapshot
    for lib in _libraries():
        try:
            snapshot["libraries"].append(_collect_library(owner, lib))
        except (RuntimeError, ValueError, KeyError) as e:
            snapshot["errors"].append(f"library {lib['name']}: {e}")
    try:
        snapshot["train"] = _collect_runs(owner, repo, "release.yml",
                                          TRAIN_RUNS_SHOWN)
    except (RuntimeError, ValueError) as e:
        snapshot["errors"].append(f"release runs: {e}")
    try:
        snapshot["nightly"] = _collect_runs(owner, "PyAutoBrain",
                                            "nightly-release.yml",
                                            NIGHTLY_RUNS_SHOWN)
    except (RuntimeError, ValueError) as e:
        snapshot["errors"].append(f"nightly runs: {e}")
    return snapshot


# --- pure helpers -------------------------------------------------------------
def _parse_ts(ts: object) -> datetime.datetime | None:
    try:
        t = datetime.datetime.fromisoformat(str(ts).replace("Z", "+00:00"))
    except (TypeError, ValueError):
        return None
    return t.replace(tzinfo=datetime.timezone.utc) if t.tzinfo is None else t


def _age(ts: object, now: datetime.datetime | None = None) -> str:
    t = _parse_ts(ts)
    if t is None:
        return "unknown"
    ref = now or datetime.datetime.now(datetime.timezone.utc)
    s = (ref - t).total_seconds()
    if s < 3600:
        return f"{max(0, int(s // 60))}m ago"
    if s < 86400:
        return f"{int(s // 3600)}h ago"
    return f"{int(s // 86400)}d ago"


def _day(ts: object) -> str:
    t = _parse_ts(ts)
    return t.strftime("%Y-%m-%d") if t else "?"


def _dur(seconds: object) -> str:
    if not isinstance(seconds, int) or seconds < 0:
        return "?"
    return f"{seconds // 60}m{seconds % 60:02d}s"


def pages_url(snapshot: dict) -> str:
    owner = str(snapshot.get("owner") or "").lower()
    repo = snapshot.get("repo") or ""
    return f"https://{owner}.github.io/{repo}/" if owner and repo else ""


def _heart_board_url(snapshot: dict) -> str:
    owner = str(snapshot.get("owner") or "").lower()
    return f"https://{owner}.github.io/PyAutoHeart/" if owner else ""


# The one-tap board family — the cross-board footer nav every board carries,
# each board skipping its own entry. Owner comes from the snapshot, so no
# instance name lives here beyond the family's repo identities.
BOARD_FAMILY = (("mind", "PyAutoMind"), ("brain", "PyAutoBrain"),
                ("heart", "PyAutoHeart"), ("memory", "PyAutoMemory"),
                ("organism", "PyAutoScientist"))


def _boards_nav(snapshot: dict) -> str:
    """The cross-board footer — one chip per sibling, each in its own organ's
    colour (the theme owns the chip palette; this board owns the URLs)."""
    owner = str(snapshot.get("owner") or "").lower()
    if not owner:
        return ""
    links = {key: f"https://{owner}.github.io/{repo}/"
             for key, repo in BOARD_FAMILY}
    return theme().boards_footer(links, BOARD_KEY)


def _latest(snapshot: dict) -> dict | None:
    """The headline: the newest released version across the library set."""
    libs = [(k, i, l) for i, l in enumerate(snapshot.get("libraries") or [])
            if (k := _version_key(str(l.get("version") or ""))) is not None]
    if not libs:
        return None
    return max(libs)[2]


def _last_train(snapshot: dict) -> dict | None:
    for r in snapshot.get("train") or []:
        if r.get("status") == "completed":
            return r
    return None


def _bug_prompt(snapshot: dict, run: dict) -> str:
    return (f"/bug Release train: {snapshot.get('repo') or 'release'} "
            f"release.yml run failed on {_day(run.get('date'))} — {run.get('url')}")


# --- renderers ----------------------------------------------------------------
def _render_md(snapshot: dict) -> str:
    lines = ["# PyAutoHands Dashboard", "",
             "_What the Hands shipped — a record of execution. Whether it is "
             "safe to release lives with the Heart._", ""]
    latest = _latest(snapshot)
    if latest:
        lines.append(f"**Latest release:** `{latest['version']}` "
                     f"({_day(latest.get('date'))}, {_age(latest.get('date'))})")
    else:
        lines.append("**Latest release:** unavailable")
    lines.append("")
    lines += ["| Library | Version | Shipped | PyPI |", "|---|---|---|---|"]
    for l in snapshot.get("libraries") or []:
        ver = f"[{l['version']}]({l['tag_url']})" if l.get("tag_url") else (l.get("version") or "?")
        lines.append(f"| {l['name']} | {ver} | {_day(l.get('date'))} | {l.get('pypi', '?')} |")
    if not snapshot.get("libraries"):
        lines.append("| _(library data unavailable)_ | | | |")
    lines += ["", "## Release train", ""]
    for r in (snapshot.get("train") or [])[:TRAIN_RUNS_SHOWN]:
        mark = ("✓" if r.get("conclusion") == "success"
                else "✗" if r.get("conclusion") else "…")
        lines.append(f"- {mark} [{_day(r.get('date'))}]({r.get('url')}) "
                     f"{r.get('conclusion') or r.get('status')} ({_dur(r.get('duration_s'))})")
    if not snapshot.get("train"):
        lines.append("- _(run history unavailable)_")
    if snapshot.get("errors"):
        lines += ["", "_Sections unavailable this render: "
                  + "; ".join(snapshot["errors"]) + "_"]
    url = pages_url(snapshot)
    if url:
        lines += ["", f"[Dashboard]({url}) · [PyAutoHeart Dashboard]({_heart_board_url(snapshot)})"]
    return "\n".join(lines)


def _render_md_brief(snapshot: dict) -> str:
    """The README strip: one line, no heading (the README supplies it)."""
    latest = _latest(snapshot)
    last = _last_train(snapshot)
    bits = []
    if latest:
        bits.append(f"📦 **{latest['version']}** · shipped {_day(latest.get('date'))} "
                    f"({_age(latest.get('date'))})")
    else:
        bits.append("📦 latest release unavailable")
    if last:
        mark = "✓" if last.get("conclusion") == "success" else "✗"
        bits.append(f"last train run {mark} [{_day(last.get('date'))}]({last.get('url')})")
    url = pages_url(snapshot)
    if url:
        bits.append(f"[dashboard →]({url})")
    return " · ".join(bits)


def _copy_btn(payload: str, label: str = "copy") -> str:
    """A one-tap payload chip. The behaviour is the family's shared script
    (``_theme.JS``): a delegated click handler reading ``data-cmd``."""
    return (f"<button class='copy' type='button' "
            f"title='{_html.escape(label, quote=True)}' "
            f"data-cmd=\"{_html.escape(payload, quote=True)}\">\U0001f4cb</button>")


_PYPI_CLS = {"live": "ok", "yanked": "fail", "missing": "warn", "unavailable": "unobs"}


# The lede, and the page-specific shapes the shared sheet has no opinion on:
# the status dot each row carries and the version chips. Written against the
# theme's variables, so this board follows the family accent rather than
# setting a second palette.
_LEDE = ("What the Hands shipped — a record of execution, newest first. Tap "
         "\U0001f4cb to put a command on your clipboard for a Claude Code chat.")

_EXTRA_CSS = """
.chip{display:inline-block;background:var(--btn);border:1px solid var(--line);
 border-radius:999px;padding:.15rem .6rem;margin:.15rem .2rem 0 0;
 font-size:.85rem;white-space:nowrap}
table.recent td.dot{width:10px;padding-right:0}
table.recent td.dot::before{content:"";display:inline-block;width:10px;
 height:10px;border-radius:50%;margin-top:.35rem;background:var(--muted)}
tr.ok td.dot::before{background:var(--ok)}
tr.warn td.dot::before{background:var(--warn)}
tr.fail td.dot::before{background:var(--bad)}
table.recent td.name{font-weight:600;white-space:nowrap}
.ndot{display:inline-block;width:12px;height:12px;border-radius:50%;
 margin-right:.25rem;background:var(--muted)}
.ndot.ok{background:var(--ok)}
.ndot.fail{background:var(--bad)}
.errors{margin-top:1.2rem}
footer{margin-top:2rem;color:var(--muted);font-size:.82em}
"""


def _render_html(snapshot: dict) -> str:
    t_ = theme()
    latest = _latest(snapshot)
    head = (f"{_html.escape(latest['version'])}" if latest else "unavailable")
    head_age = _age(latest.get("date")) if latest else ""
    chips = " ".join(
        f"<span class='chip'>{_html.escape(label)} {_copy_btn(payload, f'copy {payload}')}</span>"
        for label, payload in ACTION_CHIPS
    )
    lib_rows = []
    for l in snapshot.get("libraries") or []:
        cls = _PYPI_CLS.get(str(l.get("pypi")), "unobs")
        ver = (f"<a href=\"{_html.escape(str(l.get('tag_url')), quote=True)}\">"
               f"{_html.escape(str(l.get('version')))}</a>"
               if l.get("tag_url") else "?")
        lib_rows.append(
            f"<tr class='{cls}'><td class='dot'></td>"
            f"<td class='name'>{_html.escape(l['name'])}</td>"
            f"<td>{ver}</td><td>{_day(l.get('date'))}</td>"
            f"<td>{_html.escape(str(l.get('pypi')))}</td></tr>"
        )
    if not lib_rows:
        lib_rows.append("<tr class='unobs'><td class='dot'></td>"
                        "<td class='name'>libraries</td>"
                        "<td colspan='3'>unavailable this render</td></tr>")
    train_rows = []
    for r in (snapshot.get("train") or [])[:TRAIN_RUNS_SHOWN]:
        ok = r.get("conclusion") == "success"
        cls = "ok" if ok else ("unobs" if not r.get("conclusion") else "fail")
        cell = (f"<a href=\"{_html.escape(str(r.get('url')), quote=True)}\">"
                f"{_day(r.get('date'))}</a> {_html.escape(r.get('conclusion') or r.get('status') or '?')}"
                f" <span class='meta'>({_dur(r.get('duration_s'))})</span>")
        if not ok and r.get("conclusion"):
            cell += " " + _copy_btn(_bug_prompt(snapshot, r),
                                    "copy a fix prompt for a Claude Code chat")
        train_rows.append(f"<tr class='{cls}'><td class='dot'></td>"
                          f"<td colspan='4'>{cell}</td></tr>")
    if not train_rows:
        train_rows.append("<tr class='unobs'><td class='dot'></td>"
                          "<td colspan='4'>run history unavailable this render</td></tr>")
    nightly = ""
    if snapshot.get("nightly"):
        dots = " ".join(
            f"<a class='ndot {('ok' if n.get('conclusion') == 'success' else 'fail')}' "
            f"href=\"{_html.escape(str(n.get('url')), quote=True)}\" "
            f"title='{_day(n.get('date'))}'></a>"
            for n in snapshot["nightly"][:NIGHTLY_RUNS_SHOWN]
        )
        nightly = (f"<p class='meta'>nightly driver, newest first: "
                   f"<span class='strip'>{dots}</span></p>")
    errors = ""
    if snapshot.get("errors"):
        items = "".join(f"<li>{_html.escape(e)}</li>" for e in snapshot["errors"])
        errors = (f"<div class='errors'><p class='meta'>unavailable this "
                  f"render:</p><ul class='meta'>{items}</ul></div>")
    heart = _heart_board_url(snapshot)
    hero = t_.hero(BOARD_KEY, "Dashboard", _LEDE)
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>PyAutoHands Dashboard</title>
<style>{t_.css(BOARD_KEY)}{_EXTRA_CSS}</style>
</head>
<body>
{hero}
<p class="verdict"><b>{head}</b><span class="muted">{head_age}</span></p>
<p class="muted">Whether it is <em>safe</em> to release lives with the
<a href="{heart}">PyAutoHeart Dashboard</a> — the Hands execute, never gate.
<a href="dashboard.md">markdown version</a></p>
<p>{chips}</p>
<h2>Libraries</h2>
<table class="recent">{''.join(lib_rows)}</table>
<h2>Release train</h2>
<table class="recent">{''.join(train_rows)}</table>
{nightly}
{errors}
{_boards_nav(snapshot)}
<footer>Rendered by <code>autohands/board.py</code> from the GitHub + PyPI
APIs · generated {_html.escape(str(snapshot.get('generated') or '?'))}.</footer>
<script>{t_.JS}</script>
</body></html>
"""


def badge_endpoint(snapshot: dict) -> dict:
    latest = _latest(snapshot)
    if not latest:
        return {"schemaVersion": 1, "label": "released",
                "message": "unknown", "color": "lightgrey"}
    return {"schemaVersion": 1, "label": "released",
            "message": f"{latest['version']} · {_age(latest.get('date'))}",
            "color": "blue"}


def render(snapshot: dict, fmt: str = "md") -> str:
    if fmt == "md":
        return _render_md(snapshot)
    if fmt == "md-brief":
        return _render_md_brief(snapshot)
    if fmt == "html":
        return _render_html(snapshot)
    if fmt == "json":
        return json.dumps({**snapshot, "pages_url": pages_url(snapshot)},
                          indent=2, sort_keys=True)
    if fmt == "badge":
        return json.dumps(badge_endpoint(snapshot))
    raise ValueError(f"unknown board fmt: {fmt!r}")


# --- CLI ----------------------------------------------------------------------
def main(argv: list[str] | None = None) -> int:
    import argparse

    ap = argparse.ArgumentParser(prog="autohands board", description=__doc__)
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--md", action="store_true", help="markdown board (default)")
    g.add_argument("--md-brief", action="store_true", help="the README strip")
    g.add_argument("--html", action="store_true", help="the Pages page")
    g.add_argument("--json", action="store_true", help="the machine surface")
    g.add_argument("--badge", action="store_true", help="shields.io endpoint JSON")
    ap.add_argument("--collect", metavar="OUT", default=None,
                    help="collect a snapshot to OUT (json) and exit")
    ap.add_argument("--snapshot", metavar="F", default=None,
                    help="render from a previously collected snapshot file")
    ns = ap.parse_args(argv)

    if ns.collect:
        snap = collect()
        Path(ns.collect).write_text(json.dumps(snap, indent=2, sort_keys=True) + "\n")
        print(f"collected → {ns.collect} ({len(snap['libraries'])} libraries, "
              f"{len(snap['train'])} train runs, {len(snap['errors'])} error(s))",
              file=sys.stderr)
        return 0

    snap = (json.loads(Path(ns.snapshot).read_text()) if ns.snapshot else collect())
    fmt = "md"
    for name, label in (("md", "md"), ("md_brief", "md-brief"),
                        ("html", "html"), ("json", "json"), ("badge", "badge")):
        if getattr(ns, name):
            fmt = label
            break
    print(render(snap, fmt))
    return 0


if __name__ == "__main__":
    sys.exit(main())
