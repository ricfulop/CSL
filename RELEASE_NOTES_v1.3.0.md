# CSL v1.3.0 Release Notes

## 🎉 Major Release: Triple Lindy Real-time Control System

### Overview
CSL v1.3.0 introduces the **Triple Lindy real-time control system** for CAD automation, along with advanced surface modeling, sheet metal operations, and enhanced assembly capabilities. This release establishes the foundation for multi-CAD platform support beyond Fusion 360.

## ✨ Key Highlights

### 🚀 Triple Lindy Real-time Control
- **Production-ready** real-time control for Fusion 360
- **File-based protocol** for reliable CAD communication
- **Universal client** that works across all backends
- **Query system** for debugging and state inspection
- **Direct API** and **CSL transpilation** modes
- **Comprehensive error reporting** - no silent failures

### 🏗️ Multi-CAD Architecture
- **Backend interface** for all CAD platforms
- **Fusion 360 backend** - fully implemented with CSL v1.0-1.3 support
- **FreeCAD backend** - placeholder ready for implementation
- **Onshape backend** - placeholder with REST API structure
- Extensible design for SolidWorks, NX, Blender, etc.

### 📐 Advanced Modeling Features
- **Surface operations**: patch, extend, trim, knit with explicit queries
- **Pattern enhancements**: per-instance controls via `instances[]`
- **Constraint improvements**: construction geometry, reference dimensions, equal-length arrays
- **Loft enhancements**: G0/G1/G2 continuity, orientation options, rails/centerline
- **Export controls**: STL tessellation parameters for quality control

## 🔧 Technical Improvements

### Backend Fixes
- Fixed critical profile resolution bug in extrude operations
- Added missing `_feature_operation()` method
- Improved entity-to-sketch mapping for all entity types
- Enhanced error reporting throughout the backend

### API Enhancements
```python
# New backend interface
class BackendAdapter:
    def realize(csl_ir: Dict) -> Dict[str, str]
    def query_state() -> Dict[str, Any]
    def get_capabilities() -> Dict[str, Any]
```

## 📦 Installation

### Fusion 360 with Triple Lindy
```bash
# Install the add-in
cp -r triple_lindy_fusion_stable "$HOME/Library/Application Support/Autodesk/Autodesk Fusion 360/API/AddIns/"

# Test real-time control
python3 triple_lindy_daemon/file_client.py ping
python3 triple_lindy_daemon/file_client.py query
python3 triple_lindy_daemon/file_client.py file --file design.json
```

## 🔄 Migration from v1.2

CSL v1.3 is **fully backward compatible** with v1.2. All new fields are optional:
- Surface operations are additive features
- Pattern `instances[]` is optional (defaults to count-based)
- Loft continuity defaults to G0 if not specified
- Export controls use sensible defaults

## 📊 Capabilities

The backend now reports detailed capabilities:
```json
{
  "backend": "fusion360",
  "csl_versions": ["1.0", "1.1", "1.2", "1.3"],
  "features": {
    "surface_ops": true,
    "patterns_per_instance": true,
    "loft_continuity": true,
    "export_stl_controls": true
  }
}
```

## 🐛 Bug Fixes
- Fixed sketch plane resolution in realize()
- Fixed profile selection for extrude features
- Fixed entity ID tracking across sketches
- Improved error handling to prevent silent failures

## 📚 Documentation
- New `TRIPLE_LINDY_README.md` for the control system
- Updated examples with v1.3 features
- Enhanced user guide with surface modeling
- Added backend development guide

## 🔮 Future Roadmap
- [ ] FreeCAD backend implementation
- [ ] Onshape REST API integration
- [ ] SolidWorks COM bridge
- [ ] Web-based control interface
- [ ] AI agent integration

## 💡 Examples

### Surface Patch
```json
{
  "kind": "patch",
  "edges_query": {"type": "loop", "index": 0},
  "tangent": true
}
```

### Pattern with Instances
```json
{
  "kind": "pattern",
  "type": "rectangular",
  "instances": [
    {"dx": "0", "dy": "0"},
    {"dx": "10mm", "dy": "0"},
    {"dx": "20mm", "dy": "5mm"}
  ]
}
```

### Loft with Continuity
```json
{
  "kind": "loft",
  "profiles": ["prof1", "prof2"],
  "continuity": "G2",
  "rails_query": {"type": "edges", "tag": "guide"}
}
```

## 🙏 Acknowledgments
Special thanks to all contributors and testers who helped make CSL v1.3.0 the most robust release yet!

---
**Version**: 1.3.0  
**Release Date**: September 7, 2024  
**Status**: Production Ready (Fusion 360)
