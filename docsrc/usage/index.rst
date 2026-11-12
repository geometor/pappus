:navigation: header
:order: 20

Usage & CLI
===========

Installation
------------

Inside the ``geometor`` ``uv`` workspace (Python ``>=3.13``):

.. code-block:: bash

   uv sync
   uv run --no-sync pytest

Quickstart Python API
---------------------

*Synagoge* Classical Constructions (Books III, IV, V & VIII)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from geometor.pappus import (
       PHI,
       construct_pappus_arbelos_chain,
       construct_pappus_area_theorem,
       construct_three_means,
       verify_arbelos_chain_symbolic,
       verify_honeycomb_isoperimetry,
       verify_pappus_area_symbolic,
   )

   # Book III: Arithmetic, Geometric, and Harmonic Means in one semicircle
   means = construct_three_means(9, 16)
   print(means.arithmetic_mean, means.geometric_mean, means.harmonic_mean)  # 25/2, 12, 288/25
   print("Harmonic tangent CR (A, C; D, T):", means.harmonic_cross_ratio)   # -1
   print("Golden semicircle G on (1, phi^2):", construct_three_means(1, PHI**2).geometric_mean)

   # Book IV.1: Pappus's Parallelogram Area Theorem (13 + 15 = 28)
   area = construct_pappus_area_theorem(preset="scalene")
   print(area.area_ab, area.area_ac, area.area_bc, verify_pappus_area_symbolic())

   # Book IV.14-18: Infinite Arbelos tangent circle chain (y_n = n * d_n)
   arb = construct_pappus_arbelos_chain(2, 1, 4)
   print([(c.index, c.height, c.diameter, c.height_over_diameter) for c in arb.chain])
   print("Symbolic arbelos residuals:", verify_arbelos_chain_symbolic())

   # Book V.1 & Book VIII.23: Honeycomb isoperimetry & 7-hexagon circumradius R = s_6 * sqrt(7)
   hon = verify_honeycomb_isoperimetry(12, build_model=True)
   print("Tiling n-gons:", hon.tiling_polygons, "Areas:", hon.areas)
   print("7-hexagon radius:", hon.circumradius_seven_hexagons)  # 2*sqrt(7)

Constructing Pappus's Hexagon (*Synagoge* VII.139) & Universal Proof
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from geometor.pappus import construct_pappus_hexagon, verify_pappus_symbolic

   res = construct_pappus_hexagon(preset="hexagon", include_type_triangles=True)
   print("Meets:", [(m.x, m.y) for m in res.finite_meets])
   print("Pappus line:", res.pappus_line.equation(), "= 0")
   print("Symbolic 8-variable determinant:", verify_pappus_symbolic())  # 0

Six-Permutation Steiner Configuration ($S_3$)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from geometor.pappus import construct_pappus_configuration

   cfg = construct_pappus_configuration(preset="steiner", scan_harmonics=True)
   print("Even Star point S+:", (cfg.steiner_even.x, cfg.steiner_even.y))  # (80/39, 7/26)
   print("Odd Star point  S-:", (cfg.steiner_odd.x, cfg.steiner_odd.y))    # (5/3, -1/2)

Cross-Ratios, Complete Quadrilateral & Golden Sections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import sympy as sp
   from geometor.pappus import (
       PHI,
       construct_harmonic_fourth,
       construct_pappus_hexagon,
       cross_ratio,
       find_golden_sections,
   )

   # Straightedge fourth harmonic conjugate: (A, B; C, D) = -1
   quad = construct_harmonic_fourth()
   print("Fourth harmonic D:", (quad.d.x, quad.d.y), "CR =", quad.cross_ratio_value)

   # Golden chain & harmonic-golden identity in Q(phi)
   pts = [sp.Point(t, 0) for t in (0, 1, PHI, PHI + 1)]
   print("Golden CR:", cross_ratio(*pts))  # 1/2 + sqrt(5)/2

   gold = construct_pappus_hexagon(preset="golden")
   for gr in find_golden_sections(gold.model):
       print("Golden section:", gr.point_ids)

Pascal's *Hexagrammum Mysticum* & 60-Line Catalog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from geometor.pappus import (
       construct_pascal_hexagon,
       construct_pascal_steiner_family,
       enumerate_hexagrammum_mysticum,
       verify_pascal_symbolic,
   )

   pas = construct_pascal_hexagon(preset="hexagrammum")
   print("Pascal meets:", {k: (v.x, v.y) for k, v in pas.meets.items() if v is not None})
   print("Symbolic 6-variable determinant:", verify_pascal_symbolic())  # 0

   fam = construct_pascal_steiner_family(preset="hexagrammum")
   print("Bi-triangle Steiner G+, G-:", fam.steiner_even, fam.steiner_odd)

   cat = enumerate_hexagrammum_mysticum(preset="hexagrammum")
   print("60-line web:", len(cat.pascal_lines), len(cat.steiner_points), len(cat.kirkman_points))

