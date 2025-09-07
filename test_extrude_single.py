#!/usr/bin/env python3
"""
Test a single extrude case with full output
"""

import json
import time
from pathlib import Path

# Define paths
LIVE_COMMAND_FILE = Path.home() / "Documents" / "CSL" / "live_command.json"
LIVE_STATUS_FILE = Path.home() / "Documents" / "CSL" / "live_status.json"

# Clear first
LIVE_COMMAND_FILE.write_text(json.dumps({"action": "clear"}))
time.sleep(2)

# Simple test case
test_ir = {
    "csl": "1.1",
    "meta": {"name": "SingleTest", "units": "mm"},
    "sketches": [
        {
            "id": "s1", 
            "plane": "world.xy", 
            "entities": [
                {"kind": "circle", "id": "c1", "center": "0,0", "d": "20"}
            ]
        }
    ],
    "features": [
        {"kind": "extrude", "id": "e1", "profile": "c1", "distance": "30", "op": "new_solid"}
    ]
}

# Send command
command = {"ir": test_ir}
print("Sending command:")
print(json.dumps(command, indent=2))

LIVE_COMMAND_FILE.write_text(json.dumps(command))
time.sleep(3)

# Read result
if LIVE_STATUS_FILE.exists():
    result = json.loads(LIVE_STATUS_FILE.read_text())
    print("\nFull result:")
    print(json.dumps(result, indent=2))
else:
    print("No status file found")
