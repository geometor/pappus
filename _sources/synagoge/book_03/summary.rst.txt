:layout: book
:title: Book III · Analytical Summary & Invariant Audit
:order: 90
:folio: 0232

.. _synagoge-b3-summary:

Book III · Summary & Exact Symbolic Audit
=========================================

.. rubric:: Structural Argument Map & ``geometor.pappus`` Symbolic Verification

.. folio:: 0232
   :page: 1220

1. Methodological Architecture (*Hultsch I, pp. 30–68*)
-------------------------------------------------------

* **Theorem vs. Problem**: A theorem demonstrates a necessary consequence of given hypotheses; a problem constructs a sought figure subject to a :term:`diorismos <diorismos>` specifying existence and multiplicity.
* **Threefold Classification of Loci**:
  1. **Plane** (*ἐπίπεδα*): straight lines and circles (*Elements* I–VI).
  2. **Solid** (*στερεά*): conic sections (*Apollonius Conics*; required for Delian two mean proportionals :math:`a : x = x : y = y : b` and angle trisection).
  3. **Linear** (*γραμμικά*): higher kinematic or locus curves (Archimedean spiral, quadratrix, Nicomedean conchoid, Dioclean cissoid).

2. Semicircle Synthesis of the Three Classical Means (*Hultsch I, pp. 68–84*)
-----------------------------------------------------------------------------

Given positive magnitudes :math:`a = AD` and :math:`b = DC` placed along diameter :math:`AC = a + b` of a semicircle with center :math:`O`:

.. list-table::
   :header-rows: 1
   :widths: 22 24 26 28

   * - Mean (*Μεσότης*)
     - Semicircle Segment
     - Closed-Form Formula
     - Rational Preset :math:`(9, 16)` & Golden Preset :math:`(1, \phi^2)`
   * - **Arithmetic** (:math:`A`)
     - Radius :math:`OB`
     - :math:`A = \dfrac{a + b}{2}`
     - :math:`A = \dfrac{25}{2} \quad \big| \quad A = \dfrac{\phi + 2}{2}`
   * - **Geometric** (:math:`G`)
     - Perpendicular :math:`DB`
     - :math:`G = \sqrt{ab}`
     - :math:`G = 12 \quad \big| \quad G = \phi`
   * - **Harmonic** (:math:`H`)
     - Projection :math:`BF` on :math:`OB`
     - :math:`H = \dfrac{2ab}{a + b}`
     - :math:`H = \dfrac{288}{25} \quad \big| \quad H = \dfrac{2\phi^2}{\phi + 2}`

3. Exact Invariants Verified in ``geometor.pappus``
---------------------------------------------------

Implemented in :func:`geometor.pappus.construct_three_means` (see ``demos/synagoge_three_means.py``):

* **Proportional Identity**: :math:`A \cdot H = \left(\frac{a + b}{2}\right)\left(\frac{2ab}{a + b}\right) = ab = G^2` — i.e., :math:`G` is the geometric mean between :math:`A` and :math:`H`.
* **Geometric Ordering**: Nested right triangles :math:`\triangle ODB` and :math:`\triangle DFB` immediately yield :math:`OB \ge DB \ge BF`, proving :math:`A \ge G \ge H` with equality iff :math:`a = b` (:math:`D = O`).
* **Projective Harmonic Range**: Tangent :math:`BT \perp OB` meets :math:`AC` produced at :math:`T = \left(-\frac{a(a+b)}{b - a}, 0\right)` (for :math:`a < b` with :math:`A` at the origin), establishing the four-point harmonic cross-ratio :math:`(A, C; D, T) = -1`.

Exact rational coordinates produced by ``construct_three_means(9, 16)``:

* :math:`A = (0, 0)`, :math:`D = (9, 0)`, :math:`O = \left(\frac{25}{2}, 0\right)`, :math:`C = (25, 0)`, :math:`B = (9, 12)`, :math:`F = \left(\frac{7641}{625}, \frac{588}{625}\right)`, :math:`T = \left(-\frac{225}{7}, 0\right)`, satisfying :math:`\operatorname{CR}(A, C; D, T) = -1` identically.
