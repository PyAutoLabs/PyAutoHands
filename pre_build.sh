#!/bin/bash
# Pre-build script: validate a clean PyAutoHands main, then run black + generate
# notebooks + git commit & push for all workspace repos before triggering the
# GitHub Actions release workflow.
#
# Usage: bash pre_build.sh [minor_version]
#   minor_version  Minor version suffix (default: 1)
#
# pre_build always dispatches a full real release. To build + publish to
# TestPyPI without releasing (e.g. the Heart/Brain validation gate), dispatch
# release.yml directly with rehearsal=true instead.

set -e

MINOR_VERSION="${1:-1}"

# Resolve PYAUTOBASE from this script's location (same idiom as bin/autohands)
# so pre_build.sh works from any checkout — Linux, WSL, anywhere.
SELF="$(readlink -f "$0")"
PYAUTOBASE="$(cd "$(dirname "$SELF")/.." && pwd)"
AUTOHANDS="$PYAUTOBASE/PyAutoHands/autohands"
PYTHONPATH_EXTRA="$AUTOHANDS"

# pre_build produces no files in PyAutoHands itself. Require a clean main before
# any labels, workspace formatting, commits, pushes, or release dispatch so a
# release can never sweep unrelated local files into a misleading commit.
HANDS_REPO="$PYAUTOBASE/PyAutoHands"
HANDS_BRANCH="$(git -C "$HANDS_REPO" branch --show-current)"
HANDS_STATUS="$(git -C "$HANDS_REPO" status --porcelain --untracked-files=all)"
if [ "$HANDS_BRANCH" != "main" ] || [ -n "$HANDS_STATUS" ]; then
    echo "ABORT: PyAutoHands must be on clean main before pre_build." >&2
    echo "  branch: ${HANDS_BRANCH:-<detached>}" >&2
    if [ -n "$HANDS_STATUS" ]; then
        printf '%s\n' "$HANDS_STATUS" >&2
    fi
    exit 1
fi

# (A `VERSION="$(date …).$MINOR_VERSION"` string used to be computed here for the
# README version-pin sed. That sed was deleted with the pin bump, and the pins
# themselves are gone — see the note above `run_workspace`'s call list. Nothing
# read VERSION afterwards, so it was removed too; `MINOR_VERSION` is still what
# the release dispatch below takes.)

# Ensure the canonical `pending-release` label exists with the right config
# across every release-window repo. Idempotent — no-ops when nothing drifted.
if command -v gh >/dev/null 2>&1; then
    echo ""
    echo "=== Ensuring pending-release labels ==="
    bash "$PYAUTOBASE/PyAutoBrain/bin/ensure_workspace_labels.sh"
fi

# Positional fields: repo project [generate=true] [slam=false]
# Declared as data, not as a call list, because TWO passes read it: the
# uncommitted-work preflight below and the execution loop at the bottom. A
# second hand-maintained list would drift out of step with this one, and the
# preflight would then silently skip a repo it is meant to protect.
# The repo names are checked against PyAutoMind/repos.yaml (the body map) by
# `repos_sync.py --check`; the flags are Build policy and live only here.
# (The former readme_pkg arg / README version bump was deleted per the audit in
# docs/pre_build_failure_audit.md: its sed edit was never staged and the runner
# side was removed under #120. Phase 4 task 4 of the build-chain campaign
# (#155) then resolved the pins themselves: the three surviving `<pkg> vX` lines
# were REMOVED from the READMEs in favour of "install the latest release" plus
# the `version.minimum_library_version` floor, which Heart's version_skew check
# actually verifies. Do not re-add a README version bump here or on the runner —
# an unowned pin is what went 2 months stale.)
# The last entry is the AI assistant repo. No notebook generation; release.yml's
# release_workspaces job stamps its workspace version and regenerates
# wiki/core/api_audit_baseline.json against the released wheels.
WORKSPACE_SPECS=(
    "autofit_workspace                    autofit      true   false"
    "autogalaxy_workspace                 autogalaxy   true   false"
    "autolens_workspace                   autolens     true   true"
    "autofit_workspace_test               autofit      false  false"
    "autogalaxy_workspace_test            autogalaxy   false  false"
    "autolens_workspace_test              autolens     false  false"
    "euclid_strong_lens_modeling_pipeline -            false  false"
    "HowToGalaxy                          howtogalaxy  true   false"
    "HowToLens                            howtolens    true   false"
    "HowToFit                             howtofit     true   false"
    "autofit_workspace_developer          -            false  false"
    "autolens_workspace_developer         -            false  false"
    "autolens_assistant                   autolens     false  false"
)

# The directories run_workspace reformats with black and stages. Anything
# untracked under them BEFORE a run is human work, never run output.
MUTATED_DIRS=(notebooks scripts slam_pipeline)

