:order: 2
:layout: book
:type: book
:title: The Three Classical Means & Their Unified Semicircle Construction
:canonical_id: Syn. III.28-30
:excerpt: Pappus's elegant construction exhibiting the arithmetic mean A, geometric mean G, and harmonic mean H simultaneously within a single semicircle, proving visually that A * H = G^2 and A >= G >= H.
:tracks: English: index | Greek: el | Summary: summary | Notes: notes

.. _sec-b3-en-semicircle-means:

The Three Classical Means & Their Unified Semicircle Construction
=================================================================

.. rubric:: *Synagoge* Book III, Chs. 28–43 (*Props. 28–30*, :cite:`Hultsch I, pp. 68–84 <hultsch:1876>`) · Original English Translation from Hultsch's Greek

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

   Draw tangent :g:`BT <g1:[ B T ]>` perpendicular to radius :g:`OB <g1:[ O B ]>`, meeting diameter :g:`AC <g1:[ A C ]>` produced at :g:`T <g1:T>` $= \left(-\frac{225}{7}, 0\right)$. Parallelism of :g:`DF <g1:[ D F ]>` and :g:`BT <g1:[ B T ]>` transfers the ratio on :g:`OB <g1:[ O B ]>` onto the diameter line, yielding the four-point harmonic range $(A, C; D, T) = -1$ that recurs in projective form in :doc:`Book VII Prop. 131 <../../book_07/prop_131_harmonic/index>`.
