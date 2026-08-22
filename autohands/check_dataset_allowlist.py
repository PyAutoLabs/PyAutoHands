#!/usr/bin/env python3
"""Leg 4 of PyAutoBuild#126 — dataset allowlist guard.

Asserts that every tracked file under `dataset/` in the current workspace is
covered by that workspace's `.gitignore` allowlist (the `!dataset/...` re-include
lines). This makes the `git add -f` leak (fixed in pre_build) unable to recur: if
a simulated dataset is ever force-committed again, a `pre_build` release run fails
loudly here instead of shipping ~10 MB of runtime-generated data to users.

Allowlist-based, NOT `git check-ignore`-based: `git check-ignore` never flags an
already-tracked file (a tracked file is by definition not ignored) and mishandles
`!`-negated paths, so it cannot detect this leak. We compare tracked paths against
the parsed allowlist directly.

Allowlist-presence-gated: a workspace whose `.gitignore` has a bare `dataset/`
rule with no `!dataset/...` re-includes has not yet adopted the allowlist regime
(Group B, PyAutoBuild#126) — the guard skips it with a notice rather than
failing, until that repo opts in.

Leg 2 (PyAutoArray#470) — the mirror-image failure. The check above asserts that
nothing *generated* got committed. This one asserts that nothing *committed* gets
deleted: `should_simulate()` ends in `shutil.rmtree`, so a script that reaches an
allowlisted dataset directory while `PYAUTO_SMALL_DATASETS=1` is still in force
destroys data the allowlist exists to protect. The library-side stamp guard
(`_is_capped_at_the_current_cap`) cannot cover this in general — it reads
`<dataset>/data.fits`, so any JSON-only dataset is invisible to it.

A script opts out of the capped regime with an `__Env__` declaration whose tokens
release `PYAUTO_SMALL_DATASETS` (`full_datasets`, or the superset `real_output`).
The releasing set is derived from `env_config.ENV_DECLARATION_TOKENS`, never
hardcoded, so a future token that releases the var is picked up automatically.

Matching a call site to a directory is deliberately EXACT, not fuzzy: the
argument is resolved through a restricted AST evaluator (string literals, simple
module-level names, `Path(...) / "..."`, `os.path.join(...)`, plain f-strings).
Anything it cannot resolve is REPORTED AND SKIPPED, never guessed — this gate
runs in `pre_build`, where a false positive blocks a release. Under-reporting is
acceptable and visible; over-reporting is not. The skipped count is always
printed, so a silent partial sweep cannot read as full coverage.

Run from a workspace root. Exit 0 = clean/skipped, 1 = violation.
"""
import ast
import re
import subprocess
import sys
from pathlib import Path


def allowlist_prefixes(gitignore: Path):
    prefixes = []
    has_dataset_ignore = False
    if not gitignore.exists():
        return prefixes, has_dataset_ignore
    for line in gitignore.read_text().splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        if re.match(r"^/?dataset(/\*\*|/)?\s*$", s):
            has_dataset_ignore = True
        if s.startswith("!") and "dataset" in s:
            p = re.sub(r"/\*+$", "", s[1:].strip().lstrip("/")).rstrip("/")
            prefixes.append(p)
    return prefixes, has_dataset_ignore


def tracked_dataset_files():
    out = subprocess.run(
        ["git", "ls-files", "dataset/"], capture_output=True, text=True
    ).stdout
    return [f for f in out.splitlines() if f and not f.endswith("dataset/.gitignore")]


UNRESOLVED = None


def _releasing_tokens():
    """Tokens whose declaration unsets ``PYAUTO_SMALL_DATASETS``.

    Derived from the token map rather than hardcoded as ``{"full_datasets",
    "real_output"}``: a token added later that also releases the var must start
    protecting scripts without an edit here. Falls back to the known pair only if
    the import is unavailable (the guard must never hard-fail on an env_config
    refactor -- it would block a release).
    """
    try:
        from autohands.env_config import ENV_DECLARATION_TOKENS
    except Exception:
        return {"full_datasets", "real_output"}

    return {
        tok
        for tok, vars_ in ENV_DECLARATION_TOKENS.items()
        if "PYAUTO_SMALL_DATASETS" in vars_
    }


