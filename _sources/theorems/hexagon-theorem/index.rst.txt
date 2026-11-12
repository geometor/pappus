:type: theorem
:order: 2
:summary: Step-by-step symbolic construction of Synagoge VII.139, exact homogeneous polynomial proof over eight free symbols, and the three homologous square/circle/diamond triangles.

The Hexagon Theorem Step-by-Step
================================

General Projective Construction (*Synagoge* VII.139)
----------------------------------------------------

Let $a$ and $b$ be two distinct lines in the plane meeting at $O$, carrying triples
$(A_0, A_1, A_2)$ and $(B_0, B_1, B_2)$ respectively. Connecting alternating vertices in the
cyclic order

.. math::

   H = \langle A_0,\, B_1,\, A_2,\, B_0,\, A_1,\, B_2 \rangle

forms a self-intersecting **Pappus hexagon** inscribed between the two lines. Its six sides
group naturally into three pairs of opposite cross-joins:

.. list-table:: Canonical *Synagoge* VII.139 Exact Symbolic Coordinates (``preset="hexagon"``)
   :header-rows: 1
   :widths: 22 38 40

   * - Geometric Element
     - Incidence Definition
     - Exact SymPy Coordinates / Equation
   * - Carrier $a$
     - $[A_0 A_2]$ through $(0,0), (2,0), (5,0)$
     - $y = 0$
   * - Carrier $b$
     - $[B_0 B_2]$ through $(0,2), (2,3), (6,5)$
     - $-3x + 6y - 12 = 0$
   * - Perspective Apex $O$
     - $a \cap b$
     - $(-4, 0)$, spread $s(a, b) = \frac{1}{5}$
   * - Cross-Join Meet $M_{01}$
     - $[A_0 B_1] \cap [A_1 B_0]$
     - $\left(\frac{4}{5},\, \frac{6}{5}\right)$
   * - Cross-Join Meet $M_{20}$
     - $[A_2 B_0] \cap [A_0 B_2]$
     - $\left(\frac{60}{37},\, \frac{50}{37}\right)$
   * - Cross-Join Meet $M_{12}$
     - $[A_1 B_2] \cap [A_2 B_1]$
     - $\left(\frac{10}{3},\, \frac{5}{3}\right)$
   * - **Pappus Line** $p$
     - $[M_{01} M_{12}]$ containing $M_{20}$
     - $-7x + 38y - 40 = 0$

.. picture:: /_static/constructions/pappus_hexagon.svg
   :alt: Synagoge Book VII Proposition 139 — General Intersecting Carriers

.. step::

   Fix collinear triples :g:`A_0 <g1:A0>`, :g:`A_1 <g1:A1>`, :g:`A_2 <g1:A2>` on
   :g:`a <g1:[ A0 A2 ]>` and :g:`B_0 <g1:B0>`, :g:`B_1 <g1:B1>`, :g:`B_2 <g1:B2>` on
   :g:`b <g1:[ B0 B2 ]>`, intersecting at :g:`O <g1:O>`.

.. step::

   Trace the inscribed 6-cycle hexagon :g:`A_0 B_1 A_2 B_0 A_1 B_2 <g1:< A0 B1 A2 B0 A1 B2 >>`
   alternating between lines :g:`a <g1:[ A0 A2 ]>` and :g:`b <g1:[ B0 B2 ]>`.

.. step::

   Intersect opposite sides :g:`A_0B_1 <g1:[ A0 B1 ]>` ($-3x + 2y = 0$) and
   :g:`A_1B_0 <g1:[ A1 B0 ]>` ($-2x - 2y + 4 = 0$) at :g:`M_{01} <g1:M01>` $= (4/5, 6/5)$.

.. step::

   Intersect opposite sides :g:`A_2B_0 <g1:[ A2 B0 ]>` ($-2x - 5y + 10 = 0$) and
   :g:`A_0B_2 <g1:[ A0 B2 ]>` ($-5x + 6y = 0$) at :g:`M_{20} <g1:M20>` $= (60/37, 50/37)$,
   and :g:`A_1B_2 <g1:[ A1 B2 ]>` with :g:`A_2B_1 <g1:[ A2 B1 ]>` at
   :g:`M_{12} <g1:M12>` $= (10/3, 5/3)$.

