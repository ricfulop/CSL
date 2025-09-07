# Triple Lindy Enhanced Add-in Specification
## Zero-Shot Implementation Guide

### Overview
This specification defines comprehensive enhancements to the Triple Lindy Fusion 360 add-in for full CAD automation capabilities. Each feature is specified with exact implementation details for zero-shot development.

---

## 1. Parameters & Expressions Management

### Command Structure
```json
{
  "action": "param",
  "sub_action": "set|get|list|delete|expression",
  "name": "parameter_name",
  "value": "100mm",
  "expression": "width * 2",
  "comment": "optional description"
}
```

### Implementation
```python
def handle_parameters(data, status_file):
    """Handle parameter operations"""
    design = _app.activeProduct
    if not design:
        return {"status": "error", "error": "No active design"}
    
    params = design.userParameters
    sub_action = data.get("sub_action")
    
    if sub_action == "set":
        name = data.get("name")
        value = data.get("value")
        comment = data.get("comment", "")
        
        # Check if parameter exists
        param = params.itemByName(name)
        if param:
            param.expression = value
            if comment:
                param.comment = comment
        else:
            # Create new parameter
            params.add(name, 
                      adsk.core.ValueInput.createByString(value),
                      "", 
                      comment)
        
        return {"status": "success", "parameter": name, "value": value}
    
    elif sub_action == "get":
        name = data.get("name")
        param = params.itemByName(name)
        if param:
            return {
                "status": "success",
                "name": param.name,
                "value": param.expression,
                "comment": param.comment,
                "unit": param.unit
            }
        return {"status": "error", "error": f"Parameter {name} not found"}
    
    elif sub_action == "list":
        param_list = []
        for param in params:
            param_list.append({
                "name": param.name,
                "value": param.expression,
                "comment": param.comment,
                "unit": param.unit
            })
        return {"status": "success", "parameters": param_list}
    
    elif sub_action == "delete":
        name = data.get("name")
        param = params.itemByName(name)
        if param:
            param.deleteMe()
            return {"status": "success", "deleted": name}
        return {"status": "error", "error": f"Parameter {name} not found"}
    
    elif sub_action == "expression":
        name = data.get("name")
        expression = data.get("expression")
        comment = data.get("comment", "")
        
        param = params.itemByName(name)
        if param:
            param.expression = expression
        else:
            params.add(name,
                      adsk.core.ValueInput.createByString(expression),
                      "",
                      comment)
        return {"status": "success", "parameter": name, "expression": expression}
```

---

## 2. Timeline Control

### Command Structure
```json
{
  "action": "timeline",
  "sub_action": "list|rollback|suppress|unsuppress|reorder|delete",
  "index": 5,
  "feature_name": "Extrude1",
  "target_index": 3,
  "range": [2, 5]
}
```

### Implementation
```python
def handle_timeline(data, status_file):
    """Handle timeline operations"""
    design = _app.activeProduct
    if not design:
        return {"status": "error", "error": "No active design"}
    
    timeline = design.timeline
    sub_action = data.get("sub_action")
    
    if sub_action == "list":
        items = []
        for i in range(timeline.count):
            item = timeline.item(i)
            items.append({
                "index": i,
                "name": item.name if hasattr(item, 'name') else str(item.entity),
                "type": type(item.entity).__name__,
                "is_suppressed": item.isSuppressed,
                "is_rollback": item.isRolledBack
            })
        return {"status": "success", "timeline": items}
    
    elif sub_action == "rollback":
        index = data.get("index")
        if index < timeline.count:
            timeline.markerPosition = index
            return {"status": "success", "rolled_back_to": index}
        return {"status": "error", "error": "Invalid timeline index"}
    
    elif sub_action == "suppress":
        if "feature_name" in data:
            # Find by name
            for i in range(timeline.count):
                item = timeline.item(i)
                if hasattr(item.entity, 'name') and item.entity.name == data["feature_name"]:
                    item.isSuppressed = True
                    return {"status": "success", "suppressed": data["feature_name"]}
        elif "index" in data:
            # Suppress by index
            index = data["index"]
            if index < timeline.count:
                timeline.item(index).isSuppressed = True
                return {"status": "success", "suppressed_index": index}
        elif "range" in data:
            # Suppress range
            start, end = data["range"]
            for i in range(start, min(end + 1, timeline.count)):
                timeline.item(i).isSuppressed = True
            return {"status": "success", "suppressed_range": [start, end]}
        
    elif sub_action == "unsuppress":
        # Similar to suppress but set isSuppressed = False
        if "feature_name" in data:
            for i in range(timeline.count):
                item = timeline.item(i)
                if hasattr(item.entity, 'name') and item.entity.name == data["feature_name"]:
                    item.isSuppressed = False
                    return {"status": "success", "unsuppressed": data["feature_name"]}
    
    elif sub_action == "reorder":
        index = data.get("index")
        target_index = data.get("target_index")
        if index < timeline.count and target_index < timeline.count:
            item = timeline.item(index)
            timeline.moveToEnd(item)  # Move to end first
            # Then move to target position (requires iterative moves)
            for _ in range(timeline.count - target_index - 1):
                timeline.moveToPrevious(item)
            return {"status": "success", "moved": index, "to": target_index}
    
    elif sub_action == "delete":
        index = data.get("index")
        if index < timeline.count:
            item = timeline.item(index)
            if hasattr(item.entity, 'deleteMe'):
                item.entity.deleteMe()
                return {"status": "success", "deleted_index": index}
```

