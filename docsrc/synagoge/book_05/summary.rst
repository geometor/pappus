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

At any planar vertex where regular :math:`n`-gons meet, the interior angle :math:`\theta_n = \frac{n-2}{n} \times 180^\circ` divides :math:`360^\circ` evenly into an integer :math:`k`:

.. math::

   k \cdot \left(\frac{n-2}{n}\right) \times 180^\circ = 360^\circ \iff (n-2)(k-2) = 4.

The only positive integer solutions are :math:`(3, 6)`, :math:`(4, 4)`, and :math:`(6, 3)`.

2. Planar Isoperimetric Ordering (*Props. 1–10, Hultsch I pp. 308–336*)
-----------------------------------------------------------------------

Evaluated at equal perimeter :math:`P = 12` in :func:`geometor.pappus.verify_honeycomb_isoperimetry`:

* **Equilateral triangle** (:math:`s_3 = 4`): Area :math:`A_3 = 4\sqrt{3} \approx 6.9282`.
* **Square** (:math:`s_4 = 3`): Area :math:`A_4 = 9`.
* **Regular hexagon** (:math:`s_6 = 2`): Area :math:`A_6 = 6\sqrt{3} \approx 10.3923`.
* **Exact Ratios**: :math:`\frac{A_6}{A_3} = \frac{3}{2} = 1.5` and :math:`\frac{A_6}{A_4} = \frac{2\sqrt{3}}{3} \approx 1.1547`.
