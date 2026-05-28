"""Per-script environment variable configuration.

Loads env_vars.yaml and builds a tailored environment dict for each script,
applying defaults and per-pattern overrides.
"""

import os
import shlex
from pathlib import Path
from typing import Dict, List, Optional

import yaml


def load_env_config(config_path: Path) -> dict:
    """Load and return the parsed env_vars.yaml."""
    with open(config_path) as f:
        return yaml.safe_load(f)


def build_env_for_script(
    file: Path,
    env_config: Optional[dict],
) -> Optional[Dict[str, str]]:
    """Build the environment dict for a given script or notebook.

    Parameters
    ----------
    file
        Path to the script or notebook being executed.
    env_config
        Parsed env config from load_env_config(), or None.

    Returns
    -------
    A dict suitable for subprocess.run(env=...), or None when env_config
    is None (inherit parent environment unchanged).
    """
    if env_config is None:
        return None

    env = os.environ.copy()

    for key, value in env_config.get("defaults", {}).items():
        env[key] = str(value)

    file = Path(file)

    for override in env_config.get("overrides", []):
        pattern = override["pattern"]
        if _pattern_matches(file, pattern):
            for var_name in override.get("unset", []):
                env.pop(var_name, None)
            for key, value in override.get("set", {}).items():
                env[key] = str(value)

    return env


def args_for_script(
    file: Path,
    env_config: Optional[dict],
) -> List[str]:
    """Return CLI args to append after the script path, based on env_config.

    Reads the ``args_default`` field of env_vars.yaml — a single string
    that is shlex-split into argv tokens and appended to every
    ``python <script>`` invocation. Used by workspaces whose scripts
    require CLI args (e.g. euclid needs ``--dataset`` and ``--sample``).
    Mirrors the semantics of ``args_default`` in the ``/smoke_test`` skill.

    Returns ``[]`` when env_config is None, args_default is missing, or
    args_default is empty/whitespace — making this a no-op for every
    workspace that does not opt in.
    """
    if env_config is None:
        return []
    raw = env_config.get("args_default", "")
    if not raw or not str(raw).strip():
        return []
    return shlex.split(str(raw))


def _pattern_matches(file: Path, pattern: str) -> bool:
    """Match a pattern against a file path.

    Patterns containing '/' are substring-matched against the file's full
    path **including extension** — so a pattern may include ``.py`` to anchor
    against the script form (e.g. ``imaging/visualization.py`` matches
    ``scripts/imaging/visualization.py`` but not
    ``scripts/imaging/visualization_jax.py``). Patterns without '/' match the
    file stem exactly. Same convention as build_util.should_skip().
    """
    if "/" in pattern:
        return pattern in str(file)
    else:
        return file.stem == pattern