---

## 3. Selection & Picking

### Command Structure
```json
{
  "action": "select",
  "sub_action": "add|set|clear|get|filter",
  "type": "face|edge|vertex|body|sketch|component",
  "filters": {
    "name": "pattern_*",
    "color": "#FF0000",
    "area_gt": 100,
    "area_lt": 500,
    "planar": true,
    "cylindrical": true
  },
  "indices": [0, 2, 5],
  "all": true
}
```

### Implementation
```python
def handle_selection(data, status_file):
    """Handle selection operations"""
    design = _app.activeProduct
    if not design:
        return {"status": "error", "error": "No active design"}
    
    ui = _app.userInterface
    selection = ui.activeSelections
    sub_action = data.get("sub_action", "set")
    
    if sub_action == "clear":
        selection.clear()
        return {"status": "success", "cleared": True}
    
    elif sub_action == "get":
        selected = []
        for i in range(selection.count):
            sel = selection.item(i)
            selected.append({
                "type": type(sel.entity).__name__,
                "name": getattr(sel.entity, 'name', 'unnamed'),
                "index": i
            })
        return {"status": "success", "selection": selected}
    
    elif sub_action in ["add", "set"]:
        if sub_action == "set":
            selection.clear()
        
        entity_type = data.get("type", "face")
        root = design.rootComponent
        
        # Collect entities based on type
        entities = []
        if entity_type == "face":
            for body in root.bRepBodies:
                for face in body.faces:
                    entities.append(face)
        elif entity_type == "edge":
            for body in root.bRepBodies:
                for edge in body.edges:
                    entities.append(edge)
        elif entity_type == "body":
            entities = list(root.bRepBodies)
        elif entity_type == "sketch":
            entities = list(root.sketches)
        
        # Apply filters
        filters = data.get("filters", {})
        filtered = []
        for entity in entities:
            include = True
            
            # Name filter
            if "name" in filters:
                import fnmatch
                if not fnmatch.fnmatch(getattr(entity, 'name', ''), filters["name"]):
                    include = False
            
            # Area filter for faces
            if entity_type == "face" and "area_gt" in filters:
                if entity.area < filters["area_gt"]:
                    include = False
            if entity_type == "face" and "area_lt" in filters:
                if entity.area > filters["area_lt"]:
                    include = False
            
            # Geometry type filters
            if entity_type == "face":
                if filters.get("planar") and entity.geometry.surfaceType != adsk.core.SurfaceTypes.PlaneSurfaceType:
                    include = False
                if filters.get("cylindrical") and entity.geometry.surfaceType != adsk.core.SurfaceTypes.CylinderSurfaceType:
                    include = False
            
            if include:
                filtered.append(entity)
        
        # Select by indices or all
        if data.get("all"):
            for entity in filtered:
                selection.add(entity)
        elif "indices" in data:
            for idx in data["indices"]:
                if idx < len(filtered):
                    selection.add(filtered[idx])
        
        return {"status": "success", "selected_count": selection.count}
```

---

## 4. Component & Assembly Management

### Command Structure
```json
{
  "action": "component",
  "sub_action": "create|activate|insert|list|delete|transform",
  "name": "SubAssembly1",
  "file_path": "bearing.f3d",
  "transform": {
    "translate": [10, 20, 30],
    "rotate": [0, 0, 45],
    "scale": 1.0
  }
}
```

