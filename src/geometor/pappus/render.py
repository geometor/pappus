"""Publication-grade interactive SVG renderer for exact projective constructions.

Generates crisp pixel-space SVGs directly from :class:`~geometor.model.Model`
instances while preserving exact SymPy coordinates in metadata attributes and
``<title>`` tooltips. Outputs conform simultaneously to:

1. **Standalone SVG viewing** (GitHub ``README.rst``, browsers, ``prefers-color-scheme``
   dark/light palettes via an embedded ``<style>`` sheet), and
2. **PHOTON Publish interactive figures** (``svg.euclid-graphic``, ``#elements``,
   ``#graphics``, ``#highlights``, ``#points``, ``#labels``, 3-vertex ``<path>``
   geometry, ``data-ref``, and ``data-aliases`` consumed by ``geometor_interactive.js``).
"""
from __future__ import annotations

import html
import math
import re
from pathlib import Path
from typing import Sequence

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model
from geometor.model.sections import Section

__all__ = [
    "EMBEDDED_SVG_STYLE",
    "render_svg_string",
    "export_svg",
]

EMBEDDED_SVG_STYLE: str = """
  .euclid-graphic {
    --svg-bg: #fafaf9;
    --ink: #1c1917;
    --label-halo: rgba(250, 250, 249, 0.92);
    --carrier: #475569;
    --conic: #0284c7;
    --cross: #0e7490;
    --quad: #4338ca;
    --pappus-even: #d97706;
    --pappus-odd: #db2777;
    --steiner: #7c3aed;
    --harmonic: #059669;
    --golden: #b45309;
    --pt-given: #0f172a;
    --pt-a: #0369a1;
    --pt-b: #0f766e;
    --pt-meet-even: #d97706;
    --pt-meet-odd: #db2777;
    --pt-steiner: #7c3aed;
    --pt-harmonic: #059669;
    --tri-square: #d97706;
    --tri-circle: #0284c7;
    --tri-diamond: #db2777;
    font-family: "Inter", "Segoe UI", system-ui, -apple-system, sans-serif;
  }
  @media (prefers-color-scheme: dark) {
    .euclid-graphic {
      --svg-bg: #141417;
      --ink: #f4f4f5;
      --label-halo: rgba(20, 20, 23, 0.92);
      --carrier: #94a3b8;
      --conic: #38bdf8;
      --cross: #38bdf8;
      --quad: #818cf8;
      --pappus-even: #fbbf24;
      --pappus-odd: #f472b6;
      --steiner: #c084fc;
      --harmonic: #34d399;
      --golden: #facc15;
      --pt-given: #e2e8f0;
      --pt-a: #38bdf8;
      --pt-b: #2dd4bf;
      --pt-meet-even: #fbbf24;
      --pt-meet-odd: #f472b6;
      --pt-steiner: #c084fc;
      --pt-harmonic: #34d399;
      --tri-square: #fbbf24;
      --tri-circle: #38bdf8;
      --tri-diamond: #f472b6;
    }
  }
  .euclid-graphic .svg-bg { fill: var(--svg-bg); }
  .euclid-graphic .geom-circle.conic-curve { fill: none; stroke: var(--conic); stroke-width: 2.15; opacity: 0.88; }
  .euclid-graphic .geom-line { fill: none; stroke: var(--carrier); stroke-width: 1.6; stroke-linecap: round; }
  .euclid-graphic .carrier-line { stroke: var(--carrier); stroke-width: 2.1; opacity: 0.92; }
  .euclid-graphic .cross-line { stroke: var(--cross); stroke-width: 1.25; stroke-opacity: 0.58; }
  .euclid-graphic .quad-line { stroke: var(--quad); stroke-width: 1.45; stroke-opacity: 0.78; }
  .euclid-graphic .diagonal-line { stroke-dasharray: 5 3.5; }
  .euclid-graphic .pappus-line { stroke-width: 2.7; opacity: 0.96; }
  .euclid-graphic .pappus-even { stroke: var(--pappus-even); }
  .euclid-graphic .pappus-odd { stroke: var(--pappus-odd); }
  .euclid-graphic .steiner-line { stroke: var(--steiner); stroke-width: 2.5; stroke-dasharray: 7 4; }
  .euclid-graphic .harmonic-line { stroke: var(--harmonic); stroke-width: 2.5; }
  .euclid-graphic .geom-segment { fill: none; stroke: var(--carrier); stroke-width: 2.3; stroke-linecap: round; }
  .euclid-graphic .geom-segment.golden-segment { fill: none; stroke: var(--golden); stroke-width: 3.6; stroke-linecap: round; opacity: 0.85; }
  .euclid-graphic .geom-segment.harmonic-segment { fill: none; stroke: var(--harmonic); stroke-width: 3.2; stroke-linecap: round; opacity: 0.85; }
  .euclid-graphic .geom-segment.arithmetic-segment { fill: none; stroke: var(--pappus-even); stroke-width: 3.1; stroke-linecap: round; opacity: 0.92; }
  .euclid-graphic .geom-segment.geometric-segment { fill: none; stroke: var(--conic); stroke-width: 3.1; stroke-linecap: round; opacity: 0.92; }
  .euclid-graphic .geom-segment.vector-segment { fill: none; stroke: var(--steiner); stroke-width: 2.4; stroke-dasharray: 6 3.5; stroke-linecap: round; opacity: 0.88; }
  .euclid-graphic .geom-segment.altitude-segment { fill: none; stroke: var(--pappus-odd); stroke-width: 2.2; stroke-dasharray: 4.5 3; stroke-linecap: round; opacity: 0.85; }
  .euclid-graphic .geom-polygon.hexagon-poly { fill: var(--cross); fill-opacity: 0.06; stroke: var(--cross); stroke-width: 1.5; stroke-opacity: 0.4; stroke-linejoin: round; }
  .euclid-graphic .geom-polygon.tri-square { fill: var(--tri-square); fill-opacity: 0.09; stroke: var(--tri-square); stroke-width: 1.9; stroke-linejoin: round; }
  .euclid-graphic .geom-polygon.tri-circle { fill: var(--tri-circle); fill-opacity: 0.09; stroke: var(--tri-circle); stroke-width: 1.9; stroke-linejoin: round; }
  .euclid-graphic .geom-polygon.tri-diamond { fill: var(--tri-diamond); fill-opacity: 0.09; stroke: var(--tri-diamond); stroke-width: 1.9; stroke-linejoin: round; }
  .euclid-graphic .geom-point { fill: var(--pt-given); stroke: var(--svg-bg); stroke-width: 1.5; }
  .euclid-graphic .pt-a { fill: var(--pt-a); }
  .euclid-graphic .pt-b { fill: var(--pt-b); }
  .euclid-graphic .meet-point.pappus-even { fill: var(--pt-meet-even); }
  .euclid-graphic .meet-point.pappus-odd { fill: var(--pt-meet-odd); }
  .euclid-graphic .steiner-point { fill: var(--pt-steiner); stroke-width: 2.0; }
  .euclid-graphic .harmonic-point { fill: var(--pt-harmonic); stroke-width: 1.8; }
  .euclid-graphic .aux-point { opacity: 0.78; }
  .euclid-graphic .geom-label {
    fill: var(--ink);
    font-size: 13.5px;
    font-weight: 600;
    paint-order: stroke fill;
    stroke: var(--label-halo);
    stroke-width: 3.6px;
    stroke-linejoin: round;
    user-select: none;
  }
  .euclid-graphic .geom-label-sub { font-size: 10px; font-weight: 600; }
""".strip()


