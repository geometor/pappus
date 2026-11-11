0.1.0 (2026-11-11)
------------------

- Modernized repository to PEP 621 ``pyproject.toml`` (``name = "geometor-pappus"``, Python ``>=3.13``, ``ruff`` type/docstring enforcement) and ``src/geometor/pappus/`` namespace layout.
- Added ``geometor.pappus.projective`` with exact SymPy cross-ratios, Book VII Prop. 129 central perspectivities, Wildberger quadrances and spreads, algebraic fourth harmonic conjugates, and collinear harmonic/golden range scanners integrated with ``geometor.divine``.
- Added ``geometor.pappus.constructions`` implementing ``construct_pappus_hexagon`` (*Synagoge* VII.138 & VII.139, ideal cross-join handling, homologous ``square``/``circle``/``diamond`` triangles), ``construct_pappus_configuration`` (all 6 :math:`S_3` permutations and Steiner Star concurrency points :math:`S_+, S_-`), ``construct_harmonic_fourth`` (straightedge complete quadrilateral), and ``verify_pappus_symbolic``.
- Added ``geometor.pappus.render`` and ``pappus`` CLI (``build``, ``inspect``, ``harmonics``) producing 14 dark/light-aware interactive ``svg.euclid-graphic`` figures.
- Added standalone runnable demonstrations in ``demos/`` and a 40-test ``pytest`` verification suite in ``tests/test_pappus.py``.
- Authored interactive Sphinx documentation under ``docsrc/`` with step-by-step ``:g:`` walkthroughs and four theorem dossiers.

0.0.1 (2022-12-22)
------------------

- Initial repository scaffold, ``pappus.py`` six-permutation harmonic exploration, and ``pappus-3.py`` type-triangle investigation.
