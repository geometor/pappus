0.1.0 (2026-11-11)
------------------

- Modernized repository to PEP 621 ``pyproject.toml`` (``name = "geometor-pappus"``, Python ``>=3.13``, ``ruff`` type/docstring enforcement) and ``src/geometor/pappus/`` namespace layout.
- Added ``geometor.pappus.projective`` with exact SymPy cross-ratios, Book VII Prop. 129 central perspectivities, Wildberger quadrances and spreads, algebraic fourth harmonic conjugates, Veronese :math:`6 \times 6` coconicity (``are_coconic``, ``conic_equation_through_points``), Chasles observer-independent conic cross-ratios (``conic_cross_ratio``), and collinear harmonic/golden range scanners integrated with ``geometor.divine``.
- Added ``geometor.pappus.constructions`` implementing ``construct_pappus_hexagon`` (*Synagoge* VII.138 & VII.139, ideal cross-join handling, homologous ``square``/``circle``/``diamond`` triangles), ``construct_pappus_configuration`` (all 6 :math:`S_3` permutations and Steiner Star concurrency points :math:`S_+, S_-`), ``construct_harmonic_fourth`` (straightedge complete quadrilateral), and ``verify_pappus_symbolic``.
- Added ``geometor.pappus.pascal`` implementing Blaise Pascal's *Hexagrammum Mysticum* (1640) across circles and ellipses (``construct_pascal_hexagon``), bi-triangle :math:`S_3` Steiner concurrency families (``construct_pascal_steiner_family``), complete homogeneous enumeration of all 15 chords, 45 diagonal points, 60 Pascal lines, 20 Steiner points, 60 Kirkman points, and 15 Plücker lines (``enumerate_hexagrammum_mysticum``), universal symbolic proof ``verify_pascal_symbolic``, and emergent golden conic section ``/ M25 P4 P0 /``.
- Added ``geometor.pappus.render`` and ``pappus`` CLI (``build``, ``inspect``, ``harmonics``, ``pascal``) producing 18 dark/light-aware interactive ``svg.euclid-graphic`` figures (including smooth ``<circle>`` and ``<ellipse>`` conics).
- Added five standalone runnable demonstrations in ``demos/`` and a 59-test ``pytest`` verification suite in ``tests/test_pappus.py``.
- Authored interactive Sphinx documentation under ``docsrc/`` with step-by-step ``:g:`` walkthroughs and five theorem dossiers.

0.0.1 (2022-12-22)
------------------

- Initial repository scaffold, ``pappus.py`` six-permutation harmonic exploration, and ``pappus-3.py`` type-triangle investigation.
