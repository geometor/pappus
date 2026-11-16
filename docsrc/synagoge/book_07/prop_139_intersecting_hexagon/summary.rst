:order: 6
:layout: book
:type: book
:title: 6. Proposition 139: Intersecting Carriers (Summary)
:canonical_id: Syn. VII.139
:excerpt: Mathematical formulation, symbolic determinant proof, and Steiner web properties for Pappus's general hexagon theorem (Synagoge VII.139).
:tracks: English: index | Greek: el | Summary: summary | Notes: notes

Summary: Proposition 139 · Intersecting Carriers
================================================

.. rubric:: Exact Symbolic Audit & ``geometor.pappus`` Verification

.. picture:: /_static/constructions/pappus_hexagon.svg
   :alt: Synagoge Book VII Proposition 139 — Pappus's General Intersecting-Carrier Hexagon Theorem

1. Vanishing Bracket Determinant
--------------------------------

Let $M_{01}, M_{20}, M_{12}$ be represented in homogeneous projective coordinates as 3-vectors. Their collinearity is equivalent to the vanishing of the $3 \times 3$ determinant:

.. math::

   \det \begin{pmatrix} M_{01}^x & M_{01}^y & M_{01}^w \\ M_{20}^x & M_{20}^y & M_{20}^w \\ M_{12}^x & M_{12}^y & M_{12}^w \end{pmatrix} = 0.

As implemented and tested in :func:`geometor.pappus.verify_pappus_symbolic`, this determinant evaluates to identically zero as an element of the polynomial ring $\mathbb{Z}[a_0, a_1, a_2, b_0, b_1, b_2, u_x, u_y]$.

2. The Six-Line Steiner Web ($S_3$)
-----------------------------------

.. picture:: /_static/constructions/pappus_steiner.svg
   :alt: Six S_3 Pappus Lines Concurring at Steiner Star Points S+ and S-

* The 6 permutations of $(B_0, B_1, B_2)$ give 6 distinct Pappus lines $p_\sigma$.
* The 3 lines corresponding to even permutations concur at the **even Steiner star point** :g:`S+ <g7:S1>`.
* The 3 lines corresponding to odd permutations concur at the **odd Steiner star point** :g:`S- <g7:S2>`.
* The line connecting $S_+$ and $S_-$ is the **Steiner axis**.
