import datetime
import logging
import os
import re
import shutil
import signal
import subprocess
import sys
import tempfile
import time
import traceback
from pathlib import Path
from typing import List

TIMEOUT_SECS = int(os.environ.get("BUILD_SCRIPT_TIMEOUT", "300"))
BUILD_PATH = Path(__file__).parent

BUILD_PYTHON_INTERPRETER = os.environ.get("BUILD_PYTHON_INTERPRETER", "python3")

# Characters of captured child output kept from each stream when a run times
# out. A timed-out script is killed mid-flight, so its tail is the only clue to
# which block was executing — enough to name the block, not so much that a
# chatty script floods the report.
TIMEOUT_OUTPUT_TAIL_CHARS = 2000


def timeout_for(env=None) -> int:
    """Return the per-run timeout in seconds for a script or notebook.

    ``TIMEOUT_SECS`` is read once at import from the parent's own environment,
    so on its own it can only ever express ONE cap for a whole run. The
    per-script environment built by ``env_config.build_env_for_script`` is
    handed to the child, and a profile may set ``BUILD_SCRIPT_TIMEOUT`` on it
    for a matching pattern — but the ``run_capped(timeout=...)`` kill timer
    lives in the PARENT, so that value has no effect unless the parent reads it
    back out. This resolves it.

    Precedence (highest first):

    1. ``BUILD_SCRIPT_TIMEOUT`` on the per-script ``env`` (a profile override),
    2. ``TIMEOUT_SECS`` — the ambient/global value at import.

    A profile value deliberately wins over the ambient global. The alternative
    ("an explicitly supplied global always wins") is unimplementable here:
    ``run_all`` exports ``BUILD_SCRIPT_TIMEOUT`` unconditionally, even when 300
    was merely its CLI default, so the parent cannot tell an operator's
    deliberate cap from the default. Under that rule per-script budgets would
    work in CI (which does not go through ``run_all``) and be silently ignored
    locally — the exact silent-divergence class this function exists to remove.

    Malformed, zero or negative values fall back to ``TIMEOUT_SECS``: a bad
    profile entry must not disable the cap altogether.
    """
    if not env:
        return TIMEOUT_SECS
    raw = env.get("BUILD_SCRIPT_TIMEOUT")
    if raw is None:
        return TIMEOUT_SECS
    try:
        value = int(raw)
    except (TypeError, ValueError):
        return TIMEOUT_SECS
    return value if value > 0 else TIMEOUT_SECS


def _timeout_output(e: subprocess.TimeoutExpired) -> str:
    """Render the tail of a timed-out child's captured output.

    ``subprocess.TimeoutExpired`` carries whatever was captured before the kill,
    but only when the call captured it (``capture_output``/``stdout=PIPE``);
    otherwise both attributes are None and the child wrote straight to the
    console. Streams may be bytes or str depending on ``text=``.
    """

    def tail(stream) -> str:
        if not stream:
            return ""
        if isinstance(stream, bytes):
            stream = stream.decode("utf-8", errors="replace")
        stream = stream.strip()
        if len(stream) > TIMEOUT_OUTPUT_TAIL_CHARS:
            return "...[truncated]...\n" + stream[-TIMEOUT_OUTPUT_TAIL_CHARS:]
        return stream

    parts = []
    for label, stream in (("stdout", e.stdout), ("stderr", e.stderr)):
        text = tail(stream)
        if text:
            parts.append(f"--- last {label} before timeout ---\n{text}")
    return "\n".join(parts)



def kill_group(proc: subprocess.Popen) -> None:
    """SIGKILL the child's whole process group, tolerating an already-dead one.

    Public (unprefixed) because the workspace `run_smoke.py` runners import it
    rather than each growing a copy.
    """
    try:
        os.killpg(os.getpgid(proc.pid), signal.SIGKILL)
    except (ProcessLookupError, PermissionError):  # pragma: no cover - race
        proc.kill()


