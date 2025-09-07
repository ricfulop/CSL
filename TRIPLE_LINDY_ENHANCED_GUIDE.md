# Triple Lindy Enhanced v2.0.0 - User Guide

## Overview

Triple Lindy Enhanced is a comprehensive CAD automation add-in for Fusion 360 that provides complete programmatic control over all aspects of design, assembly, and analysis.

## Installation

1. Copy the enhanced add-in to Fusion 360:
```bash
cp -r triple_lindy_fusion_enhanced "$HOME/Library/Application Support/Autodesk/Autodesk Fusion 360/API/AddIns/"
```

2. In Fusion 360: Scripts & Add-Ins (Shift+S) → Add-Ins tab → Run "triple_lindy_fusion_enhanced"

3. Test the connection:
```bash
python3 triple_lindy_daemon/file_client_enhanced.py ping
```

## Command Reference

### 1. Parameters & Expressions

Manage design parameters programmatically:

```bash
# Set a parameter
python3 file_client_enhanced.py param set --name width --value 100mm

# Get a parameter
python3 file_client_enhanced.py param get --name width

# List all parameters
python3 file_client_enhanced.py param list

# Create expression-based parameter
python3 file_client_enhanced.py param expression --name height --expression "width * 2"

# Delete a parameter
python3 file_client_enhanced.py param delete --name old_param
```

### 2. Timeline Control

Manipulate the design timeline:

```bash
# List timeline items
python3 file_client_enhanced.py timeline list

# Roll back to position
python3 file_client_enhanced.py timeline rollback --index 5

# Suppress features
python3 file_client_enhanced.py timeline suppress --name "Fillet1"
python3 file_client_enhanced.py timeline suppress --index 3
python3 file_client_enhanced.py timeline suppress --range 2 5

# Unsuppress features
python3 file_client_enhanced.py timeline unsuppress --name "Fillet1"

# Delete timeline item
python3 file_client_enhanced.py timeline delete --index 3
```

### 3. Selection & Picking

Select geometry programmatically:

```bash
# Clear selection
python3 file_client_enhanced.py select clear

# Select all bodies
python3 file_client_enhanced.py select body --all

# Select specific faces
python3 file_client_enhanced.py select face --indices 0 2 4

# Select with filters
python3 file_client_enhanced.py select face --planar --all
python3 file_client_enhanced.py select face --cylindrical --area-gt 10
python3 file_client_enhanced.py select edge --name "Edge*"

# Get current selection
python3 file_client_enhanced.py select get
```

### 4. Component & Assembly

Manage components and assemblies:

```bash
# Create new component
python3 file_client_enhanced.py component create --name "SubAssembly1"

# Activate component
python3 file_client_enhanced.py component activate --name "SubAssembly1"

# Insert external component
python3 file_client_enhanced.py component insert --file "bearing.f3d"

# List components
python3 file_client_enhanced.py component list

# Transform component
python3 file_client_enhanced.py component transform --name "Part1" \
  --translate 10 20 30 --rotate 0 0 45

# Delete component
python3 file_client_enhanced.py component delete --name "OldPart"
```

### 5. Joint Management

Create and control joints:

```bash
# Create joint
python3 file_client_enhanced.py joint create --type revolute \
  --comp1 "Base" --comp2 "Arm" --limits -90 90

# List joints
python3 file_client_enhanced.py joint list

# Drive joint
python3 file_client_enhanced.py joint drive --name "Joint1" --value 45

# Delete joint
python3 file_client_enhanced.py joint delete --name "Joint1"
```

Joint types: rigid, revolute, slider, cylindrical, pin_slot, planar, ball

### 6. Materials & Appearance

Apply materials to bodies:

```bash
# List available materials
python3 file_client_enhanced.py material list

# Apply material
python3 file_client_enhanced.py material apply --target "Body1" \
  --material "Aluminum 6061"

# Remove material
python3 file_client_enhanced.py material remove --target "Body1"
```

### 7. View & Camera Control

Control the viewport:

```bash
# Set standard views
python3 file_client_enhanced.py view set --orientation front
python3 file_client_enhanced.py view set --orientation top
python3 file_client_enhanced.py view set --orientation iso

# Zoom operations
python3 file_client_enhanced.py view zoom --factor 1.5
python3 file_client_enhanced.py view fit

# Screenshot
python3 file_client_enhanced.py view screenshot --file "view.png" --size 1920 1080
```

Orientations: front, back, top, bottom, left, right, iso

### 8. Export

Export to various formats:

```bash
# STEP export
python3 file_client_enhanced.py export step --file "output.step"

# STL export with quality
python3 file_client_enhanced.py export stl --file "output.stl" --quality high

# IGES export
python3 file_client_enhanced.py export iges --file "output.iges"

# Fusion archive
python3 file_client_enhanced.py export f3d --file "backup.f3d"
```

