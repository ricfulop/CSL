#!/usr/bin/env python3
from __future__ import annotations

import json
import random
from pathlib import Path

from triple_lindy.transpilers.fusion360_backend import FusionBackend


def main() -> None:
    be = FusionBackend()
    be.open_session()

    # Minimal IR seed
    ir = {
        "csl": "1.1",
        "meta": {"name": "Fuzz", "units": "mm"},
        "sketches": [{"id": "s", "plane": "world.xy", "entities": [{"kind": "rect", "id": "r", "p1": "0,0", "p2": "20 mm,10 mm"}]}],
        "features": [{"kind": "extrude", "id": "e", "profile": "r", "distance": "3 mm", "op": "new_solid", "result": "p"}],
    }

    be.realize(ir)
    root = getattr(be, "_design", None)
    diagnostics = []
    preds = [
        {"kind": "face", "created_by": "e"},
        {"kind": "face", "tangent_connected": {"seed": {"kind": "face", "created_by": "e"}, "tol_deg": 1.0}},
        {"kind": "body", "pattern_instances": {"feature": "none"}},
        {"kind": "face", "largest_by": "area"},
    ]
    random.shuffle(preds)
    for q in preds:
        try:
            be._resolve_query(getattr(be, "_design", None).rootComponent if hasattr(be, "_design") else None, q, entity_type=q.get("kind") or "face")
        except Exception as ex:
            diagnostics.append({"query": q, "error": str(ex)})

    Path("out").mkdir(parents=True, exist_ok=True)
    Path("out/query_fuzz_summary.json").write_text(json.dumps({"errors": diagnostics}, indent=2))
    print("Query fuzz summary written to out/query_fuzz_summary.json")


if __name__ == "__main__":
    main()


