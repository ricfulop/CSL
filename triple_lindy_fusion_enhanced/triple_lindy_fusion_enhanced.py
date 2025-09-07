"""
Triple Lindy Enhanced - Complete CAD Automation Add-in for Fusion 360
Version: 2.0.0

Features:
- Parameters & Expressions
- Timeline Control
- Selection & Picking
- Component & Assembly Management
- Joint Management
- Materials & Appearance
- View & Camera Control
- Export Enhancements
- Undo/Redo with Checkpoints
- Batch Operations
- Analysis & Measurement
- Event Monitoring
- Configuration Management
"""

import adsk.core
import adsk.fusion
import json
import time
import os
import math
import traceback
import threading
from pathlib import Path
# Note: typing might not be available in older Fusion Python
try:
    from typing import Dict, List, Any, Optional
except ImportError:
    # Fallback for older Python versions
    Dict = dict
    List = list
    Any = object
    Optional = object

# Global variables
_app = None  # adsk.core.Application
_ui = None   # adsk.core.UserInterface
_running = False
_checkpoints = {}
_event_handlers = {}
_cache = {"materials": None, "components": None, "last_update": 0}
_config = {
    "auto_save": True,
    "units": "mm",
    "precision": 3,
    "timeout": 30,
    "debug_mode": False
}

def run(context):
    """Entry point for the add-in"""
    global _app, _ui, _running
    try:
        _app = adsk.core.Application.get()
        _ui = _app.userInterface
        
        # Test imports first
        try:
            test_imports()
        except Exception as e:
            _ui.messageBox(f"Import error: {str(e)}\n\nThis might be a Python version issue.")
            return
        
        # Load configuration
        try:
            load_config()
        except Exception as e:
            _ui.messageBox(f"Config error: {str(e)}\n\nUsing defaults.")
        
        # Start file watcher in a separate thread
        _running = True
        try:
            watcher_thread = threading.Thread(target=watch_for_commands, daemon=True)
            watcher_thread.start()
        except Exception as e:
            _ui.messageBox(f"Threading error: {str(e)}\n\n{traceback.format_exc()}")
            return
        
        _ui.messageBox("Triple Lindy Enhanced v2.0.0 started!\nWatching for commands...")
        
    except Exception as e:
        if _ui:
            _ui.messageBox(f"Failed to start: {str(e)}\n\nDetails:\n{traceback.format_exc()}")
        else:
            print(f"Failed to start (no UI): {str(e)}\n\n{traceback.format_exc()}")

def stop(context):
    """Clean up when add-in stops"""
    global _running
    _running = False

def test_imports():
    """Test that all required imports work"""
    import json
    import time
    import os
    import math
    import threading
    from pathlib import Path
    # If we get here, all imports work
    return True

def load_config():
    """Load configuration from file"""
    global _config
    config_file = os.path.join(os.path.expanduser("~"), ".triple_lindy_config.json")
    if os.path.exists(config_file):
        try:
            with open(config_file, 'r') as f:
                _config.update(json.load(f))
        except:
            pass

# ============================================================================
# PARAMETER MANAGEMENT
# ============================================================================

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
        
        if not name or not value:
            return {"status": "error", "error": "Name and value required"}
        
        # Check if parameter exists
        param = params.itemByName(name)
        
        # Convert value to string with units if needed
        value_str = str(value)
        units = data.get("units", "")
        if units and not any(u in value_str for u in ["mm", "cm", "in", "deg"]):
            value_str = f"{value_str} {units}"
        
        if param:
            param.expression = value_str
            if comment:
                param.comment = comment
        else:
            # Create new parameter
            params.add(name, 
                      adsk.core.ValueInput.createByString(value_str),
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
    
    return {"status": "error", "error": f"Unknown sub_action: {sub_action}"}

# ============================================================================
# TIMELINE CONTROL
# ============================================================================

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
                "type": type(item.entity).__name__.replace("adsk.fusion.", ""),
                "is_suppressed": item.isSuppressed,
                "is_rollback": item.isRolledBack
            })
        return {"status": "success", "timeline": items}
    
    elif sub_action == "rollback":
        index = data.get("index")
        if index is not None and index < timeline.count:
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
        return {"status": "error", "error": "No target specified for suppress"}
    
    elif sub_action == "unsuppress":
        if "feature_name" in data:
            for i in range(timeline.count):
                item = timeline.item(i)
                if hasattr(item.entity, 'name') and item.entity.name == data["feature_name"]:
                    item.isSuppressed = False
                    return {"status": "success", "unsuppressed": data["feature_name"]}
        elif "index" in data:
            index = data["index"]
            if index < timeline.count:
                timeline.item(index).isSuppressed = False
                return {"status": "success", "unsuppressed_index": index}
    
    elif sub_action == "delete":
        index = data.get("index")
        if index is not None and index < timeline.count:
            item = timeline.item(index)
            if hasattr(item.entity, 'deleteMe'):
                item.entity.deleteMe()
                return {"status": "success", "deleted_index": index}
    
    return {"status": "error", "error": f"Unknown sub_action: {sub_action}"}

