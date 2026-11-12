"""A release builds the commits that were rehearsed (M2.4, PyAutoHands#337).

On 2026-11-09 the rehearsal built one library at ``e2b05f004``; the release leg
re-checked-out ``main`` 100 minutes later and published ``6ae33d433``, four
commits the rehearsal never saw, and two downstream ``main`` branches went red
a minute later. Human ruling 2026-11-12: release exactly the rehearsed commits even if
``main`` moved; the library Colab bump moves off ``main``.

Two halves are held here:

- ``autohands/rehearsed_commits.py`` — the resolution and refusal logic, plus
  the post-checkout safeguard, exercised against real local git repos in which
  ``main`` moves ahead after the rehearsal;
- ``release.yml``'s shape — no library checkout reads ``main``; every one reads
  ``resolve_commits``; the rehearsal records what it built; the library Colab
  bump never pushes ``main``.
"""

import json
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

from autohands import rehearsed_commits as rc

ROOT = Path(__file__).resolve().parents[1]
RELEASE_WORKFLOW = ROOT / ".github" / "workflows" / "release.yml"
HELPER = ROOT / "autohands" / "rehearsed_commits.py"


def sha(c: str) -> str:
    return c * 40


# The library set comes from Build config (tenant firewall: no repo names in
# organ code, tests included) — pick libraries by position.
LIBS = rc.libraries()
REHEARSED = {lib: sha("0123456789ab"[i]) for i, lib in enumerate(LIBS)}


def write_record(records: Path, run_id: str, commit_shas=None, mode="rehearsal") -> None:
    d = records / run_id
    d.mkdir(parents=True)
    body = {"mode": mode, "index": "testpypi", "version": "2026.11.12.1.dev1", "run_id": run_id}
    if commit_shas is not None:
        body["commit_shas"] = commit_shas
    (d / "rehearsal.json").write_text(json.dumps(body))


# --------------------------------------------------------------------------
# Manifest parsing
# --------------------------------------------------------------------------


def test_blank_manifest_means_none_given():
    assert rc.parse_manifest("") is None
    assert rc.parse_manifest("   ") is None
    assert rc.parse_manifest(None) is None


def test_manifest_accepts_bare_and_wrapped_forms_and_ignores_extra_repos():
    bare = dict(REHEARSED, SomeOtherRepo=sha("f"))
    assert rc.parse_manifest(json.dumps(bare)) == REHEARSED
    assert rc.parse_manifest(json.dumps({"commit_shas": REHEARSED})) == REHEARSED


@pytest.mark.parametrize(
    "body, msg",
    [
        ("not json", "not valid JSON"),
        (json.dumps(["x"]), "expected a JSON object"),
        (json.dumps({k: v for k, v in REHEARSED.items() if k != LIBS[-1]}), f"no commit for {LIBS[-1]}"),
        (json.dumps(dict(REHEARSED, **{LIBS[2]: "e2b05f004"})), "not a full 40-character"),
    ],
)
def test_bad_manifests_refuse(body, msg):
    with pytest.raises(rc.Refused, match=msg):
        rc.parse_manifest(body)


# --------------------------------------------------------------------------
# Live resolution
# --------------------------------------------------------------------------


def test_named_rehearsal_is_the_authority(tmp_path):
    write_record(tmp_path, "111", REHEARSED)
    commits, record = rc.resolve_release(None, rc.load_records(tmp_path), "111")
    assert commits == REHEARSED
    assert record["source_run_id"] == "111"


def test_manifest_matching_the_named_record_releases_it(tmp_path):
    write_record(tmp_path, "111", REHEARSED)
    commits, _ = rc.resolve_release(dict(REHEARSED), rc.load_records(tmp_path), "111")
    assert commits == REHEARSED


