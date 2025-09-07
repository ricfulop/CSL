# Triple Lindy - Universal CAD Control System

A real-time control system for multiple CAD platforms through a unified interface. Triple Lindy provides backend adapters for various CAD software, enabling external tools to control them programmatically.

## Architecture

Triple Lindy uses a modular backend architecture where each CAD platform has its own adapter:

```
External Tools (AI, Scripts, etc.)
           ↓
    Triple Lindy Core
           ↓
    Backend Adapters
    ├── Fusion 360 Backend
    ├── FreeCAD Backend (planned)
    ├── Onshape Backend (planned)
    ├── SolidWorks Backend (planned)
    ├── NX Backend (planned)
    └── Blender Backend (planned)
```

## Supported Platforms

### ✅ Fusion 360
- **Backend**: `triple_lindy/transpilers/fusion360_backend.py`
- **Add-in**: `triple_lindy_fusion_stable/`
- **Protocol**: File-based (watches `~/Documents/CSL/live_command.json`)
- **Status**: Production ready

### 🚧 FreeCAD (Planned)
- **Backend**: `triple_lindy/transpilers/freecad_backend.py`
- **Add-in**: TBD
- **Protocol**: TBD
- **Status**: In development

### 🚧 Onshape (Planned)
- **Backend**: `triple_lindy/transpilers/onshape_backend.py`
- **API**: REST API based
- **Protocol**: WebSocket/REST
- **Status**: Planned

### 🚧 Other Platforms
- SolidWorks, NX, Blender - backends planned

## Backend Interface

All backends implement a common interface:

```python
class BackendAdapter:
    def open_session(self, config: Dict[str, Any]) -> None
    def realize(self, csl_ir: Dict[str, Any]) -> Dict[str, str]
    def export(self, export_ops: List[Dict[str, Any]]) -> None
    def get_capabilities(self) -> Dict[str, Any]
    def close_session(self) -> None
```

## CSL (CAD Specification Language)

Triple Lindy uses CSL as its intermediate representation, allowing the same design specification to work across different CAD platforms:

```json
{
  "csl": "1.3",
  "meta": {"name": "Universal Part", "units": "mm"},
  "sketches": [...],
  "features": [...]
}
```

## Installation

### For Fusion 360

1. Copy `triple_lindy_fusion_stable/` to your Fusion 360 add-ins folder
2. In Fusion 360: Scripts and Add-Ins (Shift+S) → Add-Ins tab → Run `triple_lindy_fusion_stable`
3. Use `triple_lindy_daemon/file_client.py` to send commands

### For Other Platforms

See platform-specific documentation in their respective directories (when available).

## Usage

The same client can control different CAD platforms:

```bash
# Generic commands work across all platforms
python3 triple_lindy_daemon/file_client.py ping      # Test connection
python3 triple_lindy_daemon/file_client.py clear     # Clear design
python3 triple_lindy_daemon/file_client.py query     # Query state

# Execute CSL (works on any platform with a backend)
python3 triple_lindy_daemon/file_client.py file --file design.json
```

## Development

### Adding a New Backend

1. Create `triple_lindy/transpilers/<platform>_backend.py`
2. Implement the `BackendAdapter` interface
3. Create platform-specific add-in/plugin in `triple_lindy_<platform>/`
4. Document setup in this README

### Backend Requirements

- Must translate CSL IR to platform-specific API calls
- Should provide error reporting (no silent failures)
- Should support querying current state
- Should handle units conversion appropriately

## Project Structure

```
triple_lindy/
├── transpilers/
│   ├── fusion360_backend.py    # Fusion 360 backend
│   ├── freecad_backend.py      # FreeCAD backend (planned)
│   └── onshape_backend.py      # Onshape backend (planned)
├── triple_lindy_fusion_stable/  # Fusion 360 add-in
├── triple_lindy_freecad/       # FreeCAD add-in (planned)
└── triple_lindy_daemon/         # Client tools
    └── file_client.py           # Command-line client
```

## Protocol

Each platform may use different communication protocols:

- **Fusion 360**: File-based (JSON files)
- **Onshape**: REST API / WebSocket
- **FreeCAD**: Python API direct / File-based
- **SolidWorks**: COM API / File-based

## Contributing

To add support for a new CAD platform:

1. Study the existing Fusion 360 backend as reference
2. Create a new backend following the interface
3. Implement platform-specific communication
4. Add tests and documentation
5. Submit a pull request

## License

[License information]

## Roadmap

- [x] Fusion 360 support
- [ ] FreeCAD support
- [ ] Onshape support
- [ ] SolidWorks support
- [ ] NX support
- [ ] Blender support
- [ ] Universal client library
- [ ] Web-based control interface