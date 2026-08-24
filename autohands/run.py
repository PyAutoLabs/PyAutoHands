import sys
import yaml
from pathlib import Path

import build_util

from argparse import ArgumentParser


parser = ArgumentParser()

parser.add_argument("project", type=str, help="The project to build")
parser.add_argument("directory", type=str, help="The directory to build")
parser.add_argument(
    "--visualise",
    action="store_true",
    help="Only run notebooks for which we want to create visualisations",
)
parser.add_argument(
    "--report-dir",
    type=str,
    default=None,
    help="Directory to write structured JSON results to",
)
parser.add_argument(
    "--env-config",
    type=str,
    default=None,
    help="Path to profile_smoke.yaml for per-script environment configuration",
)
parser.add_argument(
    "--list",
    dest="list_file",
    type=str,
    default=None,
    help=(
        "Path to a notebook list (e.g. a workspace's smoke_notebooks.txt). Given, "
        "only the listed notebooks run, in the list's order (opt-in coverage); "
        "omitted, notebooks are discovered recursively under DIRECTORY (opt-out "
        "coverage). no_run.yaml applies either way."
    ),
)
parser.add_argument(
    "--no-write-back",
    action="store_true",
    help=(
        "Execute a throwaway copy so the committed notebooks are left untouched. "
        "What a PR smoke gate wants; the release/generation pipeline does not "
        "pass it, because there the executed outputs are the product."
    ),
)
parser.add_argument(
    "--retry-from",
    type=str,
    default=None,
    help=(
        "Scripts directory (e.g. 'scripts'). On a genuine failure the notebook "
        "is regenerated from its source .py and retried ONCE, recovering a stale "
        "notebook whose script moved on. Timeouts are never retried."
    ),
)

args = parser.parse_args()

project = args.project
directory = args.directory
visualise = args.visualise

WORKSPACE_BUILD_CONFIG = Path.cwd() / "config" / "build"

# Each workspace owns its build config in config/build/. There is no
# autohands-level fallback: the keyed-dict fallbacks were removed once every
# build target owned its own files, so a missing config is a workspace bug and
# is reported as one rather than silently resolving to someone else's rules.
no_run_path = WORKSPACE_BUILD_CONFIG / "no_run.yaml"
if not no_run_path.exists():
    raise FileNotFoundError(
        f"{no_run_path} not found. Every workspace must own its "
        f"config/build/no_run.yaml (an empty file is valid and skips nothing). "
        f"Run from the workspace root, not from PyAutoHands."
    )

with open(no_run_path) as f:
    no_run_list = yaml.safe_load(f) or []

if visualise:
    # A workspace with no visualise_notebooks.yaml has nothing marked for
    # visualisation; that is not an error, it just selects nothing.
    workspace_visualise = WORKSPACE_BUILD_CONFIG / "visualise_notebooks.yaml"
    if workspace_visualise.exists():
        with open(workspace_visualise) as f:
            visualise_dict = yaml.safe_load(f) or []
    else:
        print(
            f"--visualise: no {workspace_visualise} in this workspace; "
            f"no notebooks are marked for visualisation."
        )
        visualise_dict = []
else:
    visualise_dict = None

# smoke profile: explicit flag > workspace config/build/profile_smoke.yaml > none
env_config_path = None
if args.env_config:
    env_config_path = Path(args.env_config)
else:
    from env_config import find_profile
    env_config_path = find_profile(WORKSPACE_BUILD_CONFIG, "smoke")

if __name__ == "__main__":
    report = None
    skip_reasons = None

    if args.report_dir:
        from result_collector import RunReport, parse_no_run_reasons

        report = RunReport(
            project=project,
            directory=directory,
            run_type="notebook",
        )
        skip_reasons = parse_no_run_reasons(no_run_path, project)

    env_config = None
    if env_config_path:
        from env_config import load_env_config
        env_config = load_env_config(env_config_path)

    files = None
    if args.list_file:
        try:
            files = build_util.files_from_list(directory, args.list_file)
        except FileNotFoundError as e:
            # A missing list is a configuration error, not a notebook failure.
            # Running nothing and exiting 0 would be a vacuously green gate.
            print(f"ERROR: {e}", file=sys.stderr)
            sys.exit(1)

    build_util.execute_notebooks_in_folder(
        no_run_list=no_run_list,
        visualise_dict=visualise_dict,
        directory=directory,
        report=report,
        skip_reasons=skip_reasons,
        env_config=env_config,
        files=files,
        write_back=not args.no_write_back,
        retry_from_scripts=args.retry_from,
    )

    if report is not None:
        report_path = report.write(Path(args.report_dir))
        print(f"Results written to {report_path}")
        if report.has_failures:
            sys.exit(1)
