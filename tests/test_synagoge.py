"""Test suite for Pappus's *Synagoge* (Books III, IV, V, VII & VIII) symbolic constructions and codex extensions."""
from __future__ import annotations

import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from types import SimpleNamespace

import pytest
import sympy as sp
import sympy.geometry as spg
from geometor.model import Model

from geometor.pappus import (
    PHI,
    build_synagoge_gallery,
    construct_honeycomb_isoperimetry,
    construct_pappus_arbelos_chain,
    construct_pappus_area_theorem,
    construct_three_means,
    cross_ratio,
    quadrance,
    verify_arbelos_chain_symbolic,
    verify_honeycomb_isoperimetry,
    verify_pappus_area_symbolic,
)
from geometor.pappus.__main__ import main
from geometor.pappus.sphinx_ext import (
    GREEK_TRACK_KEY,
    SIBLING_CODICES,
    configure_local_intersphinx,
    register_greek_book_track,
    setup,
)


def _assert_zero_floats_in_model(mdl: Model) -> None:
    """Assert that no SymPy geometric entity in ``mdl`` contains floating-point atoms."""
    assert len(mdl) > 0
    for elem in mdl:
        if isinstance(elem, sp.Basic):
            floats = elem.atoms(sp.Float)
            assert not floats, f"Found forbidden sp.Float {floats} in model element {elem!r}"


def test_three_means_rational_semicircle_and_orthogonal_foot() -> None:
    """Verify exact means, orthogonal foot F on OB, and harmonic tangent T on (9, 16)."""
    res = construct_three_means(9, 16)
    assert res.arithmetic_mean == sp.Rational(25, 2)
    assert res.geometric_mean == sp.Integer(12)
    assert res.harmonic_mean == sp.Rational(288, 25)
    assert sp.simplify(res.arithmetic_mean * res.harmonic_mean - res.geometric_mean**2) == 0
    assert res.arithmetic_mean > res.geometric_mean > res.harmonic_mean

    # Verify exact orthogonal projection foot F of D onto radius OB
    assert res.point_f == spg.Point(sp.Rational(7641, 625), sp.Rational(588, 625))
    assert spg.Line(res.center_o, res.point_b).contains(res.point_f)
    vec_df = (res.point_d.x - res.point_f.x, res.point_d.y - res.point_f.y)
    vec_ob = (res.center_o.x - res.point_b.x, res.center_o.y - res.point_b.y)
    assert sp.simplify(vec_df[0] * vec_ob[0] + vec_df[1] * vec_ob[1]) == 0
    assert quadrance(res.point_b, res.point_f) == res.harmonic_mean**2

    # Verify external harmonic tangent conjugate T on diameter AC
    assert res.tangent_t == spg.Point(sp.Rational(-225, 7), 0)
    assert res.harmonic_cross_ratio == -1
    assert cross_ratio(res.point_a, res.point_c, res.point_d, res.tangent_t) == -1
    _assert_zero_floats_in_model(res.model)


def test_three_means_golden_equal_and_model_overload() -> None:
    """Verify Q(phi) golden semicircle, equal-segment degeneracy, and Model-first overload."""
    gold = construct_three_means(1, PHI**2)
    assert sp.simplify(gold.geometric_mean - PHI) == 0
    assert sp.simplify(gold.arithmetic_mean * gold.harmonic_mean - PHI**2) == 0
    assert gold.harmonic_cross_ratio == -1
    _assert_zero_floats_in_model(gold.model)

    eq_res = construct_three_means(4, 4)
    assert eq_res.arithmetic_mean == 4
    assert eq_res.geometric_mean == 4
    assert eq_res.harmonic_mean == 4
    assert eq_res.tangent_t is None
    assert eq_res.harmonic_cross_ratio is None
    _assert_zero_floats_in_model(eq_res.model)

    mdl = Model("custom_three_means", auto_intersect=False)
    ov_res = construct_three_means(mdl, 4, 9)
    assert ov_res.model is mdl
    assert ov_res.geometric_mean == 6
    _assert_zero_floats_in_model(mdl)

    with pytest.raises(ValueError, match="both a and b"):
        construct_three_means(Model("bad_means", auto_intersect=False), 4)
    with pytest.raises(TypeError, match="not float"):
        construct_three_means(1.5, 4)  # type: ignore[arg-type]
    with pytest.raises(ValueError, match="strictly positive"):
        construct_three_means(-3, 4)


