======
pappus
======

**Pappus of Alexandria's *Synagoge* (*Μαθηματικὴ Συναγωγή*) Multi-Track Book Codex (Books III, IV, V, VII & VIII) and exact symbolic constructions for classical means, generalized Pythagorean areas, Arbelos circle chains, honeycomb isoperimetry, Pappus's Hexagon Theorem, Steiner's configuration, and Blaise Pascal's *Hexagrammum Mysticum*.**

.. image:: docsrc/_static/constructions/pappus_hexagon.svg
   :alt: Pappus's Hexagon Theorem (Synagoge Book VII, Proposition 139)
   :align: center

Overview
--------

Compiled around **340 CE** in Alexandria, **Pappus's** eight-book *Synagoge* (*Collection*)
stands as the grand synthesis of classical and Hellenistic Greek geometry—bridging
Euclidean proportion, Archimedean mensuration, Apollonian conics, and Alexandrian mechanics
while planting the seeds of modern analytic and projective geometry:

- **Book III** classifies all geometric problems into *plane*, *solid*, and *linear* loci and
  exhibits the arithmetic, geometric, and harmonic means ($A \cdot H = G^2$) simultaneously
  inside a single semicircle;
- **Book IV** generalizes Euclid's Pythagorean Theorem (*Elements* I.47) to arbitrary outward
  parallelograms on any scalene triangle and proves the *ancient proposition* on the infinite
  *arbelos* circle chain ($y_n = n\,d_n$);
- **Book V** opens with the celebrated *Preface on the Sagacity of Bees*, proving that the
  regular hexagon uniquely maximizes honey capacity among congruent plane-tiling polygons of
  equal wax perimeter;
- **Book VII** (*Treasury of Analysis*) defines geometric *analysis* and *synthesis*,
  formulates the *n*-line locus and the **Pappus–Guldinus Centroid Rule**, and proves
  **Cross-Ratio Invariance** (Prop. 129) and **Pappus's Hexagon Theorem** (Props. 138–139)—
  generalized thirteen centuries later by **Blaise Pascal** (1640) to the **60-line
  *Hexagrammum Mysticum***;
- **Book VIII** develops center-of-gravity mechanics, the inclined plane, Archimedes's lever
  saying (*«δός μοι ποῦ στῶ καὶ κινῶ τὴν γῆν»*), Hero's *Baroulkos* gear-train, fixed-compass
  constructions, and the exact inscription of seven regular hexagons in a circle ($R = s_6\sqrt{7}$).

Built on `SymPy <https://www.sympy.org/>`_, ``geometor.model``, and ``geometor.divine``,
``geometor-pappus`` unites a **four-track Greek/English Book Codex** (``-en``, ``-el``,
``-summary``, ``-notes`` from Friedrich Hultsch's 1876–1878 Greek text with 100% original
GEOMETOR English translations) and **24 interactive vector diagrams** in **100% exact symbolic
algebra** over :math:`\mathbb{Q}`, :math:`\mathbb{Q}(\sqrt{3}, \sqrt{7})`, :math:`\mathbb{Q}(\phi)`,
and multi-variable polynomial rings.

.. image:: docsrc/_static/constructions/pappus_arbelos_chain.svg
   :alt: Pappus's Arbelos Tangent Circle Chain (Synagoge Book IV, Propositions 14–18)
   :align: center

Key Capabilities
----------------

- **Five-Unit Multi-Track *Synagoge* Book Codex** (``docsrc/synagoge/``): Synchronized
  original English translation (``-en``), diplomatic Hultsch polytonic Greek (``-el``),
  symbolic summary (``-summary``), and philological notes (``-notes``) across Books III, IV,
  V, VII, and VIII, complete with bidirectional ``geometor/euclid`` concordance, *Index
  Nominum*, bibliography, and Greek/Latin lexicon.
- **Exact Classical *Synagoge* Constructions** (:mod:`geometor.pappus.synagoge_demos`):
  Semicircle three means (:func:`~geometor.pappus.construct_three_means`), parallelogram area
  theorem and 10-variable proof (:func:`~geometor.pappus.construct_pappus_area_theorem`,
  :func:`~geometor.pappus.verify_pappus_area_symbolic`), rational *arbelos* circle chain
  (:func:`~geometor.pappus.construct_pappus_arbelos_chain`,
  :func:`~geometor.pappus.verify_arbelos_chain_symbolic`), and honeycomb isoperimetry + 7-cell
  rosette (:func:`~geometor.pappus.verify_honeycomb_isoperimetry`,
  :func:`~geometor.pappus.construct_honeycomb_isoperimetry`).
- **Pappus's Hexagon Theorem & Steiner's Six-Line Configuration** (*Book VII, Props. 138–139*):
  Exact DAG constructions for intersecting and parallel carriers, homologous type triangles,
  universal 8-symbol determinant proof (:func:`~geometor.pappus.verify_pappus_symbolic`), and
  all :math:`3! = 6` :math:`S_3` Pappus lines concurring by parity at Steiner Star points
  :math:`(S_+, S_-)`.
