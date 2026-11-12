.. _synagoge-b5-en:

=====================================================================================
Book V · On the Geometric Forethought of Bees & Isoperimetry (*Translation*)
=====================================================================================

.. rubric:: *Synagoge* Book V, Preface & Props. 1–10 (:cite:`Hultsch I, pp. 304–336 <hultsch:1876>`) · Original English Translation from Hultsch's Greek

.. _sec-b5-en-bees-preface:

1. Preface to Megethius: On the Sagacity of Bees (*Περὶ τῆς τῶν μελισσῶν σοφίας*)
---------------------------------------------------------------------------------

*Hultsch Vol. I, pp. 304–308 (Book V, Chs. 1–3)*

Although many and mighty theorems concerning plane and solid figures have been discovered by geometers, best :person:`Megethius <megethius>`, none elicits sharper philosophical wonder than the theory of :term:`isoperimetric figures <isoperimetros>` (*ἰσοπερίμετρα σχήματα*)—not only because its demonstrations are subtle, but because divine Providence has implanted an image of it even in irrational creatures. For mortals, endowed with reason and discursive intellect (*λόγος*), naturally pursue what is advantageous and orderly by deliberate art; yet the **bees**, possessing no instruction from geometry, fashion the honeycombs (*κηρία*) in which they store the celestial dew they bring to humankind according to a marvelous geometric forethought (*δαιμονίᾳ τινὶ προνοίᾳ*).

First, they took it as fundamental that the cells must lie **contiguous to one another without leaving empty crevices** (*μὴ καταλιπεῖν μεταξὺ τῶν ἀγγείων κενώματα*), lest foreign matter slip into the spaces between cells and spoil their work or waste the wax of the hive. Second, for strength and symmetry every cell had to be **equilateral and equiangular** (*ἰσόπλευρόν τε καὶ ἰσογώνιον*), since dissimilar shapes fitted awkwardly together would prove fragile and uneven.

Now around a single point in a plane—where the sum of the surrounding plane angles equals **four right angles** ($360^\circ$, :just:`I.13` cor.)—**only three** equilateral and equiangular rectilinear figures are capable of filling up the space without gaps or overlaps (*Ch. 2, Hultsch I p. 306*):

1. **Six equilateral triangles** ($n = 3$), since each interior angle is $\frac{2}{3}$ of a right angle ($60^\circ$, :just:`I.32`), and $6 \times \frac{2}{3} = 4$ right angles;
2. **Four squares** ($n = 4$), since each interior angle is $1$ right angle ($90^\circ$), and $4 \times 1 = 4$ right angles;
3. **Three regular hexagons** ($n = 6$), since each interior angle is $1\frac{1}{3}$ right angles ($\frac{4}{3} \times 90^\circ = 120^\circ$), and $3 \times \frac{4}{3} = 4$ right angles.

For regular pentagons ($n = 5$), each interior angle is $1\frac{1}{5}$ right angles ($108^\circ$): three pentagons joined at a vertex total only $3\frac{3}{5}$ right angles ($324^\circ$), leaving an unfillable gap, whereas four pentagons total $4\frac{4}{5}$ right angles ($432^\circ$), exceeding the plane! Every regular polygon of $n \ge 7$ sides has interior angle strictly exceeding $\frac{4}{3}$ right angles, so not even three can meet around a point.

Perceiving by nature that only these three polygons—the triangle, the square, and the hexagon—tile the plane seamlessly, the bees rejected both the triangle and the square and **chose the six-angled figure**, discerning that **for an equal expenditure of wax along the perimeter, the regular hexagon holds a greater quantity of honey than either the square or the equilateral triangle**. While bees know only so much as serves their craft, we who profess a share in human wisdom will prove universally (*Ch. 3, Hultsch I p. 308*) that among all equilateral and equiangular polygons of **equal perimeter**, that which has the **greater number of angles is always greater in area**, and greatest of all plane figures of equal perimeter is the **circle**.

.. _sec-b5-en-isoperimetric-propositions:

2. Propositions 1–10: The Planar Isoperimetric Chain
----------------------------------------------------

*Hultsch Vol. I, pp. 308–336 (Book V, Props. 1–10, extending :cite:`Zenodorus <zenodorus:isoperimetric>`)*

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

   On the right of the diagram, central cell :g:`V1..V6 <g1:< V1 V2 V3 V4 V5 V6 >>` centered at :g:`H0 <g1:H0>` is surrounded without gaps by six congruent hexagonal cells :g:`C1 <g1:< C1 >>`, :g:`C2 <g1:< C2 >>`, :g:`C3 <g1:< C3 >>`, :g:`C4 <g1:< C4 >>`, :g:`C5 <g1:< C5 >>`, :g:`C6 <g1:< C6 >>`, all inscribed cleanly inside circle :g:`(H0, N) <g1:( H0 N )>` of radius :g:`H0N <g1:[ H0 N ]>` $= s_6\sqrt{7} = 2\sqrt{7}$, anticipating :doc:`Book VIII Proposition 23 <../book-8-mechanics/book-8-mechanics-en>`.

*In the spatial second half of Book V (Props. 11–43, Hultsch I pp. 336–473), Pappus compares the sphere and regular polyhedra of equal surface area and preserves in Chapter 34 (Prop. 19, pp. 352–358) the **sole surviving ancient Greek enumeration of all thirteen Archimedean semi-regular solids**.*
