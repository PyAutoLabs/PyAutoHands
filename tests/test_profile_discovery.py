"""Tests for env_config.find_profile — dual-name profile discovery.

Migration step 6 of docs/env_profile_redesign.md (#161): every reader accepts
BOTH the canonical name (profile_smoke.yaml / profile_release.yaml) and the
legacy env_vars*.yaml name, with the canonical preferred.
"""

import sys
from pathlib import Path

AUTOHANDS_DIR = Path(__file__).parent.parent / "autohands"
sys.path.insert(0, str(AUTOHANDS_DIR))

from env_config import PROFILE_NAMES, find_profile  # noqa: E402


def test_canonical_only_returns_canonical(tmp_path):
    (tmp_path / "profile_smoke.yaml").write_text("defaults: {}\n")
    assert find_profile(tmp_path, "smoke") == tmp_path / "profile_smoke.yaml"


def test_legacy_only_returns_legacy(tmp_path):
    (tmp_path / "env_vars.yaml").write_text("defaults: {}\n")
    assert find_profile(tmp_path, "smoke") == tmp_path / "env_vars.yaml"


def test_both_present_prefers_canonical(tmp_path):
    (tmp_path / "profile_smoke.yaml").write_text("defaults: {}\n")
    (tmp_path / "env_vars.yaml").write_text("defaults: {}\n")
    assert find_profile(tmp_path, "smoke") == tmp_path / "profile_smoke.yaml"


def test_neither_present_returns_none(tmp_path):
    assert find_profile(tmp_path, "smoke") is None


def test_release_kind_canonical_and_legacy(tmp_path):
    (tmp_path / "env_vars_release.yaml").write_text("defaults: {}\n")
    assert find_profile(tmp_path, "release") == tmp_path / "env_vars_release.yaml"
    (tmp_path / "profile_release.yaml").write_text("defaults: {}\n")
    assert find_profile(tmp_path, "release") == tmp_path / "profile_release.yaml"


def test_profile_names_shape():
    assert PROFILE_NAMES["smoke"] == ("profile_smoke.yaml", "env_vars.yaml")
    assert PROFILE_NAMES["release"] == (
        "profile_release.yaml",
        "env_vars_release.yaml",
    )
