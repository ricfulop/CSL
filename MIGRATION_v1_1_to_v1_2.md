## CSL Migration: v1.1 → v1.2

### Summary
- v1.2 extends v1.1; existing v1.1 IR remains valid. Adopt new fields for higher fidelity when available.

### Additions
- Sketch: `spline`, `text`, `ellipse`, `elliptical_arc` entities.
- Loft: `continuity` (G0/G1/G2), `orientation` (frenet/fixed_normal/binormal), optional `rail`/`centerline` and `sections_continuity`.
- Fillet/Chamfer: per‑edge groups; `transitions: setback` (when supported).
- Draft: `faces`, `neutral_plane`, `angle`, optional `pull_dir`.
- Wrap/Emboss/Project: `emboss { onto, depth, draft?, direction? }`.
- Thread: `designation`, `class`, `pitch`, `handedness`, `mode` (modeled|cosmetic).
- Selection predicates: `created_by`, `owner_feature==`, `pattern_instances`, `tangent_connected`, `curvature≈`/`radius≈`/`area≈`, `by_material`.
- Joints: `limits { linear, angular }`, `damping`, `preload`.

### Examples
Loft v1.1 → v1.2 (continuity/orientation):
```json
{
  "kind": "loft",
  "id": "L",
  "sections": ["s0.profile(c0)", "s1.profile(r1)"],
  "continuity": "G2",
  "orientation": "frenet",
  "result": "body"
}
```

Variable fillet groups:
```json
{
  "kind": "fillet",
  "edges": [
    {"q": "query.created_by('edge_set')", "r": ["2 mm", "5 mm"]}
  ],
  "transitions": "setback"
}
```

Thread designation vs cosmetic:
```json
{"kind":"thread","designation":"ISO M6x1","class":"6H","pitch":"1 mm","handedness":"right","mode":"cosmetic"}
```

### Capability‑driven adoption
Wrap new fields in capability checks or allow adapters to emit diagnostics when unsupported. Prefer conditional execution where workflows require strict fidelity.