def _resolve(node, names):
    """Resolve an AST node to a relative path string, or ``UNRESOLVED``.

    A deliberately small grammar. Every unhandled node type returns
    ``UNRESOLVED``, which the caller reports and skips -- this feeds a
    release-blocking gate, so guessing is worse than not knowing.
    """
    if isinstance(node, ast.Constant):
        return node.value if isinstance(node.value, str) else UNRESOLVED

    if isinstance(node, ast.Name):
        return names.get(node.id, UNRESOLVED)

    # Path("dataset") / "point_source" / name
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
        left = _resolve(node.left, names)
        right = _resolve(node.right, names)
        if left is UNRESOLVED or right is UNRESOLVED:
            return UNRESOLVED
        return f"{left}/{right}"

    if isinstance(node, ast.JoinedStr):
        parts = []
        for value in node.values:
            piece = _resolve(
                value.value if isinstance(value, ast.FormattedValue) else value, names
            )
            if piece is UNRESOLVED:
                return UNRESOLVED
            parts.append(piece)
        return "".join(parts)

    if isinstance(node, ast.Call):
        func = node.func
        name = func.attr if isinstance(func, ast.Attribute) else getattr(func, "id", "")

        # Path("dataset", "multi_galaxy", dataset_name) -- Path joins ALL its
        # arguments, and the multi-argument form is the dominant idiom in the
        # workspaces. Handling only the single-argument case left ~31% of call
        # sites unresolved.
        if name in ("Path", "PosixPath") and node.args:
            parts = []
            for arg in node.args:
                piece = _resolve(arg, names)
                if piece is UNRESOLVED:
                    return UNRESOLVED
                parts.append(piece)
            return "/".join(parts)

        # os.path.join(a, b, ...) / path.join(...) / Path.joinpath(...)
        if name in ("join", "joinpath"):
            parts = []
            if name == "joinpath" and isinstance(func, ast.Attribute):
                base = _resolve(func.value, names)
                if base is UNRESOLVED:
                    return UNRESOLVED
                parts.append(base)
            for arg in node.args:
                piece = _resolve(arg, names)
                if piece is UNRESOLVED:
                    return UNRESOLVED
                parts.append(piece)
            return "/".join(parts)

        # str(x) around an already-resolvable path is common at the call site.
        if name == "str" and len(node.args) == 1:
            return _resolve(node.args[0], names)

    return UNRESOLVED


def _module_assignments(tree):
    """Ordered ``(lineno, name, value_node)`` for TOP-LEVEL assignments only.

    Top-level only, because these workspace scripts are straight-line modules:
    a binding inside a function, loop or conditional is not knowable from
    position alone, so including it would mean guessing.

    Order matters. Reassignment (``dataset_name = "simple"`` then later
    ``dataset_name = "simple__no_lens_light"``) is the norm in these scripts, so
    a name is resolved against the assignments that precede the call site rather
    than being dropped as ambiguous.
    """
    out = []
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name):
                out.append((node.lineno, target.id, node.value))
    return out


def _names_before(assignments, lineno):
    """Bindings in force at ``lineno``, evaluated in source order."""
    names = {}
    for assign_line, name, value_node in assignments:
        if assign_line >= lineno:
            break
        resolved = _resolve(value_node, names)
        if resolved is UNRESOLVED:
            names.pop(name, None)
        else:
            names[name] = resolved
    return names


def _normalise(path_str: str) -> str:
    """Collapse a resolved argument to a repo-relative, slash-joined path."""
    cleaned = path_str.replace("\\", "/").strip().strip("/")
    parts = [seg for seg in cleaned.split("/") if seg not in ("", ".")]
    return "/".join(parts)


def should_simulate_sites(py_files):
    """Yield ``(file, lineno, resolved_path_or_None)`` per ``should_simulate`` call."""
    for f in py_files:
        try:
            tree = ast.parse(Path(f).read_text(encoding="utf-8", errors="replace"))
        except (SyntaxError, OSError):
            continue
        assignments = _module_assignments(tree)
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            func = node.func
            fname = func.attr if isinstance(func, ast.Attribute) else getattr(func, "id", "")
            if fname != "should_simulate" or not node.args:
                continue
            resolved = _resolve(node.args[0], _names_before(assignments, node.lineno))
            yield f, node.lineno, (
                _normalise(resolved) if resolved is not UNRESOLVED else UNRESOLVED
            )


def tracked_python_files():
    out = subprocess.run(
        ["git", "ls-files", "*.py"], capture_output=True, text=True
    ).stdout
    return [f for f in out.splitlines() if f]


