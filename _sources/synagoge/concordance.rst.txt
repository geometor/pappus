:navigation: header
:order: 14
:nav_title: Concordance
:type: apparatus
:title: Concordance — Hultsch Citation & Symbolic Concordance

.. _codex-concordance:
.. _concordance:

Concordance
===========

Bidirectional concordance mapping :person:`Friedrich Hultsch's <hultsch>` pagination across **Books II–VIII** of :person:`Pappus's <pappus>` *Synagoge* (:cite:`Vols. I–III, 1876–1878 <hultsch:1876>`) to:

1. All **eight ``pappus:collectio*`` citation keys** in ``geometor/euclid`` (:cite:`Heath 1926 <heath:1926>`),
2. Classical Euclidean proposition dependencies (:just:`I.34`–:just:`XIII.18` in ``geometor/elements``), and
3. Exact symbolic ``geometor.pappus`` SymPy models, CLI ``demos/``, and interactive ``.euclid-graphic`` SVGs.

``geometor/euclid`` Bidirectional Citation Concordance
------------------------------------------------------

.. list-table:: All 8 ``geometor/euclid`` ``pappus:collectio*`` Keys Mapped to ``geometor/pappus``
   :header-rows: 1
   :widths: 26 24 26 24

   * - ``euclid`` Citation Key
     - Hultsch Locus
     - Heath *Euclid* Locus
     - *Synagoge* Codex Unit
   * - ``pappus:collectio``
     - Vols. I–III passim
     - Vol. I, p. 26 (Ch. III, folio 0040)
     - :ref:`Synagoge Overview <synagoge-codex>`
   * - ``pappus:collectio:iii-p-72-9-23``
     - Book III, p. 72, ll. 9–23
     - Vol. II, p. 211 (VI.13 note, folio 0217)
     - :ref:`Book III: Three Means <sec-b3-en-semicircle-means>`
   * - ``pappus:collectio:iii-p-132``
     - Book III, p. 132 ff.
     - Vol. II, p. 81 (Book IV note, folio 0087)
     - :ref:`Book III: Notes & Solids <synagoge-b3-notes>`
   * - ``pappus:collectio:7``
     - Book VII, pp. 634–638
     - Vol. III, pp. 521, 526–527, 539
     - :ref:`Book VII: Treasury of Analysis <sec-b7-en-analysis-synthesis>`
   * - ``pappus:collectio:vii-p-670-19``
     - Book VII, p. 670, l. 19
     - Vol. II, p. 4 (Book III defs., folio 0010)
     - :ref:`Book VII: 33-Book Curriculum <sec-b7-en-analysis-synthesis>`
   * - ``pappus:collectio:vii-p-678``
     - Book VII, pp. 678–680
     - Vol. II, p. 113 (Book V compound ratio)
     - :ref:`Book VII: n-Line Locus & Guldin <sec-b7-en-locus-guldin>`
   * - ``pappus:collectio:vii-p-826``
     - Book VII, p. 826
     - Vol. II, p. 27 (Book III props., folio 0033)
     - :ref:`Book VII: Cross-Ratio & Harmonics <sec-b7-en-cross-ratio>`
   * - ``pappus:collectio:vii-p-928``
     - Book VII, p. 928
     - Vol. II, p. 250 (Book VI props., folio 0256)
     - :ref:`Book VII: Conics & Reception <synagoge-b7-notes>`

