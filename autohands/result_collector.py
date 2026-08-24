import dataclasses
import datetime
import json
import os
import sys
from enum import Enum
from pathlib import Path
from typing import List, Optional

# The consolidated per-entry timing dataset written alongside every report.
#
# Why a second file rather than more keys on the per-run JSON: the per-run
# ``<project>__<dir>__<run_type>.json`` files are read by PyAutoHeart
# (``script_timing`` globs ``*__script.json``, ``test_run`` reads the
# aggregated ``report.json``) and by ``aggregate_results``. Their shape is a
# published interface, so the timing dataset is emitted beside them instead —
# one file per report DIRECTORY, merged across the legs that write into it, so
# a run's timings are a single artifact regardless of how many runner
# invocations produced them.
TIMINGS_FILENAME = "smoke_timings.json"
TIMINGS_SCHEMA = "smoke_timings/1"


class Status(str, Enum):
    PASSED = "passed"
    FAILED = "failed"
    SKIPPED = "skipped"
    TIMEOUT = "timeout"


def workspace_relative(path: str) -> str:
    """Render a recorded result path relative to the workspace root (cwd).

    The runners record absolute paths (``find_scripts_in_folder`` and
    ``files_from_list`` both build from ``Path.cwd()``). The timing dataset is
    compared ACROSS runs and machines, where an absolute path is noise and, on
    a GitHub runner, a different string every time. A path outside the
    workspace, or an already-relative one, is returned unchanged.
    """
    p = Path(path)
    if not p.is_absolute():
        return str(p)
    try:
        return str(p.relative_to(Path.cwd()))
    except ValueError:  # pragma: no cover - a path outside the workspace
        return str(p)


@dataclasses.dataclass
class ScriptResult:
    file: str
    status: Status
    duration_seconds: float = 0.0
    error_message: Optional[str] = None
    traceback: Optional[str] = None
    skip_reason: Optional[str] = None
    # The wall-clock cap that was in force for this entry, as resolved by
    # ``build_util.timeout_for`` at the execution site (a profile's
    # ``BUILD_SCRIPT_TIMEOUT`` override, else the ambient global). Only an
    # entry that actually entered an execution carries one, so ``None`` is the
    # marker for "never ran" — which is what keeps a skipped entry out of the
    # timing dataset instead of being recorded as a 0-second run.
    cap_seconds: Optional[float] = None
    # The child's exit status. ``None`` for a timeout (the process group was
    # killed, so there is no exit code the script chose) and for entries that
    # never ran.
    exit_code: Optional[int] = None

    @property
    def was_timed(self) -> bool:
        """True when this entry actually ran and its duration is a measurement.

        A SKIPPED entry never started, and a listed-but-missing entry fails
        before any execution — both carry ``duration_seconds == 0.0`` purely as
        the dataclass default. Recording those as "0 seconds" would put
        fabricated rows in a dataset whose whole purpose is timing, so they are
        emitted with a null duration instead.
        """
        if self.status == Status.SKIPPED:
            return False
        return self.cap_seconds is not None or self.duration_seconds > 0

    def to_timings_entry(self) -> dict:
        """One row of the timing dataset.

        ``seconds`` is the runner's OWN measurement — the same
        ``time.time()`` delta ``build_util`` prints on the ``PASS`` /
        ``TIMEOUT`` line — never re-derived from timestamps elsewhere.
        """
        path = workspace_relative(self.file)
        return {
            "entry": path,
            "kind": "notebook" if path.endswith(".ipynb") else "script",
            "status": self.status.value,
            "seconds": round(self.duration_seconds, 2) if self.was_timed else None,
            "cap_s": self.cap_seconds,
            "exit_code": self.exit_code,
        }

    def to_dict(self):
        # ``cap_seconds`` / ``exit_code`` are deliberately NOT emitted here.
        # This dict is the per-run JSON that PyAutoHeart's ``script_timing``
        # and ``test_run`` checks and ``aggregate_results`` read; it stays
        # byte-compatible, and the new fields reach consumers through
        # ``to_timings_entry`` instead.
        d = {
            "file": self.file,
            "status": self.status.value,
            "duration_seconds": round(self.duration_seconds, 2),
        }
        if self.error_message is not None:
            d["error_message"] = self.error_message
        if self.traceback is not None:
            # Keep last 100 lines to avoid bloating JSON
            lines = self.traceback.splitlines()
            d["traceback"] = "\n".join(lines[-100:])
        if self.skip_reason is not None:
            d["skip_reason"] = self.skip_reason
        return d


