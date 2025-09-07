#!/usr/bin/env python3
"""
Safe test for extrude functionality - one test at a time with delays
"""

import json
import time
import sys
from pathlib import Path

# Define paths
LIVE_COMMAND_FILE = Path.home() / "Documents" / "CSL" / "live_command.json"
LIVE_STATUS_FILE = Path.home() / "Documents" / "CSL" / "live_status.json"

def send_command(command):
    """Send command and get response"""
    LIVE_COMMAND_FILE.write_text(json.dumps(command, indent=2))
    time.sleep(3)  # Longer delay for safety
    
    if LIVE_STATUS_FILE.exists():
        return json.loads(LIVE_STATUS_FILE.read_text())
    return {"status": "no_response"}

def test_single_extrude():
    """Test a single simple extrude"""
    print("=" * 60)
    print("SAFE EXTRUDE TEST")
    print("=" * 60)
    
    # Clear first
    print("\n1. Clearing design...")
    result = send_command({"action": "clear"})
    print(f"   Status: {result.get('status')}")
    time.sleep(2)  # Extra delay after clear
    
    # Create a simple cylinder
    print("\n2. Creating cylinder via CSL...")
    csl_ir = {
        "csl": "1.1",
        "meta": {"name": "SafeTest", "units": "mm"},
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
    
    if result.get("status") == "success":
        mapping = result.get("mapping", {})
        if mapping:
            print(f"   ✅ SUCCESS - Created {len(mapping)} features")
            for key in mapping:
                print(f"      - {key}: created")
        else:
            print("   ❌ FAILED - No features created")
    else:
        print(f"   ❌ ERROR: {result.get('error', 'Unknown error')}")
    
    time.sleep(2)
    
    # Query what was created
    print("\n3. Querying design state...")
    result = send_command({"action": "query"})
    summary = result.get("summary", {})
    
    print(f"   Bodies:   {summary.get('bodies', 0)}")
    print(f"   Sketches: {summary.get('sketches', 0)}")
    print(f"   Features: {summary.get('features', 0)}")
    print(f"   Timeline: {summary.get('timeline', 0)} items")
    
    # Final verdict
    print("\n" + "=" * 60)
    if summary.get('bodies', 0) > 0:
        print("✅ EXTRUDE IS WORKING!")
        print(f"   Successfully created {summary.get('bodies', 0)} body/bodies")
    else:
        print("❌ EXTRUDE FAILED")
        print("   No bodies were created")
    
    return summary.get('bodies', 0) > 0

if __name__ == "__main__":
    print("Starting safe extrude test...")
    print("This test will:")
    print("1. Clear the design")
    print("2. Create a simple cylinder")
    print("3. Verify the result")
    print()
    
    input("Press Enter when Fusion is ready (make sure the add-in is running)...")
    
    success = test_single_extrude()
    
    print("\n" + "=" * 60)
    print("TEST COMPLETE")
    print("=" * 60)
    
    sys.exit(0 if success else 1)