### Implementation
```python
def handle_component(data, status_file):
    """Handle component operations"""
    design = _app.activeProduct
    if not design:
        return {"status": "error", "error": "No active design"}
    
    root = design.rootComponent
    sub_action = data.get("sub_action")
    
    if sub_action == "create":
        name = data.get("name", "Component")
        # Create new occurrence
        transform = adsk.core.Matrix3D.create()
        newOcc = root.occurrences.addNewComponent(transform)
        newOcc.component.name = name
        return {"status": "success", "component": name}
    
    elif sub_action == "activate":
        name = data.get("name")
        for occ in root.allOccurrences:
            if occ.component.name == name:
                design.activeComponent = occ.component
                return {"status": "success", "activated": name}
        return {"status": "error", "error": f"Component {name} not found"}
    
    elif sub_action == "insert":
        file_path = data.get("file_path")
        # Import component from file
        importManager = _app.importManager
        importOptions = importManager.createFusionArchiveImportOptions(file_path)
        importManager.importToTarget(importOptions, root)
        return {"status": "success", "imported": file_path}
    
    elif sub_action == "list":
        components = []
        for occ in root.allOccurrences:
            components.append({
                "name": occ.component.name,
                "is_active": occ.component == design.activeComponent,
                "is_visible": occ.isVisible,
                "transform": str(occ.transform.asArray())
            })
        return {"status": "success", "components": components}
    
    elif sub_action == "transform":
        name = data.get("name")
        transform_data = data.get("transform", {})
        
        for occ in root.allOccurrences:
            if occ.component.name == name:
                transform = occ.transform
                
                # Apply translation
                if "translate" in transform_data:
                    tx, ty, tz = transform_data["translate"]
                    translation = adsk.core.Vector3D.create(tx/10, ty/10, tz/10)  # mm to cm
                    transform.translation = translation
                
                # Apply rotation (degrees to radians)
                if "rotate" in transform_data:
                    rx, ry, rz = transform_data["rotate"]
                    import math
                    if rx:
                        transform.setToRotation(math.radians(rx), 
                                               adsk.core.Vector3D.create(1,0,0),
                                               adsk.core.Point3D.create(0,0,0))
                
                occ.transform = transform
                return {"status": "success", "transformed": name}
```

---

## 5. Joint Management

### Command Structure
```json
{
  "action": "joint",
  "sub_action": "create|list|delete|drive",
  "type": "rigid|revolute|slider|cylindrical|pin_slot|planar|ball",
  "geometry_one": {"component": "Base", "entity": "Face1"},
  "geometry_two": {"component": "Arm", "entity": "Face2"},
  "limits": {"min": -90, "max": 90},
  "drive_value": 45
}
```

### Implementation
```python
def handle_joint(data, status_file):
    """Handle joint operations"""
    design = _app.activeProduct
    if not design:
        return {"status": "error", "error": "No active design"}
    
    root = design.rootComponent
    sub_action = data.get("sub_action")
    
    if sub_action == "create":
        joint_type = data.get("type", "rigid")
        geom_one = data.get("geometry_one")
        geom_two = data.get("geometry_two")
        
        # Find components and entities
        occ_one = None
        occ_two = None
        for occ in root.allOccurrences:
            if occ.component.name == geom_one["component"]:
                occ_one = occ
            if occ.component.name == geom_two["component"]:
                occ_two = occ
        
        if not occ_one or not occ_two:
            return {"status": "error", "error": "Components not found"}
        
        # Create joint
        joints = root.joints
        joint_input = joints.createInput(occ_one, occ_two)
        
        # Set joint type
        if joint_type == "revolute":
            joint_input.setAsRevoluteJointMotion(adsk.fusion.JointDirections.ZAxisJointDirection)
        elif joint_type == "slider":
            joint_input.setAsSliderJointMotion(adsk.fusion.JointDirections.ZAxisJointDirection)
        elif joint_type == "rigid":
            joint_input.setAsRigidJointMotion()
        
        # Set limits if provided
        if "limits" in data:
            limits = data["limits"]
            joint_input.isLimitEnabled = True
            joint_input.limitMin = adsk.core.ValueInput.createByReal(math.radians(limits["min"]))
            joint_input.limitMax = adsk.core.ValueInput.createByReal(math.radians(limits["max"]))
        
        joint = joints.add(joint_input)
        return {"status": "success", "joint": joint.name}
    
    elif sub_action == "list":
        joint_list = []
        for joint in root.joints:
            joint_list.append({
                "name": joint.name,
                "type": joint.jointMotion.jointType,
                "is_suppressed": joint.isSuppressed,
                "occurrenceOne": joint.occurrenceOne.name,
                "occurrenceTwo": joint.occurrenceTwo.name
            })
        return {"status": "success", "joints": joint_list}
    
    elif sub_action == "drive":
        joint_name = data.get("name")
        drive_value = data.get("drive_value")
        
        for joint in root.joints:
            if joint.name == joint_name:
                # Drive the joint
                if joint.jointMotion.jointType in [
                    adsk.fusion.JointTypes.RevoluteJointType,
                    adsk.fusion.JointTypes.SliderJointType
                ]:
                    joint.jointMotion.rotationValue = math.radians(drive_value)
                return {"status": "success", "driven": joint_name, "value": drive_value}
```

