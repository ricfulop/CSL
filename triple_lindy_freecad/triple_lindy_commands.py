"""
Triple Lindy Commands for FreeCAD Workbench
"""
import FreeCAD
import FreeCADGui
from PySide import QtGui, QtCore
from pathlib import Path
import json
import time
import threading
import traceback
import sys
import os

# Add parent directory for backend import
workbench_path = Path(__file__).parent.parent
sys.path.insert(0, str(workbench_path))

# Global watcher instance
_watcher = None

class FileWatcher:
    """File watcher for CSL commands."""
    
    def __init__(self):
        self.running = False
        self.thread = None
        self.backend = None
        self.command_file = Path.home() / "Documents" / "CSL" / "live_command.json"
        self.status_file = Path.home() / "Documents" / "CSL" / "live_status.json"
        
        # Ensure directory exists
        self.command_file.parent.mkdir(parents=True, exist_ok=True)
    
    def start(self):
        """Start the file watcher."""
        if self.running:
            FreeCAD.Console.PrintMessage("Watcher already running\n")
            return
        
        self.running = True
        self.thread = threading.Thread(target=self._watch_loop, daemon=True)
        self.thread.start()
        
        # Initial status
        self._write_status({
            "status": "ready",
            "backend": "freecad",
            "version": FreeCAD.Version()[0] + "." + FreeCAD.Version()[1],
            "timestamp": time.time()
        })
        
        FreeCAD.Console.PrintMessage("✅ Triple Lindy File Watcher Started\n")
        FreeCAD.Console.PrintMessage(f"Watching: {self.command_file}\n")
        FreeCAD.Console.PrintMessage(f"Status: {self.status_file}\n")
    
    def stop(self):
        """Stop the file watcher."""
        self.running = False
        if self.thread:
            self.thread.join(timeout=2)
        
        self._write_status({
            "status": "stopped",
            "backend": "freecad",
            "timestamp": time.time()
        })
        
        FreeCAD.Console.PrintMessage("🛑 Triple Lindy File Watcher Stopped\n")
    
    def _watch_loop(self):
        """Main watch loop."""
        last_modified = 0
        
        while self.running:
            try:
                if self.command_file.exists():
                    current_modified = self.command_file.stat().st_mtime
                    
                    if current_modified > last_modified:
                        # Read and process command
                        with open(self.command_file, 'r') as f:
                            data = json.load(f)
                        
                        # Process in GUI thread
                        QtCore.QTimer.singleShot(0, lambda: self._process_command(data))
                        last_modified = current_modified
                
                time.sleep(0.5)  # Check twice per second
                
            except json.JSONDecodeError:
                self._write_status({
                    "status": "invalid_json",
                    "backend": "freecad",
                    "timestamp": time.time()
                })
                time.sleep(1)
                
            except Exception as e:
                self._write_status({
                    "status": "watch_error",
                    "backend": "freecad",
                    "error": str(e),
                    "timestamp": time.time()
                })
                time.sleep(2)
    
    def _process_command(self, data):
        """Process a command from the file."""
        try:
            action = data.get("action")
            
            if action == "ping":
                # Simple connectivity test
                self._write_status({
                    "status": "pong",
                    "backend": "freecad",
                    "timestamp": time.time()
                })
                FreeCAD.Console.PrintMessage("Ping received\n")
            
            elif action == "query":
                # Query current state
                state = self._query_state()
                self._write_status({
                    "status": "query_result",
                    "backend": "freecad",
                    "state": state,
                    "timestamp": time.time()
                })
                FreeCAD.Console.PrintMessage("State queried\n")
            
            elif action == "clear":
                # Clear current document
                doc = FreeCAD.ActiveDocument
                if doc:
                    for obj in doc.Objects:
                        doc.removeObject(obj.Name)
                    doc.recompute()
                    FreeCAD.Console.PrintMessage("Document cleared\n")
                
                self._write_status({
                    "status": "cleared",
                    "backend": "freecad",
                    "timestamp": time.time()
                })
            
            elif action == "test_simple":
                # Create simple test geometry
                self._create_test_geometry()
                self._write_status({
                    "status": "test_created",
                    "backend": "freecad",
                    "timestamp": time.time()
                })
                FreeCAD.Console.PrintMessage("Test geometry created\n")
            
            elif "ir" in data:
                # Process CSL IR using backend
                from triple_lindy.transpilers.freecad_backend import FreeCADBackend
                
                if not self.backend:
                    self.backend = FreeCADBackend()
                    self.backend.open_session({"clear_existing": False})
                
                FreeCAD.Console.PrintMessage("Processing CSL IR...\n")
                result = self.backend.realize(data["ir"])
                
                # Fit view
                if FreeCADGui.ActiveDocument:
                    FreeCADGui.ActiveDocument.activeView().fitAll()
                
                # Check for errors
                errors = []
                for key, value in result.items():
                    if isinstance(value, str) and value.startswith("error"):
                        errors.append(f"{key}: {value}")
                
                if errors:
                    self._write_status({
                        "status": "partial_success",
                        "backend": "freecad",
                        "errors": errors,
                        "mapping": result,
                        "timestamp": time.time()
                    })
                    FreeCAD.Console.PrintWarning(f"Partial success with errors: {errors}\n")
                else:
                    self._write_status({
                        "status": "success",
                        "backend": "freecad",
                        "mapping": result,
                        "features_created": len(result),
                        "timestamp": time.time()
                    })
                    FreeCAD.Console.PrintMessage(f"✅ Created {len(result)} features\n")
            
            else:
                self._write_status({
                    "status": "unknown_command",
                    "backend": "freecad",
                    "timestamp": time.time()
                })
                FreeCAD.Console.PrintWarning(f"Unknown command: {action}\n")
                
        except Exception as e:
            self._write_status({
                "status": "command_error",
                "backend": "freecad",
                "error": str(e),
                "traceback": traceback.format_exc(),
                "timestamp": time.time()
            })
            FreeCAD.Console.PrintError(f"Command error: {e}\n")
    
    def _query_state(self):
        """Query current FreeCAD state."""
        doc = FreeCAD.ActiveDocument
        if not doc:
            return {"no_document": True}
        
        state = {
            "document": doc.Name,
            "object_count": len(doc.Objects),
            "sketches": [],
            "bodies": [],
            "features": []
        }
        
        for obj in doc.Objects:
            if obj.TypeId == "Sketcher::SketchObject":
                state["sketches"].append({
                    "name": obj.Name,
                    "label": obj.Label,
                    "geometry": len(obj.Geometry),
                    "constraints": len(obj.Constraints)
                })
            elif hasattr(obj, "Shape"):
                if obj.Shape.ShapeType == "Solid":
                    state["bodies"].append({
                        "name": obj.Name,
                        "faces": len(obj.Shape.Faces),
                        "edges": len(obj.Shape.Edges),
                        "volume": round(obj.Shape.Volume, 3)
                    })
                else:
                    state["features"].append({
                        "name": obj.Name,
                        "type": obj.TypeId
                    })
        
        return state
    
    def _create_test_geometry(self):
        """Create simple test geometry."""
        import Part
        
        doc = FreeCAD.ActiveDocument
        if not doc:
            doc = FreeCAD.newDocument("TestDoc")
        
        # Create a box
        box = doc.addObject("Part::Box", "TestBox")
        box.Length = 60
        box.Width = 60
        box.Height = 40
        
        # Create a cylinder
        cylinder = doc.addObject("Part::Cylinder", "TestCylinder")
        cylinder.Radius = 15
        cylinder.Height = 50
        cylinder.Placement.Base = FreeCAD.Vector(80, 0, 0)
        
        # Create a sphere
        sphere = doc.addObject("Part::Sphere", "TestSphere")
        sphere.Radius = 20
        sphere.Placement.Base = FreeCAD.Vector(40, 80, 0)
        
        doc.recompute()
        
        if FreeCADGui.ActiveDocument:
            FreeCADGui.ActiveDocument.activeView().fitAll()
    
    def _write_status(self, data):
        """Write status to file."""
        try:
            self.status_file.write_text(json.dumps(data, indent=2))
        except Exception as e:
            FreeCAD.Console.PrintError(f"Failed to write status: {e}\n")

