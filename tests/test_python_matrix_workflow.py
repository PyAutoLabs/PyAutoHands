from pathlib import Path

import yaml


WORKFLOW = (
    Path(__file__).resolve().parents[1] / ".github" / "workflows" / "python_matrix.yml"
)
AUTOHANDS = Path(__file__).resolve().parents[1] / "bin" / "autohands"


def load_workflow():
    return yaml.safe_load(WORKFLOW.read_text())


def test_required_matrices_cover_only_supported_python_versions():
    jobs = load_workflow()["jobs"]

    assert jobs["unit_tests"]["strategy"]["matrix"]["python-version"] == [
        "3.12",
        "3.13",
    ]
    assert jobs["smoke_tests"]["strategy"]["matrix"]["python-version"] == [
        "3.12",
        "3.13",
    ]


def test_python_314_is_isolated_and_non_required():
    jobs = load_workflow()["jobs"]
    experimental = jobs["experimental_python_314"]

    assert experimental["continue-on-error"] is True
    assert experimental["strategy"]["matrix"]["python-version"] == ["3.14"]
    assert len(experimental["strategy"]["matrix"]["project"]) == 5
    assert "experimental_python_314" in jobs["summary"]["needs"]
    assert "continue-on-error" not in jobs["unit_tests"]
    assert "continue-on-error" not in jobs["smoke_tests"]

    record_step = next(
        step for step in experimental["steps"]
        if step.get("name") == "Record experimental cell result"
    )
    assert record_step["if"] == "always()"
    assert "job.status" in record_step["run"]
    assert "does not cover workspace scripts" in record_step["run"]


def test_no_below_floor_success_or_banner_contract_remains():
    text = WORKFLOW.read_text()

    assert "Supported with warning" not in text
    assert "JAX features" not in text
    assert "Current source metadata rejects:** Python 3.11 and older" in text


def test_legacy_verify_install_shim_describes_the_heart_contract():
    text = AUTOHANDS.read_text()

    assert "[--testpypi]" in text
    assert "[--find-links DIR]" in text
    assert "pip, conda & Colab, A–F" in text
    assert "A–E" not in text
