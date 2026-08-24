#!/usr/bin/env python

import sys
import yaml
from argparse import ArgumentParser
from pathlib import Path

import build_util

parser = ArgumentParser()
parser.add_argument("project", type=str, help="The project to run scripts for")
parser.add_argument("directory", type=str, help="The directory containing scripts")
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
        "Path to a script list (e.g. a workspace's smoke_tests.txt). Given, only "
        "the listed scripts run, in the list's order (opt-in coverage); omitted, "
        "scripts are discovered recursively under DIRECTORY (opt-out coverage). "
        "no_run.yaml applies either way."
    ),
)

args = parser.parse_args()

project = args.project
directory = args.directory

AUTOHANDS_CONFIG = Path(__file__).parent / "config"
WORKSPACE_BUILD_CONFIG = Path.cwd() / "config" / "build"

# no_run.yaml: prefer workspace config/build/, fall back to autohands config
no_run_path = WORKSPACE_BUILD_CONFIG / "no_run.yaml"
if not no_run_path.exists():
    no_run_path = AUTOHANDS_CONFIG / "no_run.yaml"

if no_run_path.exists():
    with open(no_run_path) as f:
        no_run_data = yaml.safe_load(f)
    # Support both flat list (workspace) and keyed dict (legacy autohands)
    if isinstance(no_run_data, dict):
        no_run_list = no_run_data.get(project, [])
    else:
        no_run_list = no_run_data or []
elif args.list_file:
    # With an explicit list the allowlist IS the policy, so there is nothing
    # for no_run.yaml to filter and its absence is not an error. Discovery
    # still requires it — without it "run everything under this directory"
    # has no exclusion policy at all.
    no_run_list = []
else:
    raise FileNotFoundError(
        f"{no_run_path} not found. A discovery run needs an exclusion policy; "
        f"pass --list to run an explicit set of scripts instead, or add "
        f"config/build/no_run.yaml (an empty file is valid and skips nothing)."
    )

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
            run_type="script",
            env_profile=(env_config_path.name if env_config_path else "none"),
        )
        # Only when the policy file exists: with an explicit list it may be
        # absent, and there are then no skip reasons to parse.
        skip_reasons = (
            parse_no_run_reasons(no_run_path, project)
            if no_run_path.exists()
            else {}
        )

    env_config = None
    if env_config_path:
        from env_config import load_env_config
        env_config = load_env_config(env_config_path)

    files = None
    if args.list_file:
        try:
            files = build_util.files_from_list(directory, args.list_file)
        except FileNotFoundError as e:
            # A missing list is a configuration error, not a script failure.
            # Running nothing and exiting 0 would be a vacuously green gate.
            print(f"ERROR: {e}", file=sys.stderr)
            sys.exit(1)

    build_util.execute_scripts_in_folder(
        no_run_list=no_run_list,
        directory=directory,
        report=report,
        skip_reasons=skip_reasons,
        env_config=env_config,
        files=files,
    )

    if report is not None:
        report_path = report.write(Path(args.report_dir))
        print(f"Results written to {report_path}")
        if report.has_failures:
            sys.exit(1)
