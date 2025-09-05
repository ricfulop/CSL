#!/usr/bin/env python3
from __future__ import annotations

import json
import time
from pathlib import Path

from triple_lindy.transpilers.fusion360_backend import FusionBackend


def main() -> None:
    be = FusionBackend()
    t0 = time.time()
    be.open_session()
    t1 = time.time()
    # Simple perf timing of realize on a small IR
    ir = {
        "csl": "1.1",
        "meta": {"name": "Perf", "units": "mm"},
        "sketches": [{"id": "s", "plane": "world.xy", "entities": [{"kind": "rect", "id": "r", "p1": "0,0", "p2": "20 mm,10 mm"}]}],
        "features": [{"kind": "extrude", "id": "e", "profile": "r", "distance": "3 mm", "op": "new_solid", "result": "p"}],
    }
    t2 = time.time()
    be.realize(ir)
    t3 = time.time()
    Path("out").mkdir(parents=True, exist_ok=True)
    Path("out/perf_summary.json").write_text(json.dumps({
        "open_session_ms": int((t1 - t0) * 1000),
        "build_ir_ms": int((t2 - t1) * 1000),
        "realize_ms": int((t3 - t2) * 1000)
    }, indent=2))
    print("Perf summary written to out/perf_summary.json")


if __name__ == "__main__":
    main()


