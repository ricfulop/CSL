# Fusion Backend Feature Coverage (vs Fusion 360 API)

Status keys: [Done] implemented; [Partial] subset/best-effort; [Diag] emits diagnostics only; [Todo] not implemented.

- Sketch entities
  - [Done] rect, circle, line, arc, point, spline, ellipse, elliptical_arc, text
- Sketch constraints and dimensions
  - [Partial] coincident (incl. coincident-to-spline), collinear, parallel, perpendicular, concentric, equal, horizontal, vertical, symmetry, tangent, midpoint, fix/lock, equal-length arrays
  - [Partial] dimensions: diameter, radius, distance, angle (values applied; driven/reference supported best-effort)
  - [Diag] curvature continuity (emits diagnostic when unsupported)
- Extrude
  - [Done] distance extent; op new/cut/join
- Thin extrude
  - [Partial] thickness, side (best-effort mapping)
- Rib
  - [Done] path + thickness + draft
- Revolve
  - [Done] full 360 default (profile + axis)
- Sweep
  - [Partial] orientation hints; optional guide rail
- Loft
  - [Partial] sections; continuity mapping (G1/G2 via enums) best-effort; orientation hints; optional rails/centerline; [Diag] when unsupported
- Shell
  - [Partial] whole-body inward by thickness
- Draft
  - [Partial] face set + neutral plane + angle; pull direction fixed
- Fillet
  - [Partial] per-edge groups; variable radius; vertex setbacks (API-dependent); transitions → [Diag]
- Chamfer
  - [Partial] equal-distance; points variant; angle+distance variant (best-effort); transitions/setbacks → [Diag]
- Wrap/Emboss/Project
  - [Partial] native EmbossFeatures when available; otherwise [Diag]
- Hole
  - [Done] simple, counterbore, countersink, taper; drill angle; sketch-driven placement on face
- Threads
  - [Partial] cosmetic/modeled; designation/class/handedness mapping; selection simplified to last-body cylindrical faces
- Patterns
  - [Partial] rectangular/grid, circular, path; per-instance via `instances`/`table` (fallback) and native element transforms when exposed
- Boolean
  - [Done] union/subtract/intersect; keep tools
- Move/Offset/Replace Face
  - [Partial] offset faces; replace with plane proxy
- Split body
  - [Done] by face/plane/sketch profile
- Mirror
  - [Done] last body across plane
- Materials/PMI
  - [Partial] library material refs + appearance overrides; PMI notes on faces/planes with height/angle/pos; density override → [Diag]
- Selection/Queries
  - [Partial] created_by, owner_feature==, pattern_instances, tangent_connected(tol), largest_by, curvature≈/radius≈/area≈, by_material; lineage tags; cross-session persistence (basic)
- Export/Thumbnail
  - [Partial] STEP/STL with resolution/units best-effort; STL advanced tessellation (deviation/angle/aspect/max-edge); deterministic thumbnail views/styles
- APS Orchestration
  - [Done] token cache/refresh, bucket ensure, upload retries/backoff, telemetry, configurable buckets

Notes
- Where explicit options (e.g., G2 loft, variable transitions) are requested but unavailable, the backend emits diagnostics and avoids silent fallbacks.
- Constraint set can be expanded to cover curvature continuity, equal arrays, and additional geometric relations as needed.
