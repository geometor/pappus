"""Symbolic projective geometry explorations inspired by Pappus of Alexandria.

Provides exact SymPy and :mod:`geometor.model` constructions of Pappus's Hexagon
Theorem (*Synagoge* Book VII, Props. 138 & 139), the full :math:`S_3` six-permutation
Steiner configuration with its two 3-fold star concurrency points :math:`(S_+, S_-)`,
complete-quadrilateral harmonic conjugates, projective cross-ratios, and golden
ratio perspectivities.
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
from geometor.pappus.projective import (
    PHI,
    GoldenRange,
    HarmonicRange,
    anharmonic_orbit,
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
from geometor.pappus.render import export_svg, render_svg_string

__version__ = "0.1.0"

__all__ = [
    "__version__",
    "PHI",
    "PERMUTATIONS_S3",
    "TYPE_NAMES",
    "PRESETS",
    "PresetConfig",
    "HarmonicRange",
    "GoldenRange",
    "PappusHexagonResult",
    "PappusConfigurationResult",
    "HarmonicFourthResult",
    "permutation_parity",
    "get_preset",
    "construct_pappus_hexagon",
    "construct_pappus_configuration",
    "construct_harmonic_fourth",
    "verify_pappus_symbolic",
    "quadrance",
    "line_spread",
    "exact_line_meet",
    "project_point",
    "cross_ratio",
    "anharmonic_orbit",
    "is_harmonic_range",
    "harmonic_conjugate_point",
    "find_harmonic_ranges",
    "find_golden_sections",
    "enable_divine_analysis",
    "render_svg_string",
    "export_svg",
]
