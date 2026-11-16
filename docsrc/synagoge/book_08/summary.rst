:navigation: header
:order: 8
:type: book
:nav_title: Book VIII Summary
:breadcrumb_title: Book VIII · Summary
:layout: book
:book_title: Book VIII · Summary & Exact Symbolic Audit
:author: Pappus of Alexandria
:excerpt: Structural division of Book VIII and exact symbolic verification of Proposition 23 (R^2 = 7 s_6^2) over Q(sqrt(3), sqrt(7)).

.. _synagoge-b8-summary:

Book VIII · Summary & Exact Symbolic Audit (*Mechanics, Baroulkos & Seven Hexagons*)
==========================================================================================

.. rubric:: Structural Argument Map & ``geometor.pappus`` Symbolic Verification

1. Architecture of *Synagoge* Book VIII (*Hultsch III, pp. 1022–1115*)
----------------------------------------------------------------------

.. list-table:: Structural Divisions of Book VIII
   :header-rows: 1
   :widths: 22 30 48

   * - Hultsch Locus
     - Mechanical / Geometric Theme
     - Core Mathematical Result
   * - **Chs. 1–4** (*pp. 1022–1028*)
     - Preface to :person:`Hermodorus <hermodorus>`
     - Theoretical (*λογικόν*) vs. manual (*χειρουργικόν*) mechanics; defense of :person:`Archimedes <archimedes>`, :person:`Hero <heron>` & :person:`Carpus <carpus>`
   * - **Chs. 5–15** (*pp. 1030–1054*)
     - :term:`Center of gravity <kentron-barous>` (*Props. 1–8*)
     - Suspension definition; median centroid of $\triangle ABC$; centroid invariance of cyclically inscribed triangles (*Prop. 2*)
   * - **Chs. 16–18** (*pp. 1054–1060*)
     - The Inclined Plane (*Prop. 9*)
     - Earliest surviving Greek analysis of equilibrium on a plane inclined at angle $\alpha$
   * - **Chs. 19–25** (*pp. 1060–1073*)
     - Lever & :term:`Baroulkos <baroulkos>` (*Props. 10–12*)
     - ``«δός μοι ποῦ στῶ καὶ κινῶ τὴν γῆν»``; $1{,}000$ talents moved by $5$ talents ($200:1$ gear-train + worm screw); 5 simple machines
   * - **Chs. 26–37** (*pp. 1074–1096*)
     - Instrumental & :term:`Fixed-Compass <heni-diastemati>` Geometry (*Props. 13–22*)
     - Broken cylinder diameter; 5-point conic on cylinder; constructions *ἑνὶ διαστήματι* (with one compass opening)
   * - **Chs. 38–39** (*pp. 1096–1102*)
     - Seven Hexagons in a Circle (*Prop. 23*)
     - Exact circumradius law $R^2 = 7\,s_6^2 \iff R = s_6\sqrt{7}$ proved by analysis & synthesis via :just:`II.12`
   * - **Chs. 40–45** (*pp. 1104–1115*)
     - Toothed Gearwheels (*Props. 24–26*)
     - Pitch-circle diameter proportion $D_1 : D_2 = m : n$ for meshing cogwheels

2. Exact Quadrance Verification of Proposition 23 ($R^2 = 7\,s_6^2$)
--------------------------------------------------------------------

Modeled in :func:`geometor.pappus.construct_honeycomb_isoperimetry` and :func:`geometor.pappus.verify_honeycomb_isoperimetry` over $\mathbb{Q}(\sqrt{3}, \sqrt{7})$:

* **Central Hexagon** $H_0$ centered at $\left(\frac{3}{2}s_6, 0\right)$ with side $s_6 = \frac{P}{6}$ ($s_6 = 2$ at $P = 12$).
* **Six Surrounding Hexagons** $C_1, \dots, C_6$ sharing all six inner walls without gaps, with centers displaced by $\sqrt{3}\,s_6$ perpendicular to each side of $H_0$.
* **Outer Rim Vertex** $N = \left(2\,s_6, \frac{3\sqrt{3}}{2}\,s_6\right)$ of $C_1$:

  .. math::

     Q(H_0, N) = \left(\frac{1}{2}\,s_6\right)^2 + \left(\frac{3\sqrt{3}}{2}\,s_6\right)^2
     = \left(\frac{1}{4} + \frac{27}{4}\right) s_6^2 = 7\,s_6^2,

  confirming $R_7 = s_6\sqrt{7}$ ($R_7 = 2\sqrt{7}$ for $P = 12$) in 100% exact symbolic arithmetic with zero floating-point approximation.
