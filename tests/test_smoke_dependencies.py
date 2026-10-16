import json
import os
from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'autohands'))
import build_util
from result_collector import RunReport, Status
from smoke_dependencies import constructed_names


@pytest.mark.parametrize('source', [
    'import autofit as af\naf.ExampleSearch()',
    'import autofit\nautofit.ExampleSearch()',
    'from autofit import ExampleSearch as Search\nSearch()',
])
def test_constructor_aliases(source):
    assert constructed_names(source) == ({'ExampleSearch'}, False)


def test_unrelated_names_and_non_calls_are_not_searches():
    assert constructed_names('import other as af\naf.ExampleSearch()') == (set(), False)
    assert constructed_names('import autofit as af\ncls = af.ExampleSearch') == (set(), False)


def test_corner_plotter():
    source = 'from autofit import plot as afp\np = afp.MCMCPlotter()\np.corner_corner()'
    assert constructed_names(source)[1]
    assert not constructed_names('other.corner_corner()')[1]


@pytest.fixture
def runner(tmp_path, monkeypatch):
    package = tmp_path / 'autofit'
    package.mkdir()
    (package / '__init__.py').write_text('def ExampleSearch(): pass\n')
    manifest = {'schema': 'search-manifest@1', 'searches': [
        {'name': 'ExampleSearch', 'requires': ['example_backend_for_smoke']} ]}
    (package / '__main__.py').write_text('import json\nprint(' + repr(json.dumps(manifest)) + ')\n')
    monkeypatch.setattr(build_util, 'BUILD_PYTHON_INTERPRETER', sys.executable)
    script = tmp_path / 'script.py'
    def run(source, mode='2', extra_args=None):
        script.write_text(source)
        report = RunReport(project='fixture', directory=str(tmp_path), run_type='script')
        build_util.execute_script(str(script), report=report,
            env=dict(os.environ, PYTHONPATH=str(tmp_path), PYAUTO_TEST_MODE=mode), extra_args=extra_args)
        return report.results[0]
    return run


def test_missing_backend_fails_before_script_then_installed_passes(tmp_path, runner):
    source = 'import autofit as af\naf.ExampleSearch()\nopen("' + str(tmp_path / 'ran') + '", "w").close()'
    result = runner(source)
    assert result.status == Status.FAILED
    assert 'ExampleSearch requires importable module example_backend_for_smoke' in result.traceback
    assert not (tmp_path / 'ran').exists()
    (tmp_path / 'example_backend_for_smoke.py').write_text('')
    assert runner(source).status == Status.PASSED
    assert (tmp_path / 'ran').exists()


def test_broken_import_is_a_failure(tmp_path, runner):
    (tmp_path / 'example_backend_for_smoke.py').write_text('raise RuntimeError("broken binary")')
    result = runner('import autofit as af\naf.ExampleSearch()')
    assert result.status == Status.FAILED
    assert 'broken binary' in result.traceback


def test_real_mode_does_not_apply_smoke_guard(runner):
    assert runner('import autofit as af\naf.ExampleSearch()', mode='1').status == Status.PASSED


@pytest.mark.parametrize('source,code', [('if invalid syntax', 1), ('raise SystemExit(7)', 7)])
def test_script_failures_are_reported(runner, source, code):
    result = runner(source)
    assert result.status == Status.FAILED
    assert result.exit_code == code


def test_script_argv_and_local_imports_survive(tmp_path, runner):
    (tmp_path / 'sibling.py').write_text('value = 5')
    source = 'import sys, sibling\nassert sibling.value == 5\nassert sys.argv[1:] == ["argument"]\nassert __name__ == "__main__"'
    assert runner(source, extra_args=['argument']).status == Status.PASSED


def test_manifest_failure_is_not_silently_ignored(tmp_path, runner):
    (tmp_path / 'autofit/__main__.py').write_text('raise SystemExit(3)')
    result = runner('import autofit as af\naf.ExampleSearch()')
    assert result.status == Status.FAILED
    assert 'cannot read autofit search manifest' in result.traceback


@pytest.mark.parametrize('source', [
    'import autofit.plot as aplt\naplt.corner_cornerpy(samples=None)',
    'from autofit.plot import corner_cornerpy as corner_plot\ncorner_plot(samples=None)',
    'from autofit import plot as aplt\naplt.corner_cornerpy(samples=None)',
])
def test_public_corner_function(source):
    assert constructed_names(source)[1]


def test_smoke_preflight_is_inside_process_timeout(tmp_path, runner, monkeypatch):
    monkeypatch.setenv('BUILD_SCRIPT_TIMEOUT', '1')
    (tmp_path / 'autofit/__main__.py').write_text('import time\ntime.sleep(10)')
    result = runner('import autofit as af\naf.ExampleSearch()')
    assert result.status == Status.TIMEOUT
