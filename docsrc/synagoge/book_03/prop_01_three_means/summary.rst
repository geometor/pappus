:order: 5
:layout: book
:type: book
:title: The Three Means · Symbolic Invariants & Algebraic Decomposition
:canonical_id: Syn. III.28-30.summary
:folio: hultsch_1876_vol1:0115
:tracks: English: index | Greek: el | Summary: summary | Notes: notes

The Three Means · Symbolic Invariants & Algebraic Decomposition
===============================================================

.. rubric:: Structural Decomposition & Model Verification

.. folio:: hultsch_1876_vol1:0115
   :page: 82

1. Elements 2.0 Structural Decomposition
----------------------------------------

* **Given**: Two unequal straight line segments :math:`AD = a` and :math:`DC = b` (:math:`a < b`) placed contiguously along a common diameter :math:`AC = a + b`.
* **Construct**: Semicircle on diameter :math:`AC` centered at :math:`O = \frac{a+b}{2}`; perpendicular :math:`DB \perp AC` meeting the semicircle at :math:`B`; radius :math:`OB`; perpendicular :math:`DF \perp OB` from :math:`D` onto :math:`OB` with foot :math:`F`.
* **Demonstrate**:
  1. :math:`OB = \frac{a+b}{2} = A` (Arithmetic mean).
  2. :math:`DB = \sqrt{ab} = G` (Geometric mean, by *Elements* VI.8, VI.13).
  3. :math:`BF = \frac{2ab}{a+b} = H` (Harmonic mean, by similar triangles :math:`\triangle OBD \sim \triangle DBF`).
  4. :math:`A \cdot H = G^2 = ab`.
  5. :math:`OB > DB > BF \iff A > G > H`.

2. SymPy Coordinates for Rational Preset (9, 16)
------------------------------------------------

Constructed in :func:`geometor.pappus.construct_three_means`:

* :math:`A = (0, 0)`, :math:`D = (9, 0)`, :math:`O = \left(\frac{25}{2}, 0\right)`, :math:`C = (25, 0)`, :math:`B = (9, 12)`, :math:`F = \left(\frac{7641}{625}, \frac{588}{625}\right)`, :math:`T = \left(-\frac{225}{7}, 0\right)`
* Cross-ratio: :math:`\operatorname{CR}(A, C; D, T) = -1`