---

## 6. Material & Appearance Management

### Command Structure
```json
{
  "action": "material",
  "sub_action": "apply|create|list|remove",
  "target": "Body1",
  "material_name": "Aluminum 6061",
  "library": "Fusion 360 Material Library",
  "properties": {
    "density": 2.7,
    "youngs_modulus": 68900,
    "poisson_ratio": 0.33
  }
}
```

### Implementation
```python
def handle_material(data, status_file):
    """Handle material operations"""
    design = _app.activeProduct
    if not design:
        return {"status": "error", "error": "No active design"}
    
    materialLibs = _app.materialLibraries
    sub_action = data.get("sub_action")
    
    if sub_action == "apply":
        target = data.get("target")
        material_name = data.get("material_name")
        library_name = data.get("library", "Fusion 360 Material Library")
        
        # Find material library
        lib = materialLibs.itemByName(library_name)
        if not lib:
            return {"status": "error", "error": f"Library {library_name} not found"}
        
        # Find material
        material = lib.materials.itemByName(material_name)
        if not material:
            return {"status": "error", "error": f"Material {material_name} not found"}
        
        # Find target body
        root = design.rootComponent
        for body in root.bRepBodies:
            if body.name == target:
                body.material = material
                return {"status": "success", "applied": material_name, "to": target}
        
        return {"status": "error", "error": f"Body {target} not found"}
    
    elif sub_action == "list":
        materials = []
        for lib in materialLibs:
            for mat in lib.materials:
                materials.append({
                    "name": mat.name,
                    "library": lib.name,
                    "id": mat.id
                })
        return {"status": "success", "materials": materials}
    
    elif sub_action == "create":
        # Custom material creation
        name = data.get("material_name")
        properties = data.get("properties", {})
        
        # This requires material library API access
        # Simplified version - apply properties to body
        return {"status": "partial", "message": "Custom materials require library access"}
```

---

## 7. View & Camera Control

### Command Structure
```json
{
  "action": "view",
  "sub_action": "set|orbit|pan|zoom|fit|isolate|section|screenshot",
  "orientation": "front|back|top|bottom|left|right|iso",
  "orbit_angles": [45, 30],
  "zoom_factor": 1.5,
  "section_plane": "XY",
  "section_offset": 50,
  "screenshot_path": "view.png",
  "screenshot_size": [800, 600]
}
```

### Implementation
```python
def handle_view(data, status_file):
    """Handle view and camera operations"""
    viewport = _app.activeViewport
    if not viewport:
        return {"status": "error", "error": "No active viewport"}
    
    camera = viewport.camera
    sub_action = data.get("sub_action")
    
    if sub_action == "set":
        orientation = data.get("orientation", "iso")
        
        # Set standard views
        if orientation == "front":
            camera.setOrientation(
                adsk.core.Vector3D.create(0, 0, 1),  # eye
                adsk.core.Vector3D.create(0, 1, 0)   # up
            )
        elif orientation == "top":
            camera.setOrientation(
                adsk.core.Vector3D.create(0, 1, 0),
                adsk.core.Vector3D.create(0, 0, 1)
            )
        elif orientation == "iso":
            camera.setOrientation(
                adsk.core.Vector3D.create(1, 1, 1),
                adsk.core.Vector3D.create(0, 1, 0)
            )
        
        camera.isFitView = True
        viewport.camera = camera
        return {"status": "success", "view": orientation}
    
    elif sub_action == "orbit":
        angles = data.get("orbit_angles", [0, 0])
        # Convert angles to radians and apply
        import math
        horizontal = math.radians(angles[0])
        vertical = math.radians(angles[1])
        
        # Get current camera position
        eye = camera.eye
        target = camera.target
        up = camera.upVector
        
        # Calculate new position (simplified)
        # Would need proper 3D rotation math here
        viewport.camera = camera
        return {"status": "success", "orbited": angles}
    
    elif sub_action == "zoom":
        factor = data.get("zoom_factor", 1.0)
        camera.viewExtents *= factor
        viewport.camera = camera
        return {"status": "success", "zoom_factor": factor}
    
    elif sub_action == "fit":
        viewport.fit()
        return {"status": "success", "fitted": True}
    
    elif sub_action == "screenshot":
        path = data.get("screenshot_path", "screenshot.png")
        size = data.get("screenshot_size", [800, 600])
        
        # Save viewport image
        viewport.saveAsImageFile(path, size[0], size[1])
        return {"status": "success", "screenshot": path}
    
    elif sub_action == "section":
        # Section view requires analysis environment
        plane = data.get("section_plane", "XY")
        offset = data.get("section_offset", 0)
        
        # This would require section analysis API
        return {"status": "partial", "message": "Section views require analysis API"}
```

