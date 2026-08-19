"""Unit tests for autohands/tombstone.py.

The tombstone's whole job is to be *selected by pip below the floor and
invisible above it*, then to fail loudly when built. Three properties carry
that, and each is tested here rather than assumed:

1. the version sorts above the last permissive release and below the next real
   one — get this wrong and the tombstone is either never selected (silent
   backtrack continues) or becomes PyPI's displayed latest version;
2. the built artifact declares `Requires-Python <3.12` — get this wrong and it
   either never appears below the floor or breaks every supported install;
3. the generated guard raises below the floor and stays silent at or above it —
   an unconditional raise cannot be built into an sdist at all.

The end-to-end pip resolution test needs an interpreter below the floor and
network access, so it skips where either is missing (CI runs 3.12+ only). It is
the test that actually proves the mechanism, so it must not be the only one.
"""

import builtins
import sys
import types
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).parent.parent
AUTOHANDS_DIR = PROJECT_ROOT / "autohands"
sys.path.insert(0, str(AUTOHANDS_DIR))

import tombstone  # noqa: E402


def _exec_setup_py(source, version_info, cwd):
    """Execute a rendered setup.py as if on `version_info`, returning setup() kwargs.

    `sys.version_info` cannot be assigned, so the guard is exercised by giving
    the executed source its own `sys` and `setuptools` through a scoped
    `__import__`. Raising propagates to the caller, which is the point.
    """
    fake_sys = types.ModuleType("sys")
    fake_sys.version_info = version_info

    captured = {}
    fake_setuptools = types.ModuleType("setuptools")
    fake_setuptools.setup = lambda **kwargs: captured.update(kwargs)

    real_import = builtins.__import__

    def scoped_import(name, *args, **kwargs):
        if name == "sys":
            return fake_sys
        if name == "setuptools":
            return fake_setuptools
        return real_import(name, *args, **kwargs)

    namespace = {
        "__builtins__": {**vars(builtins), "__import__": scoped_import},
        "__file__": str(cwd / "setup.py"),
    }
    cwd_before = Path.cwd()
    import os

    os.chdir(cwd)
    try:
        exec(compile(source, "setup.py", "exec"), namespace)
    finally:
        os.chdir(cwd_before)
    return captured


# --- the version property the mechanism rests on ---------------------------


def test_tombstone_version_outranks_the_last_permissive_release():
    from packaging.version import Version

    assert Version(tombstone.TOMBSTONE_VERSION) > Version(
        tombstone.LAST_PERMISSIVE_VERSION
    )


def test_tombstone_version_stays_below_the_next_real_release():
    """It must not become PyPI's displayed latest version."""
    from packaging.version import Version

    assert Version(tombstone.TOMBSTONE_VERSION) < Version("2026.8.4.1")


def test_every_package_in_the_installable_stack_has_a_tombstone():
    """The libraries pin each other exactly, so a gap here is a hole a user
    falls through by installing that package directly."""
    assert set(tombstone.TOMBSTONE_PACKAGES) == {
        "autonerves",
        "autoarray",
        "autofit",
        "autogalaxy",
        "autolens",
    }


# --- the generated guard ---------------------------------------------------


@pytest.mark.parametrize("minor", [9, 10, 11])
def test_guard_raises_below_the_floor(tmp_path, minor):
    project = tombstone.write_project("autolens", tmp_path)
    source = (project / "setup.py").read_text()

    with pytest.raises(RuntimeError) as excinfo:
        _exec_setup_py(source, (3, minor, 0), project)

    message = str(excinfo.value)
    assert "autolens requires Python 3.12 or later" in message
    assert f"you are running Python 3.{minor}" in message
    # The escape hatch must be in the message, not only in the docs: a user
    # reproducing an old result needs to know the exact pin still works.
    assert f"pip install autolens=={tombstone.LAST_PERMISSIVE_VERSION}" in message


@pytest.mark.parametrize("minor", [12, 13, 14])
def test_guard_is_silent_at_or_above_the_floor(tmp_path, minor):
    """The guard is conditional so the sdist can still be built on a supported
    Python; an unconditional raise would make the tombstone unbuildable."""
    project = tombstone.write_project("autolens", tmp_path)
    source = (project / "setup.py").read_text()

    captured = _exec_setup_py(source, (3, minor, 0), project)

    assert captured["name"] == "autolens"
    assert captured["version"] == tombstone.TOMBSTONE_VERSION
    assert captured["python_requires"] == "<3.12"


