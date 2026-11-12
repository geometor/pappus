r"""Standalone demo: Pappus's Area Theorem (*Synagoge* Book IV, Prop. 1).

Demonstrates Pappus's affine generalization of the Pythagorean Theorem (*Elements* I.47)
on an arbitrary scalene triangle with oblique parallelograms, on the $3$-$4$-$5$ right
triangle with squares, and universally over $\mathbb{Z}[x_A, y_A, x_B, y_B, x_C, y_C, u_x, u_y, v_x, v_y]$.
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
    construct_pappus_area_theorem,
    verify_pappus_area_symbolic,
)


def main() -> int:
    """Run the Book IV.1 Pappus Area Theorem demonstration."""
    console = Console()
    table = Table(title="Pappus Synagoge IV.1 — Area Theorem on Arbitrary Parallelograms")
    table.add_column("Case", style="cyan bold")
    table.add_column("Apex H = [DE] ∩ [FG]", style="white")
    table.add_column("Area(ABDE)", justify="right", style="yellow")
    table.add_column("Area(ACFG)", justify="right", style="yellow")
    table.add_column("Area(BCML)", justify="right", style="green bold")
    table.add_column("Residual", justify="right", style="magenta")

    for preset in ("scalene", "pythagoras"):
        res = construct_pappus_area_theorem(preset=preset)
        table.add_row(
            preset,
            f"({res.apex_h.x}, {res.apex_h.y})",
            str(res.area_ab),
            str(res.area_ac),
            str(res.area_bc),
            str(res.area_residual),
        )

    sym_residual = verify_pappus_area_symbolic()
    table.add_row("Universal 10-var Polynomial", "symbolic H", "det(A-B,u)", "det(v,A-C)", "det(B-C,A-H)", str(sym_residual))
    console.print(table)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
