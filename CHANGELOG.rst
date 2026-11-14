0.2.1 (2026-11-14)
------------------

- Standardized Book Title Page, top-level header navigation (``Book``, ``People``, ``Bibliography``, ``Usage``), Reader's Guide (``docsrc/usage/``), featured Author and Translator profiles in People, and English structural terminology.

0.2.0 (2026-11-12)
------------------

- **Multi-Track *Synagoge* Book Codex** (``docsrc/synagoge/``): Added a 5-unit, 4-track
  (``-en``, ``-el``, ``-summary``, ``-notes``) Book Codex (:layout: ``book``) covering
  **Books III, IV, V, VII, and VIII** of Pappus of Alexandria's *Synagoge* (*Μαθηματικὴ
  Συναγωγή*, c. 340 CE), pairing Friedrich Hultsch's 1876–1878 critical polytonic Greek text
  with 100% original GEOMETOR English translations, bidirectional ``geometor/euclid`` citation
  concordance, *Index Nominum*, bibliography, and Greek/Latin mathematical glossary.
- **Exact Symbolic *Synagoge* Demonstrations** (``geometor.pappus.synagoge_demos``):

  - ``construct_three_means`` (*Book III, Props. 28–30*): arithmetic, geometric, and harmonic
    means inside a single semicircle ($A \cdot H = G^2$) with exact orthogonal foot projection
    $F$ and external harmonic tangent conjugate $(A, C; D, T) = -1$ over $\mathbb{Q}$ and
    $\mathbb{Q}(\phi)$.
  - ``construct_pappus_area_theorem`` & ``verify_pappus_area_symbolic`` (*Book IV, Prop. 1*):
    Pappus's equiaffine parallelogram generalization of *Elements* I.47 plus a universal
    10-variable polynomial proof over $\mathbb{Z}$.
  - ``construct_pappus_arbelos_chain`` & ``verify_arbelos_chain_symbolic`` (*Book IV,
    Props. 14–18*): infinite tangent circle chain inside the *arbelos* in 100% rational
    coordinates proving $y_n = n\,d_n = 2n\,r_n$ and focal ellipse locus invariance.
  - ``verify_honeycomb_isoperimetry`` & ``construct_honeycomb_isoperimetry`` (*Book V, Prop. 1
    & Book VIII, Prop. 23*): Diophantine proof of unique regular planar tessellations
    $n \in \{3, 4, 6\}$, exact $\mathbb{Q}(\sqrt{3})$ area ratios, and 7-hexagon circle
    inscription ($R = s_6\sqrt{7}$).

- **Sphinx Extension, CLI & Gallery Expansion**: Added ``geometor.pappus.sphinx_ext``
  (registering the ``-el`` Greek companion track and offline sibling ``objects.inv``
  intersphinx), ``pappus synagoge`` and ``pappus build --synagoge`` CLI commands, 6 new
  ``.euclid-graphic`` SVGs (24 total), 4 new standalone ``demos/`` scripts (9 total), and
  comprehensive ``tests/test_synagoge.py`` verification.

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