def test_guard_names_the_package_it_was_rendered_for():
    for package in tombstone.TOMBSTONE_PACKAGES:
        source = tombstone.render_setup_py(package)
        assert f'name="{package}"' in source
        assert f"{package} requires Python 3.12 or later" in source


def test_project_has_no_pyproject_toml(tmp_path):
    """A PEP 621 [project] table would let a backend answer metadata questions
    without ever executing the guard."""
    project = tombstone.write_project("autolens", tmp_path)
    assert not (project / "pyproject.toml").exists()
    assert (project / "setup.py").exists()


# --- the built artifact ----------------------------------------------------


def _build_available():
    try:
        import build  # noqa: F401
    except ImportError:
        return False
    return True


requires_build = pytest.mark.skipif(
    not _build_available(), reason="the `build` package is not installed"
)


@requires_build
def test_built_sdist_declares_sub_floor_requires_python(tmp_path):
    project = tombstone.write_project("autolens", tmp_path)
    sdist = tombstone.build_sdist(project, tmp_path / "dist", "autolens")

    assert tombstone.sdist_requires_python(sdist) == "<3.12"


@requires_build
def test_build_sdist_returns_the_package_it_was_asked_for(tmp_path):
    """Every package builds into one shared output directory, so locating the
    artifact by "newest tarball here" would hand back a sibling's sdist and
    verify its metadata instead."""
    out = tmp_path / "dist"
    first = tombstone.build_sdist(
        tombstone.write_project("autofit", tmp_path), out, "autofit"
    )
    second = tombstone.build_sdist(
        tombstone.write_project("autoarray", tmp_path), out, "autoarray"
    )

    assert first.name.startswith("autofit-")
    assert second.name.startswith("autoarray-")


@requires_build
def test_build_all_rejects_an_artifact_with_the_wrong_floor(tmp_path, monkeypatch):
    """`build_all` verifies what it produced rather than trusting its input."""
    monkeypatch.setattr(tombstone, "sdist_requires_python", lambda _: ">=3.9")

    with pytest.raises(RuntimeError, match="refusing to hand over"):
        tombstone.build_all(tmp_path / "dist", packages=("autolens",))


# --- end to end ------------------------------------------------------------


def _interpreter_below_floor():
    import shutil

    for candidate in ("python3.11", "python3.10", "python3.9"):
        path = shutil.which(candidate)
        if path:
            return path
    return None


@requires_build
@pytest.mark.skipif(
    _interpreter_below_floor() is None,
    reason="no sub-3.12 interpreter available to resolve against",
)
def test_pip_below_the_floor_fails_loudly(tmp_path):
    """The property that matters: pip picks the tombstone and reports why.

    Served from a local PEP 503 index carrying `data-requires-python`, which is
    how pip learns a candidate's floor without downloading it — the same signal
    PyPI's simple index gives.
    """
    import html
    import subprocess

    project = tombstone.write_project("autolens", tmp_path)
    sdist = tombstone.build_sdist(project, tmp_path / "dist", "autolens")

    index = tmp_path / "index" / "autolens"
    index.mkdir(parents=True)
    (index / "index.html").write_text(
        "<!DOCTYPE html><html><body>"
        f'<a href="file://{sdist.resolve()}" '
        f'data-requires-python="{html.escape("<3.12")}">{sdist.name}</a>'
        "</body></html>"
    )

    # The venv must be built *by* the older interpreter: resolution has to run
    # on a pip whose Requires-Python check is the real one, not a simulated one.
    env_dir = tmp_path / "venv"
    subprocess.run([_interpreter_below_floor(), "-m", "venv", str(env_dir)], check=True)

    result = subprocess.run(
        [
            str(env_dir / "bin" / "python"),
            "-m",
            "pip",
            "install",
            "--no-cache-dir",
            "--dry-run",
            # Keeps the test offline. Build isolation would fetch setuptools
            # from an index, and this one holds nothing but the tombstone;
            # venvs below 3.12 still bundle setuptools, so the guard runs
            # against the interpreter's own copy.
            "--no-build-isolation",
            "--index-url",
            f"file://{tmp_path / 'index'}",
            "autolens",
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode != 0
    combined = result.stdout + result.stderr
    assert "requires Python 3.12 or later" in combined
