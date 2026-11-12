.. _synagoge-b4-notes:

================================================================================
Book IV · Philological & Mathematical Notes (*Affine Area & Circle Inversion*)
================================================================================

.. rubric:: Synthetic Proofs, Inversion Duality & Cross-Corpus Commentary

1. Affine Invariance of Proposition 1 (*Hultsch I, pp. 176–179*)
----------------------------------------------------------------

Pappus concludes Proposition 1 with explicit pride: ``καὶ ἔστι τοῦτο καθολικώτερον πολλῷ τοῦ ἐν τοῖς ὀρθογωνίοις ἐπὶ τῶν τετραγώνων ἐν τοῖς Στοιχείοις δεδειγμένου`` (*"and this is far more general than what is proved in the Elements on squares in right-angled triangles"*). Whereas :cite:`Euclid's Elements I.47 <euclid:elements>` relies on the metric congruence of rotated triangles ($\triangle ABD \cong \triangle FBC$ via right-angle addition, :just:`I.4`) and *Elements* VI.31 relies on proportionality of similar figures on a right triangle (:just:`VI.8`, :just:`VI.19`), **Pappus's proof uses zero circles, zero right angles, and zero metric ratios**: it belongs purely to **equiaffine geometry** (parallelism and area-preserving shears, :just:`I.34`–:just:`I.35`). Applying any invertible linear transformation $T \in \operatorname{GL}_2(\mathbb{R})$ to a Pythagorean windmill immediately yields a general Pappus area configuration. See also ``geometor/euclid`` (:cite:`Heath 1926, Vol. I, pp. 366–367 <heath:1926>`).

2. Synthetic Secant Lemmas vs. Circular Inversion in the *Arbelos* (*Props. 14–18*)
-----------------------------------------------------------------------------------

Modern expositions since Jakob Steiner (1826) prove Pappus's :term:`arbelos <arbelos>` altitude law $y_n = n\,d_n$ in three lines by **circular inversion** centered at the left endpoint $A = (0, 0)$ with inversion circle radius $k = 2\sqrt{R r_1}$:

1. Because the outer semicircle $(O_0, A)$ on diameter $AC = [0, 2R]$ and the left inner semicircle $(O_1, A)$ on diameter $AD = [0, 2r_1]$ both pass through the center of inversion $A$ with vertical tangents there, inversion in $(A, k)$ maps $(O_0, A)$ and $(O_1, A)$ onto two **parallel vertical straight lines** $u = 2r_1$ and $u = 2R$ separated by constant strip width $2r_2$.
2. The right inner semicircle $(O_2, D)$ maps onto the circle $C_0'$ of diameter $2r_2$ resting directly on the horizontal axis $v = 0$ between those two vertical lines, and the entire chain $C_1, C_2, \dots, C_n$ maps onto a vertical stack of congruent circles $C_1', C_2', \dots, C_n'$ of identical diameter $2r_2$, whose centers sit at heights $v_n' = 2n\,r_2 = n\,d'$.
3. Because inversion from $A$ scales both a tangent circle's diameter and its center's perpendicular height above $AC$ by the same factor (up to a classical secant-tangent power correction proved synthetically in Pappus's Lemmas 15–17 via :just:`III.36`), the integer ratio $y_n / d_n = v_n' / d' = n$ is **strictly invariant**!

What makes Pappus's synthetic proof in *Props. 15–18* (*Hultsch I pp. 210–228*) historically remarkable is that Lemma 15 (collinearity of the radical center $Z$ with external/internal contact points $E, P$ and equality $ZE \cdot ZP = Z\Theta^2$) **is literally circular inversion executed in pure Euclidean ratio language** fifteen centuries before Apollonian/Steinerian inversion was named—compare ``geometor/altshiller-court`` (Chapter IX, *Inversion*) and :cite:`Ptolemy's Planisphaerium §4 <heath:1921>` in ``geometor/ptolemy``.

3. Notice on $C_2$ and $C_3$ Sharing Equal Height at $(r_1, r_2) = (2, 1)$
--------------------------------------------------------------------------

In the canonical $(r_1, r_2) = (2, 1)$ preset rendered in ``pappus_arbelos_chain.svg``, notice the delightful arithmetic symmetry at $n = 2$ and $n = 3$:

* At $n = 2$: $\Delta_2 = 6 + 4 = 10$, so $d_2 = \frac{12}{10} = \frac{6}{5}$ and $y_2 = 2\,d_2 = \frac{12}{5}$.
* At $n = 3$: $\Delta_3 = 6 + 9 = 15$, so $d_3 = \frac{12}{15} = \frac{4}{5}$ and $y_3 = 3\,d_3 = \frac{12}{5}$.

Why do $K_2 = \left(3, \frac{12}{5}\right)$ and $K_3 = \left(2, \frac{12}{5}\right)$ sit at the exact same maximum altitude $y = \frac{12}{5}$? Because all centers $K_n$ lie on the ellipse with foci $O_1 = (2, 0)$ and $O_0 = (3, 0)$, centered at $x = \frac{5}{2}$ with semi-minor axis $b = \sqrt{r_1 R} = \sqrt{6} \approx 2.4495$, and $K_2$ ($x = 3$) and $K_3$ ($x = 2$) straddle the ellipse's apex $x = \frac{5}{2}$ symmetrically!
