:order: 5
:layout: book
:type: book
:title: Proposition 131: Complete-Quadrilateral Harmonic Conjugates
:canonical_id: Syn. VII.131
:folio: 0276
:excerpt: Lemma V to Euclid's Porisms: straightedge construction of the fourth harmonic conjugate from a complete quadrilateral and the 81 emergent collinear harmonic tetrads.
:tracks: English: index | Greek: el | Summary: summary | Notes: notes

Proposition 131: Complete-Quadrilateral Harmonic Conjugates
===========================================================

.. rubric:: *Synagoge* Book VII, Proposition 131 (:cite:`Hultsch II, pp. 874–876 <hultsch:1877>`, Lemma V to Euclid's *Porisms*; App. IV, pp. 1264, 1269)

.. folio:: 0276
   :page: 1264

In **Proposition 131**, Pappus applies cross-ratio invariance to the geometry of the **complete quadrilateral**, demonstrating that opposite sides and diagonals cut any transversal line across the figure in **harmonic division** ($\operatorname{CR} = -1$).

.. picture:: /_static/constructions/pappus_harmonics.svg
   :alt: Synagoge Book VII Proposition 131 — Emergent Harmonic Ranges in the Pappus Configuration

.. enunciation::

   **Proposition 131 (Harmonic Division on a Complete Quadrilateral)**: Given three collinear points $A, B, C$, to find the fourth point $D$ on their line such that $(A, B; C, D)$ is divided harmonically—that is:

   .. math::

      \frac{AC}{CB} = \frac{AD}{DB} \quad \Longleftrightarrow \quad \operatorname{CR}(A, B; C, D) = -1.

.. step::

   **Construction (Straightedge Alone)**: Take any point $P$ not on line $AB$, and draw rays $PA, PB, PC$. From any point $Q$ on $PB$, draw a line through $C$ meeting $PA$ at $R$. Let $AQ$ and $BR$ intersect at $S$. The join $PS$ meets line $AB$ at the fourth harmonic point $D$.

.. step::

   **Demonstration**: The four vertices $P, Q, R, S$ form a complete quadrilateral whose three pairs of opposite sides are $(PQ, RS)$, $(PR, QS)$, and $(PS, QR)$. Central projection from $P$ onto $QR$ followed by projection from $A$ back onto line $AB$ preserves the cross-ratio, forcing $\operatorname{CR}(A, B; C, D) = -1$.

Archival Plate (*Hultsch Vol. III, Appendix IV, p. 1269*)
---------------------------------------------------------

.. picture:: 0281.g1.png
   :alt: Archival woodcut plate 0281.g1 — Collinear four-point range comparison (Hultsch III, p. 1269)
   :caption: Original Hultsch bitmap (folio 0281, p. 1269): dual four-point collinear point ranges αβγη and δεζθ.

.. picture:: 0281.g1.svg
   :alt: Calibrated interactive vector plate 0281.g1 — Collinear four-point ranges
   :caption: Calibrated .euclid-graphic vectorization of plate 0281.g1.
