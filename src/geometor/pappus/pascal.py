r"""Symbolic DAG constructions and combinatorics for Blaise Pascal's *Hexagrammum Mysticum* (1640).

Generalizes Pappus's Hexagon Theorem from a degenerate line-pair $a \cup b$ to six
points inscribed on a smooth conic $\mathcal{C}$ (circle or ellipse):

- **Pascal's Mystic Hexagram** (*Essai pour les coniques*, Feb. 1640): for any cyclic
  6-tuple $\langle P_{c_0}, P_{c_1}, P_{c_2}, P_{c_3}, P_{c_4}, P_{c_5} \rangle$ on a conic,
  opposite side intersections $M_{03}, M_{14}, M_{25}$ lie on a single **Pascal line**.
- **Bi-Triangle :math:`S_3` Steiner Family**: partitioning the 6 conic vertices into two
  complementary triangles $\triangle_A$ and $\triangle_B$ generates 6 alternating hexagons
  whose 3 even (:math:`A_3`) Pascal lines concur at :math:`G_+` and whose 3 odd
  (:math:`S_3 \setminus A_3`) Pascal lines concur at :math:`G_-`—directly generalizing
  Pappus's two Star points :math:`(S_+, S_-)`!
- **Complete 60-Line *Hexagrammum Mysticum* Catalog**: exact projective enumeration of all
  15 chords, 45 diagonal Pascal points, 60 Pascal lines, 20 Jakob Steiner points,
  60 Thomas Kirkman points, and 15 Julius Plücker lines.
- **Universal Symbolic Proof & Golden Conic**: exact 6-parameter polynomial proof over
  $\mathbb{Z}[t_0, t_1, t_2, t_3, t_4, t_5]$ and Golden Ratio conic perspectivities over
  $\mathbb{Q}(\phi)$.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, permutations
from typing import Sequence

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model
from geometor.model.element import CircleElement, check_existence

from geometor.pappus.constructions import PERMUTATIONS_S3, Perm3
from geometor.pappus.projective import (
    PHI,
    GoldenRange,
    HarmonicRange,
    are_coconic,
    circle_stereographic_point,
    enable_divine_analysis,
    exact_line_meet,
    find_golden_sections,
    find_harmonic_ranges,
)

PointInput = spg.Point | tuple[sp.Expr | int, sp.Expr | int]
Cycle6 = tuple[int, int, int, int, int, int]
HomVec3 = tuple[sp.Expr, sp.Expr, sp.Expr]

__all__ = [
    "Cycle6",
    "PascalPresetConfig",
    "PASCAL_PRESETS",
    "PascalHexagonResult",
    "PascalSteinerFamilyResult",
    "HexagrammumMysticumCatalog",
    "canonical_hexagon_cycle",
    "get_pascal_preset",
    "construct_pascal_hexagon",
    "construct_pascal_steiner_family",
    "enumerate_hexagrammum_mysticum",
    "verify_pascal_symbolic",
]


@dataclass(frozen=True)
class PascalPresetConfig:
    """Exact coordinate preset for Pascal *Hexagrammum Mysticum* constructions.

    Attributes:
        name: Identifier key in :data:`PASCAL_PRESETS`.
        title: Human-readable preset title.
        description: Mathematical and historical significance of the preset.
        points: Six exact points $(P_0, P_1, P_2, P_3, P_4, P_5)$ on the conic.
        default_cycle: Default cyclic ordering of vertex indices ``0..5``.
        center: Conic center $(x_0, y_0)$ for circle/ellipse rendering.
        rx: Horizontal semi-axis $a$ of the carrier circle/ellipse.
        ry: Vertical semi-axis $b$ of the carrier circle/ellipse.
    """

    name: str
    title: str
    description: str
    points: tuple[spg.Point, spg.Point, spg.Point, spg.Point, spg.Point, spg.Point]
    default_cycle: Cycle6
    center: spg.Point = spg.Point(0, 0)
    rx: sp.Expr = sp.Integer(1)
    ry: sp.Expr = sp.Integer(1)


_PYTHAG_SLOPES: tuple[sp.Expr, ...] = (
    sp.Integer(0),
    sp.Rational(1, 3),
    sp.Integer(1),
    sp.Integer(3),
    sp.Integer(-2),
    sp.Rational(-1, 2),
)
_PYTHAG_PTS = tuple(circle_stereographic_point(t) for t in _PYTHAG_SLOPES)

_CONVEX_SLOPES: tuple[sp.Expr, ...] = (
    sp.Integer(-3),
    sp.Rational(-1, 2),
    sp.Rational(-1, 3),
    sp.Integer(0),
    sp.Rational(1, 4),
    sp.Rational(1, 3),
)
_CONVEX_PTS = tuple(circle_stereographic_point(t) for t in _CONVEX_SLOPES)

_ELLIPSE_PTS = tuple(spg.Point(2 * pt.x, pt.y) for pt in _PYTHAG_PTS)

_GOLDEN_SLOPES: tuple[sp.Expr, ...] = (
    sp.Integer(0),
    sp.Integer(1),
    PHI,
    PHI + 1,
    sp.Integer(-1),
    -PHI,
)
_GOLDEN_PTS = tuple(circle_stereographic_point(t) for t in _GOLDEN_SLOPES)


PASCAL_PRESETS: dict[str, PascalPresetConfig] = {
    "hexagrammum": PascalPresetConfig(
        name="hexagrammum",
        title="Pascal's Mystic Star Hexagram on the Pythagorean Unit Circle",
        description=(
            "Six exact Pythagorean/cardinal points on x^2 + y^2 = 1 across all four quadrants; "
            "mystic cycle (0, 2, 4, 1, 3, 5) yields compact meets (2/5, 3/5), (-3/10, 1/10), "
            "(9/5, 8/5) on 25x - 35y + 11 = 0 and all 60 Pascal lines / 20 Steiner points distinct."
        ),
        points=(
            _PYTHAG_PTS[0],
            _PYTHAG_PTS[1],
            _PYTHAG_PTS[2],
            _PYTHAG_PTS[3],
            _PYTHAG_PTS[4],
            _PYTHAG_PTS[5],
        ),
        default_cycle=(0, 2, 4, 1, 3, 5),
    ),
    "convex": PascalPresetConfig(
        name="convex",
        title="Convex Cyclic Hexagon on the Unit Circle",
        description=(
            "Strictly convex inscribed hexagon (0, 1, 2, 3, 4, 5) on x^2 + y^2 = 1 with "
            "compact external meets (11/9, -8/9), (19/15, -2/15), (4/3, 1) on 15x - 2y = 20."
        ),
        points=(
            _CONVEX_PTS[0],
            _CONVEX_PTS[1],
            _CONVEX_PTS[2],
            _CONVEX_PTS[3],
            _CONVEX_PTS[4],
            _CONVEX_PTS[5],
        ),
        default_cycle=(0, 1, 2, 3, 4, 5),
    ),
    "ellipse": PascalPresetConfig(
        name="ellipse",
        title="Pascal's Hexagrammum on the General Ellipse x^2/4 + y^2 = 1",
        description=(
            "Affine transformation (x, y) -> (2x, y) of the Pythagorean hexagram onto "
            "the non-circular ellipse x^2 + 4y^2 = 4, demonstrating projective conic invariance."
        ),
        points=(
            _ELLIPSE_PTS[0],
            _ELLIPSE_PTS[1],
            _ELLIPSE_PTS[2],
            _ELLIPSE_PTS[3],
            _ELLIPSE_PTS[4],
            _ELLIPSE_PTS[5],
        ),
        default_cycle=(0, 2, 4, 1, 3, 5),
        rx=sp.Integer(2),
        ry=sp.Integer(1),
    ),
    "golden_conic": PascalPresetConfig(
        name="golden_conic",
        title="Golden Hexagrammum Mysticum in Q(phi)",
        description=(
            "Unit circle seeded with stereographic golden chain (0, 1, phi, phi + 1, -1, -phi): "
            "Chasles conic cross-ratio equals phi, M25 = (-1/phi, -phi), and geometor.divine "
            "uncovers the emergent golden section / M25 P4 P0 /."
        ),
        points=(
            _GOLDEN_PTS[0],
            _GOLDEN_PTS[1],
            _GOLDEN_PTS[2],
            _GOLDEN_PTS[3],
            _GOLDEN_PTS[4],
            _GOLDEN_PTS[5],
        ),
        default_cycle=(0, 2, 5, 1, 3, 4),
    ),
}


@dataclass
class PascalHexagonResult:
    r"""Structured output from :func:`construct_pascal_hexagon`.

    Attributes:
        model: Populated :class:`~geometor.model.Model`.
        points: Six conic vertices $(P_0, P_1, P_2, P_3, P_4, P_5)$.
        cycle: Active 6-cycle $(c_0, c_1, c_2, c_3, c_4, c_5)$.
        conic: Constructed :class:`~sympy.geometry.ellipse.Circle` or :class:`~sympy.geometry.ellipse.Ellipse`, if registered.
        side_lines: Six side lines in cyclic order.
        meets: Opposite-side meets ``{"M03": ..., "M14": ..., "M25": ...}``.
        finite_meets: List of finite opposite-side meets.
        pascal_line: Exact Pascal line joining the opposite-side meets.
        hexagon: Optional inscribed 6-gon :class:`~sympy.geometry.polygon.Polygon`.
        is_collinear: Exact algebraic check that all three opposite-side meets are collinear.
        is_coconic: Exact Veronese determinant check that all six vertices lie on a conic.
    """

    model: Model
    points: tuple[spg.Point, spg.Point, spg.Point, spg.Point, spg.Point, spg.Point]
    cycle: Cycle6
    conic: spg.Ellipse | None
    side_lines: tuple[spg.Line, spg.Line, spg.Line, spg.Line, spg.Line, spg.Line]
    meets: dict[str, spg.Point | None]
    finite_meets: list[spg.Point]
    pascal_line: spg.Line
    hexagon: spg.Polygon | None
    is_collinear: bool
    is_coconic: bool


@dataclass
class PascalSteinerFamilyResult:
    r"""Structured output from :func:`construct_pascal_steiner_family`.

    Attributes:
        model: Populated :class:`~geometor.model.Model`.
        points: Six conic vertices $(P_0, \dots, P_5)$.
        triangle_a: Vertex indices $(a_0, a_1, a_2)$ of the first inscribed triangle.
        triangle_b: Vertex indices $(b_0, b_1, b_2)$ of the complementary inscribed triangle.
        conic: Constructed circle or ellipse carrier curve.
        chords: Mapping ``(a_i, b_j) -> Line`` for the 9 cross-chords.
        pascal_lines: Mapping ``perm -> Line`` for all 6 :math:`S_3` alternating hexagons.
        even_pascal_lines: Tuple of the 3 even (:math:`A_3`) Pascal lines.
        odd_pascal_lines: Tuple of the 3 odd (:math:`S_3 \setminus A_3`) Pascal lines.
        steiner_even: Even Steiner concurrency point :math:`G_+` (ID ``"S1"``), if finite.
        steiner_odd: Odd Steiner concurrency point :math:`G_-` (ID ``"S2"``), if finite.
        steiner_line: Line :math:`[G_+ G_-]` joining the two Steiner points, if finite.
        harmonic_ranges: Discovered collinear harmonic tetrads.
        golden_sections: Discovered golden sections.
    """

    model: Model
    points: tuple[spg.Point, spg.Point, spg.Point, spg.Point, spg.Point, spg.Point]
    triangle_a: tuple[int, int, int]
    triangle_b: tuple[int, int, int]
    conic: spg.Ellipse | None
    chords: dict[tuple[int, int], spg.Line]
    pascal_lines: dict[Perm3, spg.Line]
    even_pascal_lines: tuple[spg.Line, spg.Line, spg.Line]
    odd_pascal_lines: tuple[spg.Line, spg.Line, spg.Line]
    steiner_even: spg.Point | None
    steiner_odd: spg.Point | None
    steiner_line: spg.Line | None
    harmonic_ranges: list[HarmonicRange]
    golden_sections: list[GoldenRange]


@dataclass(frozen=True)
class HexagrammumMysticumCatalog:
    r"""Complete projective catalog of the 60-line *Hexagrammum Mysticum* configuration.

    Attributes:
        points: Six exact conic vertices $(P_0, \dots, P_5)$.
        chords: Mapping ``(i, j) -> (a, b, c)`` homogeneous line coordinates for all 15 chords.
        diagonal_points: Mapping ``((i, j), (k, l)) -> (X, Y, Z)`` for all 45 Pascal diagonal points.
        pascal_lines: Mapping ``canonical_cycle -> (a, b, c)`` for all 60 Pascal lines.
        steiner_points: Mapping ``(triangle_a, parity) -> (X, Y, Z)`` for all 20 Steiner points.
        kirkman_points: Mapping ``(cyc_1, cyc_2, cyc_3) -> (X, Y, Z)`` for all 60 Kirkman points.
        plucker_lines: Tuple of 15 homogeneous line triples each incident with 4 Steiner points.
    """

    points: tuple[spg.Point, spg.Point, spg.Point, spg.Point, spg.Point, spg.Point]
    chords: dict[tuple[int, int], HomVec3]
    diagonal_points: dict[tuple[tuple[int, int], tuple[int, int]], HomVec3]
    pascal_lines: dict[Cycle6, HomVec3]
    steiner_points: dict[tuple[tuple[int, int, int], str], HomVec3]
    kirkman_points: dict[tuple[Cycle6, Cycle6, Cycle6], HomVec3]
    plucker_lines: tuple[HomVec3, ...]


def get_pascal_preset(name: str) -> PascalPresetConfig:
    """Look up a named Pascal preset in :data:`PASCAL_PRESETS`.

    Args:
        name: Preset key (``"hexagrammum"``, ``"convex"``, ``"ellipse"``, or ``"golden_conic"``).

    Returns:
        Matching :class:`PascalPresetConfig`.

    Raises:
        KeyError: If ``name`` is unknown.
    """
    if name not in PASCAL_PRESETS:
        valid = ", ".join(sorted(PASCAL_PRESETS))
        raise KeyError(f"Unknown Pascal preset {name!r}. Valid presets: {valid}")
    return PASCAL_PRESETS[name]


def canonical_hexagon_cycle(cycle: Sequence[int]) -> Cycle6:
    """Normalize a 6-vertex permutation up to dihedral rotation and reversal ($D_6$).

    Rotates ``cycle`` so ``0`` appears first and picks the lexicographically smaller
    orientation between ``(0, c1, c2, c3, c4, c5)`` and ``(0, c5, c4, c3, c2, c1)``.

    Args:
        cycle: Permutation of ``(0, 1, 2, 3, 4, 5)``.

    Returns:
        Canonical 6-tuple representative among the $6! / 12 = 60$ distinct hexagons.

    Raises:
        ValueError: If ``cycle`` is not a permutation of ``0..5``.
    """
    tup = tuple(int(k) for k in cycle)
    if len(tup) != 6 or set(tup) != {0, 1, 2, 3, 4, 5}:
        raise ValueError(f"Expected permutation of (0, 1, 2, 3, 4, 5), got {cycle!r}")
    idx0 = tup.index(0)
    rot = tup[idx0:] + tup[:idx0]
    rev = (0, rot[5], rot[4], rot[3], rot[2], rot[1])
    best = rot if rot < rev else rev
    return (best[0], best[1], best[2], best[3], best[4], best[5])


def _coerce_point(pt: PointInput) -> spg.Point:
    if isinstance(pt, spg.Point):
        return pt
    return spg.Point(sp.sympify(pt[0]), sp.sympify(pt[1]))


def _add_line(
    model: Model,
    pt_1: spg.Point,
    pt_2: spg.Point,
    *,
    classes: list[str] | None = None,
    line_id: str = "",
    guide: bool = False,
) -> spg.Line:
    cls_list = list(classes) if classes else []
    constructed = model.construct_line(pt_1, pt_2, classes=cls_list, ID=line_id, guide=True)
    if constructed is None:
        _, existing = check_existence(model, spg.Line(pt_1, pt_2), model.lines)
        if existing is None or not isinstance(existing, spg.Line):
            raise RuntimeError("Expected existing line in model after duplicate construct_line.")
        line_obj = existing
    else:
        line_obj = constructed
    if not guide:
        model[line_obj].guide = False
    return line_obj


def _register_intersection_point(
    model: Model,
    pt: spg.Point,
    line_1: spg.Line,
    line_2: spg.Line,
    *,
    classes: list[str] | None = None,
    pt_id: str = "",
    guide: bool = False,
) -> spg.Point:
    pt_model = model.set_point(
        pt.x,
        pt.y,
        parents=[line_1, line_2],
        classes=list(classes) if classes else [],
        ID=pt_id,
        guide=guide,
    )
    model[line_1].parents[pt_model] = ""
    model[line_2].parents[pt_model] = ""
    return pt_model


def _register_conic_curve(
    model: Model,
    points: Sequence[spg.Point],
    *,
    center: spg.Point | None,
    rx: sp.Expr | None,
    ry: sp.Expr | None,
) -> spg.Ellipse | None:
    """Register an exact Circle in ``model`` or attach an Ellipse carrier curve."""
    if center is None or rx is None or ry is None:
        return None

    rx_s = sp.sympify(rx)
    ry_s = sp.sympify(ry)
    if sp.simplify(rx_s - ry_s) == 0:
        pt_o = model.set_point(center.x, center.y, classes=["aux", "center"], ID="O")
        circ = spg.Circle(pt_o, rx_s)
        if not all(circ.contains(p) for p in points):
            return None
        circ_id = f"( O {model[points[0]].ID} )"
        details = CircleElement(
            circ,
            parents=[pt_o, points[0]],
            classes=["conic", "circle"],
            ID=circ_id,
            pt_radius=points[0],
            guide=False,
        )
        for p in points:
            details.parents[p] = ""
        model[circ] = details
        return circ

    ell = spg.Ellipse(center, rx_s, ry_s)
    if not all(ell.contains(p) for p in points):
        return None
    model.set_point(center.x, center.y, classes=["aux", "center"], ID="O")
    ell_id = f"( O {model[points[0]].ID} )"
    extra: list[tuple[spg.Ellipse, str]] = list(getattr(model, "_extra_conics", ()))
    extra.append((ell, ell_id))
    setattr(model, "_extra_conics", extra)
    return ell


def construct_pascal_hexagon(
    model: Model | None = None,
    points: Sequence[PointInput] | None = None,
    cycle: Sequence[int] | None = None,
    *,
    preset: str = "hexagrammum",
    include_conic: bool = True,
    include_hexagon: bool = True,
    enable_divine: bool = False,
) -> PascalHexagonResult:
    """Construct Blaise Pascal's *Hexagrammum Mysticum* for six points on a conic.

    Args:
        model: Optional existing :class:`~geometor.model.Model`; created if ``None``.
        points: Optional sequence of 6 coconic points; defaults to ``preset``.
        cycle: Optional cyclic ordering of ``0..5``; defaults to the preset's ``default_cycle``.
        preset: Key in :data:`PASCAL_PRESETS` used when ``points`` is ``None``.
        include_conic: If True and carrier circle/ellipse parameters are known, register the conic.
        include_hexagon: If True, register the 6-gon polygon ``< P_c0 ... P_c5 >``.
        enable_divine: If True, attach :mod:`geometor.divine` golden section hook.

    Returns:
        Populated :class:`PascalHexagonResult`.

    Raises:
        ValueError: If fewer/more than 6 distinct coconic points are provided or if
            two or more opposite-side pairs are parallel.
    """
    cfg = get_pascal_preset(preset)
    raw_pts = tuple(_coerce_point(p) for p in points) if points is not None else cfg.points
    if len(raw_pts) != 6 or len(set(raw_pts)) != 6:
        raise ValueError("Expected 6 distinct points for Pascal's Hexagrammum.")

    is_cocon = are_coconic(raw_pts)
    if not is_cocon:
        raise ValueError("Provided 6 points do not lie on a common conic section.")

    cyc_raw = tuple(int(k) for k in cycle) if cycle is not None else cfg.default_cycle
    if len(cyc_raw) != 6 or set(cyc_raw) != {0, 1, 2, 3, 4, 5}:
        raise ValueError(f"Invalid 6-cycle {cycle!r}; expected permutation of 0..5.")
    cyc: Cycle6 = (cyc_raw[0], cyc_raw[1], cyc_raw[2], cyc_raw[3], cyc_raw[4], cyc_raw[5])

    if model is None:
        model = Model(f"pascal_{preset}_{''.join(map(str, cyc))}")
    if enable_divine:
        enable_divine_analysis(model)

    p_mod = tuple(
        model.set_point(
            pt.x,
            pt.y,
            classes=["given", "conic_pt", f"pt_{ 'a' if idx % 2 == 0 else 'b' }"],
            ID=f"P{idx}",
        )
        for idx, pt in enumerate(raw_pts)
    )
    pts6 = (p_mod[0], p_mod[1], p_mod[2], p_mod[3], p_mod[4], p_mod[5])

    conic_obj: spg.Ellipse | None = None
    if include_conic:
        if points is None:
            conic_obj = _register_conic_curve(
                model,
                pts6,
                center=cfg.center,
                rx=cfg.rx,
                ry=cfg.ry,
            )
        else:
            # Auto-detect circle through first 3 points if all 6 lie on it
            if not spg.Point.is_collinear(pts6[0], pts6[1], pts6[2]):
                cand_circ = spg.Circle(pts6[0], pts6[1], pts6[2])
                if all(cand_circ.contains(p) for p in pts6):
                    conic_obj = _register_conic_curve(
                        model,
                        pts6,
                        center=cand_circ.center,
                        rx=cand_circ.radius,
                        ry=cand_circ.radius,
                    )

    cyc_pts = [pts6[k] for k in cyc]
    sides: list[spg.Line] = []
    for k in range(6):
        u_idx = cyc[k]
        v_idx = cyc[(k + 1) % 6]
        ln = _add_line(
            model,
            cyc_pts[k],
            cyc_pts[(k + 1) % 6],
            classes=["cross", f"pair_{k % 3}"],
            line_id=f"[ P{u_idx} P{v_idx} ]",
        )
        sides.append(ln)

    meet_specs = [
        ("M03", sides[0], sides[3]),
        ("M14", sides[1], sides[4]),
        ("M25", sides[2], sides[5]),
    ]
    meets: dict[str, spg.Point | None] = {}
    for mid, ln_1, ln_2 in meet_specs:
        pt_m = exact_line_meet(ln_1, ln_2)
        if pt_m is not None:
            pt_m = _register_intersection_point(
                model,
                pt_m,
                ln_1,
                ln_2,
                classes=["meet", "even"],
                pt_id=mid,
            )
        meets[mid] = pt_m

    finite_meets = [m for m in (meets["M03"], meets["M14"], meets["M25"]) if m is not None]
    if len(finite_meets) < 2:
        raise ValueError("At least two opposite side pairs are parallel; Pascal line is ideal.")

    pascal_line = _add_line(
        model,
        finite_meets[0],
        finite_meets[1],
        classes=["pappus", "pascal", "even"],
        line_id=f"[ {model[finite_meets[0]].ID} {model[finite_meets[1]].ID} ]",
    )
    if len(finite_meets) == 3:
        is_col = bool(spg.Point.is_collinear(*finite_meets))
        model[finite_meets[2]].parents[pascal_line] = ""
        model[pascal_line].parents[finite_meets[2]] = ""
    else:
        missing_idx = next(i for i, (_, l1, _) in enumerate(meet_specs) if meets[meet_specs[i][0]] is None)
        par_side = meet_specs[missing_idx][1]
        is_col = sp.simplify(
            pascal_line.coefficients[0] * par_side.coefficients[1]
            - pascal_line.coefficients[1] * par_side.coefficients[0]
        ) == 0

    hex_poly: spg.Polygon | None = None
    if include_hexagon:
        hex_poly = model.set_polygon(cyc_pts, classes=["hexagon"])

    return PascalHexagonResult(
        model=model,
        points=pts6,
        cycle=cyc,
        conic=conic_obj,
        side_lines=(sides[0], sides[1], sides[2], sides[3], sides[4], sides[5]),
        meets=meets,
        finite_meets=finite_meets,
        pascal_line=pascal_line,
        hexagon=hex_poly,
        is_collinear=is_col,
        is_coconic=is_cocon,
    )


def construct_pascal_steiner_family(
    model: Model | None = None,
    points: Sequence[PointInput] | None = None,
    *,
    preset: str = "hexagrammum",
    triangle_a: tuple[int, int, int] = (0, 2, 4),
    triangle_b: tuple[int, int, int] = (1, 3, 5),
    include_conic: bool = True,
    scan_harmonics: bool = True,
    enable_divine: bool = False,
) -> PascalSteinerFamilyResult:
    r"""Construct the 6-hexagon :math:`S_3` bi-triangle Pascal family and its two Steiner points.

    Partitions the 6 conic vertices into $\triangle_A = (P_{a_0}, P_{a_1}, P_{a_2})$ and
    $\triangle_B = (P_{b_0}, P_{b_1}, P_{b_2})$. Permuting $\triangle_B$ by $\sigma \in S_3$
    forms 6 alternating hexagons $\langle A_0, B_{\sigma_0}, A_1, B_{\sigma_1}, A_2, B_{\sigma_2} \rangle$
    whose 3 even (:math:`A_3`) Pascal lines concur at :math:`G_+` (ID ``"S1"``) and whose
    3 odd (:math:`S_3 \setminus A_3`) Pascal lines concur at :math:`G_-` (ID ``"S2"``).

    Args:
        model: Optional existing :class:`~geometor.model.Model`.
        points: Optional sequence of 6 coconic points; defaults to ``preset``.
        preset: Key in :data:`PASCAL_PRESETS` used when ``points`` is ``None``.
        triangle_a: Indices $(a_0, a_1, a_2)$ of the first inscribed triangle.
        triangle_b: Complementary indices $(b_0, b_1, b_2)$ of the second triangle.
        include_conic: If True, register the carrier circle or ellipse.
        scan_harmonics: If True, scan the configuration for collinear harmonic tetrads.
        enable_divine: If True, attach :mod:`geometor.divine` and scan golden sections.

    Returns:
        Populated :class:`PascalSteinerFamilyResult`.

    Raises:
        ValueError: If ``triangle_a`` and ``triangle_b`` do not partition ``0..5`` or
            points are not coconic.
    """
    if set(triangle_a) | set(triangle_b) != {0, 1, 2, 3, 4, 5} or set(triangle_a) & set(triangle_b):
        raise ValueError("triangle_a and triangle_b must partition {0, 1, 2, 3, 4, 5}.")

    cfg = get_pascal_preset(preset)
    raw_pts = tuple(_coerce_point(p) for p in points) if points is not None else cfg.points
    if len(raw_pts) != 6 or not are_coconic(raw_pts):
        raise ValueError("Expected 6 distinct coconic points.")

    if model is None:
        model = Model(f"pascal_steiner_{preset}")
    if enable_divine:
        enable_divine_analysis(model)

    p_mod = tuple(
        model.set_point(
            pt.x,
            pt.y,
            classes=["given", "conic_pt", "pt_a" if idx in triangle_a else "pt_b"],
            ID=f"P{idx}",
        )
        for idx, pt in enumerate(raw_pts)
    )
    pts6 = (p_mod[0], p_mod[1], p_mod[2], p_mod[3], p_mod[4], p_mod[5])

    conic_obj: spg.Ellipse | None = None
    if include_conic and points is None:
        conic_obj = _register_conic_curve(model, pts6, center=cfg.center, rx=cfg.rx, ry=cfg.ry)

    # All 9 cross-chords between triangle_a and triangle_b
    chords: dict[tuple[int, int], spg.Line] = {}
    for ai in triangle_a:
        for bj in triangle_b:
            chords[(ai, bj)] = _add_line(
                model,
                pts6[ai],
                pts6[bj],
                classes=["cross"],
                line_id=f"[ P{ai} P{bj} ]",
            )

    even_perms: set[Perm3] = {(0, 1, 2), (1, 2, 0), (2, 0, 1)}
    pascal_lines: dict[Perm3, spg.Line] = {}
    even_lines: list[spg.Line] = []
    odd_lines: list[spg.Line] = []
    seen_meets: dict[tuple[sp.Expr, sp.Expr], spg.Point] = {}

    for perm in PERMUTATIONS_S3:
        parity = "even" if perm in even_perms else "odd"
        a0, a1, a2 = triangle_a
        b0, b1, b2 = triangle_b[perm[0]], triangle_b[perm[1]], triangle_b[perm[2]]
        # Hexagon <a0, b0, a1, b1, a2, b2> has opposite sides:
        # ([a0 b0], [b1 a2]), ([b0 a1], [a2 b2]), ([a1 b1], [b2 a0])
        opp_pairs = [
            (chords[(a0, b0)], chords[(a2, b1)], f"M{a0}{b0}{a2}{b1}"),
            (chords[(a1, b0)], chords[(a2, b2)], f"M{a1}{b0}{a2}{b2}"),
            (chords[(a1, b1)], chords[(a0, b2)], f"M{a1}{b1}{a0}{b2}"),
        ]
        p_meets: list[spg.Point] = []
        for l1, l2, mid in opp_pairs:
            pt_m = exact_line_meet(l1, l2)
            if pt_m is not None:
                coord_key = (pt_m.x, pt_m.y)
                if coord_key in seen_meets:
                    pt_reg = seen_meets[coord_key]
                else:
                    pt_reg = _register_intersection_point(
                        model,
                        pt_m,
                        l1,
                        l2,
                        classes=["meet", parity],
                        pt_id=mid,
                    )
                    seen_meets[coord_key] = pt_reg
                p_meets.append(pt_reg)

        p_ln = _add_line(
            model,
            p_meets[0],
            p_meets[1],
            classes=["pappus", "pascal", parity],
            line_id=f"[ {model[p_meets[0]].ID} {model[p_meets[1]].ID} ]",
        )
        if len(p_meets) == 3:
            model[p_meets[2]].parents[p_ln] = ""
            model[p_ln].parents[p_meets[2]] = ""
        pascal_lines[perm] = p_ln
        if parity == "even":
            even_lines.append(p_ln)
        else:
            odd_lines.append(p_ln)

    s_even = exact_line_meet(even_lines[0], even_lines[1])
    if s_even is not None:
        if not even_lines[2].contains(s_even):
            raise AssertionError("Steiner concurrency failed on even Pascal lines.")
        s_even = _register_intersection_point(
            model,
            s_even,
            even_lines[0],
            even_lines[1],
            classes=["steiner", "even_star"],
            pt_id="S1",
        )
        model[s_even].parents[even_lines[2]] = ""
        model[even_lines[2]].parents[s_even] = ""

    s_odd = exact_line_meet(odd_lines[0], odd_lines[1])
    if s_odd is not None:
        if not odd_lines[2].contains(s_odd):
            raise AssertionError("Steiner concurrency failed on odd Pascal lines.")
        s_odd = _register_intersection_point(
            model,
            s_odd,
            odd_lines[0],
            odd_lines[1],
            classes=["steiner", "odd_star"],
            pt_id="S2",
        )
        model[s_odd].parents[odd_lines[2]] = ""
        model[odd_lines[2]].parents[s_odd] = ""

    s_line: spg.Line | None = None
    if s_even is not None and s_odd is not None and s_even != s_odd:
        s_line = _add_line(
            model,
            s_even,
            s_odd,
            classes=["steiner_line"],
            line_id="[ S1 S2 ]",
        )

    harmonics = find_harmonic_ranges(model) if scan_harmonics else []
    goldens = find_golden_sections(model, register_sections=enable_divine) if enable_divine else []

    return PascalSteinerFamilyResult(
        model=model,
        points=pts6,
        triangle_a=triangle_a,
        triangle_b=triangle_b,
        conic=conic_obj,
        chords=chords,
        pascal_lines=pascal_lines,
        even_pascal_lines=(even_lines[0], even_lines[1], even_lines[2]),
        odd_pascal_lines=(odd_lines[0], odd_lines[1], odd_lines[2]),
        steiner_even=s_even,
        steiner_odd=s_odd,
        steiner_line=s_line,
        harmonic_ranges=harmonics,
        golden_sections=goldens,
    )


def _cross3(u: HomVec3, v: HomVec3) -> HomVec3:
    return (
        u[1] * v[2] - u[2] * v[1],
        u[2] * v[0] - u[0] * v[2],
        u[0] * v[1] - u[1] * v[0],
    )


def _dot3(u: HomVec3, v: HomVec3) -> sp.Expr:
    return sp.simplify(u[0] * v[0] + u[1] * v[1] + u[2] * v[2])


def _norm_hom3(v: HomVec3) -> HomVec3:
    for k in range(3):
        val = sp.simplify(v[k])
        if val != 0:
            return (
                sp.simplify(v[0] / val),
                sp.simplify(v[1] / val),
                sp.simplify(v[2] / val),
            )
    raise ValueError("Degenerate zero homogeneous vector in Hexagrammum Mysticum.")


def enumerate_hexagrammum_mysticum(
    points: Sequence[PointInput] | None = None,
    *,
    preset: str = "hexagrammum",
) -> HexagrammumMysticumCatalog:
    r"""Enumerate and verify the complete 60-line *Hexagrammum Mysticum* web in $\mathbb{P}^2$.

    Computes in exact homogeneous coordinates:

    1. **15 Chords** $[P_i P_j]$ ($0 \le i < j \le 5$).
    2. **45 Diagonal Pascal Points** $[P_i P_j] \cap [P_k P_l]$ on disjoint vertex pairs.
    3. **60 Pascal Lines** across all $6! / 12 = 60$ cyclic hexagons, verifying 3-point collinearity.
    4. **20 Jakob Steiner Points** ($10$ triangle partitions $\times 2$ :math:`S_3` parities),
       verifying 3-line concurrency at each point.
    5. **60 Thomas Kirkman Points**, verifying 3-line concurrency on each syntheme Kirkman triple.
    6. **15 Julius Plücker Lines**, each carrying 4 of the 20 Steiner points.

    Args:
        points: Optional sequence of 6 coconic points; defaults to ``preset``.
        preset: Key in :data:`PASCAL_PRESETS` used when ``points`` is ``None``.

    Returns:
        Populated :class:`HexagrammumMysticumCatalog`.

    Raises:
        ValueError: If fewer/more than 6 distinct coconic points are given.
    """
    cfg = get_pascal_preset(preset)
    raw_pts = tuple(_coerce_point(p) for p in points) if points is not None else cfg.points
    if len(raw_pts) != 6 or not are_coconic(raw_pts):
        raise ValueError("Expected 6 distinct coconic points.")
    pts6 = (raw_pts[0], raw_pts[1], raw_pts[2], raw_pts[3], raw_pts[4], raw_pts[5])
    hpts: list[HomVec3] = [(p.x, p.y, sp.Integer(1)) for p in pts6]

    # 1. 15 chords (unordered pairs normalized with i < j)
    chords: dict[tuple[int, int], HomVec3] = {}
    for i, j in combinations(range(6), 2):
        chords[(i, j)] = _norm_hom3(_cross3(hpts[i], hpts[j]))

    def _chord(u: int, v: int) -> HomVec3:
        return chords[(u, v)] if u < v else chords[(v, u)]

    # 2. 45 diagonal Pascal points
    diagonal_points: dict[tuple[tuple[int, int], tuple[int, int]], HomVec3] = {}
    for e1, e2 in combinations(sorted(chords.keys()), 2):
        if len({e1[0], e1[1], e2[0], e2[1]}) == 4:
            diagonal_points[(e1, e2)] = _norm_hom3(_cross3(chords[e1], chords[e2]))

    def _diag(u1: int, v1: int, u2: int, v2: int) -> HomVec3:
        p1 = (u1, v1) if u1 < v1 else (v1, u1)
        p2 = (u2, v2) if u2 < v2 else (v2, u2)
        key = (p1, p2) if p1 < p2 else (p2, p1)
        return diagonal_points[key]

    # 3. 60 canonical hexagons & 60 Pascal lines
    hexagons: list[Cycle6] = []
    for pm in permutations(range(1, 6)):
        cand = (0, pm[0], pm[1], pm[2], pm[3], pm[4])
        rev = (0, pm[4], pm[3], pm[2], pm[1], pm[0])
        if cand < rev:
            hexagons.append(cand)

    pascal_lines: dict[Cycle6, HomVec3] = {}
    for cyc in hexagons:
        m03 = _diag(cyc[0], cyc[1], cyc[3], cyc[4])
        m14 = _diag(cyc[1], cyc[2], cyc[4], cyc[5])
        m25 = _diag(cyc[2], cyc[3], cyc[5], cyc[0])
        ln = _norm_hom3(_cross3(m03, m14))
        if _dot3(ln, m25) != 0:
            raise AssertionError(f"Pascal collinearity failed on cycle {cyc}.")
        pascal_lines[cyc] = ln

    # 4. 20 Jakob Steiner points (10 complementary triangle partitions x 2 S_3 parities)
    steiner_points: dict[tuple[tuple[int, int, int], str], HomVec3] = {}
    for tri_a in combinations(range(6), 3):
        if 0 not in tri_a:
            continue
        tri_b_list = [k for k in range(6) if k not in tri_a]
        tri_b = (tri_b_list[0], tri_b_list[1], tri_b_list[2])
        tri_a_t = (tri_a[0], tri_a[1], tri_a[2])
        for parity_label, pms in (
            ("even", ((0, 1, 2), (1, 2, 0), (2, 0, 1))),
            ("odd", ((0, 2, 1), (1, 0, 2), (2, 1, 0))),
        ):
            cycs = [
                canonical_hexagon_cycle(
                    (tri_a_t[0], tri_b[pm[0]], tri_a_t[1], tri_b[pm[1]], tri_a_t[2], tri_b[pm[2]])
                )
                for pm in pms
            ]
            gpt = _norm_hom3(_cross3(pascal_lines[cycs[0]], pascal_lines[cycs[1]]))
            if _dot3(pascal_lines[cycs[2]], gpt) != 0:
                raise AssertionError(f"Steiner concurrency failed on {tri_a_t} ({parity_label}).")
            steiner_points[(tri_a_t, parity_label)] = gpt

    # 5. 60 Thomas Kirkman points via dihedral syntheme triples
    kirkman_triples: set[tuple[Cycle6, Cycle6, Cycle6]] = set()
    for cyc in hexagons:
        for shift in range(6):
            x = cyc[shift:] + cyc[:shift]
            c1 = canonical_hexagon_cycle(x)
            c2 = canonical_hexagon_cycle((x[0], x[1], x[3], x[2], x[5], x[4]))
            c3 = canonical_hexagon_cycle((x[0], x[4], x[3], x[1], x[2], x[5]))
            ordered = tuple(sorted((c1, c2, c3)))
            kirkman_triples.add((ordered[0], ordered[1], ordered[2]))

    kirkman_points: dict[tuple[Cycle6, Cycle6, Cycle6], HomVec3] = {}
    for kt in sorted(kirkman_triples):
        kpt = _norm_hom3(_cross3(pascal_lines[kt[0]], pascal_lines[kt[1]]))
        if _dot3(pascal_lines[kt[2]], kpt) != 0:
            raise AssertionError(f"Kirkman concurrency failed on triple {kt}.")
        kirkman_points[kt] = kpt

    # 6. 15 Julius Plucker lines (each incident with 4 Steiner points)
    plucker_counts: dict[HomVec3, set[tuple[tuple[int, int, int], str]]] = {}
    s_items = list(steiner_points.items())
    for (k1, p1), (k2, p2) in combinations(s_items, 2):
        if p1 == p2:
            continue
        pln = _norm_hom3(_cross3(p1, p2))
        plucker_counts.setdefault(pln, set()).update((k1, k2))

    plucker_lines = tuple(
        ln for ln, keys in plucker_counts.items() if len(keys) >= 4
    )

    return HexagrammumMysticumCatalog(
        points=pts6,
        chords=chords,
        diagonal_points=diagonal_points,
        pascal_lines=pascal_lines,
        steiner_points=steiner_points,
        kirkman_points=kirkman_points,
        plucker_lines=plucker_lines,
    )


def verify_pascal_symbolic() -> sp.Expr:
    r"""Prove Pascal's *Hexagrammum Mysticum* universally over $\mathbb{Z}[t_0, t_1, t_2, t_3, t_4, t_5]$.

    Parameterizes six generic points on the projective conic $X^2 + Y^2 = Z^2$ via
    $P_k = [1 - t_k^2 : 2 t_k : 1 + t_k^2]$, computes the three opposite-side meets
    $M_{03}, M_{14}, M_{25}$ via 3D vector cross products, and expands the $3 \times 3$
    collinearity determinant $\det[M_{03}, M_{14}, M_{25}]$, returning ``0`` identically.

    Returns:
        Simplified SymPy polynomial expression (identically ``sp.Integer(0)``).
    """
    t_syms = sp.symbols("t0:6")
    pts = [sp.Matrix([1 - t**2, 2 * t, 1 + t**2]) for t in t_syms]

    def _m_cross(u: sp.Matrix, v: sp.Matrix) -> sp.Matrix:
        return sp.Matrix(
            [
                u[1] * v[2] - u[2] * v[1],
                u[2] * v[0] - u[0] * v[2],
                u[0] * v[1] - u[1] * v[0],
            ]
        )

    m_03 = _m_cross(_m_cross(pts[0], pts[1]), _m_cross(pts[3], pts[4]))
    m_14 = _m_cross(_m_cross(pts[1], pts[2]), _m_cross(pts[4], pts[5]))
    m_25 = _m_cross(_m_cross(pts[2], pts[3]), _m_cross(pts[5], pts[0]))
    det_expr = sp.Matrix.hstack(m_03, m_14, m_25).det()
    return sp.expand(det_expr)