def check_capped_deletion(prefixes, tracked) -> int:
    """Leg 2 — allowlisted datasets reachable from a capped ``should_simulate``.

    ``prefixes``/``tracked`` are leg 1's already-computed allowlist and tracked
    file list, so this adds no extra git calls beyond the Python file listing.
    """
    from autohands.env_config import read_env_declaration

    # The invariant is NOT "the path sits under an allowlist prefix" -- it is
    # "rmtree(path) would delete committed files". Those differ, and the prefix
    # form over-reports: autocti_workspace commits five doc images directly in
    # `dataset/overview/` while its overview scripts regenerate
    # `dataset/overview/imaging_ci/uniform` and `dataset/overview/dataset_1d`,
    # which hold nothing tracked. Deleting those destroys nothing. Prefix
    # matching flagged all six as release-blocking failures.
    def deletes_tracked(resolved: str) -> bool:
        return any(f == resolved or f.startswith(resolved + "/") for f in tracked)

    releasing = _releasing_tokens()
    violations, skipped = [], []

    for f, lineno, resolved in should_simulate_sites(tracked_python_files()):
        try:
            tokens = set(read_env_declaration(Path(f)) or [])
        except Exception:
            tokens = set()
        if tokens & releasing:
            continue  # releases the cap -> can never enter the small regime
        if resolved is UNRESOLVED:
            skipped.append(f"{f}:{lineno}")
            continue
        if deletes_tracked(resolved):
            violations.append((f, lineno, resolved, sorted(tokens)))

    if skipped:
        print(
            f"[capped-deletion] {len(skipped)} call site(s) skipped — argument not "
            f"statically resolvable, so NOT covered by this check:"
        )
        for s in skipped:
            print(f"    {s}")

    if violations:
        print(
            f"[capped-deletion] FAIL — should_simulate() would delete COMMITTED "
            f"files without releasing PYAUTO_SMALL_DATASETS ({len(violations)}):",
            file=sys.stderr,
        )
        for f, lineno, resolved, tokens in violations:
            declared = " ".join(tokens) if tokens else "<no __Env__ declaration>"
            print(f"    {f}:{lineno} -> {resolved}   [ENV: {declared}]", file=sys.stderr)
        print(
            "\nshould_simulate() ends in shutil.rmtree, and each path above holds "
            "git-tracked files kept by design (they carry an `!dataset/...` allowlist "
            "line). Under PYAUTO_SMALL_DATASETS=1 those files are deleted and replaced "
            "with capped-simulator output. Add a releasing token to the script's "
            "`__Env__` section (`ENV: full_datasets ...`) — see PyAutoArray#470.",
            file=sys.stderr,
        )
        return 1

    print(
        f"[capped-deletion] OK — no capped should_simulate() call site would delete "
        f"any of the {len(tracked)} committed dataset file(s)."
    )
    return 0


def main() -> int:
    prefixes, has_dataset_ignore = allowlist_prefixes(Path(".gitignore"))
    tracked = tracked_dataset_files()

    if not tracked:
        print("[dataset-allowlist] no tracked dataset/ files — OK")
        return 0

    if not prefixes:
        # bare `dataset/` (or none) with no re-includes: Group B, not yet in regime
        note = "bare `dataset/` ignore" if has_dataset_ignore else "no dataset allowlist"
        print(
            f"[dataset-allowlist] SKIP — {note}; workspace has not adopted the "
            f"allowlist regime (Group B, PyAutoBuild#126). {len(tracked)} tracked files."
        )
        return 0

    def allowed(f: str) -> bool:
        return any(f == p or f.startswith(p + "/") for p in prefixes)

    violations = sorted({"/".join(f.split("/")[:3]) for f in tracked if not allowed(f)})
    if violations:
        print(
            "[dataset-allowlist] FAIL — tracked dataset dirs outside the "
            f".gitignore allowlist ({len(violations)}):",
            file=sys.stderr,
        )
        for d in violations:
            print(f"    {d}", file=sys.stderr)
        print(
            "\nThese are simulated datasets that must be generated at runtime, not "
            "committed. Purge them (`git rm -r`) — they self-provision via "
            "should_simulate()/`.exists()` — or add a `!dataset/<dir>/**` allowlist "
            "line if the data is real/committed-by-design. See PyAutoBuild#126.",
            file=sys.stderr,
        )
        return 1

    print(
        f"[dataset-allowlist] OK — {len(tracked)} tracked dataset files, all within "
        f"the allowlist ({len(prefixes)} patterns)."
    )

    # Leg 2 runs only once leg 1 is clean: if committed data is already outside the
    # allowlist, "which allowlisted dirs are at risk" is the wrong question to ask.
    return check_capped_deletion(prefixes, tracked)


if __name__ == "__main__":
    sys.exit(main())