def _fmt(val: float) -> str:
    """Format a pixel coordinate compactly to 2 decimal places."""
    if abs(val - round(val)) < 1e-5:
        return str(int(round(val)))
    return f"{val:.2f}".rstrip("0").rstrip(".")


def _clip_line_to_rect(
    line: spg.Line,
    xmin: float,
    xmax: float,
    ymin: float,
    ymax: float,
) -> tuple[tuple[float, float], tuple[float, float]] | None:
    """Clip an infinite algebraic line $a x + b y + c = 0$ to a math bounding box."""
    a_f = float(line.coefficients[0].evalf())
    b_f = float(line.coefficients[1].evalf())
    c_f = float(line.coefficients[2].evalf())
    eps = 1e-11
    hits: list[tuple[float, float]] = []

    if abs(b_f) > eps:
        for x_edge in (xmin, xmax):
            y_val = -(a_f * x_edge + c_f) / b_f
            if ymin - 1e-7 <= y_val <= ymax + 1e-7:
                hits.append((x_edge, min(max(y_val, ymin), ymax)))

    if abs(a_f) > eps:
        for y_edge in (ymin, ymax):
            x_val = -(b_f * y_edge + c_f) / a_f
            if xmin - 1e-7 <= x_val <= xmax + 1e-7:
                hits.append((min(max(x_val, xmin), xmax), y_edge))

    unique_hits: list[tuple[float, float]] = []
    for hx, hy in hits:
        if not any(math.hypot(hx - ux, hy - uy) < 1e-5 for ux, uy in unique_hits):
            unique_hits.append((hx, hy))

    if len(unique_hits) < 2:
        return None
    # Pick the two farthest boundary intersections in case of corner hits
    best_pair = (unique_hits[0], unique_hits[1])
    best_dist = -1.0
    for i in range(len(unique_hits)):
        for j in range(i + 1, len(unique_hits)):
            d = math.hypot(
                unique_hits[j][0] - unique_hits[i][0],
                unique_hits[j][1] - unique_hits[i][1],
            )
            if d > best_dist:
                best_dist = d
                best_pair = (unique_hits[i], unique_hits[j])
    return best_pair


