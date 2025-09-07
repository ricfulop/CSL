#!/usr/bin/env python3
"""
Triple Lindy Daemon - WebSocket server for Fusion 360 live control
"""
from __future__ import annotations

import asyncio
import json
import logging
import sys
import uuid
from pathlib import Path
from typing import Any, Dict, Set

import websockets
# Any type is now just a protocol, use Any for compatibility

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

# For now, we'll just store the backend reference without importing
# The actual backend will be used by the Fusion add-in
# from triple_lindy.transpilers.fusion360_backend import FusionBackend

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class TripleLindyDaemon:
    """WebSocket server daemon for Triple Lindy Live Loop"""
    
    def __init__(self, host: str = "127.0.0.1", port: int = 9736):
        self.host = host
        self.port = port
        self.clients: Set[Any] = set()  # WebSocket connections
        # Backend is used by Fusion add-in, not the daemon
        self.pending_requests: Dict[str, Dict] = {}
        
    async def register_client(self, websocket: Any) -> None:
        """Register a new client connection"""
        self.clients.add(websocket)
        logger.info(f"Client connected: {websocket.remote_address}")
        
        # Send welcome message
        await self.send_to_client(websocket, {
            "type": "event",
            "payload": {
                "event": "connected",
                "version": "1.0",
                "capabilities": self.get_capabilities()
            }
        })
        
    async def unregister_client(self, websocket: Any) -> None:
        """Unregister a client connection"""
        if websocket in self.clients:
            self.clients.remove(websocket)
            logger.info(f"Client disconnected: {websocket.remote_address}")
            
    async def handle_client(self, websocket: Any) -> None:
        """Handle a client WebSocket connection"""
        await self.register_client(websocket)
        try:
            async for message in websocket:
                await self.process_message(websocket, message)
        except websockets.exceptions.ConnectionClosed:
            pass
        except Exception as e:
            logger.error(f"Error handling client: {e}")
        finally:
            await self.unregister_client(websocket)
            
    async def process_message(self, websocket: Any, message: str) -> None:
        """Process an incoming message from a client"""
        try:
            msg = json.loads(message)
            msg_type = msg.get("type")
            msg_id = msg.get("id", str(uuid.uuid4()))
            
            logger.debug(f"Received {msg_type} message: {msg_id}")
            
            if msg_type == "request":
                await self.handle_request(websocket, msg)
            elif msg_type == "response":
                await self.handle_response(websocket, msg)
            elif msg_type == "event":
                await self.handle_event(websocket, msg)
            else:
                await self.send_error(websocket, msg_id, f"Unknown message type: {msg_type}")
                
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON: {e}")
            await self.send_error(websocket, None, "Invalid JSON format")
        except Exception as e:
            logger.error(f"Error processing message: {e}")
            await self.send_error(websocket, None, str(e))
            
    async def handle_request(self, websocket: Any, msg: Dict) -> None:
        """Handle a request message"""
        msg_id = msg.get("id", str(uuid.uuid4()))
        payload = msg.get("payload", {})
        action = payload.get("action")
        
        try:
            if action == "realize":
                await self.handle_realize(websocket, msg_id, payload)
            elif action == "exec_api":
                await self.handle_exec_api(websocket, msg_id, payload)
            elif action == "query":
                await self.handle_query(websocket, msg_id, payload)
            elif action == "file_op":
                await self.handle_file_op(websocket, msg_id, payload)
            elif action == "ping":
                await self.send_response(websocket, msg_id, {"pong": True})
            else:
                await self.send_error(websocket, msg_id, f"Unknown action: {action}")
                
        except Exception as e:
            logger.error(f"Error handling request: {e}")
            await self.send_error(websocket, msg_id, str(e))
            
    async def handle_realize(self, websocket: Any, msg_id: str, payload: Dict) -> None:
        """Handle CSL IR realization request"""
        ir = payload.get("ir")
        options = payload.get("options", {})
        
        if not ir:
            await self.send_error(websocket, msg_id, "Missing 'ir' in payload")
            return
            
        # Store request for tracking
        self.pending_requests[msg_id] = {
            "action": "realize",
            "client": websocket,
            "ir": ir
        }
        
        # Forward to all connected Fusion clients
        fusion_msg = {
            "id": msg_id,
            "type": "request",
            "payload": {
                "action": "realize",
                "ir": ir,
                "options": options
            }
        }
        
        await self.broadcast_to_fusion(fusion_msg)
        
    async def handle_exec_api(self, websocket: Any, msg_id: str, payload: Dict) -> None:
        """Handle direct API execution request"""
        commands = payload.get("commands", [])
        
        if not commands:
            await self.send_error(websocket, msg_id, "Missing 'commands' in payload")
            return
            
        # Forward to Fusion
        fusion_msg = {
            "id": msg_id,
            "type": "request",
            "payload": {
                "action": "exec_api",
                "commands": commands
            }
        }
        
        await self.broadcast_to_fusion(fusion_msg)
        
    async def handle_query(self, websocket: Any, msg_id: str, payload: Dict) -> None:
        """Handle state query request"""
        queries = payload.get("queries", [])
        
        # Forward to Fusion
        fusion_msg = {
            "id": msg_id,
            "type": "request",
            "payload": {
                "action": "query",
                "queries": queries
            }
        }
        
        await self.broadcast_to_fusion(fusion_msg)
        
    async def handle_file_op(self, websocket: Any, msg_id: str, payload: Dict) -> None:
        """Handle file operation request"""
        operation = payload.get("operation")
        
        # Forward to Fusion
        fusion_msg = {
            "id": msg_id,
            "type": "request",
            "payload": payload
        }
        
        await self.broadcast_to_fusion(fusion_msg)
        
    async def handle_response(self, websocket: Any, msg: Dict) -> None:
        """Handle a response message from Fusion"""
        payload = msg.get("payload", {})
        request_id = payload.get("request_id")
        
        if request_id and request_id in self.pending_requests:
            # Forward response to original requester
            req_info = self.pending_requests[request_id]
            original_client = req_info.get("client")
            
            if original_client and original_client in self.clients:
                await self.send_to_client(original_client, msg)
                
            # Clean up
            del self.pending_requests[request_id]
        else:
            # Broadcast to all clients if no specific target
            await self.broadcast(msg)
            
    async def handle_event(self, websocket: Any, msg: Dict) -> None:
        """Handle an event message"""
        # Broadcast events to all clients
        await self.broadcast(msg, exclude=websocket)
        
    async def send_to_client(self, websocket: Any, msg: Dict) -> None:
        """Send a message to a specific client"""
        try:
            if websocket in self.clients:
                await websocket.send(json.dumps(msg))
        except Exception as e:
            logger.error(f"Error sending to client: {e}")
            await self.unregister_client(websocket)
            
    async def broadcast(self, msg: Dict, exclude: Any = None) -> None:
        """Broadcast a message to all clients"""
        disconnected = []
        for client in self.clients:
            if client != exclude:
                try:
                    await client.send(json.dumps(msg))
                except Exception as e:
                    logger.error(f"Error broadcasting to client: {e}")
                    disconnected.append(client)
                    
        # Clean up disconnected clients
        for client in disconnected:
            await self.unregister_client(client)
            
    async def broadcast_to_fusion(self, msg: Dict) -> None:
        """Broadcast a message to Fusion clients only"""
        # In a real implementation, we'd track which clients are Fusion
        # For now, broadcast to all
        await self.broadcast(msg)
        
    async def send_response(self, websocket: Any, msg_id: str, result: Any) -> None:
        """Send a success response"""
        response = {
            "type": "response",
            "payload": {
                "request_id": msg_id,
                "status": "success",
                "result": result
            }
        }
        await self.send_to_client(websocket, response)
        
    async def send_error(self, websocket: Any, msg_id: str, error: str) -> None:
        """Send an error response"""
        response = {
            "type": "response",
            "payload": {
                "request_id": msg_id,
                "status": "error",
                "error": {
                    "message": error
                }
            }
        }
        await self.send_to_client(websocket, response)
        
    def get_capabilities(self) -> Dict:
        """Get daemon capabilities"""
        return {
            "version": "1.0",
            "features": [
                "realize",
                "exec_api",
                "query",
                "file_op"
            ],
            "csl_version": "1.3",
            "backends": ["fusion360"]
        }
        
    async def start_server(self) -> None:
        """Start the WebSocket server"""
        logger.info(f"Starting Triple Lindy daemon on {self.host}:{self.port}")
        
        async with websockets.serve(
            self.handle_client,
            self.host,
            self.port,
            ping_interval=20,
            ping_timeout=10
        ) as server:
            logger.info(f"Server listening on ws://{self.host}:{self.port}")
            await asyncio.Future()  # Run forever
            
    def run(self) -> None:
        """Run the daemon"""
        try:
            asyncio.run(self.start_server())
        except KeyboardInterrupt:
            logger.info("Daemon shutting down...")
        except Exception as e:
            logger.error(f"Daemon error: {e}")
            sys.exit(1)


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Triple Lindy Daemon")
    parser.add_argument("--host", default="127.0.0.1", help="Host to bind to")
    parser.add_argument("--port", type=int, default=9736, help="Port to bind to")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    
    args = parser.parse_args()
    
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
        
    daemon = TripleLindyDaemon(args.host, args.port)
    daemon.run()


if __name__ == "__main__":
    main()