# Command classes

class TripleLindyStart:
    """Start the file watcher."""
    
    def GetResources(self):
        return {
            'Pixmap': 'Std_Tool1',
            'MenuText': 'Start Triple Lindy',
            'ToolTip': 'Start the CSL file watcher'
        }
    
    def Activated(self):
        global _watcher
        if not _watcher:
            _watcher = FileWatcher()
        _watcher.start()
    
    def IsActive(self):
        return True

class TripleLindyStop:
    """Stop the file watcher."""
    
    def GetResources(self):
        return {
            'Pixmap': 'Std_Stop',
            'MenuText': 'Stop Triple Lindy',
            'ToolTip': 'Stop the CSL file watcher'
        }
    
    def Activated(self):
        global _watcher
        if _watcher:
            _watcher.stop()
    
    def IsActive(self):
        return _watcher is not None and _watcher.running

class TripleLindyStatus:
    """Check watcher status."""
    
    def GetResources(self):
        return {
            'Pixmap': 'Std_DlgParameter',
            'MenuText': 'Triple Lindy Status',
            'ToolTip': 'Check the watcher status'
        }
    
    def Activated(self):
        global _watcher
        if _watcher and _watcher.running:
            QtGui.QMessageBox.information(None, "Triple Lindy Status",
                f"✅ Watcher is running\n\n"
                f"Command file:\n{_watcher.command_file}\n\n"
                f"Status file:\n{_watcher.status_file}")
        else:
            QtGui.QMessageBox.information(None, "Triple Lindy Status",
                "🛑 Watcher is not running\n\n"
                "Use 'Start Triple Lindy' to begin")
    
    def IsActive(self):
        return True

