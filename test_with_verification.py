#!/usr/bin/env python3
"""
Test Triple Lindy Enhanced with verification
This script tests each feature and verifies the results
"""

import json
import time
import subprocess
from pathlib import Path
from typing import Dict, Any, Tuple

# Define paths
LIVE_COMMAND_FILE = Path.home() / "Documents" / "CSL" / "live_command.json"
LIVE_STATUS_FILE = Path.home() / "Documents" / "CSL" / "live_status.json"

def send_command(command: Dict[str, Any]) -> Dict[str, Any]:
    """Send command and get response"""
    LIVE_COMMAND_FILE.write_text(json.dumps(command, indent=2))
    time.sleep(2)  # Wait for processing
    
    if LIVE_STATUS_FILE.exists():
        return json.loads(LIVE_STATUS_FILE.read_text())
    return {"status": "no_response"}

def verify_result(expected: str, result: Dict[str, Any]) -> Tuple[bool, str]:
    """Verify if result matches expectation"""
    status = result.get("status", "")
    
    # Check for errors first
    if status == "error":
        return False, f"Error: {result.get('error', 'Unknown error')}"
    
    # Check if status matches expected
    if expected in status:
        return True, "Success"
    
    # Check for specific fields based on command
    if expected == "parameter_set" and "parameter" in result:
        return True, f"Parameter set: {result['parameter']}"
    
    if expected == "query" and "summary" in result:
        summary = result["summary"]
        return True, f"Bodies: {summary.get('bodies', 0)}, Sketches: {summary.get('sketches', 0)}"
    
    if expected == "timeline" and "timeline" in result:
        return True, f"Timeline items: {len(result.get('timeline', []))}"
    
    if expected == "selection" and "selected_count" in result:
        return True, f"Selected: {result['selected_count']} items"
    
    return False, f"Unexpected result: {json.dumps(result)[:100]}"

def test_feature(name: str, command: Dict[str, Any], expected: str) -> bool:
    """Test a single feature"""
    print(f"\n{'='*60}")
    print(f"Testing: {name}")
    print(f"Command: {json.dumps(command)[:100]}")
    
    result = send_command(command)
    success, message = verify_result(expected, result)
    
    if success:
        print(f"✅ PASSED: {message}")
    else:
        print(f"❌ FAILED: {message}")
        print(f"Full result: {json.dumps(result, indent=2)}")
    
    return success

