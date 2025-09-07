"""
Triple Lindy Minimal - Start with core features only
Gradually add more as we verify stability
"""

import adsk.core
import adsk.fusion
import json
import time
import os
import threading
import traceback
from pathlib import Path

# Global variables
_app = None
_ui = None
_running = False

def run(context):
    """Entry point for the add-in"""
    global _app, _ui, _running
    try:
        _app = adsk.core.Application.get()
        _ui = _app.userInterface
        
        # Start file watcher in a separate thread
        _running = True
        watcher_thread = threading.Thread(target=watch_for_commands, daemon=True)
        watcher_thread.start()
        
        _ui.messageBox("Triple Lindy Minimal started!\nCore features only: ping, clear, query, param")
        
    except Exception as e:
        if _ui:
            _ui.messageBox(f"Failed to start: {str(e)}\n\n{traceback.format_exc()}")

def stop(context):
    """Clean up when add-in stops"""
    global _running
    _running = False

def watch_for_commands():
    """Simple file watcher"""
    global _running, _app
    
    try:
        command_file = Path.home() / "Documents" / "CSL" / "live_command.json"
        status_file = Path.home() / "Documents" / "CSL" / "live_status.json"
        command_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Initial status
        status_file.write_text(json.dumps({
            "status": "ready",
            "version": "minimal",
            "timestamp": time.time()
        }))
        
        last_modified = 0
        
        while _running:
            try:
                if command_file.exists():
                    current_modified = command_file.stat().st_mtime
                    
                    if current_modified > last_modified:
                        try:
                            with open(command_file, 'r') as f:
                                data = json.load(f)
                            
                            # Process command
                            result = process_command(data)
                            
                            # Write result
                            status_file.write_text(json.dumps(result))
                            last_modified = current_modified
                            
                        except json.JSONDecodeError:
                            status_file.write_text(json.dumps({
                                "status": "error",
                                "error": "Invalid JSON",
                                "timestamp": time.time()
                            }))
                        except Exception as e:
                            status_file.write_text(json.dumps({
                                "status": "error",
                                "error": str(e),
                                "timestamp": time.time()
                            }))
                
                time.sleep(0.2)
                
            except Exception as e:
                # Log error but keep running
                try:
                    status_file.write_text(json.dumps({
                        "status": "error",
                        "error": f"Watcher error: {str(e)}",
                        "timestamp": time.time()
                    }))
                except:
                    pass
                time.sleep(1)
                
    except Exception as e:
        if _ui:
            _ui.messageBox(f"Watcher failed to start: {str(e)}")
        _running = False

def process_command(data):
    """Process commands - minimal version"""
    action = data.get("action")
    
    try:
        if action == "ping":
            return {"status": "pong", "timestamp": time.time()}
        
        elif action == "clear":
            design = _app.activeProduct
            if design and hasattr(design, 'rootComponent'):
                root = design.rootComponent
                # Clear features
                while root.features.count > 0:
                    try:
                        root.features.item(0).deleteMe()
                    except:
                        break
                # Clear sketches
                while root.sketches.count > 0:
                    try:
                        root.sketches.item(0).deleteMe()
                    except:
                        break
                # Clear bodies
                while root.bRepBodies.count > 0:
                    try:
                        root.bRepBodies.item(0).deleteMe()
                    except:
                        break
            return {"status": "cleared", "timestamp": time.time()}
        
        elif action == "query":
            design = _app.activeProduct
            if not design or not hasattr(design, 'rootComponent'):
                return {"status": "no_design", "timestamp": time.time()}
            
            root = design.rootComponent
            return {
                "status": "query_result",
                "summary": {
                    "sketches": root.sketches.count,
                    "bodies": root.bRepBodies.count,
                    "features": root.features.count
                },
                "timestamp": time.time()
            }
        
        elif action == "param":
            design = _app.activeProduct
            if not design:
                return {"status": "error", "error": "No active design"}
            
            params = design.userParameters
            sub_action = data.get("sub_action")
            
            if sub_action == "set":
                name = data.get("name")
                value = data.get("value")
                if name and value:
                    param = params.itemByName(name)
                    if param:
                        param.expression = value
                    else:
                        params.add(name, 
                                  adsk.core.ValueInput.createByString(value),
                                  "", "")
                    return {"status": "success", "parameter": name, "value": value}
                return {"status": "error", "error": "Name and value required"}
            
            elif sub_action == "list":
                param_list = []
                for param in params:
                    param_list.append({
                        "name": param.name,
                        "value": param.expression,
                        "unit": param.unit
                    })
                return {"status": "success", "parameters": param_list}
            
            return {"status": "error", "error": f"Unknown sub_action: {sub_action}"}
        
        else:
            return {"status": "error", "error": f"Unknown action: {action}"}
            
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "timestamp": time.time()
        }
