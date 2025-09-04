## CSL v1.1 ↔ CAD Backend Gap Analysis

Scope: Fusion 360 (default), Onshape, SolidWorks, FreeCAD, Blender. Focus: coverage, gaps, fallbacks, API notes.
### Feature Parity Overview

| CSL Area | Fusion 360 | Onshape | SolidWorks | FreeCAD | Blender |
|---|---|---|---|---|---|
| Parameters & Units | ✓ | ✓ | ✓ | ✓ | ~ |
| Sketch Primitives | ✓ | ✓ | ✓ | ✓ | ~ |
| Sketch Constraints/Dimensions | ✓ | ✓ | ✓ | ✓ | × |
| Extrude | ✓ | ✓ | ✓ | ✓ | ✓ |
| Revolve | ✓ | ✓ | ✓ | ✓ | ✓ (Screw) |
| Sweep | ✓ | ✓ | ✓ | ✓ | ~ |
| Loft | ✓ | ✓ | ✓ | ✓ | ~ |
| Shell | ✓ | ✓ | ✓ | ✓ | ~ (Solidify) |
| Draft | ✓ | ✓ | ✓ | ~ | ~ |
| Fillet | ✓ | ✓ | ✓ | ✓ | ~ (Bevel) |
| Chamfer | ✓ | ✓ | ✓ | ✓ | ~ |
| Move/Offset/Replace Face | ✓ | ~ | ✓ | ~ | ~ |
| Thin Extrude | ✓ | ~ | ✓ | ~ | ~ |
| Rib | ✓ | ~ | ✓ | × | × |
| Wrap/Emboss | ~ | ~ | ✓ | × | ~ |
| Hole | ✓ | ✓ | ✓ | ✓ | ~ |
| Thread (cosmetic) | ✓ | ✓ | ✓ | ~ | × |
| Thread (modeled) | ✓ | ~ | ✓ | ~ | ~ |
| Boolean Ops | ✓ | ✓ | ✓ | ✓ | ✓ |
| Patterns/Arrays | ✓ | ✓ | ✓ | ✓ | ✓ |
| Helix | ✓ | ~ | ✓ | ✓ | ✓ |
| Selection/Queries | ~ | ✓ | ~ | ~ | ~ |
| Materials/Props | ✓ | ~ | ✓ | ~ | ~ |
| Assemblies/Joints | ✓ | ✓ | ✓ | × | × |
| Export (STEP/STL/etc.) | ✓ | ✓ | ✓ | ✓ | ✓ (STEP via addon) |
| Thumbnails/Viewport Capture | ✓ | ✓ | ✓ | ✓ | ✓ |
| ECAD Extension | ~ | ~ | ~ | × | × |


### Legend
- ✓: native/complete
- ~: partial/indirect
- ×: unsupported

### 1) Core: Parameters, Units, Metadata
- Fusion 360: ✓ User Parameters; scripts can read/write; unit-safe.
- Onshape: ✓ Variables/FeatureScript params; document units.
- SolidWorks: ✓ Equations/Global Variables; unit conversions.
- FreeCAD: ✓ Spreadsheet/Expressions; unit-aware system.
- Blender: ~ No unit-typed params; scene units exist; custom props needed.

Gaps: Blender lacks typed parameters; use custom properties and unit helpers.

### 2) Sketching Primitives & Constraints
- Fusion 360: ✓ rich sketch API, constraints, dims.
- Onshape: ✓ FeatureScript sketch ops + constraints.
- SolidWorks: ✓ full sketch/constraints API.
- FreeCAD: ✓ Sketcher workbench with robust constraints and entities.
- Blender: × no native 2D constraint sketcher; use curves/mesh; GN limited.

Fallbacks: Blender uses curve/mesh construction; constraints expressed procedurally.

