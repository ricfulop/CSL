# CSL – Current Handoff Summary

## Repo & Auth
- Repo: `/Users/ricfulop/CSL/CSL`
- 3‑legged token: `out/token_3l.json` (refresh logic wired)
- Env needed for Automation: `APS_CLIENT_ID`, `APS_CLIENT_SECRET`, `FUSION_PAT`

## Automation (Autodesk Automation API v3 ScriptJob)
- Submit:
  - `make fusion-auto-hello`
  - `make fusion-auto-hello-msg MSG="adsk.log('hi')"`
  - `make fusion-auto-unfold-test`
  - `make fusion-auto-fillet-test`
  - `make fusion-auto-chamfer-test`
  - `make fusion-auto-loft-test`
  - `make fusion-auto-sweep-test`
- Status/logs:
  - `make fusion-auto-status`
  - `make fusion-auto-status-logs` (saves `out/fusion_auto_report.txt`)

## Coverage
- Current weighted coverage: 86.45%
- Recompute badge: `make fusion-cov`
- Coverage doc: `FUSION_FEATURE_COVERAGE.md` (badge and sections updated)

## Implemented (marked Done in coverage)
- Sketch entities
- Sketch constraints/dimensions (G2 best‑effort with tangent fallback)
- Extrude
- Thin Extrude (side/dual‑wall/to‑face/through‑all)
- Rib
- Revolve
- Sweep (orientation/rail/twist/scale)
- Shell
- Draft
- Fillet (variable/setbacks, corner types, chordal)
- Chamfer (equal/two‑distance/distance+angle)
- Patterns (rectangular/circular/path, symmetry, align‑to‑path, per‑instance)
- Surface Ops (patch/extend/trim/knit)
- Sheet Metal (base, edge flange attempt, native bend with relief, unfold/refold)
- Materials/PMI (targeted bodies, PMI/GD&T frames on faces/planes)

## In Progress / Remaining (to 100%)
- Selection/Queries: expand operators, determinism, cross‑session IDs (next)
- Threads: finalize designation/class/handedness and selection across all cylindrical faces
- Wrap/Emboss/Project: deepen depth/draft/direction parity and fallbacks
- Loft: finalize per‑section continuity/orientation/rails across versions
- Export: true AP242 embedding; 3MF parity across Fusion versions

## Key Files
- Backend: `triple_lindy/transpilers/fusion360_backend.py`
- Automation:
  - `scripts/fusion_auto_submit.py`, `scripts/fusion_auto_status.py`
  - `scripts/fusion_auto_hello.ts`, `scripts/fusion_auto_unfold_test.ts`
  - `scripts/fusion_auto_fillet_test.ts`, `scripts/fusion_auto_chamfer_test.ts`
  - `scripts/fusion_auto_loft_test.ts`, `scripts/fusion_auto_sweep_test.ts`
- Makefile: automation and coverage targets
- Coverage script: `scripts/compute_fusion_coverage.py` (weighted, updates badge)

## Quick Commands
- Export env and run a sample job:
  - `export APS_CLIENT_ID='…'`
  - `export APS_CLIENT_SECRET='…'`
  - `export FUSION_PAT='…'`
  - `make fusion-auto-hello`
  - `make fusion-auto-status`
- Recompute coverage:
  - `make fusion-cov`

## Suggested Next Steps
1) Implement Selection/Queries to Done
2) Complete Threads
3) Improve Wrap/Emboss/Project
4) Recompute coverage and iterate