def run_capped(args, timeout, check=False, stdout=None, stderr=None,
               text=False, env=None, cwd=None) -> subprocess.CompletedProcess:
    """`subprocess.run`, but a timeout kills the child's whole process GROUP.

    A drop-in for the `subprocess.run(..., timeout=...)` calls this module used
    to make: same `TimeoutExpired` and `CalledProcessError`, carrying the same
    captured `output`/`stderr`, so every caller's handling is unchanged.

    The group is the point. `subprocess.run` kills only the direct child, so a
    grandchild -- a Popen'd helper, a multiprocessing worker, a compile server
    -- outlives the cap and keeps running, holding whatever memory and devices
    it had. Over a run of hundreds of scripts those accumulate against every
    script that follows. `start_new_session=True` puts the child in its own
    group, and killing the group takes its descendants with it.

    The same mechanism matters more for a runner that captures output without
    a cap at all: there the parent waits for the stdout pipe to reach EOF, and
    a grandchild holding that pipe open keeps the read blocked after the child
    itself has exited -- a script whose work has finished hangs the runner
    indefinitely. That shape is a workspace-side bug, not this module's, but
    the fix is this same group kill.
    """
    proc = subprocess.Popen(
        args,
        stdout=stdout,
        stderr=stderr,
        text=text,
        env=env,
        cwd=cwd,
        start_new_session=True,
    )
    try:
        output, errs = proc.communicate(timeout=timeout)
    except subprocess.TimeoutExpired:
        kill_group(proc)
        # The group is gone, so this drains whatever was buffered and returns.
        output, errs = proc.communicate()
        raise subprocess.TimeoutExpired(
            args, timeout, output=output, stderr=errs
        ) from None
    except BaseException:
        # Matches subprocess.run's context manager: never leave the child (or
        # its group) running when the caller is unwinding, e.g. on Ctrl-C.
        kill_group(proc)
        proc.wait()
        raise
    if check and proc.returncode != 0:
        raise subprocess.CalledProcessError(
            proc.returncode, args, output=output, stderr=errs
        )
    return subprocess.CompletedProcess(args, proc.returncode, output, errs)


def py_to_notebook(filename: Path):
    subprocess.run(
        ["python3", f"{BUILD_PATH}/add_notebook_quotes.py", filename, "temp.py"],
        check=True,
    )
    new_filename = filename.with_suffix(".ipynb")
    subprocess.run(
        ["ipynb-py-convert", "temp.py", new_filename],
        check=True,
    )
    os.remove("temp.py")
    uncomment_jupyter_magic(new_filename)
    return new_filename


# Projects whose generated notebooks receive the Colab setup cell, mapped to
# the public package through which local users access ``setup_colab``. The keys
# must stay in sync with the `_PROJECTS` registry in PyAutoNerves's
# `autonerves/setup_colab.py`.
COLAB_PROJECTS = {
    "autofit": "autofit",
    "autogalaxy": "autogalaxy",
    "autolens": "autolens",
    "howtofit": "autofit",
    "howtogalaxy": "autogalaxy",
    "howtolens": "autolens",
}

COLAB_SETUP_MARKDOWN = """__Google Colab Setup__

This cell sets up the environment when the notebook is run on Google Colab: it installs the
required PyAuto packages, clones the workspace (configuration files and example datasets) and
points the configuration at it. If you are running the notebook elsewhere (e.g. locally via
your own installation) it does nothing, and you can run it safely.

Colab tip: model-fits run much faster on a GPU — enable one via "Runtime" -> "Change runtime
type" -> "Hardware accelerator" before running the notebook."""

COLAB_SETUP_CODE = '''try:
    import google.colab
except ImportError:
    from {package} import setup_colab as _setup_colab
else:
    import importlib
    import subprocess
    import sys

    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "autonerves", "--no-deps"]
    )
    _setup_colab = importlib.import_module("autonerves.setup_colab")

_setup_colab.setup("{project}")'''


