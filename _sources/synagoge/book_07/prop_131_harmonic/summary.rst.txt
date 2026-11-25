:order: 5
:layout: book
:type: book
:title: Proposition 131 · Harmonic Conjugates Summary
:canonical_id: Syn. VII.131.summary
:folio: hultsch_1877_vol2:0420
:tracks: English: index | Greek: el | Summary: summary | Notes: notes

Proposition 131 · Harmonic Conjugates Summary
=============================================

.. rubric:: Exact Symbolic Audit & ``geometor.pappus`` Verification

.. folio:: hultsch_1877_vol2:0420
   :page: 874

.. picture:: /_static/constructions/harmonic_fourth.svg
   :alt: Complete Quadrilateral Straightedge Construction of Fourth Harmonic Conjugate D (Synagoge VII.131)

1. The Fourth Harmonic Conjugate
--------------------------------

.. math::

   \operatorname{CR}(A, B; C, D) = \frac{(A - C)(B - D)}{(A - D)(B - C)} = -1 \quad \Longrightarrow \quad D = \frac{2AB - C(A + B)}{2C - (A + B)}.

In Pappus's Ch. 199 (:math:`\operatorname{Prop. 131}`), the harmonic hypothesis :math:`A\Delta : \Delta\Gamma = AB : B\Gamma` forces collinearity of the transversal :math:`AH\Theta` across the complete quadrilateral.

2. Straightedge Construction & 81 Harmonic Tetrads
--------------------------------------------------

Implemented in :func:`geometor.pappus.construct_harmonic_fourth`: generates **81 collinear harmonic ranges** across the complete 9-point, 9-line Pappus–Steiner network by straightedge alone.
