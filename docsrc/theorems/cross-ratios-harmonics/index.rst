:type: theorem
:order: 4
:summary: Exact SymPy cross-ratios, Book VII Prop. 129 invariance, straightedge fourth-harmonic construction, emergent harmonic tetrads, and Golden Ratio projectivities in Q(phi).

Cross-Ratios, Harmonic Conjugates & Golden Projectivity
=======================================================

Why does a purely straightedge construction preserve quantitative algebraic ratios when
distances themselves are distorted by perspective projection? The answer already appears in
**Proposition 129 of Book VII** of Pappus's *Synagoge*: while lengths and simple ratios change
under central projection from an apex :math:`O`, the **compound ratio of ratios**—today called the
**projective cross-ratio**—is an **exact projective invariant**.

The Projective Cross-Ratio & Its Anharmonic Orbit
-------------------------------------------------

For four distinct collinear points :math:`A, B, C, D` parameterized along their carrier line by affine
coordinates :math:`t_A, t_B, t_C, t_D` (including :math:`t = \infty` for an ideal point), the cross-ratio is

.. math::

   (A, B; C, D) = \frac{(t_A - t_C)(t_B - t_D)}{(t_A - t_D)(t_B - t_C)}.

In ``geometor.pappus.projective.cross_ratio``, :math:`A, B, C, D` are verified strictly collinear and
projected onto whichever coordinate axis (:math:`x` or :math:`y`) varies, returning an exact simplified SymPy
expression with zero floating-point approximation.

Permuting four collinear points across all :math:`4! = 24` orderings preserves :math:`(A, B; C, D)` on the
Klein four-group :math:`V_4 = \{\mathrm{id}, (AB)(CD), (AC)(BD), (AD)(BC)\}`, leaving at most
:math:`24 / 4 = 6` values—the **anharmonic six-group orbit**:

.. math::

   \left\{\lambda,\; \frac{1}{\lambda},\; 1 - \lambda,\; \frac{1}{1 - \lambda},\;
   \frac{\lambda - 1}{\lambda},\; \frac{\lambda}{\lambda - 1}\right\}.

Straightedge Fourth Harmonic Conjugate (Complete Quadrilateral)
---------------------------------------------------------------

The most symmetrical cross-ratio occurs when this six-value orbit collapses to three values
:math:`\{-1,\, 2,\, \frac{1}{2}\}`:

.. math::

   (A, B; C, D) = -1 \quad \Longleftrightarrow \quad \frac{AC}{CB} = -\frac{AD}{DB}.

Here :math:`C` and :math:`D` separate :math:`A` and :math:`B` internally and externally in the **same magnitude ratio**—a
**harmonic range** (*Synagoge* VII.131). Remarkably, given three collinear points :math:`A, B, C`, the
fourth harmonic conjugate :math:`D` can be constructed **using a straightedge alone** via a **complete
quadrilateral**, and :math:`D` is completely independent of the auxiliary points chosen!

.. picture:: /_static/constructions/harmonic_fourth.svg
   :alt: Complete Quadrilateral Straightedge Construction of Fourth Harmonic D

.. step::

   Begin with three collinear points :g:`A <g1:A>` :math:`= (0, 0)`, :g:`B <g1:B>` :math:`= (4, 0)`, and
   internal division point :g:`C <g1:C>` :math:`= \left(\frac{4}{3}, 0\right)` on carrier
   :g:`AB <g1:[ A B ]>`.

.. step::

   Pick any off-line apex :g:`P <g1:P>` :math:`= (2, 2)`, draw rays :g:`PA <g1:[ P A ]>`,
   :g:`PB <g1:[ P B ]>`, and diagonal :g:`PC <g1:[ P C ]>`, and choose any relay point
   :g:`Q <g1:Q>` :math:`= \left(\frac{5}{3}, 1\right)` on :g:`PC <g1:[ P C ]>`.

