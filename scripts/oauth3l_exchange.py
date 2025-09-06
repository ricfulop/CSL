#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import sys
import urllib.parse

import requests


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: oauth3l_exchange.py '<redirected_url_with_code>'", file=sys.stderr)
        sys.exit(2)
    redirected = sys.argv[1]
    client_id = os.getenv("APS_CLIENT_ID")
    client_secret = os.getenv("APS_CLIENT_SECRET")
    redirect_uri = os.getenv("APS_REDIRECT_URI", "http://localhost:8765/callback")
    scope = os.getenv("APS_SCOPES_3L", "data:read data:write code:all")
    token_out = os.getenv("APS_TOKEN_FILE", "out/token_3l.json")
    if not (client_id and client_secret):
        print("Set APS_CLIENT_ID and APS_CLIENT_SECRET", file=sys.stderr)
        sys.exit(2)
    parsed = urllib.parse.urlparse(redirected)
    qs = urllib.parse.parse_qs(parsed.query)
    code = qs.get("code", [None])[0]
    if not code:
        print("No 'code' found in URL", file=sys.stderr)
        sys.exit(2)
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
        print(f"Token exchange failed: {r.status_code} {r.text}", file=sys.stderr)
        sys.exit(1)
    os.makedirs("out", exist_ok=True)
    with open(token_out, "w", encoding="utf-8") as f:
        json.dump(r.json(), f, indent=2)
    print(f"Saved 3-legged token to {token_out}")


if __name__ == "__main__":
    main()




