## CSL: AI Agent-Driven Meta-Parametric Design for CAD/CAE/CAM and Beyond

![LOC](https://img.shields.io/badge/LOC-30273-blue) ![Python%20LOC](https://img.shields.io/badge/Python%20LOC-15792-blue) ![Docs%20LOC](https://img.shields.io/badge/Docs%20LOC-9671-lightgrey) ![JSON%20LOC](https://img.shields.io/badge/JSON%20LOC-3686-informational) [![Validate CSL IR](https://github.com/ricfulop/CSL/actions/workflows/validate-csl.yml/badge.svg)](https://github.com/ricfulop/CSL/actions/workflows/validate-csl.yml)
### Why
Modern hardware programs span CAD, CAE, CAM, BOM, sourcing, factory automation, and project management. Designs change rapidly; syncing geometry, constraints, analyses, and manufacturing outputs across tools is fragile and manual. CSL exists to make complex, multi-domain engineering agent-friendly, reproducible, and automated.

### What
CSL (CAD-Specific Language) is a compact DSL and JSON IR that describes geometry, constraints, selections, assemblies, and exports in a deterministic, parametric way. It’s designed for AI agents and humans to co-author designs that are portable across backends. The companion “Triple Lindy” agent converts natural language into CSL, plans across backends, and realizes results in target tools.

### Key capabilities
- Meta-parametric design: parameters with units, ranges, and expressions; deterministic evaluation order.
- Robust selections: query by geometry/topology/tags/lineage for stable edits over time.
- Assemblies and joints: mate connectors/LCS, joints; stable instance IDs.
- Export and visualization: STEP/STL/… and thumbnails for downstream workflows.
- Backend capabilities: adapters declare feature support; the agent plans fallbacks.

### Multi-backend
- **Production ready**: 
  - Fusion 360 via Python API with real-time control (v12 - fully functional)
  - FreeCAD via Python API with workbench integration (v1.3 - 100% feature coverage)
- **In development**: Onshape (REST API/FeatureScript)
- **Planned**: SolidWorks (.NET/COM), NX, Blender (Geometry Nodes)
- Adapters publish capabilities so agents can pick the highest-fidelity route with graceful degradation.

### Triple Lindy Real-time Control
- **File-based protocol** for reliable communication with CAD software
- **Universal client** (`file_client.py`) works across all backends
- **Query system** for debugging and state inspection
- **Direct API** and **CSL transpilation** modes
- **No silent failures** - comprehensive error reporting

### Beyond CAD: end-to-end program automation
- CAE: link meshing/solvers and optimization runs to design parameters.
- CAM: export manufacturable geometry with tolerance/finish metadata.
- BOM and sourcing: extract parameters and materials for structured BOM lines.
- Project/PLM: emit milestones, traceability, and build artifacts per revision.
- Factory automation: generate fixtures/tooling geometry and export to downstream.

### Architecture (high level)
- Natural language → Triple Lindy agent → CSL (text) → JSON IR.
- JSON IR → Backend adapter (Fusion/Onshape/SolidWorks/FreeCAD/Blender, etc).
- Adapter executes features, applies selections, exports files and thumbnails.
- Capabilities and diagnostics guide planning, fallbacks, and error reporting.

### Quick start (Fusion 360 with real-time control)
```bash
# 1) Clone
git clone https://github.com/ricfulop/CSL.git
cd CSL

# 2) Install Triple Lindy Fusion add-in (macOS example)
cp -r triple_lindy_fusion_stable "$HOME/Library/Application Support/Autodesk/Autodesk Fusion 360/API/AddIns/"

# 3) In Fusion 360: Scripts & Add-Ins (Shift+S) → Add-Ins tab → Run "triple_lindy_fusion_stable"

# 4) Test real-time control
python3 triple_lindy_daemon/file_client.py ping    # Test connection
python3 triple_lindy_daemon/file_client.py query   # Query current state
python3 triple_lindy_daemon/file_client.py direct  # Create geometry via API

# 5) Execute CSL v1.3 examples
python3 triple_lindy_daemon/file_client.py file --file CSL_v1_2/examples/loft_continuity_demo.json
```

Optional backends
- FreeCAD workbench: copy `triple_lindy/` to `~/.FreeCAD/Mod/` and select “Triple Lindy”.
- Onshape: configure API keys and use FeatureScript/API pipeline.
- SolidWorks: install add-in or IPC shim; Windows host.
- Blender: `bpy`/Geometry Nodes realization; render/export for visualization.

### Language and schema
- Spec (v1.3 Draft): `CSL_v1_3/csl_v1_3_spec.md`
- JSON Schema (v1.3 Draft): `CSL_v1_3/csl_v1_3_schema.json`
- Spec (v1.2 Draft): `CSL_v1_2/csl_v1_2_spec.md` (extends v1.1)
- JSON Schema (v1.2 Draft): `CSL_v1_2/csl_v1_2_schema.json`
- Migration: `MIGRATION_v1_1_to_v1_2.md`
- Conformance checklists: `CSL_v1_1/conformance/README.md`, `CSL_v1_2/conformance/README.md`
- Examples: `CSL_v1_2/examples/` (v1.2) and `CSL_v1_1/examples/` (v1.1)
  - Notable v1.1 example: `constraints_patterns_demo.csl` (construction/driven constraints, per-instance patterns)

### What's new in v1.3
- Surface ops with explicit queries (patch/extend/trim/knit).
- Patterns per‑instance controls (`instances`/`table`).
- Constraints QoL: construction flags, reference (driven) dims, equal‑length arrays, curvature continuity diagnostics.
- Loft: continuity (G0/G1/G2), per‑section continuity, orientation options, rails/centerline.
- Export: STL tessellation controls (deviation, angular tolerance, aspect ratio, max edge length).
- Capabilities: refined JSON and versioned publishing (`make publish-caps`).

### What's new in v1.2
- Sketch: `spline`, `ellipse`, `elliptical_arc`, `text`.
- Loft: continuity G0/G1/G2, orientation controls, rails/centerline.
- Sweep: orientation, twist, scale, optional guide rail.
- Fillet/Chamfer: per‑edge variable groups; transitions/setbacks (best‑effort).
- Draft: explicit `faces`, `neutral_plane`, optional `pull_dir`.
- Wrap/Emboss/Project: depth/draft/direction; project along direction.
- Threads: standardized designations/classes/handedness; modeled vs cosmetic.
- Queries: `created_by`, `owner_feature==`, `pattern_instances`, `tangent_connected`, `largest_by`, `curvature≈/radius≈/area≈`, `by_material`.
- Assemblies & joints: limits `{linear, angular}`, optional damping/preload.
- Sheet metal: base/edge flange/bend; unfold/refold (best‑effort).
- Helix curve generator; light PMI notes/frames.
- Validation: `make validate-v12` checks IR against the v1.2 schema.

### Gap analysis and roadmap
- Backend parity and gaps: `BACKEND_GAP_ANALYSIS.md`.
- Roadmap priorities: Fusion adapter completeness, robust selection predicates, manufacturing exports.

See Production-Grade Closure Plan in `BACKEND_GAP_ANALYSIS.md` for remaining items (native wrap/emboss, cross-session stable IDs, units parity tests, full joints, materials/PMI, APS hardening).

### Conformance harness (Fusion backend)
Run representative cases (loft continuity G1/G2 with rail, variable fillet/chamfer including angle, emboss/native where available, joints with revolute/slider limits) and emit a JSON report.

```bash
python scripts/conformance_harness.py
```

Outputs:
- `out/conformance_report.json`: summary with per-case `ok`, `mapping_size`, and recent diagnostics.
- `out/golden_summary.json`: short summary for CI gates.
- Dry-run friendly: if Fusion API is unavailable, the adapter returns a stable mapping and diagnostics for CI.

### APS (Autodesk Platform Services)
- Auth test:
```bash
export APS_CLIENT_ID=... APS_CLIENT_SECRET=...
make aps-auth
```
- Orchestrate example (local Fusion run + upload when configured):
```bash
make aps-orchestrate-example
```
- Design Automation (DA) stub:
```bash
make aps-da-list-engines
```
Set `APS_SCOPES` and optionally `APS_BUCKET` (defaults to `csl-artifacts-<env>`).

### Export units/parity test
Quickly exercise STL/STEP unit and resolution options.

```bash
python scripts/export_units_test.py
```

### Contributing
- Issues and proposals welcome. For large changes, start with a short design note.
- Adapters should implement a minimal interface and publish capabilities for planning.

#### Getting started for contributors 
1) Create a virtualenv and install dev tools (pytest optional).
2) Review the adapter stub at `triple_lindy/transpilers/fusion360_backend.py`.
3) Run the demo script:
```bash
python scripts/run_fusion_example.py
```
4) Implement real Fusion calls in `FusionBackend.realize/export/thumbnail`.
5) Extend capabilities and add tests that validate exported artifacts.

