:layout: book
:type: book
:title: Proposition 1 · Exact Symbolic Invariants & 10-Variable Ring
:canonical_id: Syn. IV.1.summary
:tracks: English: index | Greek: el | Summary: summary | Notes: notes

Proposition 1 · Exact Symbolic Invariants & 10-Variable Ring
============================================================

.. rubric:: Algebraic Geometry & Exact Shear Verification

1. Elements 2.0 Structural Decomposition
----------------------------------------

* **Given**: Arbitrary triangle $\triangle ABC$ with vertices $A = (x_A, y_A)$, $B = (x_B, y_B)$, $C = (x_C, y_C)$, and arbitrary vectors $\vec{u} = (u_1, v_1)$, $\vec{w} = (u_2, v_2)$ defining parallelograms $ABDE$ and $ACFG$.
* **Construct**:
  1. Line $DE \parallel AB$ through $D = B + \vec{u}$ and $E = A + \vec{u}$.
  2. Line $FG \parallel AC$ through $F = C + \vec{w}$ and $G = A + \vec{w}$.
  3. Intersection $H = DE \cap FG$.
  4. Apex vector $\vec{v} = A - H$.
  5. Base parallelogram $BCML$ with $L = B + \vec{v}$ and $M = C + \vec{v}$.
* **Demonstrate**: $\operatorname{Area}(ABDE) + \operatorname{Area}(ACFG) = \operatorname{Area}(BCML)$.

2. 10-Variable Polynomial Ring Identity
---------------------------------------

Implemented in :func:`geometor.pappus.verify_pappus_area_symbolic`:

The signed 2D cross-product area identity:

.. math::

   ((B - A) \times \vec{u}) + ((A - C) \times \vec{w}) = (C - B) \times (A - H)

simplifies to $0$ identically over the 10-variable polynomial ring $\mathbb{Z}[x_A, y_A, x_B, y_B, x_C, y_C, u_1, v_1, u_2, v_2]$, confirming zero residual across all possible triangle geometries.
