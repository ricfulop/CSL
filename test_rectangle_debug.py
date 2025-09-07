#!/usr/bin/env python3
"""
Debug rectangle extrude issue specifically
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
        return json.loads(LIVE_STATUS_FILE.read_text())
    return {"status": "no_response"}

print("=" * 60)
print("RECTANGLE EXTRUDE DEBUG")
print("=" * 60)

# Clear first
print("\n1. Clearing design...")
result = send_command({"action": "clear"})
print(f"   Status: {result.get('status')}")
time.sleep(1)

# Test 1: Rectangle with center and dimensions
print("\n2. Testing rectangle with center + w/h...")
csl_ir = {
    "csl": "1.1",
    "meta": {"name": "RectTest1", "units": "mm"},
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
print(f"   Result: {json.dumps(result, indent=2)}")

# Query to see what happened
result = send_command({"action": "query"})
summary = result.get("summary", {})
print(f"   Created - Bodies: {summary.get('bodies', 0)}, Sketches: {summary.get('sketches', 0)}")

if summary.get('bodies', 0) == 0:
    print("   ❌ FAILED - No body created from rect with center+w/h")
else:
    print("   ✅ SUCCESS - Body created from rect with center+w/h")

# Clear for next test
time.sleep(2)
result = send_command({"action": "clear"})

# Test 2: Rectangle with p1 and p2 (two corners)
print("\n3. Testing rectangle with p1/p2 corners...")
csl_ir = {
    "csl": "1.1",
    "meta": {"name": "RectTest2", "units": "mm"},
    "sketches": [
        {
            "id": "s2", 
            "plane": "world.xy", 
            "entities": [
                {"kind": "rect", "id": "r2", "p1": "-10,-15", "p2": "10,15"}
            ]
        }
    ],
    "features": [
        {"kind": "extrude", "id": "e2", "profile": "r2", "distance": "15", "op": "new_solid"}
    ]
}

result = send_command({"ir": csl_ir})
print(f"   Result status: {result.get('status')}")
if "mapping" in result:
    print(f"   Mapping: {len(result['mapping'])} items")

# Query again
result = send_command({"action": "query"})
summary = result.get("summary", {})
print(f"   Created - Bodies: {summary.get('bodies', 0)}, Sketches: {summary.get('sketches', 0)}")

if summary.get('bodies', 0) == 0:
    print("   ❌ FAILED - No body created from rect with p1/p2")
else:
    print("   ✅ SUCCESS - Body created from rect with p1/p2")

# Clear for next test
time.sleep(2)
result = send_command({"action": "clear"})

# Test 3: Try extruding by sketch ID instead of entity ID
print("\n4. Testing rectangle extrude using sketch ID...")
csl_ir = {
    "csl": "1.1",
    "meta": {"name": "RectTest3", "units": "mm"},
    "sketches": [
        {
            "id": "s3", 
            "plane": "world.xy", 
            "entities": [
                {"kind": "rect", "id": "r3", "center": "0,0", "w": "20", "h": "30"}
            ]
        }
    ],
    "features": [
        {"kind": "extrude", "id": "e3", "profile": "s3", "distance": "15", "op": "new_solid"}
    ]
}

result = send_command({"ir": csl_ir})
print(f"   Result status: {result.get('status')}")

# Query again
result = send_command({"action": "query"})
summary = result.get("summary", {})
print(f"   Created - Bodies: {summary.get('bodies', 0)}, Sketches: {summary.get('sketches', 0)}")

if summary.get('bodies', 0) == 0:
    print("   ❌ FAILED - No body created using sketch ID")
else:
    print("   ✅ SUCCESS - Body created using sketch ID")

# Clear for next test
time.sleep(2)
result = send_command({"action": "clear"})

# Test 4: Mix circle and rectangle in same sketch
print("\n5. Testing mixed entities (circle + rect)...")
csl_ir = {
    "csl": "1.1",
    "meta": {"name": "MixedTest", "units": "mm"},
    "sketches": [
        {
            "id": "s4", 
            "plane": "world.xy", 
            "entities": [
                {"kind": "circle", "id": "c1", "center": "-30,0", "d": "20"},
                {"kind": "rect", "id": "r4", "center": "30,0", "w": "20", "h": "20"}
            ]
        }
    ],
    "features": [
        {"kind": "extrude", "id": "e4a", "profile": "c1", "distance": "15", "op": "new_solid"},
        {"kind": "extrude", "id": "e4b", "profile": "r4", "distance": "15", "op": "new_solid"}
    ]
}

result = send_command({"ir": csl_ir})
print(f"   Result status: {result.get('status')}")
mapping = result.get('mapping', {})
print(f"   Features created: {len(mapping)}")
for feat_id in mapping:
    print(f"      - {feat_id}: {'✅' if 'error' not in mapping[feat_id] else '❌'}")

# Query final state
result = send_command({"action": "query"})
summary = result.get("summary", {})
print(f"   Created - Bodies: {summary.get('bodies', 0)}, Sketches: {summary.get('sketches', 0)}")

print("\n" + "=" * 60)
print("RECTANGLE DEBUG SUMMARY")
print("=" * 60)
