# CSL (CAD-Specific Language) – **Version 1.1**
**Date:** 2025-01-01  
**Status:** Final  
**Changes from 1.0:** Added export/thumbnail operations (§6.1), backend capabilities (§16)

*A compact, portable DSL for describing CAD geometry, constraints, and assemblies across tools (Onshape, Fusion, FreeCAD, Blender), with optional ECAD extensions for KiCad.*

---

## 0) Goals & Scope
- **Portable**: One source, many backends (Onshape FeatureScript, Autodesk Fusion/Inventor API, FreeCAD, Blender).  
- **Declarative-first**: Describe *what* (geometry + constraints), not *how* (imperative UI sequences).  
- **Parametric**: Every numeric can be a parameter with units or expressions.  
- **Deterministic**: Explicit references + stable IDs to avoid feature-tree drift.  
- **LLM-friendly**: Minimal syntax; machine-parseable; canonical JSON IR.  
- **Composable**: Parts → subassemblies → assemblies; reusable macros.  
- **Secure & Reproducible**: Pinned imports, deterministic evaluation order.

Out of scope (1.1): full FEA, CAM toolpaths, freeform Class-A surfacing.
We provide hooks to link downstream tools.

---

## 1) File Header & Metadata
```csl
csl 1.1
name "Parametric L-Bracket"
author "Ric Fulop"
units mm
backend { targets ["onshape","fusion","freecad","blender"] }
```
- `csl` version locks grammar (1.1 adds export/thumbnail ops).  
- `units` sets file default (overridable per value).  
- `backend.targets` is advisory; compilers may ignore.

---

## 2) Core Concepts
- **Parameters**: typed scalars with units and ranges.  
- **Sketches**: 2D construction on planes; constraints + dimensions (driving/reference).  
- **Features**: solid ops (extrude, loft, sweep, fillet, chamfer, shell, draft, face ops, hole, thread, rib, wrap, thin).  
- **Selections/Queries**: robust entity selection by tags, topology, lineage, and geometry.  
- **References**: every entity has a **stable ID**; tags are user aliases.  
- **Assemblies**: instances of parts, mate connectors/LCS, joints.  
- **Materials/Props**: assign materials, density, color, metadata.  
- **Export/Thumbnail** (new in 1.1): output operations for files and visualization.
- **ECAD (optional)**: board outline, stackup, components, placement, routing hints for KiCad.  

---

## 3) Parameters & Expressions
```csl
param thickness: length = 6 mm  in [3 mm, 12 mm]
param legA: length = 80 mm
param legB: length = 60 mm
param rib:  length = thickness * 0.75
param hole_d: length = 6.5 mm
param fil_r: length = 3 mm
```
- Types: `length`, `angle`, `count`, `bool`, `real`.  
- Units: `mm, in, deg, rad, %` (dimension-checked).  
- Expressions: + − * /, min/max, trig; cross-unit checks enforced.

---

## 4) Coordinate Frames & Planes
```csl
frame world        // implicit: origin, X,Y,Z
plane base = plane.world.xy
plane up    = plane.offset(base, by: thickness)
```
Built-ins: `plane.world.xy|xz|yz`, `plane.offset`, `plane.through(point, normal)`.

---

## 5) Sketches, Construction, Constraints, Dimensions
```csl
sketch s_base on base {
  rect id:plate from (0,0) to (legA, legB)
  circle id:mount1 at (15 mm, 15 mm) d: hole_d
  circle id:mount2 at (legA-15 mm, 15 mm) d: hole_d
  circle id:boss   at (legA/2, legB/2) d: 12 mm construction

  dim horizontal name:"legA_dim" driving between plate.minX and plate.maxX = legA
  dim vertical   name:"legB_dim" driving between plate.minY and plate.maxY = legB
  dim diameter   name:"bossD"    reference on boss = 12 mm
}

sketch s_proj on plane.offset(base, by: 10 mm) {
  project from sketch s_base entities [plate] as ext_plate
  region id:slot = s_base.profile("plate") - circle((15 mm,15 mm), d:10 mm)
}
```
**Primitives**: `point`, `line`, `arc`, `circle`, `rect`, `slot`, `polyline`  
**Constraints**: coincident, colinear, parallel, perpendicular, concentric, equal, horizontal, vertical, symmetric, tangent, midpoint, lock/fix, distance, angle.  
**Dimensions**: **driving** or **reference**, with optional `name` for reuse.  
**Construction geometry**: mark with `construction` (ignored by area-filling profiles).

