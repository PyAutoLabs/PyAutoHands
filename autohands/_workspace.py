"""autohands/_workspace.py — where the workspace root is, asked in one place.

The answer belongs to the organism, not to this organ: it lives in
``PyAutoBrain/agents/_pyauto_root.py`` (mirrored by ``bin/_pyauto_root.sh``).
This module is the Hands' door to it — everything here that needs the root
imports from here, so the rule can move once, in the Brain, and the Hands
follow.

The Hands used to roll their own answer in three places: ``board.py`` fell back
to a ``$HOME``-relative path naming the directory ABOVE the workspace (so
``root / "PyAutoBrain"`` named a path that has never existed), while
``run_all.py`` and ``pre_build.sh`` counted a fixed number of directories up
from a file. Counting is right until the checkouts are grouped; a spelled-out
path is an instance fact either way.

**No hard dependency on PyAutoBrain.** The Hands run with no Brain in reach —
which is why ``board.theme()`` degrades rather than importing unconditionally.
So does this: when the Brain's resolver cannot be found, the rule below is
applied locally and the reason string says so, rather than a wrong root passing
for a right one. The local copy is deliberate duplication of a documented rule,
kept as short as it can be; the Brain's module is the one that explains it.

Stdlib only; the Brain module is loaded by file path rather than by pushing a
directory onto ``sys.path``, so importing this never changes what any other
``import`` in the process resolves to.
"""

from __future__ import annotations

import importlib.util
import os
from pathlib import Path

__all__ = ["workspace_root", "workspace_root_reason", "ROOT_MARKER"]

HANDS_HOME = Path(__file__).resolve().parents[1]

# Mirrors PyAutoBrain/agents/_pyauto_root.py. Only the degraded path below
# reads these; when the Brain is in reach its own values are used.
ROOT_MARKER = ".pyauto-root"
_SIBLING_ORGANS = (
    "PyAutoMind",
    "PyAutoCortex",
    "PyAutoMemory",
    "PyAutoHeart",
    "PyAutoHands",
    "PyAutoNerves",
    "PyAutoGut",
)

_DEGRADED = " (no PyAutoBrain in reach)"

_shared_cache: object | None = None


def _shared():
    """The Brain's resolver module, or None when no Brain checkout is in reach.

    Candidate order mirrors ``board.theme()``: the explicit ``$PYAUTO_BRAIN``
    first, then a Brain beside this checkout (where CI puts it — tests.yml and
    release_board.yml check PyAutoBrain out next to PyAutoHands), then a
    vendored one inside it.
    """
    global _shared_cache
    if _shared_cache is not None:
        return _shared_cache or None
    for cand in (
        os.environ.get("PYAUTO_BRAIN"),
        HANDS_HOME.parent / "PyAutoBrain",
        HANDS_HOME / "PyAutoBrain",
    ):
        if not cand:
            continue
        module_path = Path(cand) / "agents" / "_pyauto_root.py"
        if not module_path.is_file():
            continue
        try:
            spec = importlib.util.spec_from_file_location("_pyauto_root", module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
        except Exception:  # a broken/partial checkout must not break the Hands
            continue
        if not callable(getattr(module, "workspace_root_reason", None)):
            continue  # a resolver older than this API: degrade, do not raise
        _shared_cache = module
        return module
    _shared_cache = False
    return None


def _marked_root(start: Path) -> Path | None:
    """The nearest ANCESTOR of `start` holding the marker, or None."""
    for candidate in start.parents:
        if (candidate / ROOT_MARKER).is_file():
            return candidate
    return None


def workspace_root_reason() -> tuple[Path, str]:
    """``(root, why)`` — the workspace root and the rule that produced it."""
    shared = _shared()
    if shared is not None:
        return shared.workspace_root_reason()
    # Degraded: the same order as the Brain's module, applied here. The
    # environment override comes first, so an operator's word still wins.
    env = os.environ.get("PYAUTO_ROOT")
    if env:
        if (Path(env) / ROOT_MARKER).is_file():
            return Path(env), "PYAUTO_ROOT" + _DEGRADED
        return (
            Path(env),
            f"PYAUTO_ROOT (unverified - no {ROOT_MARKER} marker)" + _DEGRADED,
        )
    marked = _marked_root(HANDS_HOME)
    if marked is not None:
        return marked, f"{ROOT_MARKER} marker" + _DEGRADED
    parent = HANDS_HOME.parent
    if any((parent / organ).is_dir() for organ in _SIBLING_ORGANS):
        return parent, "beside this checkout" + _DEGRADED
    return parent, "unverified (no sibling organ beside this checkout)" + _DEGRADED


def workspace_root() -> Path:
    """The workspace root — the directory holding the organ checkouts."""
    return Path(workspace_root_reason()[0])
