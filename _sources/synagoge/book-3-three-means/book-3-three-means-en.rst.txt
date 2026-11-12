.. _synagoge-b3-en:

===========================================================================================
Book III · Problem Hierarchy, Cube Duplication & the Three Classical Means (*Translation*)
===========================================================================================

.. rubric:: *Synagoge* Book III, Chs. 1–27 & 28–43 (*Props. 1–5 & 28–30*, :cite:`Hultsch I, pp. 30–84 <hultsch:1876>`) · Original English Translation from Hultsch's Greek

.. _sec-b3-en-pandrosion-hierarchy:

1. Address to Pandrosion: Theorem, Problem, and the Threefold Hierarchy of Loci
-------------------------------------------------------------------------------

*Hultsch Vol. I, pp. 30–32, 54–56 (Book III, Chs. 1 & 20–22)*

Those of the ancients who wished to examine geometric inquiries with precision, most noble :person:`Pandrosion <pandrosion>`, judged it necessary to distinguish a **problem** (*πρόβλημα*) from a **theorem** (*θεώρημα*). He who proposes a theorem—whatever be the geometric matter set out and whatever attribute he claims follows from those hypotheses—invites us to behold how that consequence holds of necessity; whereas he who sets forth a problem bids us construct something not yet brought into view, and therefore stands under an obligation to determine by a :term:`diorismos <diorismos>` when, how, and in how many ways the construction is possible. If anyone announces a problem whose construction cannot be carried out by the means he assumes, he errs doubly: first in mistaking the nature of the locus to which the inquiry belongs, and second in offering a defective demonstration to learners.

Now some of those who came to us purporting to have studied geometry with you set out an attempted plane construction for finding **two mean proportionals** in continued proportion between two given unequal straight lines—the classic Delian problem of duplicating the cube, since :person:`Hippocrates of Chios <euclid>` and :cite:`Euclid (Elements XI.33) <euclid:elements>` showed that if $a : x = x : y = y : b$, then $a : b = a^3 : x^3$. When we tested their construction rigorously (*Chs. 2–19, Hultsch I pp. 32–54*), their assumed intersection failed to meet the required proportional condition, because the problem is by nature **solid** rather than **plane**.

For we affirm (*Chs. 20–21, Hultsch I pp. 54–56*) that there are **three genera** of geometric problems (:term:`ἐπίπεδα, στερεά, γραμμικά <topos-epipedos-stereos-grammikos>`):

1. **Plane problems** (*ἐπίπεδα*) are those capable of being solved exclusively by means of the straight line and the circumference of the circle; they are justly called *plane* because the lines through which they are found have their generation in a plane.
2. **Solid problems** (*στερεά*) are those whose solution requires the employment of one or more sections of the cone—parabola, hyperbola, or ellipse—for their construction demands surfaces of solid figures, namely conical surfaces.
3. **Linear problems** (*γραμμικά*) comprise a third genus still remaining beyond these: for their construction requires lines other than those just spoken of, possessing a more varied and forced generation (*ποικιλωτέραν καὶ βεβιασμένην τὴν γένεσιν*) arising from irregular surfaces and interwoven motions—such as the spirals (*ἕλικες*) of :person:`Archimedes <archimedes>`, the quadratrices (*τετραγωνίζουσαι*) of :person:`Dinostratus <dinostratus>`, the conchoids (*κογχοειδεῖς*) of :person:`Nicomedes <nicomedes>`, and the cissoids (*κισσοειδεῖς*).

Geometers consider it no small methodological fault (*ἁμάρτημα οὐ μικρόν*) whenever anyone solves a plane problem by conics or higher linear curves, or conversely attempts to force a solid problem—such as the duplication of the cube or the trisection of an arbitrary rectilinear angle—into straight lines and circles alone. Because conic sections are delicate to draw with instruments in the plane, the ancients also devised exact mechanical and :term:`neusis <neusis>` constructions for two mean proportionals (*Chs. 22–27, Props. 1–5, Hultsch I pp. 56–68*): the sliding three-plate *mesolabe* of :person:`Eratosthenes <eratosthenes>`, the conchoidal verging ruler of :person:`Nicomedes <nicomedes>`, the rectangle-and-pivot rule of :person:`Hero of Alexandria <heron>`, and our own semicircular construction equivalent in geometric effect to Hero's.

