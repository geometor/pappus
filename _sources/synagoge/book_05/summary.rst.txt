:layout: book
:title: Book V · Analytical Summary & Invariant Audit
:order: 90

.. _synagoge-b5-summary:

========================================================================================
Book V · Summary & Exact Symbolic Audit (*Sagacity of Bees & Planar Isoperimetry*)
========================================================================================

.. rubric:: Structural Decomposition & Symbolic Verification

1. Planar Tessellation Constraints (*Ch. 2, Hultsch I p. 306*)
--------------------------------------------------------------

At any planar vertex where regular $n$-gons meet, the interior angle $\theta_n = \frac{n-2}{n} \times 180^\circ$ must divide $360^\circ$ evenly into an integer $k$:

.. math::

   k \cdot \left(\frac{n-2}{n}\right) \times 180^\circ = 360^\circ \iff (n-2)(k-2) = 4.

The only positive integer solutions are:

* $(n, k) = (3, 6)$: Six equilateral triangles ($6 \times 60^\circ = 360^\circ$).
* $(n, k) = (4, 4)$: Four squares ($4 \times 90^\circ = 360^\circ$).
* $(n, k) = (6, 3)$: Three regular hexagons ($3 \times 120^\circ = 360^\circ$).

2. Planar Isoperimetric Ordering (*Props. 1–10, Hultsch I pp. 308–336*)
-----------------------------------------------------------------------

Evaluated at equal perimeter $P = 12$ in :func:`geometor.pappus.verify_honeycomb_isoperimetry`:

* **Equilateral triangle** ($s_3 = 4$): Area $A_3 = 4\sqrt{3} \approx 6.9282$.
* **Square** ($s_4 = 3$): Area $A_4 = 9$.
* **Regular hexagon** ($s_6 = 2$): Area $A_6 = 6\sqrt{3} \approx 10.3923$.
* **Exact Ratios**:
  * $\frac{A_6}{A_3} = \frac{3}{2} = 1.5$ ($50\%$ greater than triangle).
  * $\frac{A_6}{A_4} = \frac{2\sqrt{3}}{3} \approx 1.1547$ ($15.47\%$ greater than square).
  * Area strictly increases with side count: $\text{triangle} < \text{square} < \text{hexagon} < \dots < \text{circle}$.
