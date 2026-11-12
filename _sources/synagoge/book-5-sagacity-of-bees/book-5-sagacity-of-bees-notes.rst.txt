.. _synagoge-b5-notes:

===============================================================================
Book V · Philological & Mathematical Notes (*Zenodorus, Bees & 13 Solids*)
===============================================================================

.. rubric:: Variational History, Sector Inequality & Archimedean Polyhedra

1. Pappus's Honeycomb Preface in the History of Optimization (*Hultsch I, pp. 304–308*)
---------------------------------------------------------------------------------------

Pappus's Preface to :person:`Megethius <megethius>` is the founding classical text of **mathematical biology and geometric optimization**. While Varro (*Res Rusticae* III.16), Pliny, and Aelian had admired the six-sided wax cells of bees, Pappus was the first to formulate the honeycomb as a **constrained variational problem**: maximize enclosed area $A$ for fixed wall perimeter $P$ subject to the topological constraint that congruent cells partition $\mathbb{R}^2$ without interstitial voids. Sixteen centuries later, Charles Darwin (*Origin of Species*, Ch. VII) hailed the honeycomb as *"absolutely perfect in economising labour and wax,"* and in **1999 Thomas C. Hales** proved the full *Honeycomb Conjecture*—showing that even if arbitrary **curved** walls are permitted, the regular hexagonal grid still minimizes total perimeter among all equal-area partitions of the plane!

2. Zenodorus and the Sector-Tangent Lemma (*Prop. 3, Hultsch I pp. 314–318*)
----------------------------------------------------------------------------

Pappus's planar proof in *Props. 1–10* reworks and sharpens the lost second-century BCE treatise *On Isoperimetric Figures* (:cite:`Περὶ ἰσοπεριμέτρων σχημάτων <zenodorus:isoperimetric>`) by :person:`Zenodorus <zenodorus>` (also summarized more briefly by Theon of Alexandria in his commentary on Ptolemy's *Almagest* I.10). Notice the deep structural kinship between **Pappus V.3** and **Ptolemy's Inequality Lemma** (*Almagest* I.10, modeled in ``geometor/ptolemy``):

* Ptolemy compares **chords** to arcs ($\frac{\operatorname{crd}\alpha}{\operatorname{crd}\beta} < \frac{\alpha}{\beta}$ for $\alpha > \beta$) using inscribed triangles and circular sectors;
* Zenodorus and Pappus compare **tangents** to arcs ($\frac{\tan\alpha}{\tan\beta} > \frac{\alpha}{\beta}$ for $\frac{\pi}{2} > \alpha > \beta > 0$) by bounding circular sectors from inside and outside—without invoking any transcendental limit!

3. Sole Ancient Witness to the Thirteen Archimedean Solids (*Book V, Prop. 19*)
-------------------------------------------------------------------------------

Before proving spatial isoperimetric theorems for the sphere and five Platonic polyhedra (*Props. 20–43*), Pappus preserves in **Book V, Chapter 34 / Proposition 19** (*Hultsch I, pp. 352–358*) the **only surviving Greek list** of the **thirteen semi-regular convex polyhedra** (*τρισκαίδεκα σχήματα ἰσόπλευρα μὲν ἀλλʼ οὐχ ὁμοιοπρόσωπα*) discovered by :person:`Archimedes <archimedes>`:

* **Four 8-faced / 14-faced / 26-faced truncations & cuboctahedra**: truncated tetrahedron ($8$ faces: $4_3 + 4_6$), cuboctahedron ($14$ faces: $8_3 + 6_4$), truncated cube ($14$ faces: $8_3 + 6_8$), truncated octahedron ($14$ faces: $6_4 + 8_6$), rhombicuboctahedron ($26$ faces: $8_3 + 18_4$), and great rhombicuboctahedron ($26$ faces: $12_4 + 8_6 + 6_8$);
* **Icosahedral-dodecahedral family & snub solids**: icosidodecahedron ($32$ faces: $20_3 + 12_5$), truncated dodecahedron ($32$ faces: $20_3 + 12_{10}$), truncated icosahedron ($32$ faces: $12_5 + 20_6$), snub cube ($38$ faces: $32_3 + 6_4$), rhombicosidodecahedron ($62$ faces: $20_3 + 30_4 + 12_5$), great rhombicosidodecahedron ($62$ faces: $30_4 + 20_6 + 12_{10}$), and snub dodecahedron ($92$ faces: $80_3 + 12_5$).

Johannes Kepler (*Harmonices Mundi*, Book II, 1619) reconstructed all thirteen semi-regular polyhedra directly from Pappus's Book V face table via :cite:`Commandino's 1588 Latin edition <commandino:1588>`.