def main():
    print("🧪 TRIPLE LINDY ENHANCED - VERIFICATION TEST SUITE")
    print("="*60)
    
    passed = 0
    failed = 0
    
    # Start with a clean slate
    print("\n🔄 Initial Setup...")
    result = send_command({"action": "clear"})
    print(f"Clear result: {result.get('status', 'unknown')}")
    
    # 1. Test Parameters
    tests = [
        ("Set Parameter", 
         {"action": "param", "sub_action": "set", "name": "test_width", "value": "100mm"},
         "success"),
        
        ("Get Parameter",
         {"action": "param", "sub_action": "get", "name": "test_width"},
         "success"),
        
        ("List Parameters",
         {"action": "param", "sub_action": "list"},
         "success"),
    ]
    
    print("\n📐 TESTING PARAMETERS")
    for name, cmd, expected in tests:
        if test_feature(name, cmd, expected):
            passed += 1
        else:
            failed += 1
    
    # 2. Create some geometry to test with
    print("\n🔨 Creating Test Geometry...")
    
    # Create a simple cylinder using CSL
    csl_cylinder = {
        "ir": {
            "csl": "1.1",
            "meta": {"name": "TestCylinder", "units": "mm"},
            "sketches": [
                {"id": "s1", "plane": "world.xy", "entities": [
                    {"kind": "circle", "id": "c1", "center": "0,0", "d": "20"}
                ]}
            ],
            "features": [
                {"kind": "extrude", "id": "e1", "profile": "c1", "distance": "30", "op": "new_solid"}
            ]
        }
    }
    
    result = send_command(csl_cylinder)
    print(f"CSL creation result: {result.get('status', 'unknown')}")
    
    # Query to verify geometry was created
    result = send_command({"action": "query"})
    summary = result.get("summary", {})
    print(f"After creation - Bodies: {summary.get('bodies', 0)}, Sketches: {summary.get('sketches', 0)}")
    
    if summary.get('bodies', 0) > 0:
        print("✅ Geometry created successfully!")
        passed += 1
    else:
        print("❌ Failed to create geometry - this might be the extrude bug!")
        failed += 1
    
    # 3. Test Timeline
    print("\n⏰ TESTING TIMELINE")
    tests = [
        ("List Timeline",
         {"action": "timeline", "sub_action": "list"},
         "timeline"),
         
        ("Suppress First Item",
         {"action": "timeline", "sub_action": "suppress", "index": 0},
         "success"),
         
        ("Unsuppress First Item",
         {"action": "timeline", "sub_action": "unsuppress", "index": 0},
         "success"),
    ]
    
    for name, cmd, expected in tests:
        if test_feature(name, cmd, expected):
            passed += 1
        else:
            failed += 1
    
    # 4. Test Selection
    print("\n🎯 TESTING SELECTION")
    tests = [
        ("Clear Selection",
         {"action": "select", "sub_action": "clear"},
         "success"),
         
        ("Select Bodies",
         {"action": "select", "sub_action": "set", "type": "body", "all": True},
         "success"),
         
        ("Get Selection",
         {"action": "select", "sub_action": "get"},
         "success"),
    ]
    
    for name, cmd, expected in tests:
        if test_feature(name, cmd, expected):
            passed += 1
        else:
            failed += 1
    
    # 5. Test View
    print("\n📷 TESTING VIEW CONTROL")
    tests = [
        ("Set Iso View",
         {"action": "view", "sub_action": "set", "orientation": "iso"},
         "success"),
         
        ("Fit View",
         {"action": "view", "sub_action": "fit"},
         "success"),
    ]
    
    for name, cmd, expected in tests:
        if test_feature(name, cmd, expected):
            passed += 1
        else:
            failed += 1
    
    # 6. Test Analysis
    print("\n📊 TESTING ANALYSIS")
    result = send_command({"action": "analyze", "sub_action": "mass_properties"})
    if "mass_properties" in result:
        print(f"✅ Mass properties: {result['mass_properties']}")
        passed += 1
    else:
        print(f"❌ Analysis failed: {result}")
        failed += 1
    
    # 7. Test Undo/Redo
    print("\n↩️ TESTING UNDO/REDO")
    tests = [
        ("Create Checkpoint",
         {"action": "undo", "sub_action": "checkpoint", "checkpoint_name": "test_point"},
         "success"),
         
        ("List Checkpoints",
         {"action": "undo", "sub_action": "list"},
         "success"),
    ]
    
    for name, cmd, expected in tests:
        if test_feature(name, cmd, expected):
            passed += 1
        else:
            failed += 1
    
    # 8. Test Export
    print("\n📦 TESTING EXPORT")
    result = send_command({
        "action": "export",
        "format": "stl",
        "file_path": "test_export.stl",
        "options": {"quality": "medium"}
    })
    if "exported" in str(result):
        print(f"✅ Export successful: {result.get('exported', 'unknown')}")
        passed += 1
    else:
        print(f"❌ Export failed: {result}")
        failed += 1
    
    # Final Report
    print("\n" + "="*60)
    print("VERIFICATION RESULTS")
    print("="*60)
    print(f"Total Tests: {passed + failed}")
    print(f"✅ Passed: {passed}")
    print(f"❌ Failed: {failed}")
    
    if failed == 0:
        print("\n🎉 ALL FEATURES WORKING CORRECTLY!")
    else:
        print(f"\n⚠️ {failed} features need attention")
        print("\nFailed features might indicate:")
        print("1. The extrude bug we found earlier")
        print("2. Missing implementation")
        print("3. API differences in Fusion version")
    
    # Final comprehensive query
    print("\n📋 FINAL STATE:")
    result = send_command({"action": "query"})
    if "summary" in result:
        summary = result["summary"]
        print(f"Bodies: {summary.get('bodies', 0)}")
        print(f"Sketches: {summary.get('sketches', 0)}")
        print(f"Features: {summary.get('features', 0)}")
        print(f"Timeline: {summary.get('timeline', 0)}")
    
    return 0 if failed == 0 else 1

if __name__ == "__main__":
    exit(main())