# Preflight: no workspace may carry uncommitted work under MUTATED_DIRS.
#
# run_workspace both black-formats and `git add`s those directories, and both
# operations reach untracked files — so a human's in-progress script would be
# reformatted on disk and pushed inside the "pre build" commit. That is the
# same leak class as the tracked-dataset leak (#126), which was fixed for
# dataset/ and config/ by dropping their staging; the scripts/ path still had
# the hole, and it was caught by hand during the 2026-08-07 release only
# because the operator happened to notice.
#
# This runs over EVERY repo before the first one is touched, mirroring the
# PyAutoHands gate above. run_workspace commits and pushes each repo before
# moving to the next, so a per-repo check that aborted midway would leave the
# earlier repos already published.
echo ""
echo "=== Checking workspaces for uncommitted work ==="
WIP_REPORT=""
for spec in "${WORKSPACE_SPECS[@]}"; do
    # `read` rather than `set --`: this loop runs at top level, where `set --`
    # would clobber the script's own positional parameters.
    read -r wip_repo _ <<< "$spec"
    wip_dir="$PYAUTOBASE/$wip_repo"
    # Checked here so a missing checkout fails with a clear message during the
    # preflight, rather than as a bare `cd` error partway through the run once
    # earlier repos have already been committed and pushed.
    if [ ! -d "$wip_dir/.git" ]; then
        echo "ABORT: $wip_repo is missing or is not a git repo ($wip_dir)." >&2
        exit 1
    fi
    # `ls-files --others` tolerates pathspecs that match nothing (unlike
    # `git add`), so the dirs need no per-repo existence guard here.
    # `--exclude-standard` honours .gitignore, keeping output/ and friends out.
    wip="$(git -C "$wip_dir" ls-files --others --exclude-standard -- "${MUTATED_DIRS[@]}")"
    if [ -n "$wip" ]; then
        WIP_REPORT="${WIP_REPORT}  ${wip_repo}:"$'\n'"$(printf '%s\n' "$wip" | sed 's/^/    /')"$'\n'
    fi
done
if [ -n "$WIP_REPORT" ]; then
    echo "ABORT: uncommitted work under directories pre_build formats and commits." >&2
    printf '%s' "$WIP_REPORT" >&2
    echo "Commit, stash or move these before releasing — pre_build must not author them." >&2
    exit 1
fi
echo "  Clean: no untracked files under ${MUTATED_DIRS[*]} in any workspace."

run_workspace() {
    local repo="$1"
    local project="$2"
    local generate="${3:-true}"
    local slam="${4:-false}"
    local dir="$PYAUTOBASE/$repo"

    echo ""
    echo "=== $repo ==="

    cd "$dir"

    echo "  Running black..."
    # Format only the dirs this script stages — black'ing "." reformatted files
    # no staging rule covered (13 files across HowTo*/assistant), leaving them
    # perpetually dirty-local on every release (#156).
    for d in scripts slam_pipeline; do
        if [ -d "$d" ]; then black "$d/"; fi
    done

    if [ "$generate" = "true" ]; then
        echo "  Running generate.py ($project)..."
        PYTHONPATH="$PYTHONPATH_EXTRA" python "$AUTOHANDS/generate.py" "$project"
    fi

    echo "  Checking dataset allowlist (PyAutoBuild#126 leg 4)..."
    python3 "$AUTOHANDS/check_dataset_allowlist.py" || {
        echo "  ABORT: tracked dataset/ contains non-allowlisted simulated data." >&2
        exit 1
    }

    echo "  Staging what this run produced..."
    # Stage only what the run itself modifies: black'd scripts and the
    # generated notebooks. The former dataset/ and config/ adds staged nothing
    # the run produced — they swept pre-existing human-uncommitted work into
    # release commits, which is the mechanism that leaked simulated datasets
    # (#126). Releases require clean mains (Heart gates on it); human work is
    # committed by humans. See docs/pre_build_failure_audit.md §3/§6 (#156).
    local stage_dirs=()
    for d in notebooks scripts; do
        if [ -d "$d" ]; then stage_dirs+=("$d"); fi
    done
    if [ "$slam" = "true" ] && [ -d "slam_pipeline" ]; then
        stage_dirs+=("slam_pipeline")
    fi
    if [ ${#stage_dirs[@]} -gt 0 ]; then
        # Tracked edits and deletions: black's reformatting, regenerated and
        # retired notebooks.
        git add -u -- "${stage_dirs[@]}"
        # Plus what this run CREATED — a new notebook from generate.py. The
        # preflight proved these directories held no untracked files before the
        # run, so anything untracked now is run output. Added by explicit path
        # rather than as `git add <dir>/`, which also sweeps in untracked files
        # and would re-open the hole the preflight closes.
        git ls-files --others --exclude-standard -z -- "${stage_dirs[@]}" \
            | xargs -0 --no-run-if-empty git add --
    fi
    # Root-level artifacts (llms-full.txt, workspace_index.json, README Colab
    # URLs) are produced and committed by release.yml's release_workspaces job
    # on the runner — pre_build deliberately does not stage root files. The
    # former glob line here was a measured no-op in all 13 repos (#156).

    echo "  Committing and pushing..."
    if git diff --cached --quiet; then
        echo "  No changes to commit."
    else
        git commit -m "pre build"
        git push
    fi
}

# Execute. Same list the preflight above walked — see WORKSPACE_SPECS for the
# field meanings and the policy notes.
for spec in "${WORKSPACE_SPECS[@]}"; do
    # Unquoted on purpose, as in the preflight: the fields are
    # whitespace-separated and none contains a space. A no-generate repo carries
    # `-` in the project field — word splitting cannot express an empty field,
    # and run_workspace never reads project when generate is false.
    run_workspace $spec
done

# Release readiness (version skew, including the version.txt-ahead crash that
# used to be checked here) is now Heart's job, not Build's: PyAutoHands is a
# pure executor. The release agent gates on `pyauto-heart readiness` before
# invoking this script; a human running pre_build directly is trusted to have
# checked `pyauto-heart readiness` themselves.

# Trigger the GitHub Actions release workflow
echo ""
echo "=== Triggering release workflow (minor_version=$MINOR_VERSION) ==="
gh workflow run release.yml \
    --repo PyAutoLabs/PyAutoHands \
    --field minor_version="$MINOR_VERSION"

echo ""
echo "Pre-build complete. Workflow dispatched."
echo "Track it at: https://github.com/PyAutoLabs/PyAutoHands/actions"
