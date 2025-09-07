# Triple Lindy Live Loop - Quick Start (3 Minutes)

## 🚀 Install & Run

### Step 1: Install Dependencies (30 seconds)
```bash
pip install websockets websocket-client
```

### Step 2: Install Fusion Add-In (30 seconds)

**macOS:**
```bash
cp -r triple_lindy_fusion ~/Library/Application\ Support/Autodesk/Autodesk\ Fusion\ 360/API/AddIns/
```

**Windows:**
```cmd
xcopy triple_lindy_fusion "%APPDATA%\Autodesk\Autodesk Fusion 360\API\AddIns\triple_lindy_fusion\" /E /I
```

### Step 3: Start Everything (1 minute)

**Terminal 1 - Start Daemon:**
```bash
python triple_lindy_daemon/daemon.py
# You should see: "Server listening on ws://localhost:9736"
```

**Fusion 360:**
1. Open Fusion 360
2. Tools → Add-Ins → Scripts and Add-Ins
3. Add-Ins tab → Find "triple_lindy_fusion" → Click "Run"
4. You should see: "Triple Lindy Live Loop connected!"

### Step 4: Test It! (1 minute)

**Terminal 2 - Send Commands:**
```bash
# Test connection
python triple_lindy_daemon/tl_client.py ping

# Create a box with holes
python triple_lindy_daemon/tl_client.py example

# You should see geometry appear in Fusion instantly!
```

## ✅ That's It!

You now have real-time control of Fusion 360. The system is ready for:
- AI agent integration
- Automated design workflows  
- Custom scripting
- Live collaborative design

## 🎯 Test Your CSL Files

```bash
# Any CSL IR JSON file
python triple_lindy_daemon/tl_client.py realize your_file.json
```

## 📝 Quick CSL Example

Save as `test.json`:
```json
{
  "csl": "1.1",
  "meta": {"name": "Quick Test", "units": "mm"},
  "sketches": [{
    "id": "s", "plane": "world.xy",
    "entities": [{"kind": "rect", "id": "r", "p1": "0,0", "p2": "40,30"}]
  }],
  "features": [{
    "kind": "extrude", "id": "e", "profile": "r", 
    "distance": "20", "op": "new_solid"
  }]
}
```

Run it:
```bash
python triple_lindy_daemon/tl_client.py realize test.json
```

## 🔧 Troubleshooting

**Nothing happens?**
- Check daemon is running (Terminal 1)
- Check add-in shows connected message
- Try the ping command first

**Connection refused?**
- Start daemon first, then enable add-in
- Check port 9736 is free: `lsof -i :9736`

**WebSocket library missing?**
```bash
pip install websockets websocket-client
```

## 📚 Learn More

- Full spec: `SPEC_TRIPLE_LINDY_LIVE_LOOP.md`
- Installation details: `INSTALL_LIVE_LOOP.md`
- Integration tests: `python test_live_loop.py`

**Success looks like:** Geometry appearing instantly in Fusion as you send commands! 🎉
