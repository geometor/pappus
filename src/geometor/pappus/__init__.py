"""Symbolic projective geometry explorations inspired by Pappus of Alexandria and Blaise Pascal.

Provides exact SymPy and :mod:`geometor.model` constructions of Pappus's Hexagon
Theorem (*Synagoge* Book VII, Props. 138 & 139), Blaise Pascal's *Hexagrammum
Mysticum* (1640) on circles and conics, the full :math:`S_3` six-permutation
Steiner configuration with its 3-fold star concurrency points :math:`(S_+, S_-)`,
the 60-line *Hexagrammum Mysticum* catalog (20 Steiner points, 60 Kirkman points,
15 Plücker lines), complete-quadrilateral harmonic conjugates, projective
cross-ratios, and golden ratio perspectivities.
"""
from __future__ import annotations

from geometor.pappus.constructions import (
    PERMUTATIONS_S3,
    PRESETS,
    TYPE_NAMES,
    HarmonicFourthResult,
    PappusConfigurationResult,
    PappusHexagonResult,
    PresetConfig,
    construct_harmonic_fourth,
    construct_pappus_configuration,
    construct_pappus_hexagon,
    get_preset,
    permutation_parity,
    verify_pappus_symbolic,
)
from geometor.pappus.pascal import (
    PASCAL_PRESETS,
    Cycle6,
    HexagrammumMysticumCatalog,
    PascalHexagonResult,
    PascalPresetConfig,
    PascalSteinerFamilyResult,
    canonical_hexagon_cycle,
    construct_pascal_hexagon,
    construct_pascal_steiner_family,
    enumerate_hexagrammum_mysticum,
    get_pascal_preset,
    verify_pascal_symbolic,
)
from geometor.pappus.projective import (
    PHI,
    GoldenRange,
    HarmonicRange,
    anharmonic_orbit,
    are_coconic,
    circle_stereographic_point,
    conic_cross_ratio,
    conic_equation_through_points,
    cross_ratio,
    enable_divine_analysis,
    exact_line_meet,
    find_golden_sections,
    find_harmonic_ranges,
    harmonic_conjugate_point,
    is_harmonic_range,
    line_spread,
    project_point,
    quadrance,
)
from geometor.pappus.render import EMBEDDED_SVG_STYLE, export_svg, render_svg_string

__version__ = "0.1.0"

__all__ = [
    "__version__",
    "PHI",
    "PERMUTATIONS_S3",
    "TYPE_NAMES",
    "PRESETS",
    "PASCAL_PRESETS",
    "Cycle6",
    "PresetConfig",
    "PascalPresetConfig",
    "HarmonicRange",
    "GoldenRange",
    "PappusHexagonResult",
    "PappusConfigurationResult",
    "HarmonicFourthResult",
    "PascalHexagonResult",
    "PascalSteinerFamilyResult",
    "HexagrammumMysticumCatalog",
    "get_preset",
    "get_pascal_preset",
    "permutation_parity",
    "canonical_hexagon_cycle",
    "quadrance",
    "line_spread",
    "exact_line_meet",
    "project_point",
    "circle_stereographic_point",
    "conic_equation_through_points",
    "are_coconic",
    "conic_cross_ratio",
    "cross_ratio",
    "anharmonic_orbit",
    "is_harmonic_range",
    "harmonic_conjugate_point",
    "find_harmonic_ranges",
    "find_golden_sections",
    "enable_divine_analysis",
    "construct_pappus_hexagon",
    "construct_pappus_configuration",
    "construct_harmonic_fourth",
    "construct_pascal_hexagon",
    "construct_pascal_steiner_family",
    "enumerate_hexagrammum_mysticum",
    "verify_pappus_symbolic",
    "verify_pascal_symbolic",
    "EMBEDDED_SVG_STYLE",
    "render_svg_string",
    "export_svg",
]
