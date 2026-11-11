"""Command-line interface for ``geometor.pappus``.

Provides ``pappus build`` (reproducibly generating all interactive SVG figures),
``pappus inspect`` (reporting exact SymPy coordinates, Pappus lines, and Steiner
star points), and ``pappus harmonics`` (scanning configurations for exact
harmonic ranges and golden sections).
"""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from rich.console import Console
from rich.table import Table

from geometor.pappus.constructions import (
    PERMUTATIONS_S3,
    PRESETS,
    construct_harmonic_fourth,
    construct_pappus_configuration,
    construct_pappus_hexagon,
    verify_pappus_symbolic,
)
from geometor.pappus.projective import (
    cross_ratio,
    find_golden_sections,
    find_harmonic_ranges,
)
from geometor.pappus.render import export_svg

__all__ = [
    "build_gallery",
    "cmd_build",
    "cmd_inspect",
    "cmd_harmonics",
    "build_parser",
    "main",
]


def build_gallery(output_dir: str | Path = "docsrc/_static/constructions") -> list[Path]:
    """Generate the complete gallery of interactive SVG diagrams for documentation.

    Args:
        output_dir: Directory into which SVG files will be written.

    Returns:
        List of resolved :class:`~pathlib.Path` objects for generated SVGs.
    """
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []

    # 1. Canonical Hexagon Theorem (Synagoge VII.139)
    hex_res = construct_pappus_hexagon(preset="hexagon", perm=(0, 1, 2), include_hexagon=True)
    written.append(
        export_svg(
            hex_res.model,
            out / "pappus_hexagon.svg",
            graphic_id="g1",
            title="Pappus's Hexagon Theorem (Synagoge VII.139)",
            highlight_point_ids=["M01", "M12", "M20"],
        )
    )

    # 2. Parallel Carriers Case (Synagoge VII.138)
    par_res = construct_pappus_hexagon(preset="parallel", perm=(0, 1, 2), include_hexagon=True)
    written.append(
        export_svg(
            par_res.model,
            out / "pappus_parallel.svg",
            graphic_id="g1",
            title="Pappus's Parallel-Line Lemma (Synagoge VII.138)",
            highlight_point_ids=["M01", "M12", "M20"],
        )
    )

    # 3. Perspective Type Triangles (square / circle / diamond from pappus-3.py)
    tri_res = construct_pappus_hexagon(
        preset="hexagon",
        perm=(0, 1, 2),
        include_hexagon=False,
        include_type_triangles=True,
    )
    written.append(
        export_svg(
            tri_res.model,
            out / "pappus_triangles.svg",
            graphic_id="g2",
            title="Homologous Type Triangles (Square, Circle, Diamond)",
            highlight_point_ids=["M01", "M12", "M20"],
        )
    )

    # 4. Individual S_3 Permutations (0..5) on compact "steiner" preset
    for idx, perm in enumerate(PERMUTATIONS_S3):
        perm_res = construct_pappus_hexagon(preset="steiner", perm=perm, include_hexagon=True)
        written.append(
            export_svg(
                perm_res.model,
                out / f"pappus_perm_{idx}.svg",
                graphic_id=f"g{idx + 1}",
                title=f"Pappus Permutation ({perm[0]}, {perm[1]}, {perm[2]}) [{perm_res.parity}]",
                width=520,
                height=360,
                bbox=(-0.6, 6.6, -3.9, 2.5),
                highlight_point_ids=["M01", "M12", "M20"],
            )
        )

    # 5. Full Six-Permutation Steiner Configuration (compact convergent preset)
    steiner_res = construct_pappus_configuration(preset="steiner", scan_harmonics=True)
    written.append(
        export_svg(
            steiner_res.model,
            out / "pappus_steiner.svg",
            graphic_id="g7",
            title="The Six Pappus Lines and Two Steiner Star Points (S+, S-)",
            width=720,
            height=480,
            bbox=(-0.6, 6.6, -3.9, 2.5),
            show_meet_labels=False,
            highlight_point_ids=["S1", "S2"],
        )
    )

    # 6. Original 2023 Parallel Steiner Configuration (focused on S+ and central hexagon)
    par_cfg = construct_pappus_configuration(preset="parallel", scan_harmonics=True)
    written.append(
        export_svg(
            par_cfg.model,
            out / "pappus_parallel_steiner.svg",
            graphic_id="g8",
            title="2023 GEOMETOR Parallel Configuration — Even Star Point S+ = (90/73, 38/73)",
            width=680,
            height=420,
            bbox=(-0.6, 3.6, -0.45, 1.45),
            show_meet_labels=False,
            highlight_point_ids=["S1"],
        )
    )

    # 7. Straightedge Fourth Harmonic Conjugate (Complete Quadrilateral)
    harm_fourth = construct_harmonic_fourth()
    written.append(
        export_svg(
            harm_fourth.model,
            out / "harmonic_fourth.svg",
            graphic_id="g1",
            title="Complete Quadrilateral Straightedge Construction of Fourth Harmonic D",
            highlight_point_ids=["C", "D"],
        )
    )

    # 8. Rich 21-Harmonic-Range Pappus Configuration
    harm_cfg = construct_pappus_configuration(
        preset="harmonic",
        discover_all_intersections=True,
        scan_harmonics=True,
    )
    written.append(
        export_svg(
            harm_cfg.model,
            out / "pappus_harmonics.svg",
            graphic_id="g2",
            title="Emergent Harmonic Ranges in the Pappus–Steiner Configuration",
            width=700,
            height=460,
            bbox=(-2.5, 4.6, -2.0, 3.5),
            show_meet_labels=False,
            highlight_point_ids=["S1", "S2"],
        )
    )

    # 9. Golden Projective Pappus Configuration in Q(phi)
    gold_hex = construct_pappus_hexagon(preset="golden", perm=(0, 1, 2), include_hexagon=True)
    find_golden_sections(gold_hex.model, register_sections=True)
    written.append(
        export_svg(
            gold_hex.model,
            out / "golden_pappus.svg",
            graphic_id="g3",
            title="Golden Ratio Projectivity in Pappus's Hexagon over Q(phi)",
            highlight_point_ids=["A1", "A2", "B1", "B2", "M01", "M12", "M20"],
        )
    )

    return written


