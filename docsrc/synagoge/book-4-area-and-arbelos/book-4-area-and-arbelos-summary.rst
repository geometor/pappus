.. _synagoge-b4-summary:

===============================================================================
Book IV · Summary & Exact Symbolic Audit (*Area Theorem & Arbelos Chain*)
===============================================================================

.. rubric:: Structural Argument Map & ``geometor.pappus`` Symbolic Verification

1. Pappus's Parallelogram Area Theorem (*Book IV, Prop. 1*)
-----------------------------------------------------------

* **Affine Shear Decomposition**: On any counter-clockwise triangle $\triangle ABC$, erect outward parallelograms $ABDE$ (side vector $\vec{u}$) and $ACFG$ (side vector $\vec{v}$). Intersect outer lines $DE \cap FG = H$ and set translation vector $\vec{w} = A - H$. Erect parallelogram $BCML$ on $BC$ with $L = B + \vec{w}$, $M = C + \vec{w}$.
* **Universal 10-Symbol Proof**: :func:`geometor.pappus.verify_pappus_area_symbolic` solves $H = E + s(B - A) = G + t(C - A)$ over $\mathbb{Q}(x_A, y_A, x_B, y_B, x_C, y_C, u_x, u_y, v_x, v_y)$ and simplifies

  .. math::

     \det(B - C, A - H) - \bigl(\det(A - B, \vec{u}) + \det(\vec{v}, A - C)\bigr) \equiv 0.

* **Built-In Exact Presets** (:func:`~geometor.pappus.construct_pappus_area_theorem`, ``demos/pappus_area_theorem.py``):
  - ``"scalene"``: $A=(3,4), B=(0,0), C=(7,0)$, $\operatorname{Area}(ABDE) = 13$, $\operatorname{Area}(ACFG) = 15$, $\operatorname{Area}(BCML) = 28$.
  - ``"pythagoras"``: $A=(\frac{9}{5},\frac{12}{5}), B=(0,0), C=(5,0)$, squares of areas $9 + 16 = 25$ (*Elements* I.47).

2. Pappus's *Arbelos* Tangent Circle Chain (*Book IV, Props. 14–18*)
--------------------------------------------------------------------

For inner radii $r_1, r_2 > 0$ and outer radius $R = r_1 + r_2$ on baseline $AC = [0, 2R]$, setting $\Delta_n = r_1(r_1 + r_2) + n^2 r_2^2$ yields 100% rational circle parameters without square roots:

.. math::

   r_n = \frac{r_1 r_2 R}{\Delta_n}, \qquad
   x_n = \frac{r_1 R (2r_1 + r_2)}{\Delta_n}, \qquad
   y_n = \frac{2 n\,r_1 r_2 R}{\Delta_n} = 2n\,r_n = n\,d_n.

.. list-table:: Rational Chain Table for $(r_1, r_2) = (2, 1)$ ($R = 3$)
   :header-rows: 1
   :widths: 12 18 24 18 16 12

   * - Index $n$
     - $\Delta_n = 6 + n^2$
     - Center $K_n = (x_n, y_n)$
     - Diameter $d_n$
     - Altitude $y_n$
     - $y_n / d_n$
   * - $1$
     - $7$
     - $\left(\dfrac{30}{7}, \dfrac{12}{7}\right)$
     - $\dfrac{12}{7}$
     - $\dfrac{12}{7}$
     - $1$
   * - $2$
     - $10$
     - $\left(3, \dfrac{12}{5}\right)$
     - $\dfrac{6}{5}$
     - $\dfrac{12}{5}$
     - $2$
   * - $3$
     - $15$
     - $\left(2, \dfrac{12}{5}\right)$
     - $\dfrac{4}{5}$
     - $\dfrac{12}{5}$
     - $3$
   * - $4$
     - $22$
     - $\left(\dfrac{15}{11}, \dfrac{24}{11}\right)$
     - $\dfrac{6}{11}$
     - $\dfrac{24}{11}$
     - $4$

* **Universal Symbolic Tangency Proof**: :func:`geometor.pappus.verify_arbelos_chain_symbolic` proves over $\mathbb{Q}(r_1, r_2, n)$ that $y_n - 2n r_n = 0$, $Q(K_n, O_0) - (R - r_n)^2 = 0$, $Q(K_n, O_1) - (r_1 + r_n)^2 = 0$, and $Q(K_{n+1}, K_n) - (r_{n+1} + r_n)^2 = 0$ vanish identically, while all centers $K_n$ lie on the ellipse with foci $O_1 = (r_1, 0)$ and $O_0 = (R, 0)$ of major axis $2r_1 + r_2$.
