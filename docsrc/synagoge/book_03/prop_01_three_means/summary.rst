:layout: book
:type: book
:title: The Three Means · Symbolic Invariants & Algebraic Decomposition
:canonical_id: Syn. III.28-30.summary
:tracks: English: index | Greek: el | Summary: summary | Notes: notes

The Three Means · Symbolic Invariants & Algebraic Decomposition
===============================================================

.. rubric:: Structural Decomposition & Model Verification

1. Elements 2.0 Structural Decomposition
----------------------------------------

* **Given**: Two unequal straight line segments $AD = a$ and $DC = b$ ($a < b$) placed contiguously along a common diameter $AC = a + b$.
* **Construct**: Semicircle on diameter $AC$ centered at $O = \frac{a+b}{2}$; perpendicular $DB \perp AC$ meeting the semicircle at $B$; radius $OB$; perpendicular $DF \perp OB$ from $D$ onto $OB$ with foot $F$.
* **Demonstrate**:
  1. $OB = \frac{a+b}{2} = A$ (Arithmetic mean).
  2. $DB = \sqrt{ab} = G$ (Geometric mean, by *Elements* VI.8, VI.13).
  3. $BF = \frac{2ab}{a+b} = H$ (Harmonic mean, by similar triangles $\triangle OBD \sim \triangle DBF$).
  4. $A \cdot H = G^2 = ab$.
  5. $OB > DB > BF \iff A > G > H$.

2. SymPy Coordinates for Rational Preset $(9, 16)$
--------------------------------------------------

Constructed in :func:`geometor.pappus.construct_three_means`:

* $A = (0, 0)$
* $D = (9, 0)$
* $O = \left(\frac{25}{2}, 0\right)$
* $C = (25, 0)$
* $B = (9, 12)$
* $F = \left(\frac{7641}{625}, \frac{588}{625}\right)$
* $T = \left(-\frac{225}{7}, 0\right)$
* Cross-ratio: $\operatorname{CR}(A, C; D, T) = -1$
