# Triple Lindy Live Execution Loop Specification v1.0
**Purpose:** Deliver a Cursor/Zed-like live execution loop where you chat with Triple Lindy (TL) and see Autodesk Fusion 360 react immediately on your local machine.

## Executive Summary

Triple Lindy Live Loop provides real-time bidirectional communication between an AI agent and Fusion 360 desktop, enabling instant visual feedback as designs are created and modified through natural language. The architecture leverages our existing CSL transpiler infrastructure while solving the desktop control challenges through a reliable WebSocket-based message passing system.

## Architecture Overview

```
┌──────────────────┐       WebSocket        ┌──────────────────┐
│                  │◄──────────────────────►│                  │
│   TL Daemon      │      (localhost:9736)  │  Fusion Add-In   │
│   (Python)       │                        │  (Python)        │
│                  │                        │                  │
└────────┬─────────┘                        └──────────────────┘
         │                                           │
         │                                           │
    ┌────▼─────┐                           ┌────────▼────────┐
    │   CSL    │                           │   Fusion API    │
    │ Backend  │                           │  (adsk.core/    │
    │          │                           │   adsk.fusion)  │
    └──────────┘                           └─────────────────┘
```

## Core Components

### 1. TL Local Daemon (`triple_lindy_daemon.py`)
- **Role:** Command broker and CSL transpiler host
- **Language:** Python 3.9+
- **Transport:** WebSocket server on `ws://localhost:9736`
- **Features:**
  - WebSocket server for real-time bidirectional communication
  - Command queue with priority levels (immediate/batch)
  - CSL IR compilation and validation
  - Backend capability caching
  - Session management and recovery
  - File system watcher for CSL file changes

