"""Conformance harness for FusionBackend (dry-run friendly).

Runs a small battery of representative cases:
- Loft continuity G1 and G2 with guide rail
- Variable fillet/chamfer (best-effort, including angle variant)
- Wrap/Emboss (native where available, placeholder otherwise)
- Joints with revolute and slider limits

Outputs a JSON report to out/conformance_report.json and a short golden summary
file out/golden_summary.json for CI gates.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List

from triple_lindy.transpilers.fusion360_backend import FusionBackend


def build_cases() -> List[Dict[str, Any]]:
    cases: List[Dict[str, Any]] = []

    # Loft G1
    cases.append({
        "id": "loft_g1",
        "ir": {
            "csl": "1.1",
            "meta": {"name": "Loft G1", "units": "mm"},
            "sketches": [
                {"id": "s0", "plane": "world.xy", "entities": [
                    {"kind": "circle", "id": "c0", "center": "0,0", "d": "30 mm"}
                ]},
                {"id": "s1", "plane": "world.xz", "entities": [
                    {"kind": "rect", "id": "r1", "p1": "-10 mm,-5 mm", "p2": "10 mm,5 mm"}
                ]}
            ],
            "features": [
                {"kind": "loft", "id": "L", "sections": ["s0.profile(c0)", "s1.profile(r1)"], "continuity": "G1", "result": "body"}
            ]
        }
    })

    # Loft G2 with rail (best-effort if API limited)
    cases.append({
        "id": "loft_g2_with_rail",
        "ir": {
            "csl": "1.1",
            "meta": {"name": "Loft G2 Rail", "units": "mm"},
            "sketches": [
                {"id": "s0", "plane": "world.xy", "entities": [
                    {"kind": "circle", "id": "c0", "center": "0,0", "d": "24 mm"}
                ]},
                {"id": "s1", "plane": "world.xz", "entities": [
                    {"kind": "rect", "id": "r1", "p1": "-8 mm,-4 mm", "p2": "8 mm,4 mm"}
                ]},
                {"id": "rail", "plane": "world.yz", "entities": [
                    {"kind": "spline", "id": "path", "points": ["0,0", "10 mm, 5 mm", "20 mm, 0"]}
                ]}
            ],
            "features": [
                {"kind": "loft", "id": "L2", "sections": ["s0.profile(c0)", "s1.profile(r1)"], "continuity": "G2", "rail": "rail.profile(path)", "result": "body"}
            ]
        }
    })

    # Variable fillet (points) and chamfer (points/angle) - best-effort
    cases.append({
        "id": "variable_fillet_chamfer",
        "ir": {
            "csl": "1.1",
            "meta": {"name": "Variable FC", "units": "mm"},
            "sketches": [
                {"id": "s", "plane": "world.xy", "entities": [
                    {"kind": "rect", "id": "plate", "p1": "0,0", "p2": "80 mm,60 mm"}
                ]}
            ],
            "features": [
                {"kind": "extrude", "id": "e", "profile": "plate", "distance": "6 mm", "op": "new_solid", "result": "part"},
                {"kind": "fillet", "id": "vf", "edges": "query.edges(part)", "groups": [
                    {"points": [{"t": 0.0, "r": "1 mm"}, {"t": 1.0, "r": "3 mm"}]}
                ]},
                {"kind": "chamfer", "id": "vc", "edges": "query.edges(part)", "points": [
                    {"t": 0.0, "d": "0.5 mm"}, {"t": 1.0, "d": "1.5 mm"}
                ]},
                {"kind": "chamfer", "id": "vca", "edges": "query.edges(part)", "angle": "45 deg", "distance": "1.0 mm"}
            ]
        }
    })

    # Wrap/Emboss placeholder (will emit diagnostics or best-effort)
    cases.append({
        "id": "emboss_text",
        "ir": {
            "csl": "1.1",
            "meta": {"name": "Emboss", "units": "mm"},
            "sketches": [
                {"id": "s", "plane": "world.xy", "entities": [
                    {"kind": "rect", "id": "plate", "p1": "0,0", "p2": "40 mm,20 mm"}
                ]}
            ],
            "features": [
                {"kind": "extrude", "id": "e", "profile": "plate", "distance": "3 mm", "op": "new_solid", "result": "part"},
                {"kind": "emboss", "id": "em", "source_sketch": "s", "onto": "query.face(part)", "depth": "0.3 mm", "text": "CSL"}
            ]
        }
    })

    # Joints with limits (revolute and slider)
    cases.append({
        "id": "joints_limits",
        "ir": {
            "csl": "1.1",
            "meta": {"name": "Joints", "units": "mm"},
            "sketches": [
                {"id": "s1", "plane": "world.xy", "entities": [
                    {"kind": "rect", "id": "b1", "p1": "0,0", "p2": "20 mm,10 mm"}
                ]},
                {"id": "s2", "plane": "world.xy", "entities": [
                    {"kind": "rect", "id": "b2", "p1": "30 mm,0", "p2": "50 mm,10 mm"}
                ]}
            ],
            "features": [
                {"kind": "extrude", "id": "e1", "profile": "b1", "distance": "5 mm", "op": "new_solid", "result": "p1"},
                {"kind": "extrude", "id": "e2", "profile": "b2", "distance": "5 mm", "op": "new_solid", "result": "p2"},
                {"kind": "joint", "id": "j1", "type": "revolute", "a": "query.body(p1)", "b": "query.body(p2)", "axis": "Z",
                 "limits": {"angular_min": "-45 deg", "angular_max": "45 deg"}},
                {"kind": "joint", "id": "j2", "type": "slider", "a": "query.body(p1)", "b": "query.body(p2)", "axis": "X",
                 "limits": {"linear_min": "0 mm", "linear_max": "10 mm"}}
            ]
        }
    })

    # Sketch construction geometry: ensure construction flags do not error
    cases.append({
        "id": "sketch_construction",
        "ir": {
            "csl": "1.1",
            "meta": {"name": "Sketch Construction", "units": "mm"},
            "sketches": [
                {"id": "s0", "plane": "world.xy", "entities": [
                    {"kind": "line", "id": "l1", "p1": "0,0", "p2": "20 mm,0", "construction": True},
                    {"kind": "circle", "id": "c1", "center": "10 mm,10 mm", "d": "8 mm", "is_construction": True}
                ]}
            ]
        }
    })

    # Reference (driven) dimensions across kinds
    cases.append({
        "id": "reference_dimensions",
        "ir": {
            "csl": "1.1",
            "meta": {"name": "Reference Dims", "units": "mm"},
            "sketches": [
                {"id": "s0", "plane": "world.xy", "entities": [
                    {"kind": "point", "id": "pA", "at": "0,0"},
                    {"kind": "point", "id": "pB", "at": "30 mm,0"},
                    {"kind": "circle", "id": "c1", "center": "15 mm,10 mm", "d": "12 mm"}
                ],
                "constraints": [
                    {"kind": "distance", "a": "pA", "b": "pB", "value": "30 mm", "reference": True},
                    {"kind": "angle", "a": "pA", "b": "pB", "value": "0 deg", "driven": True}
                ],
                "dimensions": [
                    {"kind": "diameter", "on": "c1", "value": "12 mm", "reference": True}
                ]}
            ]
        }
    })

    return cases


def run_case(backend: FusionBackend, case: Dict[str, Any]) -> Dict[str, Any]:
    result: Dict[str, Any] = {"id": case["id"], "ok": True, "mapping_size": 0, "errors": []}
    ir = case["ir"]
    try:
        mapping = backend.realize(ir)
        result["mapping_size"] = len(mapping)
        diags = backend.get_diagnostics()
        if diags.get("errors"):
            result["errors"] = diags["errors"][-10:]
        # Optionally export/thumbnail per case if declared in IR
        if ir.get("export"):
            backend.export(ir.get("export", []))
        if ir.get("thumbnail"):
            backend.thumbnail(ir.get("thumbnail", []))
    except Exception as ex:  # pragma: no cover
        result["ok"] = False
        result["errors"].append({"error": str(ex)})
    return result


def main() -> None:
    backend = FusionBackend()
    backend.open_session()
    Path("out").mkdir(parents=True, exist_ok=True)
    report: Dict[str, Any] = {"ok": True, "cases": []}
    for case in build_cases():
        res = run_case(backend, case)
        if not res.get("ok"):
            report["ok"] = False
        report["cases"].append(res)
    Path("out/conformance_report.json").write_text(json.dumps(report, indent=2))
    # Golden summary: only ok/err counts by case id
    golden = {"ok": report["ok"], "cases": [{"id": c["id"], "ok": c["ok"], "errors": len(c.get("errors") or [])} for c in report["cases"]]}
    Path("out/golden_summary.json").write_text(json.dumps(golden, indent=2))
    print("Conformance report written to out/conformance_report.json")


if __name__ == "__main__":
    main()


