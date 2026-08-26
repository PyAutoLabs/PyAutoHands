#!/usr/bin/env bash
# GENERATED — canonical source: PyAutoMind/policy/session_start_hook.sh
# Installed into every checked-out repo as .claude/hooks/session-start.sh by
# `python3 PyAutoMind/scripts/repos_sync.py --write`, and drift-checked by
# `--check`. Edit the canonical file, never a copy.
#
# ---------------------------------------------------------------------------
# Python 3.12 is the default in Claude Code web/mobile sessions.
#
# The remote container ships /usr/local/bin/python{,3} -> /usr/bin/python3.11,
# a pip whose shebang is #!/usr/bin/python3, and a uv-managed tool set (pytest,
# ruff, black, mypy, pyright, flake8, poetry) every one of which was built on
# 3.11 — one minor version below the floor the organism set for itself in the
# Python 3.12 floor campaign, and below every CI leg it runs. The image's own
# `use-python 3.12` does not fix it: it moves the update-alternatives links
# under /usr/bin, which /usr/local/bin/python{,3} then shadow.
#
# This hook makes a session 3.12 on three surfaces:
#
#   1. a 3.12 virtualenv first on PATH — python, python3, pip, pytest;
#   2. the /usr/local/bin/python{,3} symlinks repointed at 3.12, so anything
#      resolving PATH without this session's env (a subprocess with a scrubbed
#      environment, a `#!/usr/bin/env python3` script) also gets 3.12;
#   3. the uv-managed tools rebuilt on 3.12 — mypy and flake8 read the
#      interpreter's version, so on 3.11 they judged code against 3.11 rules.
#
# What it deliberately does NOT touch: the update-alternatives links under
# /usr/bin. Scripts with a literal `#!/usr/bin/python3` shebang follow those,
# and some of the image's own tools (conan) are installed for 3.11 only — a
# flip there breaks them for no gain the three surfaces above don't already
# give.
#
# Remote-only (a local checkout keeps whatever the developer's shell provides),
# idempotent (everything is skipped once it already reads 3.12, so the second
# repo's copy in the same session costs ~0.2s), and non-blocking: every step
# degrades to a logged warning rather than failing the session start.
#
# Per-repo dependencies: a repo that needs more than pytest + PyYAML declares it
# in .claude/session-python.txt — one pip argument per line (`-e .`, a package
# spec, `-r requirements.txt`; `#` comments ignored). Installed additively into
# the shared venv, so the file stays out of this generated hook and the hook
# stays byte-identical in every repo.
set -euo pipefail

[ "${CLAUDE_CODE_REMOTE:-}" = "true" ] || exit 0

VENV="${PYAUTO_SESSION_VENV:-$HOME/.pyauto/session-py312}"
BASE_DEPS=(pytest PyYAML)

# Which checkout is this copy of the hook installed in?
#
# NOT $CLAUDE_PROJECT_DIR. That is the session's project directory, which equals
# the repo only when the session holds exactly ONE repo. A session scoped to
# several organs clones them side by side under the project directory
# (/home/user/PyAutoMind, /home/user/PyAutoBrain, ...), and then
# $CLAUDE_PROJECT_DIR is their parent — so reading session-python.txt from it
# found nothing, silently, in exactly the sessions that hold the most repos.
#
# Derive it from where this script actually is, in both the installed and the
# canonical location.
HOOK_SELF="$(readlink -f "$0")"
case "$(dirname "$HOOK_SELF")" in
    */.claude/hooks) REPO_DIR="$(cd "$(dirname "$HOOK_SELF")/../.." && pwd)" ;;
    */policy)        REPO_DIR="$(cd "$(dirname "$HOOK_SELF")/.."    && pwd)" ;;
    *)               REPO_DIR="${CLAUDE_PROJECT_DIR:-$PWD}" ;;
esac
WORKSPACE_ROOT="$(dirname "$REPO_DIR")"
EXTRAS_FILE="$REPO_DIR/.claude/session-python.txt"

# stderr, not stdout: a SessionStart hook's stdout is fed to the agent as
# session context.
log() { printf '[session-start] %s\n' "$*" >&2; }

is_py312() {
    [ -x "$1" ] && "$1" -c 'import sys; raise SystemExit(sys.version_info[:2] != (3, 12))' >/dev/null 2>&1
}

find_base_python() {
    local candidate
    for candidate in /usr/bin/python3.12 /usr/local/bin/python3.12 \
                     "$(command -v python3.12 2>/dev/null || true)"; do
        if [ -n "$candidate" ] && is_py312 "$candidate"; then
            printf '%s\n' "$candidate"
            return 0
        fi
    done
    # No system 3.12 (a future base image could drop it) — uv can fetch one.
    if command -v uv >/dev/null 2>&1; then
        log "no system python3.12; asking uv to install one"
        uv python install 3.12 >&2 || return 1
        candidate="$(uv python find 3.12 2>/dev/null || true)"
        if [ -n "$candidate" ] && is_py312 "$candidate"; then
            printf '%s\n' "$candidate"
            return 0
        fi
    fi
    return 1
}

