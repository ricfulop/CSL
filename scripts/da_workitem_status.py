#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import requests


def bearer_from_files_or_env() -> str:
    p = Path("out/token_3l.json")
    if p.exists():
        try:
            return json.loads(p.read_text()).get("access_token")
        except Exception:
            pass
    cid = os.getenv("APS_CLIENT_ID")
    csec = os.getenv("APS_CLIENT_SECRET")
    scopes = os.getenv("APS_SCOPES", "data:read data:write code:all")
    if not (cid and csec):
        print("Set APS_CLIENT_ID/APS_CLIENT_SECRET or provide out/token_3l.json", file=sys.stderr)
        sys.exit(2)
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
    work_id = os.getenv("DA_WORKITEM_ID")
    if not work_id:
        p = Path("out/da_workitem_submit.json")
        if p.exists():
            try:
                work_id = json.loads(p.read_text()).get("id")
            except Exception:
                work_id = None
    if not work_id:
        print("Set DA_WORKITEM_ID or ensure out/da_workitem_submit.json is present", file=sys.stderr)
        sys.exit(2)
    tok = bearer_from_files_or_env()
    hdr = {"Authorization": f"Bearer {tok}"}
    r = requests.get(f"{base}/workitems/{work_id}", headers=hdr, timeout=20)
    if r.status_code != 200:
        print(f"Status failed: {r.status_code} {r.text}", file=sys.stderr)
        sys.exit(1)
    res = r.json()
    Path("out/da_workitem_status.json").write_text(json.dumps(res, indent=2))
    print(json.dumps(res, indent=2))


if __name__ == "__main__":
    main()