def inject_colab_setup(notebook_path, project: str):
    """
    Prepend the standard Google Colab setup cell pair (markdown explainer +
    code cell) to a generated notebook, so every published notebook can
    bootstrap itself on Colab.

    The cells are inserted after the notebook's leading markdown cell (the
    script's intro docstring) so the title stays on top. Notebooks whose
    source already calls ``setup_colab`` (hand-written setup sections) are
    left untouched. Returns True if cells were injected.
    """
    import json

    if project not in COLAB_PROJECTS:
        raise ValueError(
            f"inject_colab_setup: unknown project '{project}' — add it to "
            f"COLAB_PROJECTS here and to the _PROJECTS registry in "
            f"PyAutoNerves's autonerves/setup_colab.py. Known: {sorted(COLAB_PROJECTS)}"
        )

    with open(notebook_path, "r") as f:
        notebook = json.load(f)

    cells = notebook["cells"]

    for cell in cells:
        if "setup_colab" in "".join(cell.get("source", [])):
            return False

    markdown_cell = {
        "cell_type": "markdown",
        "metadata": {},
        "source": COLAB_SETUP_MARKDOWN.splitlines(keepends=True),
    }
    code_cell = {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": COLAB_SETUP_CODE.format(
            project=project, package=COLAB_PROJECTS[project]
        ).splitlines(keepends=True),
    }

    insert_at = 1 if cells and cells[0]["cell_type"] == "markdown" else 0
    cells[insert_at:insert_at] = [markdown_cell, code_cell]

    with open(notebook_path, "w") as f:
        json.dump(notebook, f, indent=1)

    return True


def uncomment_jupyter_magic(f):
    with open(f, "r") as sources:
        lines = sources.readlines()
    with open(f, "w") as sources:
        for line in lines:
            line = re.sub(
                r"# from (auto\w+) import setup_notebook; setup_notebook\(\)",
                r"from \1 import setup_notebook; setup_notebook()",
                line,
            )
            sources.write(line)


def no_run_list_with_extension_from(no_run_list: List[str], extension: str):
    for i, no_run in enumerate(no_run_list):
        if not no_run.endswith(extension):
            no_run_list[i] = f"{no_run}{extension}"

    return no_run_list


def should_skip(file: Path, no_run_list: List[str]) -> bool:
    """
    Return True if the file matches any entry in no_run_list.

    Entries with a '/' are treated as path-specific patterns and are
    substring-matched against the file's full path **including extension** —
    so a pattern may include ``.py`` to anchor against the script form (e.g.
    ``imaging/visualization.py`` matches ``scripts/imaging/visualization.py``
    but not ``scripts/imaging/visualization_jax.py``).
    Entries without a '/' match any file whose stem equals the entry.
    """
    file_str = str(file)
    for pattern in no_run_list:
        if "/" in pattern:
            if pattern in file_str:
                return True
        else:
            if file.stem == pattern:
                return True
    return False


def _find_skip_reason(file: Path, no_run_list: List[str], skip_reasons: dict) -> str:
    """Find the reason a file is being skipped from the skip_reasons dict."""
    file_str = str(file)
    for pattern in no_run_list:
        if "/" in pattern:
            if pattern in file_str:
                return skip_reasons.get(pattern, "No reason documented")
        else:
            if file.stem == pattern:
                return skip_reasons.get(pattern, "No reason documented")
    return "No reason documented"


_ANSI_ESCAPE_RE = re.compile(r"\x1b\[[0-9;]*m")
_SKIP_EXIT_RE = re.compile(r"^SystemExit\s*:\s*0$")


