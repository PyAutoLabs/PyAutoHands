#!/usr/bin/env bash
# url_check_live.sh — run the live HTTP URL audit against a single PyAuto repo.
#
# Usage: bash url_check_live.sh <repo-dir>
#
# Looks for `.url_check_allowlist.txt` at the repo root. URLs listed there are
# grandfathered (broken but accepted). Exits 0 if every broken URL is in the
# allowlist; exits 1 (and writes a GitHub-issue-ready Markdown body to stdout)
# if any non-allowlisted URL is broken.
#
# Designed for use from a CI workflow:
#
#   - name: Run live URL audit
#     id: url_audit
#     run: |
#       body=$(bash PyAutoBuild/autobuild/url_check_live.sh repo) && rc=0 || rc=$?
#       echo "$body" > /tmp/url_audit_body.md
#       echo "rc=$rc" >> "$GITHUB_OUTPUT"

set -u

REPO="${1:-}"
if [ -z "$REPO" ] || [ ! -d "$REPO" ]; then
  echo "url_check_live.sh: not a directory: $REPO" >&2
  exit 2
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ABS="$(cd "$REPO" && pwd)"

ALLOWLIST="$REPO_ABS/.url_check_allowlist.txt"
ALLOW_ARG=()
if [ -f "$ALLOWLIST" ]; then
  ALLOW_ARG=(--allowlist "$ALLOWLIST")
fi

# Run from inside the target repo so cwd-based scan picks up the right files.
cd "$REPO_ABS"
exec python3 "$SCRIPT_DIR/url_check_live.py" \
  --strict \
  --format markdown-issue \
  "${ALLOW_ARG[@]}" \
  --repos .