def _split_point_label(
    pt_id: str,
    overrides: dict[str, tuple[str, str]] | None = None,
) -> tuple[str, str]:
    """Split an alphanumeric point ID into ``(base, subscript)`` for ``<tspan>`` display."""
    if overrides and pt_id in overrides:
        return overrides[pt_id]
    if pt_id == "S1":
        return ("S", "+")
    if pt_id == "S2":
        return ("S", "−")
    m = re.match(r"^([A-Za-z]+)(\d+)$", pt_id)
    if m:
        base, digits = m.group(1), m.group(2)
        if base == "M" and len(digits) == 4:
            return ("M", f"{digits[:2]},{digits[2:]}")
        return (base, digits)
    return (pt_id, "")


def _line_css_classes(classes: set[str]) -> str:
    """Map model line classes to semantic CSS classes."""
    out = ["geom-line"]
    if "carrier" in classes:
        out.append("carrier-line")
    if "cross" in classes:
        out.append("cross-line")
    if "quadrilateral" in classes:
        out.append("quad-line")
    if "diagonal" in classes:
        out.append("diagonal-line")
    if "pappus" in classes:
        out.append("pappus-line")
        if "even" in classes:
            out.append("pappus-even")
        elif "odd" in classes:
            out.append("pappus-odd")
    if "steiner_line" in classes or ("steiner" in classes and "pappus" not in classes):
        out.append("steiner-line")
    if "harmonic" in classes or "conjugate_line" in classes:
        out.append("harmonic-line")
    return " ".join(out)


def _polygon_css_classes(classes: set[str]) -> str:
    """Map model polygon classes to semantic CSS classes."""
    out = ["geom-polygon"]
    if "hexagon" in classes:
        out.append("hexagon-poly")
    if "square" in classes:
        out.append("tri-square")
    if "circle" in classes:
        out.append("tri-circle")
    if "diamond" in classes:
        out.append("tri-diamond")
    return " ".join(out)


def _point_css_and_radius(classes: set[str]) -> tuple[str, float]:
    """Map model point classes to ``(css_class_string, pixel_radius)``."""
    out = ["geom-point"]
    radius = 3.8
    if "given" in classes:
        out.append("given-point")
        radius = 4.2
    if "A" in classes:
        out.append("pt-a")
    if "B" in classes:
        out.append("pt-b")
    if "apex" in classes:
        out.append("apex-point")
        radius = 3.8
    if "meet" in classes:
        out.append("meet-point")
        radius = 4.7
        if "even" in classes:
            out.append("pappus-even")
        elif "odd" in classes:
            out.append("pappus-odd")
    if "steiner" in classes:
        out.append("steiner-point")
        radius = 6.0
    if "fourth_harmonic" in classes or "harmonic" in classes:
        out.append("harmonic-point")
        radius = 5.2
    if "intersection" in classes or "auxiliary" in classes:
        out.append("aux-point")
        radius = 3.1
    return (" ".join(out), radius)


def _point_to_segment_dist(
    px: float,
    py: float,
    x1: float,
    y1: float,
    x2: float,
    y2: float,
) -> float:
    """Compute pixel distance from ``(px, py)`` to segment ``(x1, y1)-(x2, y2)``."""
    dx = x2 - x1
    dy = y2 - y1
    len_sq = dx * dx + dy * dy
    if len_sq < 1e-9:
        return math.hypot(px - x1, py - y1)
    t = max(0.0, min(1.0, ((px - x1) * dx + (py - y1) * dy) / len_sq))
    proj_x = x1 + t * dx
    proj_y = y1 + t * dy
    return math.hypot(px - proj_x, py - proj_y)


