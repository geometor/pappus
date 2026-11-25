"""Exact symbolic projective invariants, cross-ratios, and harmonic/golden range scanners.

Provides 100% exact SymPy implementations of collinear cross-ratios, central
perspectivities (Book VII, Prop. 129 of Pappus's *Collection*), Wildberger
quadrances and spreads, collinear harmonic range detection :math:`(A, B; C, D) = -1`,
and integration with :mod:`geometor.divine` for golden section discovery.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Sequence

import sympy as sp
import sympy.geometry as spg
from geometor.divine import register_divine_hook
from geometor.model import Model
from geometor.model.sections import Section
from geometor.model.utils import clean_expr, sort_points

PHI: sp.Expr = sp.Rational(1, 2) + sp.sqrt(5) / 2

__all__ = [
    "PHI",
    "HarmonicRange",
    "GoldenRange",
    "quadrance",
    "line_spread",
    "exact_line_meet",
    "project_point",
    "cross_ratio",
    "anharmonic_orbit",
    "is_harmonic_range",
    "harmonic_conjugate_point",
    "find_harmonic_ranges",
    "find_golden_sections",
    "enable_divine_analysis",
    "circle_stereographic_point",
    "conic_equation_through_points",
    "are_coconic",
    "conic_cross_ratio",
]


@dataclass(frozen=True)
class HarmonicRange:
    """Represents four ordered collinear points forming a harmonic range :math:`(P_1, P_3; P_2, P_4) = -1`.

    Attributes:
        points: Ordered tuple :math:`(P_1, P_2, P_3, P_4)` along the carrier line such
            that :math:`(P_1, P_3)` and :math:`(P_2, P_4)` harmonically separate each other.
        point_ids: Corresponding model IDs of the four points.
        line: Carrier line in the model, if associated with one.
        line_id: Model ID of the carrier line.
        value: Exact symbolic cross-ratio :math:`(P_1, P_3; P_2, P_4) = -1`.
    """

    points: tuple[spg.Point, spg.Point, spg.Point, spg.Point]
    point_ids: tuple[str, str, str, str]
    line: spg.Line | None
    line_id: str
    value: sp.Expr = sp.Integer(-1)


@dataclass(frozen=True)
class GoldenRange:
    r"""Represents three ordered collinear points dividing a segment in the Golden Ratio :math:`\phi`.

    Attributes:
        section: Underlying :class:`~geometor.model.sections.Section` object.
        point_ids: Ordered model IDs :math:`(P_1, P_2, P_3)` of the three points.
        line: Carrier line in the model, if associated with one.
        line_id: Model ID of the carrier line.
        ratio: Exact symbolic ratio of longer to shorter segment (:math:`\phi`).
    """

    section: Section
    point_ids: tuple[str, str, str]
    line: spg.Line | None
    line_id: str
    ratio: sp.Expr


def quadrance(pt_1: spg.Point, pt_2: spg.Point) -> sp.Expr:
    """Compute the exact rational-trigonometric quadrance :math:`Q(P_1, P_2)`.

    Args:
        pt_1: First point.
        pt_2: Second point.

    Returns:
        Simplified symbolic expression :math:`(x_2 - x_1)^2 + (y_2 - y_1)^2`.
    """
    return clean_expr((pt_2.x - pt_1.x) ** 2 + (pt_2.y - pt_1.y) ** 2)


def line_spread(line_1: spg.Line, line_2: spg.Line) -> sp.Expr:
    r"""Compute the exact rational-trigonometric spread :math:`s(\ell_1, \ell_2) = \sin^2\theta`.

    Args:
        line_1: First line :math:`a_1 x + b_1 y + c_1 = 0`.
        line_2: Second line :math:`a_2 x + b_2 y + c_2 = 0`.

    Returns:
        Exact symbolic spread in :math:`[0, 1]` (equals :math:`0` iff parallel, :math:`1` iff perpendicular).
    """
    a1, b1, _ = line_1.coefficients
    a2, b2, _ = line_2.coefficients
    num = (a1 * b2 - a2 * b1) ** 2
    den = (a1**2 + b1**2) * (a2**2 + b2**2)
    return clean_expr(sp.cancel(num / den))


def exact_line_meet(line_1: spg.Line, line_2: spg.Line) -> spg.Point | None:
    """Compute the exact intersection of two lines via Cramer's rule.

    Returns ``None`` when the two lines are parallel or coincident (meeting at
    the projective line at infinity).

    Args:
        line_1: First SymPy line.
        line_2: Second SymPy line.

    Returns:
        Exact intersection :class:`sympy.geometry.point.Point`, or ``None`` if parallel.
    """
    a1, b1, c1 = line_1.coefficients
    a2, b2, c2 = line_2.coefficients
    det = sp.cancel(a1 * b2 - a2 * b1)
    if not det.free_symbols:
        if det.is_Rational:
            if det == 0:
                return None
        elif abs(complex(det.evalf(30))) < 1e-22 and sp.simplify(det) == 0:
            return None
    elif sp.simplify(det) == 0:
        return None

    x_coord = clean_expr(sp.cancel((b1 * c2 - b2 * c1) / det))
    y_coord = clean_expr(sp.cancel((c1 * a2 - c2 * a1) / det))
    return spg.Point(x_coord, y_coord)


def project_point(
    center: spg.Point,
    target_line: spg.Line,
    pt: spg.Point,
) -> spg.Point:
    r"""Project a point from a perspective center onto a target line.

    Implements central perspectivity as studied by Pappus in *Synagoge* Book VII,
    Proposition 129.

    Args:
        center: Center of perspectivity :math:`O` not lying on ``target_line``.
        target_line: Destination line onto which ``pt`` is projected.
        pt: Source point :math:`P \ne O`.

    Returns:
        Exact intersection :math:`[O P] \cap \text{target\_line}`.

    Raises:
        ValueError: If ``pt`` coincides with ``center`` or :math:`[O P]` is parallel to ``target_line``.
    """
    if pt.equals(center):
        raise ValueError("Source point cannot coincide with the center of perspectivity.")
    ray = spg.Line(center, pt)
    image = exact_line_meet(ray, target_line)
    if image is None:
        raise ValueError("Projection ray [center, pt] is parallel to target_line (meets at infinity).")
    return image


def _has_free_symbols(pts: Sequence[spg.Point]) -> bool:
    """Check whether any coordinate in ``pts`` contains unbound SymPy symbols."""
    return any(bool(pt.x.free_symbols or pt.y.free_symbols) for pt in pts)


def cross_ratio(
    pt_a: spg.Point,
    pt_b: spg.Point,
    pt_c: spg.Point,
    pt_d: spg.Point,
    *,
    check_collinear: bool = True,
) -> sp.Expr:
    r"""Compute the exact projective cross-ratio :math:`(A, B; C, D)` of four collinear points.

    Uses the standard projective convention

    .. math::

       (A, B; C, D) = \frac{(u_A - u_C)(u_B - u_D)}{(u_A - u_D)(u_B - u_C)},

    where :math:`u` is any affine coordinate along the line carrying :math:`A, B, C, D`.
    Under this convention, :math:`(A, B; C, D) = -1` iff :math:`(C, D)` harmonically separates
    :math:`(A, B)`, and :math:`(0, 1; \phi, \phi + 1) = \phi`.

    Args:
        pt_a: First point :math:`A`.
        pt_b: Second point :math:`B`.
        pt_c: Third point :math:`C`.
        pt_d: Fourth point :math:`D`.
        check_collinear: If True, verify that :math:`A, B, C, D` are collinear.

    Returns:
        Exact simplified SymPy expression for :math:`(A, B; C, D)`.

    Raises:
        ValueError: If the points are not collinear or if the denominator vanishes.
    """
    pts = (pt_a, pt_b, pt_c, pt_d)
    if check_collinear and not spg.Point.is_collinear(*pts):
        raise ValueError("Points passed to cross_ratio must be collinear.")

    # Select an affine coordinate projection with nonzero span along the line
    use_x: bool | None = None
    for p_i, p_j in combinations(pts, 2):
        dx = sp.cancel(p_j.x - p_i.x)
        dy = sp.cancel(p_j.y - p_i.y)
        if sp.simplify(dx) != 0:
            use_x = True
            break
        if sp.simplify(dy) != 0:
            use_x = False
            break

    if use_x is None:
        raise ValueError("All four points coincide; cross-ratio is undefined.")

    coords = [p.x if use_x else p.y for p in pts]
    u_a, u_b, u_c, u_d = coords
    num = (u_a - u_c) * (u_b - u_d)
    den = (u_a - u_d) * (u_b - u_c)
    if sp.simplify(den) == 0:
        raise ValueError("Degenerate cross-ratio: denominator vanishes (point coincidence).")

    return clean_expr(sp.cancel(num / den))


def anharmonic_orbit(lam: sp.Expr) -> list[sp.Expr]:
    r"""Return the six cross-ratio values generated by permuting four collinear points.

    Args:
        lam: Fundamental cross-ratio :math:`\lambda = (A, B; C, D) \notin \{0, 1\}`.

    Returns:
        List of the 6 simplified expressions
        :math:`[\lambda, 1/\lambda, 1 - \lambda, 1/(1 - \lambda), (\lambda - 1)/\lambda, \lambda/(\lambda - 1)]`.
    """
    lam_expr = sp.sympify(lam)
    raw = [
        lam_expr,
        1 / lam_expr,
        1 - lam_expr,
        1 / (1 - lam_expr),
        (lam_expr - 1) / lam_expr,
        lam_expr / (lam_expr - 1),
    ]
    return [clean_expr(sp.simplify(val)) for val in raw]


def is_harmonic_range(
    pt_a: spg.Point,
    pt_b: spg.Point,
    pt_c: spg.Point,
    pt_d: spg.Point,
) -> bool:
    """Determine whether :math:`(A, B; C, D) = -1` in exact symbolic arithmetic.

    Args:
        pt_a: First base point :math:`A`.
        pt_b: Second base point :math:`B`.
        pt_c: First conjugate point :math:`C`.
        pt_d: Second conjugate point :math:`D`.

    Returns:
        True iff :math:`A, B, C, D` are distinct collinear points satisfying :math:`(A, B; C, D) = -1`.
    """
    pts = (pt_a, pt_b, pt_c, pt_d)
    if not _has_free_symbols(pts):
        # Fast numeric pre-filter on affine parameter before exact symbolic check
        fx = [float(p.x.evalf()) for p in pts]
        fy = [float(p.y.evalf()) for p in pts]
        u = fx if (max(fx) - min(fx)) >= (max(fy) - min(fy)) else fy
        den_f = (u[0] - u[3]) * (u[1] - u[2])
        if abs(den_f) < 1e-12:
            return False
        num_f = (u[0] - u[2]) * (u[1] - u[3])
        if abs((num_f / den_f) + 1.0) > 1e-6:
            return False

    try:
        cr_val = cross_ratio(pt_a, pt_b, pt_c, pt_d, check_collinear=True)
    except ValueError:
        return False
    return sp.simplify(cr_val + 1) == 0


def harmonic_conjugate_point(
    pt_a: spg.Point,
    pt_b: spg.Point,
    pt_c: spg.Point,
) -> spg.Point:
    """Compute the exact algebraic fourth harmonic point :math:`D` such that :math:`(A, B; C, D) = -1`.

    Solves :math:`(A, B; C, D) = -1` along line :math:`[A B]` in closed symbolic form. For the
    pure straightedge geometric construction via a complete quadrilateral, see
    :func:`geometor.pappus.constructions.construct_harmonic_fourth`.

    Args:
        pt_a: First base point :math:`A`.
        pt_b: Second base point :math:`B`.
        pt_c: Given third collinear point :math:`C` (not the midpoint of :math:`A` and :math:`B`).

    Returns:
        Exact :class:`sympy.geometry.point.Point` :math:`D` satisfying :math:`(A, B; C, D) = -1`.

    Raises:
        ValueError: If :math:`A, B, C` are not distinct collinear points or :math:`C` is the midpoint of :math:`AB`
            (in which case :math:`D` lies on the line at infinity).
    """
    if pt_a.equals(pt_b) or pt_c.equals(pt_a) or pt_c.equals(pt_b):
        raise ValueError("Points A, B, C must be pairwise distinct.")
    if not spg.Point.is_collinear(pt_a, pt_b, pt_c):
        raise ValueError("Points A, B, C must be collinear.")

    # Write C = (1 - t)*A + t*B; then (A, B; C, D) = -1 with D = (1 - s)*A + s*B
    # gives ((0 - t)*(1 - s)) / ((0 - s)*(1 - t)) = -1 => t*(1 - s) = -s*(1 - t)
    # => t - t*s = -s + t*s => s*(2*t - 1) = t => s = t / (2*t - 1).
    dx = sp.cancel(pt_b.x - pt_a.x)
    if sp.simplify(dx) != 0:
        t = sp.cancel((pt_c.x - pt_a.x) / dx)
    else:
        dy = sp.cancel(pt_b.y - pt_a.y)
        t = sp.cancel((pt_c.y - pt_a.y) / dy)

    denom = sp.cancel(2 * t - 1)
    if sp.simplify(denom) == 0:
        raise ValueError("C is the Euclidean midpoint of A and B; harmonic conjugate lies at infinity.")

    s = sp.cancel(t / denom)
    x_d = clean_expr(sp.cancel(pt_a.x + s * (pt_b.x - pt_a.x)))
    y_d = clean_expr(sp.cancel(pt_a.y + s * (pt_b.y - pt_a.y)))
    return spg.Point(x_d, y_d)


def _line_contains_fast(line: spg.Line, pt: spg.Point, tol: float = 1e-8) -> bool:
    """Check point-line incidence with a fast float pre-filter before exact SymPy evaluation."""
    if not (pt.x.free_symbols or pt.y.free_symbols):
        a, b, c = line.coefficients
        if not (a.free_symbols or b.free_symbols or c.free_symbols):
            af, bf, cf = float(a.evalf()), float(b.evalf()), float(c.evalf())
            norm = (af * af + bf * bf) ** 0.5
            if norm > 0:
                px, py = float(pt.x.evalf()), float(pt.y.evalf())
                if abs(af * px + bf * py + cf) / norm > tol:
                    return False
    return bool(line.contains(pt))


def find_harmonic_ranges(
    model: Model,
    line: spg.Line | None = None,
    *,
    include_guides: bool = False,
) -> list[HarmonicRange]:
    """Scan lines in a :class:`~geometor.model.Model` for exact collinear harmonic tetrads.

    Revives and modernizes the ``analyze_harmonics`` routine from GEOMETOR's
    original 2023 ``pappus.py`` exploration. For every candidate line carrying at
    least four points, points are sorted along the line (:math:`P_1 < P_2 < P_3 < P_4`)
    so that each unordered harmonic tetrad is reported canonically once via the
    unique alternating separation :math:`(P_1, P_3; P_2, P_4) = -1`.

    Args:
        model: Geometric model to scan.
        line: Optional single line to inspect; if ``None``, scans all lines in ``model``.
        include_guides: If True, also include points and lines marked ``guide=True``.

    Returns:
        List of discovered :class:`HarmonicRange` records.
    """
    candidate_lines = (
        [line]
        if line is not None
        else [
            ln
            for ln in model.lines
            if include_guides or not model[ln].guide
        ]
    )
    candidate_points = [
        pt
        for pt in model.points
        if include_guides or not model[pt].guide
    ]

    discovered: list[HarmonicRange] = []
    seen_tetrads: set[tuple[spg.Point, spg.Point, spg.Point, spg.Point]] = set()

    for ln in candidate_lines:
        pts_on_line = [pt for pt in candidate_points if _line_contains_fast(ln, pt)]
        if len(pts_on_line) < 4:
            continue

        ordered_pts = sort_points(pts_on_line)
        ln_id = model[ln].ID if ln in model else ""

        for p1, p2, p3, p4 in combinations(ordered_pts, 4):
            key = (p1, p2, p3, p4)
            if key in seen_tetrads:
                continue
            # On ordered real points p1 < p2 < p3 < p4, only (p1, p3; p2, p4) < 0 can equal -1
            if is_harmonic_range(p1, p3, p2, p4):
                seen_tetrads.add(key)
                ids = (
                    model[p1].ID,
                    model[p2].ID,
                    model[p3].ID,
                    model[p4].ID,
                )
                discovered.append(
                    HarmonicRange(
                        points=key,
                        point_ids=ids,
                        line=ln,
                        line_id=ln_id,
                    )
                )

    return discovered


def find_golden_sections(
    model: Model,
    *,
    register_sections: bool = False,
    include_guides: bool = False,
) -> list[GoldenRange]:
    """Scan all lines in a :class:`~geometor.model.Model` for exact Golden Ratio sections.

    Complements :func:`geometor.divine.register_divine_hook` (which checks parent
    lines incrementally as intersection points are added) with a comprehensive
    post-construction scan across all points lying on each line in ``model``.

    Args:
        model: Geometric model to scan.
        register_sections: If True, also add each discovered golden :class:`Section`
            to ``model`` with ``classes=["golden"]``.
        include_guides: If True, include guide points and lines.

    Returns:
        List of discovered :class:`GoldenRange` records.
    """
    candidate_lines = [
        ln for ln in model.lines if include_guides or not model[ln].guide
    ]
    candidate_points = [
        pt for pt in model.points if include_guides or not model[pt].guide
    ]

    discovered: list[GoldenRange] = []
    seen_triples: set[tuple[spg.Point, spg.Point, spg.Point]] = set()

    for ln in candidate_lines:
        pts_on_line = [pt for pt in candidate_points if _line_contains_fast(ln, pt)]
        if len(pts_on_line) < 3:
            continue

        ordered_pts = sort_points(pts_on_line)
        ln_id = model[ln].ID if ln in model else ""

        for p1, p2, p3 in combinations(ordered_pts, 3):
            key = (p1, p2, p3)
            if key in seen_triples:
                continue
            sec = Section([p1, p2, p3])
            if sec.is_golden:
                seen_triples.add(key)
                if register_sections:
                    model.set_section([p1, p2, p3], classes=["golden"])
                exact_ratio = PHI if sp.simplify(sec.ratio - PHI) == 0 else clean_expr(sec.ratio)
                discovered.append(
                    GoldenRange(
                        section=sec,
                        point_ids=(model[p1].ID, model[p2].ID, model[p3].ID),
                        line=ln,
                        line_id=ln_id,
                        ratio=exact_ratio,
                    )
                )

    return discovered


def enable_divine_analysis(model: Model) -> Model:
    """Attach :func:`geometor.divine.register_divine_hook` to ``model`` and return it.

    Args:
        model: Target :class:`~geometor.model.Model` instance.

    Returns:
        The same model with real-time golden section analysis enabled.
    """
    register_divine_hook(model)
    return model


def circle_stereographic_point(
    t: sp.Expr | int,
    *,
    center: spg.Point | tuple[sp.Expr | int, sp.Expr | int] = (0, 0),
    radius: sp.Expr | int = 1,
) -> spg.Point:
    r"""Compute an exact point on :math:`(x - x_0)^2 + (y - y_0)^2 = R^2` via rational stereographic slope :math:`t`.

    Uses the classical Weierstrass / stereographic parameterization from :math:`(-R + x_0, y_0)`:

    .. math::

       P(t) = \left(x_0 + R \frac{1 - t^2}{1 + t^2},\; y_0 + R \frac{2 t}{1 + t^2}\right).

    Every :math:`t \in \mathbb{Q}` yields an exact rational point in :math:`\mathbb{Q}^2`, and
    every :math:`t \in \mathbb{Q}(\phi)` yields an exact point in :math:`\mathbb{Q}(\sqrt{5})^2`.

    Args:
        t: Exact symbolic or integer stereographic parameter.
        center: Circle center :math:`(x_0, y_0)`.
        radius: Exact positive circle radius :math:`R`.

    Returns:
        Exact :class:`~sympy.geometry.point.Point` on the circle.
    """
    t_sym = sp.sympify(t)
    r_sym = sp.sympify(radius)
    c_pt = center if isinstance(center, spg.Point) else spg.Point(sp.sympify(center[0]), sp.sympify(center[1]))
    denom = 1 + t_sym**2
    x_coord = sp.simplify(c_pt.x + r_sym * (1 - t_sym**2) / denom)
    y_coord = sp.simplify(c_pt.y + r_sym * (2 * t_sym) / denom)
    return spg.Point(x_coord, y_coord)


def conic_equation_through_points(
    points: Sequence[spg.Point | tuple[sp.Expr | int, sp.Expr | int]],
) -> sp.Expr:
    r"""Construct the exact quadratic conic polynomial :math:`C(x, y)` through five points.

    Evaluates the :math:`6 \times 6` Veronese determinant

    .. math::

       \det \begin{bmatrix}
       x^2 & x y & y^2 & x & y & 1 \\
       x_0^2 & x_0 y_0 & y_0^2 & x_0 & y_0 & 1 \\
       \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
       x_4^2 & x_4 y_4 & y_4^2 & x_4 & y_4 & 1
       \end{bmatrix}

    in the symbols ``x, y``.

    Args:
        points: Sequence of 5 points in the plane.

    Returns:
        Expanded SymPy polynomial in ``x`` and ``y`` (zero iff the 5 points are
        degenerate with 4+ collinear in a way that fails to determine a unique conic).

    Raises:
        ValueError: If ``len(points) != 5``.
    """
    if len(points) != 5:
        raise ValueError(f"Expected exactly 5 points to determine a conic, got {len(points)}.")
    x_sym, y_sym = sp.Symbol("x"), sp.Symbol("y")
    rows: list[list[sp.Expr]] = [[x_sym**2, x_sym * y_sym, y_sym**2, x_sym, y_sym, sp.Integer(1)]]
    for raw in points:
        pt = raw if isinstance(raw, spg.Point) else spg.Point(sp.sympify(raw[0]), sp.sympify(raw[1]))
        rows.append([pt.x**2, pt.x * pt.y, pt.y**2, pt.x, pt.y, sp.Integer(1)])
    return sp.expand(sp.Matrix(rows).det())


def are_coconic(
    points: Sequence[spg.Point | tuple[sp.Expr | int, sp.Expr | int]],
) -> bool:
    r"""Return True iff all given points lie on a single conic (smooth or degenerate line-pair).

    Unifies Pappus's degenerate two-line configuration (:math:`L_a \cdot L_b = 0`) and
    Pascal's smooth conic configuration (:math:`A x^2 + B x y + C y^2 + D x + E y + F = 0`)
    via the rank of the :math:`N \times 6` Veronese matrix :math:`[x_k^2, x_k y_k, y_k^2, x_k, y_k, 1]`.

    Args:
        points: Sequence of planar points (any :math:`\le 5` points trivially lie on at least one conic).

    Returns:
        ``True`` if the Veronese matrix has rank :math:`\le 5`, else ``False``.
    """
    if len(points) <= 5:
        return True
    rows: list[list[sp.Expr]] = []
    for raw in points:
        pt = raw if isinstance(raw, spg.Point) else spg.Point(sp.sympify(raw[0]), sp.sympify(raw[1]))
        rows.append([pt.x**2, pt.x * pt.y, pt.y**2, pt.x, pt.y, sp.Integer(1)])
    return int(sp.Matrix(rows).rank()) <= 5


def conic_cross_ratio(
    p1: spg.Point,
    p2: spg.Point,
    p3: spg.Point,
    p4: spg.Point,
    observer: spg.Point,
) -> sp.Expr:
    r"""Compute Michel Chasles's projective cross-ratio :math:`(P_1, P_2; P_3, P_4)_{\mathcal{C}}` on a conic.

    By Chasles's Theorem, for four distinct points :math:`P_1, P_2, P_3, P_4` on an irreducible
    conic :math:`\mathcal{C}`, the cross-ratio of the pencil of four rays
    :math:`[V P_1], [V P_2], [V P_3], [V P_4]` cut by any transversal line is **independent**
    of the fifth point :math:`V = \text{observer} \in \mathcal{C}`.

    Args:
        p1: First conic point.
        p2: Second conic point.
        p3: Third conic point.
        p4: Fourth conic point.
        observer: Distinct fifth point :math:`V` on the same conic.

    Returns:
        Exact simplified SymPy cross-ratio expression (or ``sp.oo``).

    Raises:
        ValueError: If the 5 points are not distinct or not coconic.
    """
    pts5 = (p1, p2, p3, p4, observer)
    if len(set(pts5)) != 5:
        raise ValueError("All four target points and observer must be distinct.")
    if not are_coconic(pts5):
        raise ValueError("Points do not lie on a common conic.")

    rays = [spg.Line(observer, pk) for pk in (p1, p2, p3, p4)]
    # Pick a clean transversal line not passing through observer
    candidates = (
        spg.Line(spg.Point(0, 0), spg.Point(1, 0)),
        spg.Line(spg.Point(0, 1), spg.Point(1, 1)),
        spg.Line(spg.Point(0, 2), spg.Point(1, 5)),
    )
    transversal = next(ln for ln in candidates if not ln.contains(observer))
    cuts = [exact_line_meet(ray, transversal) for ray in rays]
    return cross_ratio(cuts[0], cuts[1], cuts[2], cuts[3])

