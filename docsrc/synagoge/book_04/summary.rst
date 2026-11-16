:layout: book
:title: Book IV · Analytical Summary & Invariant Audit
:order: 90

.. _synagoge-b4-summary:

====================================================================================
Book IV · Summary & Exact Symbolic Audit (*Area Theorem & Arbelos Circle Chain*)
====================================================================================

.. rubric:: Structural Decomposition & Symbolic Verification

1. Pappus's Parallelogram Area Theorem (*Prop. 1, Hultsch I pp. 176–179*)
-------------------------------------------------------------------------

Given any triangle $ABC$ and arbitrary parallelograms $ABDE$ and $ACFG$ erected outward on sides $AB$ and $AC$:

* Outer sides $DE$ and $FG$ intersect at apex $H$.
* Transversal vector $\vec{v} = A - H$ defines base parallelogram $BCML$ on side $BC$ with edges $BL = CM = \vec{v}$.
* **Area Invariant**: $\operatorname{Area}(BCML) = \operatorname{Area}(ABDE) + \operatorname{Area}(ACFG)$ holds identically across all 10 coordinates in the polynomial ring $\mathbb{Z}[x_A, y_A, x_B, y_B, x_C, y_C, u_1, v_1, u_2, v_2]$ without square roots or trig functions.
* When $\angle BAC = 90^\circ$ and erected parallelograms are squares, the theorem reduces identically to :cite:`Euclid Elements I.47 <euclid:elements>`.

2. The Ancient Arbelos Circle Chain Theorem (*Props. 14–18, Hultsch I pp. 208–232*)
-----------------------------------------------------------------------------------

Given outer semicircle of radius $R = r_1 + r_2$ divided into inner semicircles of radii $r_1$ and $r_2$:

* Chain of mutually tangent circles $C_n$ ($n = 1, 2, 3, \dots$) inscribed in the :term:`arbelos <arbelos>`.
* **Altitude Law**: $y_n = n\,d_n = 2n\,r_n$ for every $n \ge 1$.
* **Center Coordinates**: $x_n = \frac{r_1 r_2 (r_1 + r_2)}{r_1 r_2 + n^2 (r_1 + r_2)^2} \dots$
* **Focal Locus**: Every center $K_n$ lies on the fixed ellipse with foci at the centers of the outer semicircle and the first inner semicircle, with major axis $2a = R + r_1$.
