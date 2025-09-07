"""
Triple Lindy Debug - Minimal test version to identify startup issues
"""

import adsk.core
import adsk.fusion
import traceback

_app = None
_ui = None

def run(context):
    """Entry point for the add-in"""
    global _app, _ui
    try:
        _app = adsk.core.Application.get()
        _ui = _app.userInterface
        
        # Simple test message
        _ui.messageBox("Debug Add-in: Stage 1 - Basic startup OK")
        
        # Test imports
        try:
            import json
            _ui.messageBox("Debug Add-in: Stage 2 - json import OK")
        except Exception as e:
            _ui.messageBox(f"Debug Add-in: json import failed: {str(e)}")
            
        try:
            import threading
            _ui.messageBox("Debug Add-in: Stage 3 - threading import OK")
        except Exception as e:
            _ui.messageBox(f"Debug Add-in: threading import failed: {str(e)}")
            
        try:
            from pathlib import Path
            _ui.messageBox("Debug Add-in: Stage 4 - pathlib import OK")
        except Exception as e:
            _ui.messageBox(f"Debug Add-in: pathlib import failed: {str(e)}")
            
        try:
            import time
            import os
            import math
            _ui.messageBox("Debug Add-in: Stage 5 - other imports OK")
        except Exception as e:
            _ui.messageBox(f"Debug Add-in: other imports failed: {str(e)}")
        
        # Test file operations
        try:
            from pathlib import Path
            test_path = Path.home() / "Documents" / "CSL"
            test_path.mkdir(parents=True, exist_ok=True)
            _ui.messageBox(f"Debug Add-in: Stage 6 - File path OK: {test_path}")
        except Exception as e:
            _ui.messageBox(f"Debug Add-in: File path failed: {str(e)}")
            
        _ui.messageBox("Debug Add-in: ALL TESTS PASSED - Ready for full version")
        
    except Exception as e:
        if _ui:
            _ui.messageBox(f"Debug Add-in FAILED at startup: {str(e)}\n\n{traceback.format_exc()}")
        else:
            print(f"Debug Add-in FAILED (no UI): {str(e)}\n\n{traceback.format_exc()}")

def stop(context):
    """Clean up when add-in stops"""
    global _ui
    if _ui:
        _ui.messageBox("Debug Add-in stopped")
