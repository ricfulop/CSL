#!/usr/bin/env python3
"""
Test rectangle extrude now that sketch creation works
"""

import json
import time
from pathlib import Path

# Define paths
LIVE_COMMAND_FILE = Path.home() / "Documents" / "CSL" / "live_command.json"
LIVE_STATUS_FILE = Path.home() / "Documents" / "CSL" / "live_status.json"

def send_command(command):
    """Send command and get response"""
    LIVE_COMMAND_FILE.write_text(json.dumps(command, indent=2))
    time.sleep(3)
    
    if LIVE_STATUS_FILE.exists():
        try:
            return json.loads(LIVE_STATUS_FILE.read_text())
        except:
            return {"status": "json_error"}
    return {"status": "no_response"}

print("=" * 60)
print("RECTANGLE EXTRUDE TEST")
print("=" * 60)

# Clear first
print("\n1. Clearing design...")
result = send_command({"action": "clear"})
print(f"   Status: {result.get('status')}")
time.sleep(2)

# Test 1: Rectangle with center/w/h and extrude by entity ID
print("\n2. Testing rectangle extrude with entity ID (r1)...")
csl_ir = {
    "csl": "1.1",
    "meta": {"name": "RectExtrudeTest", "units": "mm"},
    "sketches": [
        {
            "id": "s1", 
            "plane": "world.xy", 
            "entities": [
                {"kind": "rect", "id": "r1", "center": "0,0", "w": "20", "h": "30"}
            ]
        }
    ],
    "features": [
        {"kind": "extrude", "id": "e1", "profile": "r1", "distance": "15", "op": "new_solid"}
    ]
}

result = send_command({"ir": csl_ir})
print(f"   Status: {result.get('status')}")
if "mapping" in result:
    mapping = result.get('mapping', {})
    print(f"   Features created: {len(mapping)}")
    for feat_id, value in mapping.items():
        if "error" in str(value):
            print(f"      - {feat_id}: ❌ {value}")
        else:
            print(f"      - {feat_id}: ✅ created")

# Query to see what was created
time.sleep(1)
result = send_command({"action": "query"})
summary = result.get("summary", {})
print(f"   Result - Bodies: {summary.get('bodies', 0)}, Sketches: {summary.get('sketches', 0)}")

if summary.get('bodies', 0) > 0:
    print("   ✅ SUCCESS - Rectangle extruded with entity ID!")
else:
    print("   ❌ FAILED - No body created with entity ID")
    
    # Try with sketch ID instead
    print("\n3. Trying with sketch ID instead...")
    result = send_command({"action": "clear"})
    time.sleep(2)
    
    csl_ir["features"][0]["profile"] = "s1"  # Use sketch ID instead
    result = send_command({"ir": csl_ir})
    print(f"   Status: {result.get('status')}")
    
    result = send_command({"action": "query"})
    summary = result.get("summary", {})
    print(f"   Result - Bodies: {summary.get('bodies', 0)}, Sketches: {summary.get('sketches', 0)}")
    
    if summary.get('bodies', 0) > 0:
        print("   ✅ SUCCESS - Rectangle extruded with sketch ID!")
    else:
        print("   ❌ FAILED - Rectangle extrude still not working")

print("\n" + "=" * 60)
print("TEST COMPLETE")
print("=" * 60)