### 9. Undo/Redo & Checkpoints

Version control for designs:

```bash
# Undo/Redo
python3 file_client_enhanced.py undo undo --steps 3
python3 file_client_enhanced.py undo redo --steps 1

# Checkpoints
python3 file_client_enhanced.py undo checkpoint --name "before_fillet" \
  --description "State before adding fillets"
python3 file_client_enhanced.py undo list
python3 file_client_enhanced.py undo restore --name "before_fillet"
```

### 10. Analysis

Analyze geometry:

```bash
# Mass properties
python3 file_client_enhanced.py analyze mass

# Bounding box
python3 file_client_enhanced.py analyze bbox

# Specific bodies
python3 file_client_enhanced.py analyze mass --targets "Body1" "Body2"
```

### 11. Batch Operations

Execute multiple commands:

Create `batch.json`:
```json
[
  {"action": "clear"},
  {"action": "param", "sub_action": "set", "name": "width", "value": "100mm"},
  {"action": "direct_cylinders"},
  {"action": "view", "sub_action": "fit"},
  {"action": "export", "format": "step", "file_path": "result.step"}
]
```

Execute:
```bash
python3 file_client_enhanced.py batch --file batch.json
```

### 12. Configuration

Manage add-in settings:

```bash
# Get configuration
python3 file_client_enhanced.py config get

# Set configuration
python3 file_client_enhanced.py config set --units mm --debug true

# Reset to defaults
python3 file_client_enhanced.py config reset
```

## Advanced Examples

### Example 1: Parametric Box

```bash
# Set parameters
python3 file_client_enhanced.py param set --name width --value 100mm
python3 file_client_enhanced.py param set --name height --value 50mm
python3 file_client_enhanced.py param expression --name depth --expression "width/2"

# Create and export
python3 file_client_enhanced.py file --file box.json
python3 file_client_enhanced.py export step --file parametric_box.step
```

### Example 2: Assembly Automation

```bash
# Create base component
python3 file_client_enhanced.py component create --name "Base"
python3 file_client_enhanced.py component activate --name "Base"
python3 file_client_enhanced.py file --file base.json

# Create arm component
python3 file_client_enhanced.py component create --name "Arm"
python3 file_client_enhanced.py component activate --name "Arm"
python3 file_client_enhanced.py file --file arm.json

# Create joint
python3 file_client_enhanced.py joint create --type revolute \
  --comp1 "Base" --comp2 "Arm" --limits -90 90

# Animate joint
for angle in 0 30 60 90; do
  python3 file_client_enhanced.py joint drive --name "Joint1" --value $angle
  python3 file_client_enhanced.py view screenshot --file "frame_$angle.png"
done
```

### Example 3: Design Analysis Workflow

```bash
# Create design
python3 file_client_enhanced.py file --file design.json

# Analyze
python3 file_client_enhanced.py analyze mass
python3 file_client_enhanced.py analyze bbox

# Modify based on analysis
python3 file_client_enhanced.py param set --name thickness --value 5mm

# Re-analyze
python3 file_client_enhanced.py analyze mass

# Export if acceptable
python3 file_client_enhanced.py export step --file final_design.step
```

## Python API

You can also use the client programmatically:

```python
from triple_lindy_daemon.file_client_enhanced import send_command

# Set parameter
result = send_command({
    "action": "param",
    "sub_action": "set",
    "name": "width",
    "value": "100mm"
})

# Create checkpoint
result = send_command({
    "action": "undo",
    "sub_action": "checkpoint",
    "checkpoint_name": "iteration_1"
})

# Batch operations
result = send_command({
    "action": "batch",
    "commands": [
        {"action": "clear"},
        {"action": "direct_cylinders"},
        {"action": "view", "sub_action": "fit"}
    ]
})
```

## Troubleshooting

### Add-in not responding
1. Check if add-in is running in Fusion 360
2. Verify file permissions for `~/Documents/CSL/`
3. Check `live_status.json` for error messages

### Commands timing out
1. Increase timeout in configuration
2. Check if Fusion is busy processing
3. Try simpler commands first

### Selection not working
1. Ensure geometry exists
2. Use `query` to check current state
3. Try different filter combinations

## Performance Tips

1. **Use batch operations** for multiple commands
2. **Create checkpoints** before complex operations
3. **Use transactions** for atomic operations
4. **Cache material lists** (they don't change often)
5. **Minimize view updates** during batch operations

## Security

The add-in only accepts commands from local files. To enhance security:
1. Set appropriate file permissions
2. Use configuration to limit operations
3. Monitor command history

## Support

For issues or feature requests, please visit the GitHub repository.
