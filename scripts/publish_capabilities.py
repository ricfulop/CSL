#!/usr/bin/env python3
from __future__ import annotations

import json
import os
from datetime import datetime
from pathlib import Path

from triple_lindy.transpilers.fusion360_backend import FusionBackend


def main() -> None:
    be = FusionBackend()
    be.open_session()
    caps = be.get_capabilities()

    out_dir = Path("out")
    out_dir.mkdir(parents=True, exist_ok=True)

    # Write current snapshot
    current_path = out_dir / "capabilities_fusion.json"
    current_path.write_text(json.dumps(caps, indent=2))

    # Archive with versioned path
    version = str(caps.get("version") or os.getenv("CSL_VERSION") or "v0.x")
    ts = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    archive_dir = out_dir / "capabilities" / "archive" / version
    archive_dir.mkdir(parents=True, exist_ok=True)
    archive_file = archive_dir / f"capabilities_fusion_{version}_{ts}.json"
    archive_file.write_text(json.dumps(caps, indent=2))

    # Update latest pointer for this version
    (archive_dir / "latest.json").write_text(json.dumps(caps, indent=2))
    print(f"Published capabilities to {current_path} and {archive_file}")


if __name__ == "__main__":
    main()


