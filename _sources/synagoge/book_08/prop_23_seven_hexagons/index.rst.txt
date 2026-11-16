:order: 3
:layout: book
:type: book
:title: 3. Proposition 23: Seven Congruent Regular Hexagons Inscribed in a Circle
:canonical_id: Syn. VIII.23
:folio: 0107
:excerpt: Single-compass constructions and Proposition 23: geometric analysis and synthesis inscribing seven congruent regular hexagons in a circle with exact circumradius relation R^2 = 7 s_6^2.
:tracks: English: index | Greek: el | Summary: summary | Notes: notes

.. _sec-b8-en-rusty-seven-hexagons:

Proposition 23: Seven Regular Hexagons Inscribed in a Circle
============================================================

.. rubric:: *Synagoge* Book VIII, Chapters 26–39, Proposition 23 (:cite:`Hultsch III, pp. 1074–1102 <hultsch:1878>`) · Critical English Edition

Turning to **instrumental geometry** (*τὰ ἰδίως λεγόμενα ὀργανικά*), Pappus observes that architects, stonecutters, and engineers constantly face practical constraints in the field: restoring the true diameter of a broken temple column from a surviving fragment (**Prop. 13**), constructing the conic through five given points on a cylindrical surface (**Prop. 14**), or executing plane constructions :term:`with a single fixed compass opening <heni-diastemati>` (*τὰ ἑνὶ διαστήματι γραφόμενα*, *Hultsch III p. 1074 ff.*)—inaugurating the fixed-"rusty"-compass tradition later carried forward by Abū al-Wafāʾ, Tartaglia, Ferrari, Cardano, and Poncelet–Steiner.

Chief among these instrumental constructions—where :term:`geometric analysis <analysis>` replaces blind trial-and-error (*πεῖρα*) with exact algebraic certainty—stands **Proposition 23** (*Hultsch III, pp. 1096–1102*), which crowns both Book VIII's architectural geometry and :doc:`Book V's honeycomb rosette <../../book_05/prop_01_10_isoperimetry/index>`:

.. picture:: /_static/constructions/honeycomb_isoperimetry.svg
   :alt: Synagoge Book VIII Proposition 23 — Seven Congruent Regular Hexagons Inscribed in a Given Circle (R = s_6 * sqrt(7))

.. enunciation::

   **Proposition 23 (Hultsch III, pp. 1096–1102)**: Into a given circle :g:`(H0, N) <g1:( H0 N )>` of center :g:`H0 <g1:H0>` and radius :g:`H0N <g1:[ H0 N ]>` $= R$, to **inscribe seven congruent regular hexagons**—one central hexagon :g:`V1..V6 <g1:< V1 V2 V3 V4 V5 V6 >>` concentric with the circle, and six surrounding hexagons :g:`C1 <g1:< C1 >>`, :g:`C2 <g1:< C2 >>`, :g:`C3 <g1:< C3 >>`, :g:`C4 <g1:< C4 >>`, :g:`C5 <g1:< C5 >>`, :g:`C6 <g1:< C6 >>` erected outward upon the six sides of the central hexagon so that each surrounding hexagon's opposite outer side has both endpoints fitted cleanly upon the circumference of circle :g:`(H0, N) <g1:( H0 N )>`.

.. step::

   **Analysis** (*ἀνάλυσις*, *Hultsch III pp. 1096–1098*): Suppose the seven regular hexagons of common side $s_6$ are already inscribed around center :g:`H0 <g1:H0>`, with outer rim vertex :g:`N <g1:N>` of top cell :g:`C1 <g1:< C1 >>` lying on circle :g:`(H0, N) <g1:( H0 N )>`. Because a regular hexagon decomposes into six equilateral triangles of side $s_6$ (:just:`IV.15` cor.), stepping from center :g:`H0 <g1:H0>` to a vertex of central cell :g:`V1..V6 <g1:< V1 V2 V3 V4 V5 V6 >>` advances distance $s_6$, and stepping along the outer radial zigzag across :g:`C1 <g1:< C1 >>` to rim vertex :g:`N <g1:N>` forms an obtuse triangle with sides $s_6$ and $2s_6$ enclosing an angle of $120^\circ$!

.. step::

   Apply :just:`II.12` (Euclid's obtuse-triangle square law, where the projection beyond the $120^\circ$ vertex equals $\frac{1}{2} s_6$): the square on radius :g:`H0N <g1:[ H0 N ]>` exceeds the sum of the squares on $s_6$ and $2s_6$ by twice the rectangle $2s_6 \cdot \frac{1}{2}s_6$:

   .. math::

      R^2 = |H_0 N|^2 = s_6^2 + (2s_6)^2 + 2(2s_6)\!\left(\frac{1}{2}s_6\right) = s_6^2 + 4s_6^2 + 2s_6^2 = 7\,s_6^2.

   Equivalently, in Cartesian coordinates centered at :g:`H0 <g1:H0>` (as constructed in :func:`~geometor.pappus.construct_honeycomb_isoperimetry`), rim vertex :g:`N <g1:N>` has horizontal displacement $\frac{1}{2}s_6$ and vertical displacement $\frac{3\sqrt{3}}{2}s_6$, giving quadrance $Q(H_0, N) = \frac{1}{4}s_6^2 + \frac{27}{4}s_6^2 = \frac{28}{4}s_6^2 = 7\,s_6^2$. Therefore **$R^2 : s_6^2 = 7 : 1$**, so the side $s_6 = \frac{R}{\sqrt{7}}$ is **given in magnitude** from the given radius $R$!

.. step::

   **Synthesis** (*σύνθεσις*, *Hultsch III pp. 1098–1102*): Given circle :g:`(H0, N) <g1:( H0 N )>` of radius $R$ (in our canonical $P = 12$ model, $R = 2\sqrt{7}$), construct $s_6$ such that $7\,s_6^2 = R^2$ ($s_6 = 2$). With center :g:`H0 <g1:H0>` and radius $s_6$, inscribe central regular hexagon :g:`V1..V6 <g1:< V1 V2 V3 V4 V5 V6 >>` (:just:`IV.15`), and upon its six sides erect the six congruent regular hexagons :g:`C1 <g1:< C1 >>`–:g:`C6 <g1:< C6 >>`.

.. step::

   By symmetry and :just:`II.12`, all twelve outer rim vertices (two on the outermost side of each of :g:`C1 <g1:< C1 >>`–:g:`C6 <g1:< C6 >>`, exemplified by :g:`N <g1:N>`) have exact quadrance $7\,s_6^2 = R^2$ from :g:`H0 <g1:H0>`, so every outer edge is inscribed cleanly upon circle :g:`(H0, N) <g1:( H0 N )>` without a single trial adjustment.
