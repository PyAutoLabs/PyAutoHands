"""Unit tests for autobuild/env_config.py — args_for_script() in particular.

build_env_for_script() is exercised indirectly by
test_workspace_config_precedence.py; here we focus on the args_default
plumbing added for workspaces whose scripts require CLI args (euclid).
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
AUTOBUILD_DIR = PROJECT_ROOT / "autobuild"
sys.path.insert(0, str(AUTOBUILD_DIR))

from env_config import args_for_script  # noqa: E402


FAKE_FILE = Path("scripts/fake.py")


def test_args_for_script_none_env_config_returns_empty():
    assert args_for_script(FAKE_FILE, None) == []


def test_args_for_script_missing_key_returns_empty():
    assert args_for_script(FAKE_FILE, {"defaults": {"FOO": "bar"}}) == []


def test_args_for_script_empty_string_returns_empty():
    assert args_for_script(FAKE_FILE, {"args_default": ""}) == []


def test_args_for_script_whitespace_only_returns_empty():
    assert args_for_script(FAKE_FILE, {"args_default": "   \t  "}) == []


def test_args_for_script_simple_args():
    assert args_for_script(
        FAKE_FILE,
        {"args_default": "--dataset=foo --sample=bar"},
    ) == ["--dataset=foo", "--sample=bar"]


def test_args_for_script_quoted_arg_with_space():
    # shlex.split honours quoting so values containing spaces stay together.
    assert args_for_script(
        FAKE_FILE,
        {"args_default": '--name="a b" --flag'},
    ) == ["--name=a b", "--flag"]