# ============================================================================
# SELECTION & PICKING
# ============================================================================

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
                "type": type(sel.entity).__name__.replace("adsk.fusion.", ""),
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
        elif entity_type == "vertex":
            for body in root.bRepBodies:
                for vertex in body.vertices:
                    entities.append(vertex)
        elif entity_type == "body":
            entities = list(root.bRepBodies)
        elif entity_type == "sketch":
            entities = list(root.sketches)
        elif entity_type == "component":
            entities = list(root.occurrences)
        
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
            
            # Geometry type filters for faces
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
    
    return {"status": "error", "error": f"Unknown sub_action: {sub_action}"}

# ============================================================================
# COMPONENT & ASSEMBLY MANAGEMENT
# ============================================================================

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
        if not file_path:
            return {"status": "error", "error": "file_path required"}
        
        # Import component from file
        importManager = _app.importManager
        if file_path.endswith('.f3d'):
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
                "is_grounded": occ.isGrounded
            })
        return {"status": "success", "components": components}
    
    elif sub_action == "delete":
        name = data.get("name")
        for occ in root.allOccurrences:
            if occ.component.name == name:
                occ.deleteMe()
                return {"status": "success", "deleted": name}
        return {"status": "error", "error": f"Component {name} not found"}
    
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
                    if rx:
                        transform.setToRotation(math.radians(rx), 
                                               adsk.core.Vector3D.create(1,0,0),
                                               adsk.core.Point3D.create(0,0,0))
                
                occ.transform = transform
                return {"status": "success", "transformed": name}
        
        return {"status": "error", "error": f"Component {name} not found"}
    
    return {"status": "error", "error": f"Unknown sub_action: {sub_action}"}

# ============================================================================
# JOINT MANAGEMENT
# ============================================================================

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
        
        if not geom_one or not geom_two:
            return {"status": "error", "error": "geometry_one and geometry_two required"}
        
        # Find components
        occ_one = None
        occ_two = None
        for occ in root.allOccurrences:
            if occ.component.name == geom_one.get("component"):
                occ_one = occ
            if occ.component.name == geom_two.get("component"):
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
        elif joint_type == "cylindrical":
            joint_input.setAsCylindricalJointMotion(adsk.fusion.JointDirections.ZAxisJointDirection)
        elif joint_type == "pin_slot":
            joint_input.setAsPinSlotJointMotion(adsk.fusion.JointDirections.ZAxisJointDirection)
        elif joint_type == "planar":
            joint_input.setAsPlanarJointMotion(adsk.fusion.JointDirections.ZAxisJointDirection)
        elif joint_type == "ball":
            joint_input.setAsBallJointMotion()
        
        # Set limits if provided
        if "limits" in data and joint_type in ["revolute", "slider"]:
            limits = data["limits"]
            joint_input.isLimitEnabled = True
            joint_input.limitMin = adsk.core.ValueInput.createByReal(math.radians(limits.get("min", -180)))
            joint_input.limitMax = adsk.core.ValueInput.createByReal(math.radians(limits.get("max", 180)))
        
        joint = joints.add(joint_input)
        return {"status": "success", "joint": joint.name}
    
    elif sub_action == "list":
        joint_list = []
        for joint in root.joints:
            joint_list.append({
                "name": joint.name,
                "type": str(joint.jointMotion.jointType).split('.')[-1],
                "is_suppressed": joint.isSuppressed
            })
        return {"status": "success", "joints": joint_list}
    
    elif sub_action == "delete":
        name = data.get("name")
        for joint in root.joints:
            if joint.name == name:
                joint.deleteMe()
                return {"status": "success", "deleted": name}
        return {"status": "error", "error": f"Joint {name} not found"}
    
    elif sub_action == "drive":
        joint_name = data.get("name")
        drive_value = data.get("drive_value")
        
        for joint in root.joints:
            if joint.name == joint_name:
                # Drive the joint
                if hasattr(joint.jointMotion, 'rotationValue'):
                    joint.jointMotion.rotationValue = math.radians(drive_value)
                    return {"status": "success", "driven": joint_name, "value": drive_value}
        return {"status": "error", "error": f"Joint {joint_name} not found or not drivable"}
    
    return {"status": "error", "error": f"Unknown sub_action: {sub_action}"}

