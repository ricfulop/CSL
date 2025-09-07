#!/usr/bin/env python3
"""
Comprehensive test suite for CSL backend and enhanced add-in features
"""

import json
import time
import sys
from pathlib import Path
from typing import Dict, Any, List, Tuple

# Define paths
LIVE_COMMAND_FILE = Path.home() / "Documents" / "CSL" / "live_command.json"
LIVE_STATUS_FILE = Path.home() / "Documents" / "CSL" / "live_status.json"

# Test results tracking
test_results = {
    "passed": [],
    "failed": [],
    "skipped": []
}

def send_command(command: Dict[str, Any], timeout: float = 3.0) -> Dict[str, Any]:
    """Send command and get response"""
    LIVE_COMMAND_FILE.write_text(json.dumps(command, indent=2))
    time.sleep(timeout)
    
    if LIVE_STATUS_FILE.exists():
        try:
            return json.loads(LIVE_STATUS_FILE.read_text())
        except:
            return {"status": "json_error"}
    return {"status": "no_response"}

def test_feature(category: str, name: str, test_func) -> bool:
    """Run a single test and track results"""
    print(f"\n  Testing: {name}...")
    try:
        success, details = test_func()
        if success:
            print(f"    ✅ PASSED: {details}")
            test_results["passed"].append(f"{category}/{name}")
        else:
            print(f"    ❌ FAILED: {details}")
            test_results["failed"].append(f"{category}/{name}")
        return success
    except Exception as e:
        print(f"    ⚠️ ERROR: {str(e)}")
        test_results["failed"].append(f"{category}/{name}")
        return False

def clear_design():
    """Clear the design"""
    result = send_command({"action": "clear"})
    time.sleep(1)
    return result.get("status") == "cleared"

# ============================================================================
# CSL BACKEND TESTS
# ============================================================================

def test_csl_sketches() -> List[Tuple[bool, str]]:
    """Test CSL sketch creation"""
    tests = []
    
    # Test circle
    clear_design()
    result = send_command({
        "ir": {
            "csl": "1.1",
            "meta": {"name": "CircleTest", "units": "mm"},
            "sketches": [{
                "id": "s1", "plane": "world.xy",
                "entities": [{"kind": "circle", "id": "c1", "center": "0,0", "d": "20"}]
            }],
            "features": []
        }
    })
    query = send_command({"action": "query"})
    success = query.get("summary", {}).get("sketches", 0) > 0
    tests.append((success, "Circle sketch"))
    
    # Test rectangle
    clear_design()
    result = send_command({
        "ir": {
            "csl": "1.1",
            "meta": {"name": "RectTest", "units": "mm"},
            "sketches": [{
                "id": "s1", "plane": "world.xy",
                "entities": [{"kind": "rect", "id": "r1", "center": "0,0", "w": "30", "h": "20"}]
            }],
            "features": []
        }
    })
    query = send_command({"action": "query"})
    success = query.get("summary", {}).get("sketches", 0) > 0
    tests.append((success, "Rectangle sketch"))
    
    # Test line
    clear_design()
    result = send_command({
        "ir": {
            "csl": "1.1",
            "meta": {"name": "LineTest", "units": "mm"},
            "sketches": [{
                "id": "s1", "plane": "world.xy",
                "entities": [{"kind": "line", "id": "l1", "p1": "0,0", "p2": "10,10"}]
            }],
            "features": []
        }
    })
    query = send_command({"action": "query"})
    success = query.get("summary", {}).get("sketches", 0) > 0
    tests.append((success, "Line sketch"))
    
    return tests

def test_csl_features() -> List[Tuple[bool, str]]:
    """Test CSL feature creation"""
    tests = []
    
    # Test extrude
    clear_design()
    result = send_command({
        "ir": {
            "csl": "1.1",
            "meta": {"name": "ExtrudeTest", "units": "mm"},
            "sketches": [{
                "id": "s1", "plane": "world.xy",
                "entities": [{"kind": "circle", "id": "c1", "center": "0,0", "d": "20"}]
            }],
            "features": [
                {"kind": "extrude", "id": "e1", "profile": "c1", "distance": "30", "op": "new_solid"}
            ]
        }
    })
    query = send_command({"action": "query"})
    success = query.get("summary", {}).get("bodies", 0) > 0
    tests.append((success, "Extrude"))
    
    # Test fillet
    if success:  # Only if extrude worked
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
        query = send_command({"action": "query"})
        success = query.get("summary", {}).get("features", 0) > 1
        tests.append((success, "Fillet"))
    else:
        tests.append((False, "Fillet (skipped - no body)"))
    
    return tests