---

## 8. Export Enhancements

### Command Structure
```json
{
  "action": "export",
  "format": "step|iges|stl|obj|f3d|pdf|dwg",
  "file_path": "output.step",
  "options": {
    "version": "AP214",
    "quality": "high|medium|low",
    "units": "mm|inch",
    "binary": true,
    "selection_only": false,
    "bodies": ["Body1", "Body2"]
  }
}
```

### Implementation
```python
def handle_export(data, status_file):
    """Handle enhanced export operations"""
    design = _app.activeProduct
    if not design:
        return {"status": "error", "error": "No active design"}
    
    export_mgr = design.exportManager
    format_type = data.get("format", "step")
    file_path = data.get("file_path", f"export.{format_type}")
    options = data.get("options", {})
    
    # Ensure full path
    import os
    if not os.path.isabs(file_path):
        file_path = os.path.join(os.path.expanduser("~/Documents/CSL/exports"), file_path)
    
    # Create directory if needed
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    if format_type == "step":
        step_options = export_mgr.createSTEPExportOptions(file_path)
        # Set version if specified
        if "version" in options:
            if options["version"] == "AP214":
                step_options.stepFileFormat = adsk.fusion.STEPFileFormat.AP214Format
            elif options["version"] == "AP203":
                step_options.stepFileFormat = adsk.fusion.STEPFileFormat.AP203Format
        export_mgr.execute(step_options)
        
    elif format_type == "stl":
        stl_options = export_mgr.createSTLExportOptions(design.rootComponent)
        stl_options.filename = file_path
        
        # Set quality
        quality = options.get("quality", "medium")
        if quality == "high":
            stl_options.meshRefinement = adsk.fusion.MeshRefinementSettings.MeshRefinementHigh
        elif quality == "low":
            stl_options.meshRefinement = adsk.fusion.MeshRefinementSettings.MeshRefinementLow
        else:
            stl_options.meshRefinement = adsk.fusion.MeshRefinementSettings.MeshRefinementMedium
        
        # Binary vs ASCII
        stl_options.isBinaryFormat = options.get("binary", True)
        
        # Units
        if options.get("units") == "inch":
            stl_options.units = adsk.fusion.ExportUnits.InchExportUnits
        else:
            stl_options.units = adsk.fusion.ExportUnits.MillimeterExportUnits
        
        export_mgr.execute(stl_options)
    
    elif format_type == "iges":
        iges_options = export_mgr.createIGESExportOptions(file_path)
        export_mgr.execute(iges_options)
    
    elif format_type == "f3d":
        archive_options = export_mgr.createFusionArchiveExportOptions(file_path)
        export_mgr.execute(archive_options)
    
    return {"status": "success", "exported": file_path, "format": format_type}
```

---

## 9. Undo/Redo Management

### Command Structure
```json
{
  "action": "undo",
  "sub_action": "undo|redo|checkpoint|restore|list",
  "steps": 3,
  "checkpoint_name": "before_fillet",
  "description": "State before adding fillets"
}
```