.. step::

   Construct the Pappus line :g:`M_{01}M_{12} <g1:[ M01 M12 ]>`: substituting
   :g:`M_{20} <g1:M20>` yields $-7(60/37) + 38(50/37) - 40 = (-420 + 1900 - 1480)/37 = 0$.

Universal Homogeneous Symbolic Proof
------------------------------------

Beyond any specific rational instance, ``verify_pappus_symbolic()`` proves Pappus's Hexagon
Theorem **universally** over the eight-variable polynomial ring
$\mathbb{Z}[a_0, a_1, a_2, b_0, b_1, b_2, m, c]$:

1. By an affine frame choice, take carrier $a$ as $y = 0$ with homogeneous points
   $A_i = [a_i : 0 : 1]$, and take carrier $b$ as $y = m x + c$ with homogeneous points
   $B_j = [b_j : m b_j + c : 1]$ (simultaneously covering oblique lines $m \ne 0$ and
   parallel lines $m = 0, c \ne 0$).
2. In $\mathbb{P}^2$, both joining two points and intersecting two lines are given by the
   3D vector cross product $\times$:

   .. math::

      M_{01} = (A_0 \times B_1) \times (A_1 \times B_0), \quad
      M_{12} = (A_1 \times B_2) \times (A_2 \times B_1), \quad
      M_{20} = (A_2 \times B_0) \times (A_0 \times B_2).

3. The three points $M_{01}, M_{12}, M_{20}$ are collinear if and only if their $3 \times 3$
   homogeneous determinant vanishes:

   .. math::

      \det \begin{bmatrix} M_{01} \\ M_{12} \\ M_{20} \end{bmatrix} \equiv 0
      \quad \text{in } \mathbb{Z}[a_0, a_1, a_2, b_0, b_1, b_2, m, c].

   Expanding this degree-12 polynomial in SymPy cancels every monomial identically to ``0``—a
   direct computational manifestation of the commutativity of polynomial multiplication!

Homologous Type Triangles (``square``, ``circle``, ``diamond``)
---------------------------------------------------------------

In GEOMETOR's ``pappus-3.py`` investigation, the three indices $\{0, 1, 2\}$ are assigned
three structural types—**square** ($0$), **circle** ($1$), and **diamond** ($2$)—so that each
cross-join meet inherits the **complementary** index missing from its pair:

- **Square** ($0$): :g:`A_0 <g2:A0>`, :g:`B_0 <g2:B0>`, and opposite meet :g:`M_{12} <g2:M12>`
  form :g:`△_{square} <g2:< A0 B0 M12 >>` (exact area $\frac{10}{3}$).
- **Circle** ($1$): :g:`A_1 <g2:A1>`, :g:`B_1 <g2:B1>`, and opposite meet :g:`M_{20} <g2:M20>`
  form :g:`△_{circle} <g2:< A1 B1 M20 >>` (exact area $\frac{21}{37}$).
- **Diamond** ($2$): :g:`A_2 <g2:A2>`, :g:`B_2 <g2:B2>`, and opposite meet :g:`M_{01} <g2:M01>`
  form :g:`△_{diamond} <g2:< A2 B2 M01 >>` (exact area $\frac{111}{10}$).

.. picture:: /_static/constructions/pappus_triangles.svg
   :alt: Homologous Square, Circle, and Diamond Triangles in the Pappus Configuration

.. step::

   Highlight the **square** triad :g:`△_{square} <g2:< A0 B0 M12 >>` joining
   :g:`A_0 <g2:A0>`, :g:`B_0 <g2:B0>`, and the opposite cross-join meet :g:`M_{12} <g2:M12>`.

.. step::

   Highlight the **circle** triad :g:`△_{circle} <g2:< A1 B1 M20 >>` joining
   :g:`A_1 <g2:A1>`, :g:`B_1 <g2:B1>`, and :g:`M_{20} <g2:M20>`.

.. step::

   Highlight the **diamond** triad :g:`△_{diamond} <g2:< A2 B2 M01 >>` joining
   :g:`A_2 <g2:A2>`, :g:`B_2 <g2:B2>`, and :g:`M_{01} <g2:M01>`—the three third-vertices
   :g:`M_{12} <g2:M12>`, :g:`M_{20} <g2:M20>`, :g:`M_{01} <g2:M01>` align along the shared
   Pappus axis :g:`p <g2:[ M01 M12 ]>`.
