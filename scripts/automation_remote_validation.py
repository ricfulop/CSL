#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

import requests


def bearer() -> str:
  cid = os.getenv("APS_CLIENT_ID")
  csec = os.getenv("APS_CLIENT_SECRET")
  scopes = os.getenv("APS_SCOPES", "data:read data:write code:all")
  if not (cid and csec):
    print("Set APS_CLIENT_ID/APS_CLIENT_SECRET", file=sys.stderr)
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


def submit(script_path: str) -> str:
  base = os.getenv("DA_BASE", "https://developer.api.autodesk.com/da/us-east/v3")
  activity = os.getenv("AUTOMATION_ACTIVITY_ID", "Fusion.ScriptJob+Latest")
  pat = os.getenv("FUSION_PAT")
  if not pat:
    print("Set FUSION_PAT", file=sys.stderr)
    sys.exit(2)
  src = Path(script_path)
  if not src.exists():
    print(f"Script not found: {script_path}", file=sys.stderr)
    sys.exit(2)
  args_payload = {"PersonalAccessToken": pat, "TaskScript": src.read_text()}
  tok = bearer()
  hdr = {"Authorization": f"Bearer {tok}", "Content-Type": "application/json"}
  r = requests.post(f"{base}/workitems", headers=hdr, json={"activityId": activity, "arguments": args_payload}, timeout=30)
  if r.status_code not in (200, 201, 202):
    print(f"Submit failed: {r.status_code} {r.text}", file=sys.stderr)
    sys.exit(1)
  wid = r.json().get("id")
  print(json.dumps(r.json(), indent=2))
  return wid


def poll(work_id: str, *, polls: int = 60, sleep_s: int = 5) -> dict:
  base = os.getenv("DA_BASE", "https://developer.api.autodesk.com/da/us-east/v3")
  tok = bearer()
  hdr = {"Authorization": f"Bearer {tok}"}
  status = {}
  for _ in range(polls):
    r = requests.get(f"{base}/workitems/{work_id}", headers=hdr, timeout=20)
    status = r.json()
    phase = (status.get("status") or "").lower()
    print(f"{work_id} status: {phase}")
    if phase in ("succeeded", "failed", "cancelled", "failedinstructions"):
      break
    time.sleep(sleep_s)
  # Fetch report if available
  url = status.get("reportUrl") if isinstance(status, dict) else None
  if url:
    rr = requests.get(url, timeout=30)
    if rr.status_code == 200:
      Path("out").mkdir(parents=True, exist_ok=True)
      Path("out/automation_remote_report.txt").write_text(rr.text)
  Path("out/automation_remote_status.json").write_text(json.dumps(status, indent=2))
  return status


def main() -> None:
  tests = [
    "scripts/fusion_auto_selection_quick.ts",
    "scripts/fusion_auto_wrap_project_test.ts",
  ]
  results = []
  for t in tests:
    wid = submit(t)
    st = poll(wid, polls=int(os.getenv("DA_STATUS_POLLS", "60")))
    results.append({"id": wid, "status": st.get("status")})
  print(json.dumps({"results": results}, indent=2))


if __name__ == "__main__":
  main()