def render_svg_string(
    model: Model,
    *,
    graphic_id: str = "g1",
    title: str = "Pappus Projective Construction",
    width: int = 680,
    height: int = 440,
    margin: float = 44.0,
    bbox: tuple[float, float, float, float] | None = None,
    focus_points: Sequence[spg.Point] | None = None,
    include_guides: bool = False,
    show_labels: bool = True,
    show_meet_labels: bool = True,
    show_aux_labels: bool = False,
    label_overrides: dict[str, tuple[str, str]] | None = None,
    highlight_point_ids: Sequence[str] | None = None,
) -> str:
    """Render a :class:`~geometor.model.Model` into a complete interactive SVG string.

    Args:
        model: Populated :class:`~geometor.model.Model`.
        graphic_id: ``data-graphic-id`` identifier for ``geometor_interactive.js``.
        title: Accessible SVG title string.
        width: Pixel width of the SVG ``viewBox``.
        height: Pixel height of the SVG ``viewBox``.
        margin: Outer pixel margin around the framed point cloud.
        bbox: Optional explicit math viewport ``(xmin, xmax, ymin, ymax)``.
        focus_points: Optional subset of points used to compute auto-framing bounds.
        include_guides: If True, also render elements marked ``guide=True``.
        show_labels: Master toggle for point text labels.
        show_meet_labels: If False, suppress text labels on ``M...`` cross-join meets
            (useful on dense 18-meet composite diagrams while retaining hover refs).
        show_aux_labels: If True, also label auto-discovered ``X1..Xn`` intersections.
        label_overrides: Optional mapping ``pt_id -> (base, subscript)``.
        highlight_point_ids: Optional point IDs to emphasize with an extra halo ring.

    Returns:
        UTF-8 XML/SVG string.
    """
    visible_points = [
        pt for pt in model.points if include_guides or not model[pt].guide
    ]
    visible_lines = [
        ln for ln in model.lines if include_guides or not model[ln].guide
    ]
    visible_polygons = [
        poly
        for poly in model
        if isinstance(poly, spg.Polygon) and (include_guides or not model[poly].guide)
    ]
    visible_sections = [
        sec
        for sec in model
        if isinstance(sec, Section) and (include_guides or not model[sec].guide)
    ]
    visible_conics: list[tuple[spg.Ellipse, str]] = [
        (curve, model[curve].ID)
        for curve in model
        if isinstance(curve, spg.Circle) and (include_guides or not model[curve].guide)
    ]
    for extra_curve, extra_id in getattr(model, "_extra_conics", ()):
        visible_conics.append((extra_curve, extra_id))

    frame_pts = list(focus_points) if focus_points else visible_points
    if bbox is not None:
        xmin_m, xmax_m, ymin_m, ymax_m = bbox
    elif frame_pts or visible_conics:
        xs = [float(p.x.evalf()) for p in frame_pts]
        ys = [float(p.y.evalf()) for p in frame_pts]
        if focus_points is None:
            for curve, _ in visible_conics:
                ccx = float(curve.center.x.evalf())
                ccy = float(curve.center.y.evalf())
                hr = float(curve.hradius.evalf())
                vr = float(curve.vradius.evalf())
                xs.extend((ccx - hr, ccx + hr))
                ys.extend((ccy - vr, ccy + vr))
        xmin_m, xmax_m = min(xs), max(xs)
        ymin_m, ymax_m = min(ys), max(ys)
        span_x = max(xmax_m - xmin_m, 1.0)
        span_y = max(ymax_m - ymin_m, 1.0)
        pad_x = 0.12 * span_x
        pad_y = 0.14 * span_y
        xmin_m -= pad_x
        xmax_m += pad_x
        ymin_m -= pad_y
        ymax_m += pad_y
    else:
        xmin_m, xmax_m, ymin_m, ymax_m = -1.0, 5.0, -1.0, 3.0

    span_x = max(xmax_m - xmin_m, 1e-6)
    span_y = max(ymax_m - ymin_m, 1e-6)
    avail_w = max(width - 2.0 * margin, 100.0)
    avail_h = max(height - 2.0 * margin, 100.0)
    scale = min(avail_w / span_x, avail_h / span_y)

    cx_m = 0.5 * (xmin_m + xmax_m)
    cy_m = 0.5 * (ymin_m + ymax_m)
    cx_s = 0.5 * width
    cy_s = 0.5 * height

    def to_svg(mx: float, my: float) -> tuple[float, float]:
        return (cx_s + (mx - cx_m) * scale, cy_s - (my - cy_m) * scale)

    # Compute the math coordinates corresponding to the inset clipping rectangle in SVG space
    inset_px = 14.0
    clip_xmin = cx_m - (cx_s - inset_px) / scale
    clip_xmax = cx_m + (width - inset_px - cx_s) / scale
    clip_ymin = cy_m - (height - inset_px - cy_s) / scale
    clip_ymax = cy_m + (cy_s - inset_px) / scale

    pt_svg_coords: dict[spg.Point, tuple[float, float]] = {}
    for pt in visible_points:
        pt_svg_coords[pt] = to_svg(float(pt.x.evalf()), float(pt.y.evalf()))

    # Build circles and ellipses
    conic_elems: list[str] = []
    for curve, primary_c_ref in visible_conics:
        ccx_s, ccy_s = to_svg(float(curve.center.x.evalf()), float(curve.center.y.evalf()))
        on_curve_ids = [
            model[pt].ID
            for pt in visible_points
            if model[pt].ID and not model[pt].ID.startswith("X") and curve.contains(pt)
        ]
        c_aliases: list[str] = []
        if curve.center in model and model[curve.center].ID:
            cid = model[curve.center].ID
            for pid in on_curve_ids:
                cand2 = f"( {cid} {pid} )"
                if cand2 != primary_c_ref:
                    c_aliases.append(cand2)
        if len(on_curve_ids) >= 3:
            cand3 = f"( {on_curve_ids[0]} {on_curve_ids[1]} {on_curve_ids[2]} )"
            if cand3 != primary_c_ref:
                c_aliases.append(cand3)
        c_alias_attr = f' data-aliases="{html.escape(" | ".join(c_aliases))}"' if c_aliases else ""
        c_ref_attr = f' data-ref="{html.escape(primary_c_ref)}"' if primary_c_ref else ""
        eq_c_str = str(curve.equation())
        if isinstance(curve, spg.Circle):
            r_px = float(curve.radius.evalf()) * scale
            conic_elems.append(
                f'      <circle class="geom-circle conic-curve" '
                f'cx="{_fmt(ccx_s)}" cy="{_fmt(ccy_s)}" r="{_fmt(r_px)}"'
                f'{c_ref_attr}{c_alias_attr} fill="none">'
                f"<title>{html.escape(primary_c_ref)}: {html.escape(eq_c_str)} = 0</title></circle>"
            )
        else:
            rx_px = float(curve.hradius.evalf()) * scale
            ry_px = float(curve.vradius.evalf()) * scale
            conic_elems.append(
                f'      <ellipse class="geom-circle conic-curve" '
                f'cx="{_fmt(ccx_s)}" cy="{_fmt(ccy_s)}" rx="{_fmt(rx_px)}" ry="{_fmt(ry_px)}"'
                f'{c_ref_attr}{c_alias_attr} fill="none">'
                f"<title>{html.escape(primary_c_ref)}: {html.escape(eq_c_str)} = 0</title></ellipse>"
            )

    # Build polygons
    polygon_elems: list[str] = []
    for poly in visible_polygons:
        el = model[poly]
        pts_attr = " ".join(
            f"{_fmt(to_svg(float(v.x.evalf()), float(v.y.evalf()))[0])},{_fmt(to_svg(float(v.x.evalf()), float(v.y.evalf()))[1])}"
            for v in poly.vertices
        )
        vert_ids = [model[v].ID for v in poly.vertices if v in model and model[v].ID]
        poly_ref = f"< {' '.join(vert_ids)} >" if vert_ids else el.ID
        css_cls = _polygon_css_classes(el.classes)
        polygon_elems.append(
            f'      <polygon class="{css_cls}" points="{pts_attr}" '
            f'data-ref="{html.escape(poly_ref)}" fill="none" />'
        )

    # Sort lines so cross/carrier lines draw underneath Pappus/Steiner/harmonic lines
    def _line_z_key(ln: spg.Line) -> int:
        cls = model[ln].classes
        if "steiner_line" in cls:
            return 40
        if "pappus" in cls or "harmonic" in cls or "conjugate_line" in cls:
            return 30
        if "carrier" in cls:
            return 20
        return 10

    sorted_lines = sorted(visible_lines, key=_line_z_key)
    line_elems: list[str] = []
    drawn_segments_px: list[tuple[float, float, float, float]] = []

    for ln in sorted_lines:
        clipped = _clip_line_to_rect(ln, clip_xmin, clip_xmax, clip_ymin, clip_ymax)
        if clipped is None:
            continue
        (mx1, my1), (mx2, my2) = clipped
        sx1, sy1 = to_svg(mx1, my1)
        sx2, sy2 = to_svg(mx2, my2)
        smx, smy = 0.5 * (sx1 + sx2), 0.5 * (sy1 + sy2)
        drawn_segments_px.append((sx1, sy1, sx2, sy2))

        el = model[ln]
        css_cls = _line_css_classes(el.classes)

        # Build aliases for every pair of named visible points incident with ln
        incident_ids: list[str] = []
        for pt in visible_points:
            pid = model[pt].ID
            if not pid or pid.startswith("X"):
                continue
            # Fast pixel collinearity distance check + exact fallback
            px, py = pt_svg_coords[pt]
            if _point_to_segment_dist(px, py, sx1, sy1, sx2, sy2) < 0.75 and ln.contains(pt):
                incident_ids.append(pid)

        primary_ref = el.ID if el.ID else (
            f"[ {incident_ids[0]} {incident_ids[-1]} ]" if len(incident_ids) >= 2 else ""
        )
        aliases: list[str] = []
        for i in range(len(incident_ids)):
            for j in range(i + 1, len(incident_ids)):
                cand = f"[ {incident_ids[i]} {incident_ids[j]} ]"
                if cand != primary_ref:
                    aliases.append(cand)
        alias_attr = f' data-aliases="{html.escape(" | ".join(aliases))}"' if aliases else ""
        ref_attr = f' data-ref="{html.escape(primary_ref)}"' if primary_ref else ""
        eq_str = str(ln.equation())

        line_elems.append(
            f'      <path class="{css_cls}" '
            f'd="M {_fmt(sx1)} {_fmt(sy1)} L {_fmt(smx)} {_fmt(smy)} L {_fmt(sx2)} {_fmt(sy2)}"'
            f'{ref_attr}{alias_attr} fill="none">'
            f"<title>{html.escape(primary_ref)}: {html.escape(eq_str)} = 0</title></path>"
        )

    # Finite segments (spg.Segment) and Golden / harmonic sections (Section)
    visible_segments = [
        seg
        for seg in model
        if isinstance(seg, spg.Segment) and (include_guides or not model[seg].guide)
    ]
    section_elems: list[str] = []
    for seg in visible_segments:
        el = model[seg]
        p_start, p_end = seg.p1, seg.p2
        sx1, sy1 = to_svg(float(p_start.x.evalf()), float(p_start.y.evalf()))
        sx2, sy2 = to_svg(float(p_end.x.evalf()), float(p_end.y.evalf()))
        smx, smy = 0.5 * (sx1 + sx2), 0.5 * (sy1 + sy2)
        drawn_segments_px.append((sx1, sy1, sx2, sy2))
        id1 = model[p_start].ID if p_start in model else ""
        id2 = model[p_end].ID if p_end in model else ""
        primary_seg_ref = el.ID if el.ID else (f"[ {id1} {id2} ]" if id1 and id2 else "")
        seg_aliases: list[str] = []
        if id1 and id2:
            for cand in (f"[ {id1} {id2} ]", f"[ {id2} {id1} ]", f"/ {id1} {id2} /"):
                if cand != primary_seg_ref:
                    seg_aliases.append(cand)
        seg_alias_attr = (
            f' data-aliases="{html.escape(" | ".join(seg_aliases))}"' if seg_aliases else ""
        )
        seg_ref_attr = f' data-ref="{html.escape(primary_seg_ref)}"' if primary_seg_ref else ""
        cls_tokens = ["geom-segment"]
        for key, css_tok in (
            ("golden", "golden-segment"),
            ("harmonic", "harmonic-segment"),
            ("arithmetic", "arithmetic-segment"),
            ("geometric", "geometric-segment"),
            ("vector", "vector-segment"),
            ("altitude", "altitude-segment"),
        ):
            if key in el.classes:
                cls_tokens.append(css_tok)
        section_elems.append(
            f'      <path class="{" ".join(cls_tokens)}" '
            f'd="M {_fmt(sx1)} {_fmt(sy1)} L {_fmt(smx)} {_fmt(smy)} L {_fmt(sx2)} {_fmt(sy2)}"'
            f'{seg_ref_attr}{seg_alias_attr} fill="none" />'
        )

    for sec in visible_sections:
        if isinstance(sec, Section) and len(sec.points) >= 3:
            el = model[sec]
            p_start, p_end = sec.points[0], sec.points[-1]
            sx1, sy1 = to_svg(float(p_start.x.evalf()), float(p_start.y.evalf()))
            sx2, sy2 = to_svg(float(p_end.x.evalf()), float(p_end.y.evalf()))
            smx, smy = 0.5 * (sx1 + sx2), 0.5 * (sy1 + sy2)
            sec_ids = [model[p].ID for p in sec.points if p in model and model[p].ID]
            sec_ref = f"/ {' '.join(sec_ids)} /" if sec_ids else el.ID
            seg_cls = "golden-segment" if "golden" in el.classes else "harmonic-segment"
            section_elems.append(
                f'      <path class="geom-segment {seg_cls}" '
                f'd="M {_fmt(sx1)} {_fmt(sy1)} L {_fmt(smx)} {_fmt(smy)} L {_fmt(sx2)} {_fmt(sy2)}" '
                f'data-ref="{html.escape(sec_ref)}" fill="none" />'
            )

    # Sort points so Steiner and meet points sit cleanly above cross/aux points
    def _pt_z_key(pt: spg.Point) -> int:
        cls = model[pt].classes
        if "steiner" in cls:
            return 40
        if "fourth_harmonic" in cls or "meet" in cls:
            return 30
        if "given" in cls or "apex" in cls:
            return 20
        return 10

    sorted_pts = sorted(visible_points, key=_pt_z_key)
    highlight_ids = set(highlight_point_ids or ())
    point_elems: list[str] = []
    label_elems: list[str] = []
    placed_label_boxes: list[tuple[float, float, float, float]] = []
    all_pt_px = [pt_svg_coords[p] for p in sorted_pts]

    candidate_angles = [
        -0.5 * math.pi,
        0.5 * math.pi,
        -0.28 * math.pi,
        -0.72 * math.pi,
        0.28 * math.pi,
        0.72 * math.pi,
        0.0,
        math.pi,
    ]

    for pt in sorted_pts:
        sx, sy = pt_svg_coords[pt]
        # Skip points far outside the visible SVG canvas
        if sx < -8 or sx > width + 8 or sy < -8 or sy > height + 8:
            continue

        el = model[pt]
        pid = el.ID
        css_cls, radius = _point_css_and_radius(el.classes)
        x_latex = sp.latex(pt.x)
        y_latex = sp.latex(pt.y)
        tooltip = f"{pid} = ({pt.x}, {pt.y})"

        if pid in highlight_ids:
            point_elems.append(
                f'      <circle class="geom-point-halo" cx="{_fmt(sx)}" cy="{_fmt(sy)}" '
                f'r="{_fmt(radius + 4.2)}" fill="none" stroke="currentColor" stroke-opacity="0.35" stroke-width="1.6" />'
            )

        ref_attr = f' data-ref="{html.escape(pid)}"' if pid else ""
        point_elems.append(
            f'      <circle class="{css_cls}" cx="{_fmt(sx)}" cy="{_fmt(sy)}" r="{_fmt(radius)}"'
            f'{ref_attr} data-latex-x="{html.escape(x_latex)}" data-latex-y="{html.escape(y_latex)}">'
            f"<title>{html.escape(tooltip)}</title></circle>"
        )

        # Decide whether to place a text label
        if not show_labels or not pid:
            continue
        if pid.startswith("X") and not show_aux_labels:
            continue
        if pid.startswith("M") and not show_meet_labels:
            continue

        base_txt, sub_txt = _split_point_label(pid, label_overrides)
        est_w = 9.0 * len(base_txt) + 6.2 * len(sub_txt) + 4.0
        est_h = 14.0
        dist_r = radius + 11.5

        best_pos = (sx + 6.0, sy - 9.0)
        best_box = (sx, sy - est_h, sx + est_w, sy)
        best_score = -1e12
        for ang in candidate_angles:
            cand_cx = sx + math.cos(ang) * (dist_r + 0.35 * est_w)
            cand_cy = sy + math.sin(ang) * (dist_r + 0.25 * est_h)
            box = (
                cand_cx - 0.5 * est_w,
                cand_cy - 0.5 * est_h,
                cand_cx + 0.5 * est_w,
                cand_cy + 0.5 * est_h,
            )

            score = 0.0
            # Penalize clipping against viewport edges
            if box[0] < 6 or box[2] > width - 6 or box[1] < 6 or box[3] > height - 6:
                score -= 500.0

            # Penalize overlapping lines
            for lx1, ly1, lx2, ly2 in drawn_segments_px:
                d_line = _point_to_segment_dist(cand_cx, cand_cy, lx1, ly1, lx2, ly2)
                if d_line < 12.0:
                    score -= (12.0 - d_line) * 16.0

            # Penalize overlapping other points
            for opx, opy in all_pt_px:
                d_pt = math.hypot(cand_cx - opx, cand_cy - opy)
                if d_pt < 15.0:
                    score -= (15.0 - d_pt) * 20.0

            # Penalize overlapping already-placed labels
            for bx1, by1, bx2, by2 in placed_label_boxes:
                ox = max(0.0, min(box[2], bx2) - max(box[0], bx1))
                oy = max(0.0, min(box[3], by2) - max(box[1], by1))
                if ox > 0 and oy > 0:
                    score -= ox * oy * 6.0

            if score > best_score:
                best_score = score
                best_pos = (cand_cx - 0.45 * est_w, cand_cy + 0.34 * est_h)
                best_box = box

        placed_label_boxes.append(best_box)
        lx, ly = best_pos
        if sub_txt:
            inner_txt = (
                f'{html.escape(base_txt)}'
                f'<tspan class="geom-label-sub" dy="3">{html.escape(sub_txt)}</tspan>'
            )
        else:
            inner_txt = html.escape(base_txt)

        label_elems.append(
            f'      <text class="geom-label" x="{_fmt(lx)}" y="{_fmt(ly)}"'
            f'{ref_attr}>{inner_txt}</text>'
        )

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" class="euclid-graphic" '
        f'viewBox="0 0 {width} {height}" data-graphic-id="{html.escape(graphic_id)}" '
        f'role="img" aria-label="{html.escape(title)}">',
        f"  <title>{html.escape(title)}</title>",
        "  <style>",
        EMBEDDED_SVG_STYLE,
        "  </style>",
        f'  <rect class="svg-bg" x="0" y="0" width="{width}" height="{height}" rx="6" fill="none" />',
        '  <g id="elements">',
        '    <g id="graphics">',
        *conic_elems,
        *polygon_elems,
        *line_elems,
        *section_elems,
        "    </g>",
        '    <g id="highlights"></g>',
        '    <g id="points">',
        *point_elems,
        "    </g>",
        '    <g id="labels">',
        *label_elems,
        "    </g>",
        "  </g>",
        "</svg>",
        "",
    ]
    return "\n".join(parts)


