"""Sphinx extension for Pappus of Alexandria's *Synagoge* Multi-Track Book Codex.

Registers the ``el`` ("Greek (Hultsch 1876)") companion track in
:mod:`photon_platform.publish.book` at build time and configures offline-safe
``intersphinx_mapping`` entries against locally built sibling GEOMETOR
repositories whenever their ``docs/objects.inv`` inventories exist on disk.
"""
from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Any

GREEK_TRACK_KEY = "el"
GREEK_TRACK_LABEL = "Greek (Hultsch 1876)"

SIBLING_CODICES: tuple[tuple[str, str, str], ...] = (
    ("euclid", "euclid", "https://geometor.github.io/euclid"),
    ("elements", "elements", "https://geometor.github.io/elements"),
    ("apollonius", "apollonius", "https://geometor.github.io/apollonius"),
    ("archimedes", "archimedes", "https://geometor.github.io/archimedes"),
    ("ptolemy", "ptolemy", "https://geometor.github.io/ptolemy"),
    ("menelaus", "menelaus", "https://geometor.github.io/menelaus"),
    ("proclus", "proclus", "https://geometor.github.io/proclus"),
    ("aristotle", "aristotle", "https://geometor.github.io/aristotle"),
    ("hoenen", "hoenen", "https://geometor.github.io/hoenen"),
    ("hilbert", "hilbert", "https://geometor.github.io/hilbert"),
    ("altshiller", "altshiller-court", "https://geometor.github.io/altshiller-court"),
    ("etc", "etc", "https://geometor.github.io/etc"),
    ("wildberger", "wildberger", "https://geometor.github.io/wildberger"),
)


def register_greek_book_track() -> None:
    """Extend :mod:`photon_platform.publish.book` to recognize ``<stem>-el`` Greek tracks."""
    try:
        from photon_platform.publish import book
    except ImportError:
        return

    el_pattern = (r"^(.+)[._-]el$", GREEK_TRACK_KEY, GREEK_TRACK_LABEL)
    if not any(key == GREEK_TRACK_KEY for _pat, key, _lbl in book._TRACK_SUFFIX_PATTERNS):
        book._TRACK_SUFFIX_PATTERNS.append(el_pattern)

    if hasattr(book, "_AUX_TRACK_BASENAMES"):
        book._AUX_TRACK_BASENAMES.add(GREEK_TRACK_KEY)
    el_aux_re = re.compile(r"^.+[._-]el$")
    if hasattr(book, "_AUX_TRACK_PATTERNS") and not any(
        p.pattern == el_aux_re.pattern for p in book._AUX_TRACK_PATTERNS
    ):
        book._AUX_TRACK_PATTERNS.append(el_aux_re)

    if getattr(book.detect_companion_tracks, "_pappus_el_patched", False):
        return

    orig_detect = book.detect_companion_tracks

    def _detect_with_greek(env: object, pagename: str) -> list[dict[str, Any]]:
        found_docs: set[str] = set(getattr(env, "found_docs", set()))
        if not found_docs:
            return []

        doc_dir = os.path.dirname(pagename)
        basename = os.path.basename(pagename)
        stem = book._extract_unit_stem(basename, doc_dir)
        if basename == GREEK_TRACK_KEY and doc_dir:
            stem = os.path.basename(doc_dir)

        def _qual(local_name: str) -> str:
            return f"{doc_dir}/{local_name}" if doc_dir else local_name

        probe_page = pagename
        el_candidates = [
            _qual(f"{stem}.el"),
            _qual(f"{stem}_el"),
            _qual(f"{stem}-el"),
            _qual(GREEK_TRACK_KEY),
        ]
        el_doc = next((c for c in el_candidates if c in found_docs), None)
        if el_doc and pagename == el_doc:
            en_cand = next(
                (
                    c
                    for c in (_qual(f"{stem}-en"), _qual(f"{stem}_en"), _qual(f"{stem}.en"))
                    if c in found_docs
                ),
                None,
            )
            if en_cand:
                probe_page = en_cand

        tracks = orig_detect(env, probe_page)
        if not el_doc:
            return tracks

        updated: list[dict[str, Any]] = []
        inserted_el = False
        el_entry = {
            "key": GREEK_TRACK_KEY,
            "label": GREEK_TRACK_LABEL,
            "docname": el_doc,
            "active": el_doc == pagename,
        }
        for tr in tracks:
            if tr.get("docname") == el_doc:
                continue
            item = dict(tr)
            item["active"] = item.get("docname") == pagename
            updated.append(item)
            if item.get("key") == "en" and not inserted_el:
                updated.append(el_entry)
                inserted_el = True

        if not inserted_el:
            updated.insert(0, el_entry)

        return updated if len(updated) >= 2 else []

    _detect_with_greek._pappus_el_patched = True  # type: ignore[attr-defined]
    book.detect_companion_tracks = _detect_with_greek


def configure_local_intersphinx(
    intersphinx_mapping: dict[str, Any] | None = None,
    project_root: Path | None = None,
) -> dict[str, tuple[str, str]]:
    """Bind local sibling ``objects.inv`` inventories and prune unreachable remote-only targets.

    Args:
        intersphinx_mapping: Optional live Sphinx ``intersphinx_mapping`` dict to update in-place.
        project_root: Path to ``/home/phi/PROJECTS/geometor/pappus``; inferred from package path if ``None``.

    Returns:
        Dictionary of locally resolved ``(base_url, objects_inv_path)`` entries.
    """
    repo_root = (
        project_root
        if project_root is not None
        else Path(__file__).resolve().parents[3]
    )
    workspace_root = repo_root.parent
    local_entries: dict[str, tuple[str, str]] = {}
    for key, repo_dir, base_url in SIBLING_CODICES:
        inv_path = workspace_root / repo_dir / "docs" / "objects.inv"
        if inv_path.is_file():
            local_entries[key] = (base_url, str(inv_path.resolve()))

    if intersphinx_mapping is not None:
        intersphinx_mapping.update(local_entries)
        for key in list(intersphinx_mapping.keys()):
            _uri, inv_target = intersphinx_mapping[key]
            if inv_target is None:
                intersphinx_mapping.pop(key, None)

    return local_entries


def setup(app: object) -> dict[str, object]:
    """Initialize the ``geometor.pappus.sphinx_ext`` Sphinx extension."""
    _ = app
    register_greek_book_track()
    return {
        "version": "0.2.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