def is_clean_skip_exit(output: str) -> bool:
    """
    Return True when a notebook run failed *only* because a cell called
    ``sys.exit(0)`` — the workspace optional-dependency skip idiom:

        if importlib.util.find_spec("<optional-dep>") is None:
            print("Skipping ...")
            sys.exit(0)

    As a ``.py`` script that is a clean exit 0. Under Jupyter the same call
    raises ``SystemExit`` in the kernel, nbclient marks the cell as errored and
    ``jupyter nbconvert --execute`` exits non-zero — so an intentional skip is
    reported as a failure. CI never sees it (its matrices install the optional
    extras), but any user or local run without them does.

    ``output`` is the combined stdout/stderr of the ``jupyter nbconvert`` run.
    nbclient aborts at the *first* erroring cell, so its ``CellExecutionError``
    message ends with that one cell's terminal ``<ename>: <evalue>`` line. We
    therefore require the last non-empty line after the ``CellExecutionError``
    marker to be exactly ``SystemExit: 0``: a non-zero ``sys.exit`` renders as
    ``SystemExit: 1`` and any other error renders as its own ename, so both
    stay failures. The traceback is ANSI-coloured by IPython, so escapes are
    stripped before matching.
    """
    if not output:
        return False
    plain = _ANSI_ESCAPE_RE.sub("", output)
    idx = plain.rfind("CellExecutionError")
    if idx == -1:
        return False
    tail = [line.strip() for line in plain[idx:].splitlines() if line.strip()]
    return bool(tail) and _SKIP_EXIT_RE.match(tail[-1]) is not None


def regenerate_notebook(nb_path, scripts_dir) -> Path:
    """
    Regenerate one notebook from its source ``.py`` into a temp dir.

    The recovery for a *stale* notebook: the script moved on but the committed
    ``.ipynb`` was never refreshed by ``generate.py``. Whole-workspace
    regeneration stays ``generate.py``'s job — this regenerates only the single
    notebook in front of the runner, so the recovery is cheap.

    The regenerated copy lives in a temp dir; the committed ``notebooks/`` tree
    is never touched, so a smoke run leaves the worktree clean.

    Parameters
    ----------
    nb_path
        The notebook that failed, e.g. ``notebooks/imaging/model_fit.ipynb``.
    scripts_dir
        The directory holding the source scripts, e.g. ``<workspace>/scripts``.
        The source is looked up at the notebook's path relative to its own
        ``notebooks/`` root, with a ``.py`` suffix.

    Returns
    -------
    The path to the regenerated notebook.

    Raises
    ------
    FileNotFoundError
        If no source script exists — nothing to regenerate from.
    """
    nb_path = Path(nb_path)
    scripts_dir = Path(scripts_dir)
    script_path = scripts_dir / Path(nb_path.name).with_suffix(".py")
    if not script_path.exists():
        raise FileNotFoundError(f"No source script at {script_path}")

    tmp_dir = Path(tempfile.mkdtemp(prefix="smoke_regen_"))
    tmp_script = tmp_dir / script_path.name
    shutil.copy(script_path, tmp_script)
    old_cwd = os.getcwd()
    try:
        os.chdir(tmp_dir)
        return Path(py_to_notebook(tmp_script))
    finally:
        os.chdir(old_cwd)


def _run_notebook_once(f, report=None, env=None, recorded=None, write_back=True):
    """
    Run one notebook once and classify the outcome.

    Returns ``"passed"``, ``"failed"`` or ``"timeout"`` so the caller can decide
    whether a retry is warranted; results are still appended to ``report`` here,
    under ``recorded`` (which may differ from ``f`` when a regenerated temp copy
    is standing in for the committed notebook).
    """
    print(f"Running <{f}> at {datetime.datetime.now().isoformat()}")

    timeout_secs = timeout_for(env)
    recorded = str(recorded if recorded is not None else f)

    run_target = Path(f)
    scratch_dir = None
    if not write_back:
        # run_notebook.py writes the executed notebook back in place, so point
        # it at a throwaway copy to leave the committed tree clean. The kernel's
        # cwd is pinned to the repo root either way, so relative dataset/ and
        # output/ paths resolve identically.
        scratch_dir = Path(tempfile.mkdtemp(prefix="smoke_nb_"))
        run_target = scratch_dir / Path(f).name
        shutil.copyfile(f, run_target)

    try:
        return _classify_notebook_run(run_target, recorded, report, env, timeout_secs)
    finally:
        if scratch_dir is not None:
            shutil.rmtree(scratch_dir, ignore_errors=True)