Built-in Exact Presets
----------------------

.. list-table:: Canonical Two-Line Presets in ``geometor.pappus.PRESETS``
   :header-rows: 1
   :widths: 18 42 40

   * - Preset Key
     - Carrier Coordinates $(A_0, A_1, A_2)$ & $(B_0, B_1, B_2)$
     - Key Mathematical Highlight
   * - ``"hexagon"``
     - $[(0,0),(2,0),(5,0)]$ & $[(0,2),(2,3),(6,5)]$
     - *Synagoge* VII.139; $O=(-4,0)$, spread $s(a,b)=1/5$
   * - ``"parallel"``
     - $[(0,0),(1,0),(3,0)]$ & $[(0,1),(3/2,1),(5/2,1)]$
     - *Synagoge* VII.138; 2023 GEOMETOR $S_+ = (90/73, 38/73)$
   * - ``"steiner"``
     - $[(1,0),(2,0),(3,0)]$ & $[(0,2),(3,1),(5,1/3)]$
     - Compact $S_3$ Star points $S_+=(80/39, 7/26)$, $S_-=(5/3, -1/2)$
   * - ``"harmonic"``
     - $[(1,0),(2,0),(3,0)]$ & $[(0,1),(1,3/2),(4,3)]$
     - 19 base / 81 full collinear harmonic tetrads
   * - ``"golden"``
     - $[(0,0),(1,0),(\phi,0)]$ & $[(0,1),(\phi,\frac{\phi}{2}+1),(\phi+1,\frac{\phi+3}{2})]$
     - Emergent golden section ``/ A1 M12 B2 /`` in $\mathbb{Q}(\phi)$

.. list-table:: Smooth-Conic Presets in ``geometor.pappus.PASCAL_PRESETS``
   :header-rows: 1
   :widths: 18 42 40

   * - Preset Key
     - Carrier Conic & Stereographic Seed
     - Key Mathematical Highlight
   * - ``"hexagrammum"``
     - $x^2 + y^2 = 1$ with $t = (0, \tfrac{1}{3}, 1, 3, -2, -\tfrac{1}{2})$
     - Mystic star cycle $(0,2,4,1,3,5)$; all 60 Pascal lines & 20 Steiner pts distinct
   * - ``"convex"``
     - $x^2 + y^2 = 1$ with $t = (-3, -\tfrac{1}{2}, -\tfrac{1}{3}, 0, \tfrac{1}{4}, \tfrac{1}{3})$
     - Strictly convex cyclic hexagon with compact rational exterior meets
   * - ``"ellipse"``
     - $\frac{x^2}{4} + y^2 = 1$ via $(x, y) \mapsto (2x, y)$
     - Projective conic invariance on a non-circular ellipse
   * - ``"golden_conic"``
     - $x^2 + y^2 = 1$ with $t = (0, 1, \phi, \phi+1, -1, -\phi)$
     - Chasles conic CR $= \phi$; emergent section ``/ M25 P4 P0 /``

Command-Line Interface (``pappus``)
-----------------------------------

``geometor-pappus`` installs the ``pappus`` console entry point with Rich tabular output:

.. code-block:: bash

   # Build all 24 interactive SVG figures (18 projective + 6 Synagoge Books III-V & VIII)
   pappus build --synagoge

   # Inspect Synagoge Books III, IV, V & VIII exact tables (or filter: means, area, arbelos, honeycomb)
   pappus synagoge
   pappus synagoge --demo arbelos

   # Inspect single-hexagon meets, quadrances, spreads, and 8-symbol determinant
   pappus inspect --preset hexagon

   # Inspect all 6 S_3 Pappus lines and Steiner Star points (S+, S-)
   pappus inspect --preset steiner --all-permutations

   # Inspect Pascal's Hexagrammum Mysticum, bi-triangle Steiner pair, and full 60-line web
   pappus pascal --preset hexagrammum --steiner-family --full-60
   pappus pascal --preset golden_conic

   # Scan a configuration for emergent harmonic tetrads and golden sections
   pappus harmonics --preset harmonic --discover-all
   pappus harmonics --preset golden
