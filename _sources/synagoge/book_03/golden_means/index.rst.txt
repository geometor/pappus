:order: 6
:layout: book
:type: book
:title: Golden-Section Specialization in Q(phi)
:canonical_id: Syn. III.phi
:folio: 0233
:excerpt: Algebraic closure and geometric properties of Pappus's semicircle means when diameter segments stand in the ratio of the square of the golden ratio (a = 1, b = phi^2).
:tracks: English: index | Greek: el | Summary: summary | Notes: notes

.. _sec-b3-en-golden-semicircle:

Golden-Section Specialization in $\mathbb{Q}(\phi)$
===================================================

.. rubric:: Modern Geometric Synthesis · Algebraic Invariants in the Golden Field

.. folio:: 0233
   :page: 1221

When the diameter segments stand in the square of the golden ratio, $a = 1$ and $b = \phi^2 = \phi + 1$ (where $\phi = \frac{1 + \sqrt{5}}{2}$), the total diameter has length $1 + \phi^2 = \phi + 2 = \sqrt{5}\,\phi$, and Pappus's semicircle exhibits algebraic closure over $\mathbb{Q}(\phi)$:

.. picture:: /_static/constructions/synagoge_three_means_golden.svg
   :alt: Synagoge Book III Semicircle Means over Q(phi) with a = 1 and b = phi^2

Here :g:`OB <g2:[ O B ]>` gives the arithmetic mean:

.. math::

   A = \frac{1 + \phi^2}{2} = \frac{\phi + 2}{2},

the geometric mean :g:`DB <g2:[ D B ]>` equals the golden ratio itself:

.. math::

   G = \sqrt{1 \cdot \phi^2} = \phi,

and the harmonic mean :g:`BF <g2:[ B F ]>` equals:

.. math::

   H = \frac{2 \cdot 1 \cdot \phi^2}{1 + \phi^2} = \frac{2\phi^2}{\phi + 2} = \frac{2\phi}{\sqrt{5}},

confirming the fundamental identity:

.. math::

   A \cdot H = \left(\frac{\phi + 2}{2}\right)\left(\frac{2\phi^2}{\phi + 2}\right) = \phi^2 = G^2

and $(A, C; D, T) = -1$ at :g:`T <g2:T>` with zero floating-point approximation in :func:`geometor.pappus.construct_three_means`.