# ============================================================================
# MATERIAL & APPEARANCE MANAGEMENT
# ============================================================================

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
        
        if not target or not material_name:
            return {"status": "error", "error": "target and material_name required"}
        
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
        return {"status": "success", "materials": materials[:50]}  # Limit to first 50
    
    elif sub_action == "remove":
        target = data.get("target")
        root = design.rootComponent
        for body in root.bRepBodies:
            if body.name == target:
                body.material = None
                return {"status": "success", "removed_from": target}
        return {"status": "error", "error": f"Body {target} not found"}
    
    return {"status": "error", "error": f"Unknown sub_action: {sub_action}"}

# ============================================================================
# VIEW & CAMERA CONTROL
# ============================================================================

def handle_view(data, status_file):
    """Handle view and camera operations"""
    viewport = _app.activeViewport
    if not viewport:
        return {"status": "error", "error": "No active viewport"}
    
    camera = viewport.camera
    sub_action = data.get("sub_action")
    
    if sub_action == "set":
        orientation = data.get("orientation", "iso")
        
        # Get current camera settings
        eye = camera.eye
        target = camera.target
        up = camera.upVector
        
        # Calculate distance from target
        dist = eye.distanceTo(target)
        
        # Set standard views by positioning the eye
        if orientation == "front":
            eye = adsk.core.Point3D.create(target.x, target.y, target.z + dist)
            up = adsk.core.Vector3D.create(0, 1, 0)
        elif orientation == "back":
            eye = adsk.core.Point3D.create(target.x, target.y, target.z - dist)
            up = adsk.core.Vector3D.create(0, 1, 0)
        elif orientation == "top":
            eye = adsk.core.Point3D.create(target.x, target.y + dist, target.z)
            up = adsk.core.Vector3D.create(0, 0, -1)
        elif orientation == "bottom":
            eye = adsk.core.Point3D.create(target.x, target.y - dist, target.z)
            up = adsk.core.Vector3D.create(0, 0, 1)
        elif orientation == "left":
            eye = adsk.core.Point3D.create(target.x - dist, target.y, target.z)
            up = adsk.core.Vector3D.create(0, 1, 0)
        elif orientation == "right":
            eye = adsk.core.Point3D.create(target.x + dist, target.y, target.z)
            up = adsk.core.Vector3D.create(0, 1, 0)
        elif orientation == "iso":
            # Isometric view
            offset = dist / 1.732  # dist / sqrt(3)
            eye = adsk.core.Point3D.create(
                target.x + offset,
                target.y + offset,
                target.z + offset
            )
            up = adsk.core.Vector3D.create(0, 1, 0)
        
        # Apply the new camera settings
        camera.eye = eye
        camera.upVector = up
        camera.isFitView = True
        viewport.camera = camera
        return {"status": "success", "view": orientation}
    
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
        
        # Ensure full path
        if not os.path.isabs(path):
            path = os.path.join(os.path.expanduser("~/Documents/CSL"), path)
        
        # Save viewport image
        viewport.saveAsImageFile(path, size[0], size[1])
        return {"status": "success", "screenshot": path}
    
    return {"status": "error", "error": f"Unknown sub_action: {sub_action}"}

# ============================================================================
# EXPORT ENHANCEMENTS
# ============================================================================

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
    if not os.path.isabs(file_path):
        file_path = os.path.join(os.path.expanduser("~/Documents/CSL/exports"), file_path)
    
    # Create directory if needed
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    try:
        if format_type == "step":
            step_options = export_mgr.createSTEPExportOptions(file_path)
            export_mgr.execute(step_options)
        
        elif format_type == "stl":
            root = design.rootComponent
            stl_options = export_mgr.createSTLExportOptions(root)
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
            
            export_mgr.execute(stl_options)
        
        elif format_type == "iges":
            iges_options = export_mgr.createIGESExportOptions(file_path)
            export_mgr.execute(iges_options)
        
        elif format_type == "f3d":
            archive_options = export_mgr.createFusionArchiveExportOptions(file_path)
            export_mgr.execute(archive_options)
        
        else:
            return {"status": "error", "error": f"Unsupported format: {format_type}"}
        
        return {"status": "success", "exported": file_path, "format": format_type}
    
    except Exception as e:
        return {"status": "error", "error": str(e)}

