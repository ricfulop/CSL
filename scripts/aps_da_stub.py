#!/usr/bin/env python3
"""
APS Design Automation (DA) stub utilities

- Auth via APS env vars
- List available DA engines (region us-east)
- Sketch of creating an activity/workitem (printed guidance only)

Env required:
  APS_CLIENT_ID, APS_CLIENT_SECRET
Optional:
  APS_SCOPES (default: data:read data:write code:all bucket:create bucket:read bucket:update)
"""
from __future__ import annotations

import os
import sys
import json
from typing import Dict, Any

import requests


def aps_token() -> str | None:
    cid = os.getenv("APS_CLIENT_ID")
    csec = os.getenv("APS_CLIENT_SECRET")
    scopes = os.getenv("APS_SCOPES", "data:read data:write code:all bucket:create bucket:read bucket:update")
    if not cid or not csec:
        return None
    resp = requests.post(
        "https://developer.api.autodesk.com/authentication/v2/token",
        data={
            "grant_type": "client_credentials",
            "client_id": cid,
            "client_secret": csec,
            "scope": scopes,
        },
        timeout=20,
    )
    if resp.status_code != 200:
        print(f"APS auth failed: {resp.status_code} {resp.text}", file=sys.stderr)
        return None
    return resp.json().get("access_token")


def list_engines(token: str) -> None:
    url = "https://developer.api.autodesk.com/da/us-east/v3/engines"
    r = requests.get(url, headers={"Authorization": f"Bearer {token}"}, timeout=20)
    if r.status_code != 200:
        print(f"List engines failed: {r.status_code} {r.text}", file=sys.stderr)
        sys.exit(1)
    engines = r.json()
    # Print a short summary
    names = [e.get("id") for e in (engines if isinstance(engines, list) else [])]
    print(json.dumps({"count": len(names), "sample": names[:5]}, indent=2))


def print_workitem_guidance() -> None:
    print(
        """
To run Fusion geometry in DA, you'll need to:
1) Create an AppBundle (zip of add-in + manifest) and upload it
2) Create an Activity referencing your AppBundle and target engine
3) POST a WorkItem with input/output arguments

Endpoints:
- AppBundles: POST https://developer.api.autodesk.com/da/us-east/v3/appbundles
- Activities: POST https://developer.api.autodesk.com/da/us-east/v3/activities
- WorkItems: POST https://developer.api.autodesk.com/da/us-east/v3/workitems

This stub lists engines and validates auth. Full DA orchestration will be implemented separately.
        """.strip()
    )


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: aps_da_stub.py [list-engines|help]", file=sys.stderr)
        sys.exit(2)
    cmd = sys.argv[1]
    tok = aps_token()
    if not tok:
        print("APS credentials not set/invalid.", file=sys.stderr)
        sys.exit(1)
    if cmd == "list-engines":
        list_engines(tok)
    else:
        print_workitem_guidance()


if __name__ == "__main__":
    main()