### 3) Features (Solids)
- Extrude/Revolve/Sweep/Loft: Fusion ✓, Onshape ✓, SolidWorks ✓, FreeCAD ✓, Blender ~ (loft via bridge/curve bevel; revolve via Screw).
- Shell/Draft: Fusion ✓, Onshape ✓, SolidWorks ✓, FreeCAD ✓/~ (thickness ✓, draft ~), Blender ~ (Solidify; draft limited).
- Fillet/Chamfer: Fusion ✓, Onshape ✓, SolidWorks ✓, FreeCAD ✓, Blender ~ (Bevel, limited face-level control).
- Move/Offset/Replace Face: Fusion ✓, SolidWorks ✓, Onshape ~ (some ops via FS or sequences), FreeCAD ~, Blender ~ (modifiers/ops approximations).
- Thin Extrude/Rib: Fusion ✓, SolidWorks ✓; Onshape ~; FreeCAD ~; Blender ~.
- Wrap/Emboss: Fusion ~ (Emboss/Project), SolidWorks ✓ (Wrap/Emboss), Onshape ~ (FS techniques), FreeCAD ×, Blender ~ (shrinkwrap/curve deform).
- Hole/Thread: Fusion ✓ (hole + cosmetic/modeled threads), SolidWorks ✓, Onshape ✓/~ (cosmetic), FreeCAD ✓/~ (hole ✓, modeled ~), Blender ~ (boolean + metadata only).
- Patterns/Booleans: Fusion ✓, Onshape ✓, SolidWorks ✓, FreeCAD ✓, Blender ✓ (modifiers).
- Helix: Fusion ✓, SolidWorks ✓, Onshape ~, FreeCAD ✓, Blender ✓ (curve).

Gaps: Blender lacks many face-level CAD operations; modeled threads heavy.

### 4) Selection & Query Language
- Fusion 360: ~ selectors + lineage-based reconciliation implemented; predicates subset (created_by/owner_feature, pattern_instances, tangent_connected, largest_by, curvature/radius/area≈ with tolerances, by_material). Cross-session stability is best-effort.
- Onshape: ✓ robust queries (qCreatedBy, topology filters) align with CSL.
- SolidWorks: ~ selection manager; requires careful naming/IDs.
- FreeCAD: ~ topological naming limits; selection by labels/objects; scripts must maintain IDs.
- Blender: ~ object/data-layer attributes; limited topological stability.

Fallbacks: attach stable IDs/tags; persist mapping table; geometric searches with tolerances.

### Selection/Queries – determinism & tolerances (Fusion)
- Determinism: selections must be unambiguous; adapter emits E12xx with hints when multiple candidates match.
- Stability: uses lineage tokens plus `CSL:csl_feat` attributes to reconcile across sessions.
- Tolerances: geometric predicates accept absolute tolerances (e.g., `tol: 0.05 mm`) and angle tolerances for tangent floods (`tol_deg`).
- Recommended practice: combine geometric predicates with `created_by`/tags to prevent drift under regeneration.

### 5) Materials & Properties
- Fusion 360: ✓ material libraries; physical props.
- Onshape: ~ limited materials; metadata possible.
- SolidWorks: ✓ materials, mass props.
- FreeCAD: ~ material assignments via workbenches; densities available; limited standard libraries.
- Blender: ~ rendering materials only; custom density metadata.

### 6) Assemblies & Joints
- Fusion 360: ✓ joints, as-built joints.
- Onshape: ✓ mate connectors and joints.
- SolidWorks: ✓ mates in assemblies.
- FreeCAD: × core (assembly workbenches exist but not standard in-core).
- Blender: × no mechanical joints; represent transforms/empties.

Fallbacks: for Blender, represent constraints as annotations; export to mechanical backends for validation.

### 7) Export & Thumbnails (v1.1 additions)
- Fusion 360: ✓ STEP, STL, IGES, 3MF, OBJ; viewport capture.
- Onshape: ✓ STEP, STL via API; doc thumbnails via API.
- SolidWorks: ✓ STEP, IGES, STL, 3MF; image export.
- FreeCAD: ✓ STEP, IGES, BREP, STL; GUI image capture.
- Blender: ✓ STL, OBJ, FBX; render/viewport capture; STEP via addon (~).