.. _sec-b3-en-semicircle-means:

2. The Three Classical Means & Their Unified Semicircle Construction
--------------------------------------------------------------------

*Hultsch Vol. I, pp. 68–84 (Book III, Chs. 28–43 / Props. 28–30)*

After our friend the philosopher :person:`Hierius <hierius>` inquired further concerning proportional means, we set out the ancient doctrine of :term:`medieties <mesotes>` (*μεσότητες*) expounded by the Pythagoreans, :person:`Eratosthenes <eratosthenes>`, and :cite:`Nicomachus <nicomachus:introductio>`. Three primary proportions stand first and most ancient among all ten:

* A triple $(a, m, b)$ is in **arithmetic proportion** (*ἀριθμητικὴ μεσότης*) whenever the first exceeds the second by the very same difference by which the second exceeds the third, so that $(a - m) : (m - b) = a : a = 1 : 1$, whence $A = \frac{a + b}{2}$.
* A triple $(a, m, b)$ is in **geometric proportion** (*γεωμετρικὴ μεσότης*, proportion strictly so called) whenever the first has to the second the same ratio that the second has to the third, $(a - m) : (m - b) = a : m = m : b$, whence $G = \sqrt{ab}$.
* A triple $(a, m, b)$ is in **harmonic proportion** (*ἁρμονικὴ μεσότης*) whenever the excess of the first over the second has to the excess of the second over the third the ratio of the first extreme to the third extreme:

  .. math::

     \frac{a - H}{H - b} = \frac{a}{b} \quad \Longleftrightarrow \quad H = \frac{2ab}{a + b}.

How one may exhibit **all three means together inside a single semicircle**—establishing at one glance both the fundamental identity $A \cdot H = G^2$ and the strict ordering $A \ge G \ge H$ (with equality if and only if $a = b$)—is demonstrated as follows (*Chs. 40–43, Hultsch I pp. 72, 80–84*).

.. picture:: /_static/constructions/synagoge_three_means.svg
   :alt: Synagoge Book III — Arithmetic, Geometric, and Harmonic Means in One Semicircle (a = 9, b = 16)

.. enunciation::

   Let two unequal straight segments :g:`AD <g1:[ A C ]>` $= a$ and :g:`DC <g1:[ A C ]>` $= b$ be placed end-to-end along diameter :g:`AC <g1:[ A C ]>` of semicircle :g:`ABC <g1:( O A )>` with center :g:`O <g1:O>`. Erect :g:`DB <g1:[ D B ]>` perpendicular to :g:`AC <g1:[ A C ]>` meeting the circumference at :g:`B <g1:B>`, join radius :g:`OB <g1:[ O B ]>`, and drop :g:`DF <g1:[ D F ]>` perpendicular to :g:`OB <g1:[ O B ]>` at :g:`F <g1:F>`. Then radius :g:`OB <g1:[ O B ]>` is the **arithmetic mean** $A$, ordinate :g:`DB <g1:[ D B ]>` is the **geometric mean** $G$, and segment :g:`BF <g1:[ B F ]>` cut off from the vertex :g:`B <g1:B>` is the **harmonic mean** $H$ of $a$ and $b$; moreover, the tangent :g:`BT <g1:[ B T ]>` at :g:`B <g1:B>` meets diameter :g:`AC <g1:[ A C ]>` produced at the external :term:`harmonic conjugate <harmonike-mesotes>` :g:`T <g1:T>` satisfying $(A, C; D, T) = -1$.

.. step::

   Lay out :g:`A <g1:A>` $= (0, 0)$, division point :g:`D <g1:D>` $= (9, 0)$, and :g:`C <g1:C>` $= (25, 0)$ along diameter :g:`AC <g1:[ A C ]>` ($a = 9$, $b = 16$). Bisect :g:`AC <g1:[ A C ]>` at center :g:`O <g1:O>` $= \left(\frac{25}{2}, 0\right)$ and describe semicircle :g:`ABC <g1:( O A )>`. Because $OA = OC = OB$, radius :g:`OB <g1:[ O B ]>` equals $\frac{a + b}{2} = \frac{25}{2}$, which is the **arithmetic mean** $A$.

