#!/usr/bin/env python3
"""
Simple file-based client for Triple Lindy
Writes commands to a file that Fusion watches
"""
import json
import time
import argparse
from pathlib import Path

def send_command(command):
    """Write command to file for Fusion to process"""
    command_file = Path.home() / "Documents" / "CSL" / "live_command.json"
    status_file = Path.home() / "Documents" / "CSL" / "live_status.json"
    
    # Ensure directory exists
    command_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Write command
    with open(command_file, 'w') as f:
        json.dump(command, f, indent=2)
    
    print(f"📤 Sent command to {command_file}")
    
    # Wait for status update
    start_time = time.time()
    last_status = None
    
    while time.time() - start_time < 10:  # 10 second timeout
        if status_file.exists():
            with open(status_file, 'r') as f:
                status = json.load(f)
            
            if status.get("timestamp", 0) > start_time:
                # New status!
                if status.get("status") == "success":
                    print(f"✅ Success! Created {status.get('features_created', 0)} features")
                    return True
                elif status.get("status") == "error":
                    print(f"❌ Error: {status.get('error', 'Unknown error')}")
                    return False
                elif status.get("status") == "pong":
                    print("✅ Pong! Fusion is responding")
                    return True
                elif status.get("status") == "processing":
                    if last_status != "processing":
                        print("⏳ Processing...")
                    last_status = "processing"
        
        time.sleep(0.2)
    
    print("⏱️ Timeout - no response from Fusion")
    return False

def example_command():
    """Create example design"""
    return {
        "ir": {
            "csl": "1.1",
            "meta": {"name": "File Example", "units": "mm"},
            "sketches": [
                {
                    "id": "s",
                    "plane": "world.xy",
                    "entities": [
                        {"kind": "rect", "id": "base", "p1": "0,0", "p2": "60,40"},
                        {"kind": "circle", "id": "h1", "center": "15,20", "d": "8"},
                        {"kind": "circle", "id": "h2", "center": "45,20", "d": "8"}
                    ]
                }
            ],
            "features": [
                {
                    "kind": "extrude",
                    "id": "e",
                    "profile": "base - h1 - h2",
                    "distance": "10",
                    "op": "new_solid",
                    "result": "part"
                },
                {
                    "kind": "fillet",
                    "id": "f",
                    "edges": "query.edges(part).filter(length > 30)",
                    "radius": "3"
                }
            ]
        }
    }

def main():
    parser = argparse.ArgumentParser(description="File-based Triple Lindy client")
    parser.add_argument("command", choices=["ping", "example", "clear", "file", "query", "direct"],
                       help="Command to send")
    parser.add_argument("--file", help="CSL JSON file for 'file' command")
    
    args = parser.parse_args()
    
    if args.command == "ping":
        send_command({"action": "ping"})
    elif args.command == "example":
        send_command(example_command())
    elif args.command == "clear":
        send_command({"action": "clear"})
    elif args.command == "query":
        send_command({"action": "query"})
    elif args.command == "direct":
        send_command({"action": "direct_cylinders"})
    elif args.command == "file":
        if not args.file:
            print("❌ --file required for 'file' command")
            return 1
        with open(args.file, 'r') as f:
            data = json.load(f)
        # Check if data already has 'ir' key
        if "ir" in data:
            send_command(data)
        else:
            send_command({"ir": data})
    
    return 0

if __name__ == "__main__":
    exit(main())