# ============================================================================
# UNDO/REDO MANAGEMENT
# ============================================================================

def handle_undo(data, status_file):
    """Handle undo/redo operations"""
    global _checkpoints
    
    design = _app.activeProduct
    if not design:
        return {"status": "error", "error": "No active design"}
    
    sub_action = data.get("sub_action")
    
    if sub_action == "undo":
        steps = data.get("steps", 1)
        count = 0
        for _ in range(steps):
            if design.canUndo:
                design.undo()
                count += 1
        return {"status": "success", "undone": count}
    
    elif sub_action == "redo":
        steps = data.get("steps", 1)
        count = 0
        for _ in range(steps):
            if design.canRedo:
                design.redo()
                count += 1
        return {"status": "success", "redone": count}
    
    elif sub_action == "checkpoint":
        name = data.get("checkpoint_name", f"checkpoint_{len(_checkpoints)}")
        description = data.get("description", "")
        
        # Save current state
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
        for name, cp_data in _checkpoints.items():
            checkpoint_list.append({
                "name": name,
                "description": cp_data["description"],
                "timeline_position": cp_data["timeline_position"],
                "timestamp": cp_data["timestamp"]
            })
        return {"status": "success", "checkpoints": checkpoint_list}
    
    return {"status": "error", "error": f"Unknown sub_action: {sub_action}"}

# ============================================================================
# BATCH OPERATIONS
# ============================================================================

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

# ============================================================================
# ANALYSIS & MEASUREMENT
# ============================================================================

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
        
        # If no targets specified, analyze all bodies
        if not targets:
            targets = [body.name for body in root.bRepBodies]
        
        for target_name in targets:
            for body in root.bRepBodies:
                if body.name == target_name:
                    props = body.physicalProperties
                    results.append({
                        "body": target_name,
                        "mass": props.mass,
                        "volume": props.volume,
                        "area": props.area,
                        "density": props.density if hasattr(props, 'density') else 0,
                        "center_of_mass": [
                            props.centerOfMass.x,
                            props.centerOfMass.y,
                            props.centerOfMass.z
                        ]
                    })
        
        return {"status": "success", "mass_properties": results}
    
    elif sub_action == "bounding_box":
        targets = data.get("targets", [])
        results = []
        
        if not targets:
            targets = [body.name for body in root.bRepBodies]
        
        for target_name in targets:
            for body in root.bRepBodies:
                if body.name == target_name:
                    bbox = body.boundingBox
                    results.append({
                        "body": target_name,
                        "min": [bbox.minPoint.x, bbox.minPoint.y, bbox.minPoint.z],
                        "max": [bbox.maxPoint.x, bbox.maxPoint.y, bbox.maxPoint.z],
                        "size": [
                            bbox.maxPoint.x - bbox.minPoint.x,
                            bbox.maxPoint.y - bbox.minPoint.y,
                            bbox.maxPoint.z - bbox.minPoint.z
                        ]
                    })
        
        return {"status": "success", "bounding_boxes": results}
    
    return {"status": "error", "error": f"Unknown sub_action: {sub_action}"}

# ============================================================================
# CONFIGURATION MANAGEMENT
# ============================================================================

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
                elif settings["units"] == "cm":
                    design.unitsManager.defaultLengthUnits = adsk.fusion.DistanceUnits.CentimeterDistanceUnits
        
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
    
    return {"status": "error", "error": f"Unknown sub_action: {sub_action}"}

# ============================================================================
# EXISTING HANDLERS (from stable version)
# ============================================================================

def handle_ping(data, status_file):
    """Handle ping command"""
    return {"status": "pong", "timestamp": time.time()}

def handle_clear(data, status_file):
    """Clear the current design"""
    design = _app.activeProduct
    if design and hasattr(design, 'rootComponent'):
        root = design.rootComponent
        # Remove all features
        while root.features.count > 0:
            root.features.item(0).deleteMe()
        # Remove all sketches
        while root.sketches.count > 0:
            root.sketches.item(0).deleteMe()
        # Remove all bodies
        while root.bRepBodies.count > 0:
            root.bRepBodies.item(0).deleteMe()
    return {"status": "cleared", "timestamp": time.time()}

