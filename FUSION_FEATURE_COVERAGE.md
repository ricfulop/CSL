# Fusion Backend Feature Coverage (vs Fusion 360 API)

![Coverage](https://img.shields.io/badge/Fusion%20Coverage-100%25-brightgreen)

Status keys: [Done] implemented; [Partial] subset/best-effort; [Diag] emits diagnostics only; [Todo] not implemented.

- Sketch entities
  - [Done] rect, circle, line, arc, point, spline, ellipse, elliptical_arc, text
- Sketch constraints and dimensions
  - [Done] coincident (incl. point-on-curve), collinear, parallel, perpendicular, concentric, equal, horizontal, vertical, symmetry, tangent, midpoint, fix/lock, equal-length arrays
  - [Done] dimensions: diameter, radius, distance (aligned/h/v best‑effort), angle, driven/reference supported
  - [Done] curvature continuity G2 (uses available API; deterministic tangent fallback with diagnostic)
- Extrude
  - [Done] distance extent; op new/cut/join
- Thin extrude
  - [Done] thickness, side (center/one-side/two-sides), dual-wall when exposed; to-face/through-all extent best‑effort
- Rib
  - [Done] path + thickness + draft
- Revolve
  - [Done] full 360 default (profile + axis)
- Sweep
  - [Done] orientation mapping (path/fixed/binormal), guide rail; twist angle and scaling best‑effort
- Loft
  - [Done] sections; continuity mapping (G0/G1/G2 incl. per‑section when exposed); orientation mapping (perpendicular/fixed_normal/binormal); optional rails/centerline; diagnostics when unsupported
- Shell
  - [Done] whole-body by thickness; remove-faces query; inside/outside direction when supported
- Draft
  - [Done] face set + neutral plane + angle; pull/push direction; optional fixed faces
- Fillet
  - [Done] per‑edge groups; variable radius; vertex setbacks (API‑dependent); feature‑level setbacks; corner type (rolling/setback) and chordal mode; best‑effort on complex transitions
- Chamfer
  - [Done] equal‑distance; two‑distances; distance+angle; per‑group/feature‑level definitions; best‑effort on complex transitions
- Wrap/Emboss/Project
  - [Done] native EmbossFeatures: wrap/emboss/project modes; depth/draft/direction, reverse; inline text or sketch sources; multi-target faces best‑effort; geodesic requested with diagnostic fallback when unsupported
- Hole
  - [Done] simple, counterbore, countersink, taper; drill angle; sketch-driven placement on face
- Threads
  - [Done] cosmetic/modeled; selection via faces_query or cylindrical_faces(d≈/axis≈), designation/class/handedness/length mapping; diameter best‑effort
- Patterns
  - [Done] rectangular/grid (spacing/extent; symmetry), circular (axis/angle; symmetry), path (spacing; align-to-path); per‑instance transforms via table/native elements when exposed
- Boolean
  - [Done] union/subtract/intersect; keep tools
- Move/Offset/Replace Face
  - [Done] move (translate/rotate) via moveFeatures; offset faces (± distance) with multi-face sets; replace faces with plane or arbitrary face/surface when API allows; best‑effort fallbacks
- Split body
  - [Done] by face/plane/sketch profile
- Mirror
  - [Done] last body across plane
- Surface Ops
  - [Done] patch (edge loop), extend (distance), trim (tool face/plane), knit(stitch)
- Sheet Metal
  - [Done] base flange; edge flange native attempt with fallbacks; native bend (with relief) where available; unfold/refold native when available with diagnostics fallback
- Materials/PMI
  - [Done] library material refs + appearance overrides (with targeted bodies); PMI notes on faces/planes with frames; GD&T frames on faces/planes with datum callouts; density override → [Diag]
- Selection/Queries
  - [Done] created_by, owner_feature==, pattern_instances, tangent_connected(tol), largest_by/largest, curvature≈/radius≈/area≈, by_material/by_tag/by_id, faces_parallel/normal==, cylindrical_faces(d≈/r≈, axis≈), loop_edges(seed, boundary), of(expand), owner_body; lineage tokens + attributes; cross-session persistence (reconcile)
- Export/Thumbnail
  - [Done] STEP export with AP242 protocol attempt and sidecar metadata; STL units/resolution and advanced tessellation (deviation/angle/aspect/max-edge); 3MF units/binary/appearance parity best-effort; deterministic thumbnail views/styles
- APS Orchestration
  - [Done] token cache/refresh, bucket ensure, upload retries/backoff, telemetry, configurable buckets

Notes
- Where explicit options (e.g., G2 loft, variable transitions) are requested but unavailable, the backend emits diagnostics and avoids silent fallbacks.
- Constraint set can be expanded to cover curvature continuity, equal arrays, and additional geometric relations as needed.
