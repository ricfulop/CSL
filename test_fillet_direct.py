#!/usr/bin/env python3
"""
Test fillet using direct API to isolate the issue
"""

import json
import time
from pathlib import Path

# Define paths
LIVE_COMMAND_FILE = Path.home() / "Documents" / "CSL" / "live_command.json"
LIVE_STATUS_FILE = Path.home() / "Documents" / "CSL" / "live_status.json"

def send_command(command, timeout=3):
    """Send command and get response"""
    LIVE_COMMAND_FILE.write_text(json.dumps(command, indent=2))
    time.sleep(timeout)
    
    if LIVE_STATUS_FILE.exists():
        try:
            return json.loads(LIVE_STATUS_FILE.read_text())
        except:
            return {"status": "json_error"}
    return {"status": "no_response"}

print("=" * 60)
print("DIRECT FILLET TEST")
print("=" * 60)

# Clear
send_command({"action": "clear"})
time.sleep(2)

# Test direct cylinder creation (we know this works)
print("\n1. Creating cylinders with direct API...")
result = send_command({"action": "direct_cylinders"})
print(f"   Result: {result.get('status')}")
print(f"   Bodies created: {result.get('bodies_created', 0)}")

# Query state
result = send_command({"action": "query"})
summary = result.get("summary", {})
print(f"   Current state - Bodies: {summary.get('bodies', 0)}, Features: {summary.get('features', 0)}")

print("\nDirect API works. The issue is in the CSL backend fillet implementation.")
print("The backend might be:")
print("1. Not finding edges correctly")
print("2. Hitting a continue statement in the complex fillet logic")
print("3. Failing silently when adding the fillet")

print("\n" + "=" * 60)
