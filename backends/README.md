# Backend Platform Documentation

This directory contains platform-specific documentation, integration guides, and implementation notes for each supported CAD/CAE/CAM backend.

## 📁 Directory Structure

Each backend folder follows a consistent structure:
```
backend-name/
├── README.md                 # Platform overview and quick start
├── API_GUIDE.md              # Detailed API documentation and patterns
├── INTEGRATION_NOTES.md      # CSL integration specifics
├── ISSUES_AND_SOLUTIONS.md   # Known issues and their solutions
├── examples/                 # Code examples and test scripts
└── resources/                # Links, references, documentation
```

## 🎯 Supported Platforms

### ✅ Production Ready
- **[Fusion 360](../fusion/)** - Full CSL integration with modern API support

### 🚧 In Development
- **[FreeCAD](./freecad/)** - Python workbench integration
- **[Onshape](./onshape/)** - REST API and FeatureScript

### 📋 Planned
- **[SolidWorks](./solidworks/)** - .NET/COM integration (Windows)
- **[Blender](./blender/)** - Geometry Nodes and bpy
- **[NX](./nx/)** - NXOpen API

## 🔧 Backend Status Matrix

| Platform | Language | API Type | CSL Support | Documentation | Status |
|----------|----------|----------|-------------|---------------|---------|
| Fusion 360 | Python | Add-in | ✅ Full | ✅ Complete | Production |
| FreeCAD | Python | Workbench | 🚧 Partial | 📝 Basic | Development |
| Onshape | TypeScript/REST | FeatureScript | 🚧 Partial | 📝 Basic | Development |
| SolidWorks | .NET/VBA | COM | ❌ None | 📝 Planning | Planned |
| Blender | Python | bpy | ❌ None | 📝 Planning | Planned |
| NX | Python/C++ | NXOpen | ❌ None | 📝 Planning | Planned |

## 🎨 Template for New Backends

When adding a new backend, use this template structure:

### README.md Template
```markdown
# [Platform Name] Backend

## Overview
Brief description of the platform and its CSL integration approach.

## Quick Start
1. Installation requirements
2. Setup steps
3. First test

## Architecture
- Integration method (Add-in, Plugin, API, etc.)
- Communication protocol
- File formats supported

## Current Status
- [ ] Basic geometry creation
- [ ] Sketch support
- [ ] Feature operations
- [ ] Assembly support
- [ ] Export capabilities

## Known Limitations
- List platform-specific limitations

## Resources
- Official API documentation
- Community resources
- Example repositories
```

### API_GUIDE.md Template
```markdown
# [Platform] API Guide

## Core Concepts
- Units system
- Coordinate system
- Object model

## Key Classes/Functions
- Geometry creation
- Feature operations
- Selection methods

## Code Examples
Working examples with explanations

## Best Practices
Platform-specific tips and patterns
```

## 🔄 Contributing

When implementing a new backend:

1. **Create the folder structure** using the template
2. **Document as you go** - capture issues and solutions immediately
3. **Test scripts** - add working examples to the examples/ folder
4. **Update status** - keep the matrix current
5. **Link from DOC_INDEX.md** - ensure discoverability

## 📚 See Also

- [CSL Specification](../CSL_v1_3/csl_v1_3_spec.md)
- [Backend Gap Analysis](../BACKEND_GAP_ANALYSIS.md)
- [Fusion Implementation](../fusion/FUSION_360_API_GUIDE.md)

---

**Note for AI Agents**: Start with the README.md in each backend folder for platform-specific guidance. Check ISSUES_AND_SOLUTIONS.md for common problems before debugging.
