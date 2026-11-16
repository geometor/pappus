:layout: book
:title: Book III · Philological & Mathematical Notes
:order: 91

.. _synagoge-b3-notes:

=========================================================================
Book III · Philological & Mathematical Notes (*Pandrosion & Medieties*)
=========================================================================

.. rubric:: Textual Transmission, Reception & Cross-Corpus Commentary

1. Pandrosion and Fourth-Century Alexandrian Pedagogy (*Hultsch I, p. 30, l. 3*)
--------------------------------------------------------------------------------

In *Codex Vaticanus Graecus* 218 (the 10th-century archetype from which all extant manuscripts of the :term:`Synagoge <synagoge>` descend), the opening vocative of Book III reads ``ὦ κρατίστη Πανδροσίων`` ("O most noble Pandrosion"). In his 1588 Latin *editio princeps*, :cite:`Federico Commandino <commandino:1588>` emended the feminine superlative ``κρατίστη`` to masculine, assuming the addressee was a male teacher. :person:`Friedrich Hultsch <hultsch>` (:cite:`1876, Vol. I, p. 30 apparatus <hultsch:1876>`) restored the manuscript's feminine form, establishing **Pandrosion of Alexandria** as one of the earliest documented women mathematicians in antiquity—nearly two generations before Hypatia (c. 355–415 CE). While Pappus polemically critiques a student of Pandrosion's circle who mistook the Delian cube-duplication problem for a plane locus, the mathematical sophistication of Book III (covering solid *neuseis*, all ten Neo-Pythagorean medieties, paradoxical inscribed triangles, and an alternative analytical inscription of the five Platonic solids in Chs. 54–58) testifies to an active competitive school of higher geometry in early fourth-century Alexandria.

2. Two Versions of the Semicircle Mean Construction (*Props. 28–30 vs. Prop. 16*)
---------------------------------------------------------------------------------

As :cite:`Heath (1921, Vol. II, pp. 367–369) <heath:1921>` and ``geometor/euclid`` (:cite:`Heath 1926, Vol. II, p. 211 <heath:1926>`, note on *Elements* VI.13) observe, Book III contains **two** semicircular mean constructions:

1. **Pappus's Canonical Three-in-One Semicircle** (*Chs. 40–43, Hultsch I pp. 80–84*, modeled in :func:`~geometor.pappus.construct_three_means`): Given $AD = a$ and $DC = b$ contiguous along diameter $AC$, a single perpendicular $DB$ and a single altitude $DF \perp OB$ exhibit $A = OB$, $G = DB$, and $H = BF$ simultaneously on one diagram, yielding a visual proof without words of both $A \cdot H = G^2$ and $A \ge G \ge H$.
2. **The Anonymous Craftsman's Tangential Variant** (*Ch. 39, Hultsch I pp. 70–72*): A clever geometer (*τις*) proposed exhibiting the three means using an external secant and tangent, which Pappus critiques because the presenter omitted the proof that the third segment actually satisfies the harmonic definition $(a - H) : (H - b) = a : b$—a gap Pappus supplies before presenting his cleaner internal construction.

3. Coordinate Check on the External Harmonic Conjugate $T$
----------------------------------------------------------

With $A = (0, 0)$, $D = (a, 0)$, and $C = (a + b, 0)$ ($a < b$), center $O = \left(\frac{a+b}{2}, 0\right)$ and $B = (a, \sqrt{ab})$. Since $OB$ has vector $\left(\frac{a - b}{2}, \sqrt{ab}\right)$, the circle tangent at $B$ perpendicular to $OB$ meets the diameter line $y = 0$ at

.. math::

   x_T = a - \frac{2ab}{b - a} = -\frac{a(a + b)}{b - a}.

For the rational Pythagorean preset $(a, b) = (9, 16)$, $x_T = -\frac{9 \cdot 25}{7} = -\frac{225}{7}$. Computing the collinear cross-ratio of $(A, C; D, T)$ along $y = 0$:

.. math::

   (A, C; D, T) = \frac{(0 - 9)\left(25 - \left(-\frac{225}{7}\right)\right)}{\left(0 - \left(-\frac{225}{7}\right)\right)(25 - 9)} = \frac{-9 \cdot \frac{400}{7}}{\frac{225}{7} \cdot 16} = \frac{-3600}{3600} = -1.

4. Cross-References in the GEOMETOR Canon
-----------------------------------------

* **Euclid's Elements** (``geometor/euclid`` & ``geometor/elements``): *Elements* II.5 ($AD \cdot DC + OD^2 = OC^2$), III.31 (angle in a semicircle), VI.8 (right-triangle altitude similarity), VI.13 (mean proportional construction), and XIII.13–18 (five Platonic solids, re-inscribed analytically by Pappus in Book III Chs. 54–58).
* **Golden Ratio Engine** (``geometor/divine``): Setting $(a, b) = (1, \phi^2)$ embeds the golden ratio $G = \phi$ directly between $A = \frac{\phi+2}{2}$ and $H = \frac{2\phi^2}{\phi+2}$ inside $\mathbb{Q}(\phi)$.