---

## 6) Features (3D Ops)

### 6.1 Export & Visualization Operations (New in v1.1)

```csl
// Export operations
export step_out format STEP path "out/bracket.step" target part
export stl_out format STL path "out/bracket.stl" target part resolution fine

// Thumbnail operations  
thumbnail preview path "out/preview.png" width 1024 height 768 view iso style shaded
thumbnail ortho_views {
  path "out/top.png" view top
  path "out/front.png" view front  
  path "out/right.png" view right
}
```

**Export formats**: `STEP`, `STL`, `IGES`, `SAT`, `BREP`, `3MF`, `OBJ`  
**Export options**:
- `target`: feature ID or "all" (default)
- `resolution`: for mesh formats (`coarse|medium|fine|adaptive`)
- `units`: override file units for export
- `version`: format version if applicable

**Thumbnail options**:
- `view`: `iso|top|bottom|front|back|left|right|custom(eye,target,up)`
- `style`: `shaded|wireframe|hidden|rendered`
- `background`: color or `transparent`
- `width/height`: pixels (default 512×384)

### 6.2 Geometry Features (Original)

```csl
feature extrude main from sketch s_base.profile("plate - mount1 - mount2") 
  distance thickness operation new_solid id:part

feature fillet edges of query.edges(part) where tag=="external" radius fil_r

feature hole h on face query.face(part, normal==+Z)
  at points [(15 mm, 15 mm), (legA-15 mm, 15 mm)]
  type countersink d: hole_d cs_d: 10.5 mm cs_angle: 90 deg depth through_all

feature thread t on faces query.cylindrical_faces(part, d≈6 mm±0.5 mm, axis≈Z)
  mode cosmetic designation "M6x1-6H" handed right length 12 mm start chamfer

feature draft d on faces query.face(part, by_tag:"moldPull")
  pull_dir +Z angle 2 deg references query.edges(part, boundary:true)

feature move_face mf on faces query.face(part, by_tag:"logo") offset 0.5 mm
feature replace_face rf target query.face(part, by_tag:"wall") with offset_surface(sourceFace:+0.8 mm)

feature thin_extrude te from sketch s_base.profile("plate") thickness 2.0 mm side outward
feature rib r path sketch s_base.chain("boss, mount1") thickness 3 mm draft 1 deg

feature loft L sections [skA.profile("a"), skB.profile("b"), skC.profile("c")]
  guides [skG.curve("rail1"), skG.curve("rail2")] continuity G1

feature wrap w curves sketch logo.entities onto face query.face(part, convex:true) method geodesic
```

**Extrude modes**: `distance`, `to_next`, `to_object`, `through_all`.  
**Operations**: `new_solid`, `add`, `cut`, `intersect`.  
**Other features**: `revolve`, `sweep`, `loft`, `shell`, `draft`, `move_face`, `offset_face`, `replace_face`, `thin_extrude`, `rib`, `wrap`, `split`, `mirror`, `pattern(linear|circular|grid|path)`, `boolean(union|subtract|intersect)`, `helix` (curve generator).

---

## 7) Selection & Query Language
Robust selection is key to parametric stability.

```csl
let front      = query.face(part, normal==+Z, largest:true)
let bolt_holes = query.cylindrical_faces(part, d≈hole_d ±0.1 mm, axis≈Z)
let outer_edges= query.loop_edges(seed:front, boundary:true) tag "external"

// Lineage, ownership, tangent floods, patterns
let createdByX = query.created_by(id:"main", type:FACE)
let owner_body = query.owner_body(createdByX)
let tFaces     = query.tangent_connected_faces(seed:front, tol:5 deg)
let pattern_i  = query.pattern_instances(feature:"pat1", index:5, type:EDGE)

// Geometric predicates
let parallelZ  = query.faces_parallel(direction:+Z)
let containsPt = query.contains(point:(10,10,0)) in part
```
**Predicates**: `area>, area<, radius≈, normal==, boundary, convex, concave, planar, cylindrical, by_tag, by_id, parallel, contains, intersects`.  
**Tolerance**: `≈` supports absolute or relative.  
`tag` attaches stable labels for later use.