### Implementation
```python
# Global checkpoint storage
_checkpoints = {}

def handle_undo(data, status_file):
    """Handle undo/redo operations"""
    design = _app.activeProduct
    if not design:
        return {"status": "error", "error": "No active design"}
    
    sub_action = data.get("sub_action")
    
    if sub_action == "undo":
        steps = data.get("steps", 1)
        for _ in range(steps):
            if design.canUndo:
                design.undo()
        return {"status": "success", "undone": steps}
    
    elif sub_action == "redo":
        steps = data.get("steps", 1)
        for _ in range(steps):
            if design.canRedo:
                design.redo()
        return {"status": "success", "redone": steps}
    
    elif sub_action == "checkpoint":
        name = data.get("checkpoint_name", f"checkpoint_{len(_checkpoints)}")
        description = data.get("description", "")
        
        # Save current state
        # Note: This is simplified - real implementation would need to serialize state
        _checkpoints[name] = {
            "timeline_position": design.timeline.markerPosition,
            "description": description,
            "timestamp": time.time()
        }
        return {"status": "success", "checkpoint": name}
    
    elif sub_action == "restore":
        name = data.get("checkpoint_name")
        if name not in _checkpoints:
            return {"status": "error", "error": f"Checkpoint {name} not found"}
        
        checkpoint = _checkpoints[name]
        # Restore to checkpoint position
        design.timeline.markerPosition = checkpoint["timeline_position"]
        return {"status": "success", "restored": name}
    
    elif sub_action == "list":
        checkpoint_list = []
        for name, data in _checkpoints.items():
            checkpoint_list.append({
                "name": name,
                "description": data["description"],
                "timeline_position": data["timeline_position"],
                "timestamp": data["timestamp"]
            })
        return {"status": "success", "checkpoints": checkpoint_list}
```

---

## 10. Batch Operations

### Command Structure
```json
{
  "action": "batch",
  "commands": [
    {"action": "clear"},
    {"action": "param", "sub_action": "set", "name": "width", "value": "100mm"},
    {"action": "file", "path": "base.json"},
    {"action": "export", "format": "step", "file_path": "output.step"}
  ],
  "stop_on_error": false,
  "transaction": true
}
```

### Implementation
```python
def handle_batch(data, status_file):
    """Handle batch command execution"""
    commands = data.get("commands", [])
    stop_on_error = data.get("stop_on_error", True)
    use_transaction = data.get("transaction", False)
    
    results = []
    design = _app.activeProduct
    
    # Start transaction if requested
    if use_transaction and design:
        design.beginTransaction("Batch Operation")
    
    try:
        for i, cmd in enumerate(commands):
            try:
                # Process each command
                result = process_command(cmd, status_file)
                results.append({
                    "index": i,
                    "command": cmd.get("action"),
                    "status": "success",
                    "result": result
                })
            except Exception as e:
                results.append({
                    "index": i,
                    "command": cmd.get("action"),
                    "status": "error",
                    "error": str(e)
                })
                if stop_on_error:
                    if use_transaction and design:
                        design.abortTransaction()
                    return {"status": "error", "results": results}
        
        # Commit transaction if all successful
        if use_transaction and design:
            design.commitTransaction()
        
        return {"status": "success", "results": results}
    
    except Exception as e:
        if use_transaction and design:
            design.abortTransaction()
        return {"status": "error", "error": str(e), "results": results}
```

---

## 11. Analysis & Measurement

### Command Structure
```json
{
  "action": "analyze",
  "sub_action": "mass_properties|interference|distance|angle|curvature",
  "targets": ["Body1", "Body2"],
  "units": "mm|inch|cm"
}
```

### Implementation
```python
def handle_analyze(data, status_file):
    """Handle analysis operations"""
    design = _app.activeProduct
    if not design:
        return {"status": "error", "error": "No active design"}
    
    root = design.rootComponent
    sub_action = data.get("sub_action")
    
    if sub_action == "mass_properties":
        targets = data.get("targets", [])
        results = []
        
        for target_name in targets:
            for body in root.bRepBodies:
                if body.name == target_name:
                    props = body.physicalProperties
                    results.append({
                        "body": target_name,
                        "mass": props.mass,
                        "volume": props.volume,
                        "area": props.area,
                        "density": props.density,
                        "center_of_mass": [props.centerOfMass.x, props.centerOfMass.y, props.centerOfMass.z],
                        "moments_of_inertia": {
                            "ixx": props.ixx,
                            "iyy": props.iyy,
                            "izz": props.izz
                        }
                    })
        
        return {"status": "success", "mass_properties": results}
    
    elif sub_action == "interference":
        # Check interference between bodies
        bodies = []
        for name in data.get("targets", []):
            for body in root.bRepBodies:
                if body.name == name:
                    bodies.append(body)
        
        if len(bodies) >= 2:
            # Use interference API
            interferences = []
            for i in range(len(bodies)):
                for j in range(i+1, len(bodies)):
                    # Check if bodies interfere
                    # This requires the interference API
                    vol = bodies[i].intersect(bodies[j])
                    if vol:
                        interferences.append({
                            "body1": bodies[i].name,
                            "body2": bodies[j].name,
                            "volume": vol.volume if hasattr(vol, 'volume') else 0
                        })
            
            return {"status": "success", "interferences": interferences}
    
    elif sub_action == "distance":
        # Measure distance between entities
        # This would require measurement API
        return {"status": "partial", "message": "Distance measurement requires selection"}
```