### 8) ECAD Extension (Optional)
- Fusion 360: ~ limited; treat as metadata only; companion pipeline recommended.
- Onshape: ~ via partner apps/APIs.
- SolidWorks: ~ via CircuitWorks/partners.
- FreeCAD: × not applicable.
- Blender: × not applicable.

### 9) Backend Capability Declarations (CSL §16)
- Fusion 360: publish JSON via adapter; many features true; diagnostics (E-codes) and APS integration available.
- Onshape: publish JSON reflecting FS/API support; note partials.
- SolidWorks: publish JSON via add-in; map partials and variants.
- FreeCAD: publish JSON via adapter; reflect Part/PartDesign coverage and gaps (wrap, rib, draft granularity).
- Blender: publish JSON with limited feature set and fallbacks.

### 10) Determinism, IDs, Diagnostics
- Strategy: maintain stable ID mapping (CSL id ↔ host object GUID) and tag geometry; on re-gen, resolve by lineage or geometric predicates. Emit E12xx (selection), E23xx (boolean/geometry), E3xxx (unsupported) codes.

---

## Implementation Roadmap (Fusion 360 first)

1. Adapter skeleton + capabilities ✓
2. Params/Units + basic sketches ✓
3. Extrude/Hole/Fillet + export/thumbnail ✓
4. Queries: faces/edges by lineage predicates ✓ (expand set next)
5. Threads (cosmetic then modeled), patterns ✓
6. Loft/Sweep/Shell/Chamfer/Draft ✓ (loft continuity/orientation tuning pending)
7. Assemblies/joints ✓
8. Fallbacks for unsupported ops + diagnostics ✓

---

## API Notes & References (high level)

