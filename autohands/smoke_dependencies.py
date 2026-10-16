"""Smoke-only dependency preflight, using autofit's public search manifest.

Runs in the script interpreter, inside the existing process-group timeout.
Static detection covers imported autofit aliases and directly imported searches;
it does not try to infer dynamically selected constructors.
"""
import ast
import importlib
import json
from pathlib import Path
import runpy
import subprocess
import sys


def constructed_names(source):
    tree = ast.parse(source)
    aliases = set()
    direct = {}
    plot_aliases = set()
    plotters = set()
    direct_corner = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for item in node.names:
                if item.name == 'autofit':
                    aliases.add(item.asname or item.name)
                elif item.name == 'autofit.plot':
                    plot_aliases.add(item.asname or item.name)
        elif isinstance(node, ast.ImportFrom) and node.module == 'autofit':
            for item in node.names:
                direct[item.asname or item.name] = item.name
                if item.name == 'plot':
                    plot_aliases.add(item.asname or item.name)
        elif isinstance(node, ast.ImportFrom) and node.module == 'autofit.plot':
            for item in node.names:
                if item.name == 'corner_cornerpy':
                    direct_corner.add(item.asname or item.name)
    names = set()
    def plot_constructor(node):
        return (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
                and isinstance(node.func.value, ast.Name)
                and node.func.value.id in plot_aliases)
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and plot_constructor(node.value):
            plotters.update(t.id for t in node.targets if isinstance(t, ast.Name))
        if not isinstance(node, ast.Call):
            continue
        fn = node.func
        if isinstance(fn, ast.Attribute) and isinstance(fn.value, ast.Name) and fn.value.id in aliases:
            names.add(fn.attr)
        elif isinstance(fn, ast.Name) and fn.id in direct:
            names.add(direct[fn.id])
    corner = any(isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
                 and node.func.attr == 'corner_corner'
                 and ((isinstance(node.func.value, ast.Name) and node.func.value.id in plotters)
                      or plot_constructor(node.func.value)) for node in ast.walk(tree))
    corner = corner or any(
        isinstance(node, ast.Call) and (
            isinstance(node.func, ast.Name) and node.func.id in direct_corner
            or isinstance(node.func, ast.Attribute) and node.func.attr == 'corner_cornerpy'
            and isinstance(node.func.value, ast.Name) and node.func.value.id in plot_aliases
        ) for node in ast.walk(tree))
    return names, corner


def check_script(path):
    names, corner = constructed_names(Path(path).read_text(encoding='utf-8'))
    requirements = []
    if names:
        # Preserve this smoke interpreter's environment and source checkouts.
        proc = subprocess.run([sys.executable, '-m', 'autofit', 'search-manifest', '--json'],
                              capture_output=True, text=True)
        if proc.returncode:
            raise RuntimeError(f'{path}: cannot read autofit search manifest: {proc.stderr.strip()}')
        manifest = json.loads(proc.stdout)
        if manifest.get('schema') != 'search-manifest@1':
            raise RuntimeError(f'{path}: unsupported autofit search manifest schema')
        for search in manifest['searches']:
            if search['name'] in names:
                requirements.extend((search['name'], module) for module in search['requires'])
    if corner:
        requirements.append(('corner_corner', 'corner'))
    for search, module in sorted(set(requirements)):
        try:
            importlib.import_module(module)
        except Exception as exc:
            raise RuntimeError(f'{path}: {search} requires importable module {module}: {exc}') from exc


def main():
    path = Path(sys.argv[1]).resolve()
    sys.argv = sys.argv[1:]
    # Match `python script.py` import resolution before checking or execution.
    sys.path[0] = str(path.parent)
    check_script(path)
    runpy.run_path(str(path), run_name='__main__')


if __name__ == '__main__':
    main()
