#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import requests


def load_3l_token() -> dict | None:
    p = Path("out/token_3l.json")
    if p.exists():
        try:
            return json.loads(p.read_text())
        except Exception:
            return None
    return None


def get_bearer() -> str:
    # Prefer 2-legged for Automation/DA by default; set DA_PREFER_2L=false to use 3L
    prefer_2l = os.getenv("DA_PREFER_2L", "true").lower() != "false"
    cid = os.getenv("APS_CLIENT_ID")
    csec = os.getenv("APS_CLIENT_SECRET")
    scopes = os.getenv("APS_SCOPES", "data:read data:write code:all")

    if prefer_2l:
        if not (cid and csec):
            print("Set APS_CLIENT_ID/APS_CLIENT_SECRET for 2-legged token", file=sys.stderr)
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

    token_obj = load_3l_token()
    if token_obj:
        access_token = token_obj.get("access_token")
        refresh_token = token_obj.get("refresh_token")
        if refresh_token and cid and csec:
            r = requests.post(
                "https://developer.api.autodesk.com/authentication/v2/token",
                data={
                    "grant_type": "refresh_token",
                    "refresh_token": refresh_token,
                    "client_id": cid,
                    "client_secret": csec,
                },
                timeout=20,
            )
            if r.status_code == 200:
                new_tokens = r.json()
                Path("out").mkdir(parents=True, exist_ok=True)
                Path("out/token_3l.json").write_text(json.dumps(new_tokens, indent=2))
                return new_tokens.get("access_token")
        if access_token:
            return access_token
    print("3-legged token not available; set DA_PREFER_2L=false only if you have out/token_3l.json", file=sys.stderr)
    sys.exit(2)


def main() -> None:
    # Automation API (v3) base endpoint – default to us-east
    base = os.getenv("DA_BASE", "https://developer.api.autodesk.com/da/us-east/v3")

    # Built-in Fusion activity to run inline TypeScript
    activity = os.getenv("AUTOMATION_ACTIVITY_ID", "Fusion.ScriptJob+Latest")

    fusion_pat = os.getenv("FUSION_PAT")
    if not fusion_pat:
        print("Set FUSION_PAT (Fusion Personal Access Token with Automation scope)", file=sys.stderr)
        sys.exit(2)

    task_script = os.getenv("FUSION_TASK_SCRIPT")
    script_file = os.getenv("FUSION_SCRIPT_FILE")
    if script_file:
        # When a script file is provided, read contents and pass via TaskScript
        src = Path(script_file)
        if not src.exists():
            print(f"Script file not found: {script_file}", file=sys.stderr)
            sys.exit(2)
        script_source = src.read_text()
        args_payload = {
            "PersonalAccessToken": fusion_pat,
            "TaskScript": script_source,
        }
    else:
        task_script = task_script or "adsk.log('Hello from Automation API');"
        args_payload = {
            "PersonalAccessToken": fusion_pat,
            "TaskScript": task_script,
        }

    bearer = get_bearer()
    hdr = {"Authorization": f"Bearer {bearer}", "Content-Type": "application/json"}

    payload = {"activityId": activity, "arguments": args_payload}

    Path("out").mkdir(parents=True, exist_ok=True)
    r = requests.post(f"{base}/workitems", headers=hdr, json=payload, timeout=30)
    if r.status_code not in (200, 201, 202):
        print(f"Workitem submit failed: {r.status_code} {r.text}", file=sys.stderr)
        sys.exit(1)
    res = r.json()
    Path("out/fusion_auto_submit.json").write_text(json.dumps(res, indent=2))
    print(json.dumps(res, indent=2))


if __name__ == "__main__":
    main()

