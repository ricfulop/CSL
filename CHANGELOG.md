## v0.2.0 (Fusion backend enhancements, docs, and conformance)

Highlights
- Fusion backend: materials/PMI, APS retries+token cache+telemetry, loft G2/rails, fillet/chamfer (tangent-chain, angle/two-distance), draft pull_dir/plane, wrap/emboss direction, threads targeting, holes (through_all/depth), patterns per-instance table, advanced joints, stronger queries/stable IDs.
- Conformance: harness expanded + golden summary; export units test.
- Docs: coverage checklist, proposal updates (v1.2), README updates.

Commits
- Fix `_apply_materials_and_pmi`; add materials/PMI enhancements
- APS hardening (token cache/refresh, retry helper, telemetry, bucket default)
- Loft: sections_continuity, rail/centerline; diagnostics
- Fillet/chamfer: tangent-chain, distance+angle, two-distance; variable groups preserved
- Draft: neutral_plane via query/name; pull direction
- Wrap/emboss/project: along-direction parsing; depth/angle/engrave
- Threads: face queries, designation/class/hand/length mapping
- Holes: plane selection, through_all/depth distance, callout note
- Patterns: per-instance table (dx/dy/dz, angle+axis, count)
- Joints: cylindrical/planar/ball/pinslot where supported; limits mapping
- Queries: by_material filter; lineage persistence retained
- Conformance: harness golden summary; export_units_test
- Docs: `FUSION_FEATURE_COVERAGE.md`, updated `README.md`, `CSL_v1_2_proposal.md`

## v0.3.0 (feature parity, determinism, CI, and APS tooling)

Highlights
- Constraints parity: construction geometry toggles; driven/reference dimensions; curvature diag.
- Loft parity: enum-based continuity (G1/G2), orientation mapping, rails/centerline query support.
- Fillet/chamfer: variable groups + feature-level vertex setbacks; improved diagnostics.
- Patterns: circular axis/angle/axis_query, path spacing, rectangular axis1/axis2.
- Stable IDs: persisted-lineage refresh via `CSL:csl_feat` attributes on reopen.
- Selection determinism: new goldens (created_by, pattern_instances, tangent_connected).
- Export parity: advanced STL tessellation controls (deviation, angular tol, aspect ratio, max edge).
- Capabilities: granular JSON publishing of features/queries/export options.
- CI: golden check gating; APS auth in workflow; Make targets for conformance and APS ops.

Commits
- Constraints: add construction flags and driven/reference dims, tests, coverage updates
- Loft: continuity/orientation enums and rails handling; new orientation case
- Fillet: feature-level setbacks; conformance case
- Patterns: axis/angle/spacing/axes support; patterns suite
- Selection: determinism case and harness post-queries
- CI: golden checker filters E3000; workflow wired; Make targets
- Export: advanced STL tessellation; extended export units test
- Capabilities: publish granular JSON; snapshot saved by golden check
- APS: DA stub (list engines); APS auth check; orchestrate example target
- Stable IDs: refresh persisted tokens from attributes on reload