- Fusion 360: `adsk.core`, `adsk.fusion`, script/add-in samples; ExportManager; Camera/Canvas for thumbnails.
- Onshape: FeatureScript docs; REST API: Part Studio features, translations (export), thumbnails.
- SolidWorks: SldWorks API (C#); ModelDoc2, FeatureManager; SaveAs; DisplayDimension; mates.
- FreeCAD: Python API; Part/PartDesign/Sketcher workbenches; exporters for STEP/IGES/BREP/STL.
- Blender: `bpy` (objects, mesh), Geometry Nodes, modifiers (Solidify, Bevel, Screw, Boolean), rendering.


---

## CSL gaps vs CAD APIs (proposed v1.2 extensions)

| Category | API capability (Fusion / Onshape / SolidWorks / FreeCAD / Blender) | CSL v1.1 status | Proposed v1.2 addition |
|---|---|---|---|
| Sketch entities | Fusion: spline/NURBS, text, ellipse, elliptical arc; Onshape FS: spline/ellipse/text; SW: spline/ellipse/text; FreeCAD: spline/ellipse (text via Draft); Blender: curves/text | rect, circle, slot, polyline only | Add `spline`, `text`, `ellipse`, `elliptical_arc` |
| Sketch constraints | Fusion/SW: curvature continuity, equal-length array dims; Onshape: robust set; FreeCAD: robust Sketcher constraints | basic constraints list | Expand constraints: `curvature`, `coincident_to_spline`, richer dims |
| Loft/Sweep fidelity | Fusion/SW: G0/G1/G2, rail orientation; Onshape: continuity options; FreeCAD: limited continuity controls; Blender: limited | continuity G1 only, limited orientation hints | `continuity: G0|G1|G2`, `orientation: frenet|fixed_normal|binormal` |
| Variable fillet/chamfer | Fusion/SW: per-edge variable radius/chamfer; Onshape: variable options; FreeCAD: variable fillet support; Blender: partial | single radius globally | `fillet { edges:[{q, r}], transitions: setback }`, `chamfer { edges:[{q, d|angle}] }` |
| Draft | Fusion/SW: neutral plane, pull direction, face sets; Onshape: draft op supports faces; FreeCAD: draft limited | simple draft | `draft { faces:Q, neutral_plane:Ref, angle:expr, pull_dir:Vector }` |
| Wrap/Emboss | Fusion/SW native; Onshape via techniques; FreeCAD: not native; Blender via deform | generic `wrap` | Add `emboss { onto:face, depth|angle }`, `project { along:dir }` |
| Threads | Fusion/SW: ISO/UNC/UNF/NPT, cosmetic+modeled; Onshape: cosmetic rich; FreeCAD: modeled via helix/sweep | basic thread fields | `thread { designation:ISO|UNC|UNF|NPT, pitch, class, modeled|cosmetic }` |
| Holes | Fusion/SW rich (counterbore/countersink, drill angles, callouts); Onshape: robust; FreeCAD: Hole feature | simple | `hole { type:simple|cbore|csink|taper, params:{...} }` |
| Patterns | Fusion/SW: variable spacing, table-driven; Onshape: robust; FreeCAD: linear/circular | fixed patterns enum | `pattern { kind:linear|circular|grid|table, table:[...]} ` |
| Selection/Queries | Onshape: createdBy, owner feature, pattern instances, tangent/curvature groups; Fusion/SW: partial; FreeCAD: attribute/label-based; Blender: attribute-based | subset | Add predicates: `created_by`, `owner_feature==`, `pattern_instances`, `tangent_connected`, `curvature≈`, `area≈`, `by_material`, `largest_by(axis)` |
| Materials/PMI | Fusion/SW: material libraries, appearances, PMI; Onshape: metadata; FreeCAD: materials via WB; Blender: render materials | basic | `material ref:"ASTM/MatName" overrides{density,color}`, `pmi { note, gd&t (light) }` |
| Assemblies/Joints | Fusion/SW/Onshape: DOF limits, damping, preload; FreeCAD: external WBs; Blender: N/A | basic joint kinds | `joint { limits:{linear:{min,max}, angular:{min,max}}, damping, preload }` |
| Capabilities | All can report subsets; need granularity | present | Finer-grained fields for variable fillet, G2 loft, emboss, PMI |

Notes:
- Predicates using `≈` should allow absolute/relative tolerances for curvature/area/angle.
- Where host lacks native support (e.g., Blender), adapters should implement approximations or emit E3xxx diagnostics.

## Production-Grade Closure Plan for Fusion 360

Below are the remaining items to reach production-grade (100%) completeness, with acceptance criteria.

- Loft continuity (G1/G2) and orientation
  - Acceptance: explicit continuity/orientation flags in IR honored or deterministically approximated; visual/geometry tests pass for representative lofts; diagnostics only when API lacks support.
- Fillet/Chamfer transitions and setbacks
  - Acceptance: per-edge variable arrays with native transitions/setbacks where supported; comparison tests validate distances/radii at sample points; fallbacks documented.
- Native wrap/emboss
  - Acceptance: emboss/wrap onto planar/cylindrical faces with depth/angle; deterministic artifacts; diagnostics when unsupported.
- Stable IDs across sessions
  - Acceptance: persisted mapping (CSL id ↔ host GUID/entityToken lineage) that reconciles after reopen/regeneration; tests verify selection stability across saves.
- Queries expansion and determinism
  - Acceptance: owner_feature==, pattern_instances, tangent_connected tolerances, curvature/radius/area≈ with absolute/relative tol; unambiguous failures with suggested predicates.
- Export/units parity
  - Acceptance: exported STEP/STL units verified by import round-trip tests; resolution controls mapped to target tessellation thresholds.
- Assemblies/joints completeness
  - Acceptance: revolute/slider/rigid with min/max limits, damping, preload; param round-trip tests validate numeric fidelity.
- Materials/PMI
  - Acceptance: apply library material refs and overrides; PMI notes placement with readable formatting; appearance round-trip checks.
  - Status: complete (material refs + appearance overrides; PMI notes on faces/planes with rotation/sizing)
- APS orchestration hardening
  - Acceptance: token refresh, retries with backoff, telemetry (duration/status), configurable buckets/paths; integration test uploads artifacts.
  - Status: complete (token caching/refresh, retry-with-backoff HTTP helper, telemetry fields, default bucket via env)

Each item will include: implementation notes, test checklist, and diagnostics catalog (E-codes) for unsupported paths.


