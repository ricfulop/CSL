#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import sys
import threading
import urllib.parse
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer

import requests


def build_authorize_url(client_id: str, redirect_uri: str, scope: str, state: str) -> str:
    params = {
        "response_type": "code",
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "scope": scope,
        "state": state,
    }
    return "https://developer.api.autodesk.com/authentication/v2/authorize?" + urllib.parse.urlencode(params)


class CallbackHandler(BaseHTTPRequestHandler):
    server_version = "OAuth3L/1.0"
    code: str | None = None
    error: str | None = None

    def do_GET(self):  # noqa: N802
        try:
            parsed = urllib.parse.urlparse(self.path)
            qs = urllib.parse.parse_qs(parsed.query)
            if "code" in qs:
                CallbackHandler.code = qs["code"][0]
                body = b"<html><body>Authorization complete. You may close this window.</body></html>"
                self.send_response(200)
                self.send_header("Content-Type", "text/html")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
            else:
                CallbackHandler.error = qs.get("error", ["unknown_error"])[0]
                body = f"<html><body>Authorization failed: {CallbackHandler.error}</body></html>".encode()
                self.send_response(400)
                self.send_header("Content-Type", "text/html")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
        except Exception:
            try:
                self.send_response(500)
                self.end_headers()
            except Exception:
                pass


def exchange_code_for_token(code: str, redirect_uri: str, client_id: str, client_secret: str, scope: str) -> dict:
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect_uri,
        "scope": scope,
    }
    r = requests.post("https://developer.api.autodesk.com/authentication/v2/token", data=data, timeout=20)
    if r.status_code != 200:
        raise RuntimeError(f"Token exchange failed: {r.status_code} {r.text}")
    return r.json()


def main() -> None:
    client_id = os.getenv("APS_CLIENT_ID")
    client_secret = os.getenv("APS_CLIENT_SECRET")
    redirect_uri = os.getenv("APS_REDIRECT_URI", "http://localhost:8765/callback")
    scope = os.getenv("APS_SCOPES_3L", "data:read data:write code:all")
    token_out = os.getenv("APS_TOKEN_FILE", "out/token_3l.json")
    if not (client_id and client_secret):
        print("Set APS_CLIENT_ID and APS_CLIENT_SECRET (Traditional Web App)", file=sys.stderr)
        sys.exit(2)

    # Open browser to authorize
    state = "csl_state"
    url = build_authorize_url(client_id, redirect_uri, scope, state)
    auth_mode = os.getenv("APS_AUTH_MODE", "local").lower()
    if auth_mode == "manual":
        print("Authorize URL (copy/paste in browser):")
        print(url)
        print("After login/consent, copy the full redirected URL and provide the 'code' back using oauth3l-exchange.")
        return
    print(f"Opening browser for consent: {url}")
    # Start local HTTP server for callback
    host, port = "", int(urllib.parse.urlparse(redirect_uri).port or 8765)
    httpd = HTTPServer((host, port), CallbackHandler)
    t = threading.Thread(target=httpd.serve_forever, daemon=True)
    t.start()
    try:
        webbrowser.open(url)
    except Exception:
        print("Please open this URL in your browser:", url)
    # Wait until handler sets the code
    print("Waiting for authorization callback on", redirect_uri)
    for _ in range(600):  # up to 600 seconds
        if CallbackHandler.code or CallbackHandler.error:
            break
        threading.Event().wait(1.0)
    httpd.shutdown()

    if CallbackHandler.error:
        print(f"Authorization failed: {CallbackHandler.error}", file=sys.stderr)
        sys.exit(1)
    if not CallbackHandler.code:
        print("Timed out waiting for authorization code", file=sys.stderr)
        sys.exit(1)

    tokens = exchange_code_for_token(CallbackHandler.code, redirect_uri, client_id, client_secret, scope)
    os.makedirs(os.path.dirname(token_out), exist_ok=True)
    with open(token_out, "w", encoding="utf-8") as f:
        json.dump(tokens, f, indent=2)
    print(f"Saved 3-legged token to {token_out}")


if __name__ == "__main__":
    main()


