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
