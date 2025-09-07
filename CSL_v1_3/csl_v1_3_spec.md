## CSL v1.3 Specification (Draft)

This draft captures new features and clarifications introduced in v1.3:

- Surface operations: `patch`, `extend`, `trim`, `knit` with explicit fields
- Patterns: per‑instance controls via `instances` or `table`
- Constraints: construction toggles, driven/reference dims, equal‑length arrays; curvature continuity diag
- Loft: continuity G1/G2 enums, per‑section continuity, orientation, rails/centerline
- Export: STL tessellation controls (deviation, angular tolerance, aspect ratio, max edge length)
- Capabilities: refined, versioned capability JSON

Backward compatibility
- v1.3 is backward compatible with v1.2; new fields are optional unless noted.

See `CSL_v1_3/csl_v1_3_schema.json` for machine‑readable validation and `USER_GUIDE_v1_3.md` for examples.


### 1) Backward Compatibility
- v1.3 is backward‑compatible with v1.2; all new keys are optional.
- Validation: JSON schema enforces presence and types; adapters must ignore unknown keys.

### 2) Surface Operations
- `patch { edges_query|loop_query, tangent?, merge? }`
- `extend { faces_query|face_query, distance, side? }`
- `trim { target_query|faces_query, tool_query|plane_query, keep? }`
- `knit { faces_query|surfaces_query, tolerance, to_solid? }`

### 3) Patterns (Per‑instance)
- `pattern { kind linear|circular|path|grid|table, seed, instances[], table[] }`
- Per‑instance row: `{ dx, dy, dz, angle, axis, count }` (units where applicable).

### 4) Constraints Updates
- Construction entity flags in sketch entities.
- Reference (driven) dims via `reference true` or `driven true`.
- Equal‑length arrays for multiple lines.
- Curvature continuity: adapters may emit E1205/E1205I with guidance.

### 5) Loft Enhancements
- `continuity: G0|G1|G2`, `sections_continuity: [G0|G1|G2,...]` (best‑effort).
- `orientation: perpendicular|fixed_normal|binormal`.
- `guides[]` and single `rail|centerline` via query.

### 6) Export Controls
- STL: `units`, `resolution: low|medium|high`, `deviation`, `normal_deviation_deg`, `aspect_ratio`, `max_edge`.

### 7) Capabilities JSON
- `out/capabilities_fusion.json` reflects supported features/options with version, commit, Fusion build.
- `make publish-caps` writes versioned archive under `out/capabilities/archive/<version>/`.


