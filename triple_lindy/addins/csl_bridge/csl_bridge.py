"""Fusion Add-In: CSL Bridge (HTTP)

Simple HTTP bridge for remote control of Fusion.
"""
from __future__ import annotations

import json
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

# Fusion API
import adsk.core  # type: ignore

# Import Fusion backend
from triple_lindy.transpilers.fusion360_backend import FusionBackend

HOST = "127.0.0.1"
PORT = 8765

_app: adsk.core.Application | None = None
_ui: adsk.core.UserInterface | None = None
_httpd: ThreadingHTTPServer | None = None
_server_thread: threading.Thread | None = None
_command_queue = []
_command_lock = threading.Lock()

class _RequestHandler(BaseHTTPRequestHandler):
    def _send(self, code: int, body):
        data = json.dumps(body).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, fmt, *args):
        pass  # quiet

    def do_GET(self):
        if self.path == "/ping":
            self._send(200, {"ok": True})
        elif self.path == "/status":
            self._send(200, {"ok": True, "queue_size": len(_command_queue)})
        else:
            self._send(404, {"ok": False, "error": "not_found"})

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(length) if length > 0 else b"{}"
        try:
            payload = json.loads(raw.decode("utf-8")) if raw else {}
        except:
            payload = {}

        if self.path == "/run_example":
            with _command_lock:
                _command_queue.append({"cmd": "run_example"})
            self._send(200, {"ok": True, "queued": True})
            return
        elif self.path == "/realize":
            ir = payload.get("ir")
            if ir:
                with _command_lock:
                    _command_queue.append({"cmd": "realize", "ir": ir})
                self._send(200, {"ok": True, "queued": True})
                return
        return self._send(400, {"ok": False, "error": "bad_request"})

def _process_commands():
    """Process queued commands on UI thread"""
    while True:
        time.sleep(0.1)  # Check every 100ms

        cmd = None
        with _command_lock:
            if _command_queue:
                cmd = _command_queue.pop(0)

        if cmd:
            try:
                if cmd["cmd"] == "run_example":
                    _handle_run_example()
                elif cmd["cmd"] == "realize":
                    _handle_realize(cmd["ir"])
            except Exception as e:
                if _ui:
                    try:
                        _ui.messageBox(f"Command failed: {e}")
                    except:
                        pass

def _handle_run_example():
    try:
        backend = FusionBackend()
        backend.open_session()

        ir = {
            "csl": "1.1",
            "meta": {"name": "Remote Example", "units": "mm"},
            "sketches": [
                {"id": "s", "plane": "world.xy", "entities": [
                    {"kind": "rect", "id": "plate", "p1": "0,0", "p2": "80 mm,60 mm"},
                    {"kind": "circle", "id": "h1", "center": "20 mm,20 mm", "d": "8 mm"}
                ]}
            ],
            "features": [
                {"kind": "extrude", "id": "e", "profile": "plate - h1", "distance": "8 mm", "op": "new_solid", "result": "part"},
                {"kind": "fillet", "id": "f", "edges": "query.edges(part)", "radius": "4 mm"}
            ]
        }

        mapping = backend.realize(ir)

        # Zoom to fit
        if _app and _app.activeViewport:
            try:
                _app.activeViewport.fit()
            except:
                pass

        if _ui:
            try:
                _ui.messageBox("CSL Remote: Example completed!")
            except:
                pass

    except Exception as e:
        if _ui:
            try:
                _ui.messageBox(f"CSL Remote: Example failed - {e}")
            except:
                pass

def _handle_realize(ir):
    try:
        backend = FusionBackend()
        backend.open_session()
        mapping = backend.realize(ir)

        # Zoom to fit
        if _app and _app.activeViewport:
            try:
                _app.activeViewport.fit()
            except:
                pass

        if _ui:
            try:
                _ui.messageBox("CSL Remote: IR realized!")
            except:
                pass

    except Exception as e:
        if _ui:
            try:
                _ui.messageBox(f"CSL Remote: Realize failed - {e}")
            except:
                pass

def _start_server():
    global _httpd, _server_thread
    try:
        _httpd = ThreadingHTTPServer((HOST, PORT), _RequestHandler)
        _httpd.daemon_threads = True
        _server_thread = threading.Thread(target=_httpd.serve_forever, name="CSLBridgeHTTP", daemon=True)
        _server_thread.start()
    except:
        _httpd = None
        _server_thread = None

def _stop_server():
    global _httpd, _server_thread
    try:
        if _httpd:
            _httpd.shutdown()
            _httpd.server_close()
    except:
        pass
    _httpd = None
    _server_thread = None

def run(context):
    global _app, _ui
    try:
        _app = adsk.core.Application.get()
        _ui = _app.userInterface if _app else None

        _start_server()

        # Start command processor thread (will run on UI thread)
        command_thread = threading.Thread(target=_process_commands, name="CSLCommandProcessor", daemon=True)
        command_thread.start()

        if _ui:
            try:
                _ui.messageBox(f"CSL HTTP Bridge running on http://{HOST}:{PORT}\n\nTest with:\ncurl http://{HOST}:{PORT}/ping\ncurl -X POST http://{HOST}:{PORT}/run_example")
            except:
                pass
    except Exception as e:
        if _ui:
            try:
                _ui.messageBox(f"CSL Bridge failed: {e}")
            except:
                pass

def stop(context):
    try:
        _stop_server()
        if _ui:
            try:
                _ui.messageBox("CSL Bridge stopped.")
            except:
                pass
    except:
        pass