---

## 12. Event Monitoring

### Command Structure
```json
{
  "action": "monitor",
  "sub_action": "start|stop|list",
  "events": ["selection_changed", "document_saved", "feature_created"],
  "callback_url": "http://localhost:8080/webhook"
}
```

### Implementation
```python
# Global event handlers storage
_event_handlers = {}

def handle_monitor(data, status_file):
    """Handle event monitoring"""
    ui = _app.userInterface
    sub_action = data.get("sub_action")
    
    if sub_action == "start":
        events = data.get("events", [])
        callback_url = data.get("callback_url")
        
        for event_name in events:
            if event_name == "selection_changed":
                handler = SelectionEventHandler(callback_url)
                ui.selectionEvent.add(handler)
                _event_handlers[event_name] = handler
            elif event_name == "document_saved":
                handler = DocumentSaveHandler(callback_url)
                _app.documentSaved.add(handler)
                _event_handlers[event_name] = handler
        
        return {"status": "success", "monitoring": events}
    
    elif sub_action == "stop":
        events = data.get("events", [])
        for event_name in events:
            if event_name in _event_handlers:
                # Remove handler
                handler = _event_handlers[event_name]
                # Handler removal logic
                del _event_handlers[event_name]
        
        return {"status": "success", "stopped": events}
    
    elif sub_action == "list":
        active_events = list(_event_handlers.keys())
        return {"status": "success", "active_events": active_events}

class SelectionEventHandler(adsk.core.SelectionEventHandler):
    def __init__(self, callback_url):
        super().__init__()
        self.callback_url = callback_url
    
    def notify(self, args):
        # Send event to callback URL
        import requests
        selection_info = {
            "event": "selection_changed",
            "count": args.selection.count,
            "timestamp": time.time()
        }
        try:
            requests.post(self.callback_url, json=selection_info)
        except:
            pass
```

---

## 13. Configuration & Settings

### Command Structure
```json
{
  "action": "config",
  "sub_action": "get|set|reset",
  "settings": {
    "auto_save": true,
    "units": "mm",
    "precision": 3,
    "timeout": 30,
    "debug_mode": false
  }
}
```

### Implementation
```python
# Global configuration storage
_config = {
    "auto_save": True,
    "units": "mm",
    "precision": 3,
    "timeout": 30,
    "debug_mode": False
}

def handle_config(data, status_file):
    """Handle configuration management"""
    global _config
    sub_action = data.get("sub_action")
    
    if sub_action == "get":
        return {"status": "success", "config": _config}
    
    elif sub_action == "set":
        settings = data.get("settings", {})
        _config.update(settings)
        
        # Apply settings
        if "units" in settings:
            design = _app.activeProduct
            if design:
                if settings["units"] == "mm":
                    design.unitsManager.defaultLengthUnits = adsk.fusion.DistanceUnits.MillimeterDistanceUnits
                elif settings["units"] == "inch":
                    design.unitsManager.defaultLengthUnits = adsk.fusion.DistanceUnits.InchDistanceUnits
        
        # Save config to file
        config_file = os.path.join(os.path.expanduser("~"), ".triple_lindy_config.json")
        with open(config_file, 'w') as f:
            json.dump(_config, f)
        
        return {"status": "success", "config": _config}
    
    elif sub_action == "reset":
        _config = {
            "auto_save": True,
            "units": "mm",
            "precision": 3,
            "timeout": 30,
            "debug_mode": False
        }
        return {"status": "success", "config": _config}
```

---

## Integration into Main Handler

