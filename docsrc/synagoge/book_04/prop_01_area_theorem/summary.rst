:order: 1
:layout: book
:type: book
:title: Proposition 1 · Exact Symbolic Invariants & 10-Variable Ring
:canonical_id: Syn. IV.1.summary
:folio: 0235
:tracks: English: index | Greek: el | Summary: summary | Notes: notes

Proposition 1 · Exact Symbolic Invariants & 10-Variable Ring
============================================================

.. rubric:: Algebraic Geometry & Exact Shear Verification

.. folio:: 0235
   :page: 1223

1. Elements 2.0 Structural Decomposition
----------------------------------------

* **Given**: Arbitrary triangle $\triangle ABC$ with vertices $A, B, C$ and arbitrary lateral vectors $\vec{u}, \vec{w}$ defining parallelograms $ABDE$ and $ACFG$.
* **Construct**: Intersection $H = DE \cap FG$, apex vector $\vec{v} = A - H$, and base parallelogram $BCML$ with $L = B + \vec{v}$, $M = C + \vec{v}$.
* **Demonstrate**: $\operatorname{Area}(ABDE) + \operatorname{Area}(ACFG) = \operatorname{Area}(BCML)$.

2. 10-Variable Polynomial Ring Identity
---------------------------------------

Implemented in :func:`geometor.pappus.verify_pappus_area_symbolic`, the signed cross-product area identity vanishes identically over $\mathbb{Z}[x_A, y_A, x_B, y_B, x_C, y_C, u_1, v_1, u_2, v_2]$.
