"""
Build (and optionally publish) the sub-floor *tombstone* releases that stop pip
silently installing a stale PyAuto stack on an unsupported Python.

The problem
-----------

Raising `requires-python` does not retract anything. `2026.7.29.2` was the first
release published with `Requires-Python >=3.12`; every release at or below
`2026.7.29.1` was published with `>=3.9`, and PyPI metadata is immutable, so
those releases remain valid pip candidates forever. On Python 3.9, 3.10 and 3.11
`pip install autolens` therefore does not fail — it backtracks to `2026.7.29.1`
and installs the whole stack silently, with no JAX and no warning:

    py3.9   -> autolens 2026.7.29.1   (exit 0, no warning)
    py3.10  -> autolens 2026.7.29.1   (exit 0, no warning)
    py3.11  -> autolens 2026.7.29.1   (exit 0, no warning)
    py3.12  -> autolens 2026.8.17.1   (current)

A quietly stale install is worse than a hard failure: nothing tells the user
which version they are actually running, and every bug they report is against
code that moved on weeks ago.

The mechanism
-------------

Publish one extra release per package — `TOMBSTONE_VERSION`, sdist-only, with
`Requires-Python <3.12` — whose build raises `RuntimeError` with an explanation.
Because its version sorts *above* the last permissive release and its
`Requires-Python` excludes every supported Python, it becomes the highest
candidate pip can see below the floor, and is invisible at or above it:

    py3.10  -> tombstone selected -> build raises -> loud, explanatory failure
    py3.12  -> tombstone excluded by Requires-Python -> latest release, unchanged

This is a **one-off publish, not part of the release pipeline**. The tombstone
never needs republishing: future releases all declare `>=3.12`, so they are
invisible below the floor and the tombstone stays the top sub-floor candidate
indefinitely. Do not wire this module into `release.yml` — doing so would
republish a deliberately-broken artifact on every release.

Two properties this deliberately preserves
------------------------------------------

- **Pinned historical installs still work.** `pip install autolens==2026.7.29.1`
  on 3.10 still resolves, because an exact pin excludes the tombstone version.
  Reproducing an old result is not collateral damage of this change.
- **Supported Pythons are untouched.** Resolution at 3.12+ is byte-for-byte
  identical, since the tombstone fails the `Requires-Python` check before the
  resolver ever considers it.

The one hole, stated rather than hidden
---------------------------------------

`pip install --only-binary=:all: autolens` on 3.10 skips sdists entirely, so it
steps over the tombstone and installs the `2026.7.29.1` wheel silently, exactly
as before. There is no packaging mechanism that closes this: the fix would
require retracting the back catalogue, and yanking ~330 releases per package is
both semantically wrong and impossible in bulk (PyPI exposes no yank API). It is
documented in the install docs rather than pretended away.

All five packages need a tombstone. The libraries pin each other exactly
(`autogalaxy==<version>`), so tombstoning `autolens` alone still leaves
`pip install autogalaxy` backtracking on its own.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tarfile
from pathlib import Path

# The five packages that make up the installable stack. All of them are
# required: the exact `==` inter-pins mean a gap in this list is a hole a user
# can still fall through by installing that package directly.
TOMBSTONE_PACKAGES = (
    "autonerves",
    "autoarray",
    "autofit",
    "autogalaxy",
    "autolens",
)

# One `.post` above the last release published with `Requires-Python >=3.9`,
# so it outranks every sub-floor candidate. It stays below `2026.8.4.1`, so
# PyPI's displayed "latest version" is unaffected.
LAST_PERMISSIVE_VERSION = "2026.7.29.1"
TOMBSTONE_VERSION = f"{LAST_PERMISSIVE_VERSION}.post1"

# The floor the published stack actually declares. Kept as a tuple so the
# generated guard and the `Requires-Python` bound cannot drift apart.
PYTHON_FLOOR = (3, 12)

SETUP_PY_TEMPLATE = '''\
"""Tombstone release for {package} — see the RuntimeError below.

