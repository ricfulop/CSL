"""Simple APS OAuth client_credentials test using repo secrets.

Requires environment variables APS_CLIENT_ID, APS_CLIENT_SECRET, APS_SCOPES.
"""
from __future__ import annotations

import os
import sys
import json
import requests


def main() -> None:
    client_id = os.getenv("APS_CLIENT_ID")
    client_secret = os.getenv("APS_CLIENT_SECRET")
    scopes = os.getenv("APS_SCOPES", "data:read")
    if not client_id or not client_secret:
        print("APS credentials not set; skipping.")
        return

    url = "https://developer.api.autodesk.com/authentication/v2/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": scopes,
    }
    resp = requests.post(url, data=data, timeout=20)
    if resp.status_code != 200:
        print(f"APS auth failed: {resp.status_code} {resp.text}")
        sys.exit(1)
    token = resp.json()
    print(json.dumps({"token_type": token.get("token_type"), "expires_in": token.get("expires_in")}, indent=2))


if __name__ == "__main__":
    main()


