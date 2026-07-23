"""Tests for env_config.find_profile — canonical-only profile discovery.

Since #161 step-6 stage 3 the legacy ``env_vars*.yaml`` names are dead: every
reader resolves the canonical ``profile_smoke.yaml`` / ``profile_release.yaml``
name only, and a legacy file no longer resolves to anything.
"""

import sys
from pathlib import Path

AUTOHANDS_DIR = Path(__file__).parent.parent / "autohands"
sys.path.insert(0, str(AUTOHANDS_DIR))

from env_config import LEGACY_PROFILE_NAMES, PROFILE_NAMES, find_profile  # noqa: E402


def test_canonical_smoke_returns_path(tmp_path):
    (tmp_path / "profile_smoke.yaml").write_text("defaults: {}\n")
    assert find_profile(tmp_path, "smoke") == tmp_path / "profile_smoke.yaml"


def test_canonical_release_returns_path(tmp_path):
    (tmp_path / "profile_release.yaml").write_text("defaults: {}\n")
    assert find_profile(tmp_path, "release") == tmp_path / "profile_release.yaml"


def test_legacy_only_returns_none(tmp_path):
    # A workspace still carrying the dead name resolves to nothing — the
    # legacy name is no longer a discovery fallback.
    (tmp_path / "env_vars.yaml").write_text("defaults: {}\n")
    assert find_profile(tmp_path, "smoke") is None


def test_legacy_release_only_returns_none(tmp_path):
    (tmp_path / "env_vars_release.yaml").write_text("defaults: {}\n")
    assert find_profile(tmp_path, "release") is None


def test_neither_present_returns_none(tmp_path):
    assert find_profile(tmp_path, "smoke") is None


def test_profile_names_shape():
    assert PROFILE_NAMES["smoke"] == "profile_smoke.yaml"
    assert PROFILE_NAMES["release"] == "profile_release.yaml"


def test_legacy_profile_names_shape():
    assert LEGACY_PROFILE_NAMES == {
        "env_vars.yaml": "profile_smoke.yaml",
        "env_vars_release.yaml": "profile_release.yaml",
    }
