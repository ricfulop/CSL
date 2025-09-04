"""Export units parity test for FusionBackend (dry-run friendly).

This script builds a minimal IR and calls export with different unit/resolution
combinations to ensure code paths execute without error. In environments without
Fusion, the backend reports diagnostics and returns gracefully.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

from triple_lindy.transpilers.fusion360_backend import FusionBackend


def build_ir(units: str, resolution: str, binary: bool) -> Dict[str, Any]:
    return {
        "csl": "1.1",
        "meta": {"name": f"ExportUnitsTest-{units}-{resolution}-{int(binary)}", "units": units},
        "sketches": [
            {"id": "s", "plane": "world.xy", "entities": [
                {"kind": "rect", "id": "plate", "p1": "0,0", "p2": "20 mm, 10 mm"}
            ]}
        ],
        "features": [
            {"kind": "extrude", "id": "e", "profile": "plate", "distance": "2 mm", "op": "new_solid", "result": "part"}
        ],
        "export": [
            {"id": "stl_out", "format": "STL", "path": f"out/plate_{units}_{resolution}_{int(binary)}.stl", "target": "part", "resolution": resolution, "binary": binary, "units": units},
            {"id": "step_out", "format": "STEP", "path": f"out/plate_{units}.step"}
        ],
    }


def main() -> None:
    Path("out").mkdir(parents=True, exist_ok=True)
    backend = FusionBackend()
    backend.open_session()

    combos = [
        ("mm", "high", True),
        ("mm", "low", False),
        ("in", "medium", True),
        ("cm", "high", False),
    ]

    report = {"ok": True, "runs": []}
    for units, res, binary in combos:
        ir = build_ir(units, res, binary)
        try:
            backend.realize(ir)
            backend.export(ir.get("export", []))
            report["runs"].append({"units": units, "resolution": res, "binary": binary, "ok": True})
        except Exception as ex:  # pragma: no cover
            report["ok"] = False
            report["runs"].append({"units": units, "resolution": res, "binary": binary, "ok": False, "err": str(ex)})

    Path("out/export_units_report.json").write_text(json.dumps(report, indent=2))
    print("Export units test complete. See out/export_units_report.json")


if __name__ == "__main__":
    main()
