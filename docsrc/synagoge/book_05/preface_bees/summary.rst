:layout: book
:type: book
:title: Preface on Bees · Tessellation Invariants & Mathematical Summary
:canonical_id: Syn. V.preface.summary
:tracks: English: index | Greek: el | Summary: summary | Notes: notes

Preface on Bees · Tessellation Invariants & Mathematical Summary
================================================================

.. rubric:: Vertex Angle Diophantine Analysis

For regular polygons of $n$ sides to tile the plane around a common vertex, the sum of their interior angles must equal $360^\circ$:

.. math::

   k \times \frac{(n-2) \times 180^\circ}{n} = 360^\circ \iff \frac{1}{n} + \frac{1}{k} = \frac{1}{2}.

Solving for integer pairs $(n, k)$ with $n \ge 3$ and $k \ge 3$:

* **$n = 3$ (Equilateral triangle)**: Angle $60^\circ$; $k = 6$ triangles meet per vertex.
* **$n = 4$ (Square)**: Angle $90^\circ$; $k = 4$ squares meet per vertex.
* **$n = 6$ (Regular hexagon)**: Angle $120^\circ$; $k = 3$ hexagons meet per vertex.

For $n = 5$ (pentagon), angle is $108^\circ$: $3 \times 108^\circ = 324^\circ < 360^\circ$ and $4 \times 108^\circ = 432^\circ > 360^\circ$, rendering planar tiling impossible. For any $n \ge 7$, interior angle exceeds $128.57^\circ$, so $3$ polygons exceed $360^\circ$.
