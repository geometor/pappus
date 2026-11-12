.. _synagoge-b7-en:

===============================================================================================
Book VII · The Treasury of Analysis, Centroid Rule & Hexagon Collinearity (*Translation*)
===============================================================================================

.. rubric:: *Synagoge* Book VII, Preface to Hermodorus & Props. 129, 131, 138–139 (:cite:`Hultsch II, pp. 634–688, 868–894 <hultsch:1877>`) · Original English Translation from Hultsch's Greek

.. _sec-b7-en-analysis-synthesis:

1. Preface to Hermodorus: Analysis, Synthesis, and the Thirty-Three Books
-------------------------------------------------------------------------

*Hultsch Vol. II, pp. 634–638 (Book VII, Chs. 1–3)*

That body of doctrine which is called the :term:`Treasury of Analysis <topos-analyomenos>` (*ὁ καλούμενος ἀναλυόμενος τόπος*), my son :person:`Hermodorus <hermodorus>`, is—taken as a whole—a specialized mathematical resource prepared, after the composition of the common *Elements*, for those who wish to acquire in geometric inquiries the power of discovering solutions to problems set before them; and it was written exclusively for this purpose by three principal men: :person:`Euclid <euclid>` the author of the *Elements*, :person:`Apollonius of Perga <apollonius>`, and :person:`Aristaeus the Elder <aristaeus>`—proceeding entirely by way of :term:`analysis <analysis>` and :term:`synthesis <synthesis>`.

**Analysis** (*ἀνάλυσις*), then, is the path from that which is sought, assumed as if already admitted, through its successive consequences toward something admitted in synthesis. For in analysis, assuming the thing sought as having already come to be (*ὡς γεγονὸς ὑποθέμενοι*), we examine that antecedent from which this follows, and again the antecedent of that, until by thus retracing our steps (*ἀναποδίζοντες*) we arrive at something already known or holding the rank of a first principle; and such a procedure we call *analysis*, as being a **solution backward** (*ἀνάπαλιν λύσις*).

In **synthesis** (*σύνθεσις*), conversely, reversing our course, we set down as already done that last point apprehended in the analysis, and arranging in their natural order as consequences what had previously been antecedents, and fitting them one to another, we arrive at the final completion of the construction of what was sought; and this we call *synthesis*.

Now there are **two genera of analysis**:

1. The **theoretical** (*θεωρηματικόν*), which seeks after truth: assuming what is proposed as existing and true, we advance through its consequences, as though true and existing by hypothesis, up to something admitted. If that admitted endpoint be **true**, what was sought will also be true, and its proof will be the reverse synthesis; but if we encounter something admitted to be **false**, what was sought will also be false.
2. The **problematic** (*προβληματικόν*), which seeks to supply something proposed: assuming what is proposed as known, we advance through its consequences, as though true, up to something admitted. If that endpoint is **possible and procurable** (*δυνατόν τε καὶ ποριστόν*)—what mathematicians call *given* (*δεδομένον*)—then what was proposed will also be possible, and again the proof will correspond inversely to the analysis; if we encounter something admitted to be **impossible**, the problem will likewise be impossible. That part of the inquiry which specifies beforehand *when, how, and in how many ways* the problem will be possible is called its :term:`diorismos <diorismos>`.

The **thirty-three books** of the *Treasury of Analysis* up to :person:`Apollonius <apollonius>`, arranged in curricular order (*Hultsch II p. 636*), are these:

1. :cite:`Euclid's Data <euclid:data>` (*Δεδομένα*, 1 book);
2. :cite:`Apollonius's Cutting Off of a Ratio <apollonius:cutting-off-ratio>` (*Λόγου ἀποτομή*, 2 books);
3. Apollonius's *Cutting Off of an Area* (*Χωρίου ἀποτομή*, 2 books);
4. Apollonius's *Determinate Section* (*Διωρισμένη τομή*, 2 books);
5. Apollonius's *Tangencies* (*Ἐπαφαί*, 2 books);
6. :cite:`Euclid's Porisms <euclid:porisms>` (*Πορίσματα*, 3 books);
7. Apollonius's *Inclinations* (*Νεύσεις*, 2 books);
8. Apollonius's *Plane Loci* (*Τόποι ἐπίπεδοι*, 2 books);
9. :cite:`Apollonius's Conics <apollonius:conics>` (*Κωνικά*, 8 books);
10. :cite:`Aristaeus's Solid Loci <aristaeus:solid-loci>` (*Τόποι στερεοί*, 5 books);
11. :cite:`Euclid's Surface Loci <euclid:surface-loci>` (*Τόποι πρὸς ἐπιφανείᾳ*, 2 books);
12. :person:`Eratosthenes's <eratosthenes>` *On Means* (*Περὶ μεσοτήτων*, 2 books).