def _classify_notebook_run(run_target, recorded, report, env, timeout_secs):
    start = time.time()
    try:
        # stderr is always captured so a clean `sys.exit(0)` skip guard can be
        # told apart from a genuine cell failure (is_clean_skip_exit); stdout
        # keeps streaming live unless the report collector wants it.
        # Run via run_notebook.py rather than `jupyter nbconvert --execute`:
        # nbconvert starts the kernel in the notebook's own directory, but the
        # workspaces document (and their auto-simulate guards require) execution
        # from the repo root. nbconvert has no CLI flag for the kernel cwd, so
        # the runner sets resources['metadata']['path'] via the Python API.
        # Still a subprocess, so isolation/timeout/env are unchanged.
        #
        # It is invoked through sys.executable, NOT a bare `jupyter` binary, so
        # a missing notebook toolchain surfaces as an ordinary non-zero exit
        # (one FAIL, run continues) rather than a FileNotFoundError escaping and
        # aborting the whole run with no summary line.
        run_capped(
            [
                sys.executable,
                str(Path(__file__).parent / "run_notebook.py"),
                str(run_target),
                str(Path.cwd()),
            ],
            check=True,
            timeout=timeout_secs,
            stdout=subprocess.PIPE if report is not None else None,
            stderr=subprocess.PIPE,
            text=True,
            env=env,
        )
    except subprocess.TimeoutExpired as e:
        duration = time.time() - start
        if report is not None:
            from result_collector import ScriptResult, Status
            print(f"  TIMEOUT ({duration:.0f}s)")
            # Same reasoning as execute_script: stderr is always piped here, so
            # the failing cell's tail survives the kill and reaches the report.
            message = "Timed out after {:.0f}s (cap {}s)".format(duration, timeout_secs)
            captured = _timeout_output(e)
            if captured:
                message = f"{message}\n{captured}"
            report.results.append(ScriptResult(
                file=recorded,
                status=Status.TIMEOUT,
                duration_seconds=duration,
                error_message=message,
            ))
            return "timeout"
        logging.exception(e)
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        duration = time.time() - start
        captured = (getattr(e, "stdout", "") or "") + (getattr(e, "stderr", "") or "")

        if is_clean_skip_exit(captured):
            # An optional-dependency skip guard fired: `.py` semantics are a
            # clean exit 0, so the notebook form is a PASS too.
            if report is not None:
                from result_collector import ScriptResult, Status
                print(f"  PASS (skipped via sys.exit(0), {duration:.1f}s)")
                report.results.append(ScriptResult(
                    file=recorded,
                    status=Status.PASSED,
                    duration_seconds=duration,
                    error_message="sys.exit(0) skip guard (ignored)",
                ))
            else:
                print(f"  PASS (skipped via sys.exit(0), {duration:.1f}s)")
            return "passed"

        if "InversionException" in traceback.format_exc():
            if report is not None:
                from result_collector import ScriptResult, Status
                print(f"  PASS (InversionException, {duration:.1f}s)")
                report.results.append(ScriptResult(
                    file=recorded,
                    status=Status.PASSED,
                    duration_seconds=duration,
                    error_message="InversionException (ignored)",
                ))
            return "passed"

        if report is not None:
            from result_collector import ScriptResult, Status
            stderr = getattr(e, 'stderr', '') or ''
            last_line = stderr.strip().splitlines()[-1] if stderr.strip() else str(e)
            print(f"  FAIL ({duration:.1f}s) {last_line}")
            report.results.append(ScriptResult(
                file=recorded,
                status=Status.FAILED,
                duration_seconds=duration,
                error_message=str(e),
                traceback=stderr,
            ))
            return "failed"
        # stderr is captured now (see the subprocess call above), so echo it
        # before dying or the failure would be silent.
        if captured:
            print(captured, file=sys.stderr)
        logging.exception(e)
        sys.exit(1)

    duration = time.time() - start
    if report is not None:
        from result_collector import ScriptResult, Status
        print(f"  PASS ({duration:.1f}s)")
        report.results.append(ScriptResult(
            file=recorded,
            status=Status.PASSED,
            duration_seconds=duration,
        ))
    return "passed"