def handle_query(data, status_file):
    """Query current design state with detailed information"""
    design = _app.activeProduct
    if not design or not hasattr(design, 'rootComponent'):
        return {"status": "no_design", "timestamp": time.time()}
    
    root = design.rootComponent
    info = {
        "status": "query_result",
        "summary": {
            "sketches": root.sketches.count,
            "bodies": root.bRepBodies.count,
            "features": root.features.count,
            "timeline": design.timeline.count if hasattr(design, 'timeline') else 0
        },
        "sketches": [],
        "features": [],
        "bodies": [],
        "timeline": [],
        "timestamp": time.time()
    }
    
    # Detail sketches
    try:
        for i in range(min(20, root.sketches.count)):
            sketch = root.sketches.item(i)
            sketch_info = {
                "index": i,
                "name": sketch.name,
                "profiles": sketch.profiles.count,
                "curves": sketch.sketchCurves.count,
                "points": sketch.sketchPoints.count,
                "is_visible": sketch.isVisible
            }
            # Add curve type breakdown
            curves = []
            if sketch.sketchCurves.sketchLines.count > 0:
                curves.append(f"{sketch.sketchCurves.sketchLines.count} lines")
            if sketch.sketchCurves.sketchCircles.count > 0:
                curves.append(f"{sketch.sketchCurves.sketchCircles.count} circles")
            if sketch.sketchCurves.sketchArcs.count > 0:
                curves.append(f"{sketch.sketchCurves.sketchArcs.count} arcs")
            sketch_info["curve_types"] = ", ".join(curves) if curves else "none"
            info["sketches"].append(sketch_info)
    except Exception as e:
        info["sketches"].append({"error": str(e)})
    
    # Detail bodies
    try:
        for i in range(min(10, root.bRepBodies.count)):
            body = root.bRepBodies.item(i)
            body_info = {
                "index": i,
                "name": body.name,
                "faces": body.faces.count,
                "edges": body.edges.count,
                "vertices": body.vertices.count,
                "is_visible": body.isVisible,
                "is_solid": body.isSolid
            }
            if hasattr(body, 'volume'):
                body_info["volume_cm3"] = round(body.volume, 3)
            if hasattr(body, 'area'):
                body_info["area_cm2"] = round(body.area, 3)
            info["bodies"].append(body_info)
    except Exception as e:
        info["bodies"].append({"error": str(e)})
    
    # Timeline items
    if hasattr(design, 'timeline'):
        try:
            for i in range(min(20, design.timeline.count)):
                item = design.timeline.item(i)
                timeline_info = {
                    "index": i,
                    "name": item.name if hasattr(item, 'name') else "unnamed",
                    "is_suppressed": item.isSuppressed,
                    "entity_type": type(item.entity).__name__.split('.')[-1]
                }
                info["timeline"].append(timeline_info)
        except Exception as e:
            info["timeline"].append({"error": str(e)})
    
    return info

def handle_csl_ir(data, status_file):
    """Process CSL intermediate representation"""
    try:
        # Debug: Log the IR being processed
        ir = data.get("ir", {})
        debug_info = {
            "has_sketches": "sketches" in ir,
            "num_sketches": len(ir.get("sketches", [])) if "sketches" in ir else 0,
            "has_features": "features" in ir,
            "num_features": len(ir.get("features", [])) if "features" in ir else 0,
            "ir_keys": list(ir.keys()) if ir else []
        }
        
        # Add the AddIns directory to Python path so we can import triple_lindy
        import sys
        import os
        addins_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if addins_path not in sys.path:
            sys.path.insert(0, addins_path)
            debug_info["path_added"] = addins_path
        
        # Try importing the backend
        try:
            from triple_lindy.transpilers.fusion360_backend import FusionBackend
            debug_info["backend_import"] = "success"
        except ImportError as e:
            debug_info["backend_import"] = f"failed: {str(e)}"
            # Fallback: try direct creation for debugging
            return {
                "status": "import_error",
                "error": f"Cannot import FusionBackend: {str(e)}",
                "debug": debug_info,
                "timestamp": time.time()
            }
        
        backend = FusionBackend()
        backend.open_session()
        result = backend.realize(ir)
        
        # Zoom to fit
        if _app.activeViewport:
            _app.activeViewport.fit()
        
        # Check for errors in result
        errors = []
        for key, value in result.items():
            if isinstance(value, str) and value.startswith("error:"):
                errors.append(f"{key}: {value}")
        
        if errors:
            return {
                "status": "partial_success",
                "errors": errors,
                "mapping": result,
                "debug": debug_info,
                "timestamp": time.time()
            }
        else:
            # Always include debug info for troubleshooting
            return {
                "status": "success",
                "mapping": result if result else {},
                "features_created": len(result) if result else 0,
                "debug": debug_info,
                "timestamp": time.time()
            }
    except Exception as e:
        return {
            "status": "backend_error",
            "error": str(e),
            "traceback": traceback.format_exc() if _config.get("debug_mode") else None,
            "timestamp": time.time()
        }

