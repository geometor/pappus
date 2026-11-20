:order: 4
:layout: book
:type: book
:title: Proposition 129 · Cross-Ratio Invariance Summary
:canonical_id: Syn. VII.129.summary
:folio: 0275
:tracks: English: index | Greek: el | Summary: summary | Notes: notes

Proposition 129 · Cross-Ratio Invariance Summary
================================================

.. rubric:: Exact Symbolic Audit & ``geometor.pappus`` Verification

.. folio:: 0275
   :page: 1263

1. Definition of the Cross-Ratio
--------------------------------

.. math::

   \operatorname{CR}(A, B; C, D) = \frac{(A - C)(B - D)}{(A - D)(B - C)} = \frac{AC \cdot BD}{AD \cdot BC}.

2. Central Projection Invariance
--------------------------------

Under any central projection from apex $O$ mapping collinear points $A, B, C, D$ onto $A', B', C', D'$, $\operatorname{CR}(A, B; C, D) = \operatorname{CR}(A', B'; C', D')$, verified identically in :func:`geometor.pappus.cross_ratio` and :func:`geometor.pappus.project_point`.
