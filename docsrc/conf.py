"""Sphinx configuration for GEOMETOR • pappus (Synagoge Codex & Symbolic Projective Geometry)."""
from __future__ import annotations

from pathlib import Path
import sys

_REPO_ROOT = Path(__file__).resolve().parents[1]
_WORKSPACE_ROOT = _REPO_ROOT.parent
for _extra_path in (
    _REPO_ROOT / "src",
    _WORKSPACE_ROOT / "model" / "src",
    _WORKSPACE_ROOT / "explorer" / "src",
    _WORKSPACE_ROOT / "divine" / "src",
    _WORKSPACE_ROOT / ".venv" / "lib" / "python3.13" / "site-packages",
):
    if _extra_path.exists() and str(_extra_path) not in sys.path:
        sys.path.insert(0, str(_extra_path))

from photon_platform.publish.global_conf import *  # noqa: E402, F403

import geometor.pappus as module  # noqa: E402
from geometor.pappus.sphinx_ext import (  # noqa: E402
    configure_local_intersphinx,
    register_greek_book_track,
)

version = module.__version__

org = "geometor"
org_name = "GEOMETOR"

repo = "pappus"
repo_name = "pappus"

setup_globals(org, org_name, repo, repo_name)  # noqa: F405

if "geometor.pappus.sphinx_ext" not in extensions:  # noqa: F405
    extensions.append("geometor.pappus.sphinx_ext")  # noqa: F405

register_greek_book_track()
configure_local_intersphinx(intersphinx_mapping, _REPO_ROOT)  # noqa: F405

project = "GEOMETOR • pappus"
author = "Pappus of Alexandria • Ed. & SymPy Synthesis GEOMETOR"
copyright = (
    "c. 340 CE (Hultsch 1876–1878 / Commandino 1588) • "
    "Original English Translation & Exact Symbolic Edition GEOMETOR"
)

html_theme = "foundation"
html_static_path = ["_static"]
html_css_files = [*globals().get("html_css_files", []), "custom.css"]
html_logo = None
autoapi_dirs = [str(_REPO_ROOT / "src" / "geometor")]
autoapi_add_toctree_entry = False
napoleon_use_ivar = True
for _excl in ("intro.rst", "modules/api/geometor/pappus/index.rst"):
    if _excl not in exclude_patterns:  # noqa: F405
        exclude_patterns.append(_excl)  # noqa: F405
suppress_warnings = ["autoapi.python_import_resolution", "toc.not_included"]

mathjax3_config = {
    "tex": {
        "inlineMath": [["\\(", "\\)"], ["$", "$"]],
        "displayMath": [["\\[", "\\]"], ["$$", "$$"]],
    }
}