def execute_notebook(f, report=None, env=None, write_back=True,
                     retry_from_scripts=None, report_as=None):
    """
    Execute one notebook as a subprocess, with the kernel cwd at the repo root.

    ``write_back`` controls whether the notebook keeps its executed outputs.
    True (the default) is the generation/release contract: ``run_notebook.py``
    writes back in place, matching ``nbconvert --output <f> <f>``, so a
    partially-executed notebook keeps its outputs and generated notebooks are
    committed with them. False executes a throwaway copy and leaves the
    committed tree untouched — what a **PR smoke gate** needs, since dirtying
    ``notebooks/`` on every run would have the gate mutate the tree it is
    testing.

    ``retry_from_scripts``, set to a workspace's ``scripts`` directory, turns a
    genuine failure into one regenerate-and-retry: the notebook is rebuilt from
    its source ``.py`` (:func:`regenerate_notebook`) and run once more. This
    catches a *stale* notebook — the script moved on but the committed
    ``.ipynb`` was never refreshed by ``generate.py``. Deliberately narrow:

    * a TIMEOUT is never retried — it would burn a second full cap to reach the
      same result, doubling the slowest entry's cost;
    * a clean skip-guard exit is already a PASS and never reaches the retry;
    * the retry's verdict REPLACES the first attempt's, so one notebook
      contributes exactly one result.

    ``report_as`` is the path recorded in the report, defaulting to ``f``; the
    retry passes the original notebook so a temp path never leaks into results.

    Returns ``"passed"``, ``"failed"`` or ``"timeout"``.
    """
    recorded = report_as if report_as is not None else f
    mark = len(report.results) if report is not None else None

    status = _run_notebook_once(
        f, report=report, env=env, recorded=recorded, write_back=write_back
    )
    if status != "failed" or retry_from_scripts is None:
        return status

    print("  notebook failed; regenerating from source script and retrying...")
    try:
        regenerated = regenerate_notebook(f, retry_from_scripts)
    except Exception as exc:
        # No source script, or generation itself failed. The first attempt's
        # FAIL stands — the recovery was unavailable, not the notebook fixed.
        print(f"  [regenerate_notebook] {exc}")
        return status

    if report is not None:
        # Drop the first attempt so the retry's verdict is the only one recorded.
        del report.results[mark:]
    # The regenerated notebook is already a throwaway in /tmp, so writing its
    # outputs back costs nothing and touches no committed file.
    return _run_notebook_once(
        regenerated, report=report, env=env, recorded=recorded, write_back=True
    )



def execute_notebooks_in_folder(
    directory,
    no_run_list,
    visualise_dict=None,
    report=None,
    skip_reasons=None,
    env_config=None,
    files=None,
    write_back=True,
    retry_from_scripts=None,
):
    """
    Run the notebooks under ``directory``, honouring ``no_run_list``.

    ``files`` selects the discovery model, mirroring
    :func:`execute_scripts_in_folder`: omitted, notebooks are discovered
    recursively (opt-out coverage); supplied by :func:`files_from_list`, exactly
    those entries run in that order (opt-in). ``no_run_list`` applies either way
    and wins over the list.

    ``write_back`` and ``retry_from_scripts`` are passed through to
    :func:`execute_notebook`; a PR smoke gate wants ``write_back=False`` (leave
    the committed tree clean) plus the workspace's ``scripts`` directory for the
    stale-notebook recovery.
    """
    # Infrastructure files — always skip, never report
    infra_skip = ["__init__", "README"]
    no_run_list.extend(infra_skip)

    if files is None:
        files = sorted((Path.cwd() / directory).rglob("*.ipynb"))
        print(f"Found {len(files)} notebooks")
    else:
        print(f"Running {len(files)} listed notebooks")

    for file in files:
        if file.stem in infra_skip:
            continue
        if visualise_dict is not None:
            without_suffix = str(file.with_suffix(""))
            if not any(
                map(
                    without_suffix.endswith,
                    visualise_dict,
                )
            ):
                continue
        if should_skip(file, no_run_list):
            # Before the existence check, for the same reason as the script
            # runner: an excluded notebook that has also been deleted is still
            # excluded, and a failure would contradict the exclusion.
            if report is not None:
                from result_collector import ScriptResult, Status
                reason = _find_skip_reason(file, no_run_list, skip_reasons or {})
                report.results.append(ScriptResult(
                    file=str(file),
                    status=Status.SKIPPED,
                    skip_reason=reason,
                ))
        elif not file.exists():
            # Only reachable from an allowlist. One FAIL, run continues.
            print(f"  {file} ...  FAIL (listed but not found)")
            if report is not None:
                from result_collector import ScriptResult, Status
                report.results.append(ScriptResult(
                    file=str(file),
                    status=Status.FAILED,
                    error_message=f"Listed in the notebook list but not found at {file}",
                ))
            else:
                sys.exit(1)
        else:
            from env_config import build_env_for_script
            env = build_env_for_script(file, env_config)
            execute_notebook(
                file,
                report=report,
                env=env,
                write_back=write_back,
                retry_from_scripts=retry_from_scripts,
            )