def test_pappus_area_theorem_presets_custom_and_symbolic() -> None:
    """Verify Book IV.1 Area Theorem across presets, custom triangles, and 10-variable polynomial ring."""
    assert verify_pappus_area_symbolic() == 0

    scalene = construct_pappus_area_theorem(preset="scalene")
    assert scalene.area_ab == 13
    assert scalene.area_ac == 15
    assert scalene.area_bc == 28
    assert scalene.area_residual == 0
    _assert_zero_floats_in_model(scalene.model)

    pyth = construct_pappus_area_theorem(preset="pythagoras")
    assert pyth.area_ab == 9
    assert pyth.area_ac == 16
    assert pyth.area_bc == 25
    assert pyth.area_residual == 0
    _assert_zero_floats_in_model(pyth.model)

    custom = construct_pappus_area_theorem(
        triangle=((2, 3), (0, 0), (5, 0)),
        vec_ab=(-1, 2),
        vec_ac=(2, 1),
    )
    assert custom.preset == "custom"
    assert custom.area_residual == 0
    assert sp.simplify(custom.area_bc - (custom.area_ab + custom.area_ac)) == 0
    _assert_zero_floats_in_model(custom.model)

    with pytest.raises(KeyError, match="Unknown area-theorem preset"):
        construct_pappus_area_theorem(preset="nonexistent")
    with pytest.raises(ValueError, match="both vec_ab and vec_ac"):
        construct_pappus_area_theorem(triangle=((2, 3), (0, 0), (5, 0)), vec_ab=(-1, 2))
    with pytest.raises(ValueError, match="counter-clockwise"):
        construct_pappus_area_theorem(
            triangle=((0, 0), (2, 3), (5, 0)),
            vec_ab=(-1, 2),
            vec_ac=(2, 1),
        )


def test_arbelos_circle_chain_exact_rational_and_symbolic() -> None:
    """Verify Book IV.14-18 Arbelos circle chain altitude law, tangencies, and focal ellipse."""
    sym_residuals = verify_arbelos_chain_symbolic(n_max=6)
    assert set(sym_residuals) == {
        "altitude_law",
        "outer_tangency",
        "left_tangency",
        "adjacent_tangency",
    }
    assert all(val == 0 for val in sym_residuals.values())

    arb = construct_pappus_arbelos_chain(2, 1, 5)
    assert len(arb.chain) == 5
    assert arb.chain[0].center == spg.Point(sp.Rational(30, 7), sp.Rational(12, 7))
    assert arb.chain[0].diameter == sp.Rational(12, 7)
    # Symmetric maximum altitude at n=2 and n=3 for (r1, r2) = (2, 1)
    assert arb.chain[1].center == spg.Point(3, sp.Rational(12, 5))
    assert arb.chain[2].center == spg.Point(2, sp.Rational(12, 5))

    for item in arb.chain:
        assert item.height_over_diameter == item.index
        assert item.height == item.index * item.diameter
        assert arb.locus_ellipse.contains(item.center)
    _assert_zero_floats_in_model(arb.model)

    mdl = Model("custom_arbelos", auto_intersect=False)
    arb_ov = construct_pappus_arbelos_chain(mdl, 3, 2, 3)
    assert arb_ov.model is mdl
    assert [c.height_over_diameter for c in arb_ov.chain] == [1, 2, 3]
    _assert_zero_floats_in_model(mdl)

    with pytest.raises(ValueError, match="count must be >= 1"):
        construct_pappus_arbelos_chain(2, 1, 0)
    with pytest.raises(TypeError, match="not float"):
        construct_pappus_arbelos_chain(2.0, 1, 3)  # type: ignore[arg-type]


