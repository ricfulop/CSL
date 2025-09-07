#!/usr/bin/env python3
"""
Debug the extrude issue specifically
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
    time.sleep(3)  # Wait longer for processing
    
    if LIVE_STATUS_FILE.exists():
        return json.loads(LIVE_STATUS_FILE.read_text())
    return {"status": "no_response"}

def test_extrude(description, csl_ir):
    """Test a specific extrude case"""
    print(f"\n{'='*60}")
    print(f"Testing: {description}")
    
    # Clear first
    result = send_command({"action": "clear"})
    print(f"Clear: {result.get('status')}")
    time.sleep(1)
    
    # Send the CSL
    result = send_command({"ir": csl_ir})
    print(f"CSL Result: {json.dumps(result, indent=2)}")
    
    # Query to see what was created
    result = send_command({"action": "query"})
    summary = result.get("summary", {})
    print(f"Query Result - Bodies: {summary.get('bodies', 0)}, Sketches: {summary.get('sketches', 0)}")
    
    # Check mapping
    if "mapping" in result:
        print(f"Mapping: {result['mapping']}")
    
    return summary.get('bodies', 0) > 0

# Test 1: Simple cylinder with circle ID reference
print("🧪 EXTRUDE DEBUG TESTS")

test1 = {
    "csl": "1.1",
    "meta": {"name": "Test1_CircleID", "units": "mm"},
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

if test_extrude("Extrude with circle ID (c1)", test1):
    print("✅ PASSED")
else:
    print("❌ FAILED")

# Test 2: Extrude with sketch ID reference
test2 = {
    "csl": "1.1",
    "meta": {"name": "Test2_SketchID", "units": "mm"},
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
        {"kind": "extrude", "id": "e1", "profile": "s1", "distance": "30", "op": "new_solid"}
    ]
}

if test_extrude("Extrude with sketch ID (s1)", test2):
    print("✅ PASSED")
else:
    print("❌ FAILED")

# Test 3: Extrude with no profile specified (should use most recent)
test3 = {
    "csl": "1.1",
    "meta": {"name": "Test3_NoProfile", "units": "mm"},
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
        {"kind": "extrude", "id": "e1", "distance": "30", "op": "new_solid"}
    ]
}

if test_extrude("Extrude with no profile (implicit)", test3):
    print("✅ PASSED")
else:
    print("❌ FAILED")

# Test 4: Rectangle extrude
test4 = {
    "csl": "1.1",
    "meta": {"name": "Test4_Rectangle", "units": "mm"},
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

if test_extrude("Extrude with rectangle ID (r1)", test4):
    print("✅ PASSED")
else:
    print("❌ FAILED")

# Test 5: Multiple extrudes
test5 = {
    "csl": "1.1",
    "meta": {"name": "Test5_Multiple", "units": "mm"},
    "sketches": [
        {
            "id": "s1", 
            "plane": "world.xy", 
            "entities": [
                {"kind": "circle", "id": "c1", "center": "0,0", "d": "20"}
            ]
        },
        {
            "id": "s2", 
            "plane": "world.xy", 
            "entities": [
                {"kind": "circle", "id": "c2", "center": "50,0", "d": "15"}
            ]
        }
    ],
    "features": [
        {"kind": "extrude", "id": "e1", "profile": "c1", "distance": "30", "op": "new_solid"},
        {"kind": "extrude", "id": "e2", "profile": "c2", "distance": "20", "op": "new_solid"}
    ]
}

if test_extrude("Multiple extrudes (c1, c2)", test5):
    print("✅ PASSED - Check if 2 bodies created")
else:
    print("❌ FAILED")

print("\n" + "="*60)
print("EXTRUDE DEBUG COMPLETE")
