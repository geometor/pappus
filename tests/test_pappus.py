"""Test suite for ``geometor.pappus`` exact symbolic projective geometry."""
from __future__ import annotations

import xml.etree.ElementTree as ET
from pathlib import Path

import pytest
import sympy as sp
import sympy.geometry as spg

from geometor.pappus import (
    PERMUTATIONS_S3,
    PHI,
    anharmonic_orbit,
    are_coconic,
    canonical_hexagon_cycle,
    circle_stereographic_point,
    conic_cross_ratio,
    conic_equation_through_points,
    construct_harmonic_fourth,
    construct_pappus_configuration,
    construct_pappus_hexagon,
    construct_pascal_hexagon,
    construct_pascal_steiner_family,
    cross_ratio,
    enumerate_hexagrammum_mysticum,
    exact_line_meet,
    export_svg,
    find_golden_sections,
    find_harmonic_ranges,
    get_pascal_preset,
    get_preset,
    harmonic_conjugate_point,
    is_harmonic_range,
    line_spread,
    permutation_parity,
    project_point,
    quadrance,
    render_svg_string,
    verify_pappus_symbolic,
    verify_pascal_symbolic,
)
from geometor.pappus.__main__ import main


def test_universal_symbolic_proof() -> None:
    """Verify Pappus's Hexagon Theorem vanishes identically over 8 free symbols."""
    det = verify_pappus_symbolic()
    assert det == 0


@pytest.mark.parametrize("perm", PERMUTATIONS_S3)
@pytest.mark.parametrize("preset_name", ["hexagon", "parallel", "steiner", "harmonic", "golden"])
def test_hexagon_collinearity_all_permutations_and_presets(
    perm: tuple[int, int, int],
    preset_name: str,
) -> None:
    """Every permutation across all five presets yields collinear cross-join meets."""
    res = construct_pappus_hexagon(preset=preset_name, perm=perm)
    assert res.is_collinear is True
    finite_meets = [pt for pt in res.meets.values() if pt is not None]
    assert len(finite_meets) >= 2
    if preset_name in ("steiner", "harmonic") or perm == (0, 1, 2):
        assert len(finite_meets) == 3
    for pt in finite_meets:
        assert res.pappus_line.contains(pt)
        assert not isinstance(pt.x, sp.Float)
        assert not isinstance(pt.y, sp.Float)


def test_canonical_hexagon_exact_coordinates_and_triangles() -> None:
    """Verify exact coordinates on Synagoge VII.139 and homologous type triangles."""
    res = construct_pappus_hexagon(
        preset="hexagon",
        perm=(0, 1, 2),
        include_hexagon=True,
        include_type_triangles=True,
    )
    assert res.apex == spg.Point(-4, 0)
    assert res.meets["M01"] == spg.Point(sp.Rational(4, 5), sp.Rational(6, 5))
    assert res.meets["M20"] == spg.Point(sp.Rational(60, 37), sp.Rational(50, 37))
    assert res.meets["M12"] == spg.Point(sp.Rational(10, 3), sp.Rational(5, 3))
    assert res.hexagon is not None
    assert set(res.type_triangles) == {"square", "circle", "diamond"}
    for poly in res.type_triangles.values():
        assert abs(poly.area) > 0


def test_parallel_cross_join_ideal_point_case() -> None:
    """When one cross-join pair is parallel, the Pappus line is parallel to that pair."""
    # Under perm=(1, 0, 2), M01 = [A0 B0] ∩ [A1 B1] -> x=0 and x=1 (parallel!)
    res = construct_pappus_hexagon(
        a_points=[(0, 0), (1, 0), (3, 0)],
        b_points=[(0, 1), (1, 1), (4, 1)],
        perm=(1, 0, 2),
    )
    assert res.meets["M01"] is None
    assert res.meets["M12"] is not None
    assert res.meets["M20"] is not None
    assert res.is_collinear is True
    assert line_spread(res.pappus_line, spg.Line(spg.Point(0, 0), spg.Point(0, 1))) == 0


