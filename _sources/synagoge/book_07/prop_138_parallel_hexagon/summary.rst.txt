:order: 5
:layout: book
:type: book
:title: 5. Proposition 138: Parallel Hexagon (Summary)
:canonical_id: Syn. VII.138
:excerpt: Mathematical formulation and symbolic verification of Pappus's hexagon on parallel carriers (Synagoge VII.138).
:tracks: English: index | Greek: el | Summary: summary | Notes: notes

Summary: Proposition 138 · Parallel Carriers
============================================

.. rubric:: Exact Symbolic Audit & ``geometor.pappus`` Verification

.. picture:: /_static/constructions/pappus_parallel_steiner.svg
   :alt: Synagoge Book VII Proposition 138 — Parallel Carriers and Even Steiner Point S+ = (90/73, 38/73)

1. Affine Degeneration of Pappus's Hexagon
------------------------------------------

When the two carriers $a$ and $b$ are parallel, their projective intersection point $O$ recedes to the ideal point at infinity ($O \to \infty$). The Pappus collinearity persists:

* The three cross-joins $M_{01}, M_{20}, M_{12}$ remain collinear on the line $p$.
* Furthermore, $p$ is strictly parallel to $a$ and $b$.

2. Steiner Star Point Concurrency
---------------------------------

Across the three even permutations of the vertices on carrier $b$, the three corresponding Pappus lines concur at the **even Steiner star point**:

.. math::

   S^+ = \left(\frac{90}{73}, \frac{38}{73}\right)

verified symbolically in :func:`geometor.pappus.construct_pappus_configuration` with exact rational coordinates.
