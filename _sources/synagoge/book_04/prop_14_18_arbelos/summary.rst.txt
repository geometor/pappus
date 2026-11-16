:layout: book
:type: book
:title: Arbelos Circle Chain · Exact Symbolic Invariants
:canonical_id: Syn. IV.14-18.summary
:tracks: English: index | Greek: el | Summary: summary | Notes: notes

Arbelos Circle Chain · Exact Symbolic Invariants
================================================

.. rubric:: Recurrence Relations & Focal Ellipse

1. The Altitude Law & Inductive Recurrence
------------------------------------------

* Base circle $C_1$: $y_1 = d_1 = 2\,r_1^{(c)}$.
* Recurrence step from Lemma 3 (*Prop. 17*):

  .. math::

     \frac{y_{n+1}}{d_{n+1}} = \frac{y_n}{d_n} + 1 \implies \frac{y_n}{d_n} = n.

* Perpendicular height equals $n$ times diameter: $y_n = n\,d_n = 2n\,r_n$.

2. Exact Rational Coordinates for $(r_1, r_2) = (2, 1)$
-------------------------------------------------------

Constructed in :func:`geometor.pappus.construct_pappus_arbelos_chain`:

* $C_1$: center $\left(\frac{30}{7}, \frac{12}{7}\right)$, diameter $d_1 = \frac{12}{7}$, altitude $y_1 = \frac{12}{7} = 1 \cdot d_1$.
* $C_2$: center $\left(3, \frac{12}{5}\right)$, diameter $d_2 = \frac{6}{5}$, altitude $y_2 = \frac{12}{5} = 2 \cdot d_2$.
* $C_3$: center $\left(2, \frac{12}{5}\right)$, diameter $d_3 = \frac{4}{5}$, altitude $y_3 = \frac{12}{5} = 3 \cdot d_3$.
* $C_4$: center $\left(\frac{15}{11}, \frac{24}{11}\right)$, diameter $d_4 = \frac{6}{11}$, altitude $y_4 = \frac{24}{11} = 4 \cdot d_4$.

3. Focal Locus Ellipse
----------------------

Every center $K_n$ satisfies $|K_n O_0| + |K_n O_1| = (R - r_n) + (r_1 + r_n) = R + r_1 = 5$, establishing that all circle centers lie on a fixed ellipse whose foci are the centers of the outer semicircle $O_0$ and the left inner semicircle $O_1$.
