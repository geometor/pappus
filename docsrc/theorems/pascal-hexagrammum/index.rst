:type: theorem
:order: 5
:summary: Blaise Pascal's 1640 smooth-conic generalization of Pappus's Hexagon Theorem, the complete 60-line Hexagrammum Mysticum web (Steiner, Kirkman, and Plücker incidences), and emergent Golden Ratio conic sections in Q(φ).

Pascal's *Hexagrammum Mysticum* (1640)
======================================

From Two Straight Lines to Any Conic Section
--------------------------------------------

Thirteen centuries after Pappus proved his Hexagon Lemma (*Synagoge* VII.139) for six points
distributed along **two straight lines** $a$ and $b$, sixteen-year-old **Blaise Pascal** published a
single printed broadsheet in February 1640—*Essai pour les coniques*—announcing a breathtaking
generalization: **the two lines can be replaced by any conic section**.

Algebraically, Pappus's theorem and Pascal's theorem are **two faces of one projective law**. Six
points $P_k = (x_k, y_k)$ lie on a planar curve of degree two—whether a **smooth conic**
$\mathcal{C}: A x^2 + B x y + C y^2 + D x + E y + F = 0$ (circle, ellipse, parabola, or hyperbola)
or a **degenerate conic** $L_a(x, y) \cdot L_b(x, y) = 0$ (Pappus's pair of lines)—if and only if
their $6 \times 6$ **Veronese matrix** drops rank ($\det V_6 = 0$):

.. math::

   \det \begin{bmatrix}
   x_0^2 & x_0 y_0 & y_0^2 & x_0 & y_0 & 1 \\
   x_1^2 & x_1 y_1 & y_1^2 & x_1 & y_1 & 1 \\
   \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
   x_5^2 & x_5 y_5 & y_5^2 & x_5 & y_5 & 1
   \end{bmatrix} = 0.

In ``geometor.pappus.projective.are_coconic``, this exact SymPy rank test unifies smooth circles
and ellipses with Pappus's two-line configurations under a single algebraic predicate, while
**Colin Maclaurin** (1720) and **William Braikenridge** (1733) proved the converse: if the three
opposite-side intersections of a hexagon are collinear, its six vertices necessarily lie on a conic!

.. admonition:: Theorem (Pascal's *Hexagrammum Mysticum*, 1640)

   Let $P_0, P_1, P_2, P_3, P_4, P_5$ be any six distinct points on an irreducible conic
   $\mathcal{C}$ in $\mathbb{P}^2$, ordered in a cyclic hexagon
   $\langle P_{c_0}, P_{c_1}, P_{c_2}, P_{c_3}, P_{c_4}, P_{c_5} \rangle$. Then the three
   intersections of opposite sides,

   .. math::

      M_{03} = [P_{c_0} P_{c_1}] \cap [P_{c_3} P_{c_4}], \quad
      M_{14} = [P_{c_1} P_{c_2}] \cap [P_{c_4} P_{c_5}], \quad
      M_{25} = [P_{c_2} P_{c_3}] \cap [P_{c_5} P_{c_0}],

   are **collinear** along a single line $p$—the **Pascal line** of the inscribed hexagram.

The Mystic Star Hexagram on the Pythagorean Circle
--------------------------------------------------

To explore Pascal's theorem in **100% exact rational arithmetic** ($\mathbb{Q}^2$) without
floating-point approximations, ``geometor.pappus.projective.circle_stereographic_point`` maps
any rational parameter $t \in \mathbb{Q}$ onto the unit circle $x^2 + y^2 = 1$ via Weierstrass
stereographic projection:

.. math::

   P(t) = \left(\frac{1 - t^2}{1 + t^2},\; \frac{2t}{1 + t^2}\right) \in \mathbb{Q}^2.

Seeding ``preset="hexagrammum"`` with $t = \left(0,\, \frac{1}{3},\, 1,\, 3,\, -2,\, -\frac{1}{2}\right)$
places six cardinal and $3\text{-}4\text{-}5$ Pythagorean vertices around all four quadrants of
$x^2 + y^2 = 1$:

.. math::

   P_0 = (1, 0),\quad P_1 = \left(\frac{4}{5}, \frac{3}{5}\right),\quad
   P_2 = (0, 1),\quad P_3 = \left(-\frac{4}{5}, \frac{3}{5}\right),\quad
   P_4 = \left(-\frac{3}{5}, -\frac{4}{5}\right),\quad P_5 = \left(\frac{3}{5}, -\frac{4}{5}\right).

Tracing the non-convex **mystic star cycle** $\langle P_0, P_2, P_4, P_1, P_3, P_5 \rangle$ produces
two interior meets and one compact exterior meet, all strictly rational:

.. math::

   M_{03} = \left(\frac{2}{5},\, \frac{3}{5}\right), \qquad
   M_{14} = \left(-\frac{3}{10},\, \frac{1}{10}\right), \qquad
   M_{25} = \left(\frac{9}{5},\, \frac{8}{5}\right),

aligned along the exact Pascal line $25x - 35y + 11 = 0$:

.. picture:: /_static/constructions/pascal_hexagrammum.svg
   :alt: Pascal's Hexagrammum Mysticum (1640) on the Pythagorean Unit Circle

.. step::

   Inscribe the six Pythagorean rational points :g:`P_0 <g1:P0>`, :g:`P_1 <g1:P1>`,
   :g:`P_2 <g1:P2>`, :g:`P_3 <g1:P3>`, :g:`P_4 <g1:P4>`, and :g:`P_5 <g1:P5>` around the unit
   circle :g:`𝒞 <g1:( O P0 )>` centered at :g:`O <g1:O>` $= (0, 0)$.

.. step::

   Trace the self-intersecting star hexagram
   :g:`P_0 P_2 P_4 P_1 P_3 P_5 <g1:< P0 P2 P4 P1 P3 P5 >>` and intersect the first opposite side
   pair :g:`P_0 P_2 <g1:[ P0 P2 ]>` ($x + y = 1$) with :g:`P_1 P_3 <g1:[ P1 P3 ]>` ($y = \frac{3}{5}$)
   at :g:`M_{03} <g1:M03>` $= \left(\frac{2}{5}, \frac{3}{5}\right)$.

.. step::

   Intersect the second opposite pair :g:`P_2 P_4 <g1:[ P2 P4 ]>` ($3x - y + 1 = 0$) with
   :g:`P_3 P_5 <g1:[ P3 P5 ]>` ($5x + 5y + 1 = 0$) inside the circle at
   :g:`M_{14} <g1:M14>` $= \left(-\frac{3}{10}, \frac{1}{10}\right)$, and the third opposite pair
   :g:`P_4 P_1 <g1:[ P4 P1 ]>` ($5x - 5y = 1$) with :g:`P_5 P_0 <g1:[ P5 P0 ]>` ($2x - y = 2$)
   outside the circle at :g:`M_{25} <g1:M25>` $= \left(\frac{9}{5}, \frac{8}{5}\right)$.

.. step::

   Draw the **Pascal line** :g:`p <g1:[ M03 M14 ]>` ($25x - 35y + 11 = 0$):
   $25\left(\frac{2}{5}\right) - 35\left(\frac{3}{5}\right) + 11 = 10 - 21 + 11 = 0$,
   $25\left(-\frac{3}{10}\right) - 35\left(\frac{1}{10}\right) + 11 = -11 + 11 = 0$, and
   $25\left(\frac{9}{5}\right) - 35\left(\frac{8}{5}\right) + 11 = 45 - 56 + 11 = 0$!

Universal Symbolic Proof & Conic Invariance
-------------------------------------------

Why did Pascal need only prove his lemma for the circle in order to establish it for **every**
ellipse, parabola, and hyperbola? Because any non-degenerate conic is the central projection of a
circle from the apex of Apollonius's cone, and incidence ($P \in \ell$) is preserved under every
projective transformation $T \in \mathrm{PGL}_3(\mathbb{R})$.

1. **Universal 6-Parameter Proof**: ``verify_pascal_symbolic()`` parameterizes six completely
   generic points $P_k = [1 - t_k^2 : 2 t_k : 1 + t_k^2]$ over the six-variable polynomial ring
   $\mathbb{Z}[t_0, t_1, t_2, t_3, t_4, t_5]$, computes $M_{03}, M_{14}, M_{25}$ via homogeneous
   3D cross products, and expands $\det[M_{03}, M_{14}, M_{25}]$—which cancels **identically to
   zero**.
2. **General Ellipse Verification**: Applying the affine transformation $(x, y) \mapsto (2x, y)$
   in ``preset="ellipse"`` maps the Pythagorean hexagram onto the non-circular ellipse
   $\mathcal{E}: \frac{x^2}{4} + y^2 = 1$ ($x^2 + 4y^2 - 4 = 0$), stretching the three Pascal
   intersections to
   $M'_{03} = \left(\frac{4}{5}, \frac{3}{5}\right)$,
   $M'_{14} = \left(-\frac{3}{5}, \frac{1}{10}\right)$, and
   $M'_{25} = \left(\frac{18}{5}, \frac{8}{5}\right)$ along $25x - 70y + 22 = 0$:

.. picture:: /_static/constructions/pascal_ellipse.svg
   :alt: Pascal's Hexagrammum Mysticum on the General Ellipse x^2/4 + y^2 = 1

.. step::

   Compare the stretched ellipse :g:`ℰ <g2:( O P0 )>` ($\frac{x^2}{4} + y^2 = 1$) with the unit
   circle above: every chord, opposite meet :g:`M'_{03} <g2:M03>`, :g:`M'_{14} <g2:M14>`,
   :g:`M'_{25} <g2:M25>`, and Pascal line :g:`p' <g2:[ M03 M14 ]>` transforms covariantly while
   preserving exact three-point collinearity.

The Complete 60-Line *Hexagrammum Mysticum* Web
-----------------------------------------------

On two lines (Pappus), permuting the vertices yields $3! = 6$ hexagons and **6 Pappus lines**
concurring in **2 Steiner Star points**. On a smooth conic, however, **no three of the six vertices
are collinear**, so **every cyclic ordering** of $P_0, \dots, P_5$ up to dihedral rotation and
reversal ($D_6$, order 12) inscribes a valid hexagon—producing

.. math::

   \frac{6!}{2 \cdot 6} = \mathbf{60\text{ Pascal lines}}!

In the nineteenth century, **Jakob Steiner** (1828), **Julius Plücker** (1830), **Thomas Penyngton
Kirkman** (1850), **Arthur Cayley**, and **George Salmon** uncovered an astonishing, self-dual
incidence architecture hidden inside these 60 lines. Running
``enumerate_hexagrammum_mysticum(preset="hexagrammum")`` constructs and verifies every element of
this web in exact homogeneous coordinates with **zero combinatorial degeneracies**:

.. list-table:: Exact Projective Census of Pascal's *Hexagrammum Mysticum* (``preset="hexagrammum"``)
   :header-rows: 1
   :widths: 26 12 62

   * - Geometric Stratum
     - Count
     - Incidence Law & Discoverer
   * - **Conic Chords** $[P_i P_j]$
     - **15**
     - $\binom{6}{2} = 15$ secant lines joining pairs of the 6 conic vertices
   * - **Pascal Diagonal Points**
     - **45**
     - $\frac{1}{2}\binom{6}{2}\binom{4}{2} = 45$ intersections $[P_i P_j] \cap [P_k P_l]$; 4 Pascal lines pass through each
   * - **Pascal Lines** $p_H$
     - **60**
     - $6! / 12 = 60$ lines, each carrying 3 of the 45 diagonal points (Pascal, 1640)
   * - **Steiner Points** $G$
     - **20**
     - 60 Pascal lines concur 3-by-3 at 20 Steiner points—2 per complementary triangle pair (Steiner, 1828)
   * - **Kirkman Points** $K$
     - **60**
     - 60 Pascal lines also concur 3-by-3 in a **second** way at 60 Kirkman points—3 on each Pascal line (Kirkman, 1850)
   * - **Plücker Lines** $\ell_{\mathrm{Pl}}$
     - **15**
     - 20 Steiner points lie 4-by-4 along 15 Plücker lines—3 through each Steiner point (Plücker, 1830)

Bi-Triangle $S_3$ Concurrency: How Pappus's Two Star Points Generalize
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

How do Steiner's **20 points** on a smooth conic relate to the **2 Star points** $(S_+, S_-)$ of
the Pappus–Steiner theorem? Partition the six conic vertices into **two complementary inscribed
triangles**—say $\triangle_A = (P_0, P_2, P_4)$ and $\triangle_B = (P_1, P_3, P_5)$. There are
$\frac{1}{2}\binom{6}{3} = 10$ such complementary triangle pairs.

Fixing $\triangle_A$ and permuting $\triangle_B$ by $\sigma \in S_3$ generates **6 alternating
hexagons** $\langle P_0, B_{\sigma_0}, P_2, B_{\sigma_1}, P_4, B_{\sigma_2} \rangle$—the exact
smooth-conic counterpart of the six $S_3$ Pappus hexagons! Just as on two lines:

- The **3 even** ($\sigma \in A_3$) Pascal lines concur at the even Steiner point
  $G_+ = \left(\frac{78}{25},\; \frac{1}{25}\right)$.
- The **3 odd** ($\sigma \in S_3 \setminus A_3$) Pascal lines concur at the odd Steiner point
  $G_- = \left(\frac{498}{1565},\; \frac{281}{1565}\right)$.

Across all $10$ triangle partitions, $10 \times 2 = \mathbf{20}$ Steiner points arise; when the
conic degenerates into two straight lines $a \cup b$, only the single partition separating $a$ from
$b$ survives without collapsing onto the carrier lines, leaving Pappus's two Star points
$(S_+, S_-)$!

.. picture:: /_static/constructions/pascal_steiner_family.svg
   :alt: Bi-Triangle S_3 Pascal Lines Concurring at Steiner Points G+ and G-

.. step::

   Partition the conic vertices on :g:`𝒞 <g3:( O P0 )>` into complementary triangles
   $\triangle_A =$ (:g:`P_0 <g3:P0>`, :g:`P_2 <g3:P2>`, :g:`P_4 <g3:P4>`) and
   $\triangle_B =$ (:g:`P_1 <g3:P1>`, :g:`P_3 <g3:P3>`, :g:`P_5 <g3:P5>`), joined by their nine
   cross-chords.

.. step::

   Trace the three **even** ($A_3$) Pascal lines
   :g:`p_{012} <g3:[ M0143 M2145 ]>` ($49x + 28y = 154$),
   :g:`p_{120} <g3:[ M0345 M2341 ]>` ($15x + 5y = 47$), and
   :g:`p_{201} <g3:[ M0541 M2543 ]>` ($39x + 33y = 123$), concurring at
   :g:`G_+ <g3:S1>` $= \left(\frac{78}{25},\, \frac{1}{25}\right)$.

.. step::

   Trace the three **odd** ($S_3 \setminus A_3$) Pascal lines
   :g:`p_{021} <g3:[ M0145 M2143 ]>`, :g:`p_{102} <g3:[ M0341 M2345 ]>` ($5x - 20y + 2 = 0$),
   and :g:`p_{210} <g3:[ M0543 M2541 ]>` ($83x - 19y = 23$), concurring inside the circle at
   :g:`G_- <g3:S2>` $= \left(\frac{498}{1565},\, \frac{281}{1565}\right)$, and join the pair along
   :g:`G_+G_- <g3:[ S1 S2 ]>`.

Golden *Hexagrammum Mysticum* in $\mathbb{Q}(\phi)$
---------------------------------------------------

By **Michel Chasles's Theorem** (1865), four points $P_0, P_1, P_2, P_3$ on an irreducible conic
$\mathcal{C}$ possess an intrinsic **conic cross-ratio** $(P_0, P_1; P_2, P_3)_{\mathcal{C}}$: for
any fifth observer point $V \in \mathcal{C}$, the pencil of four rays $[V P_0], [V P_1], [V P_2], [V P_3]$
has the **exact same cross-ratio**, independent of $V$.

Because Weierstrass stereographic projection is a birational isomorphism $\mathbb{P}^1 \to \mathcal{C}$,
seeding ``preset="golden_conic"`` with the golden stereographic chain
$t = (0,\, 1,\, \phi,\, \phi + 1,\, -1,\, -\phi)$ inscribes six exact $\mathbb{Q}(\sqrt{5})$ points
on $x^2 + y^2 = 1$:

.. math::

   P_0 = (1, 0), \quad P_1 = (0, 1), \quad
   P_2 = \left(-\frac{\sqrt{5}}{5},\, \frac{2\sqrt{5}}{5}\right), \quad
   P_3 = \left(-\frac{\sqrt{5}}{3},\, \frac{2}{3}\right), \quad
   P_4 = (0, -1), \quad P_5 = \left(-\frac{\sqrt{5}}{5},\, -\frac{2\sqrt{5}}{5}\right).

1. **Chasles Golden Conic Cross-Ratio**: Calling ``conic_cross_ratio(P_0, P_1, P_2, P_3, V)`` from
   either $V = P_4$ or $V = P_5$ simplifies identically to the **Golden Ratio**
   $\phi = \frac{1 + \sqrt{5}}{2}$!
2. **Emergent Golden Section on the Mystic Hexagram**: Constructing the inscribed hexagram on
   cycle $\langle P_0, P_2, P_5, P_1, P_3, P_4 \rangle$ yields exact opposite-side intersections

   .. math::

      M_{03} = \left(\frac{5 - 4\sqrt{5}}{11},\; \frac{7 + \sqrt{5}}{11}\right), \qquad
      M_{14} = \left(-\frac{\sqrt{5}}{5},\; 0\right), \qquad
      M_{25} = \left(-\phi^{-1},\; -\phi\right) = \left(\frac{1 - \sqrt{5}}{2},\; -\frac{1 + \sqrt{5}}{2}\right).

   Running ``geometor.divine`` (``find_golden_sections``) on this model automatically discovers an
   **emergent golden section**: the Pascal intersection $M_{25} = (-\phi^{-1}, -\phi)$ extends the
   conic chord $[P_4 P_0]$ ($y = x - 1$) in the **exact Divine Proportion**! Because
   $x(P_0) - x(P_4) = 1 - 0 = 1$ and $x(P_4) - x(M_{25}) = 0 - (-\phi^{-1}) = \phi^{-1}$ along the
   $45^\circ$ chord, $|P_0 P_4| / |P_4 M_{25}| = |M_{25} P_0| / |P_0 P_4| = \phi$ identically:

.. picture:: /_static/constructions/golden_pascal.svg
   :alt: Golden Hexagrammum Mysticum in Q(phi) — Emergent Section / M25 P4 P0 /

.. step::

   Project the golden parameter chain $t = (0, 1, \phi, \phi + 1, -1, -\phi)$ onto the unit circle
   :g:`𝒞 <g4:( O P0 )>` to obtain :g:`P_0 <g4:P0>`, :g:`P_1 <g4:P1>`, :g:`P_2 <g4:P2>`,
   :g:`P_3 <g4:P3>`, :g:`P_4 <g4:P4>`, and :g:`P_5 <g4:P5>`, where $(P_0, P_1; P_2, P_3)_{\mathcal{C}} = \phi$.

.. step::

   Trace the hexagram :g:`P_0 P_2 P_5 P_1 P_3 P_4 <g4:< P0 P2 P5 P1 P3 P4 >>` and locate the three
   exact $\mathbb{Q}(\sqrt{5})$ opposite-side intersections :g:`M_{03} <g4:M03>`,
   :g:`M_{14} <g4:M14>`, and :g:`M_{25} <g4:M25>` $= (-\phi^{-1}, -\phi)$ on Pascal line
   :g:`p <g4:[ M03 M14 ]>`.

.. step::

   Inspect the emergent ``geometor.divine`` golden section
   :g:`M_{25} P_4 P_0 <g4:/ M25 P4 P0 />` along chord :g:`P_4 P_0 <g4:[ P4 P0 ]>`:
   $|P_0 P_4| = \sqrt{2}$ and $|P_4 M_{25}| = \phi^{-1}\sqrt{2}$, dividing the extended conic chord
   in the exact Golden Ratio $\phi = \frac{1 + \sqrt{5}}{2}$.
