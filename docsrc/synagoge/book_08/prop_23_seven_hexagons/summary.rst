:order: 3
:layout: book
:type: book
:title: 3. Proposition 23: Seven Hexagons (Summary)
:canonical_id: Syn. VIII.23
:folio: 0107
:excerpt: Exact symbolic verification of Proposition 23 circumradius R^2 = 7 s_6^2 over Q(sqrt(3), sqrt(7)).
:tracks: English: index | Greek: el | Summary: summary | Notes: notes

Summary: Proposition 23 · Seven Hexagons in a Circle
====================================================

.. rubric:: Exact Symbolic Audit & ``geometor.pappus`` Verification

.. picture:: /_static/constructions/honeycomb_isoperimetry.svg
   :alt: Synagoge Book VIII Proposition 23 — Seven Regular Hexagons Inscribed in a Circle

1. Derivation of the Radius Invariant via Euclid II.12
------------------------------------------------------

In any triangle with sides $a = s_6$, $b = 2s_6$ and included angle $120^\circ$, Euclid :just:`II.12` yields:

.. math::

   R^2 = a^2 + b^2 + 2ab \cos(180^\circ - 120^\circ) = s_6^2 + 4s_6^2 + 2(s_6)(2s_6)\left(\frac{1}{2}\right) = 7\,s_6^2.

2. Symbolic Verification in ``geometor.pappus``
-----------------------------------------------

* Verified in :func:`geometor.pappus.construct_honeycomb_isoperimetry` and :func:`geometor.pappus.verify_honeycomb_isoperimetry`.
* In the canonical perimeter $P = 12$ model, $s_6 = 2$, and the circumradius is:

  .. math::

     R_7 = 2\sqrt{7} \approx 5.291502622...

* All 12 outer vertices have exact quadrance $Q(H_0, V) = 28$ from the center $H_0$, with zero floating-point approximation.
