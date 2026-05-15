#!/usr/bin/env bash
# url_check.sh — fast offline regex guard against known-bad URL patterns.
#
# Usage: url_check.sh [directory]
# Exits 0 if clean, 1 if any forbidden patterns are found, 2 on usage error.
#
# Runs on every PR via .github/workflows/url_check.yml in each PyAuto repo.
# For live HTTP checking with an allowlist (weekly cron), see
# url_check_live.sh and url_check_live.py.

set -u

DIR="${1:-.}"

if [ ! -d "$DIR" ]; then
  echo "url_check.sh: not a directory: $DIR" >&2
  exit 2
fi

# Each entry is "pattern|||label". `|||` keeps it grep-safe.
ENTRIES=(
  # --- original three (Binder / wrong-owner / dead-branch) ---
  'mybinder\.org|||mybinder.org URL (Binder is no longer supported — use Colab)'
  'colab\.research\.google\.com/github/Jammy2211/|||Colab URL with Jammy2211 owner (use PyAutoLabs)'
  'colab\.research\.google\.com/github/[^/]+/[^/]+/blob/release/|||Colab URL pinned to /blob/release/ (use a tagged version or /blob/main/)'

  # --- typo ---
  'hhttps://|||hhttps:// typo (should be https://)'

  # --- workspaces moved Jammy2211 → PyAutoLabs ---
  'github\.com/Jammy2211/(autolens_workspace|autogalaxy_workspace|autofit_workspace)|||Jammy2211/<workspace> (use PyAutoLabs/<workspace>)'
  'githubusercontent\.com/Jammy2211/(autolens_workspace|autogalaxy_workspace|autofit_workspace)|||Jammy2211/<workspace> in raw URL (use PyAutoLabs/<workspace>)'

  # --- libraries moved Jammy2211|rhayes777 → PyAutoLabs ---
  'github\.com/Jammy2211/(PyAutoArray|PyAutoLens|PyAutoGalaxy)|||Jammy2211/<library> (use PyAutoLabs/<library>)'
  'githubusercontent\.com/Jammy2211/(PyAutoArray|PyAutoLens|PyAutoGalaxy)|||Jammy2211/<library> in raw URL (use PyAutoLabs/<library>)'
  'github\.com/Jammy2211/(PyAutoFit|PyAutoConf)|||Jammy2211/(PyAutoFit|PyAutoConf) (use PyAutoLabs/...)'
  'github\.com/rhayes777/(PyAutoFit|PyAutoConf|PyAutoGalaxy|PyAutoBuild)|||rhayes777/<lib> (use PyAutoLabs/<lib>)'

  # --- workspace /tree/release/ — same fate as /blob/release/ ---
  'github\.com/PyAutoLabs/(autolens_workspace|autogalaxy_workspace|autofit_workspace)/tree/release/|||workspace /tree/release/ branch removed (use /tree/main/ or a tag)'

  # --- third-party renames surfaced by the audit ---
  'github\.com/joshspeagle/[Nn]autilus|||joshspeagle/nautilus moved (use github.com/johannesulf/nautilus)'
  'www\.sphinx-doc\.org/en/main|||sphinx-doc /en/main is 404 (use /en/master)'
  'github\.com/bokeh/bokeh/blob/main/CODE_OF_CONDUCT\.md|||bokeh CoC moved (use /blob/main/docs/CODE_OF_CONDUCT.md)'
  'github\.com/numfocus/numfocus/blob/main/manual/numfocus-coc\.md|||numfocus CoC moved (use numfocus.org/code-of-conduct)'
  'Fiterence_anti-harassment|||"Fiterence_anti-harassment" typo (Conference_anti-harassment)'
)

found=0
for entry in "${ENTRIES[@]}"; do
  pattern="${entry%%|||*}"
  label="${entry##*|||}"
  matches=$(grep -REn \
    --include='*.rst' --include='*.md' --include='*.ipynb' --include='*.py' \
    "$pattern" "$DIR" 2>/dev/null || true)
  if [ -n "$matches" ]; then
    found=1
    echo ""
    echo "FORBIDDEN: $label"
    echo "$matches"
  fi
done

if [ "$found" -eq 1 ]; then
  exit 1
fi
exit 0
