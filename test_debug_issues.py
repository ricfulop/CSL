#!/usr/bin/env python3
"""
Debug the failing tests
"""

import json
import time
from pathlib import Path

# Define paths
LIVE_COMMAND_FILE = Path.home() / "Documents" / "CSL" / "live_command.json"
LIVE_STATUS_FILE = Path.home() / "Documents" / "CSL" / "live_status.json"

def send_command(command, timeout=3):
    """Send command and get response"""
    LIVE_COMMAND_FILE.write_text(json.dumps(command, indent=2))
    time.sleep(timeout)
    
    if LIVE_STATUS_FILE.exists():
        try:
            return json.loads(LIVE_STATUS_FILE.read_text())
        except:
            return {"status": "json_error"}
    return {"status": "no_response"}

print("=" * 60)
print("DEBUGGING FAILED TESTS")
print("=" * 60)

# 1. Debug Fillet
print("\n1. FILLET TEST")
print("-" * 40)

# First create a body to fillet
send_command({"action": "clear"})
time.sleep(1)

result = send_command({
    "ir": {
        "csl": "1.1",
        "meta": {"name": "FilletTest", "units": "mm"},
        "sketches": [{
            "id": "s1", "plane": "world.xy",
            "entities": [{"kind": "rect", "id": "r1", "center": "0,0", "w": "30", "h": "30"}]
        }],
        "features": [
            {"kind": "extrude", "id": "e1", "profile": "r1", "distance": "30", "op": "new_solid"}
        ]
    }
})
print(f"Created body: {result.get('status')}")

# Now try to add fillet
result = send_command({
    "ir": {
        "csl": "1.1",
        "meta": {"name": "FilletAdd", "units": "mm"},
        "sketches": [],
        "features": [
            {"kind": "fillet", "id": "f1", "radius": "3"}
        ]
    }
})
print(f"Fillet result: {json.dumps(result, indent=2)}")

# 2. Debug Get Selection
print("\n2. GET SELECTION TEST")
print("-" * 40)

# First select something
result = send_command({
    "action": "select",
    "sub_action": "set",
    "type": "body",
    "all": True
})
print(f"Select all bodies: {result.get('status')}")

# Now get selection
result = send_command({
    "action": "select",
    "sub_action": "get"
})
print(f"Get selection result: {json.dumps(result, indent=2)}")

# 3. Debug Bounding Box
print("\n3. BOUNDING BOX TEST")
print("-" * 40)

result = send_command({
    "action": "analyze",
    "sub_action": "bounding_box"
})
print(f"Bounding box result: {json.dumps(result, indent=2)}")

# Try with specific body selection
result = send_command({
    "action": "analyze",
    "sub_action": "bounding_box",
    "bodies": "all"
})
print(f"Bounding box (all bodies): {json.dumps(result, indent=2)}")

print("\n" + "=" * 60)
print("DEBUG COMPLETE")
print("=" * 60)
