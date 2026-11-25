:type: theorem
:order: 1
:summary: Historical and mathematical foundations in Book VII of Pappus's Alexandrian Synagoge—from central perspectivities (Prop. 129) to the parallel and general Hexagon Lemmas (Props. 138 & 139).

Pappus of Alexandria & Book VII of the *Collection*
===================================================

Historical Context: The *Domain of Analysis*
--------------------------------------------

Working in Alexandria around **340 CE**, **Pappus of Alexandria** stood at the twilight
of Greek antiquity's mathematical tradition. Book VII of his eight-book *Synagoge*
(*Collection*) is devoted to the *Topos Analomenos*—the **Treasury (or Domain) of Analysis**,
a curriculum of geometric problem-solving treatises authored by **Euclid**, **Apollonius of
Perga**, **Aristaeus**, and **Eratosthenes**.

Among the lost works summarized in Book VII were the three books of **Euclid's** *Porisms*
(*Πορίσματα*), which investigated variable configurations whose invariant incidences remain
fixed as points move along lines. To help readers reconstruct Euclid's terse arguments,
Pappus supplied **38 auxiliary lemmas** (Propositions 119–156 of Book VII). Without
employing modern coordinates, those lemmas quietly laid the entire foundation of
nineteenth-century projective geometry:

- **Proposition 129** (*Invariance of the Cross-Ratio under Central Perspectivity*): If four
  concurrent rays issuing from an apex :math:`O` are cut by two transversal lines :math:`a` and :math:`b`, the
  compound ratio of segments cut off on :math:`a` equals the compound ratio cut off on :math:`b`.
- **Proposition 131** (*Harmonic Division in the Complete Quadrilateral*): Establishes the
  harmonic separation induced on a transversal by opposite sides and diagonals of a
  four-line figure.
- **Proposition 138** (*The Parallel Hexagon Lemma*): Establishes collinearity of the three
  cross-join intersections when the two carrier lines :math:`a` and :math:`b` are parallel (:math:`s(a, b) = 0`).
- **Proposition 139** (*The General Projective Hexagon Lemma*): Establishes collinearity
  when the two carrier lines :math:`a` and :math:`b` intersect at a finite point :math:`O`.

Why Straightedge-Only Incidence Matters
---------------------------------------

Throughout Euclid's *Elements*, compass-and-straightedge constructions intertwine **incidence**
(drawing a line through two points, intersecting two lines) with **metric congruence**
(transferring lengths via circles, measuring angles). Pappus's Hexagon Theorem is revolutionary
because its hypotheses and conclusion involve **point-line incidence alone**:

1. No circle is drawn.
2. No distance or angle is measured—though Pappus's own ancient proof ingeniously used
   compound ratios of segments (equivalent to Menelaus's theorem or cross-ratios), the theorem
   itself is purely projective.
3. In 1899, **David Hilbert** proved in *Grundlagen der Geometrie* that within any projective
   plane, **Pappus's Hexagon Theorem is logically equivalent to the commutativity of
   multiplication** (:math:`xy = yx`) in the underlying coordinate division ring (skew field)!

Proposition 138: The Parallel Carrier Lemma
-------------------------------------------

Before proving the general oblique case, Pappus treats parallel carrier lines
:g:`a <g1:[ A0 A2 ]>` and :g:`b <g1:[ B0 B2 ]>`—precisely the coordinate setting explored
in GEOMETOR's original 2023 ``pappus.py`` study:

.. math::

   A_0 = (0, 0), \quad A_1 = (1, 0), \quad A_2 = (3, 0), \qquad
   B_0 = (0, 1), \quad B_1 = \left(\tfrac{3}{2}, 1\right), \quad B_2 = \left(\tfrac{5}{2}, 1\right).

Here the Wildberger rational-trigonometric spread between the two carriers vanishes identically,
:math:`s(a, b) = 0`, meaning their intersection lies on the **ideal line at infinity**.

.. picture:: /_static/constructions/pappus_parallel.svg
   :alt: Synagoge Book VII Proposition 138 — Parallel Carrier Lines

.. enunciation::

   Let :g:`A_0 <g1:A0>`, :g:`A_1 <g1:A1>`, :g:`A_2 <g1:A2>` lie on :g:`a <g1:[ A0 A2 ]>`
   (:math:`y = 0`) and let :g:`B_0 <g1:B0>`, :g:`B_1 <g1:B1>`, :g:`B_2 <g1:B2>` lie on the
   parallel line :g:`b <g1:[ B0 B2 ]>` (:math:`y = 1`). Then the opposite cross-join meets
   :g:`M_{01} <g1:M01>`, :g:`M_{20} <g1:M20>`, and :g:`M_{12} <g1:M12>` lie on a single
   straight line :g:`p <g1:[ M01 M12 ]>`.

.. step::

   Lay out the three collinear points :g:`A_0 <g1:A0>`, :g:`A_1 <g1:A1>`, :g:`A_2 <g1:A2>`
   along :g:`y = 0 <g1:[ A0 A2 ]>` and the three collinear points :g:`B_0 <g1:B0>`,
   :g:`B_1 <g1:B1>`, :g:`B_2 <g1:B2>` along the parallel carrier :g:`y = 1 <g1:[ B0 B2 ]>`.

.. step::

   Intersect opposite hexagon sides :g:`A_0B_1 <g1:[ A0 B1 ]>` and :g:`A_1B_0 <g1:[ A1 B0 ]>`
   to obtain :g:`M_{01} <g1:M01>` :math:`= \left(\frac{3}{5}, \frac{2}{5}\right)`.

.. step::

   Intersect :g:`A_2B_0 <g1:[ A2 B0 ]>` and :g:`A_0B_2 <g1:[ A0 B2 ]>` to obtain
   :g:`M_{20} <g1:M20>` :math:`= \left(\frac{15}{11}, \frac{6}{11}\right)`, and intersect
   :g:`A_1B_2 <g1:[ A1 B2 ]>` and :g:`A_2B_1 <g1:[ A2 B1 ]>` to obtain
   :g:`M_{12} <g1:M12>` :math:`= \left(2, \frac{2}{3}\right)`.

.. step::

   Verify exact collinearity: all three points satisfy :math:`-4x + 21y = 6`, lying on the
   Pappus line :g:`M_{01}M_{12} <g1:[ M01 M12 ]>` with exact rational quadrances
   :math:`Q(M_{01}, M_{20}) = \frac{1828}{3025}` and :math:`Q(M_{20}, M_{12}) = \frac{457}{1089}`.

From Parallelism to Projective Unity
------------------------------------

In the real projective plane :math:`\mathbb{RP}^2`, Proposition 138 and Proposition 139 are **the
exact same theorem**: applying a projective transformation sending the ideal line at infinity
to a finite line maps parallel carriers :math:`a \parallel b` directly to intersecting carriers
:math:`a \cap b = O`, and conversely sending any line through :math:`O` to infinity reduces Proposition 139
instantaneously to Proposition 138!

Even when one of the cross-join pairs itself happens to be parallel (for example
:math:`[A_0 B_0] \parallel [A_1 B_1]` when :math:`x(A_0)=x(B_0)=0` and :math:`x(A_1)=x(B_1)=1`), its intersection
is an ideal point on the line at infinity—meaning the line joining the remaining two finite
meets is **parallel** to that cross-join pair. ``construct_pappus_hexagon`` handles both
finite and ideal intersections seamlessly in exact symbolic arithmetic.