.. step::

   Draw cross-joins :g:`AQ <g1:[ A Q ]>` meeting :g:`PB <g1:[ P B ]>` at
   :g:`R <g1:R>` :math:`= \left(\frac{5}{2}, \frac{3}{2}\right)`, and :g:`BQ <g1:[ B Q ]>` meeting
   :g:`PA <g1:[ P A ]>` at :g:`S <g1:S>` :math:`= \left(\frac{6}{5}, \frac{6}{5}\right)`.

.. step::

   Draw the second diagonal :g:`RS <g1:[ R S ]>` (:math:`3x - 13y + 12 = 0`): it cuts the base line
   :g:`AB <g1:[ A B ]>` at the exact fourth harmonic conjugate :g:`D <g1:D>` :math:`= (-4, 0)`, giving
   :math:`(A, B; C, D) = \frac{(0 - 4/3)(4 - (-4))}{(0 - (-4))(4 - 4/3)} = \frac{-32/3}{32/3} = -1`.

Emergent Harmonic Tetrads in the Pappus–Steiner Web
---------------------------------------------------

Because every complete quadrilateral embedded in a projective configuration generates harmonic
divisions along its diagonals and sides, the Pappus–Steiner 9-line / 6-line web teems with
emergent harmonic ranges. Running ``find_harmonic_ranges`` on ``preset="harmonic"``
(:math:`A = [(1,0), (2,0), (3,0)]` on :math:`y = 0` and :math:`B = [(0,1), (1, \frac{3}{2}), (4, 3)]` on
:math:`-x + 2y = 2`, meeting at :math:`O = (-2, 0)`) uncovers **19 exact collinear harmonic tetrads** among
the given, cross-join, and Steiner points alone—and **81 exact collinear harmonic tetrads** when
pairwise line intersections are included!

.. list-table:: Representative Exact Harmonic Tetrads in ``preset="harmonic"``
   :header-rows: 1
   :widths: 26 30 44

   * - Carrier Line
     - Collinear Harmonic Tetrad
     - Exact Coordinates & Verification
   * - Carrier :math:`b`: :math:`-x + 2y = 2`
     - :math:`(O,\, B_1;\, B_0,\, B_2)`
     - :math:`x = (-2, 1; 0, 4) \implies (O, B_0, B_1, B_2)` has :math:`(O, B_1; B_0, B_2) = -1`
   * - Carrier :math:`a`: :math:`y = 0`
     - :math:`(A_0,\, A_1;\, X_1,\, A_2)`
     - :math:`x = (1, 2; \tfrac{5}{3}, 3) \implies \frac{(1 - 5/3)(2 - 3)}{(1 - 3)(2 - 5/3)} = -1`
   * - Carrier :math:`a`: :math:`y = 0`
     - :math:`(A_0,\, A_2;\, A_1,\, X_2)`
     - :math:`x = (1, 3; 2, \tfrac{7}{3})` cut by the Steiner line through :math:`S_+ = (\tfrac{31}{18}, \tfrac{1}{2})`
   * - Cross-Line :math:`[A_0 B_0]`
     - :math:`(B_0,\, A_0;\, M_{0021},\, M_{0022})`
     - Exact harmonic conjugate cross-join pair cut across :math:`[A_0 B_0]`

.. picture:: /_static/constructions/pappus_harmonics.svg
   :alt: Emergent Harmonic Ranges in the Pappus-Steiner Configuration

Golden Projectivity in :math:`\mathbb{Q}(\phi)`
-----------------------------------------------

At the heart of the GEOMETOR initiative lies the **Golden Ratio**
:math:`\phi = \frac{1 + \sqrt{5}}{2}` (:math:`\phi^2 = \phi + 1`). Projective cross-ratios unite harmonic
division and the divine proportion in three exact algebraic laws verified symbolically in
``geometor.pappus``:

