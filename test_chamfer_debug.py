#!/usr/bin/env python3
"""
Debug test specifically for chamfer issues
"""

import json
import time
from pathlib import Path

COMMAND_FILE = Path.home() / "Documents" / "CSL" / "live_command.json"
STATUS_FILE = Path.home() / "Documents" / "CSL" / "live_status.json"

def test_chamfer_only():
    """Test just chamfer on a simple box"""
    print("\n=== Testing Chamfer Only ===")
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
                        "width": 60,
                        "height": 60
                    }]
                }],
                "features": [{
                    "type": "extrude",
                    "id": "ext1",
                    "sketch": "sk1",
                    "profiles": "all",
                    "distance": 40
                }, {
                    "type": "chamfer",
                    "id": "chm1",
                    "edges_query": {"type": "all_edges"},
                    "distance": 2
                }]
            }
        }
    }
    
    with open(COMMAND_FILE, 'w') as f:
        json.dump(command, f, indent=2)
    
    print("Command sent - waiting for processing...")
    time.sleep(3)
    
    if STATUS_FILE.exists():
        with open(STATUS_FILE, 'r') as f:
            status = json.load(f)
        
        print(f"Status: {status.get('status')}")
        print(f"\nMapping:")
        for key, value in status.get('mapping', {}).items():
            print(f"  {key}: {value}")
        
        if 'error' in status:
            print(f"\nERROR: {status['error']}")
        
        if 'traceback' in status:
            print(f"\nTRACEBACK:\n{status['traceback']}")
        
        # Check chamfer specifically
        chm_value = status.get('mapping', {}).get('chm1', 'NOT FOUND')
        if chm_value.startswith('fusion:chamfer:'):
            print(f"\n✅ SUCCESS! Chamfer created with ID: {chm_value}")
        elif chm_value.startswith('error:'):
            print(f"\n❌ CHAMFER ERROR: {chm_value}")
        elif chm_value == 'processing_chamfer':
            print(f"\n⚠️ CHAMFER STUCK: Still shows 'processing_chamfer'")
            print("This suggests the chamfer code is not completing properly")
        else:
            print(f"\n⚠️ UNEXPECTED: Chamfer value is '{chm_value}'")

def test_fillet_only():
    """Test just fillet for comparison"""
    print("\n=== Testing Fillet Only (for comparison) ===")
    command = {
        "ir": {
            "version": "1.3",
            "parameters": {},
            "root": {
                "type": "component",
                "id": "root",
                "sketches": [{
                    "id": "sk2",
                    "plane": "XY",
                    "entities": [{
                        "type": "circle",
                        "id": "circ1",
                        "center": [100, 0],
                        "radius": 30
                    }]
                }],
                "features": [{
                    "type": "extrude",
                    "id": "ext2",
                    "sketch": "sk2",
                    "profiles": "all",
                    "distance": 40
                }, {
                    "type": "fillet",
                    "id": "fil1",
                    "edges_query": {"type": "all_edges"},
                    "radius": 5
                }]
            }
        }
    }
    
    with open(COMMAND_FILE, 'w') as f:
        json.dump(command, f, indent=2)
    
    print("Command sent - waiting for processing...")
    time.sleep(3)
    
    if STATUS_FILE.exists():
        with open(STATUS_FILE, 'r') as f:
            status = json.load(f)
        
        fil_value = status.get('mapping', {}).get('fil1', 'NOT FOUND')
        if fil_value.startswith('fusion:fillet:'):
            print(f"✅ Fillet created successfully: {fil_value[:50]}...")
        else:
            print(f"⚠️ Fillet value: {fil_value}")

if __name__ == "__main__":
    print("=" * 60)
    print("Chamfer Debug Test")
    print("=" * 60)
    
    test_chamfer_only()
    time.sleep(2)
    test_fillet_only()
    
    print("\n" + "=" * 60)
    print("Check Fusion 360:")
    print("- You should see a box with chamfered edges")
    print("- You should see a cylinder with filleted edges")
