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


def build_ir(units: str, resolution: str, binary: bool, *, extra: Dict[str, Any] | None = None) -> Dict[str, Any]:
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
            {"id": "stl_out", "format": "STL", "path": f"out/plate_{units}_{resolution}_{int(binary)}.stl", "target": "part", "resolution": resolution, "binary": binary, "units": units, **(extra or {})},
            {"id": "step_out", "format": "STEP", "path": f"out/plate_{units}.step"}
        ],
    }


def main() -> None:
    Path("out").mkdir(parents=True, exist_ok=True)
    backend = FusionBackend()
    backend.open_session()

    combos = [
        ("mm", "high", True, {"deviation": "0.05 mm", "normal_deviation_deg": 1.0, "aspect_ratio": 5.0, "max_edge_length": "2 mm"}),
        ("mm", "low", False, {}),
        ("in", "medium", True, {"angular": 2.0}),
        ("cm", "high", False, {"max_edge": "3 mm"}),
    ]

    report = {"ok": True, "runs": []}
    for units, res, binary, extra in combos:
        ir = build_ir(units, res, binary, extra=extra)
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
