:order: 7
:layout: book
:type: book
:title: Proposition 139 · Intersecting Carriers Summary
:canonical_id: Syn. VII.139.summary
:folio: 0278
:tracks: English: index | Greek: el | Summary: summary | Notes: notes

Proposition 139 · Intersecting Carriers Summary
===============================================

.. rubric:: Exact Symbolic Audit & ``geometor.pappus`` Verification

.. folio:: 0278
   :page: 1266

.. picture:: /_static/constructions/pappus_hexagon.svg
   :alt: Synagoge Book VII Proposition 139 — Pappus's General Intersecting-Carrier Hexagon Theorem

1. Vanishing Bracket Determinant
--------------------------------

Verified identically in :func:`geometor.pappus.verify_pappus_symbolic` over $\mathbb{Z}[a_0, a_1, a_2, b_0, b_1, b_2, u_x, u_y]$:

.. math::

   \det \begin{pmatrix} M_{01}^x & M_{01}^y & M_{01}^w \\ M_{20}^x & M_{20}^y & M_{20}^w \\ M_{12}^x & M_{12}^y & M_{12}^w \end{pmatrix} = 0.

2. The Six-Line Steiner Web ($S_3$)
-----------------------------------

.. picture:: /_static/constructions/pappus_steiner.svg
   :alt: Six S_3 Pappus Lines Concurring at Steiner Star Points S+ and S-

* The 3 even-permutation Pappus lines concur at :g:`S+ <g7:S1>`, the 3 odd-permutation lines concur at :g:`S- <g7:S2>`, connected by the **Steiner axis**.
