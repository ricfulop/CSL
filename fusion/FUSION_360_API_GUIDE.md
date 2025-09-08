# Fusion 360 API Development Guide

## Overview
This guide documents critical knowledge for developing with the Fusion 360 API, particularly for CSL backend integration. It consolidates discoveries from extensive debugging and testing sessions.

## Table of Contents
1. [Core API Structure](#core-api-structure)
2. [Critical Issues and Solutions](#critical-issues-and-solutions)
3. [API Best Practices](#api-best-practices)
4. [Feature Implementation](#feature-implementation)
5. [Testing and Debugging](#testing-and-debugging)
6. [Quick Reference](#quick-reference)

## Core API Structure

### Namespaces
- **`adsk.core`**: Base classes (Application, Point3D, ValueInput, ObjectCollection)
- **`adsk.fusion`**: CAD features (Sketches, Features, Bodies, Components)
- **`adsk.cam`**: CAM functionality

### Unit System
**CRITICAL**: Fusion 360 API uses **centimeters** internally
```python
# Always convert mm to cm
value_cm = value_mm / 10.0
distance = adsk.core.ValueInput.createByReal(value_cm)
```

### Application Context
```python
# Get application and UI
app = adsk.core.Application.get()
ui = app.userInterface
design = app.activeProduct
root = design.rootComponent
```

## Critical Issues and Solutions

### 1. Dry-Run Mode Fix (CRITICAL)
**Problem**: FusionBackend's `_check_fusion()` fails when running inside Fusion add-in, causing dry-run mode.

**Solution**: Override in add-in context
```python
class FusionBackendWithContext(FusionBackend):
    """FusionBackend that knows it's running in Fusion context"""
    def __init__(self, session_config=None):
        self.session_config = session_config or {}
        self._fusion_available = True  # Force availability
        self._lineage = {}
        self._diag_store = []
        self._persisted_lineage = {}
    
    def _check_fusion(self):
        return True  # Always return True in add-in context
    
    def _ensure_design(self):
        global _app, _ui
        if not _app:
            _app = adsk.core.Application.get()
            _ui = _app.userInterface
        design = _app.activeProduct
        if not design or design.classType() != adsk.fusion.Design.classType():
            _app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
            design = _app.activeProduct
        return _app, _ui, design

# Use in add-in:
backend = FusionBackendWithContext()
```

### 2. IR Structure Mismatch
**Problem**: CSL v1.3 nests sketches/features in `root` object, but backend expects them at top level.

**Solution**: Flatten the structure
```python
backend_ir = ir.copy()
if "root" in ir and isinstance(ir["root"], dict):
    root_data = ir["root"]
    if "sketches" in root_data:
        backend_ir["sketches"] = root_data["sketches"]
    if "features" in root_data:
        backend_ir["features"] = root_data["features"]
    if "components" in root_data:
        backend_ir["components"] = root_data["components"]
result = backend.realize(backend_ir)
```

### 3. Double Unit Conversion Bug
**Problem**: Rectangle dimensions were being converted mm→cm twice, creating 10x smaller geometry.

**Wrong**:
```python
w_cm = w_mm / 10.0
h_cm = h_mm / 10.0
p1 = (center[0] - w_cm/2, center[1] - h_cm/2, 0)
# Then later:
p1_cm = (p1[0]/10.0, p1[1]/10.0, 0)  # Double conversion!
```

**Correct**:
```python
# Keep in mm until final conversion
p1 = (center[0] - w_mm/2, center[1] - h_mm/2, 0)
p2 = (center[0] + w_mm/2, center[1] + h_mm/2, 0)
# Convert once when creating points
p1_cm = (p1[0]/10.0, p1[1]/10.0, 0)
p2_cm = (p2[0]/10.0, p2[1]/10.0, 0)
```

### 4. Module Reloading in Add-ins
**Problem**: Add-ins cache Python modules, not picking up changes.

**Solution**: Force reload
```python
import importlib
import sys

# Delete cached modules
if 'triple_lindy.transpilers.fusion360_backend' in sys.modules:
    del sys.modules['triple_lindy.transpilers.fusion360_backend']
if 'triple_lindy.transpilers' in sys.modules:
    del sys.modules['triple_lindy.transpilers']
if 'triple_lindy' in sys.modules:
    del sys.modules['triple_lindy']

# Now import fresh
from triple_lindy.transpilers.fusion360_backend import FusionBackend
```

## Feature Implementation

### Sketches

#### Rectangle
```python
sketch = root.sketches.add(root.xYConstructionPlane)
rect = sketch.sketchCurves.sketchLines.addTwoPointRectangle(
    adsk.core.Point3D.create(x1_cm, y1_cm, 0),
    adsk.core.Point3D.create(x2_cm, y2_cm, 0)
)
```

**Entity Parsing**: Support both formats
```python
# Support "rect" and "rectangle"
if kind == "rect" or kind == "rectangle":
    # Support both "w"/"h" and "width"/"height"
    w_mm = self._parse_length_mm(ent.get("w") or ent.get("width"))
    h_mm = self._parse_length_mm(ent.get("h") or ent.get("height"))
```

### Extrude
```python
ext_feats = root.features.extrudeFeatures
profile = sketch.profiles.item(0)
ext_input = ext_feats.createInput(
    profile, 
    adsk.fusion.FeatureOperations.NewBodyFeatureOperation
)
ext_input.setDistanceExtent(False, adsk.core.ValueInput.createByReal(distance_cm))
extrude = ext_feats.add(ext_input)
```

### Chamfer (Modern API - December 2020+)

#### CRITICAL: Use createInput2() Method
```python
# Get edges (smart selection to avoid conflicts)
edges = adsk.core.ObjectCollection.create()
# Select only opposite edges from top to avoid corner conflicts
for i in [0, 2]:  # Opposite edges
    edges.add(top_edges[i])

# Modern API
chamfer_feats = root.features.chamferFeatures
chamfer_input = chamfer_feats.createInput2()  # No parameters!

# Configure chamfer
distance = adsk.core.ValueInput.createByReal(distance_cm)
chamfer_input.chamferEdgeSets.addEqualDistanceChamferEdgeSet(
    edges,     # ObjectCollection of edges
    distance,  # ValueInput for distance
    False      # isTangentChain - FALSE for independent edges
)

# Create chamfer
chamfer = chamfer_feats.add(chamfer_input)
```

#### Alternative Chamfer Types
```python
# Distance and angle
chamfer_input.chamferEdgeSets.addDistanceAndAngleChamferEdgeSet(
    edges, distance, angle, False
)

# Two distances
chamfer_input.chamferEdgeSets.addTwoDistancesChamferEdgeSet(
    edges, distance1, distance2, False
)
```

### Fillet (Updated API)
```python
fillet_feats = root.features.filletFeatures
fillet_input = fillet_feats.createInput()

# Add edge set with radius
radius = adsk.core.ValueInput.createByReal(radius_cm)
fillet_input.addConstantRadiusEdgeSet(edges, radius, True)

# Create fillet
fillet = fillet_feats.add(fillet_input)
```

## Edge Selection Strategies

### Avoid Corner Conflicts
When chamfering/filleting box edges:
1. **Don't select all edges** - causes intersection errors
2. **Select opposite edges only** - avoids corner conflicts
3. **Use isTangentChain=False** - treat edges independently

```python
# Get top edges of a box
top_edges = []
max_z = -float('inf')

# Find max Z
for edge in body.edges:
    z = edge.startVertex.geometry.z
    max_z = max(max_z, z)

# Collect horizontal edges at top
for edge in body.edges:
    z_start = edge.startVertex.geometry.z
    z_end = edge.endVertex.geometry.z
    if abs(z_start - max_z) < 0.001 and abs(z_end - max_z) < 0.001:
        top_edges.append(edge)

# Select opposite edges (0 and 2 from 4 top edges)
selected_edges = [top_edges[0], top_edges[2]]
```

## Testing and Debugging

### Utility Scripts

#### verify_addin_status.py
Check if add-in is running and responsive:
```python
def check_addin():
    command = {"action": "ping"}
    with open(COMMAND_FILE, 'w') as f:
        json.dump(command, f)
    time.sleep(1)
    if STATUS_FILE.exists():
        with open(STATUS_FILE, 'r') as f:
            status = json.load(f)
        return status.get('status') == 'pong'
    return False
```

#### clear_design.py
Clear active design:
```python
command = {"action": "clear_design"}
with open(COMMAND_FILE, 'w') as f:
    json.dump(command, f)
```

### Debug Techniques

#### Body Count Verification
```python
bodies_before = root.bRepBodies.count
# Perform operation
chamfer = chamfer_feats.add(chamfer_input)
bodies_after = root.bRepBodies.count

if bodies_after > bodies_before:
    print("WARNING: Operation created new body instead of modifying!")
```

#### Edge Validation
```python
for edge in edges:
    if edge.isValid:
        print(f"Edge length: {edge.length}cm")
        print(f"Start: {edge.startVertex.geometry.z}")
        print(f"End: {edge.endVertex.geometry.z}")
```

## Quick Reference

### Common Errors and Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `InternalValidationError : value` | Wrong chamfer API method | Use `createInput2()` + `chamferEdgeSets.addEqualDistanceChamferEdgeSet()` |
| `ASM_BL_NO_SPR_CUR_INT` | Edges intersect at corners | Select opposite edges only, use `isTangentChain=False` |
| `ASM_BL_UNFIN_SHEET` | Chamfer/fillet too large | Reduce size or select fewer edges |
| `error:no_profile` | Sketch entity not recognized | Check entity type ("rect" vs "rectangle") and property names |
| Dry-run mode | `_fusion_available = False` | Use `FusionBackendWithContext` override |

### API Method Evolution

| Feature | Old API (Deprecated) | Modern API (2020+) |
|---------|---------------------|-------------------|
| Chamfer | `createInput(edges, False)` | `createInput2()` |
| Chamfer Config | `input.setEqualDistance()` | `input.chamferEdgeSets.addEqualDistanceChamferEdgeSet()` |
| Fillet | `createFilletDefinition()` | `createInput()` + `addConstantRadiusEdgeSet()` |

### File Locations

- **Add-in Location**: `~/Library/Application Support/Autodesk/Autodesk Fusion 360/API/AddIns/`
- **Command File**: `~/Documents/CSL/live_command.json`
- **Status File**: `~/Documents/CSL/live_status.json`

### Deployment Script
```bash
#!/bin/bash
# deploy_triple_lindy.sh
cp -r triple_lindy ~/Library/Application\ Support/Autodesk/Autodesk\ Fusion\ 360/API/AddIns/
cp -r triple_lindy_fusion_enhanced ~/Library/Application\ Support/Autodesk/Autodesk\ Fusion\ 360/API/AddIns/
echo "Deployment complete. Restart add-in in Fusion 360."
```

## References
- [Fusion 360 API Documentation](https://help.autodesk.com/view/fusion360/ENU/)
- [ChamferFeatures Reference](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/ChamferFeatures.htm)
- [API User's Guide](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/API_intro.htm)

## Version History
- 2024-12-30: Initial documentation created after fixing CSL backend integration
- Key fixes: Dry-run mode, modern chamfer API, unit conversion, edge selection strategies
