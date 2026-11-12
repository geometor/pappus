r"""Standalone demo: Pappus's Three Classical Means in a Single Semicircle (*Synagoge* III.5–16).

Constructs both the rational $(9, 16)$ semicircle ($A = 25/2, G = 12, H = 288/25$)
and the golden $(1, \phi^2)$ semicircle ($G = \phi$) in 100% exact SymPy arithmetic,
verifying $A \cdot H = G^2$, $A > G > H$, and the harmonic tangent relation $(A, C; D, T) = -1$.
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

from geometor.pappus import PHI, construct_three_means  # noqa: E402


def main() -> int:
    """Run the Book III semicircle means demonstration."""
    console = Console()
    table = Table(title="Pappus Synagoge III.5–16 — Three Means in One Semicircle")
    table.add_column("Segments (a, b)", style="cyan bold")
    table.add_column("A = (a+b)/2", style="yellow")
    table.add_column("G = sqrt(ab)", style="green")
    table.add_column("H = 2ab/(a+b)", style="magenta")
    table.add_column("A*H - G^2", justify="right", style="white")
    table.add_column("(A, C; D, T)", justify="right", style="cyan")

    for label, a_val, b_val in (
        ("Rational (9, 16)", sp.Integer(9), sp.Integer(16)),
        ("Pythagorean (4, 9)", sp.Integer(4), sp.Integer(9)),
        ("Golden (1, phi^2)", sp.Integer(1), PHI**2),
    ):
        res = construct_three_means(a_val, b_val)
        identity_zero = sp.simplify(res.arithmetic_mean * res.harmonic_mean - res.geometric_mean**2)
        table.add_row(
            label,
            str(res.arithmetic_mean),
            str(res.geometric_mean),
            str(res.harmonic_mean),
            str(identity_zero),
            str(res.harmonic_cross_ratio),
        )

    console.print(table)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
