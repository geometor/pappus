r"""Standalone demo: The Sagacity of Bees & Honeycomb Isoperimetry (*Synagoge* V.1 & VIII.23).

Proves that $n \in \{3, 4, 6\}$ are the unique regular plane-tiling polygons,
computes exact symbolic areas for equal perimeter $P = 12$, and verifies the
circumradius $R = s_6 \sqrt{7}$ of Book VIII, Prop. 23's 7-hexagon rosette.
"""
from __future__ import annotations

import sys
from pathlib import Path

_SRC_DIR = Path(__file__).resolve().parents[1] / "src"
if str(_SRC_DIR) not in sys.path:
    sys.path.insert(0, str(_SRC_DIR))

from rich.console import Console  # noqa: E402
from rich.table import Table  # noqa: E402

from geometor.pappus import verify_honeycomb_isoperimetry  # noqa: E402


def main() -> int:
    """Run the Book V Honeycomb Isoperimetry demonstration."""
    console = Console()
    res = verify_honeycomb_isoperimetry(12, build_model=True)

    table = Table(title="Pappus Synagoge V.1 — Equal-Perimeter Regular Plane Tilings (P = 12)")
    table.add_column("Polygon", style="cyan bold")
    table.add_column("Interior Angle", justify="right", style="white")
    table.add_column("Around Vertex", justify="right", style="yellow")
    table.add_column("Side s_n", justify="right", style="white")
    table.add_column("Exact Area", style="green bold")

    names = {3: "Equilateral Triangle (n=3)", 4: "Square (n=4)", 6: "Regular Hexagon (n=6)"}
    for n_gon in res.tiling_polygons:
        table.add_row(
            names[n_gon],
            f"{res.interior_angles_deg[n_gon]}°",
            str(res.polygons_per_vertex[n_gon]),
            str(res.side_lengths[n_gon]),
            str(res.areas[n_gon]),
        )

    console.print(table)
    console.print(
        f"Area_6 / Area_3 = {res.area_hex_over_tri}, "
        f"Area_6 / Area_4 = {res.area_hex_over_sq}, "
        f"Book VIII.23 7-hexagon circumradius R_7 = {res.circumradius_seven_hexagons}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
