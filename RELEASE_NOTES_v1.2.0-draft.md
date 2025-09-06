# CSL v1.2.0 (Draft)

CSL v1.2 introduces richer sketches, higher‑fidelity loft/sweep controls, variable fillet/chamfer, draft controls, wrap/emboss/project options, thread designations, expanded selection predicates, assemblies/joints with limits, sheet‑metal unfold/refold, a helix curve generator, and light PMI. A validator and CI workflow ensure IR compliance.

## Highlights
- Language/spec/schema
  - Spec: `CSL_v1_2/csl_v1_2_spec.md`
  - Schema: `CSL_v1_2/csl_v1_2_schema.json`
  - User Guide: `CSL_v1_2/USER_GUIDE_v1_2.md`
  - Migration (v1.1 → v1.2): `MIGRATION_v1_1_to_v1_2.md`
  - Conformance checklist: `CSL_v1_2/conformance/README.md`
- New examples (CSL + IR): `CSL_v1_2/examples/`
  - Loft continuity/orientation, Sweep options, Hole variants, Face ops, Sheet unfold/refold, Helix, Threads & Emboss
- Validator & CI
  - Validate IR: `make validate-v12`
  - CI badge in README; GitHub Actions validates examples on push/PR
- Conformance harness
  - Added v1.2 cases (holes, sweep, face ops, sheet, emboss/project) and reports under `out/`

## Notable v1.2 Additions
- Sketch: `spline`, `ellipse`, `elliptical_arc`, `text`
- Loft: `continuity G0|G1|G2`, `orientation`, rails/centerline, per‑section continuity
- Sweep: `orientation`, `twist`, `scale`, optional guide rail
- Fillet/Chamfer: per‑edge variable groups; transitions/setbacks (best‑effort)
- Draft: explicit faces + neutral plane + angle; optional pull direction
- Wrap/Emboss/Project: depth/draft/direction; source sketch/text; method hints
- Threads: designations/classes/handedness; modeled vs cosmetic
- Queries: `created_by`, `owner_feature==`, `pattern_instances`, `tangent_connected`, `largest_by`, `curvature≈/radius≈/area≈`, `by_material`
- Assemblies/Joints: limits `{linear, angular}`, damping, preload
- Sheet metal: base/edge flange/bend; `unfold`/`refold` (best‑effort)
- Helix curve; light PMI notes/frames

## Fusion Backend Status
- v1.2 schema fields map to implemented features (see `triple_lindy/transpilers/fusion360_backend.py`). Some fidelity remains API/version‑dependent (e.g., loft G2/orientation, advanced fillet transitions, geodesic wrap).

## Upgrade
- Existing v1.1 IR remains valid. Adopt v1.2 fields as needed; gate advanced features with capability checks.

## Thanks
- Contributors and early users helping drive parity and determinism.
