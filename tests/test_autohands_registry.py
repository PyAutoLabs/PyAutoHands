"""Tests for bin/autohands — the CLI registry is complete and well-formed.

`bin/autohands help` is documented (AGENTS.md, the file's own header) as *the*
registry of what is a CLI verb. Before this module nothing enforced that: seven
modules in `autohands/` had grown `__main__` blocks without ever appearing in
`help`, so the registry silently described a subset of the package.

The rule enforced here: every `autohands/*.py` that is executable (has an
`if __name__ == "__main__"` block) is either a registered subcommand in
`SUBCOMMAND_ORDER` or an explicitly declared internal module in
`INTERNAL_MODULES`. Neither list may name a module that no longer exists, and
every subcommand must carry the SHORT_DESC + cmd_* + help_* trio.

The dispatcher is bash, so this parses its text rather than executing it — the
lists are plain literal arrays, and reading them is cheaper and safer than
sourcing a script whose top level runs `main "$@"`.
"""

import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DISPATCHER = REPO / "bin" / "autohands"
MODULE_DIR = REPO / "autohands"

SOURCE = DISPATCHER.read_text()


def _array_entries(name):
    """Return the literal entries of a bash array `name=( ... )` in SOURCE."""
    match = re.search(rf"^{name}=\((.*?)^\)", SOURCE, re.MULTILINE | re.DOTALL)
    assert match, f"{name} array not found in {DISPATCHER}"

    entries = []
    for line in match.group(1).splitlines():
        entry = line.strip()
        if not entry.startswith('"#'):
            # Trailing `# reason` comments are bash comments, not array entries.
            entry = entry.split("#", 1)[0].strip()
        if entry:
            entries.append(entry.strip('"'))
    return entries


def subcommands():
    """Registered subcommand names, minus the `"# "` section headers."""
    return [e for e in _array_entries("SUBCOMMAND_ORDER") if not e.startswith("# ")]


def internal_modules():
    return _array_entries("INTERNAL_MODULES")


def executable_modules():
    """autohands/*.py modules with an `if __name__ == "__main__"` block."""
    return sorted(
        path.stem
        for path in MODULE_DIR.glob("*.py")
        if path.stem != "__init__" and "__main__" in path.read_text()
    )


def test_every_executable_module_is_registered_or_internal():
    known = set(subcommands()) | set(internal_modules())
    unregistered = [m for m in executable_modules() if m not in known]
    assert not unregistered, (
        f"autohands/ modules missing from the registry: {unregistered}. "
        "Every executable module must either be a subcommand (add it to "
        "SUBCOMMAND_ORDER with a SHORT_DESC, cmd_* and help_*) or be declared "
        "internal (add it to INTERNAL_MODULES with a one-line reason). "
        "`bin/autohands help` is the registry — it may not describe a subset."
    )


def test_internal_modules_all_exist():
    missing = [m for m in internal_modules() if not (MODULE_DIR / f"{m}.py").exists()]
    assert not missing, (
        f"INTERNAL_MODULES names modules that no longer exist: {missing}. "
        "A renamed or deleted module must leave the list too, or the "
        "allowlist quietly exempts a name nothing checks."
    )


def test_every_subcommand_has_short_desc_cmd_and_help():
    described = set(re.findall(r"^\s*\[(\w+)\]=", SOURCE, re.MULTILINE))
    implemented = set(re.findall(r"^cmd_(\w+)\(\)", SOURCE, re.MULTILINE))
    documented = set(re.findall(r"^help_(\w+)\(\)", SOURCE, re.MULTILINE))

    incomplete = {
        name: [
            missing
            for missing, have in (
                ("SHORT_DESC", name in described),
                ("cmd_", name in implemented),
                ("help_", name in documented),
            )
            if not have
        ]
        for name in subcommands()
    }
    incomplete = {name: gaps for name, gaps in incomplete.items() if gaps}
    assert not incomplete, (
        f"subcommands missing their registration trio: {incomplete}. "
        "bin/autohands requires a SHORT_DESC entry plus cmd_<name> and "
        "help_<name> functions for every entry in SUBCOMMAND_ORDER."
    )


def test_subcommands_and_internal_modules_are_disjoint():
    both = sorted(set(subcommands()) & set(internal_modules()))
    assert not both, (
        f"names declared as both a subcommand and internal: {both}. "
        "A module is one or the other."
    )
