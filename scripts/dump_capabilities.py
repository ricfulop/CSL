#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from triple_lindy.transpilers.fusion360_backend import FusionBackend


def main() -> None:
    be = FusionBackend()
    be.open_session()
    caps = be.get_capabilities()
    Path("out").mkdir(parents=True, exist_ok=True)
    Path("out/capabilities_fusion.json").write_text(json.dumps(caps, indent=2))
    print("Wrote out/capabilities_fusion.json")


if __name__ == "__main__":
    main()


