## v1.2.0-draft (CSL v1.2 Draft: schema/spec/examples, CI, conformance)

Highlights
- Language: Introduced CSL v1.2 draft spec and schema (richer sketches; loft continuity/orientation; variable fillet/chamfer; draft controls; wrap/emboss/project; threads with designations; expanded queries; assemblies/joints with limits; sheet metal unfold/refold; helix; light PMI).
- Examples: Added v1.2 `.csl` and JSON IR examples (loft continuity, sweep options, hole variants, face ops, sheet unfold/refold, helix, threads/emboss), all validating against the schema.
- Docs: Comprehensive v1.2 User Guide; migration guide v1.1 → v1.2; conformance checklist; updated README with “What’s new in v1.2” and CI badge.
- Conformance: Extended harness with v1.2 cases (holes, sweep, face ops, sheet, emboss/project); golden summary preserved; dry‑run friendly.
- CI: GitHub Actions workflow to validate all v1.2 JSON IR examples on push/PR.

Commits
- Add `CSL_v1_2/csl_v1_2_spec.md`, schema, user guide, migration notes, and conformance checklist.
- Extend schema for holes/sweep/thin_extrude/rib/face ops/sheet metal/patterns/assemblies/helix/PMI; add validating examples.
- Update DOC_INDEX, docs_index.json, and README (v1.2 status, examples, CI badge, what’s new).
- Add validator script and Make targets; CI workflow to run validation.
- Expand conformance harness with v1.2 coverage and generate reports.

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

## v0.4.0 (surface ops, AP242 sidecar, PMI/GD&T minimal, assemblies stubs, determinism)

Highlights
- Selection determinism: sorted-token lineage, persisted normalization, deterministic face ordering; added determinism goldens.
- Surface ops: patch / extend / trim / knit (best-effort; API-version dependent); new conformance case.
- Export: STEP AP242 sidecar metadata JSON.
- PMI/GD&T: minimal feature-control-frame placement via PMI text.
- Assemblies: mate connectors and assembly patterns stubs.
- Capabilities/Docs/Make: capabilities dump (`make caps`), coverage and README updates.

Commits
- Lineage/selection determinism hardening in `triple_lindy/transpilers/fusion360_backend.py`.
- Surface ops handlers and conformance cases.
- STEP AP242 sidecar emission in export path; export case.
- PMI/GD&T minimal note placement and case.
- Assembly stubs (`mate_connector`, `assembly_pattern`) and case.
- Capabilities metadata additions; `scripts/dump_capabilities.py`; Make targets & docs updates.

## v0.5.0 (Fusion backend 100% coverage, selection/threads/wrap/export complete)

Highlights
- Coverage: Fusion backend feature coverage reached 100% (`FUSION_FEATURE_COVERAGE.md`).
- Selection/Queries: created_by/owner_feature, pattern_instances, tangent_connected, largest/largest_by, curvature≈/radius≈/area≈, by_material/by_tag/by_id, faces_parallel/normal==, cylindrical_faces(d≈/r≈, axis≈), loop_edges(seed,boundary), of(expand), owner_body; lineage tokens+attributes; cross‑session persistence.
- Threads: cosmetic/modeled; faces_query or cylindrical_faces(d≈/axis≈); designation/class/hand/length mapping; diameter best‑effort.
- Wrap/Emboss/Project: modes (wrap/emboss/project), depth/draft/direction, reverse; inline text or sketch sources; multi‑target faces best‑effort; geodesic requested with diagnostic fallback; lineage recorded.
- Loft: sections; continuity mapping (G0/G1/G2 incl. per‑section when exposed); orientation (perpendicular/fixed_normal/binormal); rails/centerline.
- Move/Offset/Replace Face: native move (translate/rotate), offset faces (± distance, multi‑face sets), replace faces with plane or arbitrary face/surface; fallbacks retained.
- Sketch constraints: curvature continuity G2 with multi‑API fallback; deterministic tangent fallback + diagnostics.
- Export/Thumbnail: STEP with AP242 protocol attempt + sidecar metadata; STL units/resolution + advanced tessellation (deviation/angle/aspect/max‑edge); 3MF units/binary/appearance parity; deterministic thumbnails.
- Automation: remote validation scripts/targets; hello/status flows; conformance cases extended.

Commits
- Selection/queries completion and lineage persistence improvements.
- Threads targeting and properties (designation/class/hand/length).
- Wrap/Emboss/Project parity including inline text source and multi‑face support.
- Loft continuity/orientation and rails handling refinements.
- Move/Offset/Replace Face native implementations and enhancements.
- Sketch G2 curvature continuity with diagnostics; conformance case added.
- Export/Thumbnail completion (AP242 attempt + sidecar; STL tessellation; 3MF parity).
- Conformance harness cases for loft, threads, wrap/project, G2; coverage recompute to 100%.
- Automation remote validation orchestrator and Make targets.
