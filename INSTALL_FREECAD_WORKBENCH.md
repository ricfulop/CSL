# Installing Triple Lindy FreeCAD Workbench

## Quick Installation

### macOS/Linux
```bash
# Copy workbench to FreeCAD modules directory
cp -r triple_lindy_freecad ~/.FreeCAD/Mod/TripleLindy

# Or create a symlink (better for development)
ln -s $(pwd)/triple_lindy_freecad ~/.FreeCAD/Mod/TripleLindy
```

### Windows
```powershell
# Copy workbench to FreeCAD modules directory
xcopy triple_lindy_freecad "%APPDATA%\FreeCAD\Mod\TripleLindy\" /E /I

# Or in Command Prompt
xcopy triple_lindy_freecad "%APPDATA%\FreeCAD\Mod\TripleLindy\" /E /I
```

## Alternative Locations

FreeCAD looks for workbenches in these locations:
- `~/.FreeCAD/Mod/` (Linux/macOS user directory)
- `~/.local/share/FreeCAD/Mod/` (Linux alternative)
- `%APPDATA%\FreeCAD\Mod\` (Windows)
- `/usr/share/freecad/Mod/` (System-wide Linux)
- `/Applications/FreeCAD.app/Contents/Resources/Mod/` (macOS app bundle)

## Usage

1. **Start FreeCAD**
2. **Switch to Triple Lindy Workbench**
   - Use the workbench selector dropdown
   - Select "Triple Lindy"
3. **Start the File Watcher**
   - Click "Start Triple Lindy" in toolbar
   - Or use menu: Triple Lindy → Start Triple Lindy

## Available Commands

### Toolbar Buttons
- **Start** - Begin watching for CSL commands
- **Stop** - Stop the file watcher
- **Status** - Check current status

### Menu Items
- **Start Triple Lindy** - Start file watcher
- **Stop Triple Lindy** - Stop file watcher
- **Triple Lindy Status** - Check watcher status
- **Test Geometry** - Create test objects
- **Clear Document** - Remove all objects
- **Triple Lindy Help** - Show help dialog

## File Locations

- **Command file**: `~/Documents/CSL/live_command.json`
- **Status file**: `~/Documents/CSL/live_status.json`

## Testing the Workbench

### 1. Send a Ping
```python
import json
from pathlib import Path

command_file = Path.home() / "Documents" / "CSL" / "live_command.json"
command_file.write_text(json.dumps({"action": "ping"}))
```

### 2. Create Test Geometry
```python
command_file.write_text(json.dumps({"action": "test_simple"}))
```

### 3. Send CSL IR
```python
csl_ir = {
    "ir": {
        "csl": "1.3",
        "meta": {"name": "Test", "units": "mm"},
        "sketches": [{
            "id": "s1",
            "on": "XY",
            "entities": [
                {"type": "rect", "p1": [0, 0], "p2": [50, 30]}
            ]
        }],
        "features": [{
            "kind": "extrude",
            "profile": "s1",
            "distance": 20
        }]
    }
}
command_file.write_text(json.dumps(csl_ir))
```

## Troubleshooting

### Workbench Not Appearing
1. Check FreeCAD version (requires 0.19+)
2. Verify installation path
3. Restart FreeCAD
4. Check View → Workbench menu

### File Watcher Not Working
1. Check file permissions in `~/Documents/CSL/`
2. Look for errors in FreeCAD Python console
3. Verify backend is installed: `from triple_lindy.transpilers.freecad_backend import FreeCADBackend`

### Commands Not Processing
1. Check status with Status button
2. Ensure watcher is running (green status)
3. Verify JSON is valid in command file
4. Check FreeCAD Report View for errors

## Features

- ✅ File-based command watching (like Fusion 360)
- ✅ Full CSL IR support
- ✅ GUI integration with toolbar and menu
- ✅ Status monitoring
- ✅ Test geometry creation
- ✅ Document management
- ✅ Help system

## Uninstalling

Simply remove the workbench directory:
```bash
# macOS/Linux
rm -rf ~/.FreeCAD/Mod/TripleLindy

# Windows
rmdir /s "%APPDATA%\FreeCAD\Mod\TripleLindy"
```
