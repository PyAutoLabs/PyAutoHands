"""The standalone scanner works without the repository on PYTHONPATH."""

import os
from pathlib import Path
import subprocess
import sys


def test_direct_script_entrypoint_without_pythonpath(tmp_path):
    script = Path(__file__).resolve().parents[1] / "autohands" / "slow_skip_check.py"
    env = os.environ.copy()
    env.pop("PYTHONPATH", None)
    result = subprocess.run(
        [sys.executable, str(script), str(tmp_path / "missing")],
        env=env, capture_output=True, text=True,
    )
    assert result.returncode == 0, result.stderr
    assert "No SLOW-skipped scripts found." in result.stdout
def test_distinct_flat_and_grouped_brain_checkouts_are_rejected(tmp_path, monkeypatch):
    import pytest
    from autohands import _workspace
    for path in (tmp_path / "PyAutoBrain", tmp_path / "organs" / "PyAutoBrain"):
        (path / ".git").mkdir(parents=True)
    monkeypatch.setattr(_workspace, "HANDS_HOME", tmp_path / "organs" / "PyAutoHands")
    with pytest.raises(ValueError, match="ambiguous checkouts"):
        _workspace._shared()
    with pytest.raises(ValueError, match="ambiguous checkouts"):
        _workspace._repo_paths()