### License
MIT (see `LICENSE`).

### Project size (LOC)
- Current snapshot (as of 2025-01-13):
  - Total lines: 27,058
  - Python lines: 13,335
  - Markdown/docs lines: 11,726
  - JSON lines: 3,686
  - CSL language files: 301
  - Fusion backend file `triple_lindy/transpilers/fusion360_backend.py`: 5,388

- File counts by type:
  - Python files: 52
  - Markdown files: 44
  - JSON files: 16
  - CSL files: 15
  - TypeScript files: 9
  - Manifest files: 9

- Recompute locally (from repo root):
```bash
# Totals (excluding .git, out, __pycache__)
find . -type f -not -path "./.git/*" -not -path "./out/*" -not -path "*/__pycache__/*" -print0 | xargs -0 wc -l | tail -n1

# By type
find . -type f -name "*.py" -not -path "*/__pycache__/*" -print0 | xargs -0 wc -l | tail -n1
find . -type f -name "*.md" -print0 | xargs -0 wc -l | tail -n1
find . -type f -name "*.json" -print0 | xargs -0 wc -l | tail -n1
find . -type f -name "*.csl" -print0 | xargs -0 wc -l | tail -n1

# Key file
wc -l triple_lindy/transpilers/fusion360_backend.py

# File count by extension
find . -type f -not -path "./.git/*" -not -path "./out/*" -not -path "*/__pycache__/*" | sed 's/.*\.//' | sort | uniq -c | sort -nr
```

