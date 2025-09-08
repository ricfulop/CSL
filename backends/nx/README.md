# NX Backend

## Overview
Siemens NX (formerly Unigraphics) integration via NXOpen API. Enterprise-level CAD/CAM/CAE platform with Python, C++, and .NET support.

## Quick Start

### Prerequisites
- Siemens NX installed (NX 12 or later)
- NXOpen Common API Framework
- Python 3.x or .NET Framework

### Setup
```python
import NXOpen
import NXOpen.UF

# Get the session
theSession = NXOpen.Session.GetSession()
workPart = theSession.Parts.Work
displayPart = theSession.Parts.Display

# Create new part
theSession.Parts.NewDisplay("CSL_Part", NXOpen.Part.Units.Millimeters)
```

## Architecture
- **Integration Methods**:
  - NXOpen Python API
  - NXOpen .NET API  
  - NXOpen C++ API
  - Journaling (record/replay)
- **Communication**: In-process or remote (NX Connect)
- **Unit System**: Part-dependent (mm or inches)

## Current Status
- [ ] Basic geometry creation
- [ ] Sketch support
- [ ] Feature operations
- [ ] Assembly support
- [ ] PMI/GD&T support
- [ ] CAM integration
- [ ] Simulation integration

## NXOpen API Structure
```
NXOpen.Session
├── Parts
│   ├── Work (current part)
│   ├── Display
│   └── All Parts Collection
├── Features
│   ├── FeatureBuilder
│   ├── Block
│   ├── Cylinder
│   └── Extrude
├── Sketches
│   ├── SketchCollection
│   ├── Constraints
│   └── Dimensions
└── Assemblies
    ├── Components
    └── Constraints
```

## Key API Examples

### Create Sketch
```python
# Create sketch on XY plane
sketchInPlaceBuilder = workPart.Sketches.CreateSketchInPlaceBuilder2(None)
origin = NXOpen.Point3d(0.0, 0.0, 0.0)
normal = NXOpen.Vector3d(0.0, 0.0, 1.0)
plane = workPart.Planes.CreatePlane(origin, normal)

sketchInPlaceBuilder.PlaneReference = plane
sketch = sketchInPlaceBuilder.Commit()

# Add rectangle
sketch.CreateRectangle(
    NXOpen.Point3d(-30.0, -30.0, 0.0),
    NXOpen.Point3d(30.0, 30.0, 0.0)
)
```

### Create Extrude
```python
extrudeBuilder = workPart.Features.CreateExtrudeBuilder(None)
extrudeBuilder.Section.SetSectionData(sketch)

# Set direction and limits
direction = workPart.Directions.CreateDirection(
    NXOpen.Point3d(0.0, 0.0, 0.0),
    NXOpen.Vector3d(0.0, 0.0, 1.0)
)
extrudeBuilder.Direction = direction
extrudeBuilder.Limits.StartExtend.Value.Value = 0.0
extrudeBuilder.Limits.EndExtend.Value.Value = 40.0  # 40mm

feature = extrudeBuilder.Commit()
```

### Journaling Support
```python
# Record journal
theSession.StartJournaling("csl_operations.py")

# Perform operations...

# Stop recording
theSession.StopJournaling()
```

## Remote Execution (NX Connect)
```python
# Connect to remote NX session
import NXOpen.RemoteUtilities

remoteSession = NXOpen.RemoteUtilities.GetRemoteSession(
    host="nx_server.company.com",
    port=4567
)
```

## Known Limitations
- License requirements
- Version-specific API changes
- Complex feature tree management
- Performance with large assemblies
- Limited documentation for advanced features

## Advantages
- Comprehensive API coverage
- Multi-language support
- Journaling for macro recording
- Remote execution capability
- Integration with Teamcenter PLM
- Advanced CAM/CAE capabilities

## Code Structure
```
nx/
├── __init__.py
├── nx_backend.py           # CSL to NX translator
├── nx_connect.py           # Remote session management
├── journals/
│   ├── template.py         # Journal templates
│   └── utilities.py
├── features/
│   ├── sketches.py
│   ├── solids.py
│   └── assemblies.py
└── examples/
    ├── create_part.py
    ├── assembly_test.py
    └── cam_setup.py
```

## Resources
- [NXOpen Programmer's Guide](https://docs.sw.siemens.com/en-US/product/209349590/doc/DC201903.NX_help/en_US/data/nxopen_api/programmer_guide/nxopen_prog_guide.html)
- [NXOpen Python API Reference](https://docs.sw.siemens.com/documentation/nx/)
- [GTAC Support](https://support.sw.siemens.com/)
- [NX Journaling Forum](https://community.sw.siemens.com/s/topic/0TO4O000000MihFWAS/nx-design)

## TODO
- [ ] Implement NXOpen wrapper
- [ ] Create feature builders for CSL
- [ ] Handle unit conversions
- [ ] Add Teamcenter integration
- [ ] Implement selection filters
- [ ] Test with different NX versions
- [ ] Add CAM operation support

## Notes for Implementation
- Use FeatureBuilder pattern for parametric features
- Handle undo/redo through Update class
- Consider using User Defined Objects (UDO) for CSL data
- Leverage expressions for parametric relationships
- Use selection intent rules for robust selection
- Consider part families for variations