.. _sec-b7-en-locus-guldin:

2. The Multi-Line Locus Problem & the Pappus–Guldinus Centroid Rule
-------------------------------------------------------------------

*Hultsch Vol. II, pp. 676–683 (Book VII, Chs. 36–42)*

In reviewing :cite:`Apollonius's Conics <apollonius:conics>`, Pappus records the celebrated **Three- and Four-Line Locus** (*ὁ ἐπὶ τρεῖς καὶ τέσσαρας γραμμὰς τόπος*, *pp. 676–680*): if straight lines are drawn from a point at given angles to three (or four) lines given in position, and the rectangle contained by two of them bears a given ratio to the square on the third (or to the rectangle contained by the remaining two), the locus of the point is a **conic section**. When generalized to five, six, or arbitrarily many $n$ lines using **compound ratios** (*λόγοι συγκείμενοι*)—so that no impossible dimension beyond the cube or solid parallelepiped need be invoked—the ancients left the higher locus unconstructed, bequeathing the exact challenge through which :person:`René Descartes <descartes>` launched analytic geometry in :cite:`La Géométrie (1637) <descartes:geometrie>`.

Immediately thereafter (*Hultsch II, p. 682*), Pappus announces his universal **Centroid Theorem for Solids and Surfaces of Revolution** (rediscovered thirteen centuries later by :person:`Paul Guldin <guldin>`):

    *Figures generated by a complete revolution of a plane lamina about an axis not cutting it have to one another the **ratio compounded** of the ratio of the revolving areas and the ratio of the straight lines drawn perpendicularly from their :term:`centers of gravity <kentron-barous>` to the axes of revolution—that is, the ratio of the circumferences traced by their centers of gravity:*

    .. math::

       \frac{V_1}{V_2} = \left(\frac{A_1}{A_2}\right)\left(\frac{\bar{r}_1}{\bar{r}_2}\right)
       \quad \Longleftrightarrow \quad
       V = A \cdot (2\pi \bar{r}), \qquad S = L \cdot (2\pi \bar{r}).

.. _sec-b7-en-cross-ratio:

3. Propositions 129 & 131: Cross-Ratio Invariance & Complete-Quadrilateral Harmonics
------------------------------------------------------------------------------------