---

## 8) Materials & Properties
```csl
material part = { name:"6061-T6", density: 2.70 g/cm^3, color: #a8c0ff }
properties part = { 
  finish:"anodized clear", 
  tolerance_class:"ISO 2768-mK",
  drawing:"LBracket_A.dwg"
}
```

---

## 9) Assemblies, Mate Connectors & Joints
```csl
datum mcA = mate_connector at part.face(by_tag:"front") origin (10,0,0) axes (X:+X, Z:+Z)

partdef bracket from this_file id:part
partdef bolt6  from lib:fasteners/ISO4762_M6x16

assembly a1 {
  instance b1 of bracket at mcA
  instance s1 of bolt6   at mate_connector on b1.face(by_tag:"hole1")
  mate fasten b1.face(by_tag:"front") to s1.head.face(normal==−Z)
  // Optional capability (if supported): helical/screw/gear/rack joints
}
```
**Joints**: `rigid|revolute|slider|ball|planar|fasten` (core). Optional: `cylindrical|screw|gear|rack` gated by adapter capability flags.

---

## 10) ECAD Extension Block (Optional; KiCad)
```csl
ecad {
  library libs = ["${KICAD6_SYMBOL_DIR}", "my_company_symbols"]
  netlist {
    comp U1 type:"MCU" footprint:"Package_QFP:TQFP-64_10x10mm_P0.5mm" nets:{ VDD:"3V3", GND:"GND" }
    comp J1 type:"USB-C" footprint:"Connector_USB:USB_C_Receptacle" nets:{ VBUS:"5V", GND:"GND" }
  }
  board {
    outline from_sketch: s_base.profile("plate")
    stackup: 4_layer(impedance:"50 ohm microstrip")
    drc: { min_trace: 4 mil, min_space: 4 mil, via_drill: 0.2 mm }
    keepout id:ko1 region: circle( center:(50 mm,30 mm), d:20 mm) layers:["F.Cu","B.Cu"]
  }
  placement {
    place U1 at (50 mm, 30 mm) rot 0 side "Top"
    place J1 at (5 mm, 30 mm) rot 90 side "Top"
  }
  routing_hints {
    diffpair: { J1.DP <-> U1.USB_DP, J1.DM <-> U1.USB_DM, target_impedance: 90 ohm }
    match_length: [ "U1.SDCLK", "U1.SD_CMD", "U1.SD_D0..3" ] tolerance:0.5 mm
  }
}
```

---

## 11) Backend Adapter Hints
```csl
backend.blender {
  prefer geometry_nodes for [extrude, boolean, array]
  map feature.fillet -> modifier.Bevel { width: fil_r }
  map feature.thin_extrude -> modifier.Solidify { thickness: t }
  map feature.revolve -> modifier.Screw { angle: theta }
}
```
Adapters may ignore hints; they exist to improve fidelity and editability.

---

## 12) Errors, Determinism, & IDs
- All user-visible entities have IDs; adapters must preserve or stably map them.  
- Ambiguous selections must fail with a diagnostic suggesting stronger predicates/tags.  
- Deterministic evaluation order: **params → planes → sketches → features → assemblies → export → thumbnail → ecad**.  
- **Identity control**: any feature can declare `controls_identity_by: <query>` to stabilize selection under regeneration.

**Diagnostics examples**
```
E1203: query.loop_edges(seed:front) matched 6 loops; expected 1.
Hint: add normal filter (normal==+Z) or tag intended edges earlier.
E2301: boolean subtract produced non-manifold geometry. Adjust tolerances or inputs.
```

---

