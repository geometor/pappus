r"""Demonstration 4: Golden Projectivity, Cross-Ratio Orbits & Book VII Prop. 129.

Connects Pappus's invariance of the cross-ratio under central perspectivity
(*Synagoge* Book VII, Prop. 129) to GEOMETOR's central theme of the Golden Ratio
$\phi = (1 + \sqrt{5})/2$:

1. Verifies the canonical golden chain cross-ratio $(0, 1; \phi, \phi + 1) = \phi$
   and computes its six-value anharmonic $S_4 / V_4$ orbit in $\mathbb{Q}(\phi)$.
2. Proves the harmonic-golden identity $(0, \phi; 1, \phi^3) = -1$ where $\phi^3 = 2\phi + 1$.
3. Projects a golden range onto an oblique line via central perspectivity and
   verifies exact preservation of $\phi$ in the cross-ratio even when Euclidean
   ratios change.
4. Constructs the Golden Pappus Hexagon over $\mathbb{Q}(\phi)$ and scans it with
   :mod:`geometor.divine`.
"""
from __future__ import annotations

import sys
from pathlib import Path

_SRC_DIR = Path(__file__).resolve().parents[1] / "src"
if str(_SRC_DIR) not in sys.path:
    sys.path.insert(0, str(_SRC_DIR))

import sympy as sp  # noqa: E402
import sympy.geometry as spg  # noqa: E402
from geometor.model import Model  # noqa: E402
from rich.console import Console  # noqa: E402
from rich.table import Table  # noqa: E402

from geometor.pappus import (  # noqa: E402
    PHI,
    anharmonic_orbit,
    construct_pappus_hexagon,
    cross_ratio,
    enable_divine_analysis,
    find_golden_sections,
    harmonic_conjugate_point,
    project_point,
)


def run_demo() -> None:
    """Execute the Golden Projectivity demonstration."""
    console = Console()

    # 1. Canonical golden chain & anharmonic orbit
    p0 = spg.Point(0, 0)
    p1 = spg.Point(1, 0)
    p2 = spg.Point(PHI, 0)
    p3 = spg.Point(PHI + 1, 0)
    cr_golden = cross_ratio(p0, p1, p2, p3)
    orbit = anharmonic_orbit(cr_golden)

    # 2. Fourth harmonic conjugate of 1 w.r.t. (0, phi) is phi^3 = 2*phi + 1
    h_conj = harmonic_conjugate_point(p0, p2, p1)
    cr_harm_gold = cross_ratio(p0, p2, p1, h_conj)

    # 3. Central perspectivity (Synagoge VII.129) onto an oblique target line
    center = spg.Point(1, 3)
    target_line = spg.Line(spg.Point(0, 1), spg.Point(4, 2))
    projected = [project_point(center, target_line, pt) for pt in (p0, p1, p2, p3)]
    cr_projected = cross_ratio(*projected)

    inv_table = Table(title="Golden Cross-Ratios & Book VII Prop. 129 Perspectivity")
    inv_table.add_column("Property", style="cyan bold")
    inv_table.add_column("Exact Symbolic Result", style="green")
    inv_table.add_row("Golden Ratio φ", f"{PHI} ≈ {float(PHI.evalf()):.10f}")
    inv_table.add_row("Chain Cross-Ratio (0, 1; φ, φ+1)", f"{cr_golden} (equals φ: {sp.simplify(cr_golden - PHI) == 0})")
    inv_table.add_row("6-Value Anharmonic Orbit", ", ".join(str(v) for v in orbit))
    inv_table.add_row("Harmonic Conjugate D of 1 w.r.t. (0, φ)", f"x = {h_conj.x} = 2φ + 1 = φ³ (equals φ³: {sp.simplify(h_conj.x - PHI**3) == 0})")
    inv_table.add_row("Verify (0, φ; 1, φ³)", str(cr_harm_gold))
    inv_table.add_row("Projected Cross-Ratio on x - 4y + 4 = 0", f"{cr_projected} (invariant: {sp.simplify(cr_projected - cr_golden) == 0})")
    console.print(inv_table)

    # 4. Golden Pappus Hexagon with geometor.divine analysis
    model = enable_divine_analysis(Model("golden_pappus"))
    gold_hex = construct_pappus_hexagon(model=model, preset="golden", perm=(0, 1, 2))
    sections = find_golden_sections(gold_hex.model, register_sections=True)

    g_table = Table(title="Golden Pappus Hexagon in Q(φ)")
    g_table.add_column("Element", style="bold yellow")
    g_table.add_column("Exact Symbolic Expression", style="cyan")
    for m_id, m_pt in gold_hex.meets.items():
        if m_pt is not None:
            g_table.add_row(f"Meet {m_id}", f"({m_pt.x}, {m_pt.y})")
    g_table.add_row("Pappus Line", f"{gold_hex.pappus_line.equation()} = 0")
    g_table.add_row("Collinear over Q(φ)?", str(gold_hex.is_collinear))
    g_table.add_row("Golden Sections Discovered", str(len(sections)))
    for sec in sections:
        g_table.add_row(f"  Golden Section on {sec.line_id}", f"{sec.point_ids} -> ratio = {sec.ratio}")
    console.print(g_table)


if __name__ == "__main__":
    run_demo()
