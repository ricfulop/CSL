#!/usr/bin/env python3
"""
Clear the current design in Fusion 360
"""

import json
import time
from pathlib import Path

COMMAND_FILE = Path.home() / "Documents" / "CSL" / "live_command.json"
STATUS_FILE = Path.home() / "Documents" / "CSL" / "live_status.json"

def clear_design():
    """Send command to clear the current design"""
    print("\n=== Clearing Design ===")
    command = {"action": "clear"}
    
    with open(COMMAND_FILE, 'w') as f:
        json.dump(command, f, indent=2)
    
    print("Clear command sent")
    time.sleep(2)
    
    if STATUS_FILE.exists():
        with open(STATUS_FILE, 'r') as f:
            status = json.load(f)
        if status.get('status') == 'success':
            print("✅ Design cleared successfully")
        else:
            print(f"Status: {status}")
    return status

if __name__ == "__main__":
    clear_design()
