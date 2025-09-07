## CSL v1.3 User Guide (Draft)

New in v1.3:
- Surface operations: `patch`, `extend`, `trim`, `knit`
- Patterns per‑instance controls via `instances`
- Constraints: construction toggles, reference (driven) dimensions, equal‑length arrays
- Loft continuity/orientation options
- STL tessellation controls

Example (patterns per‑instance):
```
feature pattern pat_instances kind linear seed query.body(part)
  instances [ { dx 0 mm dy 0 mm dz 0 mm angle 0 axis Z count 1 },
              { dx 18 mm dy 6 mm dz 0 mm angle 10 axis Z count 1 } ]
```


Quick examples by feature

1) Surface operations
```
// Start from a thin plate
sketch s on world.xy { rect id:plate p1 (0,0) p2 (40 mm, 20 mm) }
feature extrude e profile plate distance 2 mm op new_solid result part

// Patch: fill boundary (best‑effort)
feature patch p1 edges_query { kind:edge, created_by:e }

// Extend: grow selected faces by distance and optional side
feature extend ex1 faces_query { kind:face, created_by:e } distance 1.0 mm side both

// Trim: remove with tool/plane queries
feature trim t1 target_query { kind:face, created_by:e } keep false

// Knit: attempt to merge faces/surfaces; to_solid optional
feature knit k1 faces_query { kind:face, created_by:e } tolerance 0.1 mm to_solid false
```

2) Patterns: per‑instance controls
```
// Seed body
sketch s on world.xy { rect id:seed p1 (0,0) p2 (8 mm, 8 mm) }
feature extrude e profile seed distance 3 mm op new_solid result part

// Table of instances with per‑occ translation and rotation
feature pattern pat_instances kind linear seed query.body(part)
  instances [
    { dx 0 mm dy 0 mm dz 0 mm angle 0 axis Z count 1 },
    { dx 15 mm dy 5 mm dz 0 mm angle 15 axis Z count 1 }
  ]
```

3) Constraints updates
```
// Construction toggles & driven/reference dimensions
sketch s on world.xy {
  line id:l1 p1 (0,0) p2 (20 mm,0)
  line id:l2 p1 (0,5 mm) p2 (20 mm,5 mm) construction
  point id:pt at (10 mm, 10 mm) construction
  // Equal‑length array
  constraint equal_length items [l1, l2]
  // Reference distance dimension
  dim distance a pt b l1 value 10 mm reference true
}
```

4) Loft continuity/orientation
```
sketch s0 on world.xy { circle id:c0 center (0,0) d 20 mm }
sketch s1 on world.xz { rect id:r1 p1 (-6 mm,-3 mm) p2 (6 mm,3 mm) }
sketch rail on world.yz { spline id:path points [(0,0), (12 mm,6 mm), (24 mm,0)] }

feature loft L sections [ s0.profile(c0), s1.profile(r1) ]
  continuity G2 orientation binormal rail rail.profile(path) result body
```

5) Export STL tessellation controls
```
export stl format STL path "out/mesh_high.stl" units mm resolution high
  deviation 0.05 mm normal_deviation_deg 5 aspect_ratio 6.0 max_edge 1.0 mm
```

Notes
- v1.3 is fully backward‑compatible with v1.2; all new fields are optional.
- Adapters may emit diagnostics (E23xx/E30xx) when an option is not supported; flows should continue with best‑effort behavior.


