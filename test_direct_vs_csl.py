#!/usr/bin/env python3
"""
Test direct API vs CSL to isolate the issue
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
    time.sleep(2)
    
    if LIVE_STATUS_FILE.exists():
        return json.loads(LIVE_STATUS_FILE.read_text())
    return {"status": "no_response"}

print("=" * 60)
print("TEST 1: Direct API Cylinders")
print("=" * 60)

# Clear and test direct API
result = send_command({"action": "clear"})
print(f"Clear: {result.get('status')}")

result = send_command({"action": "direct_cylinders"})
print(f"Direct API Result: {json.dumps(result, indent=2)}")

# Query what was created
result = send_command({"action": "query"})
summary = result.get("summary", {})
print(f"After Direct API - Bodies: {summary.get('bodies', 0)}, Sketches: {summary.get('sketches', 0)}")

print("\n" + "=" * 60)
print("TEST 2: CSL Backend")
print("=" * 60)

# Clear and test CSL
result = send_command({"action": "clear"})
print(f"Clear: {result.get('status')}")

# Simple CSL
csl_ir = {
    "csl": "1.1",
    "meta": {"name": "CSLTest", "units": "mm"},
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

result = send_command({"ir": csl_ir})
print(f"CSL Result: {json.dumps(result, indent=2)}")

# Query what was created
result = send_command({"action": "query"})
summary = result.get("summary", {})
print(f"After CSL - Bodies: {summary.get('bodies', 0)}, Sketches: {summary.get('sketches', 0)}")

print("\n" + "=" * 60)
print("COMPARISON:")
print("=" * 60)
print("Direct API creates geometry: ✅" if summary.get('bodies', 0) > 0 else "Direct API creates geometry: ❌")
print("CSL Backend creates geometry: ✅" if summary.get('bodies', 0) > 0 else "CSL Backend creates geometry: ❌")
