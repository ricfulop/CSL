# SolidWorks Backend

## Overview
Windows-based CAD platform with COM/.NET API support. CSL integration via add-in or standalone automation.

## Quick Start

### Prerequisites
- Windows OS (Windows 10/11)
- SolidWorks 2020 or later
- Visual Studio (for .NET development) or Python with win32com

### Setup Options

#### Option 1: Python COM Automation
```python
import win32com.client

# Connect to SolidWorks
swApp = win32com.client.Dispatch("SldWorks.Application")
swApp.Visible = True

# Create new part
part = swApp.NewDocument("C:\\ProgramData\\SolidWorks\\Templates\\Part.prtdot", 0, 0, 0)
swModel = swApp.ActiveDoc
```

#### Option 2: C# Add-in
```csharp
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;

public class CSLAddIn : ISwAddin
{
    private SldWorks swApp;
    
    public bool ConnectToSW(object ThisSW, int Cookie)
    {
        swApp = (SldWorks)ThisSW;
        // Initialize add-in
        return true;
    }
}
```

## Architecture
- **Integration Methods**: 
  - COM Automation (Python/VBA)
  - .NET Add-in (C#/VB.NET)
  - Standalone EXE
- **API**: SolidWorks API (COM-based)
- **Communication**: COM/IPC or file-based
- **Unit System**: Document-dependent (typically mm or inches)

## Current Status
- [ ] Basic geometry creation
- [ ] Sketch support
- [ ] Feature operations
- [ ] Assembly support
- [ ] Drawing generation
- [ ] PDM integration

## API Structure
```
SolidWorks.Application
├── Documents
│   ├── Parts (IPartDoc)
│   ├── Assemblies (IAssemblyDoc)
│   └── Drawings (IDrawingDoc)
├── Features
│   ├── Extrude
│   ├── Revolve
│   ├── Sweep
│   └── Loft
├── Sketches
│   ├── Lines
│   ├── Arcs
│   └── Constraints
└── Selection Manager
```

## Key API Patterns

### Create Sketch
```python
# Select plane
swModel.Extension.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, None, 0)

# Insert sketch
swModel.SketchManager.InsertSketch(True)

# Draw rectangle
swModel.SketchManager.CreateCenterRectangle(0, 0, 0, 0.06, 0.06, 0)

# Exit sketch
swModel.SketchManager.InsertSketch(True)
```

### Create Extrude
```python
# Select sketch
swModel.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, None, 0)

# Create extrude
swFeature = swModel.FeatureManager.FeatureExtrusion3(
    True,    # Single direction
    False,   # Flip
    False,   # Reverse
    0,       # End condition (blind)
    0,       # End condition 2
    0.04,    # Depth (40mm)
    0,       # Depth 2
    False,   # Draft
    False,   # Draft outward
    False,   # Draft both directions
    0,       # Draft angle
    0,       # Draft angle 2
    False,   # Reverse offset
    False,   # Translate surface
    False,   # Merge
    True,    # Use feat scope
    True,    # Use auto select
    0,       # Start condition
    0,       # Flip start offset
    False    # Sheet metal
)
```

## Known Limitations
- Windows-only
- Requires SolidWorks license
- COM performance overhead
- Version-specific API changes
- Complex API with many parameters

## Deployment Options
1. **Add-in**: Installed in SolidWorks, loads automatically
2. **Macro**: VBA/VSTA macros for simple automation
3. **Standalone**: External application controlling SolidWorks
4. **Task Scheduler**: Batch processing integration

## Code Structure
```
solidworks/
├── __init__.py
├── solidworks_backend.py    # CSL to SolidWorks translator
├── com_wrapper.py           # Python COM interface
├── addin/
│   ├── CSLAddIn.cs         # C# add-in code
│   └── CSLAddIn.csproj
└── examples/
    ├── create_part.py
    └── assembly_test.py
```

## Resources
- [SolidWorks API Documentation](https://help.solidworks.com/2024/english/api/sldworksapi/solidworks.interop.sldworks~solidworks.interop.sldworks_namespace.html)
- [API Support Forums](https://r1132100503382-eu1-3dswym.3dexperience.3ds.com/community/solidworks-api)
- [CodeStack - SolidWorks API Examples](https://www.codestack.net/solidworks-api/)
- [Python for SolidWorks](https://github.com/m9795/python-solidworks)

## TODO
- [ ] Implement COM wrapper for Python
- [ ] Create C# add-in template
- [ ] Handle unit conversions
- [ ] Add error handling for COM exceptions
- [ ] Implement selection queries
- [ ] Test on different SolidWorks versions

## Notes for Implementation
- Use early binding for better performance
- Handle COM cleanup properly to avoid memory leaks
- Consider using SwEx framework for add-in development
- Batch operations for better performance
- Be aware of selection marks and types
