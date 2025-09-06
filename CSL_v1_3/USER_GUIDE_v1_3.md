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


