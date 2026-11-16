:order: 1
:layout: book
:type: book
:title: Proposition 1: Pappus's Parallelogram Generalization of the Pythagorean Theorem
:canonical_id: Syn. IV.1
:excerpt: Universal affine area theorem erecting arbitrary parallelograms on two sides of an arbitrary triangle, proving their areas sum to the base parallelogram determined by the outer intersection apex.
:tracks: English: index | Greek: el | Summary: summary | Notes: notes

.. _sec-b4-en-area-theorem:

Proposition 1: Pappus's Parallelogram Generalization of the Pythagorean Theorem
===============================================================================

.. rubric:: *Synagoge* Book IV, Ch. 1 / Prop. 1 (:cite:`Hultsch I, pp. 176–179 <hultsch:1876>`) · Original English Translation from Hultsch's Greek

Book IV opens directly (its preface having been lost in the archetype manuscript) with a striking affine generalization of :cite:`Euclid's Elements I.47 <euclid:elements>` and :just:`VI.31`: **neither a right angle in the base triangle nor similarity between the erected figures is required**. Arbitrary parallelograms erected outward upon any two sides of any triangle sum in area to a third parallelogram erected on the remaining side, whose lateral edge is given in both magnitude and direction by the segment joining the outer intersection apex to the vertex of the triangle.

.. picture:: /_static/constructions/pappus_area_theorem.svg
   :alt: Synagoge Book IV Proposition 1 — Pappus's Parallelogram Area Theorem on a Scalene Triangle

.. enunciation::

   If :g:`ABC <g1:< A B C >>` be any triangle, and upon its sides $AB, AC$ there be described any parallelograms whatever, :g:`ABDE <g1:< A B D E >>` and :g:`ACFG <g1:< A C F G >>`, and the outer sides :g:`DE <g1:[ D E ]>` and :g:`FG <g1:[ F G ]>` be produced to meet at :g:`H <g1:H>`, and :g:`HA <g1:[ H A ]>` be joined, then the parallelograms :g:`ABDE <g1:< A B D E >>` and :g:`ACFG <g1:< A C F G >>` together are equal in area to the parallelogram :g:`BCML <g1:< B C M L >>` contained by base $BC$ and lateral edges :g:`BL <g1:[ B L ]>`, :g:`CM <g1:[ C M ]>` equal and parallel to :g:`HA <g1:[ H A ]>`. *"And this theorem is far more universal than that proved in the Elements concerning squares on right-angled triangles."*

.. step::

   Set out scalene :g:`triangle ABC <g1:< A B C >>` with :g:`A <g1:A>` $= (3, 4)$, :g:`B <g1:B>` $= (0, 0)$, and :g:`C <g1:C>` $= (7, 0)$, and erect arbitrary outward parallelograms :g:`ABDE <g1:< A B D E >>` (area $13$) and :g:`ACFG <g1:< A C F G >>` (area $15$).

.. step::

   Produce the outer sides :g:`DE <g1:[ D E ]>` (parallel to $AB$) and :g:`FG <g1:[ F G ]>` (parallel to $AC$) until they intersect at apex :g:`H <g1:H>`, and draw the transversal line :g:`HA <g1:[ H A ]>` across the vertex :g:`A <g1:A>` to meet base $BC$ at :g:`J <g1:J>`.

.. step::

   Through :g:`B <g1:B>` and :g:`C <g1:C>` draw :g:`BL <g1:[ B L ]>` and :g:`CM <g1:[ C M ]>` equal and parallel to segment $HA$ ($L - B = M - C = A - H$), and join $LM$ with :g:`JN <g1:[ J N ]>` parallel to $HA$. Because $BL$ and $CM$ are both equal and parallel to $HA$, they are equal and parallel to one another (:just:`I.30`), so :g:`BCML <g1:< B C M L >>` is a parallelogram (:just:`I.33`) partitioned by :g:`JN <g1:[ J N ]>` into sub-parallelograms $BJNL$ and $JCMN$.

.. step::

   Apply :just:`I.35` (shear-invariance of parallelograms on the same base and between the same parallels) twice on the left: parallelogram :g:`ABDE <g1:< A B D E >>` equals the intermediate parallelogram $AB\text{-}HA$ on base $AB$ between parallels $AB$ and :g:`DE <g1:[ D E ]>`, which in turn equals $BJNL$ on parallel base $HA = BL$ between parallels :g:`BL <g1:[ B L ]>` and :g:`HA <g1:[ H A ]>`.

.. step::

   By the identical double shear on the right, parallelogram :g:`ACFG <g1:< A C F G >>` equals $JCMN$ between parallels :g:`HA <g1:[ H A ]>` and :g:`CM <g1:[ C M ]>`. Adding the two parts gives

   .. math::

      \operatorname{Area}(ABDE) + \operatorname{Area}(ACFG) = \operatorname{Area}(BJNL) + \operatorname{Area}(JCMN) = \operatorname{Area}(BCML) = 13 + 15 = 28.

Specialization to *Elements* I.47 (*Right Triangle & Squares*)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When $\angle BAC = 90^\circ$ in a $3$-$4$-$5$ right triangle and :g:`ABDE <g2:< A B D E >>` (area $9$) and :g:`ACFG <g2:< A C F G >>` (area $16$) are squares, the corner triangle formed at :g:`H <g2:H>` is congruent to :g:`ABC <g2:< A B C >>` rotated by $90^\circ$, making :g:`HA <g2:[ H A ]>` perpendicular to hypotenuse $BC$ with exact length $|HA| = |BC| = 5$. Thus :g:`BCML <g2:< B C M L >>` becomes the $5 \times 5$ hypotenuse square of area $25$ partitioned along altitude :g:`JN <g2:[ J N ]>` into Euclid's windmill rectangles of areas $\frac{9}{5} \cdot 5 = 9$ and $\frac{16}{5} \cdot 5 = 16$:

.. picture:: /_static/constructions/pappus_area_pythagoras.svg
   :alt: Synagoge Book IV Proposition 1 Specialized to Euclid Elements I.47 (9 + 16 = 25)
