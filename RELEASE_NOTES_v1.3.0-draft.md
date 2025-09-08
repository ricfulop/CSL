## CSL v1.3.0 – Release Highlights

### 🎉 Major Addition: Complete FreeCAD Backend Implementation

- **100% Feature Coverage**: Full implementation of all CSL v1.3 features in FreeCAD
- **FreeCAD Workbench**: Custom workbench with file watcher for live updates
- **Cross-Platform Support**: CSL now supports both Fusion 360 and FreeCAD backends

### Core CSL v1.3 Features

- Surface ops: patch/extend/trim/knit
- Patterns: per‑instance controls via `instances`
- Constraints: construction geometry, reference dims, equal‑length arrays; curvature continuity diag
- Loft: continuity/orientation options; rails/centerline
- Export: STL tessellation controls
- Capabilities: refined JSON

Backward compatible with v1.2; new fields are optional.

### New Features
- Surface operations with explicit queries and options:
  - `patch { edges_query|loop_query, tangent?, merge? }`
  - `extend { faces_query|face_query, distance, side? }`
  - `trim { target_query|faces_query, tool_query|plane_query, keep? }`
  - `knit { faces_query|surfaces_query, tolerance, to_solid? }`
- Pattern per‑instance controls via `instances[]` or `table[]` with per‑occ translation `dx/dy/dz` and optional rotation.
- Constraints quality of life:
  - Construction entity flags
  - Driven/reference dimensions
  - Equal‑length arrays
  - Curvature continuity diagnostics (E1205/E1205I)
- Loft enhancements:
  - Continuity `G0|G1|G2`, per‑section continuity array
  - Orientation `perpendicular|fixed_normal|binormal`
  - Rails/centerline via queries
- Export (STL) tessellation controls: `deviation`, `normal_deviation_deg`, `aspect_ratio`, `max_edge`, units and resolution.
- Capabilities JSON refined and versioned; `make publish-caps` archives `out/capabilities/archive/<version>/`.

### Backend Implementations

#### FreeCAD Backend (NEW!)
- **Complete implementation** of all CSL v1.3 features
- **Native Python integration** via `triple_lindy.transpilers.freecad_backend`
- **FreeCAD Workbench** with GUI toolbar and file watcher
- **Full feature support**:
  - All sketch entities and constraints
  - All 3D features (extrude, revolve, loft, sweep, etc.)
  - Fillets, chamfers with edge/face queries
  - Boolean operations, patterns, mirrors
  - Export to STEP, IGES, STL, BREP
- **Test suite** with comprehensive examples

#### Fusion 360 Backend
- Best‑effort implementations with capability gating and diagnostics when the API lacks a direct control.
- Assemblies stubs improved (mate connector basis tagging, pattern per‑occ tagging) remain optional.

### Compatibility
- v1.3 is backward compatible with v1.2; older IR continues to validate and execute.
- Unknown fields are ignored by adapters per spec; schema enforces new fields only when present.

### Conformance & Examples
- Conformance suite expanded with v1.3 cases for patterns per‑instance, loft continuity/orientation, constraints updates, and STL export controls.
- See `CSL_v1_3/USER_GUIDE_v1_3.md` for quick examples.

### Migration
- No breaking changes expected; follow diagnostics to strengthen queries and selections where needed.