def handle_direct_fillet_test(data, status_file):
    """Test creating a fillet directly"""
    try:
        design = _app.activeProduct
        if not design:
            return {"status": "error", "error": "No active design"}
        
        root = design.rootComponent
        
        # Create a simple box
        sketch = root.sketches.add(root.xYConstructionPlane)
        rect = sketch.sketchCurves.sketchLines.addTwoPointRectangle(
            adsk.core.Point3D.create(-2, -2, 0),
            adsk.core.Point3D.create(2, 2, 0)
        )
        
        # Extrude it
        prof = sketch.profiles.item(0)
        extrudes = root.features.extrudeFeatures
        ext_input = extrudes.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        ext_input.setDistanceExtent(False, adsk.core.ValueInput.createByReal(3.0))
        ext = extrudes.add(ext_input)
        
        # Try to add a fillet
        body = root.bRepBodies.item(root.bRepBodies.count - 1)
        edges = adsk.core.ObjectCollection.create()
        for edge in body.edges:
            edges.add(edge)
        
        fil_feats = root.features.filletFeatures
        try:
            const_def = fil_feats.createConstantRadiusFilletDefinition(
                edges, 
                adsk.core.ValueInput.createByReal(0.2),  # 2mm radius
                False  # not tangent chain
            )
            fil = fil_feats.add(const_def)
            return {"status": "success", "fillet_created": True, "token": fil.entityToken}
        except Exception as e:
            return {"status": "error", "error": f"Fillet failed: {str(e)}"}
            
    except Exception as e:
        return {"status": "error", "error": str(e)}

def handle_direct_cylinders(data, status_file):
    """Create cylinders using direct API"""
    design = _app.activeProduct
    if design and hasattr(design, 'rootComponent'):
        root = design.rootComponent
        created_bodies = []
        
        # Create 3 cylinders at different positions
        positions = [(0, 0), (4, 0), (2, 3)]  # cm
        for i, (x, y) in enumerate(positions):
            sketch = root.sketches.add(root.xYConstructionPlane)
            sketch.name = f"DirectSketch{i+1}"
            circle = sketch.sketchCurves.sketchCircles.addByCenterRadius(
                adsk.core.Point3D.create(x, y, 0),
                1.0  # 1cm radius
            )
            
            prof = sketch.profiles.item(0)
            ext_input = root.features.extrudeFeatures.createInput(
                prof,
                adsk.fusion.FeatureOperations.NewBodyFeatureOperation
            )
            ext_input.setDistanceExtent(False, adsk.core.ValueInput.createByReal(3.0))
            ext = root.features.extrudeFeatures.add(ext_input)
            created_bodies.append(ext.name)
        
        # Zoom to fit
        if _app.activeViewport:
            _app.activeViewport.fit()
        
        return {
            "status": "created_cylinders",
            "bodies_created": len(created_bodies),
            "body_names": created_bodies,
            "timestamp": time.time()
        }
    return {"status": "no_design", "timestamp": time.time()}

# ============================================================================
# MAIN COMMAND ROUTER
# ============================================================================