- **Pascal's *Hexagrammum Mysticum* (1640)**: Smooth-conic generalization across circles and
  ellipses, Veronese :math:`6 \times 6` coconicity, universal 6-parameter symbolic proof, and
  complete enumeration of all **15 chords, 45 diagonal points, 60 Pascal lines, 20 Steiner
  points, 60 Kirkman points, and 15 Plücker lines**.
- **Cross-Ratios, Harmonics & Golden Projectivity**: Collinear and Chasles conic cross-ratios,
  complete-quadrilateral fourth harmonic conjugates :math:`(A, B; C, D) = -1`, and emergent
  golden sections over :math:`\mathbb{Q}(\phi)` discovered via ``geometor.divine``.

Quickstart
----------

Python API
~~~~~~~~~~

.. code-block:: python

   from geometor.pappus import (
       construct_harmonic_fourth,
       construct_pappus_arbelos_chain,
       construct_pappus_area_theorem,
       construct_pappus_hexagon,
       construct_pascal_hexagon,
       construct_three_means,
       cross_ratio,
       verify_arbelos_chain_symbolic,
       verify_honeycomb_isoperimetry,
       verify_pappus_area_symbolic,
       verify_pappus_symbolic,
       verify_pascal_symbolic,
   )

   # 1. Synagoge Books III, IV, V & VIII Classical Theorems
   means = construct_three_means(9, 16)
   assert (means.arithmetic_mean * means.harmonic_mean) == means.geometric_mean**2
   assert means.harmonic_cross_ratio == -1

   area = construct_pappus_area_theorem(preset="scalene")
   assert area.area_residual == 0 and verify_pappus_area_symbolic() == 0

   arb = construct_pappus_arbelos_chain(2, 1, 4)
   assert [c.height_over_diameter for c in arb.chain] == [1, 2, 3, 4]
   assert all(v == 0 for v in verify_arbelos_chain_symbolic().values())

   hon = verify_honeycomb_isoperimetry(12)
   assert hon.tiling_polygons == (3, 4, 6)

   # 2. Synagoge VII.139 Hexagon Theorem & Pascal's Mystic Hexagram (1640)
   hex_res = construct_pappus_hexagon(preset="hexagon")
   pas_res = construct_pascal_hexagon(preset="hexagrammum")
   assert hex_res.is_collinear and pas_res.is_collinear
   assert verify_pappus_symbolic() == 0 and verify_pascal_symbolic() == 0

   # 3. Pure Straightedge Fourth Harmonic Conjugate
   h = construct_harmonic_fourth(pt_a=(0, 0), pt_b=(4, 0), pt_c=(4, 3))
   assert cross_ratio(h.pt_a, h.pt_b, h.pt_c, h.pt_d) == -1

Command-Line Interface
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Inspect Synagoge Books III, IV, V & VIII exact tables
   pappus synagoge

   # Inspect exact coordinates, Pappus lines, and Steiner Star points
   pappus inspect --preset steiner --all-permutations

   # Inspect Pascal's Hexagrammum Mysticum, bi-triangle Steiner pair, and full 60-line web
   pappus pascal --preset hexagrammum --steiner-family --full-60

   # Scan emergent collinear harmonic tetrads (P1, P3; P2, P4) = -1
   pappus harmonics --preset harmonic --discover-all

   # Regenerate all 24 interactive SVG figures (18 projective + 6 Synagoge)
   pappus build --synagoge -o docsrc/_static/constructions

Standalone Demonstrations (``demos/``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``demos/pappus_hexagon.py`` — *Synagoge* VII.138 & VII.139, homologous type triangles, symbolic determinant proof.
- ``demos/pappus_six_permutations.py`` — All 6 :math:`S_3` Pappus lines and the two Steiner Star points :math:`S_+, S_-`.
- ``demos/harmonic_conjugate.py`` — Straightedge complete quadrilateral fourth harmonic & 81 emergent harmonic tetrads.
- ``demos/golden_pappus.py`` — Golden cross-ratios in :math:`\mathbb{Q}(\phi)`, VII.129 perspectivity, and ``divine`` golden sections.
- ``demos/pascal_hexagrammum.py`` — Pascal's *Hexagrammum Mysticum* (1640), affine ellipse, full 60-line catalog, and golden conic ``/ M25 P4 P0 /``.
- ``demos/synagoge_three_means.py`` — *Synagoge* Book III: arithmetic, geometric, and harmonic means in a single semicircle.
- ``demos/pappus_area_theorem.py`` — *Synagoge* Book IV.1: parallelogram area generalization of *Elements* I.47.
- ``demos/arbelos_circle_chain.py`` — *Synagoge* Book IV.14–18: rational *arbelos* circle chain ($y_n = n\,d_n$).
- ``demos/honeycomb_isoperimetry.py`` — *Synagoge* Book V.1 & VIII.23: honeycomb isoperimetry & seven inscribed hexagons.

Links
-----

- **Documentation**: https://geometor.github.io/pappus
- **Source Repository**: https://github.com/geometor/pappus
- **Issues**: https://github.com/geometor/pappus/issues