def cmd_build(args: argparse.Namespace, console: Console) -> int:
    """Execute ``pappus build``."""
    written = build_gallery(args.output_dir)
    table = Table(title="Generated Interactive SVG Figures")
    table.add_column("#", justify="right", style="dim")
    table.add_column("Filename", style="cyan bold")
    table.add_column("Path", style="green")
    for idx, path in enumerate(written, start=1):
        table.add_row(str(idx), path.name, str(path))
    console.print(table)
    return 0


def cmd_inspect(args: argparse.Namespace, console: Console) -> int:
    """Execute ``pappus inspect``."""
    preset_name: str = args.preset
    if args.all_permutations:
        cfg_res = construct_pappus_configuration(
            preset=preset_name,
            discover_all_intersections=args.discover_all,
            scan_harmonics=True,
            enable_divine=True,
        )
        console.print(f"[bold amber1]Preset:[/bold amber1] {PRESETS[preset_name].title}")
        p_table = Table(title="Six S_3 Pappus Lines")
        p_table.add_column("Perm", style="cyan bold")
        p_table.add_column("Parity", style="magenta")
        p_table.add_column("Meets", style="white")
        p_table.add_column("Equation (= 0)", style="green")
        for perm in PERMUTATIONS_S3:
            parity = "even" if cfg_res.pappus_lines[perm] in cfg_res.even_pappus_lines else "odd"
            m_pts = cfg_res.meets_by_perm[perm]
            m_ids = ", ".join(cfg_res.model[m].ID if m is not None else "∞" for m in m_pts)
            eq = str(cfg_res.pappus_lines[perm].equation())
            p_table.add_row(str(perm), parity, m_ids, eq)
        console.print(p_table)

        s_table = Table(title="Steiner Star Concurrency Points")
        s_table.add_column("Point", style="bold yellow")
        s_table.add_column("Exact Coordinates", style="cyan")
        s_table.add_row(
            "S+ (S1, even A_3)",
            str((cfg_res.steiner_even.x, cfg_res.steiner_even.y)) if cfg_res.steiner_even else "Ideal (∞)",
        )
        s_table.add_row(
            "S- (S2, odd S_3 \\ A_3)",
            str((cfg_res.steiner_odd.x, cfg_res.steiner_odd.y)) if cfg_res.steiner_odd else "Ideal (∞)",
        )
        if cfg_res.steiner_line is not None:
            s_table.add_row("Steiner Line [S+ S-]", f"{cfg_res.steiner_line.equation()} = 0")
        console.print(s_table)
    else:
        hex_res = construct_pappus_hexagon(preset=preset_name)
        sym_zero = verify_pappus_symbolic()
        table = Table(title=f"Pappus Hexagon Inspection — {PRESETS[preset_name].title}")
        table.add_column("Element", style="cyan bold")
        table.add_column("Exact Symbolic Value", style="green")
        for pt in (*hex_res.a_points, *hex_res.b_points):
            table.add_row(hex_res.model[pt].ID, f"({pt.x}, {pt.y})")
        if hex_res.apex is not None:
            table.add_row("O (a ∩ b)", f"({hex_res.apex.x}, {hex_res.apex.y})")
        for m_id, m_pt in hex_res.meets.items():
            table.add_row(m_id, f"({m_pt.x}, {m_pt.y})" if m_pt is not None else "Ideal (∞)")
        table.add_row("Pappus Line", f"{hex_res.pappus_line.equation()} = 0")
        table.add_row("Collinear?", str(hex_res.is_collinear))
        table.add_row("Universal Symbolic Det", str(sym_zero))
        console.print(table)
    return 0


