#!/usr/bin/env python3
"""
Test to see what path the add-in sees
"""

import json
import time
from pathlib import Path

# Define paths
LIVE_COMMAND_FILE = Path.home() / "Documents" / "CSL" / "live_command.json"
LIVE_STATUS_FILE = Path.home() / "Documents" / "CSL" / "live_status.json"

# Send a simple query to trigger the import
command = {"action": "query"}
LIVE_COMMAND_FILE.write_text(json.dumps(command))
time.sleep(2)

print("Query sent to check add-in status...")

# Now try CSL with debug
test_ir = {
    "csl": "1.1",
    "meta": {"name": "PathTest", "units": "mm"},
    "sketches": [],
    "features": []
}

command = {"ir": test_ir}
LIVE_COMMAND_FILE.write_text(json.dumps(command))
time.sleep(2)

if LIVE_STATUS_FILE.exists():
    result = json.loads(LIVE_STATUS_FILE.read_text())
    print("\nResult:")
    print(json.dumps(result, indent=2))
    
    if "debug" in result:
        debug = result["debug"]
        print("\nDebug Info:")
        print(f"- Backend import: {debug.get('backend_import', 'unknown')}")
        print(f"- Path added: {debug.get('path_added', 'not added')}")
        print(f"- Has sketches: {debug.get('has_sketches', False)}")
        print(f"- Has features: {debug.get('has_features', False)}")
else:
    print("No status file found")
