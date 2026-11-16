:layout: book
:title: Book III · Analytical Summary & Invariant Audit
:order: 90

.. _synagoge-b3-summary:

===============================================================================
Book III · Summary & Exact Symbolic Audit (*Three Means & Problem Hierarchy*)
===============================================================================

.. rubric:: Structural Argument Map & ``geometor.pappus`` Symbolic Verification

1. Methodological Architecture (*Hultsch I, pp. 30–68*)
-------------------------------------------------------

* **Theorem vs. Problem**: A theorem demonstrates a necessary consequence of given hypotheses; a problem constructs a sought figure subject to a :term:`diorismos <diorismos>` specifying existence and multiplicity.
* **Threefold Classification of Loci**:
  1. **Plane** (*ἐπίπεδα*): straight lines and circles (*Elements* I–VI).
  2. **Solid** (*στερεά*): conic sections (*Apollonius Conics*; required for Delian two mean proportionals $a : x = x : y = y : b$ and angle trisection).
  3. **Linear** (*γραμμικά*): higher kinematic or locus curves (Archimedean spiral, quadratrix, Nicomedean conchoid, Dioclean cissoid).

2. Semicircle Synthesis of the Three Classical Means (*Hultsch I, pp. 68–84*)
-----------------------------------------------------------------------------

Given positive magnitudes $a = AD$ and $b = DC$ placed along diameter $AC = a + b$ of a semicircle with center $O$:

.. list-table::
   :header-rows: 1
   :widths: 22 24 26 28

   * - Mean (*Μεσότης*)
     - Semicircle Segment
     - Closed-Form Formula
     - Rational Preset $(9, 16)$ & Golden Preset $(1, \phi^2)$
   * - **Arithmetic** ($A$)
     - Radius $OB$
     - $A = \dfrac{a + b}{2}$
     - $A = \dfrac{25}{2} \quad \big| \quad A = \dfrac{\phi + 2}{2}$
   * - **Geometric** ($G$)
     - Perpendicular $DB$
     - $G = \sqrt{ab}$
     - $G = 12 \quad \big| \quad G = \phi$
   * - **Harmonic** ($H$)
     - Projection $BF$ on $OB$
     - $H = \dfrac{2ab}{a + b}$
     - $H = \dfrac{288}{25} \quad \big| \quad H = \dfrac{2\phi^2}{\phi + 2}$

3. Exact Invariants Verified in ``geometor.pappus``
---------------------------------------------------

Implemented in :func:`geometor.pappus.construct_three_means` (see ``demos/synagoge_three_means.py``):

* **Proportional Identity**: $A \cdot H = \left(\frac{a + b}{2}\right)\left(\frac{2ab}{a + b}\right) = ab = G^2$ — i.e., $G$ is the geometric mean between $A$ and $H$.
* **Geometric Ordering**: Nested right triangles $\triangle ODB$ and $\triangle DFB$ immediately yield $OB \ge DB \ge BF$, proving $A \ge G \ge H$ with equality iff $a = b$ ($D = O$).
* **Projective Harmonic Range**: Tangent $BT \perp OB$ meets $AC$ produced at $T = \left(-\frac{a(a+b)}{b - a}, 0\right)$ (for $a < b$ with $A$ at the origin), establishing the four-point harmonic cross-ratio $(A, C; D, T) = -1$.

Exact rational coordinates produced by ``construct_three_means(9, 16)``:

* $A = (0, 0)$, $D = (9, 0)$, $O = \left(\frac{25}{2}, 0\right)$, $C = (25, 0)$, $B = (9, 12)$, $F = \left(\frac{7641}{625}, \frac{588}{625}\right)$, $T = \left(-\frac{225}{7}, 0\right)$, satisfying $\operatorname{CR}(A, C; D, T) = -1$ identically.