def test_steiner_six_permutation_concurrency_parallel_and_general() -> None:
    """Verify 3-fold concurrency of even and odd Pappus lines at S+ and S-."""
    par = construct_pappus_configuration(preset="parallel")
    assert len(par.pappus_lines) == 6
    # In the 2023 parallel preset, [A0 B1] || [A1 B2] (slope 2/3), so 17 meets are finite and 1 is ideal
    assert len(par.all_meets) == 17
    assert par.steiner_even == spg.Point(sp.Rational(90, 73), sp.Rational(38, 73))
    assert par.steiner_odd == spg.Point(10, sp.Rational(38, 3))
    assert par.steiner_line is not None
    for ln in par.even_pappus_lines:
        assert ln.contains(par.steiner_even)
    for ln in par.odd_pappus_lines:
        assert ln.contains(par.steiner_odd)

    gen = construct_pappus_configuration(preset="steiner")
    assert len(gen.all_meets) == 18
    assert gen.steiner_even == spg.Point(sp.Rational(80, 39), sp.Rational(7, 26))
    assert gen.steiner_odd == spg.Point(sp.Rational(5, 3), sp.Rational(-1, 2))
    assert gen.steiner_line is not None
    for ln in gen.even_pappus_lines:
        assert ln.contains(gen.steiner_even)
    for ln in gen.odd_pappus_lines:
        assert ln.contains(gen.steiner_odd)


def test_cross_ratio_perspectivity_and_projectivity_invariance() -> None:
    """Cross-ratio is invariant under composed central perspectivities (Synagoge VII.129)."""
    line_0 = spg.Line(spg.Point(0, 0), spg.Point(1, 0))
    pts_0 = [spg.Point(0, 0), spg.Point(1, 0), spg.Point(PHI, 0), spg.Point(PHI + 1, 0)]
    cr_0 = cross_ratio(*pts_0)
    assert sp.simplify(cr_0 - PHI) == 0

    # First perspectivity onto oblique line_1 from center O_1
    o_1 = spg.Point(-1, 3)
    line_1 = spg.Line(spg.Point(0, 1), spg.Point(3, 2))
    pts_1 = [project_point(o_1, line_1, p) for p in pts_0]
    cr_1 = cross_ratio(*pts_1)
    assert sp.simplify(cr_1 - cr_0) == 0

    # Second perspectivity onto oblique line_2 from center O_2 (general projectivity)
    o_2 = spg.Point(2, -2)
    line_2 = spg.Line(spg.Point(0, 0), spg.Point(2, 5))
    pts_2 = [project_point(o_2, line_2, p) for p in pts_1]
    cr_2 = cross_ratio(*pts_2)
    assert sp.simplify(cr_2 - cr_0) == 0
    assert line_0 != line_2


def test_anharmonic_orbit_golden_and_harmonic() -> None:
    """Verify the 6-value golden anharmonic orbit and 3-value harmonic collapse."""
    golden_orbit = anharmonic_orbit(PHI)
    assert len(golden_orbit) == 6
    # All 6 values are distinct for phi
    numeric_vals = {round(float(v.evalf()), 8) for v in golden_orbit}
    assert len(numeric_vals) == 6

    harmonic_orbit = set(anharmonic_orbit(sp.Integer(-1)))
    assert harmonic_orbit == {sp.Integer(-1), sp.Rational(1, 2), sp.Integer(2)}


def test_complete_quadrilateral_harmonic_fourth_and_invariance() -> None:
    """Straightedge fourth harmonic matches algebraic formula and is independent of P, Q."""
    r1 = construct_harmonic_fourth(
        pt_a=(0, 0),
        pt_b=(6, 0),
        pt_c=(2, 0),
        apex=(1, 4),
        relay=(sp.Rational(3, 2), 2),
    )
    r2 = construct_harmonic_fourth(
        pt_a=(0, 0),
        pt_b=(6, 0),
        pt_c=(2, 0),
        apex=(-2, -5),
        relay=(0, sp.Rational(-5, 2)),
    )
    alg_d = harmonic_conjugate_point(r1.pt_a, r1.pt_b, r1.pt_c)
    assert r1.pt_d == spg.Point(-6, 0)
    assert r1.pt_d == r2.pt_d
    assert r1.pt_d == alg_d
    assert is_harmonic_range(r1.pt_a, r1.pt_b, r1.pt_c, r1.pt_d)

    # Midpoint has harmonic conjugate at infinity
    with pytest.raises(ValueError, match="midpoint"):
        harmonic_conjugate_point(spg.Point(0, 0), spg.Point(4, 0), spg.Point(2, 0))