def cmd_harmonics(args: argparse.Namespace, console: Console) -> int:
    """Execute ``pappus harmonics``."""
    cfg_res = construct_pappus_configuration(
        preset=args.preset,
        discover_all_intersections=args.discover_all,
        scan_harmonics=False,
        enable_divine=True,
    )
    harmonics = find_harmonic_ranges(cfg_res.model)
    goldens = find_golden_sections(cfg_res.model)

    h_table = Table(title=f"Collinear Harmonic Ranges ({len(harmonics)} discovered in '{args.preset}')")
    h_table.add_column("#", justify="right", style="dim")
    h_table.add_column("Line", style="cyan")
    h_table.add_column("Ordered Tetrad (P1 < P2 < P3 < P4)", style="bold white")
    h_table.add_column("(P1, P3; P2, P4)", style="green")
    for idx, hr in enumerate(harmonics, start=1):
        cr = cross_ratio(hr.points[0], hr.points[2], hr.points[1], hr.points[3])
        h_table.add_row(
            str(idx),
            hr.line_id,
            f"({', '.join(hr.point_ids)})",
            str(cr),
        )
    console.print(h_table)

    if goldens:
        g_table = Table(title=f"Golden Ratio Sections ({len(goldens)} discovered)")
        g_table.add_column("#", justify="right", style="dim")
        g_table.add_column("Line", style="cyan")
        g_table.add_column("Points", style="bold yellow")
        g_table.add_column("Exact Ratio", style="green")
        for idx, gr in enumerate(goldens, start=1):
            g_table.add_row(str(idx), gr.line_id, f"({', '.join(gr.point_ids)})", str(gr.ratio))
        console.print(g_table)
    return 0


def build_parser() -> argparse.ArgumentParser:
    """Build the ``pappus`` CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="pappus",
        description="Symbolic projective geometry toolkit for Pappus's Hexagon Theorem & harmonic cross-ratios.",
    )
    sub = parser.add_subparsers(dest="command")

    p_build = sub.add_parser("build", help="Generate all interactive SVG figures.")
    p_build.add_argument(
        "-o",
        "--output-dir",
        default="docsrc/_static/constructions",
        help="Destination folder for generated SVGs (default: docsrc/_static/constructions).",
    )

    p_inspect = sub.add_parser("inspect", help="Inspect exact coordinates, Pappus lines, and Steiner points.")
    p_inspect.add_argument(
        "-p",
        "--preset",
        choices=sorted(PRESETS),
        default="hexagon",
        help="Coordinate preset to inspect.",
    )
    p_inspect.add_argument(
        "-a",
        "--all-permutations",
        action="store_true",
        help="Construct all 6 S_3 permutations and report Steiner concurrency points.",
    )
    p_inspect.add_argument(
        "--discover-all",
        action="store_true",
        help="Also compute all pairwise line intersections.",
    )

    p_harm = sub.add_parser("harmonics", help="Scan a Pappus configuration for harmonic & golden ranges.")
    p_harm.add_argument(
        "-p",
        "--preset",
        choices=sorted(PRESETS),
        default="harmonic",
        help="Coordinate preset to scan (default: harmonic).",
    )
    p_harm.add_argument(
        "--discover-all",
        action="store_true",
        help="Include all pairwise line-line intersections when scanning.",
    )

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Entry point for the ``pappus`` CLI."""
    parser = build_parser()
    args = parser.parse_args(argv)
    console = Console()

    if args.command == "build":
        return cmd_build(args, console)
    if args.command == "harmonics":
        return cmd_harmonics(args, console)
    if args.command == "inspect":
        return cmd_inspect(args, console)

    # Default when invoked with no subcommand: inspect canonical hexagon
    default_args = argparse.Namespace(preset="hexagon", all_permutations=False, discover_all=False)
    return cmd_inspect(default_args, console)


if __name__ == "__main__":
    raise SystemExit(main())
