======
pappus
======

**Exact symbolic projective geometry investigations into Pappus of Alexandria's Hexagon Theorem, Blaise Pascal's Hexagrammum Mysticum, Steiner's six-line configuration, cross-ratios, harmonic conjugates, and golden perspectivities.**

.. image:: docsrc/_static/constructions/pappus_hexagon.svg
   :alt: Pappus's Hexagon Theorem (Synagoge Book VII, Proposition 139)
   :align: center

Overview
--------

Written in fourth-century Alexandria as Book VII (*Domain of Analysis*) of the
*Synagoge* (*Collection*), **Pappus's Hexagon Theorem** (Propositions 138 and 139)
is the foundational incidence theorem of projective geometry:

    If three points :math:`A_0, A_1, A_2` lie on a line :math:`a` and three points
    :math:`B_0, B_1, B_2` lie on a distinct line :math:`b`, then the three
    intersections of opposite hexagon cross-joins

    .. math::

       M_{01} = [A_0 B_1] \cap [A_1 B_0], \quad
       M_{12} = [A_1 B_2] \cap [A_2 B_1], \quad
       M_{20} = [A_2 B_0] \cap [A_0 B_2]

    are collinear along a **Pappus line**—constructed by straightedge incidence alone,
    with neither compass nor metric measurement.

Thirteen centuries later (February 1640), sixteen-year-old **Blaise Pascal** showed in his
*Essai pour les coniques* that Pappus's pair of lines is the degenerate case of any **conic
section**—giving rise to the **60-line *Hexagrammum Mysticum*** web of Steiner points, Kirkman
points, and Plücker lines.

Built on `SymPy <https://www.sympy.org/>`_, ``geometor.model``, and ``geometor.divine``,
``geometor-pappus`` preserves **100% exact algebraic precision** across rational
coordinates :math:`\mathbb{Q}`, quadratic extensions :math:`\mathbb{Q}(\phi)` where
:math:`\phi = \frac{1 + \sqrt{5}}{2}`, and multi-variable symbolic function fields.

.. image:: docsrc/_static/constructions/pascal_hexagrammum.svg
   :alt: Pascal's Hexagrammum Mysticum (1640) on the Unit Circle
   :align: center

Key Capabilities
----------------

- **Pappus's Hexagon Theorem (Book VII, Props. 138 & 139)**: Exact DAG constructions
  for both intersecting and parallel carrier lines, projective ideal-point handling
  when cross-joins are parallel, homologous ``square`` / ``circle`` / ``diamond``
  perspective triangles, and a universal eight-symbol algebraic proof
  (:func:`~geometor.pappus.verify_pappus_symbolic`).
- **The Six Permutations** (:math:`S_3`) **& Steiner's Two Star Points**: Permuting
  :math:`(B_0, B_1, B_2)` across all :math:`3! = 6` elements of :math:`S_3` produces
  18 cross-join meets and 6 Pappus lines that partition by parity into two 3-fold
  concurrent triples:

  - the 3 **even** Pappus lines (:math:`A_3`) concur at the even Star point :math:`S_+`, and
  - the 3 **odd** Pappus lines (:math:`S_3 \setminus A_3`) concur at the odd Star point :math:`S_-`.

- **Pascal's *Hexagrammum Mysticum* (1640)**: Smooth-conic generalization across circles
  and ellipses, Veronese :math:`6 \times 6` coconicity (:func:`~geometor.pappus.are_coconic`),
  universal 6-parameter symbolic proof (:func:`~geometor.pappus.verify_pascal_symbolic`),
  bi-triangle :math:`S_3` Steiner families, and complete projective enumeration of all
  **15 chords, 45 diagonal points, 60 Pascal lines, 20 Steiner points, 60 Kirkman points,
  and 15 Plücker lines** (:func:`~geometor.pappus.enumerate_hexagrammum_mysticum`).
