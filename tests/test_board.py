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

import datetime
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


# The canonical board family, in the order `PyAutoBrain/config/policy.yaml`
# declares it. This board is `hands`, so its own chip never appears.
FAMILY_WITHOUT_HANDS = ["brain", "mind", "cortex", "memory", "heart", "organism"]


def _footer(html: str) -> str:
    return re.search(r'<ul class="boards">.*?</ul>', html, re.S).group(0)


def test_the_family_footer_carries_the_cortex_in_the_canonical_order():
    """The footer's membership is the Brain's config, not a tuple in here.

    It used to be a tuple in here — written before the Cortex had a board —
    so this page linked five siblings in an ad-hoc order and silently missed
    the sixth. Reading `_theme.board_links` means adding a board to
    `config/policy.yaml` lights it in every footer at once.
    """
    footer = _footer(board.render(SNAP, "html"))
    assert re.findall(r'data-organ="(\w+)"', footer) == FAMILY_WITHOUT_HANDS
    assert "https://someorg.github.io/PyAutoCortex/" in footer


def test_the_footer_never_links_the_page_it_is_on():
    footer = _footer(board.render(SNAP, "html"))
    assert f'data-organ="{board.BOARD_KEY}"' not in footer


def test_the_footer_falls_back_when_the_brain_checkout_predates_the_helper():
    """An older PyAutoBrain beside this repo has no `board_links`. The page
    must still render its footer — from the legacy tuple — rather than lose
    the whole board over a nav strip."""
    class _Older:
        def __init__(self, real):
            self.boards_footer = real.boards_footer

    real = board.theme()
    saved = board._boards_nav.__globals__["theme"]
    board._boards_nav.__globals__["theme"] = lambda: _Older(real)
    try:
        footer = board._boards_nav(SNAP)
    finally:
        board._boards_nav.__globals__["theme"] = saved
    assert re.findall(r'data-organ="(\w+)"', footer) == [
        k for k, _ in board.BOARD_FAMILY]


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


# --- the organ-cockpit feed (state.json, contract v1) -------------------------
# The contract is owned by the Brain's board/_state.py; these tests copy its
# required-key / enum checks instead of importing it, so the Hands suite needs
# no sibling checkout (release_board.yml runs the real validator in CI).
_STATE_REQUIRED = ("schema_version", "organ", "repo", "status", "headline",
                   "updated", "pages_url", "items")
_STATE_STATUSES = ("green", "yellow", "red", "stale", "grey")
_STATE_SEVERITIES = ("red", "yellow", "info")


def _assert_state_shape(state: dict) -> None:
    assert all(k in state for k in _STATE_REQUIRED), state
    assert state["schema_version"] == 1 and state["organ"] == "hands"
    assert state["status"] in _STATE_STATUSES
    assert state["headline"].strip() and "\n" not in state["headline"]
    assert state["pages_url"].strip()
    for item in state["items"]:
        assert item["severity"] in _STATE_SEVERITIES
        assert item["text"].strip() and len(item["text"]) <= 160


def _snap(**over) -> dict:
    return {**json.loads(json.dumps(SNAP)), **over}


def _run(status="completed", conclusion="success", url="https://ci.invalid/r"):
    return {"date": "2026-06-02T03:00:00Z", "status": status,
            "conclusion": conclusion, "event": "workflow_dispatch",
            "attempt": 1, "duration_s": 60, "url": url}


def test_state_carries_the_contract_keys():
    state = board.to_state(SNAP)
    _assert_state_shape(state)
    assert state["repo"] == "SomeHands"
    assert state["pages_url"] == "https://someorg.github.io/SomeHands/"


def test_state_green_when_the_latest_runs_succeeded():
    # the older failed train run was superseded by a success: not actionable
    state = board.to_state(SNAP)
    assert state["status"] == "green"
    assert state["items"] == []
    assert state["headline"].startswith("2026.6.2.1 · ")


def test_state_updated_is_whole_second_utc_z():
    for generated in ("2026-06-03T00:00:00.123456+00:00", "2026-06-03T00:00:00",
                      "not a timestamp", None):
        updated = board.to_state(_snap(generated=generated))["updated"]
        assert updated.endswith("Z") and "." not in updated
        datetime.datetime.fromisoformat(updated[:-1] + "+00:00")
    assert board.to_state(SNAP)["updated"] == "2026-06-03T00:00:00Z"


def test_state_failed_train_run_is_red_with_url_and_prompt():
    snap = _snap(train=[_run(conclusion="failure", url="https://ci.invalid/runs/9")])
    state = board.to_state(snap)
    _assert_state_shape(state)
    assert state["status"] == "red"
    assert state["headline"].startswith("RED — release failed · 2026.6.2.1")
    red = [i for i in state["items"] if i["severity"] == "red"]
    assert red[0]["url"] == "https://ci.invalid/runs/9"
    assert red[0]["prompt"].startswith("/bug Release train: SomeHands release.yml")
    assert "https://ci.invalid/runs/9" in red[0]["prompt"]


def test_state_failed_nightly_run_is_red():
    snap = _snap(nightly=[_run(conclusion="failure", url="https://ci.invalid/n/9")])
    state = board.to_state(snap)
    assert state["status"] == "red"
    item = state["items"][0]
    assert item["severity"] == "red" and item["url"] == "https://ci.invalid/n/9"
    assert "nightly-release.yml" in item["prompt"]


def test_state_in_progress_train_run_is_yellow():
    snap = _snap(train=[_run(status="in_progress", conclusion="",
                             url="https://ci.invalid/runs/10")] + SNAP["train"])
    state = board.to_state(snap)
    assert state["status"] == "yellow"
    assert state["headline"].startswith("YELLOW — release in progress")
    assert state["items"] == [{"severity": "yellow",
                               "text": "release train in_progress since 2026-06-02",
                               "url": "https://ci.invalid/runs/10", "prompt": None}]


def test_state_errors_are_info_items_and_yellow():
    state = board.to_state(_snap(errors=["nightly runs: boom", "x" * 400]))
    _assert_state_shape(state)
    assert state["status"] == "yellow"
    assert [i["severity"] for i in state["items"]] == ["info", "info"]
    assert all(i["url"] is None for i in state["items"])
    assert len(state["items"][1]["text"]) == 160


def test_state_empty_snapshot_is_grey_never_green():
    for snap in ({}, _snap(libraries=[])):
        state = board.to_state(snap)
        _assert_state_shape(state)
        assert state["status"] == "grey"


def test_state_render_is_valid_json():
    for snap in (SNAP, {}):
        _assert_state_shape(json.loads(board.render(snap, "state")))
