#!/usr/bin/env python3
"""
Enhanced Triple Lindy File Client
Supports all new features in v2.0.0
"""

import json
import time
import argparse
from pathlib import Path
from typing import Dict, Any, List

# Define paths
LIVE_COMMAND_FILE = Path.home() / "Documents" / "CSL" / "live_command.json"
LIVE_STATUS_FILE = Path.home() / "Documents" / "CSL" / "live_status.json"

def send_command(command: Dict[str, Any], wait: bool = True) -> Dict[str, Any]:
    """Send command and optionally wait for response"""
    # Ensure directory exists
    LIVE_COMMAND_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    # Write command
    with open(LIVE_COMMAND_FILE, 'w') as f:
        json.dump(command, f, indent=2)
    
    print(f"📤 Sent: {command.get('action', 'unknown')} {command.get('sub_action', '')}")
    
    if not wait:
        return {"status": "sent"}
    
    # Wait for response
    timeout = 10
    start = time.time()
    last_status = None
    
    while time.time() - start < timeout:
        if LIVE_STATUS_FILE.exists():
            try:
                with open(LIVE_STATUS_FILE, 'r') as f:
                    status = json.load(f)
                    if status != last_status:
                        return status
                    last_status = status
            except json.JSONDecodeError:
                pass
        time.sleep(0.1)
    
    return {"status": "timeout"}

