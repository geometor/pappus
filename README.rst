======
pappus
======

**Exact symbolic projective geometry investigations into Pappus of Alexandria's Hexagon Theorem, Steiner's six-line configuration, cross-ratios, harmonic conjugates, and golden perspectivities.**

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

Built on `SymPy <https://www.sympy.org/>`_, ``geometor.model``, and ``geometor.divine``,
``geometor-pappus`` preserves **100% exact algebraic precision** across rational
coordinates :math:`\mathbb{Q}`, quadratic extensions :math:`\mathbb{Q}(\phi)` where
:math:`\phi = \frac{1 + \sqrt{5}}{2}`, and eight-variable symbolic function fields.

.. image:: docsrc/_static/constructions/pappus_steiner.svg
   :alt: The Six S_3 Pappus Lines and Two Steiner Star Points (S+ and S-)
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

- **Cross-Ratios & Straightedge Harmonic Conjugates**: Exact collinear cross-ratios
  :math:`(A, B; C, D)`, central perspectivities (*Synagoge* VII.129), complete-quadrilateral
  fourth harmonic construction :math:`(A, B; C, D) = -1`, and automated scanning of
  emergent harmonic ranges across projective configurations.
- **Golden Projectivity**: Exact arithmetic in :math:`\mathbb{Q}(\phi)` demonstrating
  :math:`(0, 1; \phi, \phi + 1) = \phi`, the harmonic-golden identity
  :math:`(0, \phi; 1, \phi^3) = -1`, and emergent golden sections discovered by
  ``geometor.divine`` along Pappus cross-joins.
- **Interactive SVG Rendering & CLI**: ``pappus`` CLI generating light/dark-aware,
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
       cross_ratio,
       verify_pappus_symbolic,
   )

   # 1. Single Pappus Hexagon (Synagoge VII.139)
   hex_res = construct_pappus_hexagon(preset="hexagon")
   assert hex_res.is_collinear
   assert verify_pappus_symbolic() == 0

   # 2. Full S_3 Six-Permutation Steiner Configuration
   cfg = construct_pappus_configuration(preset="steiner")
   print("Even Steiner Star S+:", cfg.steiner_even)  # Point2D(80/39, 7/26)
   print("Odd Steiner Star  S-:", cfg.steiner_odd)   # Point2D(5/3, -1/2)

   # 3. Pure Straightedge Fourth Harmonic Conjugate
   h = construct_harmonic_fourth(pt_a=(0, 0), pt_b=(4, 0), pt_c=(4, 3))  # or exact Rational
   assert cross_ratio(h.pt_a, h.pt_b, h.pt_c, h.pt_d) == -1

Command-Line Interface
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Inspect exact coordinates, Pappus lines, and Steiner Star points
   pappus inspect --preset steiner --all-permutations

   # Scan emergent collinear harmonic tetrads (P1, P3; P2, P4) = -1
   pappus harmonics --preset harmonic --discover-all

   # Regenerate all 14 interactive SVG figures
   pappus build -o docsrc/_static/constructions

Standalone Demonstrations
~~~~~~~~~~~~~~~~~~~~~~~~~

- ``demos/pappus_hexagon.py`` — *Synagoge* VII.138 & VII.139, homologous type triangles, symbolic determinant proof.
- ``demos/pappus_six_permutations.py`` — All 6 :math:`S_3` Pappus lines and the two Steiner Star points :math:`S_+, S_-`.
- ``demos/harmonic_conjugate.py`` — Straightedge complete quadrilateral fourth harmonic & 81 emergent harmonic tetrads.
- ``demos/golden_pappus.py`` — Golden cross-ratios in :math:`\mathbb{Q}(\phi)`, VII.129 perspectivity, and ``divine`` golden sections.

Links
-----

- **Documentation**: https://geometor.github.io/pappus
- **Source Repository**: https://github.com/geometor/pappus
- **Issues**: https://github.com/geometor/pappus/issues
