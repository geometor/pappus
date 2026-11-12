.. _synagoge-b5-summary:

=====================================================================================
Book V · Summary & Exact Symbolic Audit (*Honeycomb Tessellation & Isoperimetry*)
=====================================================================================

.. rubric:: Structural Argument Map & ``geometor.pappus`` Symbolic Verification

1. Diophantine Proof of Regular Planar Tilings (*Book V, Ch. 2*)
----------------------------------------------------------------

For $k \ge 3$ congruent regular $n$-gons ($n \ge 3$) to surround a planar vertex without gaps or overlaps, their interior angles $\theta_n = \frac{n - 2}{n}\cdot 180^\circ$ must sum to $360^\circ$:

.. math::

   k \cdot \frac{n - 2}{n} = 2 \quad \Longleftrightarrow \quad k = \frac{2n}{n - 2} = 2 + \frac{4}{n - 2} \in \mathbb{Z}_{\ge 3}.

Because $(n - 2)$ must be a positive divisor of $4$, $(n - 2) \in \{1, 2, 4\}$, yielding the **unique three regular tessellations of the Euclidean plane**: $(n, k) \in \{(3, 6), (4, 4), (6, 3)\}$.

2. Exact Isoperimetric Comparison at Common Perimeter $P$ (*Book V, Props. 1–10*)
---------------------------------------------------------------------------------

Implemented in :func:`geometor.pappus.verify_honeycomb_isoperimetry` and :func:`geometor.pappus.construct_honeycomb_isoperimetry` (see ``demos/honeycomb_isoperimetry.py``):

.. list-table:: Exact Symbolic Comparison at Common Perimeter $P$ (and $P = 12$)
   :header-rows: 1
   :widths: 22 14 16 22 26

   * - Regular Tiling Polygon
     - Valence $k$
     - Side $s_n$ ($P=12$)
     - Symbolic Area $\operatorname{Area}_n(P)$
     - Exact Area at $P = 12$
   * - Equilateral Triangle ($n = 3$)
     - $6$
     - $4$
     - $\dfrac{\sqrt{3}}{36}\,P^2$
     - $4\sqrt{3}$
   * - Square ($n = 4$)
     - $4$
     - $3$
     - $\dfrac{1}{16}\,P^2$
     - $9$
   * - Regular Hexagon ($n = 6$)
     - $3$
     - $2$
     - $\dfrac{\sqrt{3}}{24}\,P^2$
     - $6\sqrt{3}$
   * - Circle ($n \to \infty$, *Prop. 2*)
     - —
     - —
     - $\dfrac{1}{4\pi}\,P^2$
     - $\dfrac{36}{\pi}$

3. Exact Area Ratios Over $\mathbb{Q}(\sqrt{3})$
------------------------------------------------

* **Hexagon vs. Triangle**: $\dfrac{\operatorname{Area}_6}{\operatorname{Area}_3} = \dfrac{3}{2}$ (exact rational $50\%$ gain).
* **Hexagon vs. Square**: $\dfrac{\operatorname{Area}_6}{\operatorname{Area}_4} = \dfrac{2\sqrt{3}}{3} > 1$, verified in pure integer arithmetic via $\left(\frac{2\sqrt{3}}{3}\right)^2 = \frac{4}{3} > 1$.
* **Square vs. Triangle**: $\dfrac{\operatorname{Area}_4}{\operatorname{Area}_3} = \dfrac{3\sqrt{3}}{4} > 1$, verified via $\left(\frac{3\sqrt{3}}{4}\right)^2 = \frac{27}{16} > 1$.
* **Seven-Hexagon Rosette Circumradius** (*Book VIII, Prop. 23*): $R_7 = s_6\sqrt{7} = \frac{\sqrt{7}}{6}\,P$ ($2\sqrt{7}$ for $P = 12$).