def test_manifest_disagreeing_with_the_named_record_refuses_and_names_the_library(tmp_path):
    write_record(tmp_path, "111", REHEARSED)
    moved = dict(REHEARSED, **{LIBS[2]: sha("e")})
    with pytest.raises(rc.Refused, match="do not match the commit_shas manifest") as exc:
        rc.resolve_release(moved, rc.load_records(tmp_path), "111")
    assert LIBS[2] in str(exc.value)
    assert LIBS[1] not in str(exc.value)


def test_manifest_alone_finds_the_rehearsal_that_built_it(tmp_path):
    write_record(tmp_path, "100", dict(REHEARSED, **{LIBS[4]: sha("d")}))
    write_record(tmp_path, "111", REHEARSED)
    commits, record = rc.resolve_release(dict(REHEARSED), rc.load_records(tmp_path))
    assert commits == REHEARSED and record["source_run_id"] == "111"


def test_manifest_never_rehearsed_refuses(tmp_path):
    write_record(tmp_path, "111", REHEARSED)
    with pytest.raises(rc.Refused, match="never rehearsed"):
        rc.resolve_release(dict(REHEARSED, **{LIBS[0]: sha("c")}), rc.load_records(tmp_path))


def test_nothing_named_refuses():
    with pytest.raises(rc.Refused, match="no rehearsal named"):
        rc.resolve_release(None, [], None)
    with pytest.raises(rc.Refused, match="no rehearsal named"):
        rc.resolve_release(None, [], "  ")


def test_named_run_without_a_record_refuses(tmp_path):
    write_record(tmp_path, "111", REHEARSED)
    with pytest.raises(rc.Refused, match="no rehearsal record for run 222"):
        rc.resolve_release(None, rc.load_records(tmp_path), "222")


def test_record_from_before_337_without_commit_shas_refuses(tmp_path):
    write_record(tmp_path, "111", None)
    with pytest.raises(rc.Refused, match="carries the commits it built"):
        rc.resolve_release(None, rc.load_records(tmp_path), "111")


def test_non_rehearsal_artifacts_are_not_records(tmp_path):
    write_record(tmp_path, "111", REHEARSED, mode="live")
    assert rc.load_records(tmp_path) == []
    assert rc.load_records(tmp_path / "absent") == []


def test_directory_name_not_body_is_the_record_identity(tmp_path):
    """A record downloaded from run 111 is run 111's, whatever its body says."""
    write_record(tmp_path, "111", REHEARSED)
    body = json.loads((tmp_path / "111" / "rehearsal.json").read_text())
    body["run_id"] = "999"
    (tmp_path / "111" / "rehearsal.json").write_text(json.dumps(body))
    with pytest.raises(rc.Refused):
        rc.resolve_release(None, rc.load_records(tmp_path), "999")


# --------------------------------------------------------------------------
# Rehearsal pinning
# --------------------------------------------------------------------------


def test_rehearsal_uses_the_manifest_verbatim_when_given():
    assert rc.resolve_rehearsal(dict(REHEARSED), heads=lambda: pytest.fail("must not read main")) == REHEARSED


def test_library_set_is_the_release_matrix():
    """config/workspaces.yaml `libraries` and release.yml's matrices name one set."""
    for name in LIB_JOBS:
        paths = [p["path"] for p in jobs()[name]["strategy"]["matrix"]["project"]]
        assert tuple(paths) == LIBS, name


def test_rehearsal_pins_main_heads_once_otherwise():
    heads = rc.main_heads(ls_remote=lambda lib: REHEARSED[lib].upper() + "\n")
    assert heads == REHEARSED
    assert rc.resolve_rehearsal(None, heads=lambda: heads) == REHEARSED


def test_unreadable_main_head_refuses():
    with pytest.raises(rc.Refused, match="no commit for"):
        rc.main_heads(ls_remote=lambda lib: "")
    with pytest.raises(rc.Refused, match="no GitHub owner"):
        rc.main_heads(owner="")


# --------------------------------------------------------------------------
# Real git: main moves after the rehearsal
# --------------------------------------------------------------------------


