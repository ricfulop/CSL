## Fusion Backend – Implementation Status (v1.1)

### Completed

### Sketch
- Spline/NURBS
- Ellipse/Elliptical arc
- Text in sketch
- Advanced constraints and dimensions mapping

### Features (3D)
- Thin extrude (thin wall with side control)
- Rib (path from sketch/edges, thickness, draft)
- Fillet/Chamfer: per-edge variable groups
- Project to surface (sketch-based projection)
- Draft: face-set targeting from queries
- Holes: taper, drill_angle; query-driven placement; counterbore/countersink
- Threads: designation/class/handedness (ISO/UNC/UNF/NPT), modeled/cosmetic
- Move/Offset/Replace Face: robust target face/surface mapping via queries
- Split: by sketch/profile or surface bodies (beyond plane)
- Patterns: grid/path; robust seed selection
- Booleans: multi-tool sets; keep-tool variants

### Selection/Queries
- Lineage tracking and predicates: created_by, largest_by(axis)

### Materials/PMI
- Material/appearance proxy and PMI notes annotations

### Export/Thumbnail (v1.1)
- Export options: STL resolution, target selection, units parity (best-effort)
- Thumbnail: deterministic view/style/background handling

### Assemblies/Joints
- Joint creation with limits {linear/angular}, basic damping/preload mapping

### Diagnostics/Capabilities
- Structured error codes (E12xx/E23xx/E3xxx)
- Granular capability reporting

### APS Integration
- APS Data/OSS storage plumbing for artifacts (token, bucket, upload)

---

### Remaining

### Features (3D)
- Loft/Sweep fidelity: explicit continuity (G0/G1/G2) and full orientation mapping ([#1](https://github.com/ricfulop/CSL/issues/1))
- Fillet/Chamfer: advanced transitions/setbacks ([#2](https://github.com/ricfulop/CSL/issues/2))
- Wrap/Emboss: native-to-surface emboss/wrap mapping ([#3](https://github.com/ricfulop/CSL/issues/3))
- Patterns: table-driven patterns ([#4](https://github.com/ricfulop/CSL/issues/4))

### Selection/Queries
- Predicates: owner_feature==, pattern_instances, tangent_connected, curvature≈, by_material ([#5](https://github.com/ricfulop/CSL/issues/5))
- Stable-ID reconciliation improvements across regen ([#5](https://github.com/ricfulop/CSL/issues/5))

### APS Integration
- Orchestration strategy (no DA for Fusion; local/hosted agent model) ([#6](https://github.com/ricfulop/CSL/issues/6))


