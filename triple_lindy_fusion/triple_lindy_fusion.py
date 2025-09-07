"""
Triple Lindy Fusion Add-In with WebSocket Support
This version includes WebSocket handling for real-time control
"""
import adsk.core
import adsk.fusion
import json
import threading
import time
import sys
import traceback
from pathlib import Path
from queue import Queue, Empty

# Add parent for backend
addon_path = Path(__file__).parent.parent
if str(addon_path) not in sys.path:
    sys.path.insert(0, str(addon_path))

# Global references
_app = None
_ui = None
_handlers = []
_ws_thread = None
_command_queue = Queue()
_running = False
_timer_id = None
_backend = None

def process_commands():
    """Process commands from the queue on the UI thread"""
    global _command_queue, _app, _ui, _backend
    
    if not _running:
        return False
        
    try:
        # Process one command per timer tick
        if not _command_queue.empty():
            try:
                command = _command_queue.get_nowait()
                
                # Import backend lazily to avoid import issues
                if _backend is None:
                    from triple_lindy.transpilers.fusion360_backend import FusionBackend
                    _backend = FusionBackend()
                    _backend.open_session()
                
                action = command.get("action")
                
                if action == "realize":
                    ir = command.get("ir")
                    if ir:
                        # Show progress
                        if _ui:
                            _ui.progressBar.show("CSL Live", "Realizing design...", 0, 1, 1)
                        
                        # Realize the IR
                        mapping = _backend.realize(ir)
                        
                        # Hide progress
                        if _ui:
                            _ui.progressBar.hide()
                        
                        # Zoom to fit
                        viewport = _app.activeViewport
                        if viewport:
                            viewport.fit()
                        
                        # Show success (brief, non-blocking)
                        if _ui:
                            _ui.messageBox(f"Created {len(mapping)} features", "CSL Live", 0, 1)
                            
                elif action == "ping":
                    if _ui:
                        _ui.messageBox("Pong!", "CSL Live", 0, 1)
                        
                elif action == "clear":
                    # Clear the design
                    design = _app.activeProduct
                    if design and isinstance(design, adsk.fusion.Design):
                        # Clear all features
                        root = design.rootComponent
                        if root.features.count > 0:
                            # Note: This is simplified, real implementation would handle timeline
                            pass
                            
            except Empty:
                pass
            except Exception as e:
                if _ui:
                    _ui.messageBox(f"Command error: {str(e)}", "CSL Error")
                print(f"Error processing command: {e}")
                print(traceback.format_exc())
                
    except Exception as e:
        print(f"Timer error: {e}")
        
    return _running  # Continue if still running

def websocket_listener():
    """WebSocket client thread"""
    global _command_queue, _running
    
    retry_count = 0
    max_retries = 5
    
    while _running and retry_count < max_retries:
        try:
            # Try to import websocket-client
            import websocket
            
            def on_message(ws, message):
                """Handle incoming WebSocket message"""
                try:
                    msg = json.loads(message)
                    msg_type = msg.get("type")
                    
                    if msg_type == "request":
                        payload = msg.get("payload", {})
                        _command_queue.put(payload)
                        
                except json.JSONDecodeError:
                    print(f"Invalid JSON: {message}")
                except Exception as e:
                    print(f"Message handling error: {e}")
                    
            def on_error(ws, error):
                print(f"WebSocket error: {error}")
                
            def on_close(ws, close_status_code, close_msg):
                print(f"WebSocket closed: {close_status_code} - {close_msg}")
                
            def on_open(ws):
                print("WebSocket connected to daemon")
                # Send identification
                ws.send(json.dumps({
                    "type": "event",
                    "payload": {
                        "event": "fusion_connected",
                        "version": "1.0"
                    }
                }))
                
            # Create WebSocket connection
            ws = websocket.WebSocketApp(
                "ws://localhost:9736",
                on_open=on_open,
                on_message=on_message,
                on_error=on_error,
                on_close=on_close
            )
            
            # Run WebSocket (blocking)
            ws.run_forever(ping_interval=20, ping_timeout=10)
            
        except ImportError:
            print("websocket-client not installed, using fallback polling")
            # Fallback to HTTP polling or direct execution
            while _running:
                time.sleep(1)
                # Could implement HTTP polling here
                
        except Exception as e:
            print(f"WebSocket connection failed: {e}")
            retry_count += 1
            if retry_count < max_retries:
                time.sleep(5)  # Wait before retry
            
    print("WebSocket listener stopped")

