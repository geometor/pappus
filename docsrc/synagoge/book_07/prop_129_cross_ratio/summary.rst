:order: 4
:layout: book
:type: book
:title: Proposition 129 · Cross-Ratio Invariance Summary
:canonical_id: Syn. VII.129.summary
:folio: hultsch_1877_vol2:0416
:tracks: English: index | Greek: el | Summary: summary | Notes: notes

Proposition 129 · Cross-Ratio Invariance Summary
================================================

.. rubric:: Exact Symbolic Audit & ``geometor.pappus`` Verification

.. folio:: hultsch_1877_vol2:0416
   :page: 870

1. Definition of the Cross-Ratio
--------------------------------

.. math::

   \operatorname{CR}(A, B; C, D) = \frac{(A - C)(B - D)}{(A - D)(B - C)} = \frac{AC \cdot BD}{AD \cdot BC}.

2. Central Projection Invariance
--------------------------------

Under any central projection from apex :math:`O` mapping collinear points :math:`A, B, C, D` onto :math:`A', B', C', D'`, :math:`\operatorname{CR}(A, B; C, D) = \operatorname{CR}(A', B'; C', D')`, verified identically in :func:`geometor.pappus.cross_ratio` and :func:`geometor.pappus.project_point`.

In Pappus's notation (Chs. 196–197), the pencil apex is :math:`\Theta` (or :math:`A` with rays :math:`AB, \Gamma A, \Delta A` cut by :math:`\Theta E` and :math:`\Theta\Delta`), yielding the invariant rectangle ratio :math:`\Theta E \cdot HZ : \Theta H \cdot ZE = \Theta B \cdot \Delta\Gamma : \Theta\Delta \cdot B\Gamma`.