*Hultsch Vol. II, pp. 870–877 (Lemmas III & V to Euclid's Porisms)*

Among the thirty-eight :term:`lemmas <lemma>` supplied by Pappus for :cite:`Euclid's lost Porisms <euclid:porisms>`, **Proposition 129** (*Hultsch II, p. 870*) proves that if three rays issuing from a common apex $O$ together with a fourth line through $O$ cut two distinct transversals $(A, B, C, D)$ and $(A', B', C', D')$, then the compound ratio of segments cut off on the first transversal equals the compound ratio cut off on the second:

.. math::

   \frac{AC \cdot BD}{AD \cdot BC} = \frac{A'C' \cdot B'D'}{A'D' \cdot B'C'}
   \quad \Longleftrightarrow \quad
   \operatorname{CR}(A, B; C, D) = \operatorname{CR}(A', B'; C', D').

In **Proposition 131** (*Hultsch II, p. 874*), Pappus applies this projective invariance to the **complete quadrilateral**, showing that opposite sides and diagonals cut any transversal in **harmonic division** ($\operatorname{CR} = -1$)—yielding pure straightedge harmonic conjugate construction (:func:`~geometor.pappus.construct_harmonic_fourth`) and generating 81 collinear harmonic tetrads across the Pappus–Steiner web (:g:`S+ <g2:S1>`, :g:`S- <g2:S2>`):

.. picture:: /_static/constructions/pappus_harmonics.svg
   :alt: Synagoge Book VII Propositions 129 & 131 — Emergent Harmonic Ranges in the Pappus Configuration

.. _sec-b7-en-hexagon-theorems:

4. Propositions 138 & 139: Pappus's Hexagon Collinearity Theorems
-----------------------------------------------------------------

*Hultsch Vol. II, pp. 884–889 (Lemmas XII & XIII to Euclid's Porisms)*

Crowning the *Porisms* lemmas are **Proposition 138** (when the two carrier lines are parallel, $a \parallel b$) and **Proposition 139** (when the two carrier lines intersect at an apex $O$). Pappus establishes collinearity by applying compound ratios (equivalent to Menelaus's transversal theorem or Prop. 129's cross-ratio invariance) without drawing a single circle.

.. picture:: /_static/constructions/pappus_hexagon.svg
   :alt: Synagoge Book VII Proposition 139 — Pappus's General Intersecting-Carrier Hexagon Theorem

.. enunciation::

   **Proposition 139 (Hultsch II, pp. 886–889)**: Let two straight lines :g:`a <g1:[ A0 A2 ]>` and :g:`b <g1:[ B0 B2 ]>` meet at :g:`O <g1:O>`, carrying three points :g:`A0 <g1:A0>`, :g:`A1 <g1:A1>`, :g:`A2 <g1:A2>` on :g:`a <g1:[ A0 A2 ]>` and three points :g:`B0 <g1:B0>`, :g:`B1 <g1:B1>`, :g:`B2 <g1:B2>` on :g:`b <g1:[ B0 B2 ]>`. If opposite cross-joins :g:`A0B1 <g1:[ A0 B1 ]>` & :g:`A1B0 <g1:[ A1 B0 ]>` meet at :g:`M01 <g1:M01>`, :g:`A2B0 <g1:[ A2 B0 ]>` & :g:`A0B2 <g1:[ A0 B2 ]>` meet at :g:`M20 <g1:M20>`, and :g:`A1B2 <g1:[ A1 B2 ]>` & :g:`A2B1 <g1:[ A2 B1 ]>` meet at :g:`M12 <g1:M12>`, then the three points :g:`M01 <g1:M01>`, :g:`M20 <g1:M20>`, and :g:`M12 <g1:M12>` **lie on a single straight line** :g:`p <g1:[ M01 M12 ]>`.

.. step::

   Set carrier :g:`a <g1:[ A0 A2 ]>` with :g:`A0 <g1:A0>` $= (0, 0)$, :g:`A1 <g1:A1>` $= (2, 0)$, :g:`A2 <g1:A2>` $= (5, 0)$ and carrier :g:`b <g1:[ B0 B2 ]>` with :g:`B0 <g1:B0>` $= (0, 2)$, :g:`B1 <g1:B1>` $= (2, 3)$, :g:`B2 <g1:B2>` $= (6, 5)$, concurring at perspective apex :g:`O <g1:O>` $= (-4, 0)$.

.. step::

   Form the three opposite cross-join intersections of hexagon :g:`A0B1A2B0A1B2 <g1:< A0 B1 A2 B0 A1 B2 >>`:

   .. math::

      M_{01} = \left(\frac{4}{5}, \frac{6}{5}\right), \qquad
      M_{20} = \left(\frac{60}{37}, \frac{50}{37}\right), \qquad
      M_{12} = \left(\frac{10}{3}, \frac{5}{3}\right).

.. step::

   By **Proposition 129**, projecting from :g:`A0 <g1:A0>` and :g:`A2 <g1:A2>` onto cross-joins :g:`A1B0 <g1:[ A1 B0 ]>` and :g:`A1B2 <g1:[ A1 B2 ]>` equates their four-point cross-ratios; since the two ranges share their apex :g:`A1 <g1:A1>`, the joins connecting corresponding points concur, forcing :g:`M01 <g1:M01>`, :g:`M20 <g1:M20>`, and :g:`M12 <g1:M12>` onto the single **Pappus line** :g:`p <g1:[ M01 M12 ]>` ($-7x + 38y = 40$).

Permuting $(B_0, B_1, B_2)$ across all $3! = 6$ elements of $S_3$ (:func:`~geometor.pappus.construct_pappus_configuration`) yields **six Pappus lines** that concur three-by-three by parity at :person:`Jakob Steiner's <steiner>` **Star points** :g:`S+ <g7:S1>` and :g:`S- <g7:S2>` along :g:`Steiner line <g7:[ S1 S2 ]>` (and at :g:`S+ <g8:S1>` $= (\frac{90}{73}, \frac{38}{73})$ in **Proposition 138**'s parallel-carrier configuration):

.. picture:: /_static/constructions/pappus_steiner.svg
   :alt: Six S_3 Pappus Lines Concurring at Steiner Star Points S+ and S-

.. picture:: /_static/constructions/pappus_parallel_steiner.svg
   :alt: Synagoge Book VII Proposition 138 — Parallel Carriers and Even Steiner Point S+ = (90/73, 38/73)

*For deep explorations of the $S_3$ Steiner web, golden perspectivities in $\mathbb{Q}(\phi)$, and :person:`Blaise Pascal's <pascal>` 60-line smooth-conic Hexagrammum Mysticum (1640), see the companion :doc:`Projective Theorems <../../theorems/index>` collection.*