def execute_script(f, report=None, env=None, extra_args=None):
    args = [BUILD_PYTHON_INTERPRETER, f]
    if extra_args:
        args.extend(extra_args)
    script_name = Path(f).relative_to(Path.cwd()) if Path(f).is_relative_to(Path.cwd()) else Path(f).name
    print(f"  {script_name} ...", end=" ", flush=True)

    timeout_secs = timeout_for(env)

    start = time.time()
    try:
        if report is not None:
            result = run_capped(
                args,
                check=True,
                timeout=timeout_secs,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                env=env,
            )
        else:
            run_capped(
                args,
                check=True,
                timeout=timeout_secs,
                env=env,
            )
    except subprocess.TimeoutExpired as e:
        duration = time.time() - start
        if report is not None:
            from result_collector import ScriptResult, Status
            print(f"  TIMEOUT ({duration:.0f}s)")
            # Keep the child's captured tail: a killed script never reports its
            # own progress, so without this a TIMEOUT cannot say WHICH block was
            # running and every diagnosis restarts from zero.
            message = "Timed out after {:.0f}s (cap {}s)".format(duration, timeout_secs)
            captured = _timeout_output(e)
            if captured:
                message = f"{message}\n{captured}"
            report.results.append(ScriptResult(
                file=str(f),
                status=Status.TIMEOUT,
                duration_seconds=duration,
                error_message=message,
            ))
            return
        logging.exception(e)
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        duration = time.time() - start

        if report is not None:
            from result_collector import ScriptResult, Status
            stderr = getattr(e, 'stderr', '') or ''
            # One-line console summary; full details go to the report file
            last_line = stderr.strip().splitlines()[-1] if stderr.strip() else str(e)
            print(f"  FAIL ({duration:.1f}s) {last_line}")
            report.results.append(ScriptResult(
                file=str(f),
                status=Status.FAILED,
                duration_seconds=duration,
                error_message=str(e),
                traceback=stderr,
            ))
            return
        logging.exception(e)
        sys.exit(1)

    duration = time.time() - start
    if report is not None:
        from result_collector import ScriptResult, Status
        print(f"  PASS ({duration:.1f}s)")
        report.results.append(ScriptResult(
            file=str(f),
            status=Status.PASSED,
            duration_seconds=duration,
        ))


def find_scripts_in_folder(directory: str) -> List[Path]:
    """
    Find all the Python scripts in a folder recursively.

    Order the scripts such that:
    - Any script with "simulator" in the path comes first
    - Any script named "start_here.py" comes next
    - Any other script comes last

    Parameters
    ----------
    directory
        The directory to search in

    Returns
    -------
    A list of paths to the scripts
    """
    files = list((Path.cwd() / directory).rglob("*.py"))
    return sorted(
        files,
        key=lambda f: (
            ("simulator" not in str(f), f.name != "start_here.py", str(f)),
            f,
        ),
    )