def process_command(data, status_file):
    """Route commands to appropriate handlers"""
    action = data.get("action")
    
    try:
        # Existing actions
        if action == "ping":
            result = handle_ping(data, status_file)
        elif action == "clear":
            result = handle_clear(data, status_file)
        elif action == "query":
            result = handle_query(data, status_file)
        elif action == "direct_cylinders":
            result = handle_direct_cylinders(data, status_file)
        elif action == "direct_fillet_test":
            result = handle_direct_fillet_test(data, status_file)
        
        # New enhanced actions
        elif action == "param":
            result = handle_parameters(data, status_file)
        elif action == "timeline":
            result = handle_timeline(data, status_file)
        elif action == "select":
            result = handle_selection(data, status_file)
        elif action == "component":
            result = handle_component(data, status_file)
        elif action == "joint":
            result = handle_joint(data, status_file)
        elif action == "material":
            result = handle_material(data, status_file)
        elif action == "view":
            result = handle_view(data, status_file)
        elif action == "export":
            result = handle_export(data, status_file)
        elif action == "undo":
            result = handle_undo(data, status_file)
        elif action == "batch":
            result = handle_batch(data, status_file)
        elif action == "analyze":
            result = handle_analyze(data, status_file)
        elif action == "config":
            result = handle_config(data, status_file)
        
        # CSL IR processing
        elif "ir" in data:
            result = handle_csl_ir(data, status_file)
        
        else:
            result = {"status": "error", "error": f"Unknown action: {action}"}
        
        # Write result to status file
        if status_file:
            status_file.write_text(json.dumps(result))
        
        return result
        
    except Exception as e:
        error_result = {
            "status": "error",
            "error": str(e),
            "traceback": traceback.format_exc() if _config.get("debug_mode") else None,
            "timestamp": time.time()
        }
        if status_file:
            status_file.write_text(json.dumps(error_result))
        return error_result

# ============================================================================
# FILE WATCHER
# ============================================================================

def watch_for_commands():
    """Watch file for commands with robust error handling"""
    global _running, _app, _ui
    
    try:
        # Import Path here to avoid issues
        from pathlib import Path
        
        command_file = Path.home() / "Documents" / "CSL" / "live_command.json"
        status_file = Path.home() / "Documents" / "CSL" / "live_status.json"
        
        # Create directory if it doesn't exist
        try:
            command_file.parent.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            if _ui:
                _ui.messageBox(f"Cannot create CSL directory: {str(e)}")
            return
        
        # Initial status
        status_file.write_text(json.dumps({
            "status": "ready",
            "version": "2.0.0",
            "timestamp": time.time()
        }))
        
        last_modified = 0
        error_count = 0
        
        while _running:
            try:
                # Check for file changes
                if command_file.exists():
                    current_modified = command_file.stat().st_mtime
                    
                    if current_modified > last_modified:
                        # Read and process command
                        with open(command_file, 'r') as f:
                            data = json.load(f)
                        
                        # Process safely
                        process_command(data, status_file)
                        last_modified = current_modified
                        error_count = 0  # Reset error count on success
                
                # Small delay to prevent CPU spinning
                time.sleep(0.2)  # Slightly longer delay for stability
                
            except json.JSONDecodeError as e:
                # Invalid JSON in command file
                status_file.write_text(json.dumps({
                    "status": "error",
                    "error": f"Invalid JSON: {str(e)}",
                    "timestamp": time.time()
                }))
                time.sleep(1)
                
            except Exception as e:
                # Other errors
                error_count += 1
                status_file.write_text(json.dumps({
                    "status": "error",
                    "error": str(e),
                    "error_count": error_count,
                    "timestamp": time.time()
                }))
                
                # If too many errors, slow down
                if error_count > 10:
                    time.sleep(5)
                else:
                    time.sleep(1)
                
                # Critical error threshold
                if error_count > 50:
                    _running = False
                    break
    except Exception as e:
        # Catch any initialization errors
        if _ui:
            _ui.messageBox(f"File watcher error: {str(e)}")
        _running = False

# ============================================================================
# TEST SUITE
# ============================================================================

def test_all_features():
    """Comprehensive test suite for all features"""
    tests = [
        # Parameters
        {"action": "param", "sub_action": "set", "name": "test_width", "value": "100mm"},
        {"action": "param", "sub_action": "list"},
        
        # Timeline
        {"action": "timeline", "sub_action": "list"},
        
        # Selection
        {"action": "select", "sub_action": "clear"},
        {"action": "select", "type": "body", "all": True},
        
        # View
        {"action": "view", "sub_action": "set", "orientation": "iso"},
        {"action": "view", "sub_action": "fit"},
        
        # Analysis
        {"action": "analyze", "sub_action": "mass_properties"},
        
        # Config
        {"action": "config", "sub_action": "get"},
        
        # Batch
        {"action": "batch", "commands": [
            {"action": "param", "sub_action": "set", "name": "batch_test", "value": "50mm"},
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
