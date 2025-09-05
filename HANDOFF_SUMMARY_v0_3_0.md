## CSL Fusion Backend – Handoff Summary (v0.3.0)

### Executive overview
- Shipped v0.3.0 with constraints parity improvements, loft/fillet/patterns upgrades, stable IDs hardening, selection goldens, export tessellation controls, granular capability publishing, APS tooling, docs/examples, and CI golden gate.

### Key changes completed in this session
- Constraints
  - Construction geometry toggles across sketch entities
  - Driven/reference flags for distance/angle/diameter/radius
  - Equal-length arrays, coincident-to-spline alias
  - Curvature continuity: best-effort mapping + diagnostics with hints

- Loft/Fillet/Patterns
  - Loft: enum-based continuity (G1/G2); orientation mapping; rails/centerline; diagnostics when unsupported
  - Fillet/Chamfer: variable per-edge groups; feature-level vertex setbacks where supported; clearer diagnostics
  - Patterns: circular axis/angle/axis_query; path spacing; rectangular axis1/axis2; per-instance via `instances`/`table`; native element transforms when exposed; robust fallback via move/copy

- Selection/Stable IDs
  - Determinism goldens: created_by, pattern_instances, tangent_connected
  - Stable IDs: refresh persisted lineage on reopen by scanning `CSL:csl_feat` attributes and reconciling entity tokens

- Export/Capabilities
  - STL tessellation controls: deviation, angular tolerance, aspect ratio, max edge length; units/resolution mapping
  - Capability JSON: publish granular feature/query/export support; golden writes snapshot to `out/capabilities_fusion.json`

- APS/CI/Docs
  - CI: golden check gates PRs; ignores env-only diagnostics (E3000); Make targets for conformance/golden
  - APS: auth check; DA stub (list engines; create appbundle/activity; submit workitem); Make targets
  - Docs: coverage matrix updated; new example `CSL_v1_1/examples/constraints_patterns_demo.csl`; README updates

### Release
- Tag: `v0.3.0` (pushed)
- Changelog: `CHANGELOG.md`

### Next milestone (v0.4.0)
- Assemblies/joints: mate connectors, assembly patterns; damping/preload realism
- Surface ops: patch/extend/trim, knit, robust replace-face variants
- Sheet metal: base flange, edge flange, bends, unfold/refold mapping
- Constraints completion: curvature continuity mapping where supported; remaining relations
- Selection determinism: harden across reorder/suppress/regenerate; multi-version Fusion tests
- Stable IDs: cross-version reconciliation and persisted mapping upgrades
- Exports: STEP AP242 metadata; 3MF parity; round-trip validations
- PMI/GD&T: extend notes and light GD&T placement rules
- APS DA: automate appbundle/activity/workitem flow; hosted-runner documentation
- Capabilities: refine/publish versioned capability JSON per release
- Docs/examples: gallery and additional CSL samples
- CI: Fusion-enabled runner job; query fuzzing; performance baselines and gates

### Quick runbook
- Conformance harness
  - `make golden-check`
  - Outputs: `out/conformance_report.json`, `out/golden_summary.json`, `out/capabilities_fusion.json`
- Export units test
  - `PYTHONPATH=. python scripts/export_units_test.py`
- APS
  - Auth: `make aps-auth`
  - DA list engines: `make aps-da-list-engines`
  - DA appbundle/activity/workitem (dev scaffold): see `make aps-da-*` in `Makefile`
- Examples
  - `CSL_v1_1/examples/constraints_patterns_demo.csl`

### Key files
- `triple_lindy/transpilers/fusion360_backend.py`
- `scripts/conformance_harness.py`, `scripts/check_golden.py`, `scripts/export_units_test.py`
- `FUSION_FEATURE_COVERAGE.md`, `CHANGELOG.md`, `README.md`