def files_from_list(directory: str, list_path) -> List[Path]:
    """
    Resolve an explicit allowlist of scripts to run, in the allowlist's own order.

    The opt-in counterpart to :func:`find_scripts_in_folder`. Blank lines and
    ``#`` comments are ignored; every other line is a path relative to
    ``directory``. Duplicated entries are collapsed to their first occurrence so
    a repeated line does not run the script twice.

    Order is the file's order, deliberately — NOT ``find_scripts_in_folder``'s
    simulator-first sort. An allowlist is hand-maintained, so its sequence is
    the author's statement of what must run before what, and re-sorting it would
    silently reorder a suite whose entries depend on an earlier one's output.

    Entries are returned whether or not they exist on disk; a missing one is
    reported per-entry by the caller rather than aborting the run.

    Parameters
    ----------
    directory
        The directory the allowlist's entries are relative to.
    list_path
        The allowlist file (e.g. a workspace's ``smoke_tests.txt``).

    Returns
    -------
    A list of paths to the scripts, in allowlist order.

    Raises
    ------
    FileNotFoundError
        If the allowlist file itself is missing. That is a configuration error,
        not a script failure: silently running nothing would be a vacuously
        green gate.
    """
    list_path = Path(list_path)
    if not list_path.exists():
        raise FileNotFoundError(f"no script list at {list_path}")

    root = Path.cwd() / directory
    files: List[Path] = []
    seen = set()
    for line in list_path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line in seen:
            continue
        seen.add(line)
        files.append(root / line)
    return files


def execute_scripts_in_folder(directory, no_run_list=None, report=None, skip_reasons=None, env_config=None, files=None):
    """
    Run the scripts under ``directory``, honouring ``no_run_list``.

    ``files`` selects the discovery model. Omitted (the default), scripts are
    discovered recursively under ``directory`` — coverage is opt-out, and
    excluding one is an entry in ``no_run.yaml``. Supplied (from
    :func:`files_from_list`), exactly those entries run, in that order —
    coverage is opt-in.

    ``no_run_list`` applies either way. An allowlisted script that is also
    ``no_run``-listed is SKIPPED with its documented reason: an explicit
    exclusion is the more specific statement of intent, and letting an
    allowlist override it would resurrect a script that was deliberately
    turned off.
    """
    no_run_list = no_run_list or []
    # Infrastructure files — always skip, never report
    infra_skip = ["__init__", "README"]
    no_run_list.extend(infra_skip)

    if files is None:
        files = find_scripts_in_folder(directory)
        print(f"Found {len(files)} scripts")
    else:
        print(f"Running {len(files)} listed scripts")

    for file in files:
        if file.stem in infra_skip:
            continue
        if should_skip(file, no_run_list):
            # Checked BEFORE existence: an excluded script that has also been
            # deleted is still excluded, and reporting it as a failure would
            # contradict the exclusion.
            if report is not None:
                from result_collector import ScriptResult, Status
                reason = _find_skip_reason(file, no_run_list, skip_reasons or {})
                report.results.append(ScriptResult(
                    file=str(file),
                    status=Status.SKIPPED,
                    skip_reason=reason,
                ))
        elif not file.exists():
            # Only reachable from an allowlist — discovery cannot yield a
            # missing path. Report it and carry on: the runner's contract is to
            # continue through failures, and a stale allowlist entry must not
            # cost coverage of every entry after it.
            print(f"  {file} ...  FAIL (listed but not found)")
            if report is not None:
                from result_collector import ScriptResult, Status
                report.results.append(ScriptResult(
                    file=str(file),
                    status=Status.FAILED,
                    error_message=f"Listed in the script list but not found at {file}",
                ))
            else:
                sys.exit(1)
        else:
            from env_config import build_env_for_script, args_for_script
            env = build_env_for_script(file, env_config)
            extra_args = args_for_script(file, env_config)
            execute_script(str(file), report=report, env=env, extra_args=extra_args)
