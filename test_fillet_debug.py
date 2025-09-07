#!/usr/bin/env python3
"""
Debug fillet feature specifically
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
print("FILLET DEBUG TEST")
print("=" * 60)

# Clear and create a box
print("\n1. Creating box for filleting...")
send_command({"action": "clear"})
time.sleep(2)

result = send_command({
    "ir": {
        "csl": "1.1",
        "meta": {"name": "BoxForFillet", "units": "mm"},
        "sketches": [{
            "id": "s1", "plane": "world.xy",
            "entities": [{"kind": "rect", "id": "r1", "center": "0,0", "w": "30", "h": "30"}]
        }],
        "features": [
            {"kind": "extrude", "id": "e1", "profile": "r1", "distance": "30", "op": "new_solid"}
        ]
    }
})
print(f"   Box created: {result.get('status')}")

# Query initial state
result = send_command({"action": "query"})
initial_features = result.get("summary", {}).get("features", 0)
initial_timeline = result.get("summary", {}).get("timeline", 0)
print(f"   Initial state - Features: {initial_features}, Timeline: {initial_timeline}")

# Try to add fillet
print("\n2. Adding fillet to all edges...")
result = send_command({
    "ir": {
        "csl": "1.1",
        "meta": {"name": "AddFillet", "units": "mm"},
        "sketches": [],
        "features": [
            {"kind": "fillet", "id": "f1", "radius": "3"}
        ]
    }
})
print(f"   Fillet result: {json.dumps(result, indent=2)}")

# Query final state
print("\n3. Checking if fillet was actually created...")
result = send_command({"action": "query"})
final_features = result.get("summary", {}).get("features", 0)
final_timeline = result.get("summary", {}).get("timeline", 0)
print(f"   Final state - Features: {final_features}, Timeline: {final_timeline}")

if final_features > initial_features:
    print(f"   ✅ Fillet was created! ({final_features - initial_features} new features)")
else:
    print(f"   ❌ No fillet created")

# Try with explicit edge selection
print("\n4. Testing fillet with edge query...")
result = send_command({"action": "clear"})
time.sleep(2)

# Create box again
send_command({
    "ir": {
        "csl": "1.1",
        "meta": {"name": "BoxForFillet2", "units": "mm"},
        "sketches": [{
            "id": "s1", "plane": "world.xy",
            "entities": [{"kind": "rect", "id": "r1", "center": "0,0", "w": "30", "h": "30"}]
        }],
        "features": [
            {"kind": "extrude", "id": "e1", "profile": "r1", "distance": "30", "op": "new_solid"},
            {"kind": "fillet", "id": "f1", "radius": "3", "edges_query": {"type": "all_edges"}}
        ]
    }
})

result = send_command({"action": "query"})
features = result.get("summary", {}).get("features", 0)
print(f"   With edge query - Features: {features}")

print("\n" + "=" * 60)
print("FILLET DEBUG COMPLETE")
print("=" * 60)
