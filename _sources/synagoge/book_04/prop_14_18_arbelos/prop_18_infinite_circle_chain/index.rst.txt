:order: 5
:layout: book
:type: book
:title: Proposition 18: Induction for the Infinite Circle Chain
:canonical_id: Syn. IV.18
:folio: 0241
:excerpt: Complete inductive proof of the endless tangent circle chain in the arbelos (y_n = n * d_n), exact rational coordinates for (r1, r2) = (2, 1), and the focal ellipse of centers.
:tracks: English: index | Greek: el | Summary: summary | Notes: notes

Proposition 18: Induction for the Infinite Circle Chain
=======================================================

.. rubric:: *Synagoge* Book IV, Ch. 26 / Prop. 18 (:cite:`Hultsch I, pp. 224–228 <hultsch:1876>`; App. IV, p. 1229) · Original English Translation

.. folio:: 0241
   :page: 1229

.. picture:: /_static/constructions/pappus_arbelos_chain.svg
   :alt: Synagoge Book IV Proposition 18 — Pappus's Arbelos Tangent Circle Chain (y_n = n d_n)

.. step::

   Along baseline :g:`AC <g3:[ A C ]>` with $r_1 = 2$ and $r_2 = 1$ ($R = 3$), place :g:`A <g3:A>` $= (0, 0)$, :g:`D <g3:D>` $= (4, 0)$, and :g:`C <g3:C>` $= (6, 0)$, and describe outer semicircle :g:`(O0, A) <g3:( O0 A )>` centered at :g:`O0 <g3:O0>` $= (3, 0)$ together with inner semicircles :g:`(O1, A) <g3:( O1 A )>` and :g:`(O2, D) <g3:( O2 D )>` centered at :g:`O1 <g3:O1>` $= (2, 0)$ and :g:`O2 <g3:O2>` $= (5, 0)$.

.. step::

   Inscribe base circle :g:`C1 <g3:( K1 X1 )>` tangent to all three semicircles (*Prop. 18 base step, Hultsch I pp. 226–228*). By Lemma 2 (*Prop. 16*), center :g:`K1 <g3:K1>` $= \left(\frac{30}{7}, \frac{12}{7}\right)$ above foot :g:`P1 <g3:P1>` has radius $r_1^{(c)} = \frac{6}{7}$ and diameter $d_1 = \frac{12}{7}$, so altitude :g:`P1K1 <g3:[ P1 K1 ]>` satisfies $y_1 = \frac{12}{7} = 1 \cdot d_1$.

.. step::

   Inscribe :g:`C2 <g3:( K2 X2 )>` tangent to :g:`(O0, A) <g3:( O0 A )>`, :g:`(O1, A) <g3:( O1 A )>`, and :g:`C1 <g3:( K1 X1 )>`. By Lemma 3 (*Prop. 17*), $\frac{y_2}{d_2} = \frac{y_1 + d_1}{d_1} = 1 + 1 = 2$. Indeed :g:`K2 <g3:K2>` $= \left(3, \frac{12}{5}\right)$ has radius $r_2^{(c)} = \frac{3}{5}$, diameter $d_2 = \frac{6}{5}$, and altitude :g:`P2K2 <g3:[ P2 K2 ]>` $= \frac{12}{5} = 2\,d_2$.

.. step::

   Repeat the inductive recurrence $\frac{y_{n+1}}{d_{n+1}} = \frac{y_n}{d_n} + 1$ (*Hultsch I p. 228*, ``καὶ τοῦτο συμβαῖνον ἐπὶ τὸ ἄπειρον ἀποδειχθήσεται``): circle :g:`C3 <g3:( K3 X3 )>` at :g:`K3 <g3:K3>` $= \left(2, \frac{12}{5}\right)$ ($\Delta_3 = 15$) has diameter $d_3 = \frac{4}{5}$ and altitude :g:`P3K3 <g3:[ P3 K3 ]>` $= \frac{12}{5} = 3\,d_3$; and circle :g:`C4 <g3:( K4 X4 )>` at :g:`K4 <g3:K4>` $= \left(\frac{15}{11}, \frac{24}{11}\right)$ ($\Delta_4 = 22$) has diameter $d_4 = \frac{6}{11}$ and altitude :g:`P4K4 <g3:[ P4 K4 ]>` $= \frac{24}{11} = 4\,d_4$. Moreover, every center $K_n$ lies on the fixed locus ellipse with foci :g:`O1 <g3:O1>` and :g:`O0 <g3:O0>` since $|K_n O_0| + |K_n O_1| = (R - r_n) + (r_1 + r_n) = R + r_1 = 5$.