venv_ready() {
    is_py312 "$VENV/bin/python" \
        && [ -x "$VENV/bin/pip" ] \
        && "$VENV/bin/python" -c 'import pytest, yaml' >/dev/null 2>&1
}

# 1. The interpreter a session types: python, python3, pip, pytest.
ensure_venv() {
    local base_python
    if venv_ready; then
        log "reusing $VENV ($("$VENV/bin/python" -V 2>&1))"
        return 0
    fi
    if ! base_python="$(find_base_python)"; then
        log "WARNING: no Python 3.12 in this container; PATH left unchanged"
        return 1
    fi
    log "building $VENV on $base_python"
    rm -rf "$VENV"
    mkdir -p "$(dirname "$VENV")"
    if command -v uv >/dev/null 2>&1; then
        # --seed puts pip inside the venv too, so `pip install` targets 3.12
        # rather than falling through to the container's 3.11 /usr/bin/pip.
        uv venv --seed --python "$base_python" "$VENV" >&2
        uv pip install --python "$VENV/bin/python" --quiet "${BASE_DEPS[@]}" >&2
    else
        "$base_python" -m venv "$VENV" >&2
        "$VENV/bin/python" -m pip install --quiet --upgrade pip >&2
        "$VENV/bin/python" -m pip install --quiet "${BASE_DEPS[@]}" >&2
    fi
    venv_ready || { log "WARNING: could not build a 3.12 venv at $VENV"; return 1; }
}

