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
        "3.14",
    ]
    assert jobs["smoke_tests"]["strategy"]["matrix"]["python-version"] == [
        "3.12",
        "3.13",
        "3.14",
    ]


def test_python_314_is_a_required_leg_not_an_isolated_experiment():
    """3.14 was promoted to a required leg of both matrices (b038fdc, following
    the PyAutoFit#1439 forkserver fix), which retired the soft
    `experimental_python_314` job. Guard the promoted shape: 3.14 must sit in
    the required matrices above, and must not quietly regrow a
    `continue-on-error` home where its failures stop counting."""
    jobs = load_workflow()["jobs"]

    assert "experimental_python_314" not in jobs

    for name in ("unit_tests", "smoke_tests"):
        assert "3.14" in jobs[name]["strategy"]["matrix"]["python-version"]
        assert "continue-on-error" not in jobs[name]

    assert sorted(jobs["summary"]["needs"]) == ["smoke_tests", "unit_tests"]


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