Master Locus, Proof & Symbolic Code Concordance (Books III–VIII)
----------------------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 22 24 18 36

   * - Hultsch Locus
     - Codex Section
     - Euclid / Elements
     - Exact Symbolic Code & SVGs
   * - **III.1–27** (*I, pp. 30–68*)
     - :ref:`Pandrosion & Plane/Solid/Linear <sec-b3-en-pandrosion-hierarchy>`
     - :just:`VI.13`, :just:`XI.33`
     - —
   * - **III.28–43** (*I, pp. 68–84*)
     - :ref:`Three Means in One Semicircle <sec-b3-en-semicircle-means>`
     - :just:`III.31`, :just:`VI.8`, :just:`VI.13`
     - ``construct_three_means()`` · ``demos/synagoge_three_means.py`` · ``synagoge_three_means.svg`` · ``synagoge_three_means_golden.svg``
   * - **III.54–58** (*I, pp. 132–162*)
     - :ref:`Five Platonic Solids in Sphere <synagoge-b3-notes>`
     - :just:`XIII.13`–:just:`XIII.18`
     - —
   * - **IV.1** (*I, pp. 176–179*)
     - :ref:`Pappus's Generalized Area Theorem <sec-b4-en-area-theorem>`
     - :just:`I.34`, :just:`I.35`, :just:`I.47`, :just:`VI.31`
     - ``construct_pappus_area_theorem()`` · ``verify_pappus_area_symbolic()`` · ``demos/pappus_area_theorem.py`` · ``pappus_area_theorem.svg`` · ``pappus_area_pythagoras.svg``
   * - **IV.14–18** (*I, pp. 208–232*)
     - :ref:`Infinite Arbelos Circle Chain <sec-b4-en-arbelos-chain>`
     - :just:`III.11`, :just:`III.12`, :just:`III.36`
     - ``construct_pappus_arbelos_chain()`` · ``verify_arbelos_chain_symbolic()`` · ``demos/arbelos_circle_chain.py`` · ``pappus_arbelos_chain.svg``
   * - **V.pr & 1–10** (*I, pp. 304–336*)
     - :ref:`Bees Preface & Isoperimetry <sec-b5-en-bees-preface>`
     - :just:`I.32`, :just:`IV.15`
     - ``verify_honeycomb_isoperimetry()`` · ``construct_honeycomb_isoperimetry()`` · ``demos/honeycomb_isoperimetry.py`` · ``honeycomb_isoperimetry.svg``
   * - **V.19** (*I, pp. 352–358*)
     - :ref:`Thirteen Archimedean Solids <synagoge-b5-notes>`
     - :just:`XIII.18`
     - —
   * - **VII.pr & Chs. 1–3** (*II, pp. 634–638*)
     - :ref:`Treasury of Analysis & 33 Books <sec-b7-en-analysis-synthesis>`
     - :just:`III.def.1`
     - —
   * - **VII Chs. 36–42** (*II, pp. 676–683*)
     - :ref:`n-Line Locus & Centroid Theorem <sec-b7-en-locus-guldin>`
     - :just:`VI.23`
     - —
   * - **VII.129, 131** (*II, pp. 870–877*)
     - :ref:`Cross-Ratio & Harmonic Division <sec-b7-en-cross-ratio>`
     - :just:`VI.2`, :just:`VI.3`
     - ``cross_ratio()`` · ``project_point()`` · ``construct_harmonic_fourth()`` · ``demos/harmonic_conjugate.py`` · ``harmonic_fourth.svg`` · ``pappus_harmonics.svg``
   * - **VII.138–139** (*II, pp. 884–889*)
     - :ref:`Parallel & General Hexagon Theorems <sec-b7-en-hexagon-theorems>`
     - :just:`VI.4`
     - ``construct_pappus_hexagon()`` · ``construct_pappus_configuration()`` · ``verify_pappus_symbolic()`` · ``construct_pascal_hexagon()`` · ``demos/pappus_hexagon.py`` · ``pappus_parallel.svg`` · ``pappus_hexagon.svg`` · ``pappus_steiner.svg`` · ``pascal_hexagrammum.svg``
   * - **VII.238** (*II, pp. 1008–1013*)
     - :ref:`Focus–Directrix of Conics <synagoge-b7-notes>`
     - :just:`I.47`, :just:`VI.4`
     - ``pascal_ellipse.svg``
   * - **VIII.pr & 1–12** (*III, pp. 1022–1073*)
     - :ref:`Mechanics, Lever & Baroulkos <sec-b8-en-inclined-baroulkos>`
     - :just:`VI.1`, :just:`XI.def.3`
     - —
   * - **VIII.13–26** (*III, pp. 1074–1115*)
     - :ref:`Rusty Compass & 7 Hexagons in Circle <sec-b8-en-rusty-seven-hexagons>`
     - :just:`II.12`, :just:`IV.15`
     - ``construct_honeycomb_isoperimetry()`` · ``demos/honeycomb_isoperimetry.py`` · ``honeycomb_isoperimetry.svg``