@dataclasses.dataclass
class RunReport:
    project: str
    directory: str
    run_type: str  # "script", "notebook", or "generate"
    # Which env profile the scripts actually ran under ("profile_smoke.yaml",
    # "profile_release.yaml", "none"). Recorded so a report states the surface
    # it measured — two runs are otherwise incomparable (PyAutoHeart#83 §5.3).
    env_profile: str = "unknown"
    results: List[ScriptResult] = dataclasses.field(default_factory=list)
    started_at: str = dataclasses.field(
        default_factory=lambda: datetime.datetime.now().isoformat()
    )
    completed_at: Optional[str] = None

    @property
    def summary(self):
        counts = {}
        for r in self.results:
            counts[r.status.value] = counts.get(r.status.value, 0) + 1
        return counts

    @property
    def total_duration_seconds(self) -> float:
        return round(sum(r.duration_seconds for r in self.results), 2)

    @property
    def has_failures(self):
        return any(
            r.status in (Status.FAILED, Status.TIMEOUT) for r in self.results
        )

    def to_dict(self):
        return {
            "project": self.project,
            "directory": self.directory,
            "run_type": self.run_type,
            "env_profile": self.env_profile,
            "started_at": self.started_at,
            "completed_at": self.completed_at,
            "summary": self.summary,
            "total_duration_seconds": self.total_duration_seconds,
            "results": [r.to_dict() for r in self.results],
        }

    def to_markdown(self) -> str:
        lines = [
            f"# Test Report: {self.project} / {self.directory} ({self.run_type})",
            "",
        ]

        s = self.summary
        total = sum(s.values())
        lines.append(f"**{total} scripts** | "
                      + " | ".join(f"{v} {k}" for k, v in sorted(s.items())))
        lines.append("")

        lines.append("| Status | Count |")
        lines.append("|--------|-------|")
        for status, count in sorted(s.items()):
            lines.append(f"| {status} | {count} |")
        lines.append("")

        failures = [r for r in self.results
                     if r.status in (Status.FAILED, Status.TIMEOUT)]
        if failures:
            lines.append("## Failures")
            lines.append("")
            for r in failures:
                duration = f"{r.duration_seconds:.1f}s" if r.duration_seconds else ""
                lines.append(f"### `{r.file}` — {r.status.value.upper()} ({duration})")
                lines.append("")
                if r.error_message:
                    lines.append(f"{r.error_message}")
                    lines.append("")
                if r.traceback:
                    tb_lines = r.traceback.strip().splitlines()[-20:]
                    lines.append("```")
                    lines.extend(tb_lines)
                    lines.append("```")
                    lines.append("")

        skipped = [r for r in self.results if r.status == Status.SKIPPED]
        if skipped:
            lines.append("## Skipped")
            lines.append("")
            lines.append("| Script | Reason |")
            lines.append("|--------|--------|")
            for r in skipped:
                name = Path(r.file).name
                reason = r.skip_reason or "No reason documented"
                lines.append(f"| `{name}` | {reason} |")
            lines.append("")

        passed = [r for r in self.results if r.status == Status.PASSED]
        if passed:
            lines.append("## Passed")
            lines.append("")
            for r in passed:
                duration = f"{r.duration_seconds:.1f}s" if r.duration_seconds else ""
                lines.append(f"- `{r.file}` ({duration})")
            lines.append("")

        return "\n".join(lines)

    # --- the timing dataset (one file per report dir) -------------------------

    def _leg(self) -> dict:
        """This report's identity within a shared report directory.

        A report dir can receive several runner invocations — the script leg
        and the notebook leg of one smoke gate, or every directory of every
        workspace in the ``run_all`` mega-run. Each is a *leg*, and the merged
        timing file records them all so the dataset states what produced it.
        """
        return {
            "project": self.project,
            "directory": self.directory,
            "run_type": self.run_type,
            "env_profile": self.env_profile,
            "ts": self.completed_at or self.started_at,
            "entries": len(self.results),
        }

    def to_timings(self) -> dict:
        """The timing dataset for THIS report, before merging."""
        return {
            "schema": TIMINGS_SCHEMA,
            "project": self.project,
            "directory": self.directory,
            "run_type": self.run_type,
            "env_profile": self.env_profile,
            "python": f"{sys.version_info.major}.{sys.version_info.minor}",
            "ts": self.completed_at or self.started_at,
            "entries": [r.to_timings_entry() for r in self.results],
            "legs": [self._leg()],
        }

    def merge_timings(self, existing: Optional[dict]) -> dict:
        """Fold this report's entries into an already-written timing dataset.

        The merge key is the workspace-relative entry path: the script leg and
        the notebook leg contribute disjoint paths, so both survive, while
        re-running the SAME leg replaces its own rows rather than duplicating
        them (a runner invoked twice into one report dir must not double-count).

        The top-level metadata describes the leg that wrote last; ``legs``
        carries every contributing leg, which is what a report dir spanning
        more than one project (the ``run_all`` mega-run) needs in order to be
        read back honestly.

        An unreadable or foreign file is replaced rather than merged — a
        corrupt sidecar must not take the run down or silently poison the
        dataset.
        """
        fresh = self.to_timings()
        if not isinstance(existing, dict) or existing.get("schema") != TIMINGS_SCHEMA:
            return fresh

        mine = {e["entry"] for e in fresh["entries"]}
        prior = [
            e
            for e in existing.get("entries", [])
            if isinstance(e, dict) and e.get("entry") not in mine
        ]
        fresh["entries"] = prior + fresh["entries"]

        def key(leg):
            return (leg.get("project"), leg.get("directory"), leg.get("run_type"))

        mine_key = key(self._leg())
        prior_legs = [
            leg
            for leg in existing.get("legs", [])
            if isinstance(leg, dict) and key(leg) != mine_key
        ]
        fresh["legs"] = prior_legs + fresh["legs"]
        return fresh

    def write_timings(self, output_dir: Path) -> Path:
        path = output_dir / TIMINGS_FILENAME
        existing = None
        if path.exists():
            try:
                existing = json.loads(path.read_text())
            except (json.JSONDecodeError, OSError, UnicodeDecodeError):
                existing = None
        with open(path, "w") as f:
            json.dump(self.merge_timings(existing), f, indent=2)
        return path

    def timings_markdown(self) -> str:
        """A slowest-first timing table for the GitHub Actions step summary.

        Only this report's own entries: the step summary is append-only, so a
        second leg adds its own table rather than restating the first's.
        """
        timed = [r for r in self.results if r.was_timed]
        untimed = [r for r in self.results if not r.was_timed]
        timed.sort(key=lambda r: r.duration_seconds, reverse=True)

        total = round(sum(r.duration_seconds for r in timed), 1)
        lines = [
            "",
            f"### Smoke timings — {self.project} / {self.directory} "
            f"({self.run_type}, Python "
            f"{sys.version_info.major}.{sys.version_info.minor})",
            "",
            "| Entry | Status | Seconds | Cap |",
            "|---|---|---:|---:|",
        ]
        for r in timed + untimed:
            entry = workspace_relative(r.file)
            seconds = f"{r.duration_seconds:.1f}" if r.was_timed else "—"
            # The cap is only informative where it BOUND the entry: on a
            # passing script it is the same number on every row and reads as
            # noise, while on a timeout it is the whole story.
            cap = (
                f"{r.cap_seconds:.0f}s"
                if r.status == Status.TIMEOUT and r.cap_seconds is not None
                else ""
            )
            lines.append(
                f"| `{entry}` | {r.status.value} | {seconds} | {cap} |"
            )
        lines.append("")
        count = len(self.results)
        lines.append(
            f"**{count} {'entry' if count == 1 else 'entries'}** | "
            f"{len(timed)} timed | {total}s total"
        )
        lines.append("")
        return "\n".join(lines)

    def append_step_summary(self) -> bool:
        """Append the timing table to ``$GITHUB_STEP_SUMMARY`` when in Actions.

        Returns False (and changes nothing) off CI, so a local run is
        byte-identical to before. A write failure is reported and swallowed:
        the summary is a convenience, and losing it must not fail a run whose
        scripts all passed.
        """
        target = os.environ.get("GITHUB_STEP_SUMMARY")
        if not target:
            return False
        try:
            with open(target, "a") as f:
                f.write(self.timings_markdown())
        except OSError as exc:
            print(f"  [smoke timings] step summary not written: {exc}")
            return False
        return True

    def write(self, output_dir: Path):
        self.completed_at = datetime.datetime.now().isoformat()
        output_dir.mkdir(parents=True, exist_ok=True)
        safe_dir = self.directory.replace("/", "__")
        base = f"{self.project}__{safe_dir}__{self.run_type}"

        json_path = output_dir / f"{base}.json"
        with open(json_path, "w") as f:
            json.dump(self.to_dict(), f, indent=2)

        md_path = output_dir / f"{base}.md"
        with open(md_path, "w") as f:
            f.write(self.to_markdown())

        # Every report contributes to the standing timing dataset, and to the
        # Actions step summary when there is one. Both legs (run_python.py and
        # run.py) reach this same call, so neither needs its own emission.
        self.write_timings(output_dir)
        self.append_step_summary()

        return json_path


def parse_no_run_reasons(yaml_path: Path, project: str) -> dict:
    """
    Parse no_run.yaml and extract pattern -> reason mappings.

    Since PyYAML strips comments, we parse the raw file line-by-line
    to capture the inline # reason comments.

    Supports both formats:
    - Flat list (workspace): every ``- entry`` line is relevant
    - Keyed dict (legacy autohands): only entries under the matching project key
    """
    reasons = {}
    has_project_keys = False
    in_project = False
    with open(yaml_path) as f:
        for line in f:
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            if stripped.endswith(":") and not stripped.startswith("-"):
                has_project_keys = True
                in_project = stripped.rstrip(":").strip() == project
                continue
            if stripped.startswith("- "):
                if has_project_keys and not in_project:
                    continue
                entry = stripped[2:]
                if "#" in entry:
                    pattern, reason = entry.split("#", 1)
                    reasons[pattern.strip()] = reason.strip()
                else:
                    reasons[entry.strip()] = "No reason documented"
    return reasons