1. **Canonical Golden Chain**: Four consecutive Fibonacci-scaled points :math:`(0, 1, \phi, \phi + 1)`
   have exact cross-ratio

   .. math::

      (0, 1;\, \phi, \phi + 1) = \frac{(0 - \phi)(1 - \phi - 1)}{(0 - \phi - 1)(1 - \phi)}
      = \frac{\phi^2}{\phi^2 \cdot \phi^{-1}} = \phi,

   whose six-value anharmonic orbit is purely powers of :math:`\phi`:
   :math:`\left\{\phi,\; \phi^{-1},\; -\phi^{-1},\; -\phi,\; \phi^{-2},\; \phi^2\right\}`.
2. **Harmonic–Golden Bridge**: The fourth harmonic conjugate of :math:`1` with respect to :math:`(0, \phi)`
   is **precisely** :math:`\phi^3 = 2\phi + 1`:

   .. math::

      (0, \phi;\, 1, \phi^3) = \frac{(0 - 1)(\phi - \phi^3)}{(0 - \phi^3)(\phi - 1)}
      = \frac{\phi(\phi^2 - 1)}{\phi^3 \phi^{-1}} = -\frac{\phi^2}{\phi^2} = -1.

3. **Emergent Golden Section in the Golden Pappus Hexagon**: In ``preset="golden"``, carrier :math:`a`
   places :math:`(A_0, A_1, A_2) = \bigl((0, 0),\, (1, 0),\, (\phi, 0)\bigr)` in golden section along
   :math:`y = 0`, while carrier :math:`b` places
   :math:`B_0 = (0, 1)`, :math:`B_1 = \left(\phi, \frac{\phi}{2} + 1\right)`,
   :math:`B_2 = \left(\phi + 1, \frac{\phi + 3}{2}\right)` in golden section along
   :math:`-(\phi + 1)x + (2\phi + 2)y = 2\phi + 2`, intersecting :math:`a` at :math:`O = (-2, 0)`.

   Computing the exact cross-join meets in :math:`\mathbb{Q}(\sqrt{5})` yields

   .. math::

      M_{01} = (-4 + 2\sqrt{5},\; 5 - 2\sqrt{5}), \quad
      M_{12} = \left(\frac{1 + \sqrt{5}}{2},\; 2 - \frac{\sqrt{5}}{2}\right), \quad
      M_{20} = \left(\frac{2}{3},\; \frac{4 - \sqrt{5}}{3}\right).

   Scanning this model with ``geometor.divine`` uncovers an **emergent third golden section**:
   the cross-join intersection :math:`M_{12}` divides the oblique hexagon side :math:`[A_1 B_2]` in the
   **exact Golden Ratio** :math:`\phi`!

.. picture:: /_static/constructions/golden_pappus.svg
   :alt: Golden Ratio Projectivity in Pappus's Hexagon over Q(phi)

.. step::

   Place golden-section triples :g:`A_0 A_1 A_2 <g3:/ A0 A1 A2 />` along carrier
   :g:`a <g3:[ A0 A2 ]>` and :g:`B_0 B_1 B_2 <g3:/ B0 B1 B2 />` along carrier
   :g:`b <g3:[ B0 B2 ]>`, meeting at :g:`O <g3:O>` :math:`= (-2, 0)`.

.. step::

   Construct the inscribed hexagon :g:`A_0 B_1 A_2 B_0 A_1 B_2 <g3:< A0 B1 A2 B0 A1 B2 >>` and
   exact :math:`\mathbb{Q}(\sqrt{5})` cross-join meets :g:`M_{01} <g3:M01>`, :g:`M_{20} <g3:M20>`,
   and :g:`M_{12} <g3:M12>` along the Pappus line :g:`p <g3:[ M01 M12 ]>`.

.. step::

   Observe the emergent ``geometor.divine`` golden section :g:`A_1 M_{12} B_2 <g3:/ A1 M12 B2 />`:
   because :math:`x(A_1) = 1`, :math:`x(M_{12}) = \phi`, and :math:`x(B_2) = \phi + 1`, we have
   :math:`x(B_2) - x(M_{12}) = 1` and :math:`x(M_{12}) - x(A_1) = \phi - 1 = \phi^{-1}`, so
   :math:`|M_{12} B_2| / |A_1 M_{12}| = \phi` **identically**!
