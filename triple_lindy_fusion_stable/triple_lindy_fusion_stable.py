"""
Triple Lindy Fusion Add-In - Stable File Watcher Version
More robust error handling to prevent crashes
"""
import adsk.core
import adsk.fusion
import json
import threading
import time
import traceback
from pathlib import Path
import sys

# Add parent for backend
addon_path = Path(__file__).parent.parent
if str(addon_path) not in sys.path:
    sys.path.insert(0, str(addon_path))

_app = None
_ui = None
_running = False
_watch_thread = None

def safe_execute(func):
    """Decorator to safely execute functions without crashing Fusion"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # Log error but don't crash
            error_file = Path.home() / "Documents" / "CSL" / "error.log"
            with open(error_file, 'a') as f:
                f.write(f"\n{time.strftime('%Y-%m-%d %H:%M:%S')} - Error: {e}\n")
                f.write(traceback.format_exc())
            return None
    return wrapper

@safe_execute
def process_command(data, status_file):
    """Process a single command safely"""
    global _app
    
    if not _app:
        return
        
    # Simple ping test
    if data.get("action") == "ping":
        status_file.write_text(json.dumps({
            "status": "pong",
            "timestamp": time.time()
        }))
        return
    
    # Query current state - DETAILED VERSION
    if data.get("action") == "query":
        design = _app.activeProduct
        if design and hasattr(design, 'rootComponent'):
            root = design.rootComponent
            info = {
                "status": "query_result",
                "summary": {
                    "sketches": root.sketches.count if hasattr(root.sketches, 'count') else 0,
                    "bodies": root.bRepBodies.count if hasattr(root.bRepBodies, 'count') else 0,
                    "features": root.features.count if hasattr(root.features, 'count') else 0,
                    "timeline": design.timeline.count if hasattr(design.timeline, 'count') else 0
                },
                "sketches": [],
                "features": [],
                "bodies": [],
                "timeline": [],
                "timestamp": time.time()
            }
            
            # Detail sketches
            try:
                for i in range(min(10, root.sketches.count)):
                    sketch = root.sketches.item(i)
                    sketch_info = {
                        "index": i,
                        "name": sketch.name,
                        "profiles": sketch.profiles.count,
                        "curves": sketch.sketchCurves.count,
                        "points": sketch.sketchPoints.count,
                        "is_visible": sketch.isVisible
                    }
                    # Get curve details
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
            
            # Detail features
            try:
                for i in range(min(20, root.features.count)):
                    feat = root.features.item(i)
                    feat_info = {
                        "index": i,
                        "type": type(feat).__name__.replace("adsk.fusion.", ""),
                        "name": getattr(feat, "name", "unnamed")
                    }
                    
                    # Get feature-specific details
                    if hasattr(feat, "extentType"):
                        feat_info["extent_type"] = str(feat.extentType)
                    if hasattr(feat, "operation"):
                        feat_info["operation"] = str(feat.operation)
                    if hasattr(feat, "participantBodies"):
                        feat_info["bodies_affected"] = feat.participantBodies.count
                    
                    info["features"].append(feat_info)
            except Exception as e:
                info["features"].append({"error": str(e)})
            
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
                    if hasattr(body, "volume"):
                        body_info["volume_cm3"] = round(body.volume, 3)
                    if hasattr(body, "area"):
                        body_info["area_cm2"] = round(body.area, 3)
                    info["bodies"].append(body_info)
            except Exception as e:
                info["bodies"].append({"error": str(e)})
            
            # Timeline details (last 10 items)
            try:
                start_idx = max(0, design.timeline.count - 10)
                for i in range(start_idx, design.timeline.count):
                    item = design.timeline.item(i)
                    timeline_info = {
                        "index": i,
                        "name": item.name if hasattr(item, "name") else "unnamed",
                        "is_suppressed": item.isSuppressed if hasattr(item, "isSuppressed") else False
                    }
                    if hasattr(item, "entity"):
                        timeline_info["entity_type"] = type(item.entity).__name__.replace("adsk.fusion.", "")
                    info["timeline"].append(timeline_info)
            except Exception as e:
                info["timeline"].append({"error": str(e)})
            
            # Write formatted output
            status_file.write_text(json.dumps(info, indent=2))
        else:
            status_file.write_text(json.dumps({
                "status": "no_design",
                "timestamp": time.time()
            }))
        return
    
    # Create geometry using direct API
    if data.get("action") == "direct_cylinders":
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
            
            status_file.write_text(json.dumps({
                "status": "created_cylinders",
                "bodies_created": len(created_bodies),
                "body_names": created_bodies,
                "timestamp": time.time()
            }))
        return
    
    # Create simple test geometry (without backend)
    if data.get("action") == "test_simple":
        design = _app.activeProduct
        if design and hasattr(design, 'rootComponent'):
            root = design.rootComponent
            
            # Create a simple sketch
            sketch = root.sketches.add(root.xYConstructionPlane)
            circles = sketch.sketchCurves.sketchCircles
            circle = circles.addByCenterRadius(
                adsk.core.Point3D.create(0, 0, 0),
                2.0  # 2cm radius
            )
            
            # Create extrude
            prof = sketch.profiles.item(0)
            extrudes = root.features.extrudeFeatures
            extInput = extrudes.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
            distance = adsk.core.ValueInput.createByReal(5.0)  # 5cm
            extInput.setDistanceExtent(False, distance)
            ext = extrudes.add(extInput)
            
            status_file.write_text(json.dumps({
                "status": "created_cylinder",
                "timestamp": time.time()
            }))
        return
    
    # For CSL IR, use backend but with error handling
    if "ir" in data:
        try:
            from triple_lindy.transpilers.fusion360_backend import FusionBackend
            backend = FusionBackend()
            backend.open_session()
            result = backend.realize(data["ir"])
        
        # Zoom to fit
        if _app.activeViewport:
            _app.activeViewport.fit()
        
        # Check for errors in result
        errors = []
        for key, value in result.items():
            if isinstance(value, str) and value.startswith("error:"):
                errors.append(f"{key}: {value}")
        
        if errors:
            status_file.write_text(json.dumps({
                "status": "partial_success",
                "errors": errors,
                "mapping": result,
                "timestamp": time.time()
            }))
        else:
            status_file.write_text(json.dumps({
                "status": "success",
                "mapping": result if result else {},
                "features_created": len(result) if result else 0,
                "timestamp": time.time()
            }))
        except Exception as e:
            import traceback
            status_file.write_text(json.dumps({
                "status": "backend_error",
                "error": str(e),
                "traceback": traceback.format_exc(),
                "timestamp": time.time()
            }))

def watch_for_commands():
    """Watch file for commands with robust error handling"""
    global _running, _app
    
    command_file = Path.home() / "Documents" / "CSL" / "live_command.json"
    status_file = Path.home() / "Documents" / "CSL" / "live_status.json"
    command_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Initial status
    status_file.write_text(json.dumps({
        "status": "ready",
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
                    
            time.sleep(0.5)  # Check twice per second
            
        except json.JSONDecodeError:
            # Invalid JSON in command file
            status_file.write_text(json.dumps({
                "status": "invalid_json",
                "timestamp": time.time()
            }))
            time.sleep(1)
            
        except Exception as e:
            # Any other error
            error_count += 1
            if error_count < 5:  # Don't spam errors
                status_file.write_text(json.dumps({
                    "status": "watch_error",
                    "error": str(e),
                    "timestamp": time.time()
                }))
            time.sleep(2)  # Wait longer after errors

def run(context):
    """Main add-in entry point"""
    global _app, _ui, _running, _watch_thread
    
    try:
        _app = adsk.core.Application.get()
        _ui = _app.userInterface
        _running = True
        
        # Start watcher thread
        _watch_thread = threading.Thread(target=watch_for_commands, daemon=True)
        _watch_thread.start()
        
        _ui.messageBox(
            "✅ Triple Lindy Stable Watcher Active\n\n" +
            "Commands:\n" +
            "• ping - Test connection\n" +
            "• query - Get current state\n" +
            "• test_simple - Create test cylinder\n" +
            "• Send CSL IR with 'ir' key\n\n" +
            "Files:\n" +
            "• Command: ~/Documents/CSL/live_command.json\n" +
            "• Status: ~/Documents/CSL/live_status.json",
            "Triple Lindy Ready"
        )
        
    except Exception as e:
        if _ui:
            _ui.messageBox(f"Failed to start: {e}", "Error")

def stop(context):
    """Clean up on add-in stop"""
    global _running
    _running = False
    
    # Mark as stopped
    try:
        status_file = Path.home() / "Documents" / "CSL" / "live_status.json"
        status_file.write_text(json.dumps({
            "status": "stopped",
            "timestamp": time.time()
        }))
    except:
        pass
