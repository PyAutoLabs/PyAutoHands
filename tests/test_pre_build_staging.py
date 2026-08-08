"""End-to-end behaviour tests for `pre_build.sh`'s staging and WIP preflight.

`test_pre_build_skill.py` asserts against the *text* of the script. That cannot
prove the preflight actually fires or that staging is exact, so these tests run
the real script against a throwaway PYAUTOBASE of fixture git repos, with
`black`, `python`/`python3` and `gh` stubbed on PATH. Nothing real is touched
and nothing is pushed anywhere but a local bare remote.

The behaviour under test is the 2026-08-07 near-miss: `git add <dir>/` also
stages *untracked* files, so a human's in-progress script in a workspace's
`scripts/` would be reformatted by black and pushed inside the "pre build"
commit.
"""

import os
import re
import shutil
import subprocess
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
PRE_BUILD = ROOT / "pre_build.sh"

# The repos pre_build walks, parsed from the script so this fixture cannot
# drift away from the executor the way a second hand-written list would.
SPECS = re.findall(
    r'^\s+"(\S+)\s+(\S+)\s+(\S+)\s+(\S+)"', PRE_BUILD.read_text(), re.MULTILINE
)


def _git(repo, *args):
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        check=True,
        capture_output=True,
        text=True,
    ).stdout


def _init_repo(path):
    path.mkdir(parents=True, exist_ok=True)
    _git(path, "init", "-q", "-b", "main", ".")
    _git(path, "config", "user.email", "fixture@example.com")
    _git(path, "config", "user.name", "fixture")
    return path


def _commit_all(repo, message):
    _git(repo, "add", "-A")
    _git(repo, "commit", "-qm", message)


@pytest.fixture
def base(tmp_path):
    """A throwaway PYAUTOBASE: PyAutoHands + every workspace pre_build walks."""
    assert SPECS, "failed to parse WORKSPACE_SPECS out of pre_build.sh"

    pyautobase = tmp_path / "PyAutoLabs"

    # PyAutoHands itself, holding the script under test. pre_build requires it
    # on a clean main before it will do anything.
    hands = _init_repo(pyautobase / "PyAutoHands")
    (hands / "autohands").mkdir()
    shutil.copy(PRE_BUILD, hands / "pre_build.sh")
    _commit_all(hands, "fixture hands")

    for repo, _project, _generate, _slam in SPECS:
        work = _init_repo(pyautobase / repo)
        (work / "scripts").mkdir()
        (work / "scripts" / "committed.py").write_text("x = 1\n")
        (work / "notebooks").mkdir()
        (work / "notebooks" / "committed.ipynb").write_text("{}\n")
        _commit_all(work, "fixture workspace")

        # A real bare remote, so the script's `git push` is exercised rather
        # than stubbed away.
        remote = tmp_path / "remotes" / f"{repo}.git"
        remote.parent.mkdir(exist_ok=True)
        subprocess.run(
            ["git", "init", "-q", "--bare", str(remote)], check=True
        )
        _git(work, "remote", "add", "origin", str(remote))
        _git(work, "push", "-q", "-u", "origin", "main")

    return pyautobase


@pytest.fixture
def stub_bin(tmp_path):
    """Stubs for the external commands pre_build shells out to."""
    bindir = tmp_path / "stubbin"
    bindir.mkdir()

    # black must be a no-op that still exits 0. `gh` must not dispatch a real
    # release workflow. `python`/`python3` stand in for generate.py and
    # check_dataset_allowlist.py; generate.py is asked to create a notebook so
    # the "new file this run produced" path is covered.
    (bindir / "black").write_text("#!/bin/bash\nexit 0\n")
    (bindir / "gh").write_text("#!/bin/bash\nexit 0\n")
    stub_python = (
        "#!/bin/bash\n"
        'case "$*" in\n'
        "  *generate.py*) mkdir -p notebooks && "
        'printf "{}\\n" > notebooks/generated.ipynb ;;\n'
        "esac\n"
        "exit 0\n"
    )
    for name in ("python", "python3"):
        (bindir / name).write_text(stub_python)

    for f in bindir.iterdir():
        f.chmod(0o755)
    return bindir