def git(cwd, *args):
    return subprocess.run(
        ["git", "-C", str(cwd), *args], capture_output=True, text=True, check=True
    ).stdout.strip()


@pytest.fixture
def moved_library(tmp_path):
    """origin with a rehearsed commit, then two merges on main; a clone at the rehearsed sha."""
    origin = tmp_path / "origin"
    origin.mkdir()
    git(origin, "init", "-q", "-b", "main")
    git(origin, "config", "user.email", "t@example.com")
    git(origin, "config", "user.name", "t")
    (origin / "a.py").write_text("x = 1\n")
    git(origin, "add", "a.py")
    git(origin, "commit", "-q", "-m", "rehearsed")
    rehearsed = git(origin, "rev-parse", "HEAD")
    for i in (2, 3):
        (origin / "a.py").write_text(f"x = {i}\n")
        git(origin, "commit", "-q", "-am", f"merged after rehearsal {i}")
    clone = tmp_path / "clone"
    subprocess.run(["git", "clone", "-q", str(origin), str(clone)], check=True)
    git(clone, "checkout", "-q", rehearsed)
    return clone, rehearsed, git(origin, "rev-parse", "main")


def test_verify_accepts_the_rehearsed_commit_and_reports_main_moved(moved_library):
    clone, rehearsed, main = moved_library
    lines = rc.verify_checkout(clone, rehearsed)
    text = "\n".join(lines)
    assert f"rehearsed commit: {rehearsed}" in text
    assert "(identical)" in text
    assert main in text
    assert "main moved since rehearsal: 2 commit(s) ahead" in text


def test_verify_refuses_a_checkout_of_main(moved_library):
    clone, rehearsed, main = moved_library
    git(clone, "checkout", "-q", main)
    with pytest.raises(rc.Refused, match="rehearsed commit is"):
        rc.verify_checkout(clone, rehearsed)


def test_cli_release_then_verify_end_to_end(moved_library, tmp_path):
    """The workflow's two calls, as a subprocess: resolve, then verify."""
    clone, rehearsed, _ = moved_library
    recorded = dict(REHEARSED, **{LIBS[2]: rehearsed})
    records = tmp_path / "records"
    write_record(records, "111", recorded)
    out = tmp_path / "commit_shas.json"
    gh_output = tmp_path / "gh_output"
    # sys.executable: the CLI imports PyYAML for the library set.
    env = {"PATH": f"{Path(sys.executable).parent}:/usr/bin:/bin", "GITHUB_OUTPUT": str(gh_output)}

    r = subprocess.run(
        [sys.executable, str(HELPER), "release", "--records-dir", str(records),
         "--rehearsal-run-id", "111", "--out", str(out)],
        capture_output=True, text=True, env=env,
    )
    assert r.returncode == 0, r.stderr
    assert json.loads(out.read_text())[LIBS[2]] == rehearsed
    (line,) = gh_output.read_text().splitlines()
    assert line.startswith("commit_shas=") and json.loads(line.split("=", 1)[1]) == recorded

    v = subprocess.run(
        [sys.executable, str(HELPER), "verify", "--repo-dir", str(clone), "--expected", rehearsed],
        capture_output=True, text=True, env=env,
    )
    assert v.returncode == 0, v.stderr
    assert "main moved since rehearsal" in v.stdout

    refused = subprocess.run(
        [sys.executable, str(HELPER), "release", "--records-dir", str(tmp_path / "none")],
        capture_output=True, text=True, env=env,
    )
    assert refused.returncode == 1
    assert "REFUSED" in refused.stderr and "no rehearsal named" in refused.stderr


# --------------------------------------------------------------------------
# release.yml shape
# --------------------------------------------------------------------------

LIB_JOBS = ("release_test_pypi", "release")
RESOLVED_REF = "fromJSON(needs.resolve_commits.outputs.commit_shas)"


def workflow():
    return yaml.safe_load(RELEASE_WORKFLOW.read_text())


def jobs():
    return workflow()["jobs"]


