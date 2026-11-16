:order: 6
:layout: book
:type: book
:title: 6. Proposition 139: Pappus's General Hexagon Collinearity Theorem
:canonical_id: Syn. VII.139
:excerpt: Lemma XIII to Euclid's Porisms: the celebrated general Pappus Hexagon Theorem on two intersecting carrier lines, generating the 6-line S_3 Steiner configuration.
:tracks: English: index | Greek: el | Summary: summary | Notes: notes

.. _sec-b7-en-hexagon-theorems:

Proposition 139: Pappus's General Hexagon Collinearity Theorem
==============================================================

.. rubric:: *Synagoge* Book VII, Proposition 139 (:cite:`Hultsch II, pp. 886–889 <hultsch:1877>`, Lemma XIII to Euclid's *Porisms*) · Critical English Edition

Crowning the lemmas to Euclid's *Porisms* is **Proposition 139**, the general theorem of collinearity for opposite sides of a hexagon whose vertices lie alternately on two intersecting carrier lines. Pappus establishes the result purely through compound ratios (cross-ratio invariance) without drawing a single circle.

.. picture:: /_static/constructions/pappus_hexagon.svg
   :alt: Synagoge Book VII Proposition 139 — Pappus's General Intersecting-Carrier Hexagon Theorem

.. enunciation::

   **Proposition 139 (Hultsch II, pp. 886–889)**: Let two straight lines :g:`a <g1:[ A0 A2 ]>` and :g:`b <g1:[ B0 B2 ]>` meet at :g:`O <g1:O>`, carrying three points :g:`A0 <g1:A0>`, :g:`A1 <g1:A1>`, :g:`A2 <g1:A2>` on :g:`a <g1:[ A0 A2 ]>` and three points :g:`B0 <g1:B0>`, :g:`B1 <g1:B1>`, :g:`B2 <g1:B2>` on :g:`b <g1:[ B0 B2 ]>`. If opposite cross-joins :g:`A0B1 <g1:[ A0 B1 ]>` & :g:`A1B0 <g1:[ A1 B0 ]>` meet at :g:`M01 <g1:M01>`, :g:`A2B0 <g1:[ A2 B0 ]>` & :g:`A0B2 <g1:[ A0 B2 ]>` meet at :g:`M20 <g1:M20>`, and :g:`A1B2 <g1:[ A1 B2 ]>` & :g:`A2B1 <g1:[ A2 B1 ]>` meet at :g:`M12 <g1:M12>`, then the three points :g:`M01 <g1:M01>`, :g:`M20 <g1:M20>`, and :g:`M12 <g1:M12>` **lie on a single straight line** :g:`p <g1:[ M01 M12 ]>`.

.. step::

   Set carrier :g:`a <g1:[ A0 A2 ]>` with :g:`A0 <g1:A0>` $= (0, 0)$, :g:`A1 <g1:A1>` $= (2, 0)$, :g:`A2 <g1:A2>` $= (5, 0)$ and carrier :g:`b <g1:[ B0 B2 ]>` with :g:`B0 <g1:B0>` $= (0, 2)$, :g:`B1 <g1:B1>` $= (2, 3)$, :g:`B2 <g1:B2>` $= (6, 5)$, concurring at perspective apex :g:`O <g1:O>` $= (-4, 0)$.

.. step::

   Form the three opposite cross-join intersections of hexagon :g:`A0B1A2B0A1B2 <g1:< A0 B1 A2 B0 A1 B2 >>`:

   .. math::

      M_{01} = \left(\frac{4}{5}, \frac{6}{5}\right), \qquad
      M_{20} = \left(\frac{60}{37}, \frac{50}{37}\right), \qquad
      M_{12} = \left(\frac{10}{3}, \frac{5}{3}\right).

.. step::

   By **Proposition 129**, projecting from :g:`A0 <g1:A0>` and :g:`A2 <g1:A2>` onto cross-joins :g:`A1B0 <g1:[ A1 B0 ]>` and :g:`A1B2 <g1:[ A1 B2 ]>` equates their four-point cross-ratios; since the two ranges share their apex :g:`A1 <g1:A1>`, the joins connecting corresponding points concur, forcing :g:`M01 <g1:M01>`, :g:`M20 <g1:M20>`, and :g:`M12 <g1:M12>` onto the single **Pappus line** :g:`p <g1:[ M01 M12 ]>` ($-7x + 38y = 40$).

Permuting $(B_0, B_1, B_2)$ across all $3! = 6$ elements of $S_3$ (:func:`~geometor.pappus.construct_pappus_configuration`) yields **six Pappus lines** that concur three-by-three by parity at :person:`Jakob Steiner's <steiner>` **Star points** :g:`S+ <g7:S1>` and :g:`S- <g7:S2>` along :g:`Steiner line <g7:[ S1 S2 ]>`:

.. picture:: /_static/constructions/pappus_steiner.svg
   :alt: Six S_3 Pappus Lines Concurring at Steiner Star Points S+ and S-
