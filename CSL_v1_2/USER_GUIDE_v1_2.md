## CSL v1.2 User Guide (Draft)

This guide introduces the full v1.2 language: core concepts, syntax, examples, and best practices.

### 1. Getting started
- Minimal header:
```csl
csl 1.2
name "Hello CSL"
units mm
```

### 2. Parameters and expressions
- Typed parameters: `length`, `angle`, `count`, `bool`, `real`.
- Ranges and expressions with units.
```csl
param thickness: length = 6 mm in [3 mm, 12 mm]
param angleA: angle = 30 deg
```

### 3. Sketches
- Entities: `point`, `line`, `arc`, `circle`, `rect`, `slot`, `polyline`, plus v1.2: `spline`, `ellipse`, `elliptical_arc`, `text`.
- Constraints/dimensions: coincident, parallel, perpendicular, tangent, equal, symmetry; driven/reference dimensions.
```csl
sketch s0 on world.xy {
  spline id:sp through [(0,0),(20,10),(40,0)] degree 3
  text id:tx at (10, -5) height 5 mm content "M6" font "Arial"
}
```

### 4. Features (3D)
- Extrude, Revolve, Sweep, Loft, Shell, Draft, Fillet, Chamfer, Hole, Thread, Rib, Wrap/Emboss/Project, Thin, Booleans, Patterns, Move/Offset/Replace/Split, Mirror, Surface ops.

Key v1.2 enhancements:
- Loft continuity/orientation:
```csl
feature loft L sections [s0.profile(c0), s1.profile(r1)] continuity G2 orientation frenet result body
```
- Variable fillet/chamfer and transitions:
```csl
feature fillet F { edges: [ { q: query.created_by("E"), r: [2 mm, 5 mm] } ] transitions: setback }
feature chamfer C { edges: [ { q: query.created_by("F"), distance: 1 mm, angle: 45 deg } ] }
```
- Draft with neutral plane and face set:
```csl
feature draft D { faces: query.by_material("6061-T6"), neutral_plane: world.xy, angle: 3 deg }
```
- Threads (designation/class/handedness/mode):
```csl
feature thread T { designation: "ISO M6x1", class: "6H", pitch: 1 mm, handedness: right, mode: modeled, target: query.created_by("E") }
```
- Emboss/Project:
```csl
feature emboss Em { onto: query.created_by("E"), depth: 0.5 mm, draft: 5 deg }
```

### 5. Selection & queries
- Deterministic selection via tags and predicates: `created_by`, `owner_feature==`, `pattern_instances`, `tangent_connected(seed, tol_deg)`, `largest_by(axis)`, `curvature≈`/`radius≈`/`area≈` (with `tol`), `by_material`.

Common patterns:
```csl
# Select all faces created by feature E
faces query.created_by("E")

# Faces owned by a specific feature id
faces query.owner_feature==("F")

# Pattern instances of a seed feature
bodies query.pattern_instances("seed_feature_id")

# Tangent-connected face set from a seed and angle tolerance (deg)
faces query.tangent_connected(seed: query.by_tag("fillet_seed"), tol_deg: 5)

# Largest face by area on the last body
face query.largest_by(axis: none)

# Cylindrical faces with approximate radius, use tolerance in length units
faces query.cylindrical_faces(r≈: "3 mm", tol: "0.05 mm")

# Faces by assigned material name
faces query.by_material("6061-T6")
```

### 6. Assemblies & joints
- Build assemblies from parts (results of features or imported parts), place instances, and connect with joints. v1.2 adds joint limits and optional damping/preload.

Example:
```csl
# Define a simple base and a slider component
sketch base_sk on world.xy { rect id:plate p1 (0,0) p2 (80 mm, 40 mm) }
feature extrude base_ex profile plate distance 6 mm op new_solid result part

sketch slide_sk on world.xy { rect id:car p1 (-10 mm,-5 mm) p2 (10 mm,5 mm) }
feature extrude car_ex profile car distance 10 mm op new_solid result part

# Assembly with two instances and a slider joint with limits
assembly A {
  instance base = created_by(base_ex)
  instance cart = created_by(car_ex) at transform(translate: (0 mm, 0 mm, 6 mm))

  joint j_slider type slider between cart and base axis world.x {
    limits { linear: { min: 0 mm, max: 50 mm } }
    damping 0.1
    preload 0 N
  }
}
```

### 7. Export & thumbnails
- Deterministic view/style; export STEP/STL/3MF/IGES/SAT/BREP.

Examples:
```csl
export step id:step_out format STEP path "out/part.step" target part
export mesh id:stl_out format STL path "out/part.stl" target part resolution { deviation 0.1 mm, angle 10 deg }

thumbnail id:preview path "out/preview.png" width 1024 height 768 view iso style shaded
```

### 8. Capabilities & diagnostics
- Use `backend.require` and `if backend.supports` for conditional fidelity; unsupported features must emit diagnostics.

Examples:
```csl
# Require specific features before execution
backend.require features:[fillet, chamfer] queries:[tangent_connected]

# Prefer loft but fallback to extrude when unsupported
backend.prefer features:[loft] fallback: extrude

if backend.supports.features.loft {
  feature loft L sections [s0.profile(c0), s1.profile(r1)] continuity G1 result body
} else {
  feature extrude E profile s0.profile(c0) distance 20 mm op new_solid result body
}
```

### 9. JSON IR and validation
- Each `.csl` maps to JSON IR. Validate IRs against the v1.2 schema:
```bash
make validate-v12
```

See `CSL_v1_2/examples/*.json` for reference IRs.

### 10. Materials & properties
- Assign materials and lightweight PMI/notes to targets selected via queries.

Examples:
```csl
materials {
  apply target: query.created_by("base_ex") name: "6061-T6" density: "2.70 g/cm^3"
}

# PMI note on a selected face
pmi note id:n1 target: query.largest_by(axis: none) text: "Critical surface" frame: world.xy
```

### 11. Best practices
- Tag important features and reference tags in queries to reduce ambiguity.
- Prefer geometry/topology predicates (`created_by`, `owner_feature==`, `tangent_connected`) over raw indices.
- Use explicit units on all numeric literals; keep `csl 1.2` header versioned.
- Gate advanced features with `backend.require`/`if backend.supports` for portability.
- Keep exports and thumbnails deterministic (fixed views/styles and tolerances).

### 12. Full example (abridged)
```csl
csl 1.2
name "Bracket with Fillet and Draft"
units mm

param t: length = 6 mm

sketch s on world.xy { rect id:plate p1 (0,0) p2 (80 mm, 40 mm) }
feature extrude E profile plate distance t op new_solid result part

feature fillet F { edges: [ { q: query.created_by("E"), r: [2 mm, 5 mm] } ] }
feature draft D { faces: query.created_by("E"), neutral_plane: world.xy, angle: 3 deg }

export step id:out format STEP path "out/bracket.step" target part
thumbnail id:shot path "out/bracket.png" width 800 height 600 view iso style shaded
```

### 13. Examples
- See `CSL_v1_2/examples/` for: `loft_continuity_demo`, `variable_fillet_chamfer`, `threads_and_emboss`.

For the detailed normative spec, see `CSL_v1_2/csl_v1_2_spec.md`.


