#!/usr/bin/env python3
"""
Direct chamfer API test to find the correct usage
"""

import json
import time
from pathlib import Path

COMMAND_FILE = Path.home() / "Documents" / "CSL" / "live_command.json"
STATUS_FILE = Path.home() / "Documents" / "CSL" / "live_status.json"

def test_direct_chamfer():
    """Test direct chamfer creation in Fusion API"""
    print("\n=== Testing Direct Chamfer API ===")
    command = {"action": "direct_chamfer_test"}
    
    with open(COMMAND_FILE, 'w') as f:
        json.dump(command, f, indent=2)
    
    print("Command sent: direct_chamfer_test")
    print("This should create a box with chamfered edges using direct API")
    time.sleep(3)
    
    if STATUS_FILE.exists():
        with open(STATUS_FILE, 'r') as f:
            status = json.load(f)
        print(f"Status: {status.get('status', 'unknown')}")
        if 'error' in status:
            print(f"Error: {status['error']}")
        else:
            print("Check Fusion 360 for a box with chamfers")
    return status

if __name__ == "__main__":
    test_direct_chamfer()