def test_golden_harmonic_identity_and_scanners() -> None:
    """Verify (0, phi; 1, phi^3) = -1 and harmonic/golden model scanners."""
    d_gold = harmonic_conjugate_point(spg.Point(0, 0), spg.Point(PHI, 0), spg.Point(1, 0))
    assert sp.simplify(d_gold.x - PHI**3) == 0
    assert is_harmonic_range(spg.Point(0, 0), spg.Point(PHI, 0), spg.Point(1, 0), d_gold)

    base_harm_cfg = construct_pappus_configuration(preset="harmonic", discover_all_intersections=False)
    assert len(base_harm_cfg.harmonic_ranges) == 19

    full_harm_cfg = construct_pappus_configuration(preset="harmonic", discover_all_intersections=True)
    ranges = find_harmonic_ranges(full_harm_cfg.model)
    assert len(ranges) == 81
    for hr in ranges:
        assert hr.value == -1

    gold_hex = construct_pappus_hexagon(preset="golden")
    gold_secs = find_golden_sections(gold_hex.model, register_sections=True)
    assert len(gold_secs) >= 2
    for gs in gold_secs:
        assert sp.simplify(gs.ratio - PHI) == 0


def test_quadrance_spread_and_helpers() -> None:
    """Check Wildberger quadrance, spread, parity,exact_line_meet, and preset errors."""
    assert quadrance(spg.Point(0, 0), spg.Point(3, 4)) == 25
    l_x = spg.Line(spg.Point(0, 0), spg.Point(1, 0))
    l_y = spg.Line(spg.Point(0, 0), spg.Point(0, 1))
    l_diag = spg.Line(spg.Point(0, 0), spg.Point(1, 1))
    assert line_spread(l_x, l_y) == 1
    assert line_spread(l_x, l_diag) == sp.Rational(1, 2)
    assert exact_line_meet(l_x, spg.Line(spg.Point(0, 2), spg.Point(1, 2))) is None
    assert permutation_parity((0, 1, 2)) == "even"
    assert permutation_parity((1, 0, 2)) == "odd"
    with pytest.raises(KeyError):
        get_preset("nonexistent")


def test_svg_rendering_and_cli_gallery(tmp_path: Path) -> None:
    """Verify SVG output is valid XML with interactive Geometor data-ref attributes."""
    hex_res = construct_pappus_hexagon(preset="hexagon")
    svg_str = render_svg_string(hex_res.model, graphic_id="g1")
    root = ET.fromstring(svg_str)
    assert root.attrib["data-graphic-id"] == "g1"
    refs = {el.attrib["data-ref"] for el in root.iter() if "data-ref" in el.attrib}
    for expected_ref in ("A0", "A1", "A2", "B0", "B1", "B2", "M01", "M12", "M20"):
        assert expected_ref in refs

    out_svg = export_svg(hex_res.model, tmp_path / "single.svg")
    assert out_svg.exists()

    # Exercise CLI subcommands
    assert main(["inspect", "--preset", "steiner", "--all-permutations"]) == 0
    assert main(["harmonics", "--preset", "parallel"]) == 0
    assert main(["pascal", "--preset", "hexagrammum"]) == 0
    assert main(["pascal", "--preset", "hexagrammum", "--steiner-family", "--full-60"]) == 0
    gallery_dir = tmp_path / "gallery"
    assert main(["build", "-o", str(gallery_dir)]) == 0
    svg_files = sorted(gallery_dir.glob("*.svg"))
    assert len(svg_files) == 18
    for svg_file in svg_files:
        ET.fromstring(svg_file.read_text(encoding="utf-8"))


def test_universal_pascal_symbolic_proof() -> None:
    """Verify Pascal's Hexagrammum Mysticum vanishes identically over Z[t0..t5]."""
    assert verify_pascal_symbolic() == 0


