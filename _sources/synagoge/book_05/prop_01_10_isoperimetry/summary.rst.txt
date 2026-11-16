:layout: book
:type: book
:title: Planar Isoperimetric Chain · Symbolic Invariants & Apothem Ordering
:canonical_id: Syn. V.1-10.summary
:tracks: English: index | Greek: el | Summary: summary | Notes: notes

Planar Isoperimetric Chain · Symbolic Invariants & Apothem Ordering
===================================================================

.. rubric:: Apothem Growth & Extremal Limits

1. Apothem Formula for Perimeter $P$
------------------------------------

For a regular $n$-gon of perimeter $P$, the side length is $s_n = P/n$ and the apothem is:

.. math::

   a_n = \frac{P}{2n \tan(\pi / n)}.

Because the function $f(x) = x \tan(\pi / x)$ is strictly decreasing for $x \ge 3$, the apothem $a_n$ is strictly increasing with $n$, converging in the limit to the circle's radius $R = P / (2\pi)$:

.. math::

   a_3 = \frac{P}{6\sqrt{3}} < a_4 = \frac{P}{8} < a_6 = \frac{P}{4\sqrt{3}} < \dots < R = \frac{P}{2\pi}.

2. Symbolic Verification in ``geometor.pappus``
-----------------------------------------------

Computed in :func:`geometor.pappus.verify_honeycomb_isoperimetry` with $P = 12$:

* $A_3 = 4\sqrt{3}$
* $A_4 = 9$
* $A_6 = 6\sqrt{3}$
* Ratios: $\frac{A_6}{A_3} = \frac{3}{2}$, $\frac{A_6}{A_4} = \frac{2\sqrt{3}}{3}$, $\frac{A_4}{A_3} = \frac{3\sqrt{3}}{4}$.
* Circumradius of seven surrounding hexagons: $R = s_6\sqrt{7} = 2\sqrt{7}$.
