:layout: book
:title: Book V · Analytical Summary & Invariant Audit
:order: 90
:folio: 0250

.. _synagoge-b5-summary:

Book V · Summary & Exact Symbolic Audit
=======================================

.. rubric:: Structural Decomposition & Symbolic Verification

.. folio:: 0250
   :page: 1238

1. Planar Tessellation Constraints (*Ch. 2, Hultsch I p. 306*)
--------------------------------------------------------------

At any planar vertex where regular $n$-gons meet, the interior angle $\theta_n = \frac{n-2}{n} \times 180^\circ$ divides $360^\circ$ evenly into an integer $k$:

.. math::

   k \cdot \left(\frac{n-2}{n}\right) \times 180^\circ = 360^\circ \iff (n-2)(k-2) = 4.

The only positive integer solutions are $(3, 6)$, $(4, 4)$, and $(6, 3)$.

2. Planar Isoperimetric Ordering (*Props. 1–10, Hultsch I pp. 308–336*)
-----------------------------------------------------------------------

Evaluated at equal perimeter $P = 12$ in :func:`geometor.pappus.verify_honeycomb_isoperimetry`:

* **Equilateral triangle** ($s_3 = 4$): Area $A_3 = 4\sqrt{3} \approx 6.9282$.
* **Square** ($s_4 = 3$): Area $A_4 = 9$.
* **Regular hexagon** ($s_6 = 2$): Area $A_6 = 6\sqrt{3} \approx 10.3923$.
* **Exact Ratios**: $\frac{A_6}{A_3} = \frac{3}{2} = 1.5$ and $\frac{A_6}{A_4} = \frac{2\sqrt{3}}{3} \approx 1.1547$.
