r"""Demonstration 2: The Six Permutations (S_3) & Steiner's Two Star Concurrency Points.

Revives and completes GEOMETOR's 2023 ``pappus.py`` exploration: permuting
$(B_0, B_1, B_2)$ across all $3! = 6$ elements of $S_3$ yields six Pappus lines
that split by permutation parity into two concurrent triples:

- The 3 **even** Pappus lines ($A_3$) concur at the even star point $S_+$.
- The 3 **odd** Pappus lines ($S_3 \setminus A_3$) concur at the odd star point $S_-$.
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
    PERMUTATIONS_S3,
    construct_pappus_configuration,
    permutation_parity,
)


def run_demo() -> None:
    """Construct and compare both the 2023 parallel configuration and the compact Steiner configuration."""
    console = Console()

    for preset_key in ("parallel", "steiner"):
        cfg = construct_pappus_configuration(preset=preset_key, scan_harmonics=True)
        table = Table(title=f"Six-Permutation Pappus–Steiner Configuration ({preset_key})")
        table.add_column("#", justify="right", style="dim")
        table.add_column("Perm σ", style="cyan bold")
        table.add_column("Parity", style="magenta")
        table.add_column("Three Cross-Join Meets", style="white")
        table.add_column("Pappus Line Equation (= 0)", style="green")

        for idx, perm in enumerate(PERMUTATIONS_S3):
            parity = permutation_parity(perm)
            meets = cfg.meets_by_perm[perm]
            meet_str = ", ".join(
                f"{cfg.model[m].ID}=({m.x},{m.y})" if m is not None else "∞"
                for m in meets
            )
            eq_str = str(cfg.pappus_lines[perm].equation())
            table.add_row(str(idx), str(perm), parity, meet_str, eq_str)
        console.print(table)

        star_table = Table(title=f"Steiner Concurrency Summary ({preset_key})")
        star_table.add_column("Invariant", style="bold yellow")
        star_table.add_column("Exact Symbolic Result", style="cyan")
        star_table.add_row("Total Cross-Join Meets", str(len(cfg.all_meets)))
        if cfg.steiner_even is not None:
            star_table.add_row("Even Star Point S+ (S1)", f"({cfg.steiner_even.x}, {cfg.steiner_even.y})")
        if cfg.steiner_odd is not None:
            star_table.add_row("Odd Star Point S- (S2)", f"({cfg.steiner_odd.x}, {cfg.steiner_odd.y})")
        if cfg.steiner_line is not None:
            star_table.add_row("Steiner Line [S+ S-]", f"{cfg.steiner_line.equation()} = 0")
        star_table.add_row("Collinear Harmonic Tetrads", str(len(cfg.harmonic_ranges)))
        console.print(star_table)


if __name__ == "__main__":
    run_demo()
