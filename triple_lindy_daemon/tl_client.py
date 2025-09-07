#!/usr/bin/env python3
"""
Triple Lindy Command Line Client
Send commands to the Triple Lindy daemon
"""
from __future__ import annotations

import argparse
import asyncio
import json
import sys
import uuid
from pathlib import Path
from typing import Any, Dict

import websockets


class TripleLindyClient:
    """Command line client for Triple Lindy daemon"""
    
    def __init__(self, url: str = "ws://localhost:9736"):
        self.url = url
        self.websocket = None
        self.response_received = asyncio.Event()
        self.last_response = None
        
    async def connect(self):
        """Connect to the daemon"""
        self.websocket = await websockets.connect(self.url)
        
    async def disconnect(self):
        """Disconnect from the daemon"""
        if self.websocket:
            await self.websocket.close()
            
    async def send_request(self, action: str, payload: Dict) -> Dict:
        """Send a request and wait for response"""
        msg_id = str(uuid.uuid4())
        
        request = {
            "id": msg_id,
            "type": "request",
            "payload": {
                "action": action,
                **payload
            }
        }
        
        # Send request
        await self.websocket.send(json.dumps(request))
        
        # Wait for response
        async for message in self.websocket:
            msg = json.loads(message)
            if msg.get("type") == "response":
                payload = msg.get("payload", {})
                if payload.get("request_id") == msg_id:
                    return msg
                    
        return None
        
    async def realize_ir(self, ir: Dict, options: Dict = None) -> Dict:
        """Realize a CSL IR"""
        payload = {
            "ir": ir,
            "options": options or {"zoom_to_fit": True}
        }
        return await self.send_request("realize", payload)
        
    async def realize_file(self, file_path: str) -> Dict:
        """Realize a CSL IR from file"""
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
            
        with open(path, "r") as f:
            data = json.load(f)
            
        # Handle both direct IR and wrapped format
        ir = data.get("ir", data)
        
        return await self.realize_ir(ir)
        
    async def ping(self) -> Dict:
        """Ping the daemon"""
        return await self.send_request("ping", {})
        
    async def query(self, queries: list) -> Dict:
        """Query Fusion state"""
        return await self.send_request("query", {"queries": queries})
        
    async def export(self, format: str, path: str) -> Dict:
        """Export from Fusion"""
        payload = {
            "action": "file_op",
            "operation": "export",
            "format": format,
            "path": path
        }
        return await self.send_request("file_op", payload)


async def run_example():
    """Run the example plate with hole"""
    ir = {
        "csl": "1.1",
        "meta": {"name": "CLI Example", "units": "mm"},
        "sketches": [
            {
                "id": "s",
                "plane": "world.xy",
                "entities": [
                    {"kind": "rect", "id": "plate", "p1": "0,0", "p2": "100 mm,60 mm"},
                    {"kind": "circle", "id": "h1", "center": "25 mm,20 mm", "d": "10 mm"},
                    {"kind": "circle", "id": "h2", "center": "75 mm,20 mm", "d": "10 mm"},
                    {"kind": "circle", "id": "h3", "center": "25 mm,40 mm", "d": "10 mm"},
                    {"kind": "circle", "id": "h4", "center": "75 mm,40 mm", "d": "10 mm"}
                ]
            }
        ],
        "features": [
            {
                "kind": "extrude",
                "id": "e",
                "profile": "plate - h1 - h2 - h3 - h4",
                "distance": "10 mm",
                "op": "new_solid",
                "result": "part"
            },
            {
                "kind": "fillet",
                "id": "f1",
                "edges": "query.edges(part).filter(length > 50 mm)",
                "radius": "5 mm"
            },
            {
                "kind": "chamfer",
                "id": "c1",
                "edges": "query.edges(h1) + query.edges(h2) + query.edges(h3) + query.edges(h4)",
                "distance": "2 mm"
            }
        ]
    }
    
    client = TripleLindyClient()
    await client.connect()
    
    print("🚀 Sending example to Fusion...")
    response = await client.realize_ir(ir)
    
    payload = response.get("payload", {})
    if payload.get("status") == "success":
        result = payload.get("result", {})
        print(f"✅ Success! Created {result.get('features_created', 0)} features")
        print(f"⏱️  Duration: {result.get('duration_ms', 0)}ms")
    else:
        error = payload.get("error", {})
        print(f"❌ Error: {error.get('message', 'Unknown error')}")
        
    await client.disconnect()