# ============================================================================
# ENHANCED ADD-IN TESTS
# ============================================================================

def test_parameters() -> List[Tuple[bool, str]]:
    """Test parameter operations"""
    tests = []
    
    # Set parameter
    result = send_command({
        "action": "param",
        "sub_action": "set",
        "name": "test_width",
        "value": "50mm"
    })
    tests.append((result.get("status") == "success", "Set parameter"))
    
    # Get parameter
    result = send_command({
        "action": "param",
        "sub_action": "get",
        "name": "test_width"
    })
    tests.append((result.get("status") == "success", "Get parameter"))
    
    # List parameters
    result = send_command({
        "action": "param",
        "sub_action": "list"
    })
    tests.append(("parameters" in result, "List parameters"))
    
    return tests

def test_timeline() -> List[Tuple[bool, str]]:
    """Test timeline operations"""
    tests = []
    
    # First create something
    clear_design()
    send_command({
        "ir": {
            "csl": "1.1",
            "meta": {"name": "TimelineTest", "units": "mm"},
            "sketches": [{
                "id": "s1", "plane": "world.xy",
                "entities": [{"kind": "circle", "id": "c1", "center": "0,0", "d": "20"}]
            }],
            "features": [
                {"kind": "extrude", "id": "e1", "profile": "c1", "distance": "30", "op": "new_solid"}
            ]
        }
    })
    
    # List timeline
    result = send_command({
        "action": "timeline",
        "sub_action": "list"
    })
    tests.append(("timeline" in result, "List timeline"))
    
    # Suppress item
    if "timeline" in result and len(result.get("timeline", [])) > 0:
        result = send_command({
            "action": "timeline",
            "sub_action": "suppress",
            "index": 0
        })
        tests.append((result.get("status") == "success", "Suppress timeline item"))
        
        # Unsuppress item
        result = send_command({
            "action": "timeline",
            "sub_action": "unsuppress",
            "index": 0
        })
        tests.append((result.get("status") == "success", "Unsuppress timeline item"))
    else:
        tests.append((False, "Suppress (no timeline items)"))
        tests.append((False, "Unsuppress (no timeline items)"))
    
    return tests

def test_selection() -> List[Tuple[bool, str]]:
    """Test selection operations"""
    tests = []
    
    # Clear selection
    result = send_command({
        "action": "select",
        "sub_action": "clear"
    })
    tests.append((result.get("status") == "success", "Clear selection"))
    
    # Select all bodies
    result = send_command({
        "action": "select",
        "sub_action": "set",
        "type": "body",
        "all": True
    })
    tests.append((result.get("status") == "success", "Select all bodies"))
    
    # Get selection
    result = send_command({
        "action": "select",
        "sub_action": "get"
    })
    tests.append(("selection" in result, "Get selection"))
    
    return tests

def test_view() -> List[Tuple[bool, str]]:
    """Test view operations"""
    tests = []
    
    # Set iso view
    result = send_command({
        "action": "view",
        "sub_action": "set",
        "orientation": "iso"
    })
    tests.append((result.get("status") == "success", "Set iso view"))
    
    # Fit view
    result = send_command({
        "action": "view",
        "sub_action": "fit"
    })
    tests.append((result.get("status") == "success", "Fit view"))
    
    # Zoom
    result = send_command({
        "action": "view",
        "sub_action": "zoom",
        "zoom_factor": 1.5
    })
    tests.append((result.get("status") == "success", "Zoom"))
    
    return tests

