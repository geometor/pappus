"""Demonstration 3: Straightedge Fourth Harmonic Conjugate & Projective Invariance.

Constructs the fourth harmonic conjugate $D$ of $C$ with respect to $(A, B)$
using only straightedge incidences via a complete quadrilateral, verifies
$(A, B; C, D) = -1$, and proves that $D$ is completely independent of the
auxiliary apex $P$ and relay point $Q$.
"""
from __future__ import annotations

import sys
from pathlib import Path

_SRC_DIR = Path(__file__).resolve().parents[1] / "src"
if str(_SRC_DIR) not in sys.path:
    sys.path.insert(0, str(_SRC_DIR))

import sympy as sp  # noqa: E402
from rich.console import Console  # noqa: E402
from rich.table import Table  # noqa: E402

from geometor.pappus import (  # noqa: E402
    construct_harmonic_fourth,
    construct_pappus_configuration,
    cross_ratio,
    harmonic_conjugate_point,
    is_harmonic_range,
)


def run_demo() -> None:
    """Run the complete quadrilateral harmonic conjugate construction and invariance check."""
    console = Console()

    res_1 = construct_harmonic_fourth(
        pt_a=(0, 0),
        pt_b=(4, 0),
        pt_c=(sp.Rational(4, 3), 0),
        apex=(2, 3),
        relay=(sp.Rational(5, 3), sp.Rational(3, 2)),
    )
    res_2 = construct_harmonic_fourth(
        pt_a=(0, 0),
        pt_b=(4, 0),
        pt_c=(sp.Rational(4, 3), 0),
        apex=(-1, 5),
        relay=(sp.Rational(2, 5), 2),
    )
    algebraic_d = harmonic_conjugate_point(res_1.pt_a, res_1.pt_b, res_1.pt_c)
    cr_val = cross_ratio(res_1.pt_a, res_1.pt_b, res_1.pt_c, res_1.pt_d)

    q_table = Table(title="Complete Quadrilateral Fourth Harmonic Construction")
    q_table.add_column("Quantity", style="cyan bold")
    q_table.add_column("Exact Value", style="green")
    q_table.add_row("Base Points A, B", f"({res_1.pt_a.x}, {res_1.pt_a.y}), ({res_1.pt_b.x}, {res_1.pt_b.y})")
    q_table.add_row("Interior Point C", f"({res_1.pt_c.x}, {res_1.pt_c.y})")
    q_table.add_row("Constructed D (Trial 1: P=(2,3))", f"({res_1.pt_d.x}, {res_1.pt_d.y})")
    q_table.add_row("Constructed D' (Trial 2: P=(-1,5))", f"({res_2.pt_d.x}, {res_2.pt_d.y})")
    q_table.add_row("Algebraic Formula D", f"({algebraic_d.x}, {algebraic_d.y})")
    q_table.add_row("D == D' == Algebraic?", str(res_1.pt_d.equals(res_2.pt_d) and res_1.pt_d.equals(algebraic_d)))
    q_table.add_row("Cross-Ratio (A, B; C, D)", str(cr_val))
    q_table.add_row("is_harmonic_range(A, B, C, D)", str(is_harmonic_range(res_1.pt_a, res_1.pt_b, res_1.pt_c, res_1.pt_d)))
    console.print(q_table)

    # Emergent harmonic tetrads inside the Pappus configuration
    cfg = construct_pappus_configuration(preset="harmonic", discover_all_intersections=True)
    h_table = Table(title=f"Sample Emergent Harmonic Ranges in Pappus Configuration ({len(cfg.harmonic_ranges)} total)")
    h_table.add_column("#", justify="right", style="dim")
    h_table.add_column("Carrier Line", style="cyan")
    h_table.add_column("Ordered Points (P1 < P2 < P3 < P4)", style="white")
    h_table.add_column("(P1, P3; P2, P4)", style="green")
    for idx, hr in enumerate(cfg.harmonic_ranges[:10], start=1):
        h_table.add_row(str(idx), hr.line_id, f"({', '.join(hr.point_ids)})", str(hr.value))
    console.print(h_table)


if __name__ == "__main__":
    run_demo()