async def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description="Triple Lindy CLI Client")
    
    subparsers = parser.add_subparsers(dest="command", help="Command to run")
    
    # Example command
    example_parser = subparsers.add_parser("example", help="Run example design")
    
    # Realize command
    realize_parser = subparsers.add_parser("realize", help="Realize CSL file")
    realize_parser.add_argument("file", help="CSL IR JSON file")
    
    # Ping command
    ping_parser = subparsers.add_parser("ping", help="Ping the daemon")
    
    # Query command
    query_parser = subparsers.add_parser("query", help="Query Fusion state")
    query_parser.add_argument("--selection", action="store_true", help="Query selection")
    query_parser.add_argument("--features", action="store_true", help="Query features")
    query_parser.add_argument("--parameters", action="store_true", help="Query parameters")
    
    # Export command
    export_parser = subparsers.add_parser("export", help="Export from Fusion")
    export_parser.add_argument("--format", default="step", choices=["step", "stl", "iges"], help="Export format")
    export_parser.add_argument("--output", required=True, help="Output file path")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 1
        
    try:
        if args.command == "example":
            await run_example()
            
        elif args.command == "realize":
            client = TripleLindyClient()
            await client.connect()
            
            print(f"📄 Loading {args.file}...")
            response = await client.realize_file(args.file)
            
            payload = response.get("payload", {})
            if payload.get("status") == "success":
                result = payload.get("result", {})
                print(f"✅ Success! Created {result.get('features_created', 0)} features")
            else:
                error = payload.get("error", {})
                print(f"❌ Error: {error.get('message', 'Unknown error')}")
                
            await client.disconnect()
            
        elif args.command == "ping":
            client = TripleLindyClient()
            await client.connect()
            
            print("🏓 Pinging daemon...")
            response = await client.ping()
            
            payload = response.get("payload", {})
            if payload.get("status") == "success":
                print("✅ Daemon is alive!")
            else:
                print("❌ Ping failed")
                
            await client.disconnect()
            
        elif args.command == "query":
            client = TripleLindyClient()
            await client.connect()
            
            queries = []
            if args.selection:
                queries.append({"type": "selection"})
            if args.features:
                queries.append({"type": "features"})
            if args.parameters:
                queries.append({"type": "parameters"})
                
            if not queries:
                queries = [{"type": "features"}]
                
            print("🔍 Querying Fusion...")
            response = await client.query(queries)
            
            payload = response.get("payload", {})
            if payload.get("status") == "success":
                result = payload.get("result", {})
                print(json.dumps(result, indent=2))
            else:
                error = payload.get("error", {})
                print(f"❌ Error: {error.get('message', 'Unknown error')}")
                
            await client.disconnect()
            
        elif args.command == "export":
            client = TripleLindyClient()
            await client.connect()
            
            print(f"📦 Exporting as {args.format.upper()}...")
            response = await client.export(args.format, args.output)
            
            payload = response.get("payload", {})
            if payload.get("status") == "success":
                result = payload.get("result", {})
                print(f"✅ Exported to: {result.get('exported', args.output)}")
            else:
                error = payload.get("error", {})
                print(f"❌ Error: {error.get('message', 'Unknown error')}")
                
            await client.disconnect()
            
    except FileNotFoundError as e:
        print(f"❌ {e}")
        return 1
    except ConnectionRefusedError:
        print("❌ Cannot connect to daemon. Is it running?")
        print("   Start with: python triple_lindy_daemon/daemon.py")
        return 1
    except KeyboardInterrupt:
        print("\n👋 Interrupted")
        return 0
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1
        
    return 0


if __name__ == "__main__":
    exit(asyncio.run(main()))
