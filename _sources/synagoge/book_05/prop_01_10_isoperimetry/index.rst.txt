:order: 2
:layout: book
:type: book
:title: Propositions 1–10: The Planar Isoperimetric Chain
:canonical_id: Syn. V.1-10
:excerpt: Pappus's rigorous demonstration extending Zenodorus that among regular polygons of equal perimeter that which has more angles encloses greater area, and greatest of all is the circle.
:tracks: English: index | Greek: el | Summary: summary | Notes: notes

.. _sec-b5-en-isoperimetric-propositions:

Propositions 1–10: The Planar Isoperimetric Chain
=================================================

.. rubric:: *Synagoge* Book V, Props. 1–10 (:cite:`Hultsch I, pp. 308–336 <hultsch:1876>`, extending :cite:`Zenodorus <zenodorus:isoperimetric>`) · Original English Translation from Hultsch's Greek

.. picture:: /_static/constructions/honeycomb_isoperimetry.svg
   :alt: Synagoge Book V Proposition 1 & Book VIII Proposition 23 — Equal-Perimeter Polygons (P = 12) and Seven-Cell Honeycomb Rosette

.. enunciation::

   **Proposition 1 (Hultsch I, pp. 308–312)**: Of all equilateral and equiangular rectilinear polygons having an **equal perimeter** $P$, that which has the **more angles encloses the greater area**; in particular, for equal perimeter $P = 12$, the regular hexagon :g:`V1..V6 <g1:< V1 V2 V3 V4 V5 V6 >>` ($s_6 = 2$, area $6\sqrt{3}$) strictly exceeds both the square :g:`Q1..Q4 <g1:< Q1 Q2 Q3 Q4 >>` ($s_4 = 3$, area $9$) and the equilateral triangle :g:`T1..T3 <g1:< T1 T2 T3 >>` ($s_3 = 4$, area $4\sqrt{3}$), while six surrounding hexagonal cells :g:`C1 <g1:< C1 >>`–:g:`C6 <g1:< C6 >>` tile seamlessly around :g:`H0 <g1:H0>` inside circle :g:`(H0, N) <g1:( H0 N )>` of radius :g:`H0N <g1:[ H0 N ]>` $= s_6\sqrt{7}$.

.. step::

   Compare any two :term:`isoperimetric <isoperimetros>` regular polygons of $m$ and $n$ sides with $n > m$ (e.g., hexagon $n = 6$ vs. square $m = 4$ or triangle $m = 3$). Subdivide each polygon from its center into $n$ (respectively $m$) congruent isosceles triangles whose bases sum to the common perimeter $P$; then each polygon's area equals half its perimeter multiplied by its **apothem** (*κάθετος*, perpendicular from the center to a side):

   .. math::

      \operatorname{Area}_n = \frac{1}{2}\,P\,a_n, \qquad \operatorname{Area}_m = \frac{1}{2}\,P\,a_m.

   Hence proving $\operatorname{Area}_n > \operatorname{Area}_m$ reduces to proving that the apothem $a_n$ strictly exceeds $a_m$!

.. step::

   Superimpose half-side right triangles sharing equal central-angle-to-tan comparison (*Props. 1–2, Hultsch I pp. 308–316*, invoking the radian/sector tangent inequality proved rigorously via circular sectors in *Prop. 3*—the exact companion to Ptolemy's chord-arc inequality in ``geometor/ptolemy``): because the half-central angle $\frac{\pi}{n} < \frac{\pi}{m}$ satisfies $\frac{\tan(\pi/m)}{\tan(\pi/n)} > \frac{n}{m}$, the half-bases $\frac{P}{2n}$ and $\frac{P}{2m}$ force $a_n = \frac{P}{2n \tan(\pi/n)} > \frac{P}{2m \tan(\pi/m)} = a_m$.

.. step::

   Evaluate explicitly at common perimeter $P = 12$ on the left of the diagram:

   * Equilateral triangle :g:`T1T2T3 <g1:< T1 T2 T3 >>` ($s_3 = 4$): $\operatorname{Area}_3 = \frac{\sqrt{3}}{4}(4)^2 = 4\sqrt{3} \approx 6.9282$.
   * Square :g:`Q1Q2Q3Q4 <g1:< Q1 Q2 Q3 Q4 >>` ($s_4 = 3$): $\operatorname{Area}_4 = 3^2 = 9$.
   * Regular hexagon :g:`V1..V6 <g1:< V1 V2 V3 V4 V5 V6 >>` ($s_6 = 2$): $\operatorname{Area}_6 = \frac{3\sqrt{3}}{2}(2)^2 = 6\sqrt{3} \approx 10.3923$.

   The exact algebraic ratios $\frac{\operatorname{Area}_6}{\operatorname{Area}_3} = \frac{3}{2}$ and $\frac{\operatorname{Area}_6}{\operatorname{Area}_4} = \frac{2\sqrt{3}}{3}$ (whose square is $\frac{12}{9} = \frac{4}{3} > 1$) prove without decimal approximation that the hexagon stores **$50\%$ more honey than the triangle** and **$\frac{2\sqrt{3}}{3} \approx 15.47\%$ more honey than the square** for the exact same wax perimeter!

.. step::

   Proceeding through **Propositions 2–10** (*Hultsch I pp. 312–336*), Pappus completes the planar extremal proof:

   * **Prop. 2**: A **circle** of perimeter $P$ has area $\frac{P^2}{4\pi}$ strictly greater than *any* regular polygon of the same perimeter: circumscribing a similar regular polygon around the circle gives area $\frac{1}{2} P_{\text{circ}} R$, and since the circumscribed polygon's perimeter strictly exceeds the circle's circumference (:person:`Archimedes <archimedes>`, *On the Sphere and Cylinder* I), scaling down to common perimeter $P$ shrinks the polygon's apothem strictly below $R$.
   * **Props. 4–6**: Among triangles on the same base with equal sum of the remaining two sides, the **isosceles** triangle has the greatest area; consequently, among all $n$-gons of given perimeter, any maximum-area $n$-gon must be **equilateral**.
   * **Props. 7–10**: Similarly, among equilateral polygons of given perimeter and side count, the **equiangular** one encloses greater area than one that is not equiangular—completing the chain $\text{irregular } n\text{-gon} < \text{regular } n\text{-gon} < \text{regular } (n+1)\text{-gon} < \text{circle}$.

.. step::

   On the right of the diagram, central cell :g:`V1..V6 <g1:< V1 V2 V3 V4 V5 V6 >>` centered at :g:`H0 <g1:H0>` is surrounded without gaps by six congruent hexagonal cells :g:`C1 <g1:< C1 >>`, :g:`C2 <g1:< C2 >>`, :g:`C3 <g1:< C3 >>`, :g:`C4 <g1:< C4 >>`, :g:`C5 <g1:< C5 >>`, :g:`C6 <g1:< C6 >>`, all inscribed cleanly inside circle :g:`(H0, N) <g1:( H0 N )>` of radius :g:`H0N <g1:[ H0 N ]>` $= s_6\sqrt{7} = 2\sqrt{7}$, anticipating :doc:`Book VIII Proposition 23 <../../book_08/prop_23_seven_hexagons/index>`.

*In the spatial second half of Book V (Props. 11–43, Hultsch I pp. 336–473), Pappus compares the sphere and regular polyhedra of equal surface area and preserves in Chapter 34 (Prop. 19, pp. 352–358) the **sole surviving ancient Greek enumeration of all thirteen Archimedean semi-regular solids**.*
