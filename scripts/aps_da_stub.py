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


def create_appbundle(token: str, name: str, engine: str, zip_path: str) -> None:
    # NOTE: This is a stub: validates inputs and prints the payload; attempts POST if file exists
    if not (name and engine and zip_path):
        print("Usage: aps_da_stub.py create-appbundle <name> <engineId> <zip_path>", file=sys.stderr)
        sys.exit(2)
    if not os.path.exists(zip_path):
        print(f"Zip not found: {zip_path}", file=sys.stderr)
        sys.exit(2)
    url = "https://developer.api.autodesk.com/da/us-east/v3/appbundles"
    hdr = {"Authorization": f"Bearer {token}"}
    files = {
        "file": (os.path.basename(zip_path), open(zip_path, "rb"), "application/zip"),
    }
    data = {"id": name, "engine": engine}
    print(json.dumps({"POST": url, "data": data}, indent=2))
    try:
        r = requests.post(url, headers=hdr, data={"data": json.dumps(data)}, files=files, timeout=60)
        print(f"create-appbundle: {r.status_code}")
        if r.status_code not in (200, 201):
            print(r.text)
    finally:
        try:
            files["file"][1].close()
        except Exception:
            pass


def create_activity(token: str, name: str, engine: str, appbundle_id: str) -> None:
    if not (name and engine and appbundle_id):
        print("Usage: aps_da_stub.py create-activity <name> <engineId> <appbundleId>", file=sys.stderr)
        sys.exit(2)
    url = "https://developer.api.autodesk.com/da/us-east/v3/activities"
    hdr = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    body = {
        "id": name,
        "engine": engine,
        "appbundles": [appbundle_id],
        "commandLine": ["$(engine.path) $(appbundles[0].path)"],
        "parameters": {"input": {"verb": "get"}, "output": {"verb": "put"}},
    }
    print(json.dumps({"POST": url, "body": body}, indent=2))
    r = requests.post(url, headers=hdr, json=body, timeout=30)
    print(f"create-activity: {r.status_code}")
    if r.status_code not in (200, 201):
        print(r.text)


def submit_workitem(token: str, activity_id: str, args_json_path: str) -> None:
    if not (activity_id and args_json_path):
        print("Usage: aps_da_stub.py submit-workitem <activityId> <args.json>", file=sys.stderr)
        sys.exit(2)
    if not os.path.exists(args_json_path):
        print(f"Args file not found: {args_json_path}", file=sys.stderr)
        sys.exit(2)
    url = "https://developer.api.autodesk.com/da/us-east/v3/workitems"
    hdr = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    body = json.loads(open(args_json_path, "r", encoding="utf-8").read())
    body["activityId"] = activity_id
    print(json.dumps({"POST": url, "body": body}, indent=2))
    r = requests.post(url, headers=hdr, json=body, timeout=30)
    print(f"submit-workitem: {r.status_code}")
    if r.status_code not in (200, 201, 202):
        print(r.text)
    else:
        print(r.json())


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: aps_da_stub.py [list-engines|create-appbundle|create-activity|submit-workitem|help]", file=sys.stderr)
        sys.exit(2)
    cmd = sys.argv[1]
    tok = aps_token()
    if not tok:
        print("APS credentials not set/invalid.", file=sys.stderr)
        sys.exit(1)
    if cmd == "list-engines":
        list_engines(tok)
    elif cmd == "create-appbundle":
        # name engine zip
        name = sys.argv[2] if len(sys.argv) > 2 else None
        engine = sys.argv[3] if len(sys.argv) > 3 else None
        z = sys.argv[4] if len(sys.argv) > 4 else None
        create_appbundle(tok, name, engine, z)
    elif cmd == "create-activity":
        name = sys.argv[2] if len(sys.argv) > 2 else None
        engine = sys.argv[3] if len(sys.argv) > 3 else None
        appb = sys.argv[4] if len(sys.argv) > 4 else None
        create_activity(tok, name, engine, appb)
    elif cmd == "submit-workitem":
        act = sys.argv[2] if len(sys.argv) > 2 else None
        args_path = sys.argv[3] if len(sys.argv) > 3 else None
        submit_workitem(tok, act, args_path)
    else:
        print_workitem_guidance()


if __name__ == "__main__":
    main()


