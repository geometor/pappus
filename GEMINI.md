# GEOMETOR • `pappus`

Multi-Track Book Codex of **Pappus of Alexandria's** *Synagoge* (*Μαθηματικὴ Συναγωγή* / *Mathematical Collection*, c. 340 CE, Books III, IV, V, VII & VIII) united with exact symbolic projective and classical geometry constructions built on [SymPy](https://www.sympy.org/), `geometor.model`, and `geometor.divine`.

---

## 1. Purpose & Dual Architecture

`geometor-pappus` (`v0.2.0`) unites Digital Scriptorium philology with 100% exact symbolic algebra (zero floating-point approximations):

### A. Multi-Track *Synagoge* Book Codex (`docsrc/synagoge/`, `:layout: book`)
- **Primary Public-Domain Sources**: Friedrich Hultsch's 3-volume critical polytonic Greek edition (*Pappi Alexandrini Collectionis quae supersunt*, Berlin: Weidmann, 1876–1878, verified via 300 DPI page scan vision), Federico Commandino's Latin *editio princeps* (1588), Sir Thomas Little Heath's public-domain mathematical commentary (1921/1926), and **100% original GEOMETOR English translations** authored directly from Hultsch's Greek.
- **Five Synchronized Four-Track Units (`-en`, `-el`, `-summary`, `-notes`)**:
  1. `book-3-three-means` — Address to Pandrosion, plane/solid/linear problem hierarchy, Delian cube-duplication methods, and **Arithmetic, Geometric, and Harmonic Means in One Semicircle** ($A \cdot H = G^2$).
  2. `book-4-area-and-arbelos` — **Pappus's Parallelogram Area Generalization** of *Elements* I.47 ($|\mathcal{P}_3| = |\mathcal{P}_1| + |\mathcal{P}_2|$) and the **Ancient Theorem on the *Arbelos* Circle Chain** ($y_n = n\,d_n$).
  3. `book-5-sagacity-of-bees` — **Preface on the Sagacity of Bees**, unique regular planar tessellations ($n \in \{3, 4, 6\}$), **Honeycomb Isoperimetry** ($A_6 : A_4 : A_3 = 3\sqrt{3} : 4 : 3$), and the 13 Archimedean solids.
  4. `book-7-domain-of-analysis` — **The Treasury of Analysis** (*Τόπος ἀναλυόμενος*), analysis vs. synthesis, 33-book canon, $n$-line locus, **Pappus–Guldinus Centroid Rule**, **Cross-Ratio Invariance** (VII.129), **Harmonic Division** (VII.131), and **Pappus's Hexagon Theorems** (VII.138–139).
  5. `book-8-mechanics` — **Architectonic Mechanics**, centers of gravity, inclined plane (VIII.9), Archimedes's lever saying & Hero's *Baroulkos* gear-train, fixed-compass ("rusty compass") constructions, and **Seven Regular Hexagons Inscribed in a Circle** ($R = s_6\sqrt{7}$, VIII.23).
- **Critical Apparatus (`docsrc/synagoge/` & `resources/synagoge/`)**: Bidirectional `concordance` (mapping all 8 `pappus:collectio*` keys in `geometor/euclid` plus `elements`, `proclus`, `hilbert`, and `geometor.pappus` code), `bibliography`, `persons` (*Index Nominum*), and polytonic Greek/Latin `glossary`. Zero `.. py_file::` blocks are embedded in `docsrc/synagoge/` per GEOMETOR's strict content/code separation mandate.

### B. Exact Symbolic Engine & Theorem Canon (`src/geometor/pappus/` & `demos/`)
1. **Classical *Synagoge* Constructions (`synagoge_demos.py`)**:
   - `construct_three_means`: Semicircle construction of $(A, G, H)$ over $\mathbb{Q}$ and $\mathbb{Q}(\phi)$ with exact orthogonal foot $F$ on $OB$ ($|BF| = H$) and external harmonic conjugate $T$ satisfying $(A, C; D, T) = -1$.
   - `construct_pappus_area_theorem` & `verify_pappus_area_symbolic`: Oblique scalene and Pythagorean ($3$-$4$-$5$) area constructions plus universal 10-variable polynomial identity over $\mathbb{Z}$.
   - `construct_pappus_arbelos_chain` & `verify_arbelos_chain_symbolic`: Infinite tangent circle chain inside the *arbelos* in 100% exact rational coordinates proving $y_n = n\,d_n = 2n\,r_n$, pairwise tangency quadrances, and carrier ellipse locus incidence.
   - `verify_honeycomb_isoperimetry` & `construct_honeycomb_isoperimetry`: Diophantine proof of $n \in \{3, 4, 6\}$, exact $\mathbb{Q}(\sqrt{3})$ area comparisons at equal perimeter, and Book VIII.23's 7-hexagon circle inscription ($R = s_6\sqrt{7}$).
2. **Pappus's Hexagon Theorem & $S_3$ Steiner Configuration (`constructions.py`)**:
   - Straightedge collinearity of opposite cross-join meets $M_{01}, M_{12}, M_{20}$ (*Synagoge* VII.138 & VII.139), homologous `square`/`circle`/`diamond` triangles, universal 8-variable proof (`verify_pappus_symbolic() == 0`), and all $6$ $S_3$ Pappus lines concurring by parity at Steiner Star points $(S_+, S_-)$.
3. **Cross-Ratios, Harmonics & Golden Projectivity (`projective.py`)**:
   - Central perspectivity (`project_point`, VII.129), complete-quadrilateral fourth harmonic (`construct_harmonic_fourth`), emergent harmonic tetrad scanner (`find_harmonic_ranges`), and $\mathbb{Q}(\phi)$ golden sections via `geometor.divine`.