This distribution contains no code. It exists so that `pip install {package}`
on a Python older than {floor_str} fails with an explanation, instead of
silently backtracking to a {last_version} release that predates the
Python {floor_str} floor.
"""

import sys

from setuptools import setup

FLOOR = {floor!r}

if sys.version_info < FLOOR:
    raise RuntimeError(
        "\\n\\n"
        "  {package} requires Python {floor_str} or later — you are running "
        "Python %d.%d.\\n"
        "\\n"
        "  Nothing is broken with your pip. This release exists only to stop pip\\n"
        "  quietly installing a version of {package} that predates the Python\\n"
        "  {floor_str} floor.\\n"
        "  Releases at or below {last_version} still declare Python >=3.9 and remain\\n"
        "  installable, but they are unsupported, months out of date, and ship\\n"
        "  without JAX.\\n"
        "\\n"
        "  Upgrade to Python {floor_str} or later, then reinstall:\\n"
        "\\n"
        "      python{floor_str} -m pip install {package}\\n"
        "\\n"
        "  If you meant to install a historical release, pin it exactly and it\\n"
        "  will still resolve on this Python:\\n"
        "\\n"
        "      pip install {package}=={last_version}\\n"
        % (sys.version_info[0], sys.version_info[1])
    )

setup(
    name="{package}",
    version="{version}",
    description=(
        "Tombstone release: {package} requires Python {floor_str} or later."
    ),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    python_requires="<{floor_str}",
    py_modules=[],
)
'''

README_TEMPLATE = """\
# {package} {version} — tombstone release

**This release contains no code and cannot be installed.** Installing it raises
an error telling you to upgrade Python.

`{package}` requires **Python {floor_str} or later**. Releases at or below
`{last_version}` were published declaring `Requires-Python >=3.9`, and PyPI
metadata is immutable, so they stay valid pip candidates forever. Without this
tombstone, `pip install {package}` on Python 3.9, 3.10 or 3.11 does not fail —
it silently backtracks to `{last_version}` and installs a stack that is months
out of date and ships without JAX, with no warning at all.

This release sorts above `{last_version}` and declares `Requires-Python
<{floor_str}`, so it is the first thing pip finds below the floor and is
invisible at or above it. The result is a clear error instead of a quietly
stale install.

## What to do

Upgrade to Python {floor_str} or later and reinstall:

```
python{floor_str} -m pip install {package}
```

To install a historical release deliberately, pin it exactly — that still
resolves on older Pythons:

```
pip install {package}=={last_version}
```
"""


def floor_str(floor: tuple[int, int] = PYTHON_FLOOR) -> str:
    """Render a version floor as `3.12`, for use in prose and metadata."""
    return ".".join(str(part) for part in floor)


def render_setup_py(
    package: str,
    version: str = TOMBSTONE_VERSION,
    floor: tuple[int, int] = PYTHON_FLOOR,
    last_version: str = LAST_PERMISSIVE_VERSION,
) -> str:
    """Render the guarded `setup.py` for one package's tombstone.

    The guard is conditional on `sys.version_info` rather than unconditional so
    that the sdist can still be *built* on a supported Python: `python -m build`
    executes this file, and an unconditional raise would make the tombstone
    impossible to produce.
    """
    return SETUP_PY_TEMPLATE.format(
        package=package,
        version=version,
        floor=floor,
        floor_str=floor_str(floor),
        last_version=last_version,
    )


def render_readme(
    package: str,
    version: str = TOMBSTONE_VERSION,
    floor: tuple[int, int] = PYTHON_FLOOR,
    last_version: str = LAST_PERMISSIVE_VERSION,
) -> str:
    """Render the long description shown on the release's PyPI page."""
    return README_TEMPLATE.format(
        package=package,
        version=version,
        floor_str=floor_str(floor),
        last_version=last_version,
    )


def write_project(
    package: str,
    dest: Path,
    version: str = TOMBSTONE_VERSION,
    floor: tuple[int, int] = PYTHON_FLOOR,
    last_version: str = LAST_PERMISSIVE_VERSION,
) -> Path:
    """Write the tombstone source tree for `package` under `dest`.

    Deliberately setup.py-only: no `pyproject.toml`. The guard has to run during
    metadata preparation, and a PEP 621 `[project]` table would let a backend
    answer metadata questions without ever executing the guard.
    """
    project_dir = dest / f"{package}-tombstone"
    if project_dir.exists():
        shutil.rmtree(project_dir)
    project_dir.mkdir(parents=True)

    (project_dir / "setup.py").write_text(
        render_setup_py(package, version=version, floor=floor, last_version=last_version)
    )
    (project_dir / "README.md").write_text(
        render_readme(package, version=version, floor=floor, last_version=last_version)
    )
    return project_dir


