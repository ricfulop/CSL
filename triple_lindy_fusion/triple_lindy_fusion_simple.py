"""
Triple Lindy Fusion Add-In (Simple Version)
Works without external WebSocket library - uses built-in urllib
"""
import adsk.core
import adsk.fusion
import json
import threading
import time
import urllib.request
import urllib.error
from pathlib import Path
import sys

# Add parent for backend
addon_path = Path(__file__).parent.parent
if str(addon_path) not in sys.path:
    sys.path.insert(0, str(addon_path))

from triple_lindy.transpilers.fusion360_backend import FusionBackend

_app = None
_ui = None
_running = False
_poll_thread = None

def poll_daemon():
    """Poll daemon for commands via HTTP (simpler than WebSocket)"""
    global _running, _app, _ui
    
    while _running:
        try:
            # Simple HTTP polling (we'll update daemon to support this)
            time.sleep(1)
        except Exception as e:
            pass

def run(context):
    """Main add-in entry point"""
    global _app, _ui, _running, _poll_thread
    
    try:
        _app = adsk.core.Application.get()
        _ui = _app.userInterface
        _running = True
        
        # For now, just show we're connected
        _ui.messageBox(
            "Triple Lindy Connected!\n\n" +
            "The add-in is running but needs WebSocket support.\n" +
            "For now, use the standalone script:\n\n" +
            "python3 remote_control.py example",
            "Triple Lindy"
        )
        
        # Test the backend directly
        try:
            backend = FusionBackend()
            backend.open_session()
            
            # Create a simple test
            ir = {
                "csl": "1.1",
                "meta": {"name": "Add-In Test", "units": "mm"},
                "sketches": [
                    {"id": "s", "plane": "world.xy", "entities": [
                        {"kind": "rect", "id": "r", "p1": "0,0", "p2": "20,15"}
                    ]}
                ],
                "features": [
                    {"kind": "extrude", "id": "e", "profile": "r", "distance": "10", "op": "new_solid"}
                ]
            }
            
            mapping = backend.realize(ir)
            
            # Zoom to fit
            if _app.activeViewport:
                _app.activeViewport.fit()
                
            _ui.messageBox("Test box created successfully!", "Triple Lindy")
            
        except Exception as e:
            _ui.messageBox(f"Backend test failed: {e}", "Triple Lindy Error")
        
    except Exception as e:
        if _ui:
            _ui.messageBox(f"Failed to start: {e}", "Triple Lindy Error")

def stop(context):
    """Clean up on add-in stop"""
    global _running
    _running = False