def export_svg(
    model: Model,
    output_path: str | Path,
    *,
    graphic_id: str = "g1",
    title: str = "Pappus Projective Construction",
    width: int = 680,
    height: int = 440,
    margin: float = 44.0,
    bbox: tuple[float, float, float, float] | None = None,
    focus_points: Sequence[spg.Point] | None = None,
    include_guides: bool = False,
    show_labels: bool = True,
    show_meet_labels: bool = True,
    show_aux_labels: bool = False,
    label_overrides: dict[str, tuple[str, str]] | None = None,
    highlight_point_ids: Sequence[str] | None = None,
) -> Path:
    """Write an interactive SVG rendering of ``model`` to ``output_path``.

    Args:
        model: Populated :class:`~geometor.model.Model`.
        output_path: Destination ``.svg`` file path (parent directories created automatically).
        graphic_id: ``data-graphic-id`` identifier for ``geometor_interactive.js``.
        title: Accessible SVG title string.
        width: Pixel width of the SVG ``viewBox``.
        height: Pixel height of the SVG ``viewBox``.
        margin: Outer pixel margin around the framed point cloud.
        bbox: Optional explicit math viewport ``(xmin, xmax, ymin, ymax)``.
        focus_points: Optional subset of points used to compute auto-framing bounds.
        include_guides: If True, also render elements marked ``guide=True``.
        show_labels: Master toggle for point text labels.
        show_meet_labels: If False, suppress text labels on ``M...`` cross-join meets.
        show_aux_labels: If True, also label auto-discovered ``X1..Xn`` intersections.
        label_overrides: Optional mapping ``pt_id -> (base, subscript)``.
        highlight_point_ids: Optional point IDs to emphasize with an extra halo ring.

    Returns:
        Resolved :class:`~pathlib.Path` of the written SVG file.
    """
    target = Path(output_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    svg_text = render_svg_string(
        model,
        graphic_id=graphic_id,
        title=title,
        width=width,
        height=height,
        margin=margin,
        bbox=bbox,
        focus_points=focus_points,
        include_guides=include_guides,
        show_labels=show_labels,
        show_meet_labels=show_meet_labels,
        show_aux_labels=show_aux_labels,
        label_overrides=label_overrides,
        highlight_point_ids=highlight_point_ids,
    )
    target.write_text(svg_text, encoding="utf-8")
    return target.resolve()

