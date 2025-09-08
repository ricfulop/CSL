#!/usr/bin/env python3
"""
Test script for Triple Lindy Enhanced CSL backend fix
Tests both direct API and CSL backend for fillet/chamfer operations
"""

import json
import time
from pathlib import Path

# File paths
COMMAND_FILE = Path.home() / "Documents" / "CSL" / "live_command.json"
STATUS_FILE = Path.home() / "Documents" / "CSL" / "live_status.json"

def write_command(command_data):
    """Write a command to the live_command.json file"""
    COMMAND_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(COMMAND_FILE, 'w') as f:
        json.dump(command_data, f, indent=2)
    print(f"Command written to {COMMAND_FILE}")

def read_status():
    """Read the status from live_status.json"""
    if STATUS_FILE.exists():
        with open(STATUS_FILE, 'r') as f:
            return json.load(f)
    return None

def test_direct_api():
    """Test direct Fusion API for fillet/chamfer (should work)"""
    print("\n=== Testing Direct API ===")
    command = {"action": "direct_fillet_test"}
    write_command(command)
    print("Command sent: direct_fillet_test")
    print("Check Fusion 360 for a box with filleted edges")
    time.sleep(2)
    status = read_status()
    if status:
        print(f"Status: {status.get('status', 'unknown')}")
        if 'error' in status:
            print(f"Error: {status['error']}")
    return status

def test_csl_backend():
    """Test CSL backend for fillet/chamfer (testing the fix)"""
    print("\n=== Testing CSL Backend ===")
    command = {
        "ir": {
            "version": "1.3",
            "parameters": {},
            "root": {
                "type": "component",
                "id": "root",
                "sketches": [{
                    "id": "sk1",
                    "plane": "XY",
                    "entities": [{
                        "type": "rectangle",
                        "id": "rect1",
                        "center": [0, 0],
                        "width": 40,
                        "height": 40
                    }]
                }],
                "features": [{
                    "type": "extrude",
                    "id": "ext1",
                    "sketch": "sk1",
                    "profiles": "all",
                    "distance": 30
                }, {
                    "type": "fillet",
                    "id": "fil1",
                    "edges_query": {"type": "all_edges"},
                    "radius": 3
                }, {
                    "type": "chamfer",
                    "id": "chm1",
                    "edges_query": {"type": "all_edges"},
                    "distance": 2
                }]
            }
        }
    }
    write_command(command)
    print("CSL IR command sent with extrude, fillet, and chamfer")
    time.sleep(3)
    status = read_status()
    if status:
        print(f"Status: {status.get('status', 'unknown')}")
        if 'mapping' in status:
            print(f"Mapping created: {len(status['mapping'])} items")
            print(f"Mapping: {status['mapping']}")
        if 'debug' in status:
            debug = status['debug']
            print(f"Debug - Fusion available: {debug.get('fusion_available', 'unknown')}")
            print(f"Debug - Backend import: {debug.get('backend_import', 'unknown')}")
        if 'error' in status:
            print(f"Error: {status['error']}")
    return status

def test_simple_extrude():
    """Test a simple extrude to verify basic CSL functionality"""
    print("\n=== Testing Simple CSL Extrude ===")
    command = {
        "ir": {
            "version": "1.3",
            "parameters": {},
            "root": {
                "type": "component",
                "id": "root",
                "sketches": [{
                    "id": "sk1",
                    "plane": "XY",
                    "entities": [{
                        "type": "circle",
                        "id": "circ1",
                        "center": [0, 0],
                        "radius": 20
                    }]
                }],
                "features": [{
                    "type": "extrude",
                    "id": "ext1",
                    "sketch": "sk1",
                    "profiles": "all",
                    "distance": 50
                }]
            }
        }
    }
    write_command(command)
    print("Simple extrude command sent")
    time.sleep(2)
    status = read_status()
    if status:
        print(f"Status: {status.get('status', 'unknown')}")
        if 'mapping' in status and status['mapping']:
            print("✅ CSL Backend is creating geometry!")
        elif status.get('mapping') == {}:
            print("❌ CSL Backend returned empty mapping (dry-run mode)")
    return status

def main():
    """Run all tests"""
    print("=" * 60)
    print("Triple Lindy Enhanced CSL Backend Test Suite")
    print("=" * 60)
    print("\nMake sure:")
    print("1. Fusion 360 is running")
    print("2. Triple Lindy Enhanced add-in is running")
    print("3. You've deployed the latest fix")
    print("\nPress Enter to start tests...")
    input()
    
    # Test 1: Direct API (should always work)
    test_direct_api()
    time.sleep(3)
    
    # Test 2: Simple CSL extrude (basic test)
    test_simple_extrude()
    time.sleep(3)
    
    # Test 3: CSL with fillet/chamfer (main test)
    test_csl_backend()
    
    print("\n" + "=" * 60)
    print("Tests complete! Check Fusion 360 for the created geometry.")
    print("If you see actual 3D objects, the fix is working!")
    print("If status shows empty mappings {}, the backend is still in dry-run mode.")

if __name__ == "__main__":
    main()
