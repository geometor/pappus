:type: theorem
:order: 6
:summary: Exact SymPy and geometor.model constructions across Books III, IV, V, and VIII of Pappus's Synagoge—Three Means in One Semicircle, Parallelogram Area Theorem, Arbelos Circle Chain, and Honeycomb Isoperimetry.

Classical *Synagoge* Constructions (Books III, IV, V & VIII)
============================================================

Alongside Book VII's projective incidence canon, :mod:`geometor.pappus.synagoge_demos` brings
four celebrated metric, affine, and isoperimetric propositions of Pappus's *Synagoge* to life in
100% exact symbolic coordinates—paired directly with the four-track Greek/English
:doc:`Synagoge Book Codex <../../synagoge/index>`.

1. Book III, Props. 28–30: Three Classical Means in One Semicircle
------------------------------------------------------------------

Given unequal positive segments $AD = a$ and $DC = b$ placed along diameter $AC$ of a semicircle
centered at $O$ (:doc:`Book III Codex <../../synagoge/book-3-three-means/book-3-three-means-en>`,
*Hultsch I, pp. 68–84*), ``construct_three_means(a, b)`` constructs the arithmetic mean $A$,
geometric mean $G$, and harmonic mean $H$ inside a single diagram, together with the external
harmonic conjugate $T$ where $(A, C; D, T) = -1$:

.. list-table:: Exact Semicircle Means over $\mathbb{Q}$ and $\mathbb{Q}(\phi)$
   :header-rows: 1
   :widths: 22 20 20 20 18

   * - Segments $(a, b)$
     - Arithmetic $A = |OB|$
     - Geometric $G = |DB|$
     - Harmonic $H = |BF|$
     - Conjugate $T$
   * - $(9,\, 16)$
     - $\frac{25}{2}$
     - $12$
     - $\frac{288}{25}$
     - $\left(-\frac{225}{7},\, 0\right)$
   * - $(4,\, 9)$
     - $\frac{13}{2}$
     - $6$
     - $\frac{72}{13}$
     - $\left(-\frac{36}{5},\, 0\right)$
   * - $(1,\, \phi^2)$
     - $\frac{\phi + 2}{2}$
     - $\phi$
     - $\frac{2\phi}{\sqrt{5}}$
     - $(-\phi,\, 0)$

.. picture:: /_static/constructions/synagoge_three_means.svg
   :alt: Synagoge Book III — Arithmetic, Geometric, and Harmonic Means in One Semicircle (9, 16)

.. step::

   Place :g:`A <g1:A>` $= (0, 0)$, :g:`D <g1:D>` $= (9, 0)$, and :g:`C <g1:C>` $= (25, 0)$ along
   diameter :g:`AC <g1:[ A C ]>` with midpoint :g:`O <g1:O>` $= \left(\frac{25}{2}, 0\right)$ on
   semicircle :g:`ABC <g1:( O A )>`, so radius :g:`OB <g1:[ O B ]>` equals $A = \frac{25}{2}$.

.. step::

   Erect ordinate :g:`DB <g1:[ D B ]>` perpendicular to :g:`AC <g1:[ A C ]>` meeting the
   semicircle at :g:`B <g1:B>` $= (9, 12)$, yielding $G = \sqrt{9 \cdot 16} = 12$.

.. step::

   Drop :g:`DF <g1:[ D F ]>` perpendicular to radius :g:`OB <g1:[ O B ]>` at foot
   :g:`F <g1:F>` $= \left(\frac{7641}{625}, \frac{588}{625}\right)$: right-triangle similarity
   $\triangle ODB \sim \triangle DFB$ gives $|BF| = \frac{G^2}{A} = \frac{288}{25} = H$, while
   tangent :g:`BT <g1:[ B T ]>` meets :g:`AC <g1:[ A C ]>` at :g:`T <g1:T>` $= \left(-\frac{225}{7}, 0\right)$
   with $(A, C; D, T) = -1$.

On the golden diameter $(a, b) = (1, \phi^2)$, the geometric mean :g:`DB <g2:[ D B ]>` equals
$\phi$ itself and the external tangent meets the diameter line at :g:`T <g2:T>` $= (-\phi, 0)$:

.. picture:: /_static/constructions/synagoge_three_means_golden.svg
   :alt: Synagoge Book III — Golden Semicircle Means over Q(phi)

2. Book IV, Prop. 1: Equiaffine Parallelogram Area Theorem
----------------------------------------------------------

In :doc:`Book IV, Proposition 1 <../../synagoge/book-4-area-and-arbelos/book-4-area-and-arbelos-en>`
(*Hultsch I, pp. 176–179*), Pappus generalizes *Elements* I.47 from squares on a right triangle to
**arbitrary outward parallelograms** erected on two sides $AB, AC$ of **any triangle** $\triangle ABC$.
If the outer sides produced meet at $H$, then the parallelogram constructed on base $BC$ with lateral
vector equal and parallel to $\overrightarrow{HA}$ has signed area identically equal to the sum of
the two side parallelograms:

.. math::

   \det(C - B,\; A - H) = \det(B - A,\; u) + \det(A - C,\; v)
   \quad \text{in } \mathbb{Z}[x_A, y_A, x_B, y_B, x_C, y_C, u_x, u_y, v_x, v_y].

``verify_pappus_area_symbolic()`` proves this universal 10-variable polynomial identity directly in
SymPy, while ``construct_pappus_area_theorem()`` models both the general scalene configuration
($13 + 15 = 28$) and Euclid's $3$-$4$-$5$ Pythagorean specialization ($9 + 16 = 25$).

3. Book IV, Props. 14–18: Infinite *Arbelos* Tangent Circle Chain
-----------------------------------------------------------------

In :doc:`Book IV, Propositions 14–18 <../../synagoge/book-4-area-and-arbelos/book-4-area-and-arbelos-en>`
(*Hultsch I, pp. 208–232*), Pappus demonstrates the *"ancient proposition"* on the shoemaker's knife
(*ἄρβηλος*): for an infinite chain of circles $C_1, C_2, C_3, \dots$ inscribed tangent to the three
bounding semicircles and successively to one another, the center altitude $y_n$ of the $n$-th circle
above baseline $AC$ is $n$ times its diameter $d_n$:

.. math::

   r_n = \frac{R\,r_1\,r_2}{r_1 r_2 + n^2 R^2 \text{ (in reduced } \lambda\text{-form)}},
   \qquad y_n = n\,d_n = 2n\,r_n \qquad (n = 1, 2, 3, \dots),

and every center $K_n$ lies on a single fixed ellipse with foci at $O_0$ and $O_1$.

.. picture:: /_static/constructions/pappus_arbelos_chain.svg
   :alt: Synagoge Book IV Propositions 14–18 — Arbelos Circle Chain (y_n = n d_n)

.. step::

   Construct outer semicircle :g:`(O0, A) <g3:( O0 A )>` of radius $R = 3$ and inner semicircles
   :g:`(O1, A) <g3:( O1 A )>` ($r_1 = 2$) and :g:`(O2, D) <g3:( O2 D )>` ($r_2 = 1$) along baseline
   :g:`AC <g3:[ A C ]>`.

.. step::

   Inscribe base circle :g:`C1 <g3:( K1 X1 )>` at :g:`K1 <g3:K1>` $= \left(\frac{30}{7}, \frac{12}{7}\right)$
   with diameter $d_1 = \frac{12}{7}$ and altitude :g:`P1K1 <g3:[ P1 K1 ]>` $= 1 \cdot d_1$.

.. step::

   Inscribe :g:`C2 <g3:( K2 X2 )>` at :g:`K2 <g3:K2>` $= \left(3, \frac{12}{5}\right)$ ($y_2 = 2\,d_2$),
   :g:`C3 <g3:( K3 X3 )>` at :g:`K3 <g3:K3>` $= \left(2, \frac{12}{5}\right)$ ($y_3 = 3\,d_3$), and
   :g:`C4 <g3:( K4 X4 )>` at :g:`K4 <g3:K4>` $= \left(\frac{15}{11}, \frac{24}{11}\right)$ ($y_4 = 4\,d_4$),
   tracing the rational focal ellipse through all centers.

4. Book V, Prop. 1 & Book VIII, Prop. 23: Honeycomb Isoperimetry & Seven Hexagons
---------------------------------------------------------------------------------

In :doc:`Book V <../../synagoge/book-5-sagacity-of-bees/book-5-sagacity-of-bees-en>` (*Hultsch I,
pp. 304–312*) and :doc:`Book VIII, Proposition 23 <../../synagoge/book-8-mechanics/book-8-mechanics-en>`
(*Hultsch III, pp. 1096–1102*), Pappus proves:

1. Around any gapless planar vertex tiled by $k \ge 3$ congruent regular $n$-gons,
   $k \cdot \frac{(n - 2)\pi}{n} = 2\pi \implies (n - 2)(k - 2) = 4$, uniquely admitting
   $(n, k) \in \{(3, 6), (4, 4), (6, 3)\}$.
2. At equal perimeter $P$, exact areas satisfy $A_6 : A_4 : A_3 = \frac{P^2}{8\sqrt{3}} : \frac{P^2}{16} : \frac{P^2}{12\sqrt{3}} = 3\sqrt{3} : 4 : 3$,
   so $A_6 / A_3 = \frac{3}{2}$ and $A_6 > A_4 > A_3$.
3. One central regular hexagon of side $s_6$ surrounded by six congruent petal hexagons has its
   twelve outer vertices concyclic on a circle of exact radius $R = s_6\sqrt{7}$ (by the Law of
   Cosines on the $120^\circ$ triangle with legs $s_6$ and $2s_6$: $R^2 = s_6^2 + 4s_6^2 + 2s_6^2 = 7s_6^2$).