# This repo's own dependencies, if it declares any. Additive and marked, so a
# session holding several repos installs each repo's set exactly once.
ensure_repo_extras() {
    [ -r "$EXTRAS_FILE" ] || return 0
    local marker args=()
    marker="$VENV/.extras-$(cksum <"$EXTRAS_FILE" | tr -d ' /')"
    [ -e "$marker" ] && return 0
    while IFS= read -r line; do
        line="${line%%#*}"
        line="$(printf '%s' "$line" | tr -d '\r' | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')"
        [ -n "$line" ] && args+=("$line")
    done <"$EXTRAS_FILE"
    [ ${#args[@]} -gt 0 ] || return 0
    log "installing this repo's declared deps: ${args[*]}"
    if (cd "$(dirname "$(dirname "$EXTRAS_FILE")")" && "$VENV/bin/python" -m pip install --quiet "${args[@]}" >&2); then
        : >"$marker"
    else
        log "WARNING: $EXTRAS_FILE install failed; continuing without it"
    fi
}

# 2. What PATH means without this session's env file.
point_system_default() {
    local base_python="$1" link
    for link in /usr/local/bin/python /usr/local/bin/python3; do
        is_py312 "$link" && continue
        [ -w "$(dirname "$link")" ] || { log "WARNING: cannot rewrite $link (not writable)"; continue; }
        ln -sfn "$base_python" "$link"
    done
    is_py312 /usr/local/bin/python3 \
        && log "/usr/local/bin/python{,3} -> $base_python" \
        || log "WARNING: /usr/local/bin/python3 is still $(/usr/local/bin/python3 -V 2>&1)"
}

# 3. The uv-managed tools — rebuilt on 3.12 only where they are not already.
#
# Pinned to the version already installed: this hook changes the INTERPRETER a
# tool runs on, and nothing else. Unpinned, `uv tool install --force` fetches
# the latest release, which quietly moved mypy across a major version (1.19 ->
# 2.3) the first time this ran — a lint-result change nobody asked for, riding
# in on a Python upgrade. Falls back to unpinned only if the pin cannot be
# resolved for 3.12.
retool_uv_tools() {
    command -v uv >/dev/null 2>&1 || return 0
    local tools_dir tool name version spec
    tools_dir="$(uv tool dir 2>/dev/null || echo "$HOME/.local/share/uv/tools")"
    [ -d "$tools_dir" ] || return 0
    for tool in "$tools_dir"/*/; do
        name="$(basename "$tool")"
        is_py312 "$tool/bin/python" && continue
        version="$(uv tool list 2>/dev/null | awk -v n="$name" '$1 == n {print substr($2, 2); exit}')"
        spec="$name"
        [ -n "$version" ] && spec="$name==$version"
        if uv tool install --python 3.12 --force "$spec" >/dev/null 2>&1 \
           || uv tool install --python 3.12 --force "$name" >/dev/null 2>&1; then
            log "rebuilt ${spec} on 3.12"
        else
            log "WARNING: could not rebuild $name on 3.12; it stays on $("$tool/bin/python" -V 2>&1)"
        fi
    done
}

# 4. Honest git history.
#
# A remote session clones shallow. `git merge-base --is-ancestor` then LIES
# across the graft boundary: it reports "not an ancestor" for a commit whose
# ancestry is simply not in the clone, and the ship/close-out skills act on that
# answer. A completion record already logged this the hard way
# (complete/2026/08/status-sh-repos-missing-source.md, "environment note").
#
# These repos are small (single-digit MB of .git), so unshallowing costs a
# couple of seconds once per container and removes a whole class of wrong
# answer. Bounded and non-fatal: a slow or blocked network leaves a shallow
# clone and a warning, never a failed session start.
ensure_full_clone() {
    local repo
    for repo in "$WORKSPACE_ROOT"/*/; do
        [ -e "${repo}.git/shallow" ] || continue
        log "unshallowing $(basename "$repo") (shallow clones make ancestry checks lie)"
        if timeout 120 git -C "$repo" fetch --unshallow --quiet 2>/dev/null \
           || timeout 120 git -C "$repo" fetch --depth=2147483647 --quiet 2>/dev/null; then
            log "  $(basename "$repo"): full history ($(git -C "$repo" rev-list --count HEAD 2>/dev/null) commits)"
        else
            log "  WARNING: $(basename "$repo") is still shallow — run 'git fetch --unshallow' before trusting any ancestry check"
        fi
    done
}

# 5. Make the NEXT session in this container start correctly.
#
# Claude Code registers project hooks from the session's project directory. In a
# one-repo session that IS the repo, and `<repo>/.claude/settings.json` is found.
# In a session holding several organs the project directory is their parent,
# which is not a repo and has no `.claude/` — so none of the per-repo hooks are
# registered and none of this script runs. That is why a multi-repo session came
# up on the container's Python 3.11: not a broken hook, an unreachable one.
#
# A repo cannot ship a file into its own parent, so install it at run time. The
# settings we write fan out to every sibling repo's own hook, so the layout
# stays "each repo owns its hook" and this file stays generated-from-one-source.
# It takes effect on the next session start in this container.
install_workspace_settings() {
    # Only in the multi-repo layout: when the project dir IS this repo, Claude
    # Code already found the repo's own settings and there is nothing to add.
    [ -n "${CLAUDE_PROJECT_DIR:-}" ] || return 0
    [ "$(readlink -f "$CLAUDE_PROJECT_DIR")" != "$(readlink -f "$REPO_DIR")" ] || return 0

    local settings="$CLAUDE_PROJECT_DIR/.claude/settings.json"
    local fanout="$CLAUDE_PROJECT_DIR/.claude/hooks/session-start.sh"
    [ -w "$CLAUDE_PROJECT_DIR" ] || { log "WARNING: $CLAUDE_PROJECT_DIR not writable; multi-repo sessions will keep skipping the hook"; return 0; }

    mkdir -p "$(dirname "$fanout")"
    cat >"$fanout" <<'FANOUT'
#!/usr/bin/env bash
# GENERATED at session start by a PyAuto repo's own session-start hook.
# Runs every sibling repo's hook, because the workspace root is not a repo and
# therefore has no hook of its own. Each repo's hook is idempotent, so the
# second and later ones cost ~0.2s.
set -u
ROOT="$(cd "$(dirname "$(readlink -f "$0")")/../.." && pwd)"
for repo in "$ROOT"/*/; do
    hook="${repo}.claude/hooks/session-start.sh"
    [ -x "$hook" ] || continue
    CLAUDE_PROJECT_DIR="${repo%/}" "$hook" || \
        printf '[session-start] WARNING: %s failed\n' "$hook" >&2
done
FANOUT
    chmod 0755 "$fanout"

    if [ ! -f "$settings" ]; then
        cat >"$settings" <<'SETTINGS'
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/session-start.sh"
          }
        ]
      }
    ]
  }
}
SETTINGS
        log "installed $settings — multi-repo sessions in this container now run the hook"
    fi
}

# Git history and hook reachability have nothing to do with the interpreter, so
# they run first and unconditionally: a container where the 3.12 venv cannot be
# built still wants honest ancestry and a hook that fires next session.
ensure_full_clone
install_workspace_settings

# PYAUTO_SESSION_SKIP_PYTHON=1 stops here — the seam the hook's own tests use to
# exercise the legs above without building an interpreter.
if [ "${PYAUTO_SESSION_SKIP_PYTHON:-}" = "1" ]; then
    log "PYAUTO_SESSION_SKIP_PYTHON=1 — leaving the interpreter alone"
    exit 0
fi

if ensure_venv; then
    ensure_repo_extras
    point_system_default "$(readlink -f "$VENV/bin/python")"
    retool_uv_tools
    # Every repo in the session registers this hook, so the second copy must not
    # prepend the venv a second time.
    if [ -n "${CLAUDE_ENV_FILE:-}" ] && ! grep -qs 'PYAUTO_SESSION_PY312=' "$CLAUDE_ENV_FILE"; then
        {
            echo "export PYAUTO_SESSION_PY312=\"$VENV\""
            echo "export VIRTUAL_ENV=\"$VENV\""
            echo "export PATH=\"$VENV/bin:\$PATH\""
            # The workspace root, so the Brain's shell/python resolvers agree
            # with the session instead of each re-deriving it.
            echo "export PYAUTO_ROOT=\"$WORKSPACE_ROOT\""
        } >>"$CLAUDE_ENV_FILE"
    fi
    log "default python is now $("$VENV/bin/python" -V 2>&1) ($VENV/bin)"
fi
