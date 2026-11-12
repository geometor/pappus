:navigation: header
:order: 5
:layout: book
:book_title: Synagoge (Μαθηματικὴ Συναγωγή)
:book_subtitle: Pappus of Alexandria · Books III, IV, V, VII & VIII · Hultsch Greek, Original Translation & Exact Symbolic Synthesis

.. _synagoge-codex:

============================================================
Synagoge (*Μαθηματικὴ Συναγωγή*) — Multi-Track Book Codex
============================================================

.. rubric:: :person:`Pappus of Alexandria <pappus>` (fl. c. 320–340 CE) · Critical Greek Text (:person:`Friedrich Hultsch <hultsch>`, 1876–1878) · Original GEOMETOR English Translation · Exact ``SymPy`` / ``geometor.model`` Demonstrations

Around **340 CE** in Alexandria, :person:`Pappus <pappus>` gathered seven centuries of classical and Hellenistic geometry into his eight-book :term:`Synagoge <synagoge>` (*Mathematical Collection*). Far more than an encyclopedic compiler, Pappus repaired lost demonstrations, classified geometric problems into :term:`plane, solid, and linear loci <topos-epipedos-stereos-grammikos>`, generalized :person:`Euclid's <euclid>` Pythagorean area theorem to arbitrary parallelograms, proved the invariant altitude law of the :term:`arbelos <arbelos>` tangent circle chain, demonstrated the :term:`isoperimetric <isoperimetros>` optimality of the honeycomb, preserved the 33-book :term:`Treasury of Analysis <topos-analyomenos>` alongside the **Pappus–Guldinus Centroid Rule**, and established the **Cross-Ratio** and **Hexagon Collinearity Theorems** that birthed modern projective geometry.

Each treatise unit in this **Multi-Track Book Codex** synchronizes **four parallel tracks**:

1. **English** (``-en``) — Fresh, complete scholarly translation authored directly from :cite:`Hultsch's 1876–1878 <hultsch:1876>` critical Greek text, wired with interactive ``:g:`` vector diagrams.
2. **Greek (Hultsch 1876)** (``-el``) — Diplomatic polytonic Greek text from Weidmann Vols. I–III (:cite:`1876 <hultsch:1876>`, :cite:`1877 <hultsch:1877>`, :cite:`1878 <hultsch:1878>`), keyed by Hultsch page and proposition numbers and wired to the same interactive SVGs.
3. **Summary** (``-summary``) — Concise structural argument map, exact algebraic invariants, and ``geometor.pappus`` construction audit.
4. **Notes** (``-notes``) — Philological commentary, :cite:`Commandino (1588) <commandino:1588>` and :cite:`Heath (1921) <heath:1921>` reception notes, and cross-corpus links to ``euclid``, ``elements``, ``apollonius``, ``archimedes``, ``ptolemy``, ``proclus``, and ``hilbert``.

Conspectus Operis
-----------------

.. list-table::
   :header-rows: 1
   :widths: 16 42 20 22

   * - Book & Unit
     - Classical & Projective Propositions
     - Hultsch Locus
     - Parallel Tracks
   * - **Unit I · Book III**
     - Address to :person:`Pandrosion <pandrosion>`, Hierarchy of Plane / Solid / Linear Problems, Delian Two Mean Proportionals & **Arithmetic, Geometric, and Harmonic Means in a Single Semicircle** ($A \cdot H = G^2$)
     - Vol. I, pp. 30–84 (*Props. 1–5, 28–30*)
     - :doc:`EN <book-3-three-means/book-3-three-means-en>` · :doc:`EL <book-3-three-means/book-3-three-means-el>` · :doc:`Summary <book-3-three-means/book-3-three-means-summary>` · :doc:`Notes <book-3-three-means/book-3-three-means-notes>`
   * - **Unit II · Book IV**
     - **Pappus's Parallelogram Generalization of the Pythagorean Theorem** ($|\mathcal{P}_3| = |\mathcal{P}_1| + |\mathcal{P}_2|$) & **The Ancient Proposition on the Arbelos Tangent Circle Chain** ($y_n = n\,d_n$)
     - Vol. I, pp. 176–179, 208–232 (*Props. 1, 14–18*)
     - :doc:`EN <book-4-area-and-arbelos/book-4-area-and-arbelos-en>` · :doc:`EL <book-4-area-and-arbelos/book-4-area-and-arbelos-el>` · :doc:`Summary <book-4-area-and-arbelos/book-4-area-and-arbelos-summary>` · :doc:`Notes <book-4-area-and-arbelos/book-4-area-and-arbelos-notes>`
   * - **Unit III · Book V**
     - **On the Geometric Forethought of Bees** (*Περὶ τῆς τῶν μελισσῶν σοφίας*), Planar Tessellations ($n \in \{3,4,6\}$) & **Honeycomb Isoperimetric Theorem** ($A_6 : A_4 : A_3 = 3\sqrt{3} : 4 : 3$)
     - Vol. I, pp. 304–336 (*Preface & Props. 1–10*)
     - :doc:`EN <book-5-sagacity-of-bees/book-5-sagacity-of-bees-en>` · :doc:`EL <book-5-sagacity-of-bees/book-5-sagacity-of-bees-el>` · :doc:`Summary <book-5-sagacity-of-bees/book-5-sagacity-of-bees-summary>` · :doc:`Notes <book-5-sagacity-of-bees/book-5-sagacity-of-bees-notes>`
   * - **Unit IV · Book VII**
     - **The Treasury of Analysis** (*Τόπος ἀναλυόμενος*): Analysis vs. Synthesis, 33-Book Canon, Three-/Four-Line Locus, **Pappus–Guldinus Centroid Rule**, **Cross-Ratio Invariance** (*VII.129*) & **Hexagon Collinearity** (*VII.138–139*)
     - Vol. II, pp. 634–688, 868–894
     - :doc:`EN <book-7-domain-of-analysis/book-7-domain-of-analysis-en>` · :doc:`EL <book-7-domain-of-analysis/book-7-domain-of-analysis-el>` · :doc:`Summary <book-7-domain-of-analysis/book-7-domain-of-analysis-summary>` · :doc:`Notes <book-7-domain-of-analysis/book-7-domain-of-analysis-notes>`
   * - **Unit V · Book VIII**
     - **Architectonic Mechanics**, Centers of Gravity, the Inclined Plane (*VIII.9*), :person:`Archimedes's <archimedes>` Lever Saying & :person:`Hero's <heron>` :term:`Baroulkos <baroulkos>`, Single-Compass Constructions & **Seven Hexagons in a Circle** ($R = s_6\sqrt{7}$, *VIII.23*)
     - Vol. III, pp. 1022–1102 (*Props. 1–19, 23*)
     - :doc:`EN <book-8-mechanics/book-8-mechanics-en>` · :doc:`EL <book-8-mechanics/book-8-mechanics-el>` · :doc:`Summary <book-8-mechanics/book-8-mechanics-summary>` · :doc:`Notes <book-8-mechanics/book-8-mechanics-notes>`

