:order: 2
:layout: book
:type: book
:title: Proposition 1: Isoperimetric Regular Polygons
:canonical_id: Syn. V.1
:folio: 0247
:excerpt: Proof that among regular polygons of equal perimeter, the polygon with more angles encloses the greater area (hexagon > square > triangle).
:tracks: English: index | Greek: el | Summary: summary | Notes: notes

.. _sec-b5-en-isoperimetric-propositions:

Proposition 1: Isoperimetric Regular Polygons
=============================================

.. rubric:: *Synagoge* Book V, Prop. 1 (:cite:`Hultsch I, pp. 308–312 <hultsch:1876>`, extending :cite:`Zenodorus <zenodorus:isoperimetric>`; App. IV, p. 1235) · Original English Translation

.. folio:: 0247
   :page: 1235

.. picture:: /_static/constructions/honeycomb_isoperimetry.svg
   :alt: Synagoge Book V Proposition 1 & Book VIII Proposition 23 — Equal-Perimeter Polygons (P = 12) and Seven-Cell Honeycomb Rosette

.. enunciation::

   Of all equilateral and equiangular rectilinear polygons having an **equal perimeter** $P$, that which has the **more angles encloses the greater area**; in particular, for equal perimeter $P = 12$, the regular hexagon :g:`V1..V6 <g1:< V1 V2 V3 V4 V5 V6 >>` ($s_6 = 2$, area $6\sqrt{3}$) strictly exceeds both the square :g:`Q1..Q4 <g1:< Q1 Q2 Q3 Q4 >>` ($s_4 = 3$, area $9$) and the equilateral triangle :g:`T1..T3 <g1:< T1 T2 T3 >>` ($s_3 = 4$, area $4\sqrt{3}$), while six surrounding hexagonal cells :g:`C1 <g1:< C1 >>`–:g:`C6 <g1:< C6 >>` tile seamlessly around :g:`H0 <g1:H0>` inside circle :g:`(H0, N) <g1:( H0 N )>` of radius :g:`H0N <g1:[ H0 N ]>` $= s_6\sqrt{7}$.

.. step::

   Compare any two :term:`isoperimetric <isoperimetros>` regular polygons of $m$ and $n$ sides with $n > m$. Subdivide each polygon from its center into $n$ (respectively $m$) congruent isosceles triangles whose bases sum to the common perimeter $P$; then each polygon's area equals half its perimeter multiplied by its **apothem** (*κάθετος*, perpendicular from center to side):

   .. math::

      \operatorname{Area}_n = \frac{1}{2}\,P\,a_n, \qquad \operatorname{Area}_m = \frac{1}{2}\,P\,a_m.

   Hence proving $\operatorname{Area}_n > \operatorname{Area}_m$ reduces to proving $a_n > a_m$.

.. step::

   Because the half-central angle $\frac{\pi}{n} < \frac{\pi}{m}$ satisfies $\frac{\tan(\pi/m)}{\tan(\pi/n)} > \frac{n}{m}$ (established rigorously in :doc:`Proposition 3 <../prop_03_sector_tangent_inequality/index>`), the half-bases $\frac{P}{2n}$ and $\frac{P}{2m}$ force $a_n = \frac{P}{2n \tan(\pi/n)} > \frac{P}{2m \tan(\pi/m)} = a_m$.

.. step::

   Evaluate explicitly at common perimeter $P = 12$: triangle :g:`T1T2T3 <g1:< T1 T2 T3 >>` ($s_3 = 4$, $4\sqrt{3} \approx 6.9282$), square :g:`Q1Q2Q3Q4 <g1:< Q1 Q2 Q3 Q4 >>` ($s_4 = 3$, $9$), hexagon :g:`V1..V6 <g1:< V1 V2 V3 V4 V5 V6 >>` ($s_6 = 2$, $6\sqrt{3} \approx 10.3923$). Surrounding six cells :g:`C1 <g1:< C1 >>`–:g:`C6 <g1:< C6 >>` fit inside :g:`(H0, N) <g1:( H0 N )>` anticipating :doc:`Book VIII Proposition 23 <../../book_08/prop_23_seven_hexagons/index>`.
