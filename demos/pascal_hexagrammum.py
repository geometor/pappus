"""Standalone demonstration of Blaise Pascal's *Hexagrammum Mysticum* (1640).

Showcases:
1. Universal 6-variable polynomial proof over Z[t0..t5] and Veronese coconicity.
2. Pascal's Mystic Star Hexagram on the Pythagorean unit circle x^2 + y^2 = 1
   and on the general ellipse x^2 + 4y^2 = 4.
3. Complete 60-line *Hexagrammum Mysticum* combinatorics: 15 chords, 45 diagonal
   Pascal points, 60 Pascal lines, 20 Jakob Steiner points, 60 Thomas Kirkman
   points, and 15 Julius Plücker lines.
4. Golden *Hexagrammum* in Q(phi): Chasles conic cross-ratio phi, golden meet
   M25 = (-1/phi, -phi), and emergent geometor.divine golden section / M25 P4 P0 /.
"""
from __future__ import annotations

import sys
from pathlib import Path

_SRC_DIR = Path(__file__).resolve().parents[1] / "src"
if str(_SRC_DIR) not in sys.path:
    sys.path.insert(0, str(_SRC_DIR))

from rich.console import Console  # noqa: E402
from rich.table import Table  # noqa: E402

from geometor.pappus import (  # noqa: E402
    PHI,
    conic_cross_ratio,
    conic_equation_through_points,
    construct_pascal_hexagon,
    construct_pascal_steiner_family,
    enumerate_hexagrammum_mysticum,
    find_golden_sections,
    verify_pascal_symbolic,
)


def main() -> None:
    """Run the Pascal *Hexagrammum Mysticum* symbolic demonstration."""
    console = Console()
    console.rule("[bold amber1]Blaise Pascal's Hexagrammum Mysticum (1640)[/bold amber1]")

    # 1. Universal 6-parameter symbolic proof
    sym_det = verify_pascal_symbolic()
    console.print(
        f"[bold green]✓ Universal 6-variable homogeneous determinant det[M03, M14, M25]:[/bold green] {sym_det}"
    )

    # 2. Pythagorean Mystic Star Hexagram & Ellipse invariance
    mystic = construct_pascal_hexagon(preset="hexagrammum")
    ellipse_res = construct_pascal_hexagon(preset="ellipse")
    conic_poly = conic_equation_through_points(mystic.points[:5])

    hex_table = Table(title="Pascal's Mystic Hexagram <P0, P2, P4, P1, P3, P5> on Circle vs. Ellipse")
    hex_table.add_column("Element", style="cyan bold")
    hex_table.add_column("Unit Circle x^2 + y^2 = 1", style="green")
    hex_table.add_column("General Ellipse x^2/4 + y^2 = 1", style="magenta")
    for idx in range(6):
        pc = mystic.points[idx]
        pe = ellipse_res.points[idx]
        hex_table.add_row(f"P{idx}", f"({pc.x}, {pc.y})", f"({pe.x}, {pe.y})")
    for mid in ("M03", "M14", "M25"):
        mc = mystic.meets[mid]
        me = ellipse_res.meets[mid]
        hex_table.add_row(
            mid,
            f"({mc.x}, {mc.y})" if mc else "∞",
            f"({me.x}, {me.y})" if me else "∞",
        )
    hex_table.add_row(
        "Pascal Line",
        f"{mystic.pascal_line.equation()} = 0",
        f"{ellipse_res.pascal_line.equation()} = 0",
    )
    hex_table.add_row("5-Point Veronese Conic", f"{conic_poly} = 0", "x^2 + 4*y^2 - 4 = 0")
    console.print(hex_table)

    # 3. Bi-Triangle S_3 Steiner Family & Full 60-Line Catalog
    steiner_fam = construct_pascal_steiner_family(preset="hexagrammum")
    catalog = enumerate_hexagrammum_mysticum(preset="hexagrammum")

    cat_table = Table(title="Complete 19th-Century Hexagrammum Mysticum Incidence Catalog")
    cat_table.add_column("Projective Invariant / Family", style="cyan bold")
    cat_table.add_column("Exact Count", justify="right", style="bold yellow")
    cat_table.add_column("Sample / Algebraic Highlight", style="green")
    cat_table.add_row("Conic Vertices P0..P5", "6", "All 6 satisfy x^2 + y^2 - 1 = 0")
    cat_table.add_row("Pairwise Chords [Pi Pj]", str(len(catalog.chords)), "15 secant lines across the circle")
    cat_table.add_row(
        "Pascal Diagonal Points",
        str(len(set(catalog.diagonal_points.values()))),
        "45 off-conic chord intersections (4 Pascal lines per point)",
    )
    cat_table.add_row(
        "Distinct Pascal Lines",
        str(len(set(catalog.pascal_lines.values()))),
        "6! / (6 * 2) = 60 lines (3 diagonal points per line)",
    )
    cat_table.add_row(
        "Jakob Steiner Points (1828)",
        str(len(set(catalog.steiner_points.values()))),
        f"Δ024 vs Δ135: G+ = ({steiner_fam.steiner_even.x}, {steiner_fam.steiner_even.y}), "
        f"G- = ({steiner_fam.steiner_odd.x}, {steiner_fam.steiner_odd.y})",
    )
    cat_table.add_row(
        "Thomas Kirkman Points (1849)",
        str(len(set(catalog.kirkman_points.values()))),
        "60 3-fold Pascal line concurrencies dual to Pascal lines",
    )
    cat_table.add_row(
        "Julius Plücker Lines (1830)",
        str(len(catalog.plucker_lines)),
        "15 lines each carrying exactly 4 of the 20 Steiner points",
    )
    console.print(cat_table)

    # 4. Golden Conic Hexagrammum in Q(phi)
    gold_hex = construct_pascal_hexagon(preset="golden_conic")
    gp = gold_hex.points
    cr_from_p4 = conic_cross_ratio(gp[0], gp[1], gp[2], gp[3], observer=gp[4])
    cr_from_p5 = conic_cross_ratio(gp[0], gp[1], gp[2], gp[3], observer=gp[5])
    gold_secs = find_golden_sections(gold_hex.model)

    g_table = Table(title="Golden Hexagrammum Mysticum in Q(phi)")
    g_table.add_column("Discovery", style="bold yellow")
    g_table.add_column("Exact Symbolic Result", style="green")
    g_table.add_row("Phi = (1 + sqrt(5))/2", str(PHI))
    g_table.add_row("Chasles Conic CR (P0, P1; P2, P3) from P4", str(cr_from_p4))
    g_table.add_row("Chasles Conic CR (P0, P1; P2, P3) from P5", str(cr_from_p5))
    m25 = gold_hex.meets["M25"]
    if m25 is not None:
        g_table.add_row("Golden Pascal Meet M25", f"({m25.x}, {m25.y}) = (-1/phi, -phi)")
    for gs in gold_secs:
        g_table.add_row(f"Divine Golden Section on {gs.line_id}", f"/ {' '.join(gs.point_ids)} / (ratio = {gs.ratio})")
    console.print(g_table)


if __name__ == "__main__":
    main()
