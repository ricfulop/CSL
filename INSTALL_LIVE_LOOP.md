# Triple Lindy Live Loop - Quick Installation Guide

## Prerequisites
- Python 3.9+ installed
- Fusion 360 installed and running
- WebSocket libraries: `pip install websockets websocket-client`

## Installation Steps

### 1. Install the Daemon

```bash
# Install WebSocket dependencies
pip install websockets websocket-client

# Optional: Install as package for CLI commands
cd triple_lindy_daemon
pip install -e .
cd ..
```

### 2. Install Fusion Add-In

**macOS:**
```bash
cp -r triple_lindy_fusion ~/Library/Application\ Support/Autodesk/Autodesk\ Fusion\ 360/API/AddIns/
```

**Windows:**
```cmd
xcopy triple_lindy_fusion "%APPDATA%\Autodesk\Autodesk Fusion 360\API\AddIns\triple_lindy_fusion\" /E /I
```

**Linux:**
```bash
cp -r triple_lindy_fusion ~/.config/Autodesk/Autodesk\ Fusion\ 360/API/AddIns/
```

### 3. Start the Daemon

```bash
# Method 1: Direct Python
python triple_lindy_daemon/daemon.py

# Method 2: If installed as package
tl-daemon

# The daemon will start on ws://localhost:9736
```

### 4. Enable Add-In in Fusion 360

1. Open Fusion 360
2. Go to Tools → Add-Ins → Scripts and Add-Ins
3. Switch to "Add-Ins" tab
4. Find "triple_lindy_fusion" in the list
5. Click "Run" (and optionally check "Run on Startup")
6. You should see: "Triple Lindy Live Loop connected!"

## Testing the Connection

### Method 1: Command Line Client

```bash
# Test connection
python triple_lindy_daemon/tl_client.py ping

# Run example design
python triple_lindy_daemon/tl_client.py example

# Realize a CSL file
python triple_lindy_daemon/tl_client.py realize path/to/file.json
```

### Method 2: Direct WebSocket

```bash
# Using websocat or similar tool
echo '{"type":"request","id":"test","payload":{"action":"ping"}}' | websocat ws://localhost:9736
```

### Method 3: Python Script

```python
import asyncio
import websockets
import json

async def test():
    async with websockets.connect("ws://localhost:9736") as ws:
        # Send ping
        await ws.send(json.dumps({
            "type": "request",
            "id": "test",
            "payload": {"action": "ping"}
        }))
        
        # Get response
        response = await ws.recv()
        print(json.loads(response))

asyncio.run(test())
```

## Example CSL File

Create `test_box.json`:
```json
{
  "csl": "1.1",
  "meta": {"name": "Test Box", "units": "mm"},
  "sketches": [
    {
      "id": "s",
      "plane": "world.xy",
      "entities": [
        {"kind": "rect", "id": "box", "p1": "0,0", "p2": "50 mm,30 mm"}
      ]
    }
  ],
  "features": [
    {
      "kind": "extrude",
      "id": "e",
      "profile": "box",
      "distance": "20 mm",
      "op": "new_solid",
      "result": "part"
    }
  ]
}
```

Then realize it:
```bash
python triple_lindy_daemon/tl_client.py realize test_box.json
```

## Troubleshooting

### Daemon won't start
- Check port 9736 is free: `lsof -i :9736`
- Check Python version: `python --version` (needs 3.9+)

### Add-In doesn't connect
- Check daemon is running
- Check firewall isn't blocking localhost connections
- Check Fusion console: View → Show Text Commands

### Commands don't execute
- Check Fusion has an active document open
- Check daemon logs for errors
- Try the ping command first

### WebSocket library missing
```bash
pip install websockets websocket-client
```

## Architecture Overview

```
Your Computer
├── Daemon (Python Process)
│   ├── WebSocket Server (port 9736)
│   ├── CSL Transpiler
│   └── Command Router
│
├── Fusion 360
│   ├── Add-In (triple_lindy_fusion)
│   ├── WebSocket Client
│   └── API Executor
│
└── CLI/Scripts
    ├── tl_client.py
    └── Your automation scripts
```

## Next Steps

1. **Test the example**: Run the example to verify everything works
2. **Try your CSL files**: Realize your existing CSL designs
3. **Build automation**: Create scripts that send commands to the daemon
4. **Integrate with AI**: Connect your AI agent to send commands

## Support

- Check logs: `~/Documents/CSL/logs/triple_lindy_fusion.log`
- Daemon debug mode: `python daemon.py --debug`
- Test connection: `tl-cli ping`
