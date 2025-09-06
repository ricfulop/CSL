# CSL Glossary (v1.0 → v1.2)

A comprehensive, versioned glossary of CSL constructs, syntax, and JSON IR fields across v1.0, v1.1, and v1.2. Use alongside:
- Spec v1.1: `CSL_v1_1/csl_v1_1_spec.md`
- Spec v1.2 (Draft): `CSL_v1_2/csl_v1_2_spec.md`
- User Guide v1.2: `CSL_v1_2/USER_GUIDE_v1_2.md`
- Schema v1.2: `CSL_v1_2/csl_v1_2_schema.json`

Version tags: [v1.0], [v1.1], [v1.2]

## Header & Metadata
- `csl <version>`: language version ([v1.0], [v1.1], [v1.2])
- `name <string>`: document name ([v1.0])
- `author <string>`: optional author ([v1.0])
- `units mm|in|cm|m|ft`: default units ([v1.0])
- `backend { targets [...] }`: advisory backend targets ([v1.1])

## Parameters & Expressions
- `param <id>: <type> = <expr> in [min, max]` ([v1.0])
  - Types: `length`, `angle`, `count`, `bool`, `real` ([v1.0])
  - Units in expressions (e.g., `10 mm`, `45 deg`) ([v1.0])

## Frames & Planes (selection names vary by backend)
- `world.xy|xz|yz` construction planes ([v1.0])
- Offsets and references by expression or name ([v1.1])

## Sketches
- Declaration: `sketch <id> on <plane> { entities ... constraints ... }` ([v1.0])
- Entities
  - Core: `point`, `line`, `arc`, `circle`, `rect`, `slot`, `polyline` ([v1.0])
  - Additions: `spline` (NURBS), `ellipse`, `elliptical_arc`, `text` ([v1.2])
- Constraints & Dimensions
  - Core: coincident, collinear, parallel, perpendicular, concentric, equal, horizontal, vertical, symmetry, tangent, midpoint, lock/fix ([v1.0])
  - Dimensions: distance (aligned/H/V), angle, radius, diameter; driven/reference dims ([v1.1])
  - Curvature continuity (G2) constraint (diagnostic/interop) ([v1.1])

## Selections & Queries
- Deterministic selection for geometry/topology ([v1.1])
- Predicates (union across versions; availability per backend):
  - Lineage/ownership: `created_by(<featureId>)`, `owner_feature==(<featureId>)` ([v1.1])
  - Patterns: `pattern_instances(feature: id)` ([v1.1])
  - Connectivity: `tangent_connected(seed, tol_deg)` ([v1.1])
  - Metrics: `largest_by(axis)`, `largest` ([v1.1])
  - Geometry with tolerances: `curvature≈`, `radius≈`, `area≈`, `cylindrical_faces(d≈, axis≈)` ([v1.1])
  - Orientation: `faces_parallel(direction)`, `normal==` ([v1.1])
  - Topology helpers: `loop_edges(seed, boundary)`, `of(expand)`, `owner_body` ([v1.1])
  - Attributes: `by_material(name)`, `by_tag`, `by_id` ([v1.1])

## Features (3D)
- Extrude: `feature extrude <id> profile <Q|expr> distance|to_object|through_all ... op new_solid|add|cut|intersect result part|body` ([v1.0])
- Revolve: profile + axis; full angle default ([v1.0])
- Sweep ([v1.0] base, [v1.2] additions)
  - Path + profile; `orientation frenet|fixed|binormal` ([v1.2])
  - Optional `twist <angle>`; `scale <factor>`; `guide`/`rail` via query ([v1.2])
- Loft ([v1.0] base, [v1.1]/[v1.2] additions)
  - `sections [profile1, profile2, ...]` ([v1.0])
  - `continuity G0|G1|G2`, `sections_continuity [...]` ([v1.2])
  - `orientation perpendicular|fixed_normal|binormal` ([v1.2])
  - `guides [...]`, `rail`, `centerline` ([v1.2])
