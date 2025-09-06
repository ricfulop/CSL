#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import requests


def load_3l_token() -> str | None:
    p = Path("out/token_3l.json")
    if p.exists():
        try:
            return json.loads(p.read_text()).get("access_token")
        except Exception:
            return None
    return None


def get_bearer() -> str:
    tok = load_3l_token()
    if tok:
        return tok
    cid = os.getenv("APS_CLIENT_ID")
    csec = os.getenv("APS_CLIENT_SECRET")
    if not (cid and csec):
        print("Set APS_CLIENT_ID/APS_CLIENT_SECRET or provide out/token_3l.json", file=sys.stderr)
        sys.exit(2)
    scopes = os.getenv("APS_SCOPES", "data:read data:write code:all")
    r = requests.post(
        "https://developer.api.autodesk.com/authentication/v2/token",
        data={
            "grant_type": "client_credentials",
            "client_id": cid,
            "client_secret": csec,
            "scope": scopes,
        },
        timeout=20,
    )
    if r.status_code != 200:
        print(f"Auth failed: {r.status_code} {r.text}", file=sys.stderr)
        sys.exit(1)
    return r.json().get("access_token")


def main() -> None:
    base = os.getenv("DA_BASE", "https://developer.api.autodesk.com/da/us-east/v3")
    activity = os.getenv("DA_ACTIVITY_ID")
    fusion_pat = os.getenv("FUSION_PAT")
    task_params = os.getenv("TASK_PARAMS", '{"message":"hello"}')
    if not activity:
        print("Set DA_ACTIVITY_ID (e.g., MyActivity+v1)", file=sys.stderr)
        sys.exit(2)
    if not fusion_pat:
        print("Set FUSION_PAT (Fusion Personal Access Token)", file=sys.stderr)
        sys.exit(2)

    bearer = get_bearer()
    hdr = {"Authorization": f"Bearer {bearer}", "Content-Type": "application/json"}
    payload = {
        "activityId": activity,
        "arguments": {
            "PersonalAccessToken": fusion_pat,
            "TaskParameters": task_params,
        },
    }
    Path("out").mkdir(parents=True, exist_ok=True)
    r = requests.post(f"{base}/workitems", headers=hdr, json=payload, timeout=30)
    if r.status_code not in (200, 201, 202):
        print(f"Workitem submit failed: {r.status_code} {r.text}", file=sys.stderr)
        sys.exit(1)
    res = r.json()
    Path("out/da_workitem_submit.json").write_text(json.dumps(res, indent=2))
    print(json.dumps(res, indent=2))


if __name__ == "__main__":
    main()