## 13) Minimal Grammar (EBNF-ish)
```
Program      := Header Decl*
Header       := 'csl' Version NL (Meta NL)*
Meta         := nameDecl | authorDecl | unitsDecl | backendDecl
Decl         := Param | Frame | Plane | Sketch | Feature | Let | Material | Props | Assembly | Import | Macro | Datum | Export | Thumbnail | ECAD
Param        := 'param' Id ':' Type '=' Expr ( 'in' '[' Expr ',' Expr ']' )?
Frame        := 'frame' Id
Plane        := 'plane' Id '=' PlaneExpr
Sketch       := 'sketch' Id 'on' PlaneRef '{' SketchStmt* '}'
Feature      := 'feature' FeatureKind ... ('id:' Id)?
Export       := 'export' Id 'format' Format 'path' Path ('target' Target)? (Options)*
Thumbnail    := 'thumbnail' Id 'path' Path ('view' View)? ('style' Style)? ('width' Int)? ('height' Int)?
Let          := 'let' Id '=' Query
Material     := 'material' Target '=' Obj
Props        := 'properties' Target '=' Obj
Assembly     := 'assembly' Id '{' (Instance|Mate|Let)* '}'
Datum        := 'datum' Id '=' MateConnectorExpr
ECAD         := 'ecad' Obj
Import       := 'import' Source 'as'? Id?
Macro        := 'macro' Id '(' ParamList? ')' '{' Program '}'

Type         := 'length'|'angle'|'count'|'bool'|'real'
Expr         := literals | ids | arithmetic | functions | units
Query        := 'query.' QueryKind '(' Args? ')' Predicates?
Format       := 'STEP'|'STL'|'IGES'|'SAT'|'BREP'|'3MF'|'OBJ'
View         := 'iso'|'top'|'bottom'|'front'|'back'|'left'|'right'
Style        := 'shaded'|'wireframe'|'hidden'|'rendered'
```

A fully formal grammar is available in the JSON Schema annotations.

---

## 14) Canonical JSON IR
Every `.csl` compiles to JSON IR (`.csl.json`) for adapters.

```json
{
  "csl": "1.1",
  "meta": {"name":"Parametric L-Bracket","units":"mm"},
  "params": [
    {"id":"thickness","type":"length","value":"6 mm","range":["3 mm","12 mm"]},
    {"id":"legA","type":"length","value":"80 mm"}
  ],
  "sketches": [
    {"id":"s_base","plane":"world.xy","entities":[
      {"kind":"rect","id":"plate","p1":"0,0","p2":"legA,legB"},
      {"kind":"circle","id":"mount1","center":"15 mm, 15 mm","d":"hole_d"}
    ]}
  ],
  "features": [
    {"kind":"extrude","id":"main","profile":"plate - mount1 - mount2","distance":"thickness","op":"new_solid","result":"part"}
  ],
  "export": [
    {"id":"step_out","format":"STEP","path":"out/bracket.step","target":"part"}
  ],
  "thumbnail": [
    {"id":"preview","path":"out/preview.png","width":1024,"height":768,"view":"iso","style":"shaded"}
  ],
  "materials": [{"target":"part","name":"6061-T6","density":"2.70 g/cm^3"}]
}
```

---

## 15) Cross-Tool Mapping (Adapter Hints)
| CSL concept | Onshape | Fusion 360 | FreeCAD | Blender |
|---|---|---|---|---|
| `param` | FeatureScript vars/queries | User Parameters | Spreadsheet/Expressions | Custom props |
| `sketch` | FS sketch ops | Sketch API | Sketcher WB | GN/BMesh construction |
| `extrude` | `opExtrude` | `createExtrude` | PartDesign Pad | Extrude Mesh/GN |
| `draft/move/replace face` | FS ops | Face ops | Part/PD ops | Modifiers/BMesh |
| `hole/thread` | Hole/Cosmetic threads | Hole/Thread | Hole/helix | Boolean/Screw |
| queries | `qCreatedBy`, etc. | API selectors | Topo naming | Attr groups |
| assemblies | Mate connectors | Joints | LCS/Asm | Empties/constraints |
| **export** | exportAs() | export() | Part.export() | bpy.ops.export |
| **thumbnail** | getImage() | viewport.capture() | saveImage() | render() |

---

## 16) Backend Capabilities (New in v1.1)

Adapters must report their capabilities programmatically to enable graceful degradation and feature discovery.

