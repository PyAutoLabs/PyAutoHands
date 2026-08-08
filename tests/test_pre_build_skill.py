"""Keep the pre-build skill's safety preflight aligned with its executor."""

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_pre_build_skill_checks_every_executor_repo():
    script = (ROOT / "pre_build.sh").read_text()
    body = (ROOT / "skills" / "pre_build" / "pre_build.md").read_text()
    # Repos come from the WORKSPACE_SPECS array — the single list that both the
    # uncommitted-work preflight and the execution loop read.
    executor_repos = set(
        re.findall(r'^\s+"(\S+)\s+\S+\s+\S+\s+\S+"', script, re.MULTILINE)
    )
    fixed_dependencies = set(re.findall(r'\$PYAUTOBASE/([^/"$]+)', script))
    preflight = body.split("Check that all required repositories exist", 1)[1]
    preflight = preflight.split("For each, verify", 1)[0]
    documented_repos = set(re.findall(r"^- `([^`]+)`", preflight, re.MULTILINE))

    assert documented_repos == executor_repos | fixed_dependencies


def test_pre_build_guards_pyautohands_instead_of_staging_it():
    script = (ROOT / "pre_build.sh").read_text()

    guard = 'HANDS_STATUS="$(git -C "$HANDS_REPO" status --porcelain --untracked-files=all)"'
    assert guard in script
    assert 'if [ "$HANDS_BRANCH" != "main" ] || [ -n "$HANDS_STATUS" ]' in script
    assert script.index(guard) < script.index("=== Ensuring pending-release labels ===")
    assert "git add -A" not in script


def test_pre_build_never_stages_a_directory():
    """`git add <dir>/` also stages untracked files.

    That is how a human's uncommitted script was reformatted and pushed inside
    a "pre build" commit during the 2026-08-07 release. Staging must name the
    tracked set (`git add -u`) and add created files by explicit path.
    """
    script = (ROOT / "pre_build.sh").read_text()

    assert not re.search(r"git add\s+[\"']?\$?\w+/", script)
    assert 'git add -u -- "${stage_dirs[@]}"' in script


def test_pre_build_wip_preflight_precedes_every_mutation():
    """The preflight must sweep all repos before the first is touched.

    run_workspace commits and pushes each workspace before moving to the next,
    so a per-repo check that aborted midway would leave earlier repos already
    published.
    """
    script = (ROOT / "pre_build.sh").read_text()

    preflight = script.index("=== Checking workspaces for uncommitted work ===")
    assert preflight < script.index("run_workspace() {")
    # The invocations themselves, not the words — both appear in prose above.
    assert preflight < script.index('black "$d/"')
    assert preflight < script.index("git add -u --")
    assert "ABORT: uncommitted work" in script