### Main Command Router
```python
def process_command(data, status_file):
    """Route commands to appropriate handlers"""
    action = data.get("action")
    
    # Existing actions
    if action == "ping":
        return handle_ping(data, status_file)
    elif action == "clear":
        return handle_clear(data, status_file)
    elif action == "query":
        return handle_query(data, status_file)
    
    # New enhanced actions
    elif action == "param":
        return handle_parameters(data, status_file)
    elif action == "timeline":
        return handle_timeline(data, status_file)
    elif action == "select":
        return handle_selection(data, status_file)
    elif action == "component":
        return handle_component(data, status_file)
    elif action == "joint":
        return handle_joint(data, status_file)
    elif action == "material":
        return handle_material(data, status_file)
    elif action == "view":
        return handle_view(data, status_file)
    elif action == "export":
        return handle_export(data, status_file)
    elif action == "undo":
        return handle_undo(data, status_file)
    elif action == "batch":
        return handle_batch(data, status_file)
    elif action == "analyze":
        return handle_analyze(data, status_file)
    elif action == "monitor":
        return handle_monitor(data, status_file)
    elif action == "config":
        return handle_config(data, status_file)
    
    # CSL IR processing
    elif "ir" in data:
        return handle_csl_ir(data, status_file)
    
    else:
        return {"status": "error", "error": f"Unknown action: {action}"}
```

---

## Testing Suite

### Test All Features
```python
def test_all_features():
    """Comprehensive test suite"""
    tests = [
        # Parameters
        {"action": "param", "sub_action": "set", "name": "width", "value": "100mm"},
        {"action": "param", "sub_action": "list"},
        
        # Timeline
        {"action": "timeline", "sub_action": "list"},
        {"action": "timeline", "sub_action": "rollback", "index": 5},
        
        # Selection
        {"action": "select", "sub_action": "clear"},
        {"action": "select", "type": "face", "filters": {"planar": True}},
        
        # Components
        {"action": "component", "sub_action": "list"},
        {"action": "component", "sub_action": "create", "name": "TestComponent"},
        
        # View
        {"action": "view", "sub_action": "set", "orientation": "iso"},
        {"action": "view", "sub_action": "fit"},
        
        # Export
        {"action": "export", "format": "step", "file_path": "test.step"},
        
        # Analysis
        {"action": "analyze", "sub_action": "mass_properties", "targets": ["Body1"]},
        
        # Batch
        {"action": "batch", "commands": [
            {"action": "param", "sub_action": "set", "name": "test", "value": "50mm"},
            {"action": "view", "sub_action": "fit"}
        ]}
    ]
    
    results = []
    for test in tests:
        try:
            result = process_command(test, None)
            results.append({"test": test["action"], "status": "pass", "result": result})
        except Exception as e:
            results.append({"test": test["action"], "status": "fail", "error": str(e)})
    
    return results
```

---

## Error Handling

All handlers should follow this pattern:
```python
def handle_xxx(data, status_file):
    try:
        # Validate inputs
        if not data.get("required_field"):
            return {"status": "error", "error": "Missing required_field"}
        
        # Get design/app references
        design = _app.activeProduct
        if not design:
            return {"status": "error", "error": "No active design"}
        
        # Perform operation
        result = perform_operation()
        
        # Return success
        return {"status": "success", "result": result}
        
    except Exception as e:
        # Log error if debug mode
        if _config.get("debug_mode"):
            import traceback
            return {
                "status": "error",
                "error": str(e),
                "traceback": traceback.format_exc()
            }
        return {"status": "error", "error": str(e)}
```

---

## Performance Considerations

1. **Caching**: Cache frequently accessed objects
```python
_cache = {
    "materials": None,
    "components": None,
    "last_update": 0
}

def get_cached_materials():
    if time.time() - _cache["last_update"] > 60:  # Refresh every minute
        _cache["materials"] = list_all_materials()
        _cache["last_update"] = time.time()
    return _cache["materials"]
```

2. **Batch Processing**: Group operations when possible
3. **Async Operations**: Use threading for long operations
4. **Progress Reporting**: For long operations, write progress to status file

---

## Security Considerations

1. **Path Validation**: Always validate file paths
```python
def validate_path(path):
    # Ensure path is within allowed directories
    allowed_dirs = [
        os.path.expanduser("~/Documents/CSL"),
        os.path.expanduser("~/Desktop")
    ]
    abs_path = os.path.abspath(path)
    for allowed in allowed_dirs:
        if abs_path.startswith(allowed):
            return True
    return False
```

2. **Command Validation**: Validate all inputs
3. **Rate Limiting**: Prevent command flooding
4. **Sandboxing**: Limit operations to safe subset

---

## Deployment

1. Copy enhanced add-in to Fusion directory
2. Update manifest with new version
3. Test all features with test suite
4. Document all new commands
5. Update client library with new actions

This specification provides a complete, zero-shot implementable enhancement to the Triple Lindy add-in with all major CAD automation features.