def _run(base, stub_bin):
    env = dict(os.environ)
    env["PATH"] = f"{stub_bin}:{env['PATH']}"
    # pre_build only runs ensure_workspace_labels.sh when gh is on PATH; it is
    # stubbed, so give it a real (no-op) script to find.
    brain_bin = base / "PyAutoBrain" / "bin"
    brain_bin.mkdir(parents=True, exist_ok=True)
    labels = brain_bin / "ensure_workspace_labels.sh"
    labels.write_text("#!/bin/bash\nexit 0\n")
    labels.chmod(0o755)

    return subprocess.run(
        ["bash", str(base / "PyAutoHands" / "pre_build.sh")],
        capture_output=True,
        text=True,
        env=env,
        cwd=str(base),
    )


def test_untracked_wip_aborts_before_anything_is_touched(base, stub_bin):
    """A human's uncommitted script blocks the release and is left alone."""
    victim = base / "autolens_assistant" / "scripts" / "wip_private.py"
    victim.write_text("secret  =  1\n")
    original = victim.read_bytes()

    result = _run(base, stub_bin)

    assert result.returncode != 0, result.stdout
    assert "ABORT: uncommitted work" in result.stderr
    # Names the repo and the exact path, so one run surfaces the whole problem.
    assert "autolens_assistant" in result.stderr
    assert "scripts/wip_private.py" in result.stderr

    # Untouched on disk: the abort precedes black.
    assert victim.read_bytes() == original

    # And nothing was committed anywhere — the abort precedes the first repo.
    for repo, *_ in SPECS:
        log = _git(base / repo, "log", "--oneline")
        assert "pre build" not in log


def test_wip_in_any_repo_is_reported_together(base, stub_bin):
    """The preflight sweeps every repo before aborting, not just the first."""
    (base / SPECS[0][0] / "scripts" / "a_wip.py").write_text("a = 1\n")
    (base / SPECS[-1][0] / "notebooks" / "z_wip.ipynb").write_text("{}\n")

    result = _run(base, stub_bin)

    assert result.returncode != 0
    assert SPECS[0][0] in result.stderr
    assert SPECS[-1][0] in result.stderr


def test_gitignored_files_do_not_block_a_release(base, stub_bin):
    """`--exclude-standard` keeps output/ and other ignored cruft out."""
    work = base / "autolens_workspace"
    (work / ".gitignore").write_text("scripts/scratch/\n")
    _commit_all(work, "fixture gitignore")
    (work / "scripts" / "scratch").mkdir()
    (work / "scripts" / "scratch" / "junk.py").write_text("junk = 1\n")

    result = _run(base, stub_bin)

    assert result.returncode == 0, result.stderr


def test_generated_notebooks_are_still_staged(base, stub_bin):
    """The narrower staging must not drop genuinely new run output."""
    result = _run(base, stub_bin)
    assert result.returncode == 0, result.stderr

    # generate.py runs for the repos flagged generate=true; each must have
    # committed the notebook the stub created.
    generating = [repo for repo, _p, generate, _s in SPECS if generate == "true"]
    assert generating, "fixture expects at least one generate=true repo"
    for repo in generating:
        tracked = _git(base / repo, "ls-files", "notebooks")
        assert "notebooks/generated.ipynb" in tracked, repo
        assert "pre build" in _git(base / repo, "log", "--oneline")


def test_missing_checkout_aborts_in_the_preflight(base, stub_bin):
    """A missing repo fails clearly up front, not as a bare `cd` error midway."""
    shutil.rmtree(base / "HowToFit")

    result = _run(base, stub_bin)

    assert result.returncode != 0
    assert "HowToFit is missing or is not a git repo" in result.stderr
    # Nothing was published before the failure was noticed.
    assert "pre build" not in _git(base / "autofit_workspace", "log", "--oneline")


def test_tracked_deletions_are_staged(base, stub_bin):
    """`git add -u` must carry a retired notebook's deletion into the commit."""
    work = base / "autolens_workspace"
    (work / "notebooks" / "committed.ipynb").unlink()

    result = _run(base, stub_bin)
    assert result.returncode == 0, result.stderr

    assert "notebooks/committed.ipynb" not in _git(work, "ls-files", "notebooks")
    assert "pre build" in _git(work, "log", "--oneline")