class TimerHandler(adsk.core.ApplicationCommandEventHandler):
    """Timer handler for processing commands on UI thread"""
    def __init__(self):
        super().__init__()
        
    def notify(self, args):
        """Called periodically by Fusion"""
        try:
            # Process commands and determine if we should continue
            should_continue = process_commands()
            
            # If still running, fire timer again
            if should_continue:
                # Schedule next timer event (100ms)
                adsk.core.Application.get().fireCustomEvent('TL_ProcessCommands')
                
        except Exception as e:
            print(f"Timer handler error: {e}")

def run(context):
    """Main add-in entry point"""
    global _app, _ui, _handlers, _ws_thread, _running, _timer_id
    
    try:
        _app = adsk.core.Application.get()
        _ui = _app.userInterface
        _running = True
        
        print("Starting Triple Lindy Live Loop Add-In...")
        
        # Register custom event for timer
        custom_event = _app.registerCustomEvent('TL_ProcessCommands')
        timer_handler = TimerHandler()
        custom_event.add(timer_handler)
        _handlers.append(timer_handler)
        
        # Start WebSocket listener thread
        _ws_thread = threading.Thread(target=websocket_listener, daemon=True)
        _ws_thread.start()
        
        # Start timer loop
        def start_timer():
            """Start the timer loop"""
            while _running:
                time.sleep(0.1)  # 100ms intervals
                if _running:
                    try:
                        _app.fireCustomEvent('TL_ProcessCommands')
                    except:
                        pass
                        
        timer_thread = threading.Thread(target=start_timer, daemon=True)
        timer_thread.start()
        
        # Try WebSocket first, with fallback message
        try:
            import websocket
            _ui.messageBox(
                "✅ Triple Lindy Live Loop Connected!\n\n" +
                "WebSocket: ws://localhost:9736\n" +
                "Status: Ready for commands",
                "Triple Lindy"
            )
        except ImportError:
            # Offer to install or use fallback
            result = _ui.messageBox(
                "WebSocket library not installed.\n\n" +
                "To install (in Terminal):\n" +
                "pip3 install websocket-client\n\n" +
                "For now, the add-in will use direct execution mode.",
                "Triple Lindy Setup",
                adsk.core.MessageBoxButtonTypes.OKCancelButtonType
            )
            
            if result == adsk.core.DialogResults.DialogOK:
                # Continue with fallback mode
                _ui.messageBox(
                    "Running in direct mode.\n" +
                    "Use Scripts to run CSL commands.",
                    "Triple Lindy"
                )
                
        print("Add-in started successfully")
        
    except Exception as e:
        if _ui:
            _ui.messageBox(f"Failed to start: {str(e)}", "Triple Lindy Error")
        print(f"Startup error: {e}")
        print(traceback.format_exc())

def stop(context):
    """Clean up on add-in stop"""
    global _running, _ws_thread, _app
    
    try:
        _running = False
        
        # Wait briefly for threads to stop
        if _ws_thread and _ws_thread.is_alive():
            _ws_thread.join(timeout=1)
            
        # Unregister custom event
        try:
            _app.unregisterCustomEvent('TL_ProcessCommands')
        except:
            pass
            
        print("Add-in stopped")
        
    except Exception as e:
        print(f"Cleanup error: {e}")
