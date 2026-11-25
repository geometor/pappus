:order: 6
:layout: book
:type: book
:title: Proposition 138 · Parallel Hexagon Summary
:canonical_id: Syn. VII.138.summary
:folio: hultsch_1877_vol2:0430
:tracks: English: index | Greek: el | Summary: summary | Notes: notes

Proposition 138 · Parallel Hexagon Summary
==========================================

.. rubric:: Exact Symbolic Audit & ``geometor.pappus`` Verification

.. folio:: hultsch_1877_vol2:0430
   :page: 884

.. picture:: /_static/constructions/pappus_parallel_steiner.svg
   :alt: Synagoge Book VII Proposition 138 — Parallel Carriers and Even Steiner Point S+ = (90/73, 38/73)

* When carriers :math:`a \parallel b` (:math:`AB \parallel \Gamma\Delta` in Ch. 206), their intersection :math:`O` lies at infinity (:math:`O \to \infty`).
* Pappus applies the preceding triangle-transversal lemma (Ch. 205 / Prop. 137) twice to :math:`\triangle \Delta AZ` and :math:`\triangle \Gamma BZ`, equating the compound rectangle ratios along :math:`\Gamma M\Lambda` and :math:`\Delta M\Theta`, which by Lemma X forces :math:`H, M, K` onto one straight line.
* All three cross-join intersections :math:`M_{01}, M_{20}, M_{12}` lie on a Pappus line parallel to :math:`a` and :math:`b`, concurring across even permutations at :math:`S^+ = \left(\frac{90}{73}, \frac{38}{73}\right)` in :func:`geometor.pappus.construct_pappus_configuration`.
