GEOMETOR • pappus
=================

**Visit the Online Archive:** https://geometor.github.io/pappus/

.. image:: docsrc/_static/constructions/golden_pappus.svg
   :alt: GEOMETOR • pappus featured geometric construction
   :target: https://geometor.github.io/pappus/
   :align: center

**Pappus of Alexandria • Mathematical Collection • semantic digital archive**

Mission
-------

``geometor/pappus`` is part of the interconnected `GEOMETOR <https://geometor.com>`_ semantic digital archive. It unites a four-track bilingual Book Codex of Pappus of Alexandria's eight-book *Mathematical Collection* (*Μαθηματικὴ Συναγωγή*) with an extensive computational catalog of constructive projective theorems. Through addressable semantic units, calibrated theme-adaptive vector diagrams, primary-source folio provenance, and exact SymPy symbolic algebra, this repository bridges ancient Greek geometry and mechanics with the modern projective theorems of Steiner, Pascal, and Desargues across the GEOMETOR corpus.

Books in This Archive
---------------------

- `Mathematical Collection <https://geometor.github.io/pappus/synagoge/>`_ — Critical bilingual edition of Books III, IV, V, VII, and VIII surveying classical Greek geometry, three means in a semicircle, the Arbelos circle chain, honeycomb isoperimetry, and the Hellenistic Treasury of Analysis (c. 340 CE).
- `Theorems <https://geometor.github.io/pappus/theorems/>`_ — Constructive projective theorems including Pappus's Hexagon Theorem, Steiner's six-line configuration, cross-ratio invariants, harmonic conjugates, and Pascal's *Hexagrammum Mysticum*.

Projective Geometry & Classical Mechanics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Pappus's Hexagon Theorem & Steiner Configurations** (``geometor.pappus.hexagon``): Universal determinant proofs, homologous type triangles, and all six :math:`S_3` Pappus lines concurring at Steiner Star points.
- **Pascal's Mystic Hexagram (1640)** (``geometor.pappus.pascal``): Conic generalizations across circles and ellipses, complete 60-line web enumeration, 20 Steiner points, and 15 Plücker lines.
- **Synagoge Classical Demonstrations** (``geometor.pappus.synagoge_demos``): Semicircle arithmetic/geometric/harmonic means, generalized Pythagorean area theorem, and rational Arbelos circle chain.

Repository Contents
-------------------

- ``docsrc/`` — RST documentation source, 4-track *Synagoge* codex, interactive *Theorems* catalog, and Sphinx docs compiled by `PHOTON publish <https://github.com/photon-platform/publish>`_.
- ``resources/`` — Primary-source folios, Hultsch polytonic Greek texts, and apparatus registries.
- ``src/geometor/pappus/`` — Exact SymPy symbolic engines for projective incidence, cross-ratios, harmonic fourths, and classical *Synagoge* theorems.

Local Build & Verification
--------------------------

.. code-block:: bash

   publish build
   uv run --no-sync pytest

Part of the GEOMETOR Knowledge Archive
--------------------------------------

Explore all **74 Book Codices** and **11 Mathematical Catalogs** at https://geometor.com/books/.