- Thin Extrude: `thickness`, `side one_side|two_sides|center`, `dual_wall` ([v1.1]/[v1.2])
- Rib: `path`, `thickness`, `draft` ([v1.1]/[v1.2])
- Fillet: per-edge groups; `variable radii`; `transitions setback|rolling` ([v1.1]/[v1.2])
- Chamfer: `equal-distance`, `two-distance`, `distance+angle`; per-edge groups ([v1.1]/[v1.2])
- Draft: `faces:Q`, `neutral_plane:Ref`, `angle`, optional `pull_dir` ([v1.2])
- Wrap/Emboss/Project: `onto:face`, `depth`, `draft`, `direction`, `method geodesic|shortest`, `source sketch|text` ([v1.2])
- Move/Offset/Replace Face: `move_face { translate|rotate }`, `offset_face { distance }`, `replace_face { target, with }` ([v1.1]/[v1.2])
- Split Body: `split { body, by: plane|face|profile }` ([v1.1]/[v1.2])
- Mirror: `mirror { bodies, across: plane }` ([v1.1]/[v1.2])
- Surface Ops: `patch`, `extend { distance }`, `trim { tool }`, `knit { targets[], to_solid? }` ([v1.1])
- Holes: `hole { type: simple|counterbore|countersink|taper, diameter, depth|through_all, drill_angle, cbore{diameter,depth}, csink{diameter,angle}, on|face_query }` ([v1.2])
- Threads: `{ designation, class, pitch, handedness, mode: modeled|cosmetic, target|faces_query }` ([v1.1]/[v1.2])
- Patterns: `linear{axis1,axis2,spacing,extent}`, `circular{axis,angle,count}`, `path{path,spacing,align_to_path}`, `table[...]` ([v1.1]/[v1.2])
- Helix: `helix { axis, pitch, turns|height, start_radius }` ([v1.2])

## Sheet Metal
- Base: `sheet_base { profile, thickness }` ([v1.1]/[v1.2])
- Edge flange: `{ edge, length, angle }` ([v1.1]/[v1.2])
- Bend: `{ radius, relief }` ([v1.1]/[v1.2])
- Unfold/Refold: `unfold {}`, `refold {}` ([v1.2])

## Assemblies & Joints
- Assembly: `assembly <id> { instance <name> = <ref> at transform(...); joint ... }` ([v1.1])
- Instances: `transform { matrix[16] | translate | rotate | scale }` ([v1.2])
- Joints: `type rigid|revolute|slider|cylindrical|pin_slot|planar|ball` ([v1.1]/[v1.2])
  - `limits { linear:{min,max}, angular:{min,max} }`, optional `damping`, `preload` ([v1.2])

## Materials & PMI
- Materials: `apply target:Q name:"6061-T6" density:"2.70 g/cm^3"` ([v1.1])
- PMI (light): `pmi note { target:Q, text, frame }`; GD&T (minimal feature-control frames) ([v1.1]/[v1.2])

## Export & Thumbnail
- `export { format: STEP|STL|IGES|3MF|OBJ|..., path, target, options }` ([v1.1])
- `thumbnail { path, width, height, view iso|top|..., style shaded|wireframe|... }` ([v1.1])

## Capabilities & Diagnostics
- `backend.require features:[...] queries:[...]` ([v1.1])
- `backend.prefer features:[...] fallback:<feature>` ([v1.1])
- Conditional: `if backend.supports.features.<name> { ... }` ([v1.1])
- Error codes (typical): E12xx input/validation; E23xx feature/selection; E3xxx environment/runtime ([v1.1])

## JSON IR & Validation
- Each `.csl` compiles to JSON IR. Validate against the v1.2 schema:
  - `make validate-v12` ([v1.2])

## Version Crosswalk (high level)
- v1.0: core parameters, basic sketches, extrude/revolve/sweep/loft, minimal selection, export/thumbnail (early), JSON IR.
- v1.1: export/thumbnail formalization; capabilities; richer constraints; surface ops; selection predicates and determinism; assemblies/joints (basic); materials/PMI (light); conformance.
- v1.2: sketch entities (spline/text/ellipse/elliptical_arc); loft continuity/orientation; variable fillet/chamfer; draft controls; wrap/emboss/project; thread designations; expanded queries; joints with limits/damping/preload; sheet unfold/refold; helix; PMI refinements; validator & CI.
