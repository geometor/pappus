:order: 1
:layout: book
:type: book
:title: Proposition 1 · Exact Symbolic Invariants & 10-Variable Ring
:canonical_id: Syn. IV.1.summary
:folio: hultsch_1876_vol1:0209
:tracks: English: index | Greek: el | Summary: summary | Notes: notes

Proposition 1 · Exact Symbolic Invariants & 10-Variable Ring
============================================================

.. rubric:: Algebraic Geometry & Exact Shear Verification

.. folio:: hultsch_1876_vol1:0209
   :page: 176

1. Elements 2.0 Structural Decomposition
----------------------------------------

* **Given**: Arbitrary triangle :math:`\triangle ABC` with vertices :math:`A, B, C` and arbitrary lateral vectors :math:`\vec{u}, \vec{w}` defining parallelograms :math:`ABDE` and :math:`ACFG`.
* **Construct**: Intersection :math:`H = DE \cap FG`, apex vector :math:`\vec{v} = A - H`, and base parallelogram :math:`BCML` with :math:`L = B + \vec{v}`, :math:`M = C + \vec{v}`.
* **Demonstrate**: :math:`\operatorname{Area}(ABDE) + \operatorname{Area}(ACFG) = \operatorname{Area}(BCML)`.

2. 10-Variable Polynomial Ring Identity
---------------------------------------

Implemented in :func:`geometor.pappus.verify_pappus_area_symbolic`, the signed cross-product area identity vanishes identically over :math:`\mathbb{Z}[x_A, y_A, x_B, y_B, x_C, y_C, u_1, v_1, u_2, v_2]`.