def needs(job):
    n = job.get("needs", [])
    return [n] if isinstance(n, str) else n


def library_checkout(job):
    (step,) = [
        s for s in job["steps"]
        if str(s.get("uses", "")).startswith("actions/checkout")
        and "matrix.project.repository" in str(s.get("with", {}).get("repository", ""))
    ]
    return step


def test_dispatch_takes_the_rehearsal_inputs():
    inputs = workflow()[True]["workflow_dispatch"]["inputs"]  # `on:` parses as True
    assert {"rehearsal_run_id", "commit_shas"} <= set(inputs)
    assert inputs["rehearsal_run_id"]["required"] is False


def test_no_library_matrix_reads_main():
    for name in LIB_JOBS:
        job = jobs()[name]
        for project in job["strategy"]["matrix"]["project"]:
            assert "ref" not in project, (name, project)


def test_every_library_checkout_uses_the_resolved_commit():
    all_jobs = jobs()
    tp = all_jobs["release_test_pypi"]
    assert "resolve_commits" in needs(tp)
    assert RESOLVED_REF in library_checkout(tp)["with"]["ref"]

    rel = all_jobs["release"]
    assert "resolve_commits" in needs(rel)
    assert RESOLVED_REF in rel["env"]["REHEARSED_SHA"]
    assert library_checkout(rel)["with"]["ref"] == "${{ env.REHEARSED_SHA }}"


def test_release_verifies_before_tagging_and_confirms_identical_after():
    steps = jobs()["release"]["steps"]
    names = [s.get("name", "") for s in steps]
    verify = names.index("Confirm the checkout is the rehearsed commit")
    tag = names.index("Tag")
    build = names.index("Build")
    assert verify < tag < build
    assert "rehearsed_commits.py verify" in steps[verify]["run"]
    tag_run = steps[tag]["run"]
    assert '"$HEAD_SHA" != "$REHEARSED_SHA"' in tag_run
    assert tag_run.index("REHEARSED_SHA") < tag_run.index("git tag -m")
    assert "identical" in tag_run


def test_resolve_commits_runs_first_and_fetches_records_only_live():
    job = jobs()["resolve_commits"]
    assert needs(job) == ["resolve_mode"]
    assert job["permissions"]["actions"] == "read"
    fetch = [s for s in job["steps"] if s.get("name", "").startswith("Fetch rehearsal records")][0]
    assert "rehearsal != 'true'" in fetch["if"]
    assert "testpypi-rehearsal-version" in fetch["run"]
    assert '"$conclusion" != "success"' in fetch["run"]
    resolve = [s for s in job["steps"] if s.get("id") == "resolve"][0]["run"]
    assert "rehearsed_commits.py rehearsal" in resolve
    assert "rehearsed_commits.py release" in resolve
    # dispatch inputs reach the shell through env, never interpolated into it
    assert "github.event.inputs" not in resolve
    assert "github.event.inputs" not in fetch["run"]


def test_rehearsal_records_the_commits_it_built():
    job = jobs()["rehearsal_version"]
    assert "resolve_commits" in needs(job)
    (step,) = [s for s in job["steps"] if s.get("name", "").startswith("Record resolved")]
    assert step["env"]["COMMIT_SHAS"] == "${{ needs.resolve_commits.outputs.commit_shas }}"
    assert '"commit_shas": $COMMIT_SHAS' in step["run"]
    assert "json.tool" in step["run"]


def test_library_colab_bump_never_pushes_main():
    job = jobs()["bump_library_colab_urls"]
    assert "resolve_commits" in needs(job)
    checkout = [s for s in job["steps"] if s.get("name", "").startswith("Checkout library")][0]
    assert RESOLVED_REF in checkout["with"]["ref"]
    run = "\n".join(s.get("run", "") for s in job["steps"])
    assert "git push origin main" not in run
    assert 'git push origin "HEAD:refs/heads/$BRANCH"' in run
    assert 'BRANCH="release/$VERSION"' in run
