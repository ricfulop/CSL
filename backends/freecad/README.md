# FreeCAD Backend

## Overview
FreeCAD integration via Python workbench for CSL support. Open-source parametric 3D CAD modeler with Python scripting capabilities.

## Quick Start

### Installation
1. Install FreeCAD (v0.20 or later recommended)
2. Copy workbench to FreeCAD modules:
   ```bash
   cp -r triple_lindy/ ~/.FreeCAD/Mod/
   ```
3. Restart FreeCAD
4. Select "Triple Lindy" workbench

### First Test
```python
import FreeCAD as App
import Part

# Create a box
doc = App.newDocument()
box = doc.addObject("Part::Box", "Box")
box.Length = 60  # mm
box.Width = 60   # mm
box.Height = 40  # mm
doc.recompute()
```

## Architecture
- **Integration Method**: Python Workbench
- **API**: FreeCAD Python API (FreeCADGui, Part, Sketcher modules)
- **Communication**: Direct Python calls or file-based IR processing
- **Unit System**: Millimeters (native)

## Current Status
- [x] Basic geometry creation (box, cylinder, sphere)
- [x] Sketch support (partial)
- [ ] Advanced features (fillets, chamfers need refinement)
- [ ] Assembly support (Assembly4 or A2plus integration)
- [x] Export capabilities (STEP, STL, etc.)

## Known Limitations
- Less robust chamfer/fillet compared to commercial CAD
- Limited assembly constraints
- Performance issues with complex models
- Different sketch constraint solver behavior

## Key API Differences from Fusion 360
| Feature | FreeCAD | Fusion 360 |
|---------|----------|------------|
| Units | mm (native) | cm (internal) |
| Sketches | `Sketcher.Sketch()` | `sketches.add()` |
| Extrude | `Part.Extrusion()` | `extrudeFeatures.add()` |
| Chamfer | `Part.makeChamfer()` | `chamferFeatures.add()` |

## Code Structure
```
freecad/
├── __init__.py
├── freecad_backend.py    # CSL to FreeCAD translator
├── workbench.py          # FreeCAD workbench definition
└── examples/
    ├── basic_shapes.py
    └── csl_test.py
```

## Resources
- [FreeCAD Python API Documentation](https://wiki.freecadweb.org/Python_scripting_tutorial)
- [FreeCAD Forum](https://forum.freecadweb.org/)
- [Part Module Documentation](https://wiki.freecadweb.org/Part_Module)
- [Sketcher Workbench](https://wiki.freecadweb.org/Sketcher_Workbench)

## TODO
- [ ] Complete fillet/chamfer implementation
- [ ] Add assembly support
- [ ] Implement selection queries
- [ ] Add parameter support
- [ ] Test complex CSL examples

## Notes for Implementation
- FreeCAD uses Document-Object model
- Topology naming problem affects edge/face selection
- Consider using Part Design workbench for parametric features
- May need to handle units conversion explicitly
