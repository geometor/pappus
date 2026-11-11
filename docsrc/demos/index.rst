:navigation: header
:order: 30

Demos
=====

Five standalone runnable scripts in ``demos/`` showcase every layer of ``geometor.pappus`` with
formatted Rich terminal tables—reviving and extending the repository's original 2023 ``pappus.py``
and ``pappus-3.py`` explorations without requiring a GUI window.

1. ``demos/pappus_hexagon.py`` — *Synagoge* VII.138 & VII.139
-------------------------------------------------------------

Constructs both the oblique intersecting-carrier hexagon (Prop. 139) and the parallel-carrier
hexagon (Prop. 138), verifies the universal 8-variable polynomial proof, and computes the exact
signed areas of the three homologous ``square`` / ``circle`` / ``diamond`` triangles.

.. code-block:: bash

   uv run python demos/pappus_hexagon.py

.. literalinclude:: ../../demos/pappus_hexagon.py
   :language: python

2. ``demos/pappus_six_permutations.py`` — Six $S_3$ Lines & Steiner Star Points
-------------------------------------------------------------------------------

Constructs all $3! = 6$ permutations on both ``preset="steiner"`` and the 2023 ``preset="parallel"``
configuration, printing every cross-join meet, Pappus line equation, and exact Star concurrency
point $(S_+, S_-)$.

.. code-block:: bash

   uv run python demos/pappus_six_permutations.py

.. literalinclude:: ../../demos/pappus_six_permutations.py
   :language: python

3. ``demos/harmonic_conjugate.py`` — Complete Quadrilateral & Harmonic Tetrads
------------------------------------------------------------------------------

Verifies Book VII Prop. 129 central perspectivity invariance, demonstrates straightedge fourth
harmonic construction across two distinct auxiliary apex/relay choices (confirming invariance of
$D = (-4, 0)$), and catalogs emergent harmonic tetrads on ``preset="harmonic"``.

.. code-block:: bash

   uv run python demos/harmonic_conjugate.py

.. literalinclude:: ../../demos/harmonic_conjugate.py
   :language: python

4. ``demos/golden_pappus.py`` — Golden Projectivity in $\mathbb{Q}(\phi)$
-------------------------------------------------------------------------

Computes the canonical golden cross-ratio $(0, 1; \phi, \phi + 1) = \phi$, its six-value
anharmonic power orbit, the harmonic-golden identity $(0, \phi; 1, \phi^3) = -1$, and runs
``geometor.divine`` to uncover the emergent golden section ``/ A1 M12 B2 /``.

.. code-block:: bash

   uv run python demos/golden_pappus.py

.. literalinclude:: ../../demos/golden_pappus.py
   :language: python

5. ``demos/pascal_hexagrammum.py`` — Pascal's *Hexagrammum Mysticum* (1640)
---------------------------------------------------------------------------

Proves Pascal's smooth-conic theorem universally over $\mathbb{Z}[t_0, \dots, t_5]$, compares
the Pythagorean unit circle and stretched affine ellipse $\frac{x^2}{4} + y^2 = 1$, enumerates all
**60 Pascal lines, 20 Steiner points, 60 Kirkman points, and 15 Plücker lines**, and uncovers the
emergent golden conic section ``/ M25 P4 P0 /`` in $\mathbb{Q}(\phi)$.

.. code-block:: bash

   uv run python demos/pascal_hexagrammum.py

.. literalinclude:: ../../demos/pascal_hexagrammum.py
   :language: python
