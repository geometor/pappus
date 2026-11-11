**Symbolic projective geometry investigations into Pappus of Alexandria's Hexagon Theorem, Steiner's six-line configuration, cross-ratios, harmonic conjugates, and golden perspectivities.**

Around 340 CE in Alexandria, **Pappus** compiled Book VII (*On the Domain of Analysis*)
of his *Synagoge* (*Collection*)—preserving lemmas to the lost treatises of Euclid's
*Porisms* and Apollonius. Hidden among those lemmas (Propositions 138 and 139) stands the
oldest and deepest incidence theorem of projective geometry: **three collinear points on each
of two lines determine three opposite cross-join intersections that are themselves collinear**,
established by straightedge incidence alone without a single circle or metric measurement.

``geometor.pappus`` models Pappus's projective canon in **100% exact symbolic algebra** using
`SymPy <https://www.sympy.org/>`_, ``geometor.model``, and ``geometor.divine``. Hover over
any highlighted symbol below—or use the **Play / Step** controls beneath the diagram—to trace
the construction interactively.

.. picture:: /_static/constructions/pappus_hexagon.svg
   :alt: Interactive Pappus Hexagon Construction (Synagoge Book VII, Proposition 139)

.. enunciation::

   Let :g:`A_0 <g1:A0>`, :g:`A_1 <g1:A1>`, :g:`A_2 <g1:A2>` lie on carrier line
   :g:`a <g1:[ A0 A2 ]>` and let :g:`B_0 <g1:B0>`, :g:`B_1 <g1:B1>`, :g:`B_2 <g1:B2>`
   lie on carrier line :g:`b <g1:[ B0 B2 ]>` meeting at :g:`O <g1:O>`. Then the three
   opposite cross-join intersections :g:`M_{01} <g1:M01>`, :g:`M_{20} <g1:M20>`, and
   :g:`M_{12} <g1:M12>` are collinear on the **Pappus line** :g:`p <g1:[ M01 M12 ]>`.

.. step::

   Establish carrier line :g:`a <g1:[ A0 A2 ]>` carrying :g:`A_0 <g1:A0>` $= (0, 0)$,
   :g:`A_1 <g1:A1>` $= (2, 0)$, :g:`A_2 <g1:A2>` $= (5, 0)$ and carrier line
   :g:`b <g1:[ B0 B2 ]>` carrying :g:`B_0 <g1:B0>` $= (0, 2)$, :g:`B_1 <g1:B1>` $= (2, 3)$,
   :g:`B_2 <g1:B2>` $= (6, 5)$, concurring at perspective apex :g:`O <g1:O>` $= (-4, 0)$.

.. step::

   Draw the first opposite cross-join pair :g:`A_0B_1 <g1:[ A0 B1 ]>` and
   :g:`A_1B_0 <g1:[ A1 B0 ]>`, intersecting at the exact rational point
   :g:`M_{01} <g1:M01>` $= \left(\frac{4}{5}, \frac{6}{5}\right)$.

.. step::

   Draw the second opposite cross-join pair :g:`A_2B_0 <g1:[ A2 B0 ]>` and
   :g:`A_0B_2 <g1:[ A0 B2 ]>`, intersecting at
   :g:`M_{20} <g1:M20>` $= \left(\frac{60}{37}, \frac{50}{37}\right)$.

.. step::

   Draw the third opposite cross-join pair :g:`A_1B_2 <g1:[ A1 B2 ]>` and
   :g:`A_2B_1 <g1:[ A2 B1 ]>` of hexagon :g:`H <g1:< A0 B1 A2 B0 A1 B2 >>`,
   intersecting at :g:`M_{12} <g1:M12>` $= \left(\frac{10}{3}, \frac{5}{3}\right)$.

.. step::

   Join :g:`M_{01} <g1:M01>`, :g:`M_{20} <g1:M20>`, and :g:`M_{12} <g1:M12>`: all three
   points satisfy the exact linear equation $-7x + 38y = 40$, proving collinearity along
   the **Pappus line** :g:`M_{01}M_{12} <g1:[ M01 M12 ]>`.