- **Cross-Ratios & Straightedge Harmonic Conjugates**: Exact collinear cross-ratios
  :math:`(A, B; C, D)`, Michel Chasles's observer-independent conic cross-ratio
  :math:`(P_1, P_2; P_3, P_4)_{\mathcal{C}}`, central perspectivities (*Synagoge* VII.129),
  complete-quadrilateral fourth harmonic construction :math:`(A, B; C, D) = -1`, and
  automated scanning of emergent harmonic ranges.
- **Golden Projectivity**: Exact arithmetic in :math:`\mathbb{Q}(\phi)` demonstrating
  :math:`(0, 1; \phi, \phi + 1) = \phi`, the harmonic-golden identity
  :math:`(0, \phi; 1, \phi^3) = -1`, and emergent golden sections discovered by
  ``geometor.divine`` on both Pappus cross-joins (``/ A1 M12 B2 /``) and Pascal conic
  chords (``/ M25 P4 P0 /``).
- **Interactive SVG Rendering & CLI**: ``pappus`` CLI generating 18 light/dark-aware,
  step-interactive vector diagrams integrated with ``photon_platform.publish``.

Quickstart
----------

Python API
~~~~~~~~~~

.. code-block:: python

   from geometor.pappus import (
       construct_harmonic_fourth,
       construct_pappus_configuration,
       construct_pappus_hexagon,
       construct_pascal_hexagon,
       cross_ratio,
       enumerate_hexagrammum_mysticum,
       verify_pappus_symbolic,
       verify_pascal_symbolic,
   )

   # 1. Single Pappus Hexagon (Synagoge VII.139) & Pascal Mystic Hexagram (1640)
   hex_res = construct_pappus_hexagon(preset="hexagon")
   pas_res = construct_pascal_hexagon(preset="hexagrammum")
   assert hex_res.is_collinear and pas_res.is_collinear
   assert verify_pappus_symbolic() == 0 and verify_pascal_symbolic() == 0

   # 2. Full S_3 Six-Permutation Steiner Configuration & 60-Line Hexagrammum Web
   cfg = construct_pappus_configuration(preset="steiner")
   cat = enumerate_hexagrammum_mysticum(preset="hexagrammum")
   assert (len(cat.pascal_lines), len(cat.steiner_points), len(cat.kirkman_points)) == (60, 20, 60)

   # 3. Pure Straightedge Fourth Harmonic Conjugate
   h = construct_harmonic_fourth(pt_a=(0, 0), pt_b=(4, 0), pt_c=(4, 3))
   assert cross_ratio(h.pt_a, h.pt_b, h.pt_c, h.pt_d) == -1

Command-Line Interface
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Inspect exact coordinates, Pappus lines, and Steiner Star points
   pappus inspect --preset steiner --all-permutations

   # Inspect Pascal's Hexagrammum Mysticum, bi-triangle Steiner pair, and full 60-line web
   pappus pascal --preset hexagrammum --steiner-family --full-60

   # Scan emergent collinear harmonic tetrads (P1, P3; P2, P4) = -1
   pappus harmonics --preset harmonic --discover-all

   # Regenerate all 18 interactive SVG figures
   pappus build -o docsrc/_static/constructions

Standalone Demonstrations
~~~~~~~~~~~~~~~~~~~~~~~~~

- ``demos/pappus_hexagon.py`` — *Synagoge* VII.138 & VII.139, homologous type triangles, symbolic determinant proof.
- ``demos/pappus_six_permutations.py`` — All 6 :math:`S_3` Pappus lines and the two Steiner Star points :math:`S_+, S_-`.
- ``demos/harmonic_conjugate.py`` — Straightedge complete quadrilateral fourth harmonic & 81 emergent harmonic tetrads.
- ``demos/golden_pappus.py`` — Golden cross-ratios in :math:`\mathbb{Q}(\phi)`, VII.129 perspectivity, and ``divine`` golden sections.
- ``demos/pascal_hexagrammum.py`` — Pascal's *Hexagrammum Mysticum* (1640), affine ellipse, full 60-line catalog, and golden conic ``/ M25 P4 P0 /``.

Links
-----

- **Documentation**: https://geometor.github.io/pappus
- **Source Repository**: https://github.com/geometor/pappus
- **Issues**: https://github.com/geometor/pappus/issues
