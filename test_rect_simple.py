#!/usr/bin/env python3
"""
Simple test to debug rectangle creation
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
print("SIMPLE RECTANGLE TEST")
print("=" * 60)

# Clear first
print("\n1. Clearing design...")
result = send_command({"action": "clear"})
print(f"   Status: {result.get('status')}")
time.sleep(2)

# Test: Just create a rectangle sketch, no extrude
print("\n2. Creating rectangle sketch only (no extrude)...")
csl_ir = {
    "csl": "1.1",
    "meta": {"name": "RectSketchOnly", "units": "mm"},
    "sketches": [
        {
            "id": "s1", 
            "plane": "world.xy", 
            "entities": [
                {"kind": "rect", "id": "r1", "center": "0,0", "w": "20", "h": "30"}
            ]
        }
    ],
    "features": []  # No features, just sketch
}

result = send_command({"ir": csl_ir})
print(f"   Status: {result.get('status')}")
if "error" in result:
    print(f"   Error: {result.get('error')}")
if "debug" in result:
    print(f"   Debug: {result.get('debug')}")

# Query to see if sketch was created
time.sleep(1)
result = send_command({"action": "query"})
summary = result.get("summary", {})
print(f"   Sketches created: {summary.get('sketches', 0)}")
print(f"   Bodies: {summary.get('bodies', 0)}")

if summary.get('sketches', 0) > 0:
    print("   ✅ Rectangle sketch created successfully")
else:
    print("   ❌ Failed to create rectangle sketch")

print("\n" + "=" * 60)
print("If sketch was created, the issue is with profile resolution.")
print("If sketch wasn't created, the issue is with rectangle entity creation.")
print("=" * 60)
