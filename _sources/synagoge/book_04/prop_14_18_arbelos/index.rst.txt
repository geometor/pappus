:order: 2
:layout: book
:type: book
:title: Propositions 14–18: The Ancient Theorem on the Arbelos Circle Chain
:canonical_id: Syn. IV.14-18
:excerpt: Pappus's presentation of the ancient theorem on an endless chain of tangent circles inscribed within the arbelos, establishing that the perpendicular height of the n-th circle center equals n times its own diameter.
:tracks: English: index | Greek: el | Summary: summary | Notes: notes

.. _sec-b4-en-arbelos-chain:

Propositions 14–18: The Ancient Theorem on the *Arbelos* Circle Chain
======================================================================

.. rubric:: *Synagoge* Book IV, Chs. 19–26 / Props. 14–18 (:cite:`Hultsch I, pp. 208–232 <hultsch:1876>`) · Original English Translation from Hultsch's Greek

*"There is set forth in the ancient geometrical inquiries a proposition of the following kind, which appears marvelous to many"* (*φέρεταί τις ἐν τοῖς ἀρχαίοις πρότασις τοιαύτη*, *Hultsch I p. 208*): Suppose three semicircles be described tangent to one another upon a single straight diameter—forming the curvilinear region bounded by the three arcs which the ancients call the :term:`arbelos <arbelos>` (*ἄρβηλος*, "shoemaker's knife")—and into the space between the three circumferences there be inscribed an endless chain of circles tangent both to the bounding semicircles and successively to one another. Then **the perpendicular dropped from the center of the first circle to the base diameter equals its own diameter, that from the center of the second circle is double its diameter, that from the third is triple its diameter, and so on without end according to the natural numbers exceeding one another by unity**:

.. math::

   y_n = n\,d_n = 2n\,r_n \qquad (n = 1, 2, 3, \dots).

After stating that the proposition remains equally valid whether the two inner semicircles lie on the same side (the *arbelos* proper) or embrace one another externally, Pappus establishes three preliminary tangent-circle lemmas (*Props. 15–17, Hultsch I pp. 210–224*):

* **Lemma 1 (Prop. 15)**: If two circles touch at $\Theta$ and a third circle touches both at $E$ and $P$, the chord $EP$ produced meets the line of centers on the radical tangent at $Z$ where $ZE \cdot ZP = Z\Theta^2$.
* **Lemma 2 (Prop. 16)**: For any single circle inscribed tangent to two nested semicircles on baseline $AC$, the square of its center's perpendicular height satisfies a fixed rectangle relation on the base segments cut off by rays from the outer semicircle's endpoints (:just:`III.36`).
* **Lemma 3 (Prop. 17)**: If two consecutive circles centered at $K_n$ and $K_{n+1}$ touch both nested semicircles and touch each other externally at $\Theta$, then the sum of the $n$-th altitude and its diameter stands to its diameter in the exact same ratio as the $(n+1)$-th altitude stands to the $(n+1)$-th diameter:

  .. math::

     \frac{y_n + d_n}{d_n} = \frac{y_{n+1}}{d_{n+1}} \quad \Longleftrightarrow \quad \frac{y_{n+1}}{d_{n+1}} = \frac{y_n}{d_n} + 1.

.. picture:: /_static/constructions/pappus_arbelos_chain.svg
   :alt: Synagoge Book IV Propositions 14–18 — Pappus's Arbelos Tangent Circle Chain (y_n = n d_n)

.. enunciation::

   Let outer semicircle :g:`(O0, A) <g3:( O0 A )>` on diameter :g:`AC <g3:[ A C ]>` be divided at :g:`D <g3:D>` into inner semicircles :g:`(O1, A) <g3:( O1 A )>` of radius $r_1$ and :g:`(O2, D) <g3:( O2 D )>` of radius $r_2$ ($R = r_1 + r_2$). Inscribe circles :g:`C1 <g3:( K1 X1 )>`, :g:`C2 <g3:( K2 X2 )>`, :g:`C3 <g3:( K3 X3 )>`, :g:`C4 <g3:( K4 X4 )>`, $\dots$ mutually tangent in the :term:`arbelos <arbelos>`, and drop altitudes :g:`P1K1 <g3:[ P1 K1 ]>`, :g:`P2K2 <g3:[ P2 K2 ]>`, :g:`P3K3 <g3:[ P3 K3 ]>`, :g:`P4K4 <g3:[ P4 K4 ]>` perpendicular to :g:`AC <g3:[ A C ]>`. Then for every $n \ge 1$, the altitude $y_n = |P_n K_n|$ equals $n$ times the diameter $d_n$ of circle $C_n$.

