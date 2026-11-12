r"""Exact symbolic *Synagoge* constructions for Books III, IV, and V of Pappus of Alexandria.

Brings Pappus's classical geometric, proportional, and isoperimetric propositions
alive in 100% exact SymPy and :mod:`geometor.model` arithmetic alongside the
projective Book VII constructions in :mod:`geometor.pappus.constructions`:

1. **Book III, Props. 5–16 (Hultsch I, pp. 68–84)** — *The Three Classical Means
   in a Single Semicircle*: exhibits the arithmetic mean $A = \frac{a+b}{2}$,
   geometric mean $G = \sqrt{ab}$, and harmonic mean $H = \frac{2ab}{a+b}$ in one
   semicircle on $AC = a + b$, proves $A \cdot H = G^2$ and $A \ge G \ge H$, and
   links the tangent meet $T$ to Book VII's harmonic division $(A, C; D, T) = -1$.
2. **Book IV, Prop. 1 (Hultsch I, pp. 176–179)** — *Pappus's Area Theorem*:
   generalizes Euclid *Elements* I.47 from squares on a right triangle to arbitrary
   outward parallelograms erected on two sides of any triangle $\triangle ABC$,
   including a universal 10-variable polynomial proof over $\mathbb{Z}$.
3. **Book IV, Props. 14–18 (Hultsch I, pp. 208–227)** — *The Infinite Arbelos
   Circle Chain* («ἀρχαία πρότασις»): constructs the shoemaker's knife (*arbelos*)
   and its tangent circle chain $C_1, \dots, C_n$ in 100% exact rational coordinates
   over $\mathbb{Q}(r_1, r_2)$, proving pairwise tangencies and $y_n = n d_n = 2 n r_n$.
4. **Book V, Preface & Prop. 1 (Hultsch I, pp. 304–310)** — *The Sagacity of Bees
   & Hexagonal Honeycomb Isoperimetry*: proves that $n \in \{3, 4, 6\}$ are the
   unique regular plane-tiling polygons, computes exact area ratios
   $\operatorname{Area}_6 : \operatorname{Area}_4 : \operatorname{Area}_3 = 6\sqrt{3} : 9 : 4\sqrt{3}$
   for equal perimeter $P$, and builds a 7-cell hexagonal honeycomb cluster that
   simultaneously realizes Book VIII, Prop. 23's 7-hexagon circle inscription.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model
from geometor.model.element import CircleElement, Element

from geometor.pappus.projective import PHI, cross_ratio, exact_line_meet, quadrance
from geometor.pappus.render import export_svg

ScalarInput = int | sp.Expr
PointInput = spg.Point | tuple[ScalarInput, ScalarInput]

__all__ = [
    "ThreeMeansResult",
    "PappusAreaResult",
    "ArbelosCircle",
    "ArbelosChainResult",
    "HoneycombIsoperimetryResult",
    "signed_area2",
    "construct_three_means",
    "construct_pappus_area_theorem",
    "verify_pappus_area_symbolic",
    "construct_pappus_arbelos_chain",
    "verify_arbelos_chain_symbolic",
    "verify_honeycomb_isoperimetry",
    "construct_honeycomb_isoperimetry",
    "build_synagoge_gallery",
]


@dataclass(frozen=True)
class ThreeMeansResult:
    r"""Exact symbolic result for Pappus's semicircle construction of the three means.

    Attributes:
        model: Populated :class:`~geometor.model.Model`.
        a: First positive segment length $AD = a$.
        b: Second positive segment length $DC = b$.
        arithmetic_mean: Exact arithmetic mean :math:`A = \frac{a + b}{2} = |OB|`.
        geometric_mean: Exact geometric mean :math:`G = \sqrt{ab} = |DB|`.
        harmonic_mean: Exact harmonic mean :math:`H = \frac{2ab}{a + b} = |BF|`.
        point_a: Left diameter endpoint $A = (0, 0)$.
        point_d: Interior division point $D = (a, 0)$.
        point_c: Right diameter endpoint $C = (a + b, 0)$.
        center_o: Semicircle center $O = \left(\frac{a + b}{2}, 0\right)$.
        point_b: Semicircle ordinate apex $B = (a, \sqrt{ab})$.
        point_f: Perpendicular foot $F$ from $D$ onto radius $OB$.
        tangent_t: Optional harmonic conjugate $T$ where tangent at $B$ meets $AC$
            (when $a \ne b$), satisfying $(A, C; D, T) = -1$.
        semicircle: Carrier circle $(O, A)$ of radius $R = \frac{a + b}{2}$.
        harmonic_cross_ratio: Exact cross-ratio $(A, C; D, T) = -1$ when $T$ is finite.
    """

    model: Model
    a: sp.Expr
    b: sp.Expr
    arithmetic_mean: sp.Expr
    geometric_mean: sp.Expr
    harmonic_mean: sp.Expr
    point_a: spg.Point
    point_d: spg.Point
    point_c: spg.Point
    center_o: spg.Point
    point_b: spg.Point
    point_f: spg.Point
    tangent_t: spg.Point | None
    semicircle: spg.Circle
    harmonic_cross_ratio: sp.Expr | None


@dataclass(frozen=True)
class PappusAreaResult:
    r"""Exact symbolic result for Pappus's Area Theorem (*Synagoge* Book IV, Prop. 1).

    Attributes:
        model: Populated :class:`~geometor.model.Model`.
        preset: Preset identifier (``"scalene"``, ``"pythagoras"``, or ``"custom"``).
        triangle: Tuple $(A, B, C)$ of counter-clockwise triangle vertices.
        parallelogram_ab: Tuple $(A, B, D, E)$ of outward parallelogram on $AB$.
        parallelogram_ac: Tuple $(A, C, F, G)$ of outward parallelogram on $AC$.
        parallelogram_bc: Tuple $(B, C, M, L)$ of translated parallelogram on $BC$.
        apex_h: Meet $H = [DE] \cap [FG]$ of the two outer parallelogram sides.
        ridge_j: Meet $J = [HA] \cap [BC]$ dividing $BCML$ into two sub-parallelograms.
        area_ab: Exact positive area of parallelogram $ABDE$.
        area_ac: Exact positive area of parallelogram $ACFG$.
        area_bc: Exact positive area of parallelogram $BCML$.
        area_residual: Exact simplified difference $\operatorname{Area}(BCML) - (\operatorname{Area}(ABDE) + \operatorname{Area}(ACFG)) = 0$.
    """

    model: Model
    preset: str
    triangle: tuple[spg.Point, spg.Point, spg.Point]
    parallelogram_ab: tuple[spg.Point, spg.Point, spg.Point, spg.Point]
    parallelogram_ac: tuple[spg.Point, spg.Point, spg.Point, spg.Point]
    parallelogram_bc: tuple[spg.Point, spg.Point, spg.Point, spg.Point]
    apex_h: spg.Point
    ridge_j: spg.Point
    area_ab: sp.Expr
    area_ac: sp.Expr
    area_bc: sp.Expr
    area_residual: sp.Expr


@dataclass(frozen=True)
class ArbelosCircle:
    r"""Exact symbolic record for the $n$-th tangent circle in Pappus's Arbelos chain.

    Attributes:
        index: Chain index $n \ge 1$ ($n = 1$ rests on the baseline semicircle $C_{\mathrm{right}}$).
        center: Exact rational center $K_n = (x_n, y_n)$.
        radius: Exact rational radius $r_n$.
        diameter: Exact rational diameter $d_n = 2 r_n$.
        height: Exact center altitude $y_n$ above baseline $AC$.
        height_over_diameter: Exact simplified ratio $y_n / d_n = n$.
        circle: Registered :class:`sympy.geometry.Circle` in the model.
        foot: Projection foot $P_n = (x_n, 0)$ on baseline $AC$.
    """

    index: int
    center: spg.Point
    radius: sp.Expr
    diameter: sp.Expr
    height: sp.Expr
    height_over_diameter: sp.Expr
    circle: spg.Circle
    foot: spg.Point


@dataclass(frozen=True)
class ArbelosChainResult:
    r"""Exact symbolic result for Pappus's *Ancient Proposition* on the Arbelos (*Synagoge* IV.14–18).

    Attributes:
        model: Populated :class:`~geometor.model.Model`.
        r1: Radius of left inner semicircle $C_{\mathrm{left}}$ on $AD$.
        r2: Radius of right inner semicircle $C_{\mathrm{right}}$ on $DC$.
        outer_radius: Outer semicircle radius $R = r_1 + r_2$ on $AC$.
        outer_circle: Carrier circle on diameter $AC$.
        left_circle: Left inner circle on diameter $AD$.
        right_circle: Right inner circle on diameter $DC$ ($n = 0$ base of chain).
        chain: Tuple of :class:`ArbelosCircle` entries for $n = 1, \dots, \text{count}$.
        locus_ellipse: Exact ellipse with foci $(O_1, O_0)$ carrying all centers $K_n$.
    """

    model: Model
    r1: sp.Expr
    r2: sp.Expr
    outer_radius: sp.Expr
    outer_circle: spg.Circle
    left_circle: spg.Circle
    right_circle: spg.Circle
    chain: tuple[ArbelosCircle, ...]
    locus_ellipse: spg.Ellipse


@dataclass(frozen=True)
class HoneycombIsoperimetryResult:
    r"""Exact symbolic result for Book V's Honeycomb Isoperimetry & Book VIII's 7-Hexagon Cluster.

    Attributes:
        perimeter: Common perimeter $P > 0$ shared by the equilateral triangle, square, and hexagon.
        tiling_polygons: Tuple ``(3, 4, 6)`` of the unique regular $n$-gons tiling the plane.
        interior_angles_deg: Exact interior angles ``{3: 60, 4: 90, 6: 120}`` in degrees.
        polygons_per_vertex: Exact valence ``{3: 6, 4: 4, 6: 3}`` meeting around each vertex.
        side_lengths: Exact side lengths ``{3: P/3, 4: P/4, 6: P/6}``.
        areas: Exact symbolic areas ``{3: Area_3, 4: Area_4, 6: Area_6}``.
        area_hex_over_tri: Exact rational ratio $\operatorname{Area}_6 / \operatorname{Area}_3 = 3/2$.
        area_hex_over_sq: Exact radical ratio $\operatorname{Area}_6 / \operatorname{Area}_4 = 2\sqrt{3}/3$.
        area_sq_over_tri: Exact radical ratio $\operatorname{Area}_4 / \operatorname{Area}_3 = 9\sqrt{3}/16$.
        circumradius_seven_hexagons: Exact circumradius $R_7 = s_6 \sqrt{7}$ of the 7-hexagon cluster (*Synagoge* VIII.23).
        model: Optional populated :class:`~geometor.model.Model` when constructed geometrically.
    """

    perimeter: sp.Expr
    tiling_polygons: tuple[int, int, int]
    interior_angles_deg: dict[int, sp.Expr]
    polygons_per_vertex: dict[int, int]
    side_lengths: dict[int, sp.Expr]
    areas: dict[int, sp.Expr]
    area_hex_over_tri: sp.Expr
    area_hex_over_sq: sp.Expr
    area_sq_over_tri: sp.Expr
    circumradius_seven_hexagons: sp.Expr
    model: Model | None = None


def _sym_pos(value: ScalarInput, name: str) -> sp.Expr:
    """Convert ``value`` to an exact SymPy expression and reject floats or non-positive scalars."""
    if isinstance(value, float):
        raise TypeError(f"{name} must be an exact int or SymPy expression, not float.")
    expr = sp.sympify(value)
    if expr.has(sp.Float):
        raise TypeError(f"{name} contains sp.Float; use sp.Rational or exact radicals.")
    if expr.is_real is False or (expr.is_number and bool(expr <= 0)):
        raise ValueError(f"{name} must be strictly positive, got {expr!r}.")
    return sp.simplify(expr)


def _as_exact_point(pt: PointInput, name: str) -> spg.Point:
    """Coerce ``pt`` to a 2D :class:`sympy.geometry.Point` without floating-point atoms."""
    if isinstance(pt, spg.Point):
        x_val, y_val = sp.sympify(pt.x), sp.sympify(pt.y)
    else:
        if len(pt) != 2:
            raise ValueError(f"{name} must have 2 coordinates, got {pt!r}.")
        if isinstance(pt[0], float) or isinstance(pt[1], float):
            raise TypeError(f"{name} coordinates must be exact, not float.")
        x_val, y_val = sp.sympify(pt[0]), sp.sympify(pt[1])
    if x_val.has(sp.Float) or y_val.has(sp.Float):
        raise TypeError(f"{name} contains sp.Float; use exact rational or radical expressions.")
    return spg.Point(sp.simplify(x_val), sp.simplify(y_val))


def _register_segment(
    model: Model,
    p1: spg.Point,
    p2: spg.Point,
    *,
    classes: list[str],
    seg_id: str | None = None,
) -> spg.Segment:
    """Register an exact finite :class:`sympy.geometry.Segment` in ``model``."""
    seg = spg.Segment(p1, p2)
    id1 = model[p1].ID if p1 in model else ""
    id2 = model[p2].ID if p2 in model else ""
    resolved_id = seg_id if seg_id is not None else f"[ {id1} {id2} ]"
    if seg in model:
        for cls_name in classes:
            model[seg].classes[cls_name] = ""
        return seg
    details = Element(
        seg,
        parents=[p1, p2],
        classes=classes,
        ID=resolved_id,
        guide=False,
    )
    model[seg] = details
    return seg


def _register_polygon(
    model: Model,
    vertices: list[spg.Point],
    *,
    classes: list[str],
    poly_id: str | None = None,
) -> spg.Polygon:
    """Register an exact :class:`sympy.geometry.Polygon` in ``model``."""
    poly = spg.Polygon(*vertices)
    vert_ids = [model[v].ID for v in vertices if v in model and model[v].ID]
    resolved_id = poly_id if poly_id is not None else f"< {' '.join(vert_ids)} >"
    if poly in model:
        for cls_name in classes:
            model[poly].classes[cls_name] = ""
        return poly
    details = Element(
        poly,
        parents=list(vertices),
        classes=classes,
        ID=resolved_id,
        guide=False,
    )
    model[poly] = details
    return poly


def _register_circle(
    model: Model,
    center: spg.Point,
    rim_point: spg.Point,
    *,
    radius: sp.Expr,
    classes: list[str],
    circ_id: str | None = None,
) -> spg.Circle:
    """Register an exact :class:`sympy.geometry.Circle` in ``model``."""
    circ = spg.Circle(center, sp.simplify(radius))
    cid = model[center].ID if center in model else "O"
    rid = model[rim_point].ID if rim_point in model else "R"
    resolved_id = circ_id if circ_id is not None else f"( {cid} {rid} )"
    if circ in model:
        for cls_name in classes:
            model[circ].classes[cls_name] = ""
        return circ
    details = CircleElement(
        circ,
        parents=[center, rim_point],
        classes=classes,
        ID=resolved_id,
        pt_radius=rim_point,
        guide=False,
    )
    model[circ] = details
    return circ


def signed_area2(p1: spg.Point, p2: spg.Point, p3: spg.Point) -> sp.Expr:
    r"""Return twice the signed Euclidean area $\det(p_2 - p_1, p_3 - p_1)$ of $\triangle p_1 p_2 p_3$.

    For a parallelogram with consecutive vertices $(p_1, p_2, p_2 + \vec{w}, p_1 + \vec{w})$,
    the signed area of the full parallelogram equals ``signed_area2(p1, p2, p1 + w)``.

    Args:
        p1: First vertex.
        p2: Second vertex.
        p3: Third vertex.

    Returns:
        Simplified exact SymPy expression $(x_2 - x_1)(y_3 - y_1) - (y_2 - y_1)(x_3 - x_1)$.
    """
    return sp.simplify((p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x))


def construct_three_means(
    model_or_a: Model | ScalarInput = 9,
    a_or_b: ScalarInput = 16,
    b: ScalarInput | None = None,
    *,
    model: Model | None = None,
    include_harmonic_tangent: bool = True,
) -> ThreeMeansResult:
    r"""Construct Pappus's semicircle diagram exhibiting the three classical means (*Synagoge* III.5–16).

    Supports both ``construct_three_means(a, b, *, model=None)`` and
    ``construct_three_means(model, a, b)``.

    On diameter $AC = a + b$ with center $O = \left(\frac{a+b}{2}, 0\right)$ and interior point
    $D = (a, 0)$:

    - Erect $DB \perp AC$ to the semicircle at $B = (a, \sqrt{ab})$ so :math:`|DB| = \sqrt{ab} = G`.
    - Join radius $OB$ so :math:`|OB| = \frac{a+b}{2} = A`.
    - Drop $DF \perp OB$ to foot $F$ so right-triangle similarity $\triangle BFD \sim \triangle BDO$
      gives :math:`|BF| = \frac{|DB|^2}{|OB|} = \frac{2ab}{a+b} = H`.
    - When $a \ne b$ and ``include_harmonic_tangent=True``, construct the circle tangent at $B$
      meeting $AC$ at $T = \left(\frac{a(a+b)}{a-b}, 0\right)$, exhibiting the exact harmonic
      conjugate $(A, C; D, T) = -1$ that bridges Book III's mean theory to Book VII's *Porisms*.

    Args:
        model_or_a: Either a :class:`~geometor.model.Model` or the first positive scalar $a$.
        a_or_b: First scalar $a$ (when ``model_or_a`` is a ``Model``) or second scalar $b$.
        b: Second scalar $b$ when ``model_or_a`` is a ``Model``.
        model: Optional explicit :class:`~geometor.model.Model` keyword argument.
        include_harmonic_tangent: If True and $a \ne b$, construct tangent meet $T$ on $AC$.

    Returns:
        Populated :class:`ThreeMeansResult`.
    """
    if isinstance(model_or_a, Model):
        if b is None:
            raise ValueError("When passing a Model first, both a and b must be provided.")
        mdl = model_or_a
        a_expr = _sym_pos(a_or_b, "a")
        b_expr = _sym_pos(b, "b")
    else:
        mdl = model if model is not None else Model("synagoge_three_means", auto_intersect=False)
        a_expr = _sym_pos(model_or_a, "a")
        b_expr = _sym_pos(a_or_b if b is None else b, "b")

    a_mean = sp.simplify((a_expr + b_expr) / 2)
    g_mean = sp.simplify(sp.sqrt(a_expr * b_expr))
    h_mean = sp.simplify(2 * a_expr * b_expr / (a_expr + b_expr))

    pt_a = mdl.set_point(sp.Integer(0), sp.Integer(0), classes=["given", "A"], ID="A")
    pt_d = mdl.set_point(a_expr, sp.Integer(0), classes=["given", "B"], ID="D")
    pt_c = mdl.set_point(a_expr + b_expr, sp.Integer(0), classes=["given", "A"], ID="C")
    pt_o = mdl.set_point(a_mean, sp.Integer(0), classes=["apex", "center"], ID="O")
    pt_b = mdl.set_point(a_expr, g_mean, classes=["meet", "even"], ID="B")

    diff = sp.simplify(a_expr - b_expr)
    denom = sp.simplify(a_expr + b_expr)
    fx = sp.simplify(a_expr * (a_expr**2 + 3 * b_expr**2) / (denom**2))
    fy = sp.simplify((diff**2) * g_mean / (denom**2))
    pt_f = mdl.set_point(fx, fy, classes=["harmonic"], ID="F")

    semicircle = _register_circle(
        mdl,
        pt_o,
        pt_a,
        radius=a_mean,
        classes=["conic", "circle"],
        circ_id="( O A )",
    )
    semicircle_el = mdl[semicircle]
    semicircle_el.parents[pt_c] = ""
    semicircle_el.parents[pt_b] = ""

    mdl.construct_line(pt_a, pt_c, classes=["carrier"], ID="[ A C ]")
    _register_polygon(mdl, [pt_a, pt_c, pt_b], classes=["circle"], poly_id="< A C B >")
    _register_segment(mdl, pt_o, pt_b, classes=["arithmetic"], seg_id="[ O B ]")
    _register_segment(mdl, pt_d, pt_b, classes=["geometric"], seg_id="[ D B ]")
    _register_segment(mdl, pt_b, pt_f, classes=["harmonic"], seg_id="[ B F ]")
    if pt_d != pt_f:
        _register_segment(mdl, pt_d, pt_f, classes=["altitude"], seg_id="[ D F ]")

    pt_t: spg.Point | None = None
    cr_val: sp.Expr | None = None
    if include_harmonic_tangent and diff != 0:
        tx = sp.simplify(a_expr * (a_expr + b_expr) / diff)
        pt_t = mdl.set_point(tx, sp.Integer(0), classes=["harmonic", "fourth_harmonic"], ID="T")
        _register_segment(mdl, pt_b, pt_t, classes=["vector"], seg_id="[ B T ]")
        cr_val = cross_ratio(pt_a, pt_c, pt_d, pt_t)

    return ThreeMeansResult(
        model=mdl,
        a=a_expr,
        b=b_expr,
        arithmetic_mean=a_mean,
        geometric_mean=g_mean,
        harmonic_mean=h_mean,
        point_a=pt_a,
        point_d=pt_d,
        point_c=pt_c,
        center_o=pt_o,
        point_b=pt_b,
        point_f=pt_f,
        tangent_t=pt_t,
        semicircle=semicircle,
        harmonic_cross_ratio=cr_val,
    )


def construct_pappus_area_theorem(
    model: Model | None = None,
    *,
    preset: str = "scalene",
    triangle: tuple[PointInput, PointInput, PointInput] | None = None,
    vec_ab: PointInput | None = None,
    vec_ac: PointInput | None = None,
) -> PappusAreaResult:
    r"""Construct Pappus's Area Theorem (*Synagoge* Book IV, Prop. 1, Hultsch I, pp. 176–179).

    Given an arbitrary counter-clockwise triangle $\triangle ABC$ and two arbitrary
    outward parallelograms $ABDE$ (with $D = B + \vec{u}$, $E = A + \vec{u}$) and
    $ACFG$ (with $F = C + \vec{v}$, $G = A + \vec{v}$):

    1. Extend outer sides $[DE]$ and $[FG]$ to meet at $H$.
    2. Join $[HA]$ and extend it across base $[BC]$ to meet $[BC]$ at $J$.
    3. Translate segment $HA$ to $BL$ and $CM$ ($L = B + (A - H)$, $M = C + (A - H)$)
       forming outward parallelogram $BCML$ on base $BC$.
    4. By shear-invariance through parallels $[DE] \parallel [AB]$, $[FG] \parallel [AC]$,
       and $[HA] \parallel [BL] \parallel [CM]$:

       .. math::

          \operatorname{Area}(ABDE) = \operatorname{Area}(ABLH\text{-shear}) = \operatorname{Area}(BLNJ), \quad
          \operatorname{Area}(ACFG) = \operatorname{Area}(JCMN),

       whence $\operatorname{Area}(BCML) = \operatorname{Area}(ABDE) + \operatorname{Area}(ACFG)$.

    Presets:
        - ``"scalene"``: Oblique scalene $\triangle ABC$ with $A = (3, 4)$, $B = (0, 0)$,
          $C = (7, 0)$ and skewed non-rectangular parallelograms of areas $13$ and $15$,
          yielding $\operatorname{Area}(BCML) = 28$.
        - ``"pythagoras"``: Exact $3$-$4$-$5$ right triangle at apex $A = \left(\frac{9}{5}, \frac{12}{5}\right)$
          on hypotenuse $B = (0, 0)$, $C = (5, 0)$ with squares of areas $9$ and $16$,
          yielding the exact $5 \times 5$ hypotenuse square of area $25$ (*Elements* I.47).

    Args:
        model: Optional :class:`~geometor.model.Model`; created if ``None``.
        preset: ``"scalene"`` or ``"pythagoras"`` when ``triangle`` is ``None``.
        triangle: Optional custom ``(A, B, C)`` counter-clockwise vertices.
        vec_ab: Optional outward side vector $\vec{u}$ for parallelogram $ABDE$.
        vec_ac: Optional outward side vector $\vec{v}$ for parallelogram $ACFG$.

    Returns:
        Populated :class:`PappusAreaResult`.
    """
    if triangle is not None:
        if vec_ab is None or vec_ac is None:
            raise ValueError("Custom triangle requires both vec_ab and vec_ac.")
        raw_a, raw_b, raw_c = (
            _as_exact_point(triangle[0], "A"),
            _as_exact_point(triangle[1], "B"),
            _as_exact_point(triangle[2], "C"),
        )
        u_pt = _as_exact_point(vec_ab, "vec_ab")
        v_pt = _as_exact_point(vec_ac, "vec_ac")
        preset_key = "custom"
    elif preset == "scalene":
        raw_a = spg.Point(3, 4)
        raw_b = spg.Point(0, 0)
        raw_c = spg.Point(7, 0)
        u_pt = spg.Point(-2, sp.Rational(5, 3))
        v_pt = spg.Point(sp.Rational(9, 4), sp.Rational(3, 2))
        preset_key = "scalene"
    elif preset == "pythagoras":
        raw_a = spg.Point(sp.Rational(9, 5), sp.Rational(12, 5))
        raw_b = spg.Point(0, 0)
        raw_c = spg.Point(5, 0)
        u_pt = spg.Point(sp.Rational(-12, 5), sp.Rational(9, 5))
        v_pt = spg.Point(sp.Rational(12, 5), sp.Rational(16, 5))
        preset_key = "pythagoras"
    else:
        raise KeyError(
            f"Unknown area-theorem preset {preset!r}. Valid presets: 'scalene', 'pythagoras'."
        )

    if signed_area2(raw_a, raw_b, raw_c) <= 0:
        raise ValueError("Triangle (A, B, C) must be positively (counter-clockwise) oriented.")

    mdl = model if model is not None else Model(f"pappus_area_{preset_key}", auto_intersect=False)

    pt_a = mdl.set_point(raw_a.x, raw_a.y, classes=["given", "apex"], ID="A")
    pt_b = mdl.set_point(raw_b.x, raw_b.y, classes=["given", "A"], ID="B")
    pt_c = mdl.set_point(raw_c.x, raw_c.y, classes=["given", "A"], ID="C")

    pt_d = mdl.set_point(raw_b.x + u_pt.x, raw_b.y + u_pt.y, classes=["B"], ID="D")
    pt_e = mdl.set_point(raw_a.x + u_pt.x, raw_a.y + u_pt.y, classes=["B"], ID="E")
    pt_f = mdl.set_point(raw_c.x + v_pt.x, raw_c.y + v_pt.y, classes=["B"], ID="F")
    pt_g = mdl.set_point(raw_a.x + v_pt.x, raw_a.y + v_pt.y, classes=["B"], ID="G")

    ln_de = mdl.construct_line(pt_d, pt_e, classes=["cross", "diagonal"], ID="[ D E ]")
    ln_fg = mdl.construct_line(pt_f, pt_g, classes=["cross", "diagonal"], ID="[ F G ]")
    meet_h = exact_line_meet(ln_de, ln_fg)
    if meet_h is None:
        raise ValueError("Outer parallelogram lines [D E] and [F G] are parallel.")
    pt_h = mdl.set_point(meet_h.x, meet_h.y, classes=["steiner"], ID="H")

    wx = sp.simplify(pt_a.x - pt_h.x)
    wy = sp.simplify(pt_a.y - pt_h.y)
    pt_l = mdl.set_point(pt_b.x + wx, pt_b.y + wy, classes=["meet", "even"], ID="L")
    pt_m = mdl.set_point(pt_c.x + wx, pt_c.y + wy, classes=["meet", "even"], ID="M")

    ln_bc = spg.Line(pt_b, pt_c)
    ln_ha = mdl.construct_line(pt_h, pt_a, classes=["steiner_line"], ID="[ H A ]")
    meet_j = exact_line_meet(ln_ha, ln_bc)
    if meet_j is None:
        raise ValueError("Line [H A] is parallel to base [B C].")
    pt_j = mdl.set_point(meet_j.x, meet_j.y, classes=["harmonic"], ID="J")
    pt_n = mdl.set_point(pt_j.x + wx, pt_j.y + wy, classes=["auxiliary"], ID="N")
    ln_ha_el = mdl[ln_ha]
    ln_ha_el.parents[pt_j] = ""
    ln_ha_el.parents[pt_n] = ""

    _register_polygon(mdl, [pt_a, pt_b, pt_c], classes=["hexagon"], poly_id="< A B C >")
    _register_polygon(mdl, [pt_a, pt_b, pt_d, pt_e], classes=["circle"], poly_id="< A B D E >")
    _register_polygon(mdl, [pt_a, pt_c, pt_f, pt_g], classes=["diamond"], poly_id="< A C F G >")
    _register_polygon(mdl, [pt_b, pt_c, pt_m, pt_l], classes=["square"], poly_id="< B C M L >")

    _register_segment(mdl, pt_b, pt_l, classes=["arithmetic"], seg_id="[ B L ]")
    _register_segment(mdl, pt_c, pt_m, classes=["arithmetic"], seg_id="[ C M ]")
    _register_segment(mdl, pt_j, pt_n, classes=["harmonic"], seg_id="[ J N ]")

    area_ab = sp.Abs(signed_area2(pt_a, pt_b, pt_e))
    area_ac = sp.Abs(signed_area2(pt_a, pt_c, pt_g))
    area_bc = sp.Abs(signed_area2(pt_b, pt_c, pt_l))
    residual = sp.simplify(
        signed_area2(pt_c, pt_b, pt_l)
        - (signed_area2(pt_b, pt_a, pt_e) + signed_area2(pt_a, pt_c, pt_g))
    )

    return PappusAreaResult(
        model=mdl,
        preset=preset_key,
        triangle=(pt_a, pt_b, pt_c),
        parallelogram_ab=(pt_a, pt_b, pt_d, pt_e),
        parallelogram_ac=(pt_a, pt_c, pt_f, pt_g),
        parallelogram_bc=(pt_b, pt_c, pt_m, pt_l),
        apex_h=pt_h,
        ridge_j=pt_j,
        area_ab=sp.simplify(area_ab),
        area_ac=sp.simplify(area_ac),
        area_bc=sp.simplify(area_bc),
        area_residual=residual,
    )


def verify_pappus_area_symbolic() -> sp.Expr:
    r"""Verify Pappus's Area Theorem universally over $\mathbb{Q}(x_A, y_A, x_B, y_B, x_C, y_C, u_x, u_y, v_x, v_y)$.

    Constructs generic symbolic points $A, B, C$ and generic parallelogram vectors
    $\vec{u} = (u_x, u_y)$ and $\vec{v} = (v_x, v_y)$, intersects the outer parallel
    lines $[DE]$ and $[FG]$ symbolically at $H$, translates $A - H$ onto base $BC$,
    and simplifies the oriented parallelogram area identity

    .. math::

       \det(B - C, A - H) - \bigl(\det(A - B, \vec{u}) + \det(\vec{v}, A - C)\bigr).

    Returns:
        Exact simplified SymPy expression (identically ``sp.Integer(0)``).
    """
    xa, ya, xb, yb, xc, yc = sp.symbols("x_A y_A x_B y_B x_C y_C")
    ux, uy, vx, vy = sp.symbols("u_x u_y v_x v_y")

    ex, ey = xa + ux, ya + uy
    gx, gy = xa + vx, ya + vy

    # Solve E + s*(B - A) = G + t*(C - A) symbolically via Cramer's rule
    dx_ab, dy_ab = xb - xa, yb - ya
    dx_ac, dy_ac = xc - xa, yc - ya
    rhs_x = gx - ex
    rhs_y = gy - ey
    det_tri = dx_ab * (-dy_ac) - dy_ab * (-dx_ac)
    s_param = (rhs_x * (-dy_ac) - rhs_y * (-dx_ac)) / det_tri

    hx = ex + s_param * dx_ab
    hy = ey + s_param * dy_ab

    wx = xa - hx
    wy = ya - hy

    area_bc_oriented = (xb - xc) * wy - (yb - yc) * wx
    area_ab_oriented = (xa - xb) * uy - (ya - yb) * ux
    area_ac_oriented = vx * (ya - yc) - vy * (xa - xc)
    return sp.simplify(sp.together(area_bc_oriented - (area_ab_oriented + area_ac_oriented)))


def construct_pappus_arbelos_chain(
    model_or_r1: Model | ScalarInput = 2,
    r1_or_r2: ScalarInput = 1,
    r2_or_count: ScalarInput | int = 4,
    count: int | None = None,
    *,
    model: Model | None = None,
) -> ArbelosChainResult:
    r"""Construct Pappus's Arbelos tangent circle chain (*Synagoge* IV.14–18, Hultsch I, pp. 208–227).

    Supports both ``construct_pappus_arbelos_chain(r1=2, r2=1, count=4, *, model=None)``
    and ``construct_pappus_arbelos_chain(model, r1, r2, count=4)``.

    For inner semicircle radii $r_1, r_2 > 0$ and outer radius $R = r_1 + r_2$ along
    baseline $AC$ ($A = (0, 0)$, $D = (2r_1, 0)$, $C = (2R, 0)$), circle inversion centered
    at $A$ with squared radius $k^2 = 4 R r_1$ maps $C_{\mathrm{outer}}$ and $C_{\mathrm{left}}$
    to the parallel vertical lines $u = 2r_1$ and $u = 2R$, yielding 100% rational coordinates
    for every circle $C_n$ ($n \ge 1$) with zero square roots:

    .. math::

       \Delta_n = r_1(r_1 + r_2) + n^2 r_2^2, \qquad
       r_n = \frac{r_1 r_2 (r_1 + r_2)}{\Delta_n},

    .. math::

       x_n = \frac{r_1 (r_1 + r_2)(2r_1 + r_2)}{\Delta_n}, \qquad
       y_n = \frac{2 n \, r_1 r_2 (r_1 + r_2)}{\Delta_n} = 2 n r_n = n d_n.

    Args:
        model_or_r1: Either a :class:`~geometor.model.Model` or left inner radius $r_1$.
        r1_or_r2: Left radius $r_1$ (when ``model_or_r1`` is a ``Model``) or right radius $r_2$.
        r2_or_count: Right radius $r_2$ (when ``model_or_r1`` is a ``Model``) or chain length ``count``.
        count: Number of chain circles $n = 1, \dots, \text{count}$ when ``model_or_r1`` is a ``Model``.
        model: Optional explicit :class:`~geometor.model.Model` keyword argument.

    Returns:
        Populated :class:`ArbelosChainResult`.
    """
    if isinstance(model_or_r1, Model):
        mdl = model_or_r1
        r1_expr = _sym_pos(r1_or_r2, "r1")
        r2_expr = _sym_pos(r2_or_count, "r2")
        n_count = 4 if count is None else int(count)
    else:
        mdl = model if model is not None else Model("pappus_arbelos_chain", auto_intersect=False)
        r1_expr = _sym_pos(model_or_r1, "r1")
        r2_expr = _sym_pos(r1_or_r2, "r2")
        n_count = int(r2_or_count) if count is None else int(count)

    if n_count < 1:
        raise ValueError(f"count must be >= 1, got {n_count}.")

    big_r = sp.simplify(r1_expr + r2_expr)
    pt_a = mdl.set_point(sp.Integer(0), sp.Integer(0), classes=["given", "A"], ID="A")
    pt_d = mdl.set_point(2 * r1_expr, sp.Integer(0), classes=["given", "B"], ID="D")
    pt_c = mdl.set_point(2 * big_r, sp.Integer(0), classes=["given", "A"], ID="C")

    pt_o0 = mdl.set_point(big_r, sp.Integer(0), classes=["apex", "center"], ID="O0")
    pt_o1 = mdl.set_point(r1_expr, sp.Integer(0), classes=["auxiliary", "center"], ID="O1")
    pt_o2 = mdl.set_point(2 * r1_expr + r2_expr, sp.Integer(0), classes=["auxiliary", "center"], ID="O2")

    mdl.construct_line(pt_a, pt_c, classes=["carrier"], ID="[ A C ]")

    c_outer = _register_circle(
        mdl,
        pt_o0,
        pt_a,
        radius=big_r,
        classes=["conic", "circle"],
        circ_id="( O0 A )",
    )
    mdl[c_outer].parents[pt_c] = ""

    c_left = _register_circle(
        mdl,
        pt_o1,
        pt_a,
        radius=r1_expr,
        classes=["conic", "circle"],
        circ_id="( O1 A )",
    )
    mdl[c_left].parents[pt_d] = ""

    c_right = _register_circle(
        mdl,
        pt_o2,
        pt_d,
        radius=r2_expr,
        classes=["conic", "circle"],
        circ_id="( O2 D )",
    )
    mdl[c_right].parents[pt_c] = ""

    chain_items: list[ArbelosCircle] = []
    for n_idx in range(1, n_count + 1):
        delta_n = sp.simplify(r1_expr * big_r + (n_idx**2) * (r2_expr**2))
        rn = sp.simplify(r1_expr * r2_expr * big_r / delta_n)
        xn = sp.simplify(r1_expr * big_r * (2 * r1_expr + r2_expr) / delta_n)
        yn = sp.simplify(2 * n_idx * r1_expr * r2_expr * big_r / delta_n)
        dn = sp.simplify(2 * rn)
        ratio_n = sp.simplify(yn / dn)

        parity_cls = "even" if n_idx % 2 == 1 else "odd"
        pt_kn = mdl.set_point(xn, yn, classes=["meet", parity_cls], ID=f"K{n_idx}")
        pt_rn = mdl.set_point(xn + rn, yn, classes=["auxiliary"], ID=f"X{n_idx}")
        pt_pn = mdl.set_point(xn, sp.Integer(0), classes=["harmonic"], ID=f"P{n_idx}")

        circ_n = _register_circle(
            mdl,
            pt_kn,
            pt_rn,
            radius=rn,
            classes=["conic", "circle"],
            circ_id=f"( K{n_idx} X{n_idx} )",
        )
        seg_cls = "arithmetic" if n_idx % 2 == 1 else "harmonic"
        _register_segment(mdl, pt_pn, pt_kn, classes=[seg_cls], seg_id=f"[ P{n_idx} K{n_idx} ]")

        chain_items.append(
            ArbelosCircle(
                index=n_idx,
                center=pt_kn,
                radius=rn,
                diameter=dn,
                height=yn,
                height_over_diameter=ratio_n,
                circle=circ_n,
                foot=pt_pn,
            )
        )

    # All centers K_n lie on the exact ellipse with foci O1 = (r1, 0) and O0 = (R, 0):
    # |K_n O0| + |K_n O1| = (R - r_n) + (r_1 + r_n) = R + r_1 = 2*r_1 + r_2
    ell_center = spg.Point(sp.simplify((2 * r1_expr + r2_expr) / 2), sp.Integer(0))
    ell_rx = sp.simplify((2 * r1_expr + r2_expr) / 2)
    ell_ry = sp.simplify(sp.sqrt(r1_expr * big_r))
    locus_ellipse = spg.Ellipse(ell_center, ell_rx, ell_ry)

    return ArbelosChainResult(
        model=mdl,
        r1=r1_expr,
        r2=r2_expr,
        outer_radius=big_r,
        outer_circle=c_outer,
        left_circle=c_left,
        right_circle=c_right,
        chain=tuple(chain_items),
        locus_ellipse=locus_ellipse,
    )


def verify_arbelos_chain_symbolic(n_max: int = 5) -> dict[str, sp.Expr]:
    r"""Prove Pappus's Arbelos Theorem symbolically over $\mathbb{Q}(r_1, r_2, n)$.

    Verifies four universal polynomial identities in $\mathbb{Q}(r_1, r_2, n)$:

    1. **Pappus's Altitude Law**: $y_n - n (2 r_n) = 0$ for symbolic $n$.
    2. **Internal Tangency to Outer Semicircle**: $Q(K_n, O_0) - (R - r_n)^2 = 0$.
    3. **External Tangency to Left Semicircle**: $Q(K_n, O_1) - (r_1 + r_n)^2 = 0$.
    4. **Chain-to-Chain External Tangency**: $Q(K_{n+1}, K_n) - (r_{n+1} + r_n)^2 = 0$
       for symbolic $n$ (including $n = 0$, tangency of $C_1$ to $C_{\mathrm{right}}$).

    Args:
        n_max: Optional positive check bound for explicit integer spot-checks alongside symbolic $n$.

    Returns:
        Dictionary mapping each invariant name to its simplified residual (all ``sp.Integer(0)``).
    """
    r1_sym, r2_sym, n_sym = sp.symbols("r_1 r_2 n", positive=True)
    big_r = r1_sym + r2_sym

    def _circle_data(idx: sp.Expr) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
        delta = r1_sym * big_r + (idx**2) * (r2_sym**2)
        rad = r1_sym * r2_sym * big_r / delta
        cx = r1_sym * big_r * (2 * r1_sym + r2_sym) / delta
        cy = 2 * idx * r1_sym * r2_sym * big_r / delta
        return cx, cy, rad

    xn, yn, rn = _circle_data(n_sym)
    x_next, y_next, r_next = _circle_data(n_sym + 1)

    res_altitude = sp.simplify(sp.together(yn - 2 * n_sym * rn))
    res_outer = sp.simplify(sp.together((xn - big_r) ** 2 + yn**2 - (big_r - rn) ** 2))
    res_left = sp.simplify(sp.together((xn - r1_sym) ** 2 + yn**2 - (r1_sym + rn) ** 2))
    res_adj = sp.simplify(
        sp.together((x_next - xn) ** 2 + (y_next - yn) ** 2 - (r_next + rn) ** 2)
    )

    # Also verify every integer index 0..n_max specializes cleanly to 0
    for k_int in range(n_max):
        if res_adj.subs(n_sym, k_int) != 0:
            raise AssertionError(f"Arbelos adjacency failed at n={k_int}.")

    return {
        "altitude_law": res_altitude,
        "outer_tangency": res_outer,
        "left_tangency": res_left,
        "adjacent_tangency": res_adj,
    }


def verify_honeycomb_isoperimetry(
    perimeter: ScalarInput = 12,
    *,
    build_model: bool = False,
) -> HoneycombIsoperimetryResult:
    r"""Verify Pappus's Book V Honeycomb Isoperimetry & Regular Planar Tiling Theorem.

    Proves two pillars of *Synagoge* Book V (Preface & Prop. 1, Hultsch I, pp. 304–310):

    1. **Uniqueness of Regular Planar Tilings**: For $k \ge 3$ congruent regular $n$-gons
       ($n \ge 3$) to surround a point without gaps or overlaps, their interior angle
       $\frac{n - 2}{n} \cdot 180^\circ$ must satisfy $k \cdot \frac{n - 2}{n} = 2$, i.e.
       $k = \frac{2n}{n - 2} = 2 + \frac{4}{n - 2} \in \mathbb{Z}_{\ge 3}$, whose unique
       integer solutions are $(n - 2) \in \{1, 2, 4\} \iff n \in \{3, 4, 6\}$ with
       $k \in \{6, 4, 3\}$.
    2. **Isoperimetric Superiority of the Hexagon**: For common perimeter $P > 0$:

       .. math::

          \operatorname{Area}_3 = \frac{\sqrt{3}}{36} P^2, \qquad
          \operatorname{Area}_4 = \frac{1}{16} P^2, \qquad
          \operatorname{Area}_6 = \frac{\sqrt{3}}{24} P^2,

       giving $\frac{\operatorname{Area}_6}{\operatorname{Area}_3} = \frac{3}{2}$ and
       $\frac{\operatorname{Area}_6}{\operatorname{Area}_4} = \frac{2\sqrt{3}}{3} > 1$
       (since $\left(\frac{2\sqrt{3}}{3}\right)^2 = \frac{4}{3} > 1$).

    Args:
        perimeter: Common positive perimeter $P$ (default ``12``, giving integer sides $4, 3, 2$).
        build_model: If True, also construct the geometric :class:`~geometor.model.Model`.

    Returns:
        Populated :class:`HoneycombIsoperimetryResult`.
    """
    p_expr = _sym_pos(perimeter, "perimeter")

    # Exhaustively verify (n - 2) | 4 is necessary and sufficient for k = 2n/(n-2) in Z_{>=3}
    valid_ns: list[int] = []
    angles_deg: dict[int, sp.Expr] = {}
    valences: dict[int, int] = {}
    for n_cand in range(3, 20):
        k_rat = sp.Rational(2 * n_cand, n_cand - 2)
        if k_rat.q == 1 and k_rat >= 3:
            valid_ns.append(n_cand)
            angles_deg[n_cand] = sp.Rational((n_cand - 2) * 180, n_cand)
            valences[n_cand] = int(k_rat)

    tiling_tuple = (valid_ns[0], valid_ns[1], valid_ns[2])
    s3 = sp.simplify(p_expr / 3)
    s4 = sp.simplify(p_expr / 4)
    s6 = sp.simplify(p_expr / 6)

    area3 = sp.simplify(sp.sqrt(3) / 4 * s3**2)
    area4 = sp.simplify(s4**2)
    area6 = sp.simplify(3 * sp.sqrt(3) / 2 * s6**2)

    ratio_6_3 = sp.simplify(area6 / area3)
    ratio_6_4 = sp.simplify(area6 / area4)
    ratio_4_3 = sp.simplify(area4 / area3)
    r7 = sp.simplify(s6 * sp.sqrt(7))

    mdl = construct_honeycomb_isoperimetry(p_expr) if build_model else None

    return HoneycombIsoperimetryResult(
        perimeter=p_expr,
        tiling_polygons=tiling_tuple,
        interior_angles_deg=angles_deg,
        polygons_per_vertex=valences,
        side_lengths={3: s3, 4: s4, 6: s6},
        areas={3: area3, 4: area4, 6: area6},
        area_hex_over_tri=ratio_6_3,
        area_hex_over_sq=ratio_6_4,
        area_sq_over_tri=ratio_4_3,
        circumradius_seven_hexagons=r7,
        model=mdl,
    )


def construct_honeycomb_isoperimetry(
    perimeter: ScalarInput = 12,
    *,
    model: Model | None = None,
) -> Model:
    r"""Construct an exact :class:`~geometor.model.Model` for Book V's Honeycomb & Book VIII.23's 7-Hexagon Circle.

    Builds:

    1. **Left Comparison Row**: Equilateral triangle ($s_3 = P/3$), square ($s_4 = P/4$),
       and regular hexagon ($s_6 = P/6$) sharing exact perimeter $P$.
    2. **Right 7-Cell Honeycomb Rosette**: Central regular hexagon $H_0$ of side $s_6$
       surrounded by six congruent regular hexagons sharing every wall without interstices,
       inscribed inside the exact outer circle of radius $R = s_6 \sqrt{7}$ proved in
       *Synagoge* Book VIII, Prop. 23 (Hultsch III, pp. 1096–1102).

    Args:
        perimeter: Common perimeter $P$ (default ``12``, giving $s_3 = 4, s_4 = 3, s_6 = 2$).
        model: Optional existing :class:`~geometor.model.Model`.

    Returns:
        Populated :class:`~geometor.model.Model`.
    """
    p_expr = _sym_pos(perimeter, "perimeter")
    mdl = model if model is not None else Model("honeycomb_isoperimetry", auto_intersect=False)

    s3 = sp.simplify(p_expr / 3)
    s4 = sp.simplify(p_expr / 4)
    s6 = sp.simplify(p_expr / 6)
    rt3 = sp.sqrt(3)

    # 1. Equal-perimeter equilateral triangle (bottom-left) and square (top-left)
    tx0 = sp.simplify(-5 * s6)
    ty0 = sp.simplify(-sp.Rational(5, 2) * s6)
    t1 = mdl.set_point(tx0, ty0, classes=["given", "A"], ID="T1")
    t2 = mdl.set_point(tx0 + s3, ty0, classes=["given", "A"], ID="T2")
    t3 = mdl.set_point(
        tx0 + s3 / 2,
        ty0 + rt3 * s3 / 2,
        classes=["given", "A"],
        ID="T3",
    )
    _register_polygon(mdl, [t1, t2, t3], classes=["diamond"], poly_id="< T1 T2 T3 >")

    sx0 = sp.simplify(-sp.Rational(19, 4) * s6)
    sy0 = sp.simplify(sp.Rational(3, 4) * s6)
    q1 = mdl.set_point(sx0, sy0, classes=["given", "B"], ID="Q1")
    q2 = mdl.set_point(sx0 + s4, sy0, classes=["given", "B"], ID="Q2")
    q3 = mdl.set_point(sx0 + s4, sy0 + s4, classes=["given", "B"], ID="Q3")
    q4 = mdl.set_point(sx0, sy0 + s4, classes=["given", "B"], ID="Q4")
    _register_polygon(mdl, [q1, q2, q3, q4], classes=["circle"], poly_id="< Q1 Q2 Q3 Q4 >")

    # 2. 7-cell hexagonal honeycomb rosette centered at H0 = (2*s6, 0)
    cx0 = sp.simplify(sp.Rational(3, 2) * s6)
    cy0 = sp.Integer(0)
    pt_h0 = mdl.set_point(cx0, cy0, classes=["steiner", "center"], ID="H0")

    def _hex_vertices(
        hx: sp.Expr,
        hy: sp.Expr,
        prefix: str,
        *,
        is_central: bool,
    ) -> list[spg.Point]:
        offsets = (
            (s6, sp.Integer(0)),
            (s6 / 2, rt3 * s6 / 2),
            (-s6 / 2, rt3 * s6 / 2),
            (-s6, sp.Integer(0)),
            (-s6 / 2, -rt3 * s6 / 2),
            (s6 / 2, -rt3 * s6 / 2),
        )
        verts: list[spg.Point] = []
        for idx, (dx, dy) in enumerate(offsets, start=1):
            vx = sp.simplify(hx + dx)
            vy = sp.simplify(hy + dy)
            cand = spg.Point(vx, vy)
            if cand in mdl:
                verts.append(cand)
            else:
                pt_cls = ["meet", "even"] if is_central else ["auxiliary"]
                pid = f"V{idx}" if is_central else f"X{prefix}{idx}"
                verts.append(mdl.set_point(vx, vy, classes=pt_cls, ID=pid))
        return verts

    central_verts = _hex_vertices(cx0, cy0, "0", is_central=True)
    _register_polygon(
        mdl,
        central_verts,
        classes=["square"],
        poly_id="< V1 V2 V3 V4 V5 V6 >",
    )

    neighbor_offsets = (
        (sp.Integer(0), rt3 * s6),
        (sp.Rational(3, 2) * s6, rt3 * s6 / 2),
        (sp.Rational(3, 2) * s6, -rt3 * s6 / 2),
        (sp.Integer(0), -rt3 * s6),
        (sp.Rational(-3, 2) * s6, -rt3 * s6 / 2),
        (sp.Rational(-3, 2) * s6, rt3 * s6 / 2),
    )
    outer_rim_pt: spg.Point | None = None
    for cell_idx, (ndx, ndy) in enumerate(neighbor_offsets, start=1):
        n_verts = _hex_vertices(cx0 + ndx, cy0 + ndy, str(cell_idx), is_central=False)
        _register_polygon(
            mdl,
            n_verts,
            classes=["hexagon"],
            poly_id=f"< C{cell_idx} >",
        )
        if cell_idx == 1:
            # Top-right vertex of top hexagon sits at exact distance s6*sqrt(7) from H0
            outer_rim_pt = n_verts[1]

    if outer_rim_pt is not None:
        pt_r7 = mdl.set_point(
            outer_rim_pt.x,
            outer_rim_pt.y,
            classes=["harmonic"],
            ID="N",
        )
        r7_val = sp.simplify(s6 * sp.sqrt(7))
        if quadrance(pt_h0, pt_r7) != sp.simplify(r7_val**2):
            raise AssertionError("Book VIII.23 7-hexagon circumradius identity failed.")
        _register_circle(
            mdl,
            pt_h0,
            pt_r7,
            radius=r7_val,
            classes=["conic", "circle"],
            circ_id="( H0 N )",
        )
        _register_segment(mdl, pt_h0, pt_r7, classes=["harmonic"], seg_id="[ H0 N ]")

    return mdl


def build_synagoge_gallery(
    output_dir: str | Path = "docsrc/_static/constructions",
) -> list[Path]:
    r"""Generate publication-grade interactive `.euclid-graphic` SVGs for the *Synagoge* Codex.

    Exports six standalone theme-adaptive SVGs covering Books III, IV, V, and VIII:

    1. ``synagoge_three_means.svg`` — Rational $(9, 16)$ semicircle means ($A = 25/2, G = 12, H = 288/25$)
       plus harmonic conjugate $T$.
    2. ``synagoge_three_means_golden.svg`` — Golden $(1, \phi^2)$ semicircle means ($G = \phi$) in $\mathbb{Q}(\phi)$.
    3. ``pappus_area_theorem.svg`` — General scalene Pappus Area Theorem (*Synagoge* IV.1).
    4. ``pappus_area_pythagoras.svg`` — Right-triangle + squares specialization (*Elements* I.47).
    5. ``pappus_arbelos_chain.svg`` — Rational Arbelos tangent circle chain (*Synagoge* IV.14–18).
    6. ``honeycomb_isoperimetry.svg`` — Equal-perimeter $n \in \{3, 4, 6\}$ comparison & 7-cell
       honeycomb rosette inscribed in $(H_0, N)$ (*Synagoge* V.1 & VIII.23).

    Args:
        output_dir: Destination directory for `.svg` files.

    Returns:
        List of resolved :class:`~pathlib.Path` objects written.
    """
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []

    # 1. Book III: Three Means (9, 16) with harmonic tangent T = (-36, 0) clipped cleanly
    means_rat = construct_three_means(9, 16, include_harmonic_tangent=True)
    written.append(
        export_svg(
            means_rat.model,
            out / "synagoge_three_means.svg",
            graphic_id="g1",
            title="Synagoge III.5–16 — Arithmetic, Geometric, and Harmonic Means in One Semicircle",
            width=720,
            height=420,
            bbox=(-2.5, 27.5, -2.5, 14.5),
            highlight_point_ids=("B", "F", "O"),
        )
    )

    # 2. Book III: Golden Three Means (1, phi^2) -> G = phi, harmonic tangent T = (-phi, 0)
    means_phi = construct_three_means(1, PHI**2, include_harmonic_tangent=True)
    written.append(
        export_svg(
            means_phi.model,
            out / "synagoge_three_means_golden.svg",
            graphic_id="g2",
            title="Synagoge III — Golden Semicircle Means on (1, phi^2) with Harmonic Conjugate T = (-phi, 0)",
            width=720,
            height=420,
            bbox=(-2.1, 4.1, -0.5, 2.2),
            highlight_point_ids=("B", "F", "T"),
        )
    )

    # 3. Book IV.1: General Scalene Pappus Area Theorem
    area_scalene = construct_pappus_area_theorem(preset="scalene")
    written.append(
        export_svg(
            area_scalene.model,
            out / "pappus_area_theorem.svg",
            graphic_id="g1",
            title="Synagoge IV.1 — Pappus's Area Theorem on Arbitrary Parallelograms",
            width=720,
            height=500,
            highlight_point_ids=("H", "A", "J"),
        )
    )

    # 4. Book IV.1 -> Elements I.47 Specialization
    area_pyth = construct_pappus_area_theorem(preset="pythagoras")
    written.append(
        export_svg(
            area_pyth.model,
            out / "pappus_area_pythagoras.svg",
            graphic_id="g2",
            title="Synagoge IV.1 Specialization — Reduction of Pappus's Area Theorem to Euclid I.47",
            width=680,
            height=520,
            highlight_point_ids=("H", "A", "J"),
        )
    )

    # 5. Book IV.14-18: Infinite Arbelos Tangent Circle Chain (y_n = n d_n)
    arbelos = construct_pappus_arbelos_chain(2, 1, 4)
    written.append(
        export_svg(
            arbelos.model,
            out / "pappus_arbelos_chain.svg",
            graphic_id="g3",
            title="Synagoge IV.14–18 — Pappus's Arbelos Tangent Circle Chain (y_n = n d_n)",
            width=720,
            height=440,
            bbox=(-0.4, 6.4, -0.5, 3.35),
            highlight_point_ids=("K1", "K2", "K3", "K4"),
        )
    )

    # 6. Book V.1 & VIII.23: Honeycomb Isoperimetry & 7-Hexagon Circle Inscription
    honeycomb_mdl = construct_honeycomb_isoperimetry(12)
    written.append(
        export_svg(
            honeycomb_mdl,
            out / "honeycomb_isoperimetry.svg",
            graphic_id="g1",
            title="Synagoge V.1 & VIII.23 — Honeycomb Isoperimetry (P = 12) and Seven Inscribed Hexagons",
            width=760,
            height=460,
            highlight_point_ids=("H0", "N"),
        )
    )

    return written
