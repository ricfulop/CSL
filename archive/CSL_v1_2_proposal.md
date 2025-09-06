## CSL v1.2 – Fusion Parity and Cross-Backend Extensions (Proposal)

### Goals
- Achieve practical feature parity with Fusion 360 for day-to-day mechanical workflows.
- Maintain portability to Onshape, SolidWorks, FreeCAD, and Blender with capability-driven fallbacks.
- Keep grammar minimal, deterministic, and LLM-friendly.

### Scope Overview
- Sketch entities and constraints
- Solids (loft/sweep fidelity, variable fillet/chamfer, draft)
- Holes and threads
- Patterns and mirrors
- Face operations (move/offset/replace/split)
- Wrap/emboss/project
- Selection predicates and queries
- Materials and PMI (light)
- Assemblies/joints (limits/damping/preload)

### Parity Matrix – Fusion focus (others indicative)

| Area | Fusion | Onshape | SolidWorks | FreeCAD | Blender |
|---|---|---|---|---|---|
| Spline/NURBS | ✓ | ✓ | ✓ | ✓ | ~ |
| Text in sketch | ✓ | ✓ | ✓ | ✓ (Draft) | ✓ |
| Ellipse/Elliptical arc | ✓ | ✓ | ✓ | ✓ | ~ |
| Loft continuity G0/G1/G2 | ✓ | ~ | ✓ | ~ | ~ |
| Loft rail orientation | ✓ | ~ | ✓ | ~ | ~ |
| Variable fillet/chamfer | ✓ | ~ | ✓ | ~ | ~ |
| Draft neutral plane | ✓ | ✓ | ✓ | ~ | ~ |
| Hole variants (cbore/csink/taper) | ✓ | ✓ | ✓ | ~ | ~ |
| Threads (ISO/UNC/UNF/NPT) | ✓ | ~ | ✓ | ~ | × |
| Pattern table-driven | ✓ | ~ | ✓ | ~ | ~ |
| Wrap/Emboss | ✓ | ~ | ✓ | × | ~ |
| Selection: created_by/owner/pattern/curvature | ~ | ✓ | ~ | ~ | ~ |
| Materials + PMI (light) | ✓ | ~ | ✓ | ~ | ~ |
| Joints with limits/damping/preload | ✓ | ✓ | ✓ | × | × |

### Syntax Additions (proposed)

- Sketch
  - `spline id:s1 through [(x,y),(x,y),...] degree 3`  (optional degree/fit)
  - `ellipse id:e1 center (x,y) axes (a,b) rot 30 deg`
  - `elliptical_arc id:ea1 center (...) axes (...) start 0 deg end 90 deg`
  - `text id:tx at (x,y) height 5 mm content "M6" font "Arial"`

- Loft/Sweep
  - `feature loft L sections [...] guides [...] continuity G2 orientation frenet`
  - `feature loft L sections [...] rail qEdge` (alias: `centerline qEdge`)
  - `feature loft L sections [...] sections_continuity [G0,G1,G2]` (per-section; best-effort)
  - `feature sweep S path skP.curve("p") profile skQ.profile("q") orientation fixed_normal`

- Variable fillet/chamfer
  - `feature fillet f edges [ {q: query.edges(...), r: 2 mm, tangent_chain:true}, {...} ] transitions setback 1 mm`
  - `feature chamfer c edges [ {q: qEdges, d: 1 mm}, {q: qEdges2, angle: 45 deg}, {q: qEdges3, d:1 mm, d2:0.5 mm} ]`
  - Global flags allowed: `tangent_chain:true` (fillet), `angle:45 deg` (chamfer)

- Draft
  - `feature draft d faces query.face(part, by_tag:"mold") neutral_plane plane.world.xy angle 2 deg pull_dir +Z`

- Holes
  - `feature hole h on face qFace at points [(x,y)] type simple d: 5 mm depth through_all`
  - `feature hole h2 on face qFace at points [...] type counterbore d: 4 mm cb_d: 8 mm cb_depth: 3 mm`
  - `type countersink ... cs_d: X cs_angle: 82 deg`  `type taper ... drill_angle: 118 deg`

- Threads
  - `feature thread t on faces qCyl mode modeled designation "UNC 1/4-20-2B" handed right length 12 mm`

- Patterns
  - `feature pattern p kind linear seed feature:"main" direction +X count 3 spacing 20 mm`
  - `feature pattern p2 kind table seed feature:"h1" table [ {dx:0,dy:0}, {dx:20,dy:0}, {dx:40,dy:10} ]`
  - Per-instance overrides (optional): `{dx,dy,count}` rows; additional fields may be added per backend capability

- Wrap/Emboss/Project
  - `feature emboss em onto face qFace depth 0.5 mm from sketch logo`
  - `feature project pr along +Z curves sketch logo onto face qFace`

- Selection Predicates (queries)
  - Add: `created_by(id:"...", type:...)`, `owner_feature=="..."`, `pattern_instances(feature:"...", index:*, type:...)`, `tangent_connected`, `curvature≈`, `by_material`, `largest_by(axis)`

- Materials / PMI
  - `material part = { ref:"ISO:6061-T6", density:"2.70 g/cm^3", color:#a8c0ff }`
  - `pmi note n1 on face qFace text "CSINK 82°"`
  - GD&T (light) remains out-of-scope for v1.2; consider v1.3

- Joints
  - `joint j1 type revolute between a.mc and b.mc limits { angular:{min:0 deg,max:90 deg} } damping 0.1 preload 5 N`

### JSON Schema Extensions (high level)
- Add new sketch entity kinds: `spline`, `ellipse`, `elliptical_arc`, `text`.
- Sketch constraints: add `curvature`, `coincident_to_spline` (alias), and `equal_length { items:[id...] }` form.
- Fillet/Chamfer objects permit arrays per-edge with parameters.
- Fillet: add `tangent_chain: boolean` at group or feature level.
- Chamfer: add `angle` (deg), and `d2|distance2` for two-distance definition; allow group/global.
- Draft object with `faces`, `neutral_plane`, `pull_dir`.
- Hole object with variant-specific fields.
- Thread object includes `designation`, `class`, `handed`, `modeled|cosmetic`.
- Pattern object supports `kind`, `seed`, `direction(s)`, `count`, `spacing`, and optional `table`.
- Wrap/Emboss/Project feature objects.
- Query predicates expanded; toleranced numeric fields for curvature/area.
- Loft: `sections_continuity` array (G0/G1/G2), and single `rail|centerline` in addition to `guides`.

### Backwards Compatibility
- All new fields are optional with sensible defaults.
- v1.1 programs remain valid; adapters can ignore unsupported ops based on capabilities.

### Implementation Plan (Fusion-first)
1) Holes (all variants) + Chamfer + Draft
2) Threads (cosmetic → mode led), Patterns (linear/circular → table), Wrap/Emboss
3) Loft/Sweep G2 + orientation, Variable fillet arrays
4) Sketch: spline/ellipse/text, advanced constraints
5) Predicates, Materials/PMI, Joints limits/damping/preload

### Notes on APS Design Automation
- For headless jobs and batch exports, align with APS Design Automation work patterns (AppBundle/Activity/WorkItem). See Autodesk’s common workflows tutorial: https://aps.autodesk.com/en/docs/design-automation/v3/tutorials/common/


