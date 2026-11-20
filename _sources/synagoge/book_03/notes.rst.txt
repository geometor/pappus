:layout: book
:title: Book III · Philological & Mathematical Notes
:order: 91
:folio: 0232

.. _synagoge-b3-notes:

Book III · Philological & Mathematical Notes
============================================

.. rubric:: Textual Transmission, Reception & Cross-Corpus Commentary

.. folio:: 0232
   :page: 1220

1. Pandrosion and Fourth-Century Alexandrian Pedagogy (*Hultsch I, p. 30, l. 3*)
--------------------------------------------------------------------------------

In *Codex Vaticanus Graecus* 218 (the 10th-century archetype from which all extant manuscripts of the :term:`Synagoge <synagoge>` descend), the opening vocative of Book III reads ``ὦ κρατίστη Πανδροσίων`` ("O most noble Pandrosion"). In his 1588 Latin *editio princeps*, :cite:`Federico Commandino <commandino:1588>` emended the feminine superlative ``κρατίστη`` to masculine, assuming the addressee was a male teacher. :person:`Friedrich Hultsch <hultsch>` (:cite:`1876, Vol. I, p. 30 apparatus <hultsch:1876>`) restored the manuscript's feminine form, establishing **Pandrosion of Alexandria** as one of the earliest documented women mathematicians in antiquity—nearly two generations before Hypatia (c. 355–415 CE).

2. Two Versions of the Semicircle Mean Construction (*Props. 28–30 vs. Prop. 16*)
---------------------------------------------------------------------------------

As :cite:`Heath (1921, Vol. II, pp. 367–369) <heath:1921>` and ``geometor/euclid`` (:cite:`Heath 1926, Vol. II, p. 211 <heath:1926>`, note on *Elements* VI.13) observe, Book III contains **two** semicircular mean constructions:

1. **Pappus's Canonical Three-in-One Semicircle** (*Chs. 40–43, Hultsch I pp. 80–84*, modeled in :func:`~geometor.pappus.construct_three_means`): Given $AD = a$ and $DC = b$ contiguous along diameter $AC$, a single perpendicular $DB$ and a single altitude $DF \perp OB$ exhibit $A = OB$, $G = DB$, and $H = BF$ simultaneously on one diagram.
2. **The Anonymous Craftsman's Tangential Variant** (*Ch. 39, Hultsch I pp. 70–72*): A geometer (*τις*) proposed exhibiting the three means using an external secant and tangent, which Pappus critiques because the presenter omitted the proof of $(a - H) : (H - b) = a : b$.

3. Coordinate Check on the External Harmonic Conjugate $T$
----------------------------------------------------------

With $A = (0, 0)$, $D = (a, 0)$, and $C = (a + b, 0)$ ($a < b$), center $O = \left(\frac{a+b}{2}, 0\right)$ and $B = (a, \sqrt{ab})$. Since $OB$ has vector $\left(\frac{a - b}{2}, \sqrt{ab}\right)$, the circle tangent at $B$ perpendicular to $OB$ meets $y = 0$ at $x_T = -\frac{a(a + b)}{b - a}$. For $(a, b) = (9, 16)$, $x_T = -\frac{225}{7}$, yielding $\operatorname{CR}(A, C; D, T) = -1$.

4. Cross-References in the GEOMETOR Canon
-----------------------------------------

* **Euclid's Elements** (``geometor/euclid`` & ``geometor/elements``): *Elements* II.5, III.31, VI.8, VI.13, and XIII.13–18 (re-inscribed analytically in Book III Chs. 54–58).
* **Golden Ratio Engine** (``geometor/divine``): Setting $(a, b) = (1, \phi^2)$ embeds $G = \phi$ cleanly inside $\mathbb{Q}(\phi)$.
