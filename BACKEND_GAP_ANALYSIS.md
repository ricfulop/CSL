## CSL v1.1 ↔ CAD Backend Gap Analysis

Scope: Fusion 360 (default), Onshape, SolidWorks, Blender. Focus: coverage, gaps, fallbacks, API notes.
### Feature Parity Overview

| CSL Area | Fusion 360 | Onshape | SolidWorks | Blender |
|---|---|---|---|---|
| Parameters & Units | ✓ | ✓ | ✓ | ~ |
| Sketch Primitives | ✓ | ✓ | ✓ | ~ |
| Sketch Constraints/Dimensions | ✓ | ✓ | ✓ | × |
| Extrude | ✓ | ✓ | ✓ | ✓ |
| Revolve | ✓ | ✓ | ✓ | ✓ (Screw) |
| Sweep | ✓ | ✓ | ✓ | ~ |
| Loft | ✓ | ✓ | ✓ | ~ |
| Shell | ✓ | ✓ | ✓ | ~ (Solidify) |
| Draft | ✓ | ✓ | ✓ | ~ |
| Fillet | ✓ | ✓ | ✓ | ~ (Bevel) |
| Chamfer | ✓ | ✓ | ✓ | ~ |
| Move/Offset/Replace Face | ✓ | ~ | ✓ | ~ |
| Thin Extrude | ✓ | ~ | ✓ | ~ |
| Rib | ✓ | ~ | ✓ | × |
| Wrap/Emboss | ~ | ~ | ✓ | ~ |
| Hole | ✓ | ✓ | ✓ | ~ |
| Thread (cosmetic) | ✓ | ✓ | ✓ | × |
| Thread (modeled) | ✓ | ~ | ✓ | ~ |
| Boolean Ops | ✓ | ✓ | ✓ | ✓ |
| Patterns/Arrays | ✓ | ✓ | ✓ | ✓ |
| Helix | ✓ | ~ | ✓ | ✓ |
| Selection/Queries | ~ | ✓ | ~ | ~ |
| Materials/Props | ✓ | ~ | ✓ | ~ |
| Assemblies/Joints | ✓ | ✓ | ✓ | × |
| Export (STEP/STL/etc.) | ✓ | ✓ | ✓ | ✓ (STEP via addon) |
| Thumbnails/Viewport Capture | ✓ | ✓ | ✓ | ✓ |
| ECAD Extension | ~ | ~ | ~ | × |


### Legend
- ✓: native/complete
- ~: partial/indirect
- ×: unsupported

### 1) Core: Parameters, Units, Metadata
- Fusion 360: ✓ User Parameters; scripts can read/write; unit-safe.
- Onshape: ✓ Variables/FeatureScript params; document units.
- SolidWorks: ✓ Equations/Global Variables; unit conversions.
- Blender: ~ No unit-typed params; scene units exist; custom props needed.

Gaps: Blender lacks typed parameters; use custom properties and unit helpers.

### 2) Sketching Primitives & Constraints
- Fusion 360: ✓ rich sketch API, constraints, dims.
- Onshape: ✓ FeatureScript sketch ops + constraints.
- SolidWorks: ✓ full sketch/constraints API.
- Blender: × no native 2D constraint sketcher; use curves/mesh; GN limited.

Fallbacks: Blender uses curve/mesh construction; constraints expressed procedurally.

### 3) Features (Solids)
- Extrude/Revolve/Sweep/Loft: Fusion ✓, Onshape ✓, SolidWorks ✓, Blender ~ (loft via bridge/curve bevel; revolve via Screw).
- Shell/Draft: Fusion ✓, Onshape ✓, SolidWorks ✓, Blender ~ (Solidify; draft limited).
- Fillet/Chamfer: Fusion ✓, Onshape ✓, SolidWorks ✓, Blender ~ (Bevel, limited face-level control).
- Move/Offset/Replace Face: Fusion ✓, SolidWorks ✓, Onshape ~ (some ops via FS or sequences), Blender ~ (modifiers/ops approximations).
- Thin Extrude/Rib: Fusion ✓, SolidWorks ✓; Onshape ~; Blender ~.
- Wrap/Emboss: Fusion ~ (Emboss/Project), SolidWorks ✓ (Wrap/Emboss), Onshape ~ (FS techniques), Blender ~ (shrinkwrap/curve deform).
- Hole/Thread: Fusion ✓ (hole + cosmetic/modeled threads), SolidWorks ✓, Onshape ✓/~ (cosmetic), Blender ~ (boolean + metadata only).
- Patterns/Booleans: Fusion ✓, Onshape ✓, SolidWorks ✓, Blender ✓ (modifiers).
- Helix: Fusion ✓, SolidWorks ✓, Onshape ~, Blender ✓ (curve).