def build_sdist(
    project_dir: Path,
    out_dir: Path,
    package: str,
    version: str = TOMBSTONE_VERSION,
) -> Path:
    """Build the sdist for a written tombstone project and return its path.

    Runs with `--no-isolation` so the build cannot silently depend on network
    access; setuptools is the only requirement and is already present wherever
    this tool runs.

    The built artifact is located by its exact expected filename rather than by
    globbing the output directory: every package builds into the same `out_dir`,
    so "the newest tarball here" would happily hand back a sibling package's
    sdist and verify *its* metadata instead.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            sys.executable,
            "-m",
            "build",
            "--sdist",
            "--no-isolation",
            "--outdir",
            str(out_dir),
            str(project_dir),
        ],
        check=True,
    )
    sdist = out_dir / f"{package}-{version}.tar.gz"
    if not sdist.exists():
        raise RuntimeError(f"expected {sdist.name} in {out_dir}, but it was not built")
    return sdist


def sdist_requires_python(sdist: Path) -> str | None:
    """Read `Requires-Python` back out of a built sdist's PKG-INFO.

    Verifying the artifact rather than trusting the input is the whole point:
    a tombstone published with the wrong `Requires-Python` would either be
    invisible (never selected, silent backtrack continues) or visible on
    supported Pythons (breaking every working install).
    """
    with tarfile.open(sdist) as tar:
        for member in tar.getmembers():
            if Path(member.name).name == "PKG-INFO":
                handle = tar.extractfile(member)
                if handle is None:
                    continue
                for line in handle.read().decode().splitlines():
                    if line.startswith("Requires-Python:"):
                        return line.split(":", 1)[1].strip()
    return None


def build_all(out_dir: Path, packages=TOMBSTONE_PACKAGES, work_dir: Path | None = None):
    """Build every tombstone sdist, verifying each artifact's metadata."""
    work_dir = work_dir or out_dir / "src"
    work_dir.mkdir(parents=True, exist_ok=True)

    expected = f"<{floor_str()}"
    built = []
    for package in packages:
        project_dir = write_project(package, work_dir)
        sdist = build_sdist(project_dir, out_dir, package)
        found = sdist_requires_python(sdist)
        if found != expected:
            raise RuntimeError(
                f"{sdist.name}: Requires-Python is {found!r}, expected {expected!r} — "
                "refusing to hand over an artifact that would not behave as a tombstone"
            )
        built.append(sdist)
    return built


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.strip().splitlines()[0])
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("dist-tombstone"),
        help="directory to write the sdists into (default: dist-tombstone)",
    )
    parser.add_argument(
        "--package",
        action="append",
        choices=TOMBSTONE_PACKAGES,
        help="build only this package (repeatable); default is all five",
    )
    args = parser.parse_args(argv)

    packages = tuple(args.package) if args.package else TOMBSTONE_PACKAGES
    if set(packages) != set(TOMBSTONE_PACKAGES):
        print(
            "WARNING: building a subset. The libraries pin each other exactly, so a\n"
            "         package without a tombstone is still installable directly on an\n"
            "         unsupported Python.",
            file=sys.stderr,
        )

    built = build_all(args.out, packages=packages)
    print(f"\nBuilt {len(built)} tombstone sdist(s) in {args.out}:")
    for sdist in built:
        print(f"  {sdist.name}  Requires-Python {sdist_requires_python(sdist)}")
    print(
        "\nThese are deliberately broken artifacts. Upload is a separate, human\n"
        "authorized act — rehearse on TestPyPI first:\n"
        f"    python3 -m twine upload --repository testpypi {args.out}/*.tar.gz\n"
        f"    python3 -m twine upload {args.out}/*.tar.gz\n"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
