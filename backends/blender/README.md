# Blender Backend

## Overview
Open-source 3D creation suite with Python API (bpy) and Geometry Nodes. CSL integration for visualization, rendering, and procedural modeling.

## Quick Start

### Installation
1. Install Blender (3.0+ recommended)
2. Enable Python console: Window → Toggle System Console
3. Install as add-on or run scripts directly

### First Test
```python
import bpy
import bmesh

# Clear existing mesh objects
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Create mesh
mesh = bpy.data.meshes.new(name="CSL_Box")
obj = bpy.data.objects.new("CSL_Box", mesh)
bpy.context.collection.objects.link(obj)

# Create box using bmesh
bm = bmesh.new()
bmesh.ops.create_cube(bm, size=1)
bm.to_mesh(mesh)
bm.free()

# Set dimensions
obj.scale = (0.06, 0.06, 0.04)  # 60x60x40mm
```

## Architecture
- **Integration Method**: Python Add-on or Script
- **APIs**: 
  - bpy (Blender Python API)
  - bmesh (mesh editing)
  - Geometry Nodes (procedural)
- **Communication**: Direct Python or file-based
- **Unit System**: Blender Units (typically meters)

## Current Status
- [ ] Basic geometry creation
- [ ] Procedural modeling via Geometry Nodes
- [ ] Material assignment
- [ ] Rendering setup
- [ ] Animation support
- [ ] Export capabilities (STL, OBJ, etc.)

## Unique Capabilities for CSL
- **Visualization**: High-quality rendering
- **Animation**: Exploded views, assembly animations
- **Procedural**: Geometry Nodes for parametric modeling
- **Materials**: PBR materials and textures
- **Physics**: Simulation capabilities

## Geometry Nodes Integration
```python
# Create Geometry Nodes modifier for procedural modeling
def create_csl_geometry_nodes(obj):
    # Add Geometry Nodes modifier
    modifier = obj.modifiers.new("CSL_Geometry", 'NODES')
    
    # Create node group
    node_group = bpy.data.node_groups.new('CSL_Nodes', 'GeometryNodeTree')
    modifier.node_group = node_group
    
    # Add nodes
    input_node = node_group.nodes.new('NodeGroupInput')
    output_node = node_group.nodes.new('NodeGroupOutput')
    
    # Add CSL parameters as inputs
    node_group.inputs.new('NodeSocketFloat', 'Width')
    node_group.inputs.new('NodeSocketFloat', 'Height')
    node_group.inputs.new('NodeSocketFloat', 'Depth')
```

## Mesh Operations
```python
# Chamfer edges
def chamfer_edges(obj, width=0.002):  # 2mm chamfer
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.mesh.select_mode(type='EDGE')
    
    # Select edges programmatically
    bm = bmesh.from_edit_mesh(obj.data)
    for edge in bm.edges:
        if edge.verts[0].co.z > 0.039 and edge.verts[1].co.z > 0.039:  # Top edges
            edge.select = True
    
    bmesh.update_edit_mesh(obj.data)
    bpy.ops.mesh.bevel(offset=width, segments=1)
    bpy.ops.object.mode_set(mode='OBJECT')
```

## Add-on Structure
```python
bl_info = {
    "name": "CSL for Blender",
    "blender": (3, 0, 0),
    "category": "Object",
}

class CSL_OT_import(bpy.types.Operator):
    """Import CSL file"""
    bl_idname = "csl.import"
    bl_label = "Import CSL"
    
    def execute(self, context):
        # Parse CSL and create geometry
        return {'FINISHED'}

def register():
    bpy.utils.register_class(CSL_OT_import)

def unregister():
    bpy.utils.unregister_class(CSL_OT_import)
```

## Code Structure
```
blender/
├── __init__.py
├── blender_backend.py       # CSL to Blender translator
├── addon/
│   ├── __init__.py         # Add-on entry point
│   ├── operators.py        # Blender operators
│   └── panels.py           # UI panels
├── geometry_nodes/
│   ├── csl_nodes.py        # Procedural implementations
│   └── node_groups.blend   # Pre-made node setups
└── examples/
    ├── render_csl.py
    └── animation_test.py
```

## Resources
- [Blender Python API Documentation](https://docs.blender.org/api/current/)
- [BMesh Module](https://docs.blender.org/api/current/bmesh.html)
- [Geometry Nodes Manual](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/)
- [Blender Stack Exchange](https://blender.stackexchange.com/)

## TODO
- [ ] Implement CSL parser for Blender
- [ ] Create Geometry Nodes templates
- [ ] Add material library
- [ ] Implement assembly constraints
- [ ] Add rendering presets
- [ ] Create animation templates
- [ ] Test performance with complex models

## Notes for Implementation
- Blender uses right-handed Z-up coordinate system
- Consider using collections for organization
- Geometry Nodes offer true parametric capabilities
- Leverage modifiers for non-destructive workflow
- Use bmesh for complex mesh operations
- Consider viewport performance with high poly counts
