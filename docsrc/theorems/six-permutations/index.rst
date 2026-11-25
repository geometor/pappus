:type: theorem
:order: 3
:summary: Action of the symmetric group S₃ on (B₀, B₁, B₂), the six distinct Pappus lines, and Jakob Steiner's parity concurrency at the two Star Points S₊ and S₋.

The Six Permutations (:math:`S_3`) & The Two Star Points
========================================================

Symmetric Group Action on Six Collinear Vertices
------------------------------------------------

A single instance of Pappus's Hexagon Theorem fixes an ordering of the two collinear triples
:math:`(A_0, A_1, A_2)` on carrier :math:`a` and :math:`(B_0, B_1, B_2)` on carrier :math:`b`. Yet the nine cross-lines
:math:`\{[A_i B_j] : 0 \le i, j \le 2\}` exist independently of how the indices on :math:`b` are labeled!

Hold :math:`(A_0, A_1, A_2)` fixed and let the symmetric group :math:`S_3` of order :math:`3! = 6` permute
the labels on :math:`b` via :math:`\sigma = (\sigma_0, \sigma_1, \sigma_2) \in S_3`. Each permutation
inscribes a distinct hexagon

.. math::

   H_\sigma = \langle A_0,\, B_{\sigma_1},\, A_2,\, B_{\sigma_0},\, A_1,\, B_{\sigma_2} \rangle,

whose three opposite cross-join intersections

.. math::

   M_{01}^{(\sigma)} = [A_0 B_{\sigma_1}] \cap [A_1 B_{\sigma_0}], \quad
   M_{12}^{(\sigma)} = [A_1 B_{\sigma_2}] \cap [A_2 B_{\sigma_1}], \quad
   M_{20}^{(\sigma)} = [A_2 B_{\sigma_0}] \cap [A_0 B_{\sigma_2}]

determine a distinct **Pappus line** :math:`p_\sigma`. Across all six elements of :math:`S_3`, the nine
cross-lines meet in **18 cross-join intersections** arranged three-by-three along **six Pappus
lines**—splitting cleanly by permutation parity into the alternating subgroup
:math:`A_3 = \{(0,1,2),\, (1,2,0),\, (2,0,1)\}` (**even**, 3-cycles) and its odd coset
:math:`S_3 \setminus A_3 = \{(0,2,1),\, (1,0,2),\, (2,1,0)\}` (**odd**, transpositions).

.. list-table:: Exact Six :math:`S_3` Pappus Lines on ``preset="steiner"`` (:math:`A = [(1,0),(2,0),(3,0)]`, :math:`B = [(0,2),(3,1),(5,\tfrac{1}{3})]`)
   :header-rows: 1
   :widths: 15 10 47 28

   * - :math:`\sigma \in S_3`
     - Parity
     - Three Collinear Cross-Join Meets
     - Exact Line Equation
   * - :math:`(0, 1, 2)`
     - **even**
     - :math:`\left(\frac{5}{3}, \frac{1}{3}\right),\; \left(3, \frac{1}{9}\right),\; \left(\frac{25}{9}, \frac{4}{27}\right)`
     - :math:`3x + 18y = 11`
   * - :math:`(1, 2, 0)`
     - **even**
     - :math:`\left(\frac{23}{11}, \frac{1}{11}\right),\; \left(\frac{15}{7}, -\frac{1}{7}\right),\; (3, -4)`
     - :math:`9x + 2y = 19`
   * - :math:`(2, 0, 1)`
     - **even**
     - :math:`\left(\frac{20}{19}, -\frac{2}{19}\right),\; \left(\frac{12}{5}, \frac{2}{5}\right),\; \left(0, -\frac{1}{2}\right)`
     - :math:`3x - 8y = 4`
   * - :math:`(0, 2, 1)`
     - **odd**
     - :math:`\left(\frac{25}{13}, \frac{1}{13}\right),\; \left(\frac{9}{5}, -\frac{1}{5}\right),\; \left(\frac{15}{7}, \frac{4}{7}\right)`
     - :math:`9x - 4y = 17`
   * - :math:`(1, 0, 2)`
     - **odd**
     - :math:`\left(\frac{4}{3}, -\frac{2}{3}\right),\; \left(\frac{20}{7}, \frac{2}{21}\right),\; \left(3, \frac{1}{6}\right)`
     - :math:`3x - 6y = 8`
   * - :math:`(2, 1, 0)`
     - **odd**
     - :math:`\left(\frac{5}{7}, -\frac{1}{7}\right),\; (3, -1),\; \left(\frac{15}{13}, -\frac{4}{13}\right)`
     - :math:`3x + 8y = 1`

