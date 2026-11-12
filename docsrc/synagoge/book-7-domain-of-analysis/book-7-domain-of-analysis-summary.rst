.. _synagoge-b7-summary:

===============================================================================
Book VII · Summary & Exact Symbolic Audit (*Analysis, Cross-Ratio & Hexagon*)
===============================================================================

.. rubric:: Structural Argument Map & ``geometor.pappus`` Symbolic Verification

1. Epistemological & Analytical Pillars (*Hultsch II, pp. 634–688*)
-------------------------------------------------------------------

* **Analysis ($\alpha\nu\alpha\lambda\upsilon\sigma\iota\varsigma$) vs. Synthesis ($\sigma\upsilon\nu\theta\varepsilon\sigma\iota\varsigma$)**: Backward heuristic resolution from the assumed target to first principles vs. forward deductive composition; split into **theoretical** (*zetetic*) and **problematic** (*poristic* + :term:`diorismos <diorismos>`).
* **The 33-Book Curriculum**: 1 book *Data*, 12 books of Apollonian ratio/area/tangency/inclination/plane-locus treatises, 3 books *Porisms*, 8 books *Conics*, 5 books *Solid Loci*, 2 books *Surface Loci*, and 2 books *On Means*.
* **$n$-Line Locus & Centroid Rule**: Compound-ratio formulation of the $n$-line conic/algebraic locus (*pp. 676–680*) and the Pappus–Guldinus Centroid Theorem $V = 2\pi\bar{r}\,A$, $S = 2\pi\bar{r}\,L$ (*p. 682*).

2. Projective Invariants & Straightedge Constructions (*Props. 129, 131, 138–139*)
----------------------------------------------------------------------------------

.. picture:: /_static/constructions/harmonic_fourth.svg
   :alt: Complete Quadrilateral Straightedge Construction of Fourth Harmonic Conjugate D (Synagoge VII.131)

* **Cross-Ratio Perspectivity (VII.129)** — :func:`geometor.pappus.cross_ratio` and :func:`geometor.pappus.project_point` preserve $\operatorname{CR}(A, B; C, D) = \frac{(A - C)(B - D)}{(A - D)(B - C)}$ identically across central projections.
* **Complete Quadrilateral Fourth Harmonic (VII.131)** — :func:`geometor.pappus.construct_harmonic_fourth` constructs :g:`D <g1:D>` from :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>` by straightedge alone so $\operatorname{CR}(A, B; C, D) = -1$, independent of the auxiliary quadrilateral chosen.
* **Hexagon Collinearity (VII.138–139)** — :func:`geometor.pappus.construct_pappus_hexagon` constructs $M_{01}, M_{20}, M_{12}$ on the Pappus line $p$, while :func:`geometor.pappus.verify_pappus_symbolic` proves that the homogeneous $3 \times 3$ bracket determinant $\det[M_{01}, M_{12}, M_{20}]$ vanishes identically over $\mathbb{Z}[a_0, a_1, a_2, b_0, b_1, b_2, u_x, u_y]$.
* **Six-Permutation Steiner Web ($S_3$)** — :func:`geometor.pappus.construct_pappus_configuration` verifies across all $6$ permutations that the $3$ even Pappus lines ($A_3$) concur at $S_+$ and the $3$ odd Pappus lines concur at $S_-$.