### Learn more
- Documentation index: `DOC_INDEX.md`
- CSL Glossary: `CSL_GLOSSARY.md`
- Triple Lindy implementation guide: `triple_lindy_complete with CSL.md`

### Fusion backend status (v1.3)
- Adds: surface ops explicit queries, patterns per‑instance (`instances`/`table`), constraints QoL, loft continuity/orientation/rails, STL controls.
- Continues: v1.2 features (loft, sweep, wrap/emboss/project, threads, face ops, patterns, booleans), robust queries, diagnostics, export/thumbnail.
- Assemblies/joints: creation with limits; best‑effort mate connectors and assembly patterns.
- APS: token/bucket upload helpers and an `orchestrate(plan)` helper for local/hosted agent models.

### Query determinism and tolerances
- Predicates supported: `created_by`/`owner_feature==`, `pattern_instances`, `tangent_connected(seed, tol_deg)`, `largest_by(axis)`, `curvature≈`/`radius≈`/`area≈` with `tol`, `by_material`.
- Tolerances: use absolute tolerances via `tol` (e.g., `tol: 0.1` mm) or `tol_deg` for angular floods; values are unit-checked.
- Determinism policy: ambiguous queries fail with E12xx diagnostics and guidance to strengthen predicates/tags; lineage/attributes are used for stable reconciliation across sessions.

## Automation

- Golden check: `make golden-check`
- Dump capabilities: `make caps` (writes `out/capabilities_fusion.json` with version/commit and determinism metadata)
 - Publish/Archive capabilities: `make publish-caps` (writes versioned archive under `out/capabilities/archive/<version>/`)
- APS Design Automation helpers:
  - List engines: `make aps-da-list-engines` (requires `APS_CLIENT_ID`/`APS_CLIENT_SECRET`)
  - Bootstrap check: `make aps-da-bootstrap`
  - Create AppBundle: `make aps-da-create-appbundle NAME=<name> ENGINE=<engineId> ZIP=<path.zip>`
  - Create Activity: `make aps-da-create-activity NAME=<name> ENGINE=<engineId> APPBUNDLE=<bundleId>`
  - Submit WorkItem: `make aps-da-submit-workitem ACTIVITY=<activityId> ARGS=<args.json>`
  - Clean: `make aps-da-clean`
  - DA pipeline: `make aps-da-pipeline` (ensure + submit; see env below)

### Environment

- Optional env for metadata: `CSL_VERSION`, `GIT_COMMIT`/`CI_COMMIT_SHA`, `FUSION_BUILD`
- APS DA env: `APS_ENGINE`, `APS_BUNDLE_ZIP`, optional `APS_BUNDLE_NAME`, `APS_ACTIVITY_NAME`, `APS_INPUT_URL`, `APS_OUTPUT_URL`
