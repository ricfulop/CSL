#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path


def run(cmd: list[str]) -> int:
    print("$", " ".join(cmd))
    return subprocess.call(cmd)


def main() -> None:
    # Required inputs
    name = os.getenv("APS_BUNDLE_NAME") or "csl_fusion_bundle"
    activity = os.getenv("APS_ACTIVITY_NAME") or f"{name}_activity"
    engine = os.getenv("APS_ENGINE")  # e.g. Autodesk.Fusion+<ver>
    zip_path = os.getenv("APS_BUNDLE_ZIP")  # path to AppBundle zip
    if not (engine and zip_path and Path(zip_path).exists()):
        print("Set APS_ENGINE and APS_BUNDLE_ZIP to run the pipeline", file=sys.stderr)
        sys.exit(2)

    # Ensure appbundle and activity
    rc = run([sys.executable, "scripts/aps_da_stub.py", "ensure-appbundle", name, engine, zip_path])
    if rc != 0:
        sys.exit(rc)
    rc = run([sys.executable, "scripts/aps_da_stub.py", "ensure-activity", activity, engine, name])
    if rc != 0:
        sys.exit(rc)

    # Create a minimal workitem args file under out/
    out_dir = Path("out"); out_dir.mkdir(parents=True, exist_ok=True)
    args_path = out_dir / "workitem_args.json"
    args = {
        "arguments": {
            "input": {"url": os.getenv("APS_INPUT_URL", "https://example.com/input.json")},
            "output": {"url": os.getenv("APS_OUTPUT_URL", "https://example.com/output.json"), "verb": "put"}
        }
    }
    args_path.write_text(json.dumps(args, indent=2))

    # Submit workitem
    rc = run([sys.executable, "scripts/aps_da_stub.py", "submit-workitem", activity, str(args_path)])
    sys.exit(rc)


if __name__ == "__main__":
    main()


