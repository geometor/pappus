r"""Standalone demo: Pappus's *Ancient Proposition* on the Arbelos (*Synagoge* IV.14–18).

Constructs the tangent circle chain $C_1, \dots, C_5$ inside the shoemaker's knife
(*arbelos*) in 100% exact rational coordinates over $\mathbb{Q}$ and verifies both
pairwise tangency quadrances and Pappus's altitude law $y_n = n d_n = 2 n r_n$.
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
    construct_pappus_arbelos_chain,
    verify_arbelos_chain_symbolic,
)


def main() -> int:
    """Run the Book IV.14–18 Arbelos circle chain demonstration."""
    console = Console()
    res = construct_pappus_arbelos_chain(2, 1, 5)
    sym_checks = verify_arbelos_chain_symbolic()

    table = Table(title="Pappus Synagoge IV.14–18 — Infinite Arbelos Circle Chain (r1 = 2, r2 = 1)")
    table.add_column("n", justify="right", style="cyan bold")
    table.add_column("Rational Center K_n", style="white")
    table.add_column("Radius r_n", justify="right", style="yellow")
    table.add_column("Diameter d_n", justify="right", style="yellow")
    table.add_column("Height y_n", justify="right", style="green")
    table.add_column("y_n / d_n", justify="right", style="magenta bold")

    for item in res.chain:
        table.add_row(
            str(item.index),
            f"({item.center.x}, {item.center.y})",
            str(item.radius),
            str(item.diameter),
            str(item.height),
            str(item.height_over_diameter),
        )

    console.print(table)
    console.print(f"Symbolic proof residuals over Q(r1, r2, n): {sym_checks}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