Editorial & Translation Provenance
----------------------------------

* **Primary Greek Edition** — :cite:`Friedrich Hultsch <hultsch:1876>`, *Pappi Alexandrini Collectionis quae supersunt*, 3 vols., Berlin: Weidmann, 1876–1878 (*Public Domain*; established from *Codex Vaticanus Graecus* 218).
* **Renaissance Latin Editio Princeps** — :cite:`Federico Commandino <commandino:1588>`, *Pappi Alexandrini Mathematicae Collectiones*, Pesaro: Hieronymus Concordia, 1588 (*Public Domain*).
* **Public-Domain Historical Commentary** — :cite:`Sir Thomas Little Heath <heath:1921>`, *A History of Greek Mathematics*, Vol. II, Ch. XIX (*Pappus of Alexandria*, pp. 355–439), Oxford: Clarendon Press, 1921 (*Public Domain*).
* **100% Original English Translation** — Every English ``-en`` track in this codex is translated freshly from Hultsch's Greek text by **GEOMETOR**; no copyrighted modern translations (*Jones 1986, Cuomo 2000, Sefrin-Weis 2010, Ver Eecke 1933*) are reproduced.

Scholarly Apparatus
-------------------

* :doc:`concordance` — Bidirectional mapping across Hultsch pagination, sister **GEOMETOR** codices, and ``geometor.pappus`` symbolic modules.
* :doc:`bibliography` — Critical editions, ancient treatises of the *Treasury of Analysis*, and modern projective literature.
* :doc:`persons` — *Index Nominum* of classical, Hellenistic, late-antique, and modern geometers.
* :doc:`glossary` — Polytonic Greek & Latin technical mathematical lexicon.

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Treatise Units

   book-3-three-means/book-3-three-means-en
   book-3-three-means/book-3-three-means-el
   book-3-three-means/book-3-three-means-summary
   book-3-three-means/book-3-three-means-notes
   book-4-area-and-arbelos/book-4-area-and-arbelos-en
   book-4-area-and-arbelos/book-4-area-and-arbelos-el
   book-4-area-and-arbelos/book-4-area-and-arbelos-summary
   book-4-area-and-arbelos/book-4-area-and-arbelos-notes
   book-5-sagacity-of-bees/book-5-sagacity-of-bees-en
   book-5-sagacity-of-bees/book-5-sagacity-of-bees-el
   book-5-sagacity-of-bees/book-5-sagacity-of-bees-summary
   book-5-sagacity-of-bees/book-5-sagacity-of-bees-notes
   book-7-domain-of-analysis/book-7-domain-of-analysis-en
   book-7-domain-of-analysis/book-7-domain-of-analysis-el
   book-7-domain-of-analysis/book-7-domain-of-analysis-summary
   book-7-domain-of-analysis/book-7-domain-of-analysis-notes
   book-8-mechanics/book-8-mechanics-en
   book-8-mechanics/book-8-mechanics-el
   book-8-mechanics/book-8-mechanics-summary
   book-8-mechanics/book-8-mechanics-notes

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Apparatus

   concordance
   bibliography
   persons
   glossary
