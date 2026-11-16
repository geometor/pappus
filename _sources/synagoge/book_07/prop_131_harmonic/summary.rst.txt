:order: 4
:layout: book
:type: book
:title: 4. Proposition 131: Harmonic Conjugates (Summary)
:canonical_id: Syn. VII.131
:excerpt: Mathematical formulation and symbolic verification of complete quadrilateral harmonic division (Synagoge VII.131).
:tracks: English: index | Greek: el | Summary: summary | Notes: notes

Summary: Proposition 131 · Harmonic Conjugates
==============================================

.. rubric:: Exact Symbolic Audit & ``geometor.pappus`` Verification

.. picture:: /_static/constructions/harmonic_fourth.svg
   :alt: Complete Quadrilateral Straightedge Construction of Fourth Harmonic Conjugate D (Synagoge VII.131)

1. The Fourth Harmonic Conjugate
--------------------------------

Given three distinct collinear points $A, B, C$, their fourth harmonic conjugate $D$ satisfies:

.. math::

   \operatorname{CR}(A, B; C, D) = \frac{(A - C)(B - D)}{(A - D)(B - C)} = -1.

Solving for $D$ gives the exact rational formula:

.. math::

   D = \frac{2AB - C(A + B)}{2C - (A + B)}.

2. Straightedge Construction & 81 Harmonic Tetrads
--------------------------------------------------

* Implemented in :func:`geometor.pappus.construct_harmonic_fourth`: constructs the point $D$ using an auxiliary complete quadrilateral by ruler alone, with zero measurement of angles or distances.
* In the full 9-point, 9-line Pappus–Steiner configuration, the cross-joins and diagonals create exactly **81 collinear harmonic ranges** across the complete network of intersection points.