.. step::

   Erect the perpendicular at :g:`D <g1:D>` to meet semicircle :g:`ABC <g1:( O A )>` at :g:`B <g1:B>` $= (9, 12)$. By :just:`III.31`, $\angle ABC$ in :g:`triangle ABC <g1:< A C B >>` is right, so by :just:`VI.8` and :just:`VI.13` the altitude :g:`DB <g1:[ D B ]>` is the mean proportional between $AD$ and $DC$: $DB^2 = AD \cdot DC = ab = 144$, giving the **geometric mean** $G = 12$.

.. step::

   Join radius :g:`OB <g1:[ O B ]>` and drop :g:`DF <g1:[ D F ]>` perpendicular to :g:`OB <g1:[ O B ]>` at foot :g:`F <g1:F>` $= \left(\frac{7641}{625}, \frac{588}{625}\right)$. Since right triangles $\triangle ODB$ and $\triangle DFB$ share acute angle $\angle OBD$ at :g:`B <g1:B>`, they are equiangular (:just:`VI.8`), whence $OB : DB = DB : BF$. Therefore

   .. math::

      A \cdot BF = OB \cdot BF = DB^2 = G^2 = ab \quad \Longrightarrow \quad BF = \frac{2ab}{a + b} = \frac{288}{25},

   proving that :g:`BF <g1:[ B F ]>` is the exact **harmonic mean** $H$, and that $G$ is itself the geometric mean between $A$ and $H$ ($A \cdot H = G^2$).

.. step::

   Observe the nested right triangles $\triangle ODB$ (hypotenuse :g:`OB <g1:[ O B ]>`, leg :g:`DB <g1:[ D B ]>`) and $\triangle DFB$ (hypotenuse :g:`DB <g1:[ D B ]>`, leg :g:`BF <g1:[ B F ]>`). Because the hypotenuse of a right triangle strictly exceeds either leg (:just:`I.19`) whenever :g:`D <g1:D>` $\neq$ :g:`O <g1:O>`, we read off immediately $OB > DB > BF$, i.e., $A > G > H$ ($\frac{25}{2} > 12 > \frac{288}{25}$), collapsing to equality $A = G = H$ when $a = b$.

.. step::

   Draw tangent :g:`BT <g1:[ B T ]>` perpendicular to radius :g:`OB <g1:[ O B ]>`, meeting diameter :g:`AC <g1:[ A C ]>` produced at :g:`T <g1:T>` $= \left(-\frac{225}{7}, 0\right)$. Parallelism of :g:`DF <g1:[ D F ]>` and :g:`BT <g1:[ B T ]>` transfers the ratio on :g:`OB <g1:[ O B ]>` onto the diameter line, yielding the four-point harmonic range $(A, C; D, T) = -1$ that recurs in projective form in :doc:`Book VII Prop. 131 <../book-7-domain-of-analysis/book-7-domain-of-analysis-en>`.

.. _sec-b3-en-golden-semicircle:

3. Golden-Section Specialization in $\mathbb{Q}(\phi)$
------------------------------------------------------

When the diameter segments stand in the square of the golden ratio, $a = 1$ and $b = \phi^2 = \phi + 1$ (where $\phi = \frac{1 + \sqrt{5}}{2}$), the total diameter has length $1 + \phi^2 = \phi + 2 = \sqrt{5}\,\phi$, and Pappus's semicircle exhibits algebraic closure over $\mathbb{Q}(\phi)$:

.. picture:: /_static/constructions/synagoge_three_means_golden.svg
   :alt: Synagoge Book III Semicircle Means over Q(phi) with a = 1 and b = phi^2

Here :g:`OB <g2:[ O B ]>` gives $A = \frac{\phi + 2}{2}$, the geometric mean :g:`DB <g2:[ D B ]>` equals the golden ratio itself $G = \sqrt{1 \cdot \phi^2} = \phi$, and the harmonic mean :g:`BF <g2:[ B F ]>` equals $H = \frac{2\phi^2}{\phi + 2} = \frac{2\phi}{\sqrt{5}}$, confirming $A \cdot H = \phi^2 = G^2$ and $(A, C; D, T) = -1$ at :g:`T <g2:T>` with zero floating-point approximation in :func:`geometor.pappus.construct_three_means`.
