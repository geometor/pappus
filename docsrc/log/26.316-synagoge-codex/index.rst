:date: 2026-11-12
:type: log
:summary: Added the 5-unit, 4-track Synagoge Multi-Track Book Codex (Books III, IV, V, VII & VIII) from Hultsch's 1876–1878 Greek edition alongside exact SymPy / geometor.model constructions, 24 interactive SVGs, 9 standalone demos, and full verification suite (v0.2.0).

*Synagoge* Multi-Track Book Codex & Books III–VIII Symbolic Constructions (``v0.2.0``)
======================================================================================

Expanded ``geometor/pappus`` (``v0.2.0``) into a unified Digital Scriptorium edition and exact
symbolic geometry package housing both **Pappus of Alexandria's** *Synagoge* (*Μαθηματικὴ
Συναγωγή*, c. 340 CE) and executable ``SymPy`` / ``geometor.model`` demonstrations:

- **Five-Unit Four-Track Book Codex** (``docsrc/synagoge/``, ``:layout: book``):

  - Inspected 300 DPI scans of **Friedrich Hultsch's** 3-volume critical Greek edition
    (*Weidmann*, 1876–1878) across Books III, IV, V, VII, and VIII, pairing diplomatic polytonic
    Greek (``-el``) with **100% original GEOMETOR English translations** (``-en``), algebraic
    summaries (``-summary``), and philological commentary (``-notes``) referencing **Federico
    Commandino** (1588) and **Sir Thomas Little Heath** (1921/1926).
  - Built structured JSON apparatus in ``resources/synagoge/`` (``sources_manifest.json``,
    ``citations.json``, ``persons.json``, ``glossary.json``, ``concordance.json``) and matching
    Sphinx apparatus pages, including bidirectional resolution of all 8 ``pappus:collectio*``
    keys in ``geometor/euclid``.
  - Added ``geometor.pappus.sphinx_ext`` registering the ``-el`` Greek companion track in
    ``photon_platform.publish.book`` and offline sibling ``objects.inv`` intersphinx mappings.

- **Exact Symbolic *Synagoge* Constructions** (``geometor.pappus.synagoge_demos``):

  - **Book III (Props. 28–30)**: ``construct_three_means`` exhibiting $A, G, H$ in one semicircle
    ($A \cdot H = G^2$) with exact orthogonal foot $F$ on $OB$ and external harmonic tangent
    conjugate $(A, C; D, T) = -1$ over $\mathbb{Q}$ and $\mathbb{Q}(\phi)$.
  - **Book IV (Prop. 1)**: ``construct_pappus_area_theorem`` and 10-variable universal polynomial
    identity ``verify_pappus_area_symbolic() == 0`` generalizing *Elements* I.47 to arbitrary
    parallelograms on any scalene triangle.
  - **Book IV (Props. 14–18)**: ``construct_pappus_arbelos_chain`` and
    ``verify_arbelos_chain_symbolic`` proving $y_n = n\,d_n = 2n\,r_n$ and focal ellipse locus
    incidence in 100% rational coordinates.
  - **Book V (Prop. 1) & Book VIII (Prop. 23)**: ``verify_honeycomb_isoperimetry`` and
    ``construct_honeycomb_isoperimetry`` proving $n \in \{3, 4, 6\}$ planar tiling uniqueness,
    $A_6 : A_4 : A_3 = 3\sqrt{3} : 4 : 3$, and the 7-hexagon circle circumradius $R = s_6\sqrt{7}$.

- **Interactive SVG Gallery, CLI & Demos**: Extended ``render.py`` with exact circular arc support
  (``_extra_arcs``), added ``pappus synagoge`` and ``pappus build --synagoge`` CLI commands
  generating 24 ``.euclid-graphic`` SVGs, added 4 new standalone scripts in ``demos/`` (9 total),
  and authored ``docsrc/theorems/synagoge-constructions/index.rst`` plus ``tests/test_synagoge.py``.