.. step::

   Along baseline :g:`AC <g3:[ A C ]>` with $r_1 = 2$ and $r_2 = 1$ ($R = 3$), place :g:`A <g3:A>` $= (0, 0)$, :g:`D <g3:D>` $= (4, 0)$, and :g:`C <g3:C>` $= (6, 0)$, and describe outer semicircle :g:`(O0, A) <g3:( O0 A )>` centered at :g:`O0 <g3:O0>` $= (3, 0)$ together with inner semicircles :g:`(O1, A) <g3:( O1 A )>` and :g:`(O2, D) <g3:( O2 D )>` centered at :g:`O1 <g3:O1>` $= (2, 0)$ and :g:`O2 <g3:O2>` $= (5, 0)$.

.. step::

   Inscribe the base circle :g:`C1 <g3:( K1 X1 )>` tangent to all three semicircles (*Prop. 18 base step, Hultsch I pp. 226–228*). By Lemma 2, its center :g:`K1 <g3:K1>` $= \left(\frac{30}{7}, \frac{12}{7}\right)$ above foot :g:`P1 <g3:P1>` has radius $r_1^{(c)} = \frac{6}{7}$ and diameter $d_1 = \frac{12}{7}$, so altitude :g:`P1K1 <g3:[ P1 K1 ]>` satisfies $y_1 = \frac{12}{7} = 1 \cdot d_1$.

.. step::

   Inscribe :g:`C2 <g3:( K2 X2 )>` tangent to :g:`(O0, A) <g3:( O0 A )>`, :g:`(O1, A) <g3:( O1 A )>`, and :g:`C1 <g3:( K1 X1 )>`. By Lemma 3 (*Prop. 17*), $\frac{y_2}{d_2} = \frac{y_1 + d_1}{d_1} = 1 + 1 = 2$. Indeed :g:`K2 <g3:K2>` $= \left(3, \frac{12}{5}\right)$ has radius $r_2^{(c)} = \frac{3}{5}$, diameter $d_2 = \frac{6}{5}$, and altitude :g:`P2K2 <g3:[ P2 K2 ]>` $= \frac{12}{5} = 2\,d_2$.

.. step::

   Repeat the inductive recurrence $\frac{y_{n+1}}{d_{n+1}} = \frac{y_n}{d_n} + 1$ (*Hultsch I p. 228*, ``καὶ τοῦτο συμβαῖνον ἐπὶ τὸ ἄπειρον ἀποδειχθήσεται``): circle :g:`C3 <g3:( K3 X3 )>` at :g:`K3 <g3:K3>` $= \left(2, \frac{12}{5}\right)$ ($\Delta_3 = 15$) has diameter $d_3 = \frac{4}{5}$ and altitude :g:`P3K3 <g3:[ P3 K3 ]>` $= \frac{12}{5} = 3\,d_3$; and circle :g:`C4 <g3:( K4 X4 )>` at :g:`K4 <g3:K4>` $= \left(\frac{15}{11}, \frac{24}{11}\right)$ ($\Delta_4 = 22$) has diameter $d_4 = \frac{6}{11}$ and altitude :g:`P4K4 <g3:[ P4 K4 ]>` $= \frac{24}{11} = 4\,d_4$. Moreover, every center $K_n$ lies on the fixed locus ellipse with foci :g:`O1 <g3:O1>` and :g:`O0 <g3:O0>` since $|K_n O_0| + |K_n O_1| = (R - r_n) + (r_1 + r_n) = R + r_1 = 5$.

*In Chapters 29–68 of Book IV (Hultsch I pp. 230–303), Pappus adds the odd-multiple corollary $y_n = (2n - 1)r_n$ when the second inner semicircle degenerates to a point at $A$, and then investigates the linear curves of antiquity—the spiral of :person:`Archimedes <archimedes>` (proving the sector-area one-third theorem), the conchoid of :person:`Nicomedes <nicomedes>`, the quadratrix of :person:`Dinostratus <dinostratus>`, and three solid hyperbola/:term:`neusis <neusis>` constructions for trisecting any rectilinear angle.*
