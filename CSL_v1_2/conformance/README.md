# CSL v1.2 Conformance Checklist

This checklist covers incremental items beyond v1.1. Adapters should publish capabilities and produce diagnostics for unsupported items.

## Sketch
- [ ] Spline entity with degree; interpolation of control points
- [ ] Ellipse and elliptical arc
- [ ] Text entity with font/height

## Loft/Sweep
- [ ] Loft continuity: G0/G1/G2
- [ ] Loft orientation: frenet/fixed_normal/binormal
- [ ] Rails and centerline support (best‑effort)

## Fillet/Chamfer
- [ ] Per‑edge groups and variable radii/distances
- [ ] Transitions: setback/rolling mapping (diagnostics if unavailable)

## Draft
- [ ] Faces selection + neutral plane + angle
- [ ] Pull direction where supported

## Wrap/Emboss/Project
- [ ] Emboss onto face (depth/draft/direction)
- [ ] Project along direction

## Thread
- [ ] Designation/class/pitch/handedness mapping
- [ ] Cosmetic vs modeled threads

## Patterns
- [ ] Table‑driven patterns (per‑instance transforms)

## Selection/Queries
- [ ] created_by, owner_feature==, pattern_instances
- [ ] tangent_connected with tolerance
- [ ] curvature≈/radius≈/area≈ with tolerance
- [ ] by_material

## Assemblies/Joints
- [ ] Limits {linear/angular}
- [ ] Damping and preload (diagnostics if not available)

## Export/Thumbnail
- [ ] AP242 sidecar metadata where available

## Determinism & Diagnostics
- [ ] Ambiguous queries fail with E12xx diagnostics
- [ ] Capabilities published; conditional execution pathways validated


