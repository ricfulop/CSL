# CSL (CAD-Specific Language) – Version 1.2
**Date:** 2025-09-06  
**Status:** Draft (candidate for Final)

CSL v1.2 advances v1.1 with richer sketch entities, higher‑fidelity loft/sweep controls, variable fillet/chamfer, explicit draft controls, wrap/emboss/project, thread designations, expanded selection predicates, and enhanced joints. It remains deterministic, portable, and LLM‑friendly, with a canonical JSON IR.

---

## 0) Goals & Scope (changes vs 1.1)
- Add spline, text, ellipse, and elliptical arc to sketch entities.
- Add loft continuity G0/G1/G2 and orientation controls; rails/centerline.
- Add variable fillet/chamfer definitions with per‑edge groups and setbacks.
- Add draft with explicit neutral plane and face sets.
- Add wrap/emboss/project with depth/draft/direction.
- Add thread designations (ISO/UNC/UNF/NPT), classes, handedness; modeled vs cosmetic.
- Expand selection predicates: created_by, owner_feature==, pattern_instances, tangent_connected(tol), curvature≈/radius≈/area≈, by_material.
- Enhance joints with limits {linear/angular}, damping, preload.

Out of scope (1.2): full CAM toolpaths, Class‑A surfacing beyond continuity controls, full PMI standardization (kept light).

---

## 1) Header & Metadata
```csl
csl 1.2
name "Sample Part"
author ""
units mm
backend { targets ["fusion","onshape","freecad","solidworks","blender"] }
```

---

## 2) Sketches (additions)
- Entities: `spline`, `ellipse`, `elliptical_arc`, `text`.
- Constraints: add curvature continuity and richer driven/reference dimensioning.

Example:
```csl
sketch s0 on world.xy {
  spline id:sp1 through [(0,0), (20,10), (40,0)] degree 3
  text id:tx at (10, -5) height 5 mm content "M6" font "Arial"
}
```

---

## 3) Features (additions)
- Loft: `continuity G0|G1|G2`, optional `orientation frenet|fixed_normal|binormal`, `rail`, `centerline`, per‑section continuity via `sections_continuity`.
- Sweep: orientation/rail and twist/scale best‑effort where supported.
- Fillet: `edges:[{q, radius|r1..rn}]`, `transitions:setback` (when available).
- Chamfer: equal/two‑distance/distance+angle per‑edge groups.
- Draft: `faces:Q`, `neutral_plane:Ref`, `angle: expr`, `pull_dir: Vector`.
- Wrap/Emboss/Project: `emboss { onto:face, depth, draft, direction }`, `project { along: dir }`.
- Thread: `{ designation, class, pitch, handedness, modeled|cosmetic }`.
- Patterns: table‑driven per‑instance transforms when exposed.

---

## 4) Selection & Queries (expanded)
Predicates include: `created_by`, `owner_feature==`, `pattern_instances`, `tangent_connected(seed, tol_deg)`, `largest_by(axis)`, `curvature≈`/`radius≈`/`area≈` with `tol`, `by_material`. Ambiguity policy unchanged: ambiguous queries fail with diagnostics.

---

## 5) Assemblies & Joints (enhanced)
Joints accept `limits { linear:{min,max}, angular:{min,max} }`, `damping`, and `preload` when supported; otherwise adapters emit diagnostics.

---

## 6) Export & Thumbnail
Unchanged from 1.1; AP242 sidecar metadata recommended when available.

---

## 7) Minimal Grammar (delta only)
```text
SketchEnt   := spline | ellipse | elliptical_arc | text | …
Loft        := 'feature' 'loft' Id Sections Guides? Rail? Centerline?
               ('continuity' ('G0'|'G1'|'G2'))?
               ('orientation' ('frenet'|'fixed_normal'|'binormal'))?
Fillet      := 'feature' 'fillet' Id '{' EdgeGroup+ ('transitions' 'setback')? '}'
Chamfer     := 'feature' 'chamfer' Id '{' EdgeGroup+ '}'
Draft       := 'feature' 'draft' Id '{' 'faces':Q 'neutral_plane':Ref 'angle':Expr ('pull_dir':Vec)? '}'
Emboss      := 'feature' 'emboss' Id '{' 'onto':Face 'depth':Expr ('draft':Expr)? ('direction':Vec)? '}'
Thread      := 'feature' 'thread' Id '{' 'designation':Str ('class':Str)? ('pitch':Expr)? ('mode':'modeled'|'cosmetic') '}'
Joint       := 'joint' Id '{' Kind Refs ('limits':{...})? ('damping':Expr)? ('preload':Expr)? '}'
```

---

## 8) Canonical JSON IR (excerpt)
```json
{
  "csl": "1.2",
  "meta": {"name": "Sample Part", "units": "mm"},
  "sketches": [
    {"id":"s0","plane":"world.xy","entities":[
      {"kind":"spline","id":"sp1","through":["0,0","20,10","40,0"],"degree":3}
    ]}
  ],
  "features": [
    {"kind":"loft","id":"L","sections":["s0.profile(sp1)","s1.profile(r1)"],"continuity":"G2","orientation":"frenet","result":"body"},
    {"kind":"fillet","id":"F","edges":[{"q":"query.created_by('cut1')","r":["2 mm","5 mm"]}],"transitions":"setback"},
    {"kind":"draft","id":"D","faces":"query.by_material('6061-T6')","neutral_plane":"world.xy","angle":"3 deg"}
  ],
  "materials": [{"target":"part","name":"6061-T6"}],
  "export": [{"id":"step_out","format":"STEP","path":"out/part.step","target":"part"}]
}
```

---

## 9) Capabilities & Determinism
Same contract as v1.1. Adapters publish `get_capabilities()`; conditional execution encouraged via `backend.require/prefer` and `if backend.supports…` blocks.

---

## 10) Version History
- v1.2 (2025-09-06): Adds sketch entities (spline/text/ellipse/elliptical_arc), loft continuity/orientation, variable fillet/chamfer, draft controls, wrap/emboss/project, thread designations/classes, expanded selection predicates, and enhanced joint options.


