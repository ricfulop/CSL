#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

import requests


def main() -> None:
    base = os.getenv("DA_BASE", "https://developer.api.autodesk.com/da/us-east/v3")
    work_id = os.getenv("DA_WORKITEM_ID")
    if not work_id:
        p = Path("out/fusion_auto_submit.json")
        if p.exists():
            try:
                work_id = json.loads(p.read_text()).get("id")
            except Exception:
                work_id = None
    if not work_id:
        print("Set DA_WORKITEM_ID or ensure out/fusion_auto_submit.json is present", file=sys.stderr)
        sys.exit(2)

    # Reuse bearer helper logic: prefer refresh of 3L token if present
    cid = os.getenv("APS_CLIENT_ID")
    csec = os.getenv("APS_CLIENT_SECRET")
    scopes = os.getenv("APS_SCOPES", "data:read data:write code:all")
    prefer_2l = os.getenv("DA_PREFER_2L", "true").lower() != "false"

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
        tok = r.json().get("access_token")
    else:
        tok = None
        p3l = Path("out/token_3l.json")
        if p3l.exists():
            try:
                token_obj = json.loads(p3l.read_text())
                access_token = token_obj.get("access_token")
                refresh_token = token_obj.get("refresh_token")
                if refresh_token and cid and csec:
                    rr = requests.post(
                        "https://developer.api.autodesk.com/authentication/v2/token",
                        data={
                            "grant_type": "refresh_token",
                            "refresh_token": refresh_token,
                            "client_id": cid,
                            "client_secret": csec,
                        },
                        timeout=20,
                    )
                    if rr.status_code == 200:
                        new_tokens = rr.json()
                        Path("out").mkdir(parents=True, exist_ok=True)
                        Path("out/token_3l.json").write_text(json.dumps(new_tokens, indent=2))
                        tok = new_tokens.get("access_token")
                if not tok and access_token:
                    tok = access_token
            except Exception:
                tok = None
        if not tok:
            print("3-legged token not available; set DA_PREFER_2L=false only if you have out/token_3l.json", file=sys.stderr)
            sys.exit(2)
    hdr = {"Authorization": f"Bearer {tok}"}

    out_dir = Path("out"); out_dir.mkdir(parents=True, exist_ok=True)
    for _ in range(int(os.getenv("DA_STATUS_POLLS", "10"))):
        r = requests.get(f"{base}/workitems/{work_id}", headers=hdr, timeout=20)
        if r.status_code != 200:
            print(f"Status failed: {r.status_code} {r.text}", file=sys.stderr)
            sys.exit(1)
        st = r.json()
        Path("out/fusion_auto_status.json").write_text(json.dumps(st, indent=2))
        phase = (st.get("status") or "").lower()
        print(f"Workitem {work_id} status: {phase}")
        if phase in ("succeeded", "failed", "cancelled"):
            break
        time.sleep(5)

    # Optionally fetch and save the execution report/logs
    if os.getenv("DA_FETCH_REPORT", "1").lower() not in ("0", "false"):
        url = st.get("reportUrl") if isinstance(st, dict) else None
        if url:
            try:
                rr = requests.get(url, timeout=30)
                if rr.status_code == 200:
                    report_path = Path("out/fusion_auto_report.txt")
                    report_path.write_text(rr.text)
                    print(f"Saved report to {report_path}")
                    try:
                        tail_n = int(os.getenv("DA_REPORT_TAIL", "50"))
                    except Exception:
                        tail_n = 50
                    lines = rr.text.splitlines()
                    tail = "\n".join(lines[-tail_n:])
                    if tail:
                        print(tail)
                else:
                    print(f"Failed to fetch report: {rr.status_code}")
            except Exception as ex:
                print(f"Error fetching report: {ex}", file=sys.stderr)


if __name__ == "__main__":
    main()


