:navigation: header
:order: 20
:nav_title: About

.. _about:
.. _about-index:

About
=====

.. rubric:: Extracting Historical Semantic Knowledge & Repurposing It for Exact Symbolic Reasoning

About This Edition
------------------

``geometor.pappus`` establishes a definitive Digital Scriptorium edition and symbolic computational synthesis of **Pappus of Alexandria's** (*c.* 340 CE) *Synagoge* (*Μαθηματικὴ Συναγωγή*, *Mathematical Collection*). Compiled during the twilight of ancient Greek geometry, the *Synagoge* constitutes the primary surviving compendium of classical Hellenistic mathematics. Across eight books, Pappus preserved the methods of lost masterpieces by Euclid, Apollonius, and Aristaeus, while advancing groundbreaking discoveries in solid and linear loci, isoperimetric optimization, and mechanical synthesis.

This edition extracts the implicit deductive architecture of the *Synagoge* into addressable semantic elements across five synchronized codex units: Book III (the classical problem hierarchy and three means inside a single semicircle); Book IV (Pappus's generalization of Euclid's area theorem and the infinite *arbelos* circle chain :math:`y_n = n \cdot d_n`); Book V (the isoperimetric optimality of the bees' hexagonal honeycomb and Archimedean semiregular polyhedra); Book VII (the *Treasury of Analysis*, Pappus–Guldinus centroid rules, anharmonic cross-ratio invariance, and the foundational **Pappus Hexagon Theorem**); and Book VIII (Alexandrian mechanics, Hero's *Baroulkos*, and toothed gear kinematics).

At the core of ``geometor.pappus`` is the formalization of Book VII's projective incidence geometry. Long before Desargues, Pascal, and Poncelet, Pappus discovered that collinear triples on intersecting lines determine collinear cross-join intersections (Props. 138–139). We model these configurations as exact directed acyclic graphs in ``geometor.model``, tracing the symmetric group :math:`S_3` actions on collinear triples, the 18 cross-join meets, the six Pappus lines, the parity decomposition into :math:`A_3` and :math:`S_3 \setminus A_3`, and Jakob Steiner's two Star concurrency points :math:`(S_+, S_-)`. This connects directly across the GEOMETOR ecosystem to Euclid's *Elements* (:external+elements:doc:`index`), Menelaus of Alexandria's spherical transversals (``geometor.menelaus``), the modern triangle centers of Kimberling (``geometor.etc``), and the quantitative operational calculus of Émile Lemoine's *Géométrographie* (``geometor.lemoine``).

The GEOMETOR Mission
--------------------

The GEOMETOR project, conceived and directed by **phi ARCHITECT**, is dedicated to a multi-generational synthesis of geometry, computation, and symbolic reasoning. At its core, the project operates across three foundational pillars:

Extracting Historical Semantic Knowledge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Moving beyond passive page scans and superficial OCR, GEOMETOR recovers the living deductive architecture of more than 2,300 years of geometric, axiomatic, and philosophical treatises. From ancient Greek codices and Renaissance folios to nineteenth-century synthetic treatises, our Digital Scriptorium elevates prose, marginal citations, primary-source folios (via ``publish folio``), and calibrated Ink-to-Vector ``.euclid-graphic`` diagrams into structured, machine-addressable semantic knowledge graphs. Every proposition, step, enunciation, and justification is isolated, verified, and interconnected across history.

Exact Symbolic Grounding (``geometor.model``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Geometry in GEOMETOR is never approximated through floating-point fuzz or numerical instability. Constructions are anchored in 100% exact symbolic algebra via `SymPy` and Norman Wildberger's Rational Trigonometry invariants (quadrance, spread, and cross-ratio) over exact algebraic number fields. By eliminating rounding errors entirely, geometric configurations retain absolute fidelity, allowing geometric proofs, collinearities, and concyclicities to be verified symbolically with mathematical certainty.

Repurposing Knowledge Across Mediums
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The extracted semantic graphs and exact algebraic models are re-deployed across a unified computational medium: synchronized multi-track **Book Codices** and EPUB 3 editions published with `photon-platform/publish`; computable deductive canons (such as ``geometor.elements``, ``geometor.etc``, ``geometor.pappus``, and ``geometor.divine``); interactive SVG laboratories powered by ``geometor.explorer``; ultra-high-definition (QHD) visual broadcasts; and neuro-symbolic program synthesis guided by ``geometor.seer`` across `geometor.com <https://geometor.com>`_.

Sources, Provenance & Methodology
---------------------------------

The textual transmission of Pappus's *Synagoge* relies on a narrow manuscript tradition descending almost exclusively from the ninth/tenth-century *Codex Vaticanus Graecus* 218. This digital edition builds upon the following primary witnesses and classical scholarship:

* **Friedrich Hultsch**, *Pappi Alexandrini Collectionis quae supersunt* (3 vols., Berlin: Weidmann, 1876–1878; CTS URN ``urn:cts:greekLit:tlg2032.tlg001.1st1K-grc1``), providing the definitive critical polytonic Greek text and parallel Latin translation.
* **Federico Commandino**, *Pappi Alexandrini Mathematicae Collectiones a Federico Commandino Urbinate in Latinum conversae* (Pesaro: Hieronymus Concordia, 1588), the historic Renaissance *editio princeps* that inspired Descartes, Kepler, Fermat, Desargues, Pascal, and Newton.
* **Sir Thomas Little Heath**, *A History of Greek Mathematics*, Vol. II: *From Aristarchus to Diophantus* (Oxford: Clarendon Press, 1921, Chapter XIX: Pappus of Alexandria, pp. 355–439).
* **Alexander Jones**, *Book 7 of the Collection* (2 vols., New York: Springer-Verlag, 1986), offering essential modern historical and philological commentary on the *Treasury of Analysis*.

All constructions are verified through 100% exact symbolic DAG computations in ``geometor.model`` and rendered with interactive dark/light-aware ``.euclid-graphic`` SVG diagrams.
