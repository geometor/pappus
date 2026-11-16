:order: 3
:layout: book
:type: book
:title: 3. Proposition 129: Cross-Ratio Invariance (Summary)
:canonical_id: Syn. VII.129
:excerpt: Mathematical formulation and symbolic verification of cross-ratio invariance under central projection (Synagoge VII.129).
:tracks: English: index | Greek: el | Summary: summary | Notes: notes

Summary: Proposition 129 · Cross-Ratio Invariance
=================================================

.. rubric:: Exact Symbolic Audit & ``geometor.pappus`` Verification

1. Definition of the Cross-Ratio
--------------------------------

For four collinear points $A, B, C, D$, their cross-ratio (or double ratio) is defined as:

.. math::

   \operatorname{CR}(A, B; C, D) = \frac{(A - C)(B - D)}{(A - D)(B - C)} = \frac{AC \cdot BD}{AD \cdot BC}.

2. Central Projection Invariance
--------------------------------

Let $O$ be a center of perspectivity. Under any central projection from $O$ mapping collinear points $A, B, C, D$ on transversal line $L$ to points $A', B', C', D'$ on transversal line $L'$:

.. math::

   \operatorname{CR}(A, B; C, D) = \operatorname{CR}(A', B'; C', D').

Implemented and symbolically verified in :func:`geometor.pappus.cross_ratio` and :func:`geometor.pappus.project_point`: the rational cross-ratio invariant holds identically over arbitrary symbolic coordinates without rounding or approximation.
