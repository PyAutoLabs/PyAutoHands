#!/usr/bin/env python3
"""
Live URL audit for PyAutoLabs repos — used as a weekly CI gate.

Scans a repo tree for http(s) URLs, dedupes them, and validates each one in
parallel via HEAD (falling back to GET on 405/403). Google Colab URLs of the
form ``colab.research.google.com/github/<owner>/<repo>/blob/<ref>/<path>``
are validated through the underlying ``raw.githubusercontent.com/<owner>/
<repo>/<ref>/<path>`` because Colab itself returns HTTP 200 even for dead
refs.

Designed to be invoked from CI (typical: weekly cron, see
``url_check_live.sh``). Reads an optional allowlist of URLs to ignore so the
job only fails when *new* breakage appears, not on the ~hundred external
paywalled / dead links the existing docs already reference.

Usage in CI::

    cd <repo>
    python /path/to/url_check_live.py --strict \
        --allowlist .url_check_allowlist.txt \
        --format markdown-issue

  - exit 0 → every broken URL is in the allowlist (no action needed)
  - exit 1 → at least one broken URL is NOT allowlisted; stdout is a
    Markdown body suitable for ``gh issue create --body-file -``.

Interactive multi-repo audit and scripted rewrites are also supported (kept
for parity with the originally-shipped ``admin_jammy/software/url_check/``
tool — see ``--repos``, ``--fix-known-patterns``).
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import json
import os
import re
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


SCAN_SUFFIXES = {
    ".md", ".rst", ".py", ".ipynb", ".txt", ".yml", ".yaml", ".cfg", ".toml",
}
SCAN_BASENAMES = {"README", "AUTHORS", "CONTRIBUTORS", "LICENSE"}
# Don't scan the allowlist registry itself — every URL there would otherwise
# appear as a location, which is noise and a self-reference.
SCAN_EXCLUDE_BASENAMES = {".url_check_allowlist.txt"}

URL_RE = re.compile(r"https?://[^\s<>\"'`\\\[\]]+")
TRAILING_PUNCT = ".,;:!?*'\""
JSON_ESCAPE_SUFFIX_RE = re.compile(r"(\\[nrt\"']+|n+\\)$")

COLAB_RE = re.compile(
    r"^https?://colab\.research\.google\.com/github/"
    r"(?P<owner>[^/]+)/(?P<repo>[^/]+)/blob/(?P<ref>[^/]+)/(?P<path>.+)$"
)


@dataclass
class Location:
    repo: str
    file: str
    line: int


@dataclass
class Result:
    url: str
    status: str  # ok | redirect | broken | allowlisted
    http_code: int | None
    final_url: str | None
    error: str | None
    locations: list[Location] = field(default_factory=list)


KNOWN_PATTERN_REWRITES: list[tuple[re.Pattern[str], str, str]] = [
    # (regex, replacement, description)
    (re.compile(r"hhttps://"), "https://", "hhttps:// typo"),
    (re.compile(
        r"(github\.com|githubusercontent\.com)/Jammy2211/"
        r"(autolens_workspace|autogalaxy_workspace|autofit_workspace)"
    ), r"\1/PyAutoLabs/\2", "Jammy2211/<workspace> → PyAutoLabs/<workspace>"),
    (re.compile(
        r"(github\.com|githubusercontent\.com)/Jammy2211/"
        r"(PyAutoArray|PyAutoLens|PyAutoGalaxy)"
    ), r"\1/PyAutoLabs/\2", "Jammy2211/<library> → PyAutoLabs/<library>"),
    (re.compile(r"(github\.com|githubusercontent\.com)/(?:Jammy2211|rhayes777)/(PyAutoFit|PyAutoConf)"),
     r"\1/PyAutoLabs/\2", "Jammy2211|rhayes777/{PyAutoFit,PyAutoConf} → PyAutoLabs/..."),
    (re.compile(r"(github\.com|githubusercontent\.com)/rhayes777/PyAutoGalaxy"),
     r"\1/PyAutoLabs/PyAutoGalaxy", "rhayes777/PyAutoGalaxy → PyAutoLabs/PyAutoGalaxy"),
    (re.compile(r"/blob/release/"), "/blob/main/", "/blob/release/ → /blob/main/"),
    (re.compile(r"/tree/release/"), "/tree/main/", "/tree/release/ → /tree/main/"),
    (re.compile(r"github\.com/joshspeagle/[Nn]autilus"),
     "github.com/johannesulf/nautilus", "joshspeagle/nautilus → johannesulf/nautilus"),
    (re.compile(r"github\.com/rhayes777/PyAutoBuild"),
     "github.com/PyAutoLabs/PyAutoBuild", "rhayes777/PyAutoBuild → PyAutoLabs/PyAutoBuild"),
    (re.compile(r"www\.sphinx-doc\.org/en/main"),
     "www.sphinx-doc.org/en/master", "sphinx-doc /en/main → /en/master"),
    (re.compile(r"github\.com/bokeh/bokeh/blob/main/CODE_OF_CONDUCT\.md"),
     "github.com/bokeh/bokeh/blob/main/docs/CODE_OF_CONDUCT.md",
     "bokeh CoC moved to /docs/"),
    (re.compile(
        r"https?://github\.com/numfocus/numfocus/blob/main/manual/numfocus-coc\.md"
        r"(#the-short-version)?"
    ), "https://numfocus.org/code-of-conduct",
     "numfocus CoC → numfocus.org/code-of-conduct"),
    (re.compile(r"Fiterence_anti-harassment"), "Conference_anti-harassment",
     "Fiterence → Conference (typo)"),
    (re.compile(
        r"(colab\.research\.google\.com/github/PyAutoLabs/autofit_workspace/blob/[^/]+/)start_here\.ipynb"
    ), r"\1notebooks/overview/overview_1_the_basics.ipynb",
     "autofit_workspace Colab badge → notebooks/overview/overview_1_the_basics.ipynb"),
    (re.compile(
        r"(colab\.research\.google\.com/github/PyAutoLabs/autogalaxy_workspace/blob/[^/]+/)start_here\.ipynb"
    ), r"\1notebooks/imaging/start_here.ipynb",
     "autogalaxy_workspace Colab badge → notebooks/imaging/start_here.ipynb"),
    (re.compile(
        r"(colab\.research\.google\.com/github/PyAutoLabs/autolens_workspace/blob/[^/]+/)start_here\.ipynb"
    ), r"\1notebooks/imaging/start_here.ipynb",
     "autolens_workspace Colab badge → notebooks/imaging/start_here.ipynb"),
    (re.compile(r"autofit_workspace/blob/main/notebooks/overview/simple/fit\.ipynb"),
     "autofit_workspace/blob/main/notebooks/overview/overview_1_the_basics.ipynb",
     "autofit_workspace simple/fit → overview_1_the_basics"),
    (re.compile(r"autofit_workspace/blob/main/notebooks/overview/complex/fit\.ipynb"),
     "autofit_workspace/blob/main/notebooks/overview/overview_2_scientific_workflow.ipynb",
     "autofit_workspace complex/fit → overview_2_scientific_workflow"),
    (re.compile(r"autofit_workspace/blob/main/notebooks/overview/(simple|complex)/result\.ipynb"),
     "autofit_workspace/blob/main/notebooks/cookbooks/result.ipynb",
     "autofit_workspace overview/*/result → cookbooks/result"),
    (re.compile(r"autofit_workspace/tree/main/notebooks/overview/simplee"),
     "autofit_workspace/tree/main/notebooks/overview",
     "autofit_workspace simplee typo → overview"),
    (re.compile(r"pyautofit\.readthedocs\.io/en/latest/cookbooks/cookbook_1_basics\.html"),
     "pyautofit.readthedocs.io/en/latest/cookbooks/model.html",
     "PyAutoFit cookbook_1_basics → cookbooks/model"),
    (re.compile(r"pyautofit\.readthedocs\.io/en/latest/overview/model_fit\.html"),
     "pyautofit.readthedocs.io/en/latest/overview/the_basics.html",
     "PyAutoFit overview/model_fit → overview/the_basics"),
    (re.compile(r"pyautofit\.readthedocs\.io/en/latest/overview/model_complex\.html"),
     "pyautofit.readthedocs.io/en/latest/cookbooks/model.html",
     "PyAutoFit overview/model_complex → cookbooks/model"),
    (re.compile(r"pyautofit\.readthedocs\.io/en/latest/overview/non_linear_search\.html"),
     "pyautofit.readthedocs.io/en/latest/cookbooks/search.html",
     "PyAutoFit overview/non_linear_search → cookbooks/search"),
    (re.compile(r"pyautofit\.readthedocs\.io/en/latest/overview/result\.html"),
     "pyautofit.readthedocs.io/en/latest/cookbooks/result.html",
     "PyAutoFit overview/result → cookbooks/result"),
    (re.compile(
        r"(autogalaxy_workspace|autolens_workspace)/blob/main/notebooks/"
        r"modeling/imaging/features/(multi_gaussian_expansion|shapelets|"
        r"linear_light_profiles|pixelization|extra_galaxies|operated_light_profile|"
        r"sky_background)\.ipynb"
    ), r"\1/blob/main/notebooks/imaging/features/\2/modeling.ipynb",
     "workspaces modeling/imaging/features/<x>.ipynb → imaging/features/<x>/modeling.ipynb"),
    (re.compile(
        r"(autogalaxy_workspace|autolens_workspace)/blob/main/notebooks/"
        r"multi/modeling/features/(wavelength_dependence|same_wavelength|dataset_offsets|"
        r"one_by_one|imaging_and_interferometer|pixelization)\.ipynb"
    ), r"\1/blob/main/notebooks/multi/features/\2/modeling.ipynb",
     "workspaces multi/modeling/features/<x>.ipynb → multi/features/<x>/modeling.ipynb"),
    (re.compile(
        r"(autogalaxy_workspace|autolens_workspace)/blob/main/notebooks/"
        r"multi/modeling/start_here\.ipynb"
    ), r"\1/blob/main/notebooks/multi/start_here.ipynb",
     "workspaces multi/modeling/start_here → multi/start_here"),
    (re.compile(r"autolens_workspace/blob/main/notebooks/imaging/features/shapelets/"),
     "autolens_workspace/blob/main/notebooks/imaging/features/advanced/shapelets/",
     "autolens shapelets under imaging/features/advanced/"),
    (re.compile(
        r"(autogalaxy_workspace|autolens_workspace|autofit_workspace)/tree/main/notebooks/plot"
    ), r"\1/tree/main/notebooks/guides/plot",
     "workspaces tree/main/notebooks/plot → notebooks/guides/plot"),
    (re.compile(
        r"raw\.githubusercontent\.com/(?:rhayes777|PyAutoLabs)/PyAutoFit/feature/docs_update/"
    ), "raw.githubusercontent.com/PyAutoLabs/PyAutoFit/main/",
     "PyAutoFit docs_update branch images → PyAutoLabs/main"),
]


_TOOL_DIR_ABS = Path(__file__).resolve().parent  # PyAutoBuild/autobuild


def _should_scan(path: Path) -> bool:
    if path.name in SCAN_EXCLUDE_BASENAMES:
        return False
    if path.suffix in SCAN_SUFFIXES:
        return True
    if path.stem.upper() in {b.upper() for b in SCAN_BASENAMES}:
        return True
    return False


def _skip_dir(name: str) -> bool:
    return name in {
        ".git", ".github", "__pycache__", ".pytest_cache", ".mypy_cache",
        ".tox", "build", "dist", "node_modules", ".idea", ".vscode",
        "output", "out", "output_mode", ".ipynb_checkpoints",
    }


def _is_tool_dir(path: Path) -> bool:
    try:
        path.resolve().relative_to(_TOOL_DIR_ABS)
        return True
    except ValueError:
        return False


def iter_scan_files(repo_root: Path) -> Iterable[Path]:
    for dirpath, dirnames, filenames in os.walk(repo_root, followlinks=False):
        dirnames[:] = [d for d in dirnames if not _skip_dir(d)]
        for fn in filenames:
            p = Path(dirpath) / fn
            if _should_scan(p) and not _is_tool_dir(p):
                yield p


def _clean_url(url: str) -> str:
    url = JSON_ESCAPE_SUFFIX_RE.sub("", url)
    while url and url[-1] in TRAILING_PUNCT:
        url = url[:-1]
    while url:
        c = url[-1]
        if c == ")" and url.count("(") < url.count(")"):
            url = url[:-1]
        elif c == "]" and url.count("[") < url.count("]"):
            url = url[:-1]
        elif c == "}" and url.count("{") < url.count("}"):
            url = url[:-1]
        elif c in TRAILING_PUNCT:
            url = url[:-1]
        else:
            break
    return url


def extract_urls(file_path: Path) -> list[tuple[str, int]]:
    out: list[tuple[str, int]] = []
    try:
        text = file_path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return out
    for lineno, line in enumerate(text.splitlines(), start=1):
        for m in URL_RE.finditer(line):
            url = _clean_url(m.group(0))
            if "$" in url or "{" in url:
                continue
            if len(url) > 10:
                out.append((url, lineno))
    return out


def scan_repos(repos: list[Path]) -> dict[str, list[Location]]:
    index: dict[str, list[Location]] = {}
    for repo_root in repos:
        repo_name = repo_root.name
        if not repo_root.exists():
            print(f"skip: {repo_root} does not exist", file=sys.stderr)
            continue
        for fp in iter_scan_files(repo_root):
            try:
                rel = fp.relative_to(repo_root).as_posix()
            except ValueError:
                rel = fp.as_posix()
            for url, lineno in extract_urls(fp):
                index.setdefault(url, []).append(Location(repo_name, rel, lineno))
    return index


def _colab_to_raw(url: str) -> str | None:
    m = COLAB_RE.match(url)
    if not m:
        return None
    return (
        f"https://raw.githubusercontent.com/{m['owner']}/{m['repo']}/"
        f"{m['ref']}/{m['path']}"
    )


def _build_session() -> requests.Session:
    s = requests.Session()
    retry = Retry(
        total=2, connect=2, read=2, backoff_factor=0.3,
        status_forcelist=(500, 502, 503, 504),
        allowed_methods=frozenset(["GET", "HEAD"]),
    )
    adapter = HTTPAdapter(max_retries=retry, pool_connections=32, pool_maxsize=32)
    s.mount("http://", adapter)
    s.mount("https://", adapter)
    s.headers.update({"User-Agent": "PyAutoLabs-url-check/1.0"})
    return s


def check_url(session: requests.Session, url: str, timeout: float = 12.0) -> Result:
    raw = _colab_to_raw(url)
    probe_url = raw if raw else url

    try:
        r = session.head(probe_url, allow_redirects=True, timeout=timeout)
        if r.status_code in (403, 405) or (raw is None and r.status_code == 404):
            if raw is None or r.status_code in (403, 405):
                r = session.get(probe_url, allow_redirects=True, timeout=timeout, stream=True)
                try:
                    r.close()
                except Exception:
                    pass
    except requests.exceptions.RequestException as e:
        return Result(url=url, status="broken", http_code=None, final_url=None,
                      error=type(e).__name__ + ": " + str(e)[:160])

    code = r.status_code
    final = r.url if r.url != probe_url else None
    if 200 <= code < 300:
        status = "redirect" if final and final != probe_url else "ok"
    elif 300 <= code < 400:
        status = "redirect"
    else:
        status = "broken"
    return Result(url=url, status=status, http_code=code, final_url=final, error=None)


def check_all(urls: list[str], workers: int = 16) -> list[Result]:
    session = _build_session()
    results: list[Result] = []
    t0 = time.monotonic()
    done = 0
    with cf.ThreadPoolExecutor(max_workers=workers) as ex:
        fut_to_url = {ex.submit(check_url, session, u): u for u in urls}
        for fut in cf.as_completed(fut_to_url):
            try:
                results.append(fut.result())
            except Exception as e:
                u = fut_to_url[fut]
                results.append(Result(url=u, status="broken", http_code=None,
                                      final_url=None, error=f"executor: {e}"))
            done += 1
            if done % 50 == 0 or done == len(urls):
                elapsed = time.monotonic() - t0
                print(f"  checked {done}/{len(urls)} ({elapsed:.1f}s)", file=sys.stderr)
    return results


_INLINE_COMMENT_RE = re.compile(r"\s+#")


def load_allowlist(path: Path | None) -> set[str]:
    """Parse an allowlist file. Lines starting with ``#`` are comments;
    inline comments require whitespace before ``#`` so URL fragments
    (e.g. ``foo.html#section``) survive."""
    if path is None or not path.exists():
        return set()
    urls: set[str] = set()
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        if raw_line.lstrip().startswith("#"):
            continue
        line = _INLINE_COMMENT_RE.split(raw_line, maxsplit=1)[0].strip()
        if line:
            urls.add(line)
    return urls


def render_text_report(results: list[Result]) -> str:
    by_status: dict[str, list[Result]] = {"broken": [], "allowlisted": [],
                                          "redirect": [], "ok": []}
    for r in results:
        by_status[r.status].append(r)

    lines: list[str] = []
    lines.append(f"Total URLs: {len(results)}")
    lines.append(f"  broken (not allowlisted): {len(by_status['broken'])}")
    lines.append(f"  allowlisted broken:       {len(by_status['allowlisted'])}")
    lines.append(f"  redirect:                 {len(by_status['redirect'])}")
    lines.append(f"  ok:                       {len(by_status['ok'])}")
    if by_status["broken"]:
        lines.append("")
        lines.append("Broken (not allowlisted):")
        for r in sorted(by_status["broken"], key=lambda r: r.url):
            tag = f"HTTP {r.http_code}" if r.http_code else (r.error or "error")
            locs = ", ".join(f"{loc.file}:{loc.line}" for loc in r.locations[:3])
            extra = f" (+ {len(r.locations) - 3} more)" if len(r.locations) > 3 else ""
            lines.append(f"  [{tag}] {r.url}")
            lines.append(f"     at: {locs}{extra}")
    return "\n".join(lines) + "\n"


def render_markdown_issue(results: list[Result], repo_label: str) -> str:
    broken = [r for r in results if r.status == "broken"]
    if not broken:
        return ""
    lines: list[str] = []
    lines.append(f"The weekly URL audit found **{len(broken)} broken URL(s)** "
                 f"in `{repo_label}` that are not in `.url_check_allowlist.txt`.")
    lines.append("")
    lines.append("If these are genuinely-broken-but-acceptable (paywalled, "
                 "dead-external, etc.), append them to "
                 "`.url_check_allowlist.txt` to grandfather them. Otherwise "
                 "fix the references in-repo.")
    lines.append("")
    for r in sorted(broken, key=lambda r: r.url):
        tag = f"HTTP {r.http_code}" if r.http_code is not None else (r.error or "error")
        lines.append(f"### `{r.url}`")
        lines.append(f"- status: {tag}")
        lines.append(f"- referenced from {len(r.locations)} site(s):")
        for loc in r.locations[:20]:
            lines.append(f"  - `{loc.file}:{loc.line}`")
        if len(r.locations) > 20:
            lines.append(f"  - … and {len(r.locations) - 20} more")
        lines.append("")
    lines.append("---")
    lines.append("*Generated by `PyAutoBuild/autobuild/url_check_live.py`. "
                 "Re-runs every Monday 04:00 UTC.*")
    return "\n".join(lines) + "\n"


def apply_known_pattern_fixes(repos: list[tuple[Path, Path]], dry_run: bool = False) -> int:
    total_changes = 0
    for input_path, resolved in repos:
        if input_path.is_symlink():
            print(f"  skip-symlink {input_path.name} -> {resolved}", file=sys.stderr)
            continue
        for fp in iter_scan_files(resolved):
            if _is_tool_dir(fp):
                continue
            try:
                with open(fp, "r", encoding="utf-8", newline="") as f:
                    original = f.read()
            except OSError:
                continue
            new = original
            file_changes = 0
            for pat, repl, _desc in KNOWN_PATTERN_REWRITES:
                new2, n = pat.subn(repl, new)
                if n:
                    file_changes += n
                    new = new2
            if file_changes and new != original:
                total_changes += file_changes
                rel = fp.relative_to(resolved.parent)
                print(f"  {'would-fix' if dry_run else 'fix'} {rel}: {file_changes} rewrite(s)")
                if not dry_run:
                    with open(fp, "w", encoding="utf-8", newline="") as f:
                        f.write(new)
    return total_changes


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Audit URLs and (optionally) fail on new breakage.")
    p.add_argument("--repos", nargs="+",
                   help="Repo paths (or names under --root). Defaults to cwd.")
    p.add_argument("--root", default=None,
                   help="Base directory for bare repo names (default: cwd).")
    p.add_argument("--allowlist", default=None,
                   help="File listing URLs to ignore (one per line, # comments).")
    p.add_argument("--strict", action="store_true",
                   help="Exit 1 if any URL is broken AND not in the allowlist.")
    p.add_argument("--format", default="text",
                   choices=("text", "markdown-issue", "json"),
                   help="Output format (default: text).")
    p.add_argument("--workers", type=int, default=16)
    p.add_argument("--fix-known-patterns", action="store_true",
                   help="Apply scripted rewrites in place. Interactive use only.")
    p.add_argument("--dry-run-fixes", action="store_true")
    p.add_argument("--no-check", action="store_true",
                   help="Skip network audit (useful with --fix-known-patterns).")
    args = p.parse_args(argv)

    # Default root: cwd. Bare-repo args (e.g. "PyAutoLens") resolve under it.
    # Note: NEVER use Path(__file__).resolve() for the root — this tool may
    # be run from a worktree where its admin_jammy parent is symlinked back
    # to the canonical checkout (the bug behind ``feedback_path_file_resolve_symlink``).
    root = Path(args.root).resolve() if args.root else Path.cwd().resolve()

    repo_args = args.repos or ["."]
    repos: list[tuple[Path, Path]] = []
    for r in repo_args:
        path = Path(r)
        if not path.is_absolute():
            path = root / r
        repos.append((path, path.resolve()))

    print(f"Scanning {len(repos)} repo(s) under {root}", file=sys.stderr)

    if args.fix_known_patterns:
        print("Applying known-pattern rewrites…", file=sys.stderr)
        n = apply_known_pattern_fixes(repos, dry_run=args.dry_run_fixes)
        print(f"  total rewrites: {n}", file=sys.stderr)
        if args.no_check:
            return 0

    locations = scan_repos([resolved for _, resolved in repos])
    urls = sorted(locations.keys())
    print(f"Extracted {len(urls)} unique URLs", file=sys.stderr)

    if args.no_check:
        return 0

    results = check_all(urls, workers=args.workers)
    for r in results:
        r.locations = locations.get(r.url, [])

    allowlist = load_allowlist(Path(args.allowlist)) if args.allowlist else set()
    if allowlist:
        for r in results:
            if r.status == "broken" and r.url in allowlist:
                r.status = "allowlisted"

    repo_label = repos[0][1].name if len(repos) == 1 else f"{len(repos)} repos"
    if args.format == "text":
        sys.stdout.write(render_text_report(results))
    elif args.format == "json":
        payload = {
            "summary": {
                "total": len(results),
                "broken": sum(1 for r in results if r.status == "broken"),
                "allowlisted": sum(1 for r in results if r.status == "allowlisted"),
                "redirect": sum(1 for r in results if r.status == "redirect"),
                "ok": sum(1 for r in results if r.status == "ok"),
            },
            "results": [
                {"url": r.url, "status": r.status, "http_code": r.http_code,
                 "final_url": r.final_url, "error": r.error,
                 "locations": [{"file": l.file, "line": l.line} for l in r.locations]}
                for r in sorted(results, key=lambda r: (r.status, r.url))
            ],
        }
        sys.stdout.write(json.dumps(payload, indent=2) + "\n")
    elif args.format == "markdown-issue":
        body = render_markdown_issue(results, repo_label)
        if body:
            sys.stdout.write(body)

    broken_unallowed = sum(1 for r in results if r.status == "broken")
    if args.strict and broken_unallowed > 0:
        print(f"FAIL: {broken_unallowed} broken URL(s) not in allowlist",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