def test_analysis() -> List[Tuple[bool, str]]:
    """Test analysis operations"""
    tests = []
    
    # Mass properties
    result = send_command({
        "action": "analyze",
        "sub_action": "mass_properties"
    })
    tests.append(("mass_properties" in result, "Mass properties"))
    
    # Bounding box
    result = send_command({
        "action": "analyze",
        "sub_action": "bounding_box"
    })
    tests.append(("bounding_boxes" in result, "Bounding box"))
    
    return tests

def test_undo() -> List[Tuple[bool, str]]:
    """Test undo/redo operations"""
    tests = []
    
    # Create checkpoint
    result = send_command({
        "action": "undo",
        "sub_action": "checkpoint",
        "checkpoint_name": "test_checkpoint"
    })
    tests.append((result.get("status") == "success", "Create checkpoint"))
    
    # List checkpoints
    result = send_command({
        "action": "undo",
        "sub_action": "list"
    })
    tests.append(("checkpoints" in result, "List checkpoints"))
    
    return tests

# ============================================================================
# MAIN TEST RUNNER
# ============================================================================

def main():
    print("=" * 70)
    print("COMPREHENSIVE CSL & ENHANCED ADD-IN TEST SUITE")
    print("=" * 70)
    
    # CSL Backend Tests
    print("\n📦 CSL BACKEND TESTS")
    print("-" * 40)
    
    print("\n1. Sketch Entities:")
    for success, name in test_csl_sketches():
        test_feature("CSL/Sketches", name, lambda: (success, ""))
    
    print("\n2. Features:")
    for success, name in test_csl_features():
        test_feature("CSL/Features", name, lambda: (success, ""))
    
    # Enhanced Add-in Tests
    print("\n\n🚀 ENHANCED ADD-IN TESTS")
    print("-" * 40)
    
    print("\n3. Parameters:")
    for success, name in test_parameters():
        test_feature("AddIn/Parameters", name, lambda: (success, ""))
    
    print("\n4. Timeline:")
    for success, name in test_timeline():
        test_feature("AddIn/Timeline", name, lambda: (success, ""))
    
    print("\n5. Selection:")
    for success, name in test_selection():
        test_feature("AddIn/Selection", name, lambda: (success, ""))
    
    print("\n6. View Control:")
    for success, name in test_view():
        test_feature("AddIn/View", name, lambda: (success, ""))
    
    print("\n7. Analysis:")
    for success, name in test_analysis():
        test_feature("AddIn/Analysis", name, lambda: (success, ""))
    
    print("\n8. Undo/Redo:")
    for success, name in test_undo():
        test_feature("AddIn/Undo", name, lambda: (success, ""))
    
    # Final Report
    print("\n" + "=" * 70)
    print("TEST RESULTS SUMMARY")
    print("=" * 70)
    
    total = len(test_results["passed"]) + len(test_results["failed"]) + len(test_results["skipped"])
    print(f"\nTotal Tests: {total}")
    print(f"✅ Passed: {len(test_results['passed'])}")
    print(f"❌ Failed: {len(test_results['failed'])}")
    print(f"⏭️ Skipped: {len(test_results['skipped'])}")
    
    if test_results["failed"]:
        print("\nFailed Tests:")
        for test in test_results["failed"]:
            print(f"  - {test}")
    
    success_rate = (len(test_results["passed"]) / total * 100) if total > 0 else 0
    print(f"\nSuccess Rate: {success_rate:.1f}%")
    
    if success_rate == 100:
        print("\n🎉 ALL TESTS PASSING!")
    elif success_rate >= 80:
        print("\n✅ Most features working well!")
    elif success_rate >= 60:
        print("\n⚠️ Some features need attention")
    else:
        print("\n❌ Significant issues detected")
    
    return 0 if success_rate >= 80 else 1

if __name__ == "__main__":
    print("Starting comprehensive test suite...")
    print("This will test both CSL backend and enhanced add-in features.")
    print()
    
    # Make sure Fusion is ready
    result = send_command({"action": "ping"})
    if result.get("status") != "pong":
        print("❌ Add-in not responding. Please ensure:")
        print("  1. Fusion 360 is running")
        print("  2. Triple Lindy Enhanced add-in is running")
        sys.exit(1)
    
    print("✅ Add-in is responding. Starting tests...")
    time.sleep(2)
    
    sys.exit(main())
