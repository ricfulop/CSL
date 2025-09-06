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

### 6. Assemblies & joints
- Instances and joints with limits and optional damping/preload.

### 7. Export & thumbnails
- Deterministic view/style; STEP/STL/3MF/IGES/SAT/BREP.

### 8. Capabilities & diagnostics
- Use `backend.require` and `if backend.supports` for conditional fidelity; unsupported features must emit diagnostics.

### 9. JSON IR and validation
- Each `.csl` maps to JSON IR; validate with:
```bash
make validate-v12
```

### 10. Examples
- See `CSL_v1_2/examples/` for: `loft_continuity_demo`, `variable_fillet_chamfer`, `threads_and_emboss`.

For the detailed normative spec, see `CSL_v1_2/csl_v1_2_spec.md`.


