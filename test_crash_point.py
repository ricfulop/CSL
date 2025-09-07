#!/usr/bin/env python3
"""
Find the exact point where Fusion crashes
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
print("FINDING CRASH POINT")
print("=" * 60)

# Create a simple body first
print("\n1. Creating test body...")
send_command({"action": "clear"})
time.sleep(2)

result = send_command({
    "ir": {
        "csl": "1.1",
        "meta": {"name": "TestBody", "units": "mm"},
        "sketches": [{
            "id": "s1", "plane": "world.xy",
            "entities": [{"kind": "circle", "id": "c1", "center": "0,0", "d": "20"}]
        }],
        "features": [
            {"kind": "extrude", "id": "e1", "profile": "c1", "distance": "30", "op": "new_solid"}
        ]
    }
})
print(f"   Body created: {result.get('status')}")
time.sleep(2)

# Test each analysis operation separately
print("\n2. Testing analysis operations one by one...")

print("\n   a) Mass properties...")
result = send_command({
    "action": "analyze",
    "sub_action": "mass_properties"
})
print(f"      Result: {result.get('status')}")
time.sleep(2)

print("\n   b) Bounding box...")
result = send_command({
    "action": "analyze",
    "sub_action": "bounding_box"
})
print(f"      Result: {result.get('status')}")
time.sleep(2)

print("\n3. Testing undo operations...")

print("\n   a) Create checkpoint...")
result = send_command({
    "action": "undo",
    "sub_action": "checkpoint",
    "checkpoint_name": "test_point"
})
print(f"      Result: {result.get('status')}")
time.sleep(2)

print("\n   b) List checkpoints...")
result = send_command({
    "action": "undo",
    "sub_action": "list"
})
print(f"      Result: {result.get('status')}")
if "checkpoints" in result:
    print(f"      Found {len(result['checkpoints'])} checkpoints")
time.sleep(2)

print("\n4. Testing timeline operations after undo...")

print("\n   a) List timeline...")
result = send_command({
    "action": "timeline",
    "sub_action": "list"
})
print(f"      Result: {result.get('status')}")
if "timeline" in result:
    print(f"      Found {len(result['timeline'])} timeline items")
time.sleep(2)

print("\n5. Testing fillet (this might be the issue)...")
result = send_command({
    "ir": {
        "csl": "1.1",
        "meta": {"name": "FilletTest", "units": "mm"},
        "sketches": [],
        "features": [
            {"kind": "fillet", "id": "f1", "radius": "2"}
        ]
    }
})
print(f"   Fillet result: {result.get('status')}")
if "mapping" in result:
    print(f"   Mapping: {result['mapping']}")
time.sleep(2)

print("\n" + "=" * 60)
print("If Fusion crashed, check which step was the last one printed.")
print("=" * 60)