def test_conic_equation_and_coconicity_unifies_pappus_and_pascal() -> None:
    """are_coconic unifies smooth circles/ellipses and degenerate Pappus line-pairs."""
    # Stereographic points lie strictly on x^2 + y^2 = 1
    for t_val in (sp.Integer(0), sp.Rational(1, 3), PHI):
        pt = circle_stereographic_point(t_val)
        assert sp.simplify(pt.x**2 + pt.y**2 - 1) == 0

    x_sym, y_sym = sp.Symbol("x"), sp.Symbol("y")
    circ_pts = get_pascal_preset("hexagrammum").points
    circ_poly = conic_equation_through_points(circ_pts[:5])
    assert circ_poly != 0
    # Ratio to x^2 + y^2 - 1 must be a nonzero constant
    assert sp.simplify(circ_poly / (x_sym**2 + y_sym**2 - 1)).is_Rational

    ell_pts = get_pascal_preset("ellipse").points
    ell_poly = conic_equation_through_points(ell_pts[:5])
    assert sp.simplify(ell_poly / (x_sym**2 + 4 * y_sym**2 - 4)).is_Rational

    assert are_coconic(circ_pts) is True
    assert are_coconic(ell_pts) is True

    # Degenerate conic: 6 points on two intersecting Pappus lines!
    pap = get_preset("hexagon")
    assert are_coconic(list(pap.a_points) + list(pap.b_points)) is True

    # Perturbing one point off the circle breaks coconicity
    off_conic = list(circ_pts[:5]) + [spg.Point(sp.Integer(2), sp.Integer(3))]
    assert are_coconic(off_conic) is False


def test_chasles_conic_cross_ratio_observer_invariance_and_golden() -> None:
    """Chasles conic cross-ratio is observer-independent and equals PHI on golden_conic."""
    c_pts = get_pascal_preset("hexagrammum").points
    obs_extra = circle_stereographic_point(sp.Integer(2))
    cr_from_p4 = conic_cross_ratio(c_pts[0], c_pts[1], c_pts[2], c_pts[3], c_pts[4])
    cr_from_p5 = conic_cross_ratio(c_pts[0], c_pts[1], c_pts[2], c_pts[3], c_pts[5])
    cr_from_extra = conic_cross_ratio(c_pts[0], c_pts[1], c_pts[2], c_pts[3], obs_extra)
    assert sp.simplify(cr_from_p4 - cr_from_p5) == 0
    assert sp.simplify(cr_from_p4 - cr_from_extra) == 0

    g_pts = get_pascal_preset("golden_conic").points
    g_cr_4 = conic_cross_ratio(g_pts[0], g_pts[1], g_pts[2], g_pts[3], g_pts[4])
    g_cr_5 = conic_cross_ratio(g_pts[0], g_pts[1], g_pts[2], g_pts[3], g_pts[5])
    assert sp.simplify(g_cr_4 - PHI) == 0
    assert sp.simplify(g_cr_5 - PHI) == 0


@pytest.mark.parametrize(
    "cycle",
    [(0, 2, 4, 1, 3, 5), (0, 1, 2, 3, 4, 5), (0, 2, 5, 1, 3, 4)],
)
@pytest.mark.parametrize("preset_name", ["hexagrammum", "convex", "ellipse", "golden_conic"])
def test_pascal_hexagon_collinearity_all_presets_and_cycles(
    preset_name: str,
    cycle: tuple[int, int, int, int, int, int],
) -> None:
    """Every cycle across all four smooth-conic presets yields collinear Pascal meets."""
    res = construct_pascal_hexagon(preset=preset_name, cycle=cycle)
    assert res.is_coconic is True
    assert res.is_collinear is True
    assert len(res.finite_meets) >= 2
    for pt in res.finite_meets:
        assert res.pascal_line.contains(pt)
        assert not isinstance(pt.x, sp.Float)
        assert not isinstance(pt.y, sp.Float)


