:navigation: header
:order: 20

Usage & CLI
===========

Installation
------------

Inside the ``geometor`` ``uv`` workspace (Python ``>=3.13``):

.. code-block:: bash

   uv sync
   uv run pytest

Quickstart Python API
---------------------

Constructing Pappus's Hexagon (*Synagoge* VII.139) & Universal Proof
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from geometor.pappus import construct_pappus_hexagon, verify_pappus_symbolic

   res = construct_pappus_hexagon(preset="hexagon", include_triangles=True)
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

   # Build all 18 interactive SVG figures into docsrc/_static/constructions/
   uv run pappus build

   # Inspect single-hexagon meets, quadrances, spreads, and 8-symbol determinant
   uv run pappus inspect --preset hexagon

   # Inspect all 6 S_3 Pappus lines and Steiner Star points (S+, S-)
   uv run pappus inspect --preset steiner --all-permutations

   # Inspect Pascal's Hexagrammum Mysticum, bi-triangle Steiner pair, and full 60-line web
   uv run pappus pascal --preset hexagrammum --steiner-family --full-60
   uv run pappus pascal --preset golden_conic

   # Scan a configuration for emergent harmonic tetrads and golden sections
   uv run pappus harmonics --preset harmonic --discover-all
   uv run pappus harmonics --preset golden