def test_honeycomb_isoperimetry_and_seven_hexagons() -> None:
    """Verify Book V.1 planar tiling isoperimetry and Book VIII.23 7-hexagon circumradius R = s_6 * sqrt(7)."""
    hon = verify_honeycomb_isoperimetry(12, build_model=True)
    assert hon.tiling_polygons == (3, 4, 6)
    assert hon.interior_angles_deg == {3: 60, 4: 90, 6: 120}
    assert hon.polygons_per_vertex == {3: 6, 4: 4, 6: 3}
    assert hon.side_lengths == {3: 4, 4: 3, 6: 2}
    assert hon.areas == {3: 4 * sp.sqrt(3), 4: 9, 6: 6 * sp.sqrt(3)}
    assert hon.area_hex_over_tri == sp.Rational(3, 2)
    assert sp.simplify(hon.area_hex_over_sq - 2 * sp.sqrt(3) / 3) == 0
    assert sp.simplify(hon.area_sq_over_tri - 3 * sp.sqrt(3) / 4) == 0
    assert sp.simplify(hon.circumradius_seven_hexagons - 2 * sp.sqrt(7)) == 0
    assert hon.model is not None
    _assert_zero_floats_in_model(hon.model)

    mdl = construct_honeycomb_isoperimetry(6)
    _assert_zero_floats_in_model(mdl)


def test_synagoge_svg_gallery_and_cli(tmp_path: Path) -> None:
    """Verify build_synagoge_gallery and pappus CLI synagoge / build --synagoge subcommands."""
    written = build_synagoge_gallery(tmp_path)
    assert len(written) == 6
    expected_names = {
        "synagoge_three_means.svg",
        "synagoge_three_means_golden.svg",
        "pappus_area_theorem.svg",
        "pappus_area_pythagoras.svg",
        "pappus_arbelos_chain.svg",
        "honeycomb_isoperimetry.svg",
    }
    assert {p.name for p in written} == expected_names
    for svg_path in written:
        root = ET.parse(svg_path).getroot()
        assert "euclid-graphic" in root.attrib.get("class", "")
        assert root.attrib.get("data-graphic-id", "").startswith("g")

    assert main(["synagoge", "--demo", "all"]) == 0
    cli_syn_dir = tmp_path / "cli_syn"
    assert main(["synagoge", "--demo", "means", "--build", "-o", str(cli_syn_dir)]) == 0
    assert len(list(cli_syn_dir.glob("*.svg"))) == 6

    cli_full_dir = tmp_path / "cli_full"
    assert main(["build", "--synagoge", "-o", str(cli_full_dir)]) == 0
    assert len(list(cli_full_dir.glob("*.svg"))) == 24


