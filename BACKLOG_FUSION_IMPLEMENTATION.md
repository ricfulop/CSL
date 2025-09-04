## Fusion Backend – Remaining Implementation Backlog

### Sketch
- Spline/NURBS
- Ellipse/Elliptical arc
- Text in sketch
- Advanced constraints and dimensions mapping

### Features (3D)
- Thin extrude
- Rib
- Loft/Sweep fidelity: continuity (G0/G1/G2), orientation (frenet/fixed/binormal)
- Fillet/Chamfer: true per-edge variable arrays and transitions
- Wrap/Emboss/Project to surface
- Draft: face-set targeting from queries
- Holes: taper/drill_angle/callouts; query-driven placement
- Threads: designation/class/handedness (ISO/UNC/UNF/NPT)
- Move/Offset/Replace Face: robust target face/surface mapping
- Split: by sketch/surface bodies (beyond plane)
- Patterns: grid/path; table-driven; robust seed selection
- Booleans: multi-tool sets; keep-tool variants

### Selection/Queries
- Predicates: created_by, owner_feature==, pattern_instances, tangent_connected, curvature≈, by_material, largest_by(axis)
- Stable-ID reconciliation and lineage mapping

### Materials/PMI
- Material references (standardized) with overrides
- PMI notes/annotations

### Export/Thumbnail (v1.1)
- Export options: STL resolution, target selection, units parity
- Thumbnail: deterministic view/style/background handling

### Assemblies/Joints
- Joint creation with limits {linear/angular}, damping, preload

### Diagnostics/Capabilities
- Structured error codes (E12xx/E23xx/E3xxx)
- Granular capability reporting

### APS Integration
- APS Data/OSS storage plumbing for artifacts
- Orchestration strategy (no DA for Fusion; local/hosted agent model)


