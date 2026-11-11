# GEOMETOR • `pappus`

Symbolic projective geometry investigations inspired by **Pappus of Alexandria** (*Synagoge* / *Collection*, Book VII, c. 340 CE), built on exact SymPy algebra, `geometor.model`, and `geometor.divine`.

---

## 1. Purpose & Mathematical Scope

`geometor-pappus` bridges classical Alexandrian analysis and modern projective incidence geometry without floating-point approximation:

1. **Pappus's Hexagon Theorem (*Synagoge* VII.138 & VII.139)**:
   - Straightedge-only collinearity of opposite cross-join meets $M_{01}, M_{12}, M_{20}$ for both parallel ($s(a, b) = 0$) and intersecting carrier lines.
   - Homologous `square` / `circle` / `diamond` triangles formed by pairing corresponding carrier vertices with opposite cross-join meets.
   - Universal polynomial identity proof (`verify_pappus_symbolic()`) over $\mathbb{Q}(a_0, a_1, a_2, b_0, b_1, b_2, m, c)$.
2. **The $S_3$ Six-Permutation Steiner Configuration**:
   - Permuting $(B_0, B_1, B_2)$ across all $6$ permutations in $S_3$ yields up to $18$ cross-join meets and $6$ Pappus lines.
   - The $3$ **even** Pappus lines ($A_3$) concur at the even **Steiner Star point** $S_+$ (`S1`), and the $3$ **odd** Pappus lines ($S_3 \setminus A_3$) concur at the odd **Steiner Star point** $S_-$ (`S2`).
3. **Cross-Ratios, Perspectivities & Harmonic Conjugates**:
   - Central perspectivity (`project_point`, *Synagoge* VII.129) preserving cross-ratios $(A, B; C, D)$.
   - Complete quadrilateral straightedge construction (`construct_harmonic_fourth`) producing $D$ with $(A, B; C, D) = -1$ independently of auxiliary points.
   - Automated harmonic tetrad discovery (`find_harmonic_ranges`) across full line arrangements (e.g., 19 base / 81 full harmonic ranges in the `"harmonic"` preset).
4. **Golden Projectivity in $\mathbb{Q}(\phi)$**:
   - Exact golden chain cross-ratio $(0, 1; \phi, \phi + 1) = \phi$ and its 6-element anharmonic orbit $\{\phi, \phi^{-1}, -\phi^{-1}, -\phi, \phi^{-2}, \phi^2\}$.
   - Harmonic-golden identity $(0, \phi; 1, \phi^3) = -1$ where $\phi^3 = 2\phi + 1$.
   - Emergent golden sections discovered by `geometor.divine` along cross-join $[A_1 B_2]$ (`"golden"` Pappus preset) and conic chord $[P_4 P_0]$ (`"golden_conic"` Pascal preset, `/ M25 P4 P0 /`).
5. **Pascal's *Hexagrammum Mysticum* (1640)**:
   - Smooth-conic generalization across circles and ellipses, Veronese $6 \times 6$ coconicity (`are_coconic`), Chasles observer-independent conic cross-ratio (`conic_cross_ratio`), and universal 6-variable polynomial proof (`verify_pascal_symbolic() == 0`).
   - Bi-triangle $S_3$ Steiner family (`construct_pascal_steiner_family`) concurring at $G_+, G_-$ and complete projective enumeration (`enumerate_hexagrammum_mysticum`) of all **15 chords, 45 diagonal points, 60 Pascal lines, 20 Steiner points, 60 Kirkman points, and 15 Plücker lines**.

---

## 2. Package Architecture (`src/geometor/pappus/`)

- [`__init__.py`](src/geometor/pappus/__init__.py): Public namespace exports and `__version__`.
- [`projective.py`](src/geometor/pappus/projective.py): Exact projective & conic invariants (`PHI`, `quadrance`, `line_spread`, `exact_line_meet`, `project_point`, `cross_ratio`, `anharmonic_orbit`, `is_harmonic_range`, `harmonic_conjugate_point`, `find_harmonic_ranges`, `find_golden_sections`, `enable_divine_analysis`, `circle_stereographic_point`, `conic_equation_through_points`, `are_coconic`, `conic_cross_ratio`).
- [`constructions.py`](src/geometor/pappus/constructions.py): Canonical `PRESETS` (`"hexagon"`, `"parallel"`, `"steiner"`, `"harmonic"`, `"golden"`), `construct_pappus_hexagon`, `construct_pappus_configuration`, `construct_harmonic_fourth`, and `verify_pappus_symbolic`.
- [`pascal.py`](src/geometor/pappus/pascal.py): Smooth-conic `PASCAL_PRESETS` (`"hexagrammum"`, `"convex"`, `"ellipse"`, `"golden_conic"`), `construct_pascal_hexagon`, `construct_pascal_steiner_family`, `enumerate_hexagrammum_mysticum`, and `verify_pascal_symbolic`.
- [`render.py`](src/geometor/pappus/render.py): Pixel-space interactive SVG serializer (`render_svg_string`, `export_svg`) supporting lines, circles, general ellipses (`model._extra_conics`), polygons, segments, and golden/harmonic sections for `photon_platform.publish` (`svg.euclid-graphic`, `geometor_interactive.js`).
- [`__main__.py`](src/geometor/pappus/__main__.py): `pappus` CLI (`build`, `inspect`, `harmonics`, `pascal`).

---

## 3. Development & Verification Commands

All commands run on Python 3.13 via the GEOMETOR `uv` workspace environment:

```bash
# Lint (enforces E, F, I, ANN, and Google-convention D rules)
ruff check src tests demos

# Run test suite (59 exact symbolic, conic, rendering, and CLI tests)
/home/phi/PROJECTS/geometor/.venv/bin/python -m pytest -v

# Run standalone demonstrations
/home/phi/PROJECTS/geometor/.venv/bin/python demos/pappus_hexagon.py
/home/phi/PROJECTS/geometor/.venv/bin/python demos/pappus_six_permutations.py
/home/phi/PROJECTS/geometor/.venv/bin/python demos/harmonic_conjugate.py
/home/phi/PROJECTS/geometor/.venv/bin/python demos/golden_pappus.py
/home/phi/PROJECTS/geometor/.venv/bin/python demos/pascal_hexagrammum.py

# Build Sphinx documentation into docs/
publish build
```

---

## 4. Interactive SVG & `:g:` Role Conventions

To preserve 100% compatibility with `photon_platform.publish`'s `geometor_interactive.js`:
- Point IDs inside `geometor.model.Model` and SVG `data-ref` attributes are strictly clean alphanumeric identifiers without underscores (`A0..A2`, `B0..B2`, `P0..P5`, `M01..M20`, `M03..M25`, `S1`, `S2`, `O`, `P`, `Q`, `R`, `S`, `D`).
- Conic circles and ellipses register `data-ref="( O P0 )"` with `data-aliases="( O P1 ) | ... | ( P0 P1 P2 )"` so ``:g:`𝒞 <g1:( O P0 )>` `` highlights the smooth conic curve cleanly.
- In Sphinx RST prose and `.. step::` blocks, use `:g:` target mapping for subscripted mathematical display, e.g. ``:g:`A_0 <g1:A0>` ``, ``:g:`M_{03} <g1:M03>` ``, ``:g:`G_+ <g3:S1>` ``, and ``:g:`M_{25} P_4 P_0 <g4:/ M25 P4 P0 />` ``.