### 16.1 Capability Structure
```json
{
  "csl": "1.1",
  "backend": "freecad",
  "version": "0.21",
  "supports": {
    "brep": true,
    "mesh": true, 
    "params": true,
    "queries": true,
    
    "features": {
      "extrude": true,
      "revolve": true,
      "sweep": false,
      "loft": true,
      "shell": true,
      "fillet": true,
      "chamfer": true,
      "draft": false,
      "move_face": false,
      "replace_face": false,
      "thin_extrude": true,
      "rib": false,
      "wrap": false,
      "hole": true,
      "thread_cosmetic": true,
      "thread_modeled": false,
      "pattern": ["linear", "circular"],
      "boolean": ["union", "subtract", "intersect"],
      "helix": true
    },
    
    "queries": {
      "boundary": true,
      "cylindrical_faces": true,
      "by_normal": true,
      "largest": true,
      "created_by": false,
      "tangent_connected": false,
      "pattern_instances": false
    },
    
    "assemblies": {
      "enabled": false,
      "joints": []
    },
    
    "export": ["STEP", "STL", "IGES", "BREP"],
    "thumbnail": {
      "enabled": true,
      "views": ["iso", "top", "front", "right"],
      "styles": ["shaded", "wireframe"]
    },
    
    "ecad": false
  }
}
```

### 16.2 Capability Negotiation
```csl
// Query backend capabilities before execution
backend.require features:[fillet, chamfer] queries:[boundary]
backend.prefer features:[loft] fallback:extrude

// Conditional execution based on capabilities
if backend.supports.features.loft {
  feature loft ...
} else {
  feature extrude ...  // fallback
}
```

### 16.3 Adapter Requirements
- Adapters MUST provide a `get_capabilities()` method/endpoint
- Capabilities MUST be queryable before CSL execution
- Unsupported features MUST fail with clear error codes (E3xxx series)
- Partial support (e.g., linear patterns only) MUST be indicated

---

## 17) Security & Reproducibility
- Remote imports are content-addressed and pinned (SHA-256).  
- Required units/tolerances for manufacturable exports.  
- `meta.build` can record kernel and adapter versions, RNG seeds.  
- Sandboxed macro expansion; no network at compile-time unless explicitly enabled.
- Export paths are sanitized; relative paths resolved from document location.

---

## 18) Version History
- **v1.0** (2024-08-30): Initial release
- **v1.1** (2025-01-01): Added export/thumbnail operations, backend capabilities

---

## 18.1) Known Gaps and v1.2 Candidates (non-normative)
- Sketch entities: add `spline (NURBS)`, `text`, `ellipse`, `elliptical_arc`.
- Loft/Sweep fidelity: `continuity: G0|G1|G2`, `orientation: frenet|fixed_normal|binormal`.
- Variable fillet/chamfer: per-edge arrays with transitions/setbacks.
- Draft: `neutral_plane` and explicit `faces` set.
- Threads: ISO + UNC/UNF + NPT designations; cosmetic vs modeled controls.
- Joints: limits `{linear:{min,max}, angular:{min,max}}`, `damping`, `preload`.
- Selector predicates: `created_by`, `owner_feature==`, `pattern_instances`, `tangent_connected`, `curvature≈`.
- Materials/PMI: `material ref` to standardized libraries + overrides; light PMI.

## 19) Quick Reference (Cheatsheet)
- Header: `csl 1.1`, `name`, `units`, `backend { targets [...] }`  
- Param: `param id: type = expr in [min, max]`  
- Plane: `plane id = plane.world.xy | plane.offset(base, by:X)`  
- Sketch: `sketch id on plane { primitives; constraints; dim ... }`  
- Feature: `feature extrude|revolve|sweep|...` with `operation` and `id`  
- Export: `export id format STEP|STL path "file.ext" target part`  
- Thumbnail: `thumbnail id path "preview.png" view iso style shaded`  
- Query: `query.face/edges/... (target, predicates)` then `tag "alias"`  
- Material: `material target = { name:"", density: x }`  
- Assembly: `assembly id { instance; mate; }`  
- ECAD: `ecad { netlist; board; placement; routing_hints }`