def main():
    parser = argparse.ArgumentParser(
        description="Enhanced Triple Lindy Client",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic commands
  %(prog)s ping
  %(prog)s clear
  %(prog)s query
  
  # Parameters
  %(prog)s param set width 100mm
  %(prog)s param list
  %(prog)s param expression height "width * 2"
  
  # Timeline
  %(prog)s timeline list
  %(prog)s timeline rollback 5
  %(prog)s timeline suppress --name "Fillet1"
  
  # Selection
  %(prog)s select face --planar --all
  %(prog)s select body --indices 0 1 2
  
  # View
  %(prog)s view set iso
  %(prog)s view screenshot output.png
  
  # Export
  %(prog)s export step output.step
  %(prog)s export stl output.stl --quality high
  
  # Analysis
  %(prog)s analyze mass
  %(prog)s analyze bbox
  
  # Batch
  %(prog)s batch commands.json
        """
    )
    
    # Main command
    parser.add_argument("action", 
                       choices=["ping", "clear", "query", "direct", 
                               "param", "timeline", "select", "component", 
                               "joint", "material", "view", "export",
                               "undo", "batch", "analyze", "config", "file"],
                       help="Main action to perform")
    
    # Sub-action (for commands that need it)
    parser.add_argument("sub_action", nargs="?", 
                       help="Sub-action for the command")
    
    # Common arguments
    parser.add_argument("--name", help="Name parameter")
    parser.add_argument("--value", help="Value parameter")
    parser.add_argument("--file", help="File path")
    parser.add_argument("--index", type=int, help="Index parameter")
    parser.add_argument("--indices", nargs="+", type=int, help="Multiple indices")
    parser.add_argument("--all", action="store_true", help="Select all")
    parser.add_argument("--type", help="Entity type")
    parser.add_argument("--format", help="Export format")
    parser.add_argument("--quality", choices=["low", "medium", "high"], help="Quality setting")
    parser.add_argument("--orientation", help="View orientation")
    parser.add_argument("--steps", type=int, help="Number of steps")
    parser.add_argument("--range", nargs=2, type=int, help="Range of indices")
    parser.add_argument("--expression", help="Parameter expression")
    parser.add_argument("--comment", help="Comment/description")
    parser.add_argument("--no-wait", action="store_true", help="Don't wait for response")
    
    # Filter arguments for selection
    parser.add_argument("--planar", action="store_true", help="Select planar faces")
    parser.add_argument("--cylindrical", action="store_true", help="Select cylindrical faces")
    parser.add_argument("--area-gt", type=float, help="Area greater than")
    parser.add_argument("--area-lt", type=float, help="Area less than")
    
    args = parser.parse_args()
    
    # Build command based on action
    command = {"action": args.action}
    
    # Handle different actions
    if args.action == "ping":
        pass  # No additional parameters needed
    
    elif args.action == "clear":
        pass  # No additional parameters needed
    
    elif args.action == "query":
        pass  # No additional parameters needed
    
    elif args.action == "direct":
        command["action"] = "direct_cylinders"
    
    elif args.action == "param":
        if not args.sub_action:
            print("❌ param requires sub_action (set|get|list|delete|expression)")
            return 1
        command["sub_action"] = args.sub_action
        if args.name:
            command["name"] = args.name
        if args.value:
            command["value"] = args.value
        if args.expression:
            command["expression"] = args.expression
        if args.comment:
            command["comment"] = args.comment
    
    elif args.action == "timeline":
        if not args.sub_action:
            print("❌ timeline requires sub_action (list|rollback|suppress|unsuppress|delete)")
            return 1
        command["sub_action"] = args.sub_action
        if args.index is not None:
            command["index"] = args.index
        if args.name:
            command["feature_name"] = args.name
        if args.range:
            command["range"] = args.range
    
    elif args.action == "select":
        if not args.sub_action:
            args.sub_action = "set"  # Default to set
        command["sub_action"] = args.sub_action
        if args.type:
            command["type"] = args.type
        if args.all:
            command["all"] = True
        if args.indices:
            command["indices"] = args.indices
        
        # Build filters
        filters = {}
        if args.planar:
            filters["planar"] = True
        if args.cylindrical:
            filters["cylindrical"] = True
        if args.area_gt:
            filters["area_gt"] = args.area_gt
        if args.area_lt:
            filters["area_lt"] = args.area_lt
        if args.name:
            filters["name"] = args.name
        if filters:
            command["filters"] = filters
    
    elif args.action == "view":
        if not args.sub_action:
            print("❌ view requires sub_action (set|fit|zoom|screenshot)")
            return 1
        command["sub_action"] = args.sub_action
        if args.orientation:
            command["orientation"] = args.orientation
        if args.sub_action == "screenshot":
            if args.file:
                command["screenshot_path"] = args.file
    
    elif args.action == "export":
        if not args.sub_action:
            print("❌ export requires format (step|stl|iges|f3d)")
            return 1
        command["format"] = args.sub_action
        if args.file:
            command["file_path"] = args.file
        options = {}
        if args.quality:
            options["quality"] = args.quality
        if options:
            command["options"] = options
    
    elif args.action == "analyze":
        if not args.sub_action:
            args.sub_action = "mass_properties"
        
        # Handle shortcuts
        if args.sub_action == "mass":
            args.sub_action = "mass_properties"
        elif args.sub_action == "bbox":
            args.sub_action = "bounding_box"
        
        command["sub_action"] = args.sub_action
    
    elif args.action == "undo":
        command["sub_action"] = args.sub_action or "undo"
        if args.steps:
            command["steps"] = args.steps
        if args.name:
            command["checkpoint_name"] = args.name
    
    elif args.action == "config":
        command["sub_action"] = args.sub_action or "get"
    
    elif args.action == "batch":
        if not args.file:
            print("❌ batch requires --file with commands JSON")
            return 1
        with open(args.file, 'r') as f:
            commands = json.load(f)
        command["commands"] = commands
    
    elif args.action == "file":
        if not args.file:
            print("❌ file command requires --file")
            return 1
        with open(args.file, 'r') as f:
            data = json.load(f)
        # Check if data already has 'ir' key
        if "ir" in data:
            command = data
        else:
            command = {"ir": data}
    
    # Send command
    result = send_command(command, wait=not args.no_wait)
    
    # Display result
    if result.get("status") == "timeout":
        print("⏱️ Timeout - no response from Fusion")
        return 1
    elif result.get("status") == "error":
        print(f"❌ Error: {result.get('error', 'Unknown error')}")
        return 1
    elif result.get("status") == "pong":
        print("✅ Pong! Fusion is responding")
    else:
        print(f"✅ {result.get('status', 'Success')}")
        
        # Show relevant details
        if "parameters" in result:
            print("\nParameters:")
            for param in result["parameters"]:
                print(f"  {param['name']} = {param['value']} {param.get('unit', '')}")
        
        if "timeline" in result:
            print(f"\nTimeline: {len(result['timeline'])} items")
            for item in result["timeline"][:5]:
                print(f"  [{item['index']}] {item['name']} ({item['type']})")
        
        if "selection" in result:
            print(f"\nSelected: {len(result['selection'])} items")
        
        if "mass_properties" in result:
            print("\nMass Properties:")
            for prop in result["mass_properties"]:
                print(f"  {prop['body']}: {prop['mass']:.3f} kg, {prop['volume']:.3f} cm³")
        
        if "bounding_boxes" in result:
            print("\nBounding Boxes:")
            for bbox in result["bounding_boxes"]:
                size = bbox["size"]
                print(f"  {bbox['body']}: {size[0]:.1f} x {size[1]:.1f} x {size[2]:.1f} cm")
    
    return 0

if __name__ == "__main__":
    exit(main())
