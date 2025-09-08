#!/usr/bin/env python3
"""
Test only chamfer operation without the fillet that might be adding extra geometry
"""

import json
import time
from pathlib import Path

COMMAND_FILE = Path.home() / "Documents" / "CSL" / "live_command.json"
STATUS_FILE = Path.home() / "Documents" / "CSL" / "live_status.json"

def test_chamfer_only():
    """Test just chamfer without any other operations"""
    print("\n=== Testing Chamfer Only (No Fillet) ===")
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
        
        # Check chamfer specifically
        chm_value = status.get('mapping', {}).get('chm1', 'NOT FOUND')
        if chm_value.startswith('fusion:chamfer:'):
            print(f"\n✅ SUCCESS! Chamfer created with ID: {chm_value}")
        elif chm_value.startswith('error:'):
            print(f"\n❌ CHAMFER ERROR: {chm_value}")
        else:
            print(f"\n⚠️ Chamfer value: {chm_value}")
        
        print("\n============================================================")
        print("Check Fusion 360:")
        print("- You should see ONLY a box with chamfered edges")
        print("- NO cylinder or other geometry should be present")
    else:
        print("No status file found")

if __name__ == "__main__":
    test_chamfer_only()