class TripleLindyTest:
    """Create test geometry."""
    
    def GetResources(self):
        return {
            'Pixmap': 'Part_Box',
            'MenuText': 'Test Geometry',
            'ToolTip': 'Create test geometry'
        }
    
    def Activated(self):
        global _watcher
        if not _watcher:
            _watcher = FileWatcher()
        _watcher._create_test_geometry()
        FreeCAD.Console.PrintMessage("Test geometry created\n")
    
    def IsActive(self):
        return True

class TripleLindyClear:
    """Clear the document."""
    
    def GetResources(self):
        return {
            'Pixmap': 'Std_Delete',
            'MenuText': 'Clear Document',
            'ToolTip': 'Clear all objects from the document'
        }
    
    def Activated(self):
        doc = FreeCAD.ActiveDocument
        if doc:
            reply = QtGui.QMessageBox.question(None, "Clear Document",
                "Clear all objects from the current document?",
                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
            
            if reply == QtGui.QMessageBox.Yes:
                for obj in doc.Objects:
                    doc.removeObject(obj.Name)
                doc.recompute()
                FreeCAD.Console.PrintMessage("Document cleared\n")
    
    def IsActive(self):
        return FreeCAD.ActiveDocument is not None

class TripleLindyHelp:
    """Show help information."""
    
    def GetResources(self):
        return {
            'Pixmap': 'Std_WhatsThis',
            'MenuText': 'Triple Lindy Help',
            'ToolTip': 'Show help for Triple Lindy'
        }
    
    def Activated(self):
        help_text = """
Triple Lindy CSL Integration for FreeCAD

COMMANDS:
• Start - Begin watching for CSL commands
• Stop - Stop the file watcher
• Status - Check watcher status
• Test - Create test geometry
• Clear - Clear the document
• Help - Show this help

FILE LOCATIONS:
• Commands: ~/Documents/CSL/live_command.json
• Status: ~/Documents/CSL/live_status.json

USAGE:
1. Start the watcher
2. Send commands to live_command.json
3. Check results in live_status.json

COMMAND EXAMPLES:
• {"action": "ping"} - Test connection
• {"action": "query"} - Get document state
• {"action": "clear"} - Clear document
• {"action": "test_simple"} - Create test geometry
• {"ir": {...}} - Process CSL IR

For more information, see the documentation.
        """
        QtGui.QMessageBox.information(None, "Triple Lindy Help", help_text)
    
    def IsActive(self):
        return True

# Register commands
FreeCADGui.addCommand('TripleLindyStart', TripleLindyStart())
FreeCADGui.addCommand('TripleLindyStop', TripleLindyStop())
FreeCADGui.addCommand('TripleLindyStatus', TripleLindyStatus())
FreeCADGui.addCommand('TripleLindyTest', TripleLindyTest())
FreeCADGui.addCommand('TripleLindyClear', TripleLindyClear())
FreeCADGui.addCommand('TripleLindyHelp', TripleLindyHelp())
