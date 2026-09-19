"""Hands resolves workspace families through the shared Brain service."""
from autohands import _workspace


def test_grouped_workspace_is_discovered(tmp_path):
    checkout = tmp_path / "workspaces" / "demo_workspace"
    checkout.mkdir(parents=True)
    (checkout / ".git").mkdir()
    assert _workspace.repo_path(tmp_path, "demo_workspace", required=True) == checkout
    assert checkout in _workspace.iter_checkouts(tmp_path)
