#!/usr/bin/env python3
"""
Verification script to check add-in status and confirm changes
"""

import json
import time
from pathlib import Path

COMMAND_FILE = Path.home() / "Documents" / "CSL" / "live_command.json"
STATUS_FILE = Path.home() / "Documents" / "CSL" / "live_status.json"

def check_addin_ready():
    """Check if the add-in is responding"""
    print("\n=== Checking Add-in Status ===")
    
    # Send a simple test command
    command = {"action": "ping"}
    
    with open(COMMAND_FILE, 'w') as f:
        json.dump(command, f, indent=2)
    
    print("Sending ping to add-in...")
    time.sleep(2)
    
    if STATUS_FILE.exists():
        # Check if status file was updated recently
        import os
        mod_time = os.path.getmtime(STATUS_FILE)
        current_time = time.time()
        
        if current_time - mod_time < 5:  # Updated within last 5 seconds
            with open(STATUS_FILE, 'r') as f:
                status = json.load(f)
            
            if status.get('status') == 'pong':
                print(f"✅ Add-in is running and responsive!")
                return True
            elif '_version' in status.get('mapping', {}):
                version = status['mapping']['_version']
                print(f"✅ Add-in is running! Version: {version}")
                return True
            elif status.get('status') == 'ready':
                print(f"✅ Add-in is ready!")
                return True
            else:
                print(f"⚠️ Add-in responded but may not be fully ready")
                print(f"Status: {json.dumps(status, indent=2)}")
                return False
        else:
            print(f"❌ Status file exists but wasn't updated (last update: {int(current_time - mod_time)}s ago)")
            return False
    else:
        print("❌ No status file found - add-in may not be running")
        return False

def verify_latest_changes():
    """Send a test command that will trigger our debug output"""
    print("\n=== Verifying Latest Changes ===")
    
    # Send a minimal chamfer test
    command = {
        "ir": {
            "version": "1.3",
            "parameters": {},
            "root": {
                "type": "component",
                "id": "root",
                "sketches": [{
                    "id": "sk_verify",
                    "plane": "XY",
                    "entities": [{
                        "type": "circle",
                        "id": "circ_verify",
                        "center": [200, 0],
                        "radius": 10
                    }]
                }],
                "features": [{
                    "type": "extrude",
                    "id": "ext_verify",
                    "sketch": "sk_verify",
                    "profiles": "all",
                    "distance": 10
                }]
            }
        }
    }
    
    with open(COMMAND_FILE, 'w') as f:
        json.dump(command, f, indent=2)
    
    print("Sending verification command...")
    time.sleep(3)
    
    if STATUS_FILE.exists():
        with open(STATUS_FILE, 'r') as f:
            status = json.load(f)
        
        # Check if our debug version string is present
        if 'mapping' in status and '_version' in status['mapping']:
            version = status['mapping']['_version']
            if 'v16-debug' in version:
                print(f"✅ Latest backend version detected: {version}")
                return True
            else:
                print(f"⚠️ Unexpected version: {version}")
                return False
        else:
            print("⚠️ No version info in response")
            return False
    return False

if __name__ == "__main__":
    print("=" * 60)
    print("Add-in Status Verification")
    print("=" * 60)
    
    if check_addin_ready():
        print("\nAdd-in is responding. Checking if latest changes are active...")
        if verify_latest_changes():
            print("\n✅ All systems operational!")
        else:
            print("\n⚠️ Add-in is running but may need to be restarted to load latest changes")
    else:
        print("\n❌ Add-in is not responding. Please:")
        print("1. Open Fusion 360")
        print("2. Go to Utilities → Add-Ins → Scripts and Add-Ins")
        print("3. Find 'triple_lindy_fusion_enhanced'")
        print("4. Click Stop, then Run")
        print("5. Wait for the success message")
        print("6. Run this script again")