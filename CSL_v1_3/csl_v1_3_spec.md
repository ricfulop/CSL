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


