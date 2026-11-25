:order: 7
:layout: book
:type: book
:title: Proposition 139 · Intersecting Carriers Summary
:canonical_id: Syn. VII.139.summary
:folio: hultsch_1877_vol2:0432
:tracks: English: index | Greek: el | Summary: summary | Notes: notes

Proposition 139 · Intersecting Carriers Summary
===============================================

.. rubric:: Exact Symbolic Audit & ``geometor.pappus`` Verification

.. folio:: hultsch_1877_vol2:0432
   :page: 886

.. picture:: /_static/constructions/pappus_hexagon.svg
   :alt: Synagoge Book VII Proposition 139 — Pappus's General Intersecting-Carrier Hexagon Theorem

1. Vanishing Bracket Determinant & Cross-Ratio Proof
----------------------------------------------------

In Pappus's Ch. 207 (:math:`AB, \Gamma\Delta` meeting at :math:`N`), applying Lemma III (Prop. 129) from :math:`\Gamma` and from :math:`\Delta` equates the compound rectangle ratios along :math:`\Gamma M\Lambda` and :math:`\Delta M\Theta`, reducing collinearity of :math:`H, M, K` to Lemma X.

Verified identically in :func:`geometor.pappus.verify_pappus_symbolic` over :math:`\mathbb{Z}[a_0, a_1, a_2, b_0, b_1, b_2, u_x, u_y]`:

.. math::

   \det \begin{pmatrix} M_{01}^x & M_{01}^y & M_{01}^w \\ M_{20}^x & M_{20}^y & M_{20}^w \\ M_{12}^x & M_{12}^y & M_{12}^w \end{pmatrix} = 0.

For canonical carriers :math:`A_0 = (0, 0), A_1 = (2, 0), A_2 = (5, 0)` and :math:`B_0 = (0, 2), B_1 = (2, 3), B_2 = (6, 5)` meeting at :math:`O = (-4, 0)`, the intersections :math:`M_{01} = \left(\frac{4}{5}, \frac{6}{5}\right)`, :math:`M_{20} = \left(\frac{60}{37}, \frac{50}{37}\right)`, and :math:`M_{12} = \left(\frac{10}{3}, \frac{5}{3}\right)` lie on :math:`-7x + 38y = 40`.

2. The Six-Line Steiner Web (:math:`S_3`)
-----------------------------------------

.. picture:: /_static/constructions/pappus_steiner.svg
   :alt: Six S_3 Pappus Lines Concurring at Steiner Star Points S+ and S-

* Permuting :math:`(B_0, B_1, B_2)` across all :math:`3! = 6` elements of :math:`S_3` (:func:`geometor.pappus.construct_pappus_configuration`) yields six Pappus lines: the 3 even-permutation lines concur at :g:`S+ <g7:S1>`, the 3 odd-permutation lines concur at :g:`S- <g7:S2>`, connected by the **Steiner axis** :g:`Steiner line <g7:[ S1 S2 ]>`.