Jakob Steiner's Theorem (1828): The Two Star Points
---------------------------------------------------

In 1828, **Jakob Steiner** discovered a remarkable higher-order concurrency hidden inside the
six Pappus lines: they do not meet in 15 generic points, nor do all six concur at a single point.
Instead, **concurrency respects permutation parity**:

- The **three even Pappus lines** (:math:`\sigma \in A_3`, amber) concur at a single point, the **even
  Steiner Star point** :math:`S_+`.
- The **three odd Pappus lines** (:math:`\sigma \in S_3 \setminus A_3`, magenta) concur at a second
  point, the **odd Steiner Star point** :math:`S_-`.

.. picture:: /_static/constructions/pappus_steiner.svg
   :alt: The Six Pappus Lines and Two Steiner Star Points S+ and S-

.. step::

   Trace the three **even** (:math:`A_3`) Pappus lines: :g:`p_{012} <g7:[ M0110 M1221 ]>`,
   :g:`p_{120} <g7:[ M0211 M1022 ]>`, and :g:`p_{201} <g7:[ M0012 M1120 ]>`.

.. step::

   Verify their exact concurrency at the even Star point :g:`S_+ <g7:S1>`
   :math:`= \left(\frac{80}{39},\, \frac{7}{26}\right)`:
   :math:`3\left(\frac{80}{39}\right) + 18\left(\frac{7}{26}\right) = \frac{80 + 63}{13} = 11`,
   :math:`9\left(\frac{80}{39}\right) + 2\left(\frac{7}{26}\right) = \frac{240 + 7}{13} = 19`, and
   :math:`3\left(\frac{80}{39}\right) - 8\left(\frac{7}{26}\right) = \frac{80 - 28}{13} = 4`.

.. step::

   Trace the three **odd** (:math:`S_3 \setminus A_3`) Pappus lines:
   :g:`p_{021} <g7:[ M0210 M1122 ]>`, :g:`p_{102} <g7:[ M0011 M1220 ]>`, and
   :g:`p_{210} <g7:[ M0112 M1021 ]>`.

.. step::

   Verify their exact concurrency at the odd Star point :g:`S_- <g7:S2>`
   :math:`= \left(\frac{5}{3},\, -\frac{1}{2}\right)`, and join the two Star points along the dashed
   violet **Steiner line** :g:`S_+S_- <g7:[ S1 S2 ]>` (:math:`12x - 6y = 23`).

Individual :math:`S_3` Permutation Gallery
------------------------------------------

Inspecting each permutation :math:`\sigma \in S_3` individually reveals how cycling :math:`(B_0, B_1, B_2)`
sweeps the three even Pappus lines around :math:`S_+` while transposing any pair switches parity into
the odd pencil around :math:`S_-`:

Even Permutations (:math:`\sigma \in A_3`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Identity** :math:`\sigma = (0, 1, 2)` — :g:`M_{01} <g1:M01>`, :g:`M_{20} <g1:M20>`, :g:`M_{12} <g1:M12>` on :g:`p_{012} <g1:[ M01 M12 ]>`:

.. picture:: /_static/constructions/pappus_perm_0.svg
   :alt: Even Permutation (0, 1, 2)

**3-Cycle** :math:`\sigma = (1, 2, 0)` — :g:`M_{01} <g4:M01>`, :g:`M_{20} <g4:M20>`, :g:`M_{12} <g4:M12>` on :g:`p_{120} <g4:[ M01 M12 ]>`:

.. picture:: /_static/constructions/pappus_perm_3.svg
   :alt: Even Permutation (1, 2, 0)

**3-Cycle** :math:`\sigma = (2, 0, 1)` — :g:`M_{01} <g5:M01>`, :g:`M_{20} <g5:M20>`, :g:`M_{12} <g5:M12>` on :g:`p_{201} <g5:[ M01 M12 ]>`:

.. picture:: /_static/constructions/pappus_perm_4.svg
   :alt: Even Permutation (2, 0, 1)

Odd Permutations (:math:`\sigma \in S_3 \setminus A_3`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Transposition** :math:`\sigma = (0, 2, 1)` — :g:`M_{01} <g2:M01>`, :g:`M_{20} <g2:M20>`, :g:`M_{12} <g2:M12>` on :g:`p_{021} <g2:[ M01 M12 ]>`:

.. picture:: /_static/constructions/pappus_perm_1.svg
   :alt: Odd Permutation (0, 2, 1)

**Transposition** :math:`\sigma = (1, 0, 2)` — :g:`M_{01} <g3:M01>`, :g:`M_{20} <g3:M20>`, :g:`M_{12} <g3:M12>` on :g:`p_{102} <g3:[ M01 M12 ]>`:

.. picture:: /_static/constructions/pappus_perm_2.svg
   :alt: Odd Permutation (1, 0, 2)

**Transposition** :math:`\sigma = (2, 1, 0)` — :g:`M_{01} <g6:M01>`, :g:`M_{20} <g6:M20>`, :g:`M_{12} <g6:M12>` on :g:`p_{210} <g6:[ M01 M12 ]>`:

.. picture:: /_static/constructions/pappus_perm_5.svg
   :alt: Odd Permutation (2, 1, 0)

GEOMETOR's 2023 Parallel Configuration Discovery
------------------------------------------------

In GEOMETOR's original 2023 ``pappus.py`` exploration (:math:`A = [(0,0), (1,0), (3,0)]` on :math:`y = 0`
and :math:`B = [(0,1), (3/2, 1), (5/2, 1)]` on :math:`y = 1`), constructing all nine cross-lines uncovered
both a subtle projective phenomenon and exact rational Star coordinates:

- Because :math:`[A_0 B_1]` and :math:`[A_1 B_2]` share exact slope :math:`\frac{2}{3}`, one of the 18 cross-join
  pairs meets at an **ideal point on the line at infinity**, leaving **17 finite cross-join
  meets** in :math:`\mathbb{Q}^2`. On the odd transposition :math:`\sigma = (2, 1, 0)`, that parallel
  cross-join pair :math:`[A_0 B_1] \parallel [A_1 B_2]` directs its Pappus line along exact slope
  :math:`\frac{2}{3}` toward the ideal meet!
- All three **even** Pappus lines meet inside the central strip at the exact rational Star point

  .. math::

     S_+ = \left(\frac{90}{73},\; \frac{38}{73}\right),

  while the three **odd** Pappus lines concur far in the first quadrant at
  :math:`S_- = \left(10,\; \frac{38}{3}\right)`.

.. picture:: /_static/constructions/pappus_parallel_steiner.svg
   :alt: 2023 GEOMETOR Parallel Configuration — Even Star Point S+ = (90/73, 38/73)

.. step::

   Observe the three **even** Pappus lines :g:`p_{012} <g8:[ M0110 M1221 ]>`,
   :g:`p_{120} <g8:[ M0211 M1022 ]>`, and :g:`p_{201} <g8:[ M0012 M1120 ]>` converging inside
   the parallel carrier band at :g:`S_+ <g8:S1>` :math:`= \left(\frac{90}{73}, \frac{38}{73}\right)`.