def test_sphinx_ext_greek_track_intersphinx_and_apparatus_parity(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Verify Greek track registration, local intersphinx resolution, and apparatus JSON parity."""
    publish_src = Path("/home/phi/PROJECTS/photon-platform/publish/src")
    if publish_src.is_dir():
        monkeypatch.syspath_prepend(str(publish_src))

    meta = setup(SimpleNamespace())
    assert meta["version"] == "0.2.0"
    register_greek_book_track()

    from photon_platform.publish import book

    fake_env = SimpleNamespace(
        found_docs={
            "synagoge/book_03/prop_01_three_means/index",
            "synagoge/book_03/prop_01_three_means/el",
            "synagoge/book_03/prop_01_three_means/summary",
            "synagoge/book_03/prop_01_three_means/notes",
        },
        metadata={
            "synagoge/book_03/prop_01_three_means/el": {
                "tracks": "English: index | Greek: el | Summary: summary | Notes: notes"
            }
        },
    )
    tracks_from_el = book.detect_companion_tracks(
        fake_env,
        "synagoge/book_03/prop_01_three_means/el",
    )
    track_keys = [tr["key"] for tr in tracks_from_el]
    assert GREEK_TRACK_KEY in track_keys
    assert "index" in track_keys
    active_keys = [tr["key"] for tr in tracks_from_el if tr.get("active")]
    assert active_keys == [GREEK_TRACK_KEY]

    # Verify offline-safe configure_local_intersphinx prunes None targets and binds existing objects.inv
    fake_ws = tmp_path / "geometor"
    fake_pappus = fake_ws / "pappus"
    fake_euclid_docs = fake_ws / "euclid" / "docs"
    fake_euclid_docs.mkdir(parents=True)
    fake_pappus.mkdir(parents=True)
    inv_file = fake_euclid_docs / "objects.inv"
    inv_file.write_bytes(b"# Sphinx inventory version 2\n")

    mapping: dict[str, tuple[str, str | None]] = {
        "remote_unreachable": ("https://example.org/docs", None),
    }
    resolved = configure_local_intersphinx(mapping, project_root=fake_pappus)
    assert "euclid" in resolved
    assert "euclid" in mapping
    assert "remote_unreachable" not in mapping
    sibling_keys = {k for k, _, _ in SIBLING_CODICES}
    assert {"euclid", "elements", "apollonius", "archimedes", "ptolemy", "menelaus"} <= sibling_keys

    # Verify resources/ and resources/synagoge/ JSON apparatus parity
    repo_root = Path(__file__).resolve().parents[1]
    for fname in ("citations.json", "persons.json", "glossary.json"):
        top_data = json.loads((repo_root / "resources" / fname).read_text(encoding="utf-8"))
        sub_data = json.loads((repo_root / "resources" / "synagoge" / fname).read_text(encoding="utf-8"))
        assert top_data == sub_data


def test_synagoge_codex_rst_and_euclid_concordance_integrity() -> None:
    """Verify 5-unit 4-track codex layout, zero py_file blocks, 8 euclid keys, and apparatus anchors."""
    repo_root = Path(__file__).resolve().parents[1]
    synagoge_dir = repo_root / "docsrc" / "synagoge"
    assert (synagoge_dir / "index.rst").is_file()
    assert ":layout: book" in (synagoge_dir / "index.rst").read_text(encoding="utf-8")

    expected_books = {
        "book_03": ("preface", "prop_01_three_means", "golden_means"),
        "book_04": ("prop_01_area_theorem", "prop_14_18_arbelos"),
        "book_05": ("preface_bees", "prop_01_10_isoperimetry"),
        "book_07": (
            "preface_analysis",
            "multi_line_locus",
            "prop_129_cross_ratio",
            "prop_131_harmonic",
            "prop_138_parallel_hexagon",
            "prop_139_intersecting_hexagon",
        ),
        "book_08": (
            "preface_mechanics",
            "prop_01_04_center_of_gravity",
            "prop_23_seven_hexagons",
        ),
    }
    for book_name, units in expected_books.items():
        book_dir = synagoge_dir / book_name
        assert (book_dir / "index.rst").is_file(), f"Missing book index in {book_name}"
        assert (book_dir / "summary.rst").is_file(), f"Missing book summary in {book_name}"
        assert (book_dir / "notes.rst").is_file(), f"Missing book notes in {book_name}"
        for unit in units:
            unit_dir = book_dir / unit
            for track in ("index", "el", "summary", "notes"):
                track_path = unit_dir / f"{track}.rst"
                assert track_path.is_file(), f"Missing codex track {track_path}"

    # Verify all 8 euclid pappus:collectio* citation keys are mapped in concordance.json
    concordance = json.loads(
        (repo_root / "resources" / "synagoge" / "concordance.json").read_text(encoding="utf-8")
    )
    mapped_euclid_keys = {
        key for locus in concordance["loci"] for key in locus.get("euclid_keys", [])
    }
    expected_euclid_keys = {
        "pappus:collectio",
        "pappus:collectio:7",
        "pappus:collectio:iii-p-132",
        "pappus:collectio:iii-p-72-9-23",
        "pappus:collectio:vii-p-670-19",
        "pappus:collectio:vii-p-678",
        "pappus:collectio:vii-p-826",
        "pappus:collectio:vii-p-928",
    }
    assert expected_euclid_keys <= mapped_euclid_keys

    # Collect defined anchors across apparatus pages
    defined_anchors: set[str] = set()
    for app_name in ("bibliography.rst", "persons.rst", "glossary.rst"):
        app_text = (synagoge_dir / app_name).read_text(encoding="utf-8")
        defined_anchors.update(re.findall(r"^\.\. _([a-z0-9-]+):", app_text, flags=re.MULTILINE))

    role_pattern = re.compile(r":(cite|person|term):`([^`]+)`")
    for rst_path in synagoge_dir.rglob("*.rst"):
        text = rst_path.read_text(encoding="utf-8")
        assert ".. py_file::" not in text, f"Forbidden py_file directive in {rst_path}"
        for role_name, raw_target in role_pattern.findall(text):
            key = raw_target.split("<")[-1].rstrip(">").strip()
            slug = re.sub(r"[^a-z0-9]+", "-", key.lower()).strip("-")
            expected_anchor = f"{role_name}-{slug}"
            assert expected_anchor in defined_anchors, (
                f"Unresolved :{role_name}:`{raw_target}` -> {expected_anchor} in {rst_path.name}"
            )

