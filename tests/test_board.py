"""tests/test_board.py — the PyAutoHands Dashboard renderer (autohands/board.py).

Render is pure (snapshot in → string out), so everything here runs from
fixtures — no network. Fixture names are deliberately fake (SomeOrg, RepoA):
this file is not on the tenant-firewall allowlist, so no instance fact may
appear. The contract under test: every fmt renders, degraded sections say
"unavailable" rather than fabricating, failed train runs carry a copyable
/bug prompt, the html is self-contained (no external assets), and the
version scheme drives both ordering and the shipped date.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "autohands"))

import board  # noqa: E402

SNAP = {
    "schema_version": 1,
    "generated": "2026-06-03T00:00:00+00:00",
    "owner": "SomeOrg",
    "repo": "SomeHands",
    "libraries": [
        {"name": "RepoA", "package": "pkga", "version": "2026.6.1.1",
         "date": "2026-06-01", "pypi": "live",
         "tag_url": "https://github.com/SomeOrg/RepoA/releases/tag/2026.6.1.1"},
        {"name": "RepoB", "package": "pkgb", "version": "2026.6.2.1",
         "date": "2026-06-02", "pypi": "yanked",
         "tag_url": "https://github.com/SomeOrg/RepoB/releases/tag/2026.6.2.1"},
    ],
    "train": [
        {"date": "2026-06-02T03:00:00Z", "status": "completed",
         "conclusion": "success", "event": "workflow_dispatch", "attempt": 1,
         "duration_s": 800, "url": "https://ci.invalid/runs/2"},
        {"date": "2026-06-01T03:00:00Z", "status": "completed",
         "conclusion": "failure", "event": "workflow_dispatch", "attempt": 1,
         "duration_s": 3000, "url": "https://ci.invalid/runs/1"},
    ],
    "nightly": [
        {"date": "2026-06-02T02:00:00Z", "status": "completed",
         "conclusion": "success", "event": "schedule", "attempt": 1,
         "duration_s": 60, "url": "https://ci.invalid/n/2"},
    ],
    "errors": [],
}


def test_every_fmt_renders():
    for fmt in ("md", "md-brief", "html", "json", "badge"):
        out = board.render(SNAP, fmt)
        assert out and isinstance(out, str)


def test_latest_is_the_max_version_not_list_order():
    out = board.render(SNAP, "md")
    assert "**Latest release:** `2026.6.2.1`" in out


def test_shipped_date_comes_from_the_version_scheme():
    assert board.version_date("2026.6.2.1") == "2026-06-02"
    assert board.version_date("v1.15.2") is None
    assert board.version_date("pull") is None


def test_failed_train_run_carries_a_bug_prompt():
    html = board.render(SNAP, "html")
    assert "data-cmd=" in html  # the shared copy handler's payload hook
    assert "/bug Release train: SomeHands release.yml run failed on 2026-06-01" in html
    assert "https://ci.invalid/runs/1" in html
    # the action chips are present too
    for _, payload in board.ACTION_CHIPS:
        assert payload in html


def test_degraded_sections_say_unavailable_never_fabricate():
    empty = {**SNAP, "libraries": [], "train": [], "nightly": [],
             "errors": ["release runs: kaboom"]}
    md = board.render(empty, "md")
    assert "unavailable" in md and "kaboom" in md
    html = board.render(empty, "html")
    assert "unavailable this render" in html
    badge = json.loads(board.render(empty, "badge"))
    assert badge["message"] == "unknown" and badge["color"] == "lightgrey"


def test_md_brief_is_one_line_with_board_link():
    out = board.render(SNAP, "md-brief")
    assert "\n" not in out
    assert "📦 **2026.6.2.1**" in out
    assert "https://someorg.github.io/SomeHands/" in out


def test_badge_shape():
    badge = json.loads(board.render(SNAP, "badge"))
    assert badge == {"schemaVersion": 1, "label": "released",
                     "message": badge["message"], "color": "blue"}
    assert badge["message"].startswith("2026.6.2.1")


def test_html_is_self_contained():
    out = board.render(SNAP, "html")
    assert out.lstrip().startswith("<!doctype html>")
    # The header links the markdown twin and the repository front door.
    assert '<a href="dashboard.md">markdown version</a>' in out
    assert ('<a href="https://github.com/SomeOrg/SomeHands/blob/main/'
            'README.md">GitHub Page</a>') in out
    # No external ASSETS: no src=, no <link>, no fetches; inline <script> is
    # the clipboard buttons; every URL sits in an href (same contract the
    # Heart board pins).
    assert "src=" not in out and "<link" not in out.lower()
    assert "fetch(" not in out and "XMLHttpRequest" not in out
    # data-copy payloads are inert clipboard text, not asset loads — strip
    # them, then every remaining URL must sit in an href.
    stripped = re.sub(r'data-cmd="[^"]*"', "", out)
    for m in re.finditer(r"(?:http|https)://", stripped):
        before = stripped[max(0, m.start() - 30):m.start()]
        assert 'href="' in before or "href='" in before, f"non-href URL at {m.start()}"


def test_owner_repo_parses_https_and_ssh():
    assert board.parse_owner_repo("https://github.com/SomeOrg/SomeHands.git") == \
        ("SomeOrg", "SomeHands")
    assert board.parse_owner_repo("git@github.com:SomeOrg/SomeHands.git") == \
        ("SomeOrg", "SomeHands")
    assert board.parse_owner_repo("") == ("", "")


def test_boundary_language_links_the_heart():
    md = board.render(SNAP, "md")
    html = board.render(SNAP, "html")
    for out in (md, html):
        assert "Heart" in out  # readiness explicitly deferred to the Heart
    assert "https://someorg.github.io/PyAutoHeart/" in html


def test_html_wears_the_shared_family_theme():
    # The look is the Brain's `board/_theme.py`, not a stylesheet copied in
    # here: the page must carry this board's hero (mark, wordmark, tagline)
    # and its accent, or it has silently fallen out of the family.
    t = board.theme()
    html = board.render(SNAP, "html")
    assert t.MARKS[board.BOARD_KEY] in html
    assert t.ORGANS[board.BOARD_KEY]["tagline"] in html
    assert t.ORGANS[board.BOARD_KEY]["ink_dark"] in html
    assert "#58a6ff" not in html  # the old hard-coded GitHub blue