def test_pascal_exact_coordinates_circle_and_ellipse() -> None:
    """Verify exact rational coordinates on Pythagorean circle and affine ellipse."""
    hex_res = construct_pascal_hexagon(preset="hexagrammum")
    assert hex_res.meets["M03"] == spg.Point(sp.Rational(2, 5), sp.Rational(3, 5))
    assert hex_res.meets["M14"] == spg.Point(sp.Rational(-3, 10), sp.Rational(1, 10))
    assert hex_res.meets["M25"] == spg.Point(sp.Rational(9, 5), sp.Rational(8, 5))

    ell_res = construct_pascal_hexagon(preset="ellipse")
    assert ell_res.meets["M03"] == spg.Point(sp.Rational(4, 5), sp.Rational(3, 5))
    assert ell_res.meets["M14"] == spg.Point(sp.Rational(-3, 5), sp.Rational(1, 10))
    assert ell_res.meets["M25"] == spg.Point(sp.Rational(18, 5), sp.Rational(8, 5))

    with pytest.raises(KeyError):
        get_pascal_preset("unknown_conic")


def test_pascal_steiner_family_concurrency() -> None:
    """Bi-triangle S_3 Pascal lines concur 3-by-3 at Steiner points G+ and G-."""
    fam = construct_pascal_steiner_family(preset="hexagrammum")
    assert len(fam.pascal_lines) == 6
    assert fam.steiner_even == spg.Point(sp.Rational(78, 25), sp.Rational(1, 25))
    assert fam.steiner_odd == spg.Point(sp.Rational(498, 1565), sp.Rational(281, 1565))
    assert fam.steiner_line is not None
    for ln in fam.even_pascal_lines:
        assert ln.contains(fam.steiner_even)
    for ln in fam.odd_pascal_lines:
        assert ln.contains(fam.steiner_odd)


def test_hexagrammum_mysticum_complete_60_line_catalog() -> None:
    """Enumerate all 15 chords, 45 diagonal pts, 60 Pascal lines, 20 Steiner, 60 Kirkman, 15 Plucker."""
    base = (0, 2, 4, 1, 3, 5)
    canon = canonical_hexagon_cycle(base)
    # Check all 12 dihedral rotations and reversals collapse to the same canonical 6-cycle
    for shift in range(6):
        rot = base[shift:] + base[:shift]
        assert canonical_hexagon_cycle(rot) == canon
        assert canonical_hexagon_cycle(tuple(reversed(rot))) == canon

    cat = enumerate_hexagrammum_mysticum(preset="hexagrammum")
    assert len(cat.chords) == 15
    assert len(set(cat.chords.values())) == 15
    assert len(cat.diagonal_points) == 45
    assert len(set(cat.diagonal_points.values())) == 45
    assert len(cat.pascal_lines) == 60
    assert len(set(cat.pascal_lines.values())) == 60
    assert len(cat.steiner_points) == 20
    assert len(set(cat.steiner_points.values())) == 20
    assert len(cat.kirkman_points) == 60
    assert len(set(cat.kirkman_points.values())) == 60
    assert len(cat.plucker_lines) == 15
    assert len(set(cat.plucker_lines)) == 15


def test_golden_pascal_emergent_divine_section_and_conic_svg() -> None:
    """Golden conic discovers / M25 P4 P0 / with ratio PHI and renders <circle>/<ellipse>."""
    gold = construct_pascal_hexagon(preset="golden_conic", enable_divine=True)
    m25 = gold.meets["M25"]
    assert m25 is not None
    assert sp.simplify(m25.x - (-1 / PHI)) == 0
    assert sp.simplify(m25.y - (-PHI)) == 0

    secs = find_golden_sections(gold.model, register_sections=True)
    sec_ids = {gs.point_ids for gs in secs}
    assert ("M25", "P4", "P0") in sec_ids or ("P0", "P4", "M25") in sec_ids
    for gs in secs:
        assert sp.simplify(gs.ratio - PHI) == 0

    svg_gold = ET.fromstring(render_svg_string(gold.model, graphic_id="g4"))
    gold_refs = {el.attrib["data-ref"] for el in svg_gold.iter() if "data-ref" in el.attrib}
    assert "( O P0 )" in gold_refs
    assert "/ M25 P4 P0 /" in gold_refs

    ell = construct_pascal_hexagon(preset="ellipse")
    svg_ell = ET.fromstring(render_svg_string(ell.model, graphic_id="g2"))
    tags = {el.tag.split("}")[-1] for el in svg_ell.iter()}
    assert "ellipse" in tags

