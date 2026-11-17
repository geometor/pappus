:order: 25
:nav_title: Demos

Demos
=====

Nine standalone runnable scripts in ``demos/`` showcase every layer of ``geometor.pappus``—spanning
both the projective Pappus–Steiner–Pascal canon and Books III, IV, V, and VIII of the *Synagoge*—with
formatted Rich terminal tables and 100% exact SymPy coordinates.

1. ``demos/pappus_hexagon.py`` — *Synagoge* VII.138 & VII.139
-------------------------------------------------------------

Constructs both the oblique intersecting-carrier hexagon (Prop. 139) and the parallel-carrier
hexagon (Prop. 138), verifies the universal 8-variable polynomial proof, and computes the exact
signed areas of the three homologous ``square`` / ``circle`` / ``diamond`` triangles.

.. code-block:: bash

   uv run --no-sync python demos/pappus_hexagon.py

.. literalinclude:: ../../demos/pappus_hexagon.py
   :language: python

2. ``demos/pappus_six_permutations.py`` — Six $S_3$ Lines & Steiner Star Points
-------------------------------------------------------------------------------

Constructs all $3! = 6$ permutations on both ``preset="steiner"`` and the 2023 ``preset="parallel"``
configuration, printing every cross-join meet, Pappus line equation, and exact Star concurrency
point $(S_+, S_-)$.

.. code-block:: bash

   uv run --no-sync python demos/pappus_six_permutations.py

.. literalinclude:: ../../demos/pappus_six_permutations.py
   :language: python

3. ``demos/harmonic_conjugate.py`` — Complete Quadrilateral & Harmonic Tetrads
------------------------------------------------------------------------------

Verifies Book VII Prop. 129 central perspectivity invariance, demonstrates straightedge fourth
harmonic construction across two distinct auxiliary apex/relay choices (confirming invariance of
$D = (-4, 0)$), and catalogs emergent harmonic tetrads on ``preset="harmonic"``.

.. code-block:: bash

   uv run --no-sync python demos/harmonic_conjugate.py

.. literalinclude:: ../../demos/harmonic_conjugate.py
   :language: python

4. ``demos/golden_pappus.py`` — Golden Projectivity in $\mathbb{Q}(\phi)$
-------------------------------------------------------------------------

Computes the canonical golden cross-ratio $(0, 1; \phi, \phi + 1) = \phi$, its six-value
anharmonic power orbit, the harmonic-golden identity $(0, \phi; 1, \phi^3) = -1$, and runs
``geometor.divine`` to uncover the emergent golden section ``/ A1 M12 B2 /``.

.. code-block:: bash

   uv run --no-sync python demos/golden_pappus.py

.. literalinclude:: ../../demos/golden_pappus.py
   :language: python

5. ``demos/pascal_hexagrammum.py`` — Pascal's *Hexagrammum Mysticum* (1640)
---------------------------------------------------------------------------

Proves Pascal's smooth-conic theorem universally over $\mathbb{Z}[t_0, \dots, t_5]$, compares
the Pythagorean unit circle and stretched affine ellipse $\frac{x^2}{4} + y^2 = 1$, enumerates all
**60 Pascal lines, 20 Steiner points, 60 Kirkman points, and 15 Plücker lines**, and uncovers the
emergent golden conic section ``/ M25 P4 P0 /`` in $\mathbb{Q}(\phi)$.

.. code-block:: bash

   uv run --no-sync python demos/pascal_hexagrammum.py

.. literalinclude:: ../../demos/pascal_hexagrammum.py
   :language: python

6. ``demos/synagoge_three_means.py`` — *Synagoge* Book III: Three Means in One Semicircle
-----------------------------------------------------------------------------------------

Constructs Pappus's semicircle diagram (*Hultsch I, pp. 68–84*) on rational $(9, 16)$, Pythagorean
$(4, 9)$, and golden $(1, \phi^2)$ segments, verifying $A \cdot H = G^2$, $A > G > H$, and the
external harmonic tangent relation $(A, C; D, T) = -1$.

.. code-block:: bash

   uv run --no-sync python demos/synagoge_three_means.py

.. literalinclude:: ../../demos/synagoge_three_means.py
   :language: python

7. ``demos/pappus_area_theorem.py`` — *Synagoge* Book IV.1: Parallelogram Area Theorem
--------------------------------------------------------------------------------------

Demonstrates Pappus's equiaffine generalization of *Elements* I.47 (*Hultsch I, pp. 176–179*) on an
oblique scalene triangle ($13 + 15 = 28$), on the $3$-$4$-$5$ right triangle ($9 + 16 = 25$), and
universally over $\mathbb{Z}[x_A, y_A, x_B, y_B, x_C, y_C, u_x, u_y, v_x, v_y]$.

.. code-block:: bash

   uv run --no-sync python demos/pappus_area_theorem.py

.. literalinclude:: ../../demos/pappus_area_theorem.py
   :language: python

8. ``demos/arbelos_circle_chain.py`` — *Synagoge* Book IV.14–18: Arbelos Circle Chain
-------------------------------------------------------------------------------------

Constructs the infinite tangent circle chain $C_1, \dots, C_5$ inside the *arbelos* (*Hultsch I,
pp. 208–232*) in 100% exact rational coordinates and verifies both pairwise tangency quadrances and
Pappus's altitude law $y_n = n\,d_n = 2n\,r_n$.

.. code-block:: bash

   uv run --no-sync python demos/arbelos_circle_chain.py

.. literalinclude:: ../../demos/arbelos_circle_chain.py
   :language: python

9. ``demos/honeycomb_isoperimetry.py`` — *Synagoge* Book V.1 & VIII.23: Honeycomb & 7 Hexagons
----------------------------------------------------------------------------------------------

Proves that $n \in \{3, 4, 6\}$ are the unique regular plane-tiling polygons (*Hultsch I,
pp. 304–312*), evaluates exact symbolic areas at equal perimeter $P = 12$, and verifies the exact
circumradius $R = s_6\sqrt{7}$ of Book VIII Proposition 23's seven-hexagon circle inscription.

.. code-block:: bash

   uv run --no-sync python demos/honeycomb_isoperimetry.py

.. literalinclude:: ../../demos/honeycomb_isoperimetry.py
   :language: python