Gaps: Blender lacks many face-level CAD operations; modeled threads heavy.

### 4) Selection & Query Language
- Fusion 360: ~ selectors exist; not as robust as FeatureScript queries.
- Onshape: ✓ robust queries (qCreatedBy, topology filters) align with CSL.
- SolidWorks: ~ selection manager; requires careful naming/IDs.
- Blender: ~ object/data-layer attributes; limited topological stability.

Fallbacks: attach stable IDs/tags; persist mapping table; geometric searches with tolerances.

### 5) Materials & Properties
- Fusion 360: ✓ material libraries; physical props.
- Onshape: ~ limited materials; metadata possible.
- SolidWorks: ✓ materials, mass props.
- Blender: ~ rendering materials only; custom density metadata.

### 6) Assemblies & Joints
- Fusion 360: ✓ joints, as-built joints.
- Onshape: ✓ mate connectors and joints.
- SolidWorks: ✓ mates in assemblies.
- Blender: × no mechanical joints; represent transforms/empties.

Fallbacks: for Blender, represent constraints as annotations; export to mechanical backends for validation.

### 7) Export & Thumbnails (v1.1 additions)
- Fusion 360: ✓ STEP, STL, IGES, 3MF, OBJ; viewport capture.
- Onshape: ✓ STEP, STL via API; doc thumbnails via API.
- SolidWorks: ✓ STEP, IGES, STL, 3MF; image export.
- Blender: ✓ STL, OBJ, FBX; render/viewport capture; STEP via addon (~).

### 8) ECAD Extension (Optional)
- Fusion 360: ~ limited; separate product; treat as metadata only.
- Onshape: ~ via partner apps/APIs.
- SolidWorks: ~ via CircuitWorks/partners.
- Blender: × not applicable.

### 9) Backend Capability Declarations (CSL §16)
- Fusion 360: publish JSON via adapter; many features true.
- Onshape: publish JSON reflecting FS/API support; note partials.
- SolidWorks: publish JSON via add-in; map partials and variants.
- Blender: publish JSON with limited feature set and fallbacks.

### 10) Determinism, IDs, Diagnostics
- Strategy: maintain stable ID mapping (CSL id ↔ host object GUID) and tag geometry; on re-gen, resolve by lineage or geometric predicates. Emit E12xx (selection), E23xx (boolean/geometry), E3xxx (unsupported) codes.

---

## Implementation Roadmap (Fusion 360 first)

1. Adapter skeleton + capabilities
2. Params/Units + basic sketches
3. Extrude/Hole/Fillet + export/thumbnail
4. Queries: faces/edges by tag, normals, diameter≈
5. Threads (cosmetic then modeled), patterns
6. Loft/Sweep/Shell/Chamfer/Draft
7. Assemblies/joints
8. Fallbacks for unsupported ops

---

## API Notes & References (high level)

- Fusion 360: `adsk.core`, `adsk.fusion`, script/add-in samples; ExportManager; Camera/Canvas for thumbnails.
- Onshape: FeatureScript docs; REST API: Part Studio features, translations (export), thumbnails.
- SolidWorks: SldWorks API (C#); ModelDoc2, FeatureManager; SaveAs; DisplayDimension; mates.
- Blender: `bpy` (objects, mesh), Geometry Nodes, modifiers (Solidify, Bevel, Screw, Boolean), rendering.