### 2. Fusion Add-In (`triple_lindy_fusion/`)
- **Role:** Fusion API executor and state reporter
- **Language:** Python (Fusion's embedded Python 3.9)
- **Transport:** WebSocket client
- **Features:**
  - Persistent WebSocket connection with auto-reconnect
  - Command execution on UI thread via timer polling
  - Real-time geometry creation/modification
  - Selection state reporting
  - Error recovery and rollback
  - Performance telemetry

### 3. Message Protocol
- **Format:** JSON over WebSocket
- **Compression:** Optional zlib for large payloads (>10KB)
- **Schema Version:** 1.0

## Message Protocol Specification

### Message Envelope
```json
{
  "id": "uuid-v4",
  "type": "request|response|event|stream",
  "timestamp": "2025-01-15T10:30:00Z",
  "version": "1.0",
  "payload": {}
}
```

### Request Types

#### 1. Realize CSL IR
```json
{
  "type": "request",
  "payload": {
    "action": "realize",
    "ir": { /* CSL IR object */ },
    "options": {
      "clear_document": false,
      "zoom_to_fit": true,
      "capture_thumbnail": false
    }
  }
}
```

#### 2. Execute Direct API
```json
{
  "type": "request",
  "payload": {
    "action": "exec_api",
    "commands": [
      {"api": "sketch.create", "args": {"plane": "XY"}},
      {"api": "sketch.rect", "args": {"p1": [0,0], "p2": [100,50]}}
    ]
  }
}
```

#### 3. Query State
```json
{
  "type": "request",
  "payload": {
    "action": "query",
    "queries": [
      {"type": "selection", "filter": "edges"},
      {"type": "features", "id": "part1"},
      {"type": "parameters", "scope": "document"}
    ]
  }
}
```

#### 4. File Operations
```json
{
  "type": "request",
  "payload": {
    "action": "file_op",
    "operation": "export",
    "format": "step",
    "path": "~/Desktop/part.step",
    "entities": ["part1", "part2"]
  }
}
```

### Response Types

#### Success Response
```json
{
  "type": "response",
  "payload": {
    "request_id": "original-uuid",
    "status": "success",
    "result": {
      "features_created": 5,
      "mapping": {"sketch1": "id:xyz", "extrude1": "id:abc"},
      "duration_ms": 234
    }
  }
}
```

#### Error Response
```json
{
  "type": "response",
  "payload": {
    "request_id": "original-uuid",
    "status": "error",
    "error": {
      "code": "E2301",
      "message": "Profile not closed",
      "details": {"sketch_id": "s1", "gap": 0.001},
      "stack_trace": "..."
    }
  }
}
```

### Event Types

#### State Change Event
```json
{
  "type": "event",
  "payload": {
    "event": "state_change",
    "changes": [
      {"type": "feature_added", "id": "extrude1"},
      {"type": "selection_changed", "count": 3}
    ]
  }
}
```

#### Progress Event
```json
{
  "type": "event",
  "payload": {
    "event": "progress",
    "operation": "realize",
    "current": 3,
    "total": 10,
    "message": "Creating extrusion..."
  }
}
```

## Implementation Details

### Fusion Add-In Structure
```
triple_lindy_fusion/
├── triple_lindy_fusion.py      # Main add-in entry
├── triple_lindy_fusion.manifest
├── lib/
│   ├── websocket_manager.py    # WebSocket connection handling
│   ├── command_executor.py     # Command execution on UI thread
│   ├── state_reporter.py       # State query and reporting
│   └── error_handler.py        # Error recovery
└── resources/
    └── icons/
```

### Add-In Core Loop (Reliable Implementation)
```python
# triple_lindy_fusion.py
import adsk.core
import adsk.fusion
import threading
import json
import time
from queue import Queue, Empty
from lib.websocket_manager import WebSocketManager

class TripleLindyFusion:
    def __init__(self):
        self.app = adsk.core.Application.get()
        self.ui = self.app.userInterface
        self.ws = None
        self.command_queue = Queue()
        self.timer_handler = None
        
    def start(self):
        """Initialize add-in and start WebSocket connection"""
        # Connect to daemon
        self.ws = WebSocketManager("ws://localhost:9736")
        self.ws.on_message = self.handle_message
        self.ws.connect()
        
        # Create timer for UI thread execution (100ms interval)
        self.timer_handler = self.ui.registerCustomEvent("TL_Timer")
        self.timer_handler.add(self.process_queue)
        self.start_timer()
        
    def start_timer(self):
        """Start repeating timer for command processing"""
        def timer_loop():
            while self.running:
                time.sleep(0.1)  # 100ms
                self.app.fireCustomEvent("TL_Timer")
        
        timer_thread = threading.Thread(target=timer_loop, daemon=True)
        timer_thread.start()
        
    def handle_message(self, message):
        """Handle incoming WebSocket message"""
        msg = json.loads(message)
        if msg["type"] == "request":
            self.command_queue.put(msg)
            
    def process_queue(self, args):
        """Process commands on UI thread (called by timer)"""
        try:
            msg = self.command_queue.get_nowait()
            result = self.execute_command(msg["payload"])
            response = {
                "type": "response",
                "id": msg.get("id"),
                "payload": {
                    "request_id": msg.get("id"),
                    "status": "success",
                    "result": result
                }
            }
            self.ws.send(json.dumps(response))
        except Empty:
            pass  # No commands to process
        except Exception as e:
            # Send error response
            error_response = {
                "type": "response",
                "payload": {
                    "request_id": msg.get("id"),
                    "status": "error",
                    "error": {"message": str(e)}
                }
            }
            self.ws.send(json.dumps(error_response))
```

### TL Daemon Structure
```
triple_lindy_daemon/
├── daemon.py                   # Main daemon entry
├── websocket_server.py        # WebSocket server
├── command_processor.py       # Command routing and validation
├── csl_compiler.py           # CSL to IR compilation
├── backend_manager.py        # Backend capability management
└── config.yaml              # Configuration
```

### Daemon Core Implementation
```python
# daemon.py
import asyncio
import websockets
import json
from pathlib import Path
from triple_lindy.transpilers.fusion360_backend import FusionBackend

class TripleLindyDaemon:
    def __init__(self, port=9736):
        self.port = port
        self.clients = set()
        self.backend = FusionBackend()
        
    async def handle_client(self, websocket, path):
        """Handle WebSocket client connection"""
        self.clients.add(websocket)
        try:
            async for message in websocket:
                await self.process_message(websocket, message)
        finally:
            self.clients.remove(websocket)
            
    async def process_message(self, websocket, message):
        """Process incoming message from Fusion"""
        msg = json.loads(message)
        
        if msg["type"] == "response":
            # Handle response from Fusion
            await self.handle_response(msg)
        elif msg["type"] == "event":
            # Handle event from Fusion
            await self.broadcast_event(msg)
            
    async def send_command(self, command):
        """Send command to all connected Fusion instances"""
        message = json.dumps(command)
        await asyncio.gather(
            *[client.send(message) for client in self.clients]
        )
        
    async def realize_ir(self, ir):
        """Send CSL IR to Fusion for realization"""
        command = {
            "id": str(uuid.uuid4()),
            "type": "request",
            "payload": {
                "action": "realize",
                "ir": ir,
                "options": {"zoom_to_fit": True}
            }
        }
        await self.send_command(command)
        
    def start(self):
        """Start WebSocket server"""
        start_server = websockets.serve(
            self.handle_client, 
            "localhost", 
            self.port
        )
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
```

## Security Model

### Authentication
- Local-only binding (127.0.0.1/::1)
- Optional token-based auth for multi-user scenarios
- Process isolation via user-specific ports

### Sandboxing
- No arbitrary code execution
- Whitelisted API operations only
- Resource limits (max entities, timeout)
- Audit logging of all operations

### Data Protection
- No external network access from add-in
- Local file system access restricted to user directories
- Encrypted storage for sensitive configuration

## Testing Strategy

### Unit Tests
```python
# test_protocol.py
def test_message_serialization():
    msg = Message(type="request", payload={"action": "realize"})
    assert msg.to_json() == '{"type":"request",...}'
    
def test_error_handling():
    with pytest.raises(ProtocolError):
        Message(type="invalid")
```

### Integration Tests
```python
# test_integration.py
async def test_realize_simple_part():
    daemon = TripleLindyDaemon()
    ir = load_fixture("simple_box.json")
    result = await daemon.realize_ir(ir)
    assert result["features_created"] == 2
```

### End-to-End Tests
```python
# test_e2e.py
def test_live_loop():
    # 1. Start daemon
    # 2. Start Fusion with add-in
    # 3. Send CSL command
    # 4. Verify geometry created
    # 5. Query state
    # 6. Verify response
```

## Performance Targets

- **Latency:** < 50ms round-trip for simple commands
- **Throughput:** 100+ commands/second
- **Memory:** < 100MB daemon, < 50MB add-in
- **Startup:** < 2 seconds to ready state
- **Recovery:** < 5 seconds to reconnect after failure

## Extensibility

### Plugin Architecture
```python
class CommandPlugin:
    def can_handle(self, action: str) -> bool:
        pass
    
    def execute(self, payload: dict) -> dict:
        pass
```

### Custom Commands
```json
{
  "action": "custom.analyze_mass",
  "plugin": "physics_analyzer",
  "args": {"units": "kg"}
}
```

### Backend Switching
```json
{
  "action": "switch_backend",
  "backend": "freecad",
  "options": {"port": 9737}
}
```

## Error Handling

### Error Codes
- **E1xxx:** Protocol errors (malformed message, version mismatch)
- **E2xxx:** CSL errors (invalid IR, unsupported feature)
- **E3xxx:** Fusion API errors (operation failed, selection invalid)
- **E4xxx:** System errors (connection lost, resource exhausted)

### Recovery Strategies
1. **Automatic Retry:** Transient failures (network, busy)
2. **Graceful Degradation:** Fallback to simpler operations
3. **State Recovery:** Checkpoint and rollback mechanisms
4. **User Intervention:** Clear error messages with fix suggestions

## Installation & Usage

### Quick Start
```bash
# 1. Install daemon
pip install -e triple_lindy_daemon/

# 2. Install Fusion add-in
cp -r triple_lindy_fusion/ ~/Library/Application\ Support/Autodesk/Autodesk\ Fusion\ 360/API/AddIns/

# 3. Start daemon
tl-daemon start

# 4. Launch Fusion 360
# Add-in auto-connects to daemon

# 5. Send commands via CLI
tl-cli realize examples/box.csl

# Or via Python
from triple_lindy import Client
client = Client()
client.realize_file("examples/box.csl")
```

### Configuration
```yaml
# ~/.triple_lindy/config.yaml
daemon:
  port: 9736
  log_level: INFO
  
fusion:
  auto_connect: true
  reconnect_interval: 5
  
features:
  live_preview: true
  auto_save: false
```

## Roadmap & Future Enhancements

### Phase 1: Core Loop (Current)
- [x] WebSocket transport
- [x] Basic command execution
- [x] CSL IR realization
- [ ] State querying

### Phase 2: Enhanced Features
- [ ] Bi-directional selection sync
- [ ] Live parameter editing
- [ ] Constraint solver integration
- [ ] Multi-document support

### Phase 3: Advanced Capabilities
- [ ] Real-time collaboration
- [ ] Version control integration
- [ ] AI-assisted design suggestions
- [ ] Cloud rendering pipeline

## Appendix A: Complete Message Examples

### Complex Assembly Creation
```json
{
  "type": "request",
  "payload": {
    "action": "realize",
    "ir": {
      "csl": "1.3",
      "assemblies": [
        {
          "id": "main_asm",
          "instances": [
            {"id": "base", "part": "base_plate"},
            {"id": "top", "part": "top_cover", "transform": {...}}
          ],
          "joints": [
            {"type": "rigid", "from": "base", "to": "top"}
          ]
        }
      ]
    }
  }
}
```

### Parametric Update
```json
{
  "type": "request",
  "payload": {
    "action": "update_params",
    "parameters": {
      "thickness": "10 mm",
      "hole_diameter": "8 mm"
    },
    "regenerate": true
  }
}
```

## Appendix B: Troubleshooting Guide

### Common Issues

1. **WebSocket Connection Failed**
   - Check daemon is running: `tl-daemon status`
   - Verify port not in use: `lsof -i :9736`
   - Check firewall settings

2. **Commands Not Executing**
   - Verify add-in loaded in Fusion
   - Check Fusion console for errors
   - Review daemon logs: `tl-daemon logs`

3. **Slow Performance**
   - Reduce command batch size
   - Enable performance logging
   - Check system resources

## Appendix C: CSL Backend Integration

The daemon leverages our existing `FusionBackend` class:

```python
from triple_lindy.transpilers.fusion360_backend import FusionBackend

class CommandProcessor:
    def __init__(self):
        self.backend = FusionBackend()
        
    async def realize(self, ir, options):
        # Compile CSL to Fusion API calls
        self.backend.open_session()
        mapping = self.backend.realize(ir)
        
        # Send to Fusion via WebSocket
        await self.send_to_fusion({
            "action": "exec_batch",
            "commands": self.backend.get_command_buffer()
        })
```

This ensures all our CSL v1.3 features work seamlessly in the live loop.