4. **Pascal's *Hexagrammum Mysticum* (`pascal.py`)**:
   - Smooth-conic generalization across circles and ellipses, Veronese $6 \times 6$ coconicity (`are_coconic`), Chasles conic cross-ratio (`conic_cross_ratio`), universal 6-variable proof (`verify_pascal_symbolic() == 0`), and complete projective enumeration of **15 chords, 45 diagonal points, 60 Pascal lines, 20 Steiner points, 60 Kirkman points, and 15 Plücker lines**.

---

## 2. Package Architecture (`src/geometor/pappus/`)

- [`__init__.py`](src/geometor/pappus/__init__.py): Public namespace exports and `__version__ = "0.2.0"`.
- [`projective.py`](src/geometor/pappus/projective.py): Exact projective & conic invariants (`PHI`, `quadrance`, `line_spread`, `exact_line_meet`, `project_point`, `cross_ratio`, `anharmonic_orbit`, `is_harmonic_range`, `harmonic_conjugate_point`, `find_harmonic_ranges`, `find_golden_sections`, `enable_divine_analysis`, `circle_stereographic_point`, `conic_equation_through_points`, `are_coconic`, `conic_cross_ratio`).
- [`constructions.py`](src/geometor/pappus/constructions.py): Canonical `PRESETS` (`"hexagon"`, `"parallel"`, `"steiner"`, `"harmonic"`, `"golden"`), `construct_pappus_hexagon`, `construct_pappus_configuration`, `construct_harmonic_fourth`, and `verify_pappus_symbolic`.
- [`pascal.py`](src/geometor/pappus/pascal.py): Smooth-conic `PASCAL_PRESETS` (`"hexagrammum"`, `"convex"`, `"ellipse"`, `"golden_conic"`), `construct_pascal_hexagon`, `construct_pascal_steiner_family`, `enumerate_hexagrammum_mysticum`, and `verify_pascal_symbolic`.
- [`synagoge_demos.py`](src/geometor/pappus/synagoge_demos.py): Classical *Synagoge* Books III, IV, V & VIII symbolic models, polynomial verifiers, and `build_synagoge_gallery` (`export_synagoge_svgs`).
- [`render.py`](src/geometor/pappus/render.py): Pixel-space interactive SVG serializer (`render_svg_string`, `export_svg`) supporting lines, circles, semicircular/circular arcs (`model._extra_arcs`), general ellipses (`model._extra_conics`), polygons, segments, and golden/harmonic sections for `photon_platform.publish` (`svg.euclid-graphic`, `geometor_interactive.js`).
- [`sphinx_ext.py`](src/geometor/pappus/sphinx_ext.py): Sphinx extension registering the `-el` (`Greek (Hultsch 1876)`) companion track in `photon_platform.publish.book` and offline sibling `objects.inv` intersphinx resolution.
- [`__main__.py`](src/geometor/pappus/__main__.py): `pappus` CLI (`build`, `inspect`, `harmonics`, `pascal`, `synagoge`).

---

## 3. Development & Verification Commands

All commands run on Python 3.13 via the GEOMETOR `uv` workspace environment (avoid bare `uv run` inside `pappus/` so no local `.venv` shadows workspace editable packages):

```bash
# Lint (enforces E, F, I, ANN, and Google-convention D rules)
/home/phi/.local/bin/ruff check src tests demos

# Run full test suite (test_pappus.py + test_synagoge.py)
/home/phi/PROJECTS/geometor/.venv/bin/python -m pytest -v

# Run standalone demonstrations (9 scripts across projective & Synagoge canon)
/home/phi/PROJECTS/geometor/.venv/bin/python demos/pappus_hexagon.py
/home/phi/PROJECTS/geometor/.venv/bin/python demos/pappus_six_permutations.py
/home/phi/PROJECTS/geometor/.venv/bin/python demos/harmonic_conjugate.py
/home/phi/PROJECTS/geometor/.venv/bin/python demos/golden_pappus.py
/home/phi/PROJECTS/geometor/.venv/bin/python demos/pascal_hexagrammum.py
/home/phi/PROJECTS/geometor/.venv/bin/python demos/synagoge_three_means.py
/home/phi/PROJECTS/geometor/.venv/bin/python demos/pappus_area_theorem.py
/home/phi/PROJECTS/geometor/.venv/bin/python demos/arbelos_circle_chain.py
/home/phi/PROJECTS/geometor/.venv/bin/python demos/honeycomb_isoperimetry.py

# Regenerate all 24 interactive SVG diagrams & build Sphinx Book Codex into docs/
/home/phi/PROJECTS/geometor/.venv/bin/python -m geometor.pappus build --synagoge
/home/phi/.local/bin/publish build
```

---

## 4. Interactive SVG & `:g:` Role Conventions

To preserve 100% compatibility with `photon_platform.publish`'s `geometor_interactive.js`:
- Point IDs inside `geometor.model.Model` and SVG `data-ref` attributes are strictly clean alphanumeric identifiers without underscores (`A0..A2`, `B0..B2`, `P0..P5`, `M01..M20`, `M03..M25`, `S1`, `S2`, `O0..O2`, `K1..K4`, `O`, `A`, `B`, `C`, `D`, `F`, `T`).
- Conic circles, arcs, and ellipses register `data-ref="( O P0 )"` with `data-aliases` so ``:g:`𝒞 <g1:( O P0 )>` `` highlights the curve cleanly; keep `data-graphic-id` (`g1`, `g2`, `g3`, ...) unique whenever multiple `.. picture::` blocks appear on a single `.rst` page.
