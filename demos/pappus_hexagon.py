"""Demonstration 1: Pappus's Hexagon Theorem (Synagoge VII.138 & VII.139) and Type Triangles.

Constructs both the general intersecting-carrier case (Prop. 139) and the parallel
carrier case (Prop. 138), verifies the universal symbolic polynomial proof over
eight free indeterminates, and revives the homologous ``square`` / ``circle`` /
``diamond`` triangles from GEOMETOR's ``pappus-3.py`` exploration.
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
    construct_pappus_hexagon,
    line_spread,
    quadrance,
    verify_pappus_symbolic,
)


def run_demo() -> None:
    """Execute the Pappus Hexagon demonstration and print exact symbolic tables."""
    console = Console()

    # 1. General projective case (Synagoge Book VII, Prop. 139)
    general = construct_pappus_hexagon(
        preset="hexagon",
        perm=(0, 1, 2),
        include_hexagon=True,
        include_type_triangles=True,
    )
    table_gen = Table(title="Synagoge VII.139 — General Intersecting Carriers")
    table_gen.add_column("Element", style="cyan bold")
    table_gen.add_column("Exact Symbolic Expression", style="green")
    table_gen.add_row("Line a", f"{general.line_a.equation()} = 0")
    table_gen.add_row("Line b", f"{general.line_b.equation()} = 0")
    table_gen.add_row("Carrier Spread s(a, b)", str(line_spread(general.line_a, general.line_b)))
    if general.apex is not None:
        table_gen.add_row("Carrier Apex O = a ∩ b", f"({general.apex.x}, {general.apex.y})")
    for m_id, m_pt in general.meets.items():
        if m_pt is not None:
            table_gen.add_row(f"Meet {m_id}", f"({m_pt.x}, {m_pt.y})")
    table_gen.add_row("Pappus Line", f"{general.pappus_line.equation()} = 0")
    table_gen.add_row("Collinear?", str(general.is_collinear))
    console.print(table_gen)

    # 2. Parallel carrier case (Synagoge Book VII, Prop. 138)
    parallel = construct_pappus_hexagon(preset="parallel", perm=(0, 1, 2))
    table_par = Table(title="Synagoge VII.138 — Parallel Carriers (s(a, b) = 0)")
    table_par.add_column("Element", style="cyan bold")
    table_par.add_column("Exact Symbolic Expression", style="green")
    table_par.add_row("Carrier Spread s(a, b)", str(line_spread(parallel.line_a, parallel.line_b)))
    for m_id, m_pt in parallel.meets.items():
        if m_pt is not None:
            table_par.add_row(f"Meet {m_id}", f"({m_pt.x}, {m_pt.y})")
    m01, m12, m20 = parallel.meets["M01"], parallel.meets["M12"], parallel.meets["M20"]
    if m01 is not None and m12 is not None and m20 is not None:
        table_par.add_row("Quadrance Q(M01, M20)", str(quadrance(m01, m20)))
        table_par.add_row("Quadrance Q(M20, M12)", str(quadrance(m20, m12)))
    table_par.add_row("Pappus Line", f"{parallel.pappus_line.equation()} = 0")
    table_par.add_row("Collinear?", str(parallel.is_collinear))
    console.print(table_par)

    # 3. Homologous Type Triangles (reviving pappus-3.py)
    tri_table = Table(title="Homologous Type Triangles (Square, Circle, Diamond)")
    tri_table.add_column("Type", style="magenta bold")
    tri_table.add_column("Vertices", style="white")
    tri_table.add_column("Exact Area", style="yellow")
    for t_name, poly in general.type_triangles.items():
        v_ids = ", ".join(general.model[v].ID for v in poly.vertices)
        tri_table.add_row(t_name, f"({v_ids})", str(abs(poly.area)))
    console.print(tri_table)

    # 4. Universal algebraic proof over Q(a0, a1, a2, b0, b1, b2, m, c)
    det_expr = verify_pappus_symbolic()
    console.print(
        f"[bold green]Universal symbolic collinearity determinant:[/bold green] {det_expr} (identically zero)"
    )


if __name__ == "__main__":
    run_demo()
