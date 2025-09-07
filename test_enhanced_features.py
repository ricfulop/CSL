#!/usr/bin/env python3
"""
Test script for Triple Lindy Enhanced features
Tests all new capabilities systematically
"""

import json
import time
import subprocess
from pathlib import Path

def run_command(cmd_list):
    """Run a file_client_enhanced command"""
    full_cmd = ["python3", "triple_lindy_daemon/file_client_enhanced.py"] + cmd_list
    print(f"  → {' '.join(cmd_list)}")
    result = subprocess.run(full_cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"    ❌ Failed: {result.stderr}")
        return False
    else:
        print(f"    ✅ {result.stdout.strip()}")
        return True

def test_category(name, tests):
    """Test a category of features"""
    print(f"\n{'='*60}")
    print(f"Testing: {name}")
    print(f"{'='*60}")
    
    passed = 0
    failed = 0
    
    for test_name, cmd in tests:
        print(f"\n{test_name}:")
        if run_command(cmd):
            passed += 1
        else:
            failed += 1
        time.sleep(0.5)  # Small delay between commands
    
    print(f"\n{name} Results: {passed} passed, {failed} failed")
    return passed, failed

def main():
    print("🧪 TRIPLE LINDY ENHANCED - COMPREHENSIVE TEST SUITE")
    print("="*60)
    
    total_passed = 0
    total_failed = 0
    
    # 1. Basic Operations
    passed, failed = test_category("Basic Operations", [
        ("Ping", ["ping"]),
        ("Clear design", ["clear"]),
        ("Query state", ["query"]),
    ])
    total_passed += passed
    total_failed += failed
    
    # 2. Parameters
    passed, failed = test_category("Parameters", [
        ("Set parameter", ["param", "set", "--name", "width", "--value", "100mm"]),
        ("Set another", ["param", "set", "--name", "height", "--value", "50mm"]),
        ("List parameters", ["param", "list"]),
        ("Expression", ["param", "expression", "--name", "depth", "--expression", "width/2"]),
        ("Get parameter", ["param", "get", "--name", "width"]),
    ])
    total_passed += passed
    total_failed += failed
    
    # 3. Direct Geometry Creation
    passed, failed = test_category("Direct Geometry", [
        ("Create cylinders", ["direct"]),
        ("Query after creation", ["query"]),
    ])
    total_passed += passed
    total_failed += failed
    
    # 4. Timeline
    passed, failed = test_category("Timeline", [
        ("List timeline", ["timeline", "list"]),
        ("Suppress item", ["timeline", "suppress", "--index", "0"]),
        ("Unsuppress item", ["timeline", "unsuppress", "--index", "0"]),
    ])
    total_passed += passed
    total_failed += failed
    
    # 5. Selection
    passed, failed = test_category("Selection", [
        ("Clear selection", ["select", "clear"]),
        ("Select all bodies", ["select", "body", "--all"]),
        ("Get selection", ["select", "get"]),
        ("Select planar faces", ["select", "face", "--planar", "--all"]),
    ])
    total_passed += passed
    total_failed += failed
    
    # 6. View Control
    passed, failed = test_category("View Control", [
        ("Set iso view", ["view", "set", "--orientation", "iso"]),
        ("Set front view", ["view", "set", "--orientation", "front"]),
        ("Fit view", ["view", "fit"]),
        ("Take screenshot", ["view", "screenshot", "--file", "test_view.png"]),
    ])
    total_passed += passed
    total_failed += failed
    
    # 7. Analysis
    passed, failed = test_category("Analysis", [
        ("Mass properties", ["analyze", "mass"]),
        ("Bounding box", ["analyze", "bbox"]),
    ])
    total_passed += passed
    total_failed += failed
    
    # 8. Export
    passed, failed = test_category("Export", [
        ("Export STEP", ["export", "step", "--file", "test_export.step"]),
        ("Export STL", ["export", "stl", "--file", "test_export.stl", "--quality", "high"]),
    ])
    total_passed += passed
    total_failed += failed
    
    # 9. Undo/Redo
    passed, failed = test_category("Undo/Redo", [
        ("Create checkpoint", ["undo", "checkpoint", "--name", "test_point"]),
        ("List checkpoints", ["undo", "list"]),
        ("Undo one step", ["undo", "undo", "--steps", "1"]),
        ("Redo one step", ["undo", "redo", "--steps", "1"]),
    ])
    total_passed += passed
    total_failed += failed
    
    # 10. Configuration
    passed, failed = test_category("Configuration", [
        ("Get config", ["config", "get"]),
        ("Set units", ["config", "set", "--name", "units", "--value", "mm"]),
    ])
    total_passed += passed
    total_failed += failed
    
    # 11. Batch Operations
    print("\n" + "="*60)
    print("Testing: Batch Operations")
    print("="*60)
    
    # Create batch command file
    batch_commands = [
        {"action": "param", "sub_action": "set", "name": "batch_width", "value": "75mm"},
        {"action": "view", "sub_action": "fit"},
        {"action": "query"}
    ]
    
    batch_file = Path("test_batch.json")
    batch_file.write_text(json.dumps(batch_commands, indent=2))
    
    passed, failed = test_category("Batch", [
        ("Execute batch", ["batch", "--file", "test_batch.json"]),
    ])
    total_passed += passed
    total_failed += failed
    
    # Clean up
    batch_file.unlink()
    
    # Final Report
    print("\n" + "="*60)
    print("FINAL RESULTS")
    print("="*60)
    print(f"Total Tests: {total_passed + total_failed}")
    print(f"✅ Passed: {total_passed}")
    print(f"❌ Failed: {total_failed}")
    
    if total_failed == 0:
        print("\n🎉 ALL TESTS PASSED! Triple Lindy Enhanced is fully operational!")
    else:
        print(f"\n⚠️ {total_failed} tests failed. Check the add-in logs for details.")
    
    return 0 if total_failed == 0 else 1

if __name__ == "__main__":
    exit(main())
