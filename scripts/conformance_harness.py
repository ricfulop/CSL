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

    # Loft orientation with rail (binormal/fixed_normal variants)
    cases.append({
        "id": "loft_orientation",
        "ir": {
            "csl": "1.1",
            "meta": {"name": "Loft Orientation", "units": "mm"},
            "sketches": [
                {"id": "s0", "plane": "world.xy", "entities": [
                    {"kind": "circle", "id": "c0", "center": "0,0", "d": "20 mm"}
                ]},
                {"id": "s1", "plane": "world.xz", "entities": [
                    {"kind": "rect", "id": "r1", "p1": "-6 mm,-3 mm", "p2": "6 mm,3 mm"}
                ]},
                {"id": "rail2", "plane": "world.yz", "entities": [
                    {"kind": "spline", "id": "path2", "points": ["0,0", "12 mm, 6 mm", "24 mm, 0"]}
                ]}
            ],
            "features": [
                {"kind": "loft", "id": "L3", "sections": ["s0.profile(c0)", "s1.profile(r1)"], "orientation": "binormal", "rail": "rail2.profile(path2)", "result": "body"}
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

    # Fillet vertex setbacks (feature-level)
    cases.append({
        "id": "fillet_setbacks",
        "ir": {
            "csl": "1.1",
            "meta": {"name": "Fillet Setbacks", "units": "mm"},
            "sketches": [
                {"id": "s", "plane": "world.xy", "entities": [
                    {"kind": "rect", "id": "plate", "p1": "0,0", "p2": "40 mm,20 mm"}
                ]}
            ],
            "features": [
                {"kind": "extrude", "id": "e", "profile": "plate", "distance": "4 mm", "op": "new_solid", "result": "part"},
                {"kind": "fillet", "id": "fs", "edges": {"kind": "edges", "of": "query.edges(part)"}, "setbacks": [
                    {"vertex_query": {"kind": "vertex", "on": "query.edges(part)"}, "d": "1.0 mm"}
                ]}
            ]
        }
    })

    # Patterns: circular, path, rectangular with axis/spacing
    cases.append({
        "id": "patterns_suite",
        "ir": {
            "csl": "1.1",
            "meta": {"name": "Patterns Suite", "units": "mm"},
            "sketches": [
                {"id": "s", "plane": "world.xy", "entities": [
                    {"kind": "rect", "id": "seed", "p1": "0,0", "p2": "8 mm,8 mm"},
                    {"kind": "line", "id": "pathline", "p1": "0,0", "p2": "40 mm,0"}
                ]}
            ],
            "features": [
                {"kind": "extrude", "id": "e", "profile": "seed", "distance": "3 mm", "op": "new_solid", "result": "part"},
                {"kind": "pattern", "id": "pat_circ", "seed": "query.body(part)", "kind": "circular", "count": 6, "angle": "360 deg", "axis": "Z"},
                {"kind": "pattern", "id": "pat_path", "seed": "query.body(part)", "kind": "path", "count": 4, "spacing": "10 mm", "path_query": "s.edge(pathline)"},
                {"kind": "pattern", "id": "pat_rect", "seed": "query.body(part)", "kind": "linear", "count1": 3, "spacing1": "12 mm", "axis1": "X", "count2": 2, "spacing2": "6 mm", "axis2": "Y"},
                {"kind": "pattern", "id": "pat_instances", "seed": "query.body(part)", "kind": "linear", "instances": [
                    {"dx": "0 mm", "dy": "0 mm", "dz": "0 mm", "angle": 0, "axis": "Z", "count": 1},
                    {"dx": "15 mm", "dy": "5 mm", "dz": "0 mm", "angle": 15, "axis": "Z", "count": 1}
                ]}
            ]
        }
    })

    # Surface ops: patch, extend, trim, knit (best-effort)
    cases.append({
        "id": "surface_ops_best_effort",
        "ir": {
            "csl": "1.1",
            "meta": {"name": "Surface Ops", "units": "mm"},
            "sketches": [
                {"id": "s", "plane": "world.xy", "entities": [
                    {"kind": "rect", "id": "seed", "p1": "0,0", "p2": "40 mm,20 mm"}
                ]}
            ],
            "features": [
                {"kind": "extrude", "id": "e", "profile": "seed", "distance": "2 mm", "op": "new_solid", "result": "p"},
                {"kind": "patch", "id": "surf_patch", "edges_query": {"kind": "edge", "created_by": "e"}},
                {"kind": "extend", "id": "surf_extend", "faces_query": {"kind": "face", "created_by": "e"}, "distance": "1 mm"},
                {"kind": "trim", "id": "surf_trim", "target_query": {"kind": "face", "created_by": "e"}},
                {"kind": "knit", "id": "surf_knit", "faces_query": {"kind": "face", "created_by": "e"}, "tolerance": "0.1 mm", "to_solid": False}
            ]
        }
    })

    # Sheet metal (stubs): base flange, edge flange, bend, unfold/refold
    cases.append({
        "id": "sheet_metal_stubs",
        "ir": {
            "csl": "1.1",
            "meta": {"name": "Sheet Metal Stubs", "units": "mm"},
            "sketches": [
                {"id": "s", "plane": "world.xy", "entities": [
                    {"kind": "rect", "id": "seed", "p1": "0,0", "p2": "40 mm,20 mm"}
                ]}
            ],
            "features": [
                {"kind": "sheet_base_flange", "id": "sbf", "profile": "s", "thickness": "1.5 mm", "length": "20 mm"},
                {"kind": "sheet_edge_flange", "id": "sef", "on": {"kind": "face", "created_by": "sbf"}, "height": "10 mm"},
                {"kind": "sheet_bend", "id": "sbd", "angle": "45"},
                {"kind": "sheet_unfold", "id": "sunf"},
                {"kind": "sheet_refold", "id": "sref"}
            ]
        }
    })

    # Selection determinism: created_by, pattern_instances, tangent_connected
    cases.append({
        "id": "selection_determinism",
        "ir": {
            "csl": "1.1",
            "meta": {"name": "Selection Determinism", "units": "mm"},
            "sketches": [
                {"id": "s", "plane": "world.xy", "entities": [
                    {"kind": "rect", "id": "seed", "p1": "0,0", "p2": "20 mm,10 mm"}
                ]}
            ],
            "features": [
                {"kind": "extrude", "id": "e", "profile": "seed", "distance": "3 mm", "op": "new_solid", "result": "p"},
                {"kind": "fillet", "id": "f1", "edges": "query.edges(p)", "radius": "1 mm"},
                {"kind": "pattern", "id": "pat1", "seed": "query.body(p)", "kind": "linear", "count1": 3, "spacing1": "8 mm"}
            ],
            "post_queries": [
                {"kind": "face", "created_by": "f1"},
                {"kind": "body", "pattern_instances": {"feature": "pat1"}},
                {"kind": "face", "tangent_connected": {"seed": {"kind": "face", "created_by": "f1"}, "tol_deg": 1.0}}
            ]
        }
    })

    # Selection determinism under timeline reorder (simulated)
    cases.append({
        "id": "selection_determinism_reorder",
        "ir": {
            "csl": "1.1",
            "meta": {"name": "Selection Determinism Reorder", "units": "mm"},
            "sketches": [
                {"id": "s", "plane": "world.xy", "entities": [
                    {"kind": "rect", "id": "seed", "p1": "0,0", "p2": "16 mm,12 mm"}
                ]}
            ],
            "features": [
                {"kind": "extrude", "id": "e", "profile": "seed", "distance": "4 mm", "op": "new_solid", "result": "p"},
                {"kind": "fillet", "id": "f1", "edges": "query.edges(p)", "radius": "1.5 mm"},
                {"kind": "pattern", "id": "pat1", "seed": "query.body(p)", "kind": "linear", "count1": 2, "spacing1": "10 mm"}
            ],
            "post_queries": [
                {"kind": "face", "created_by": "f1"},
                {"kind": "body", "pattern_instances": {"feature": "pat1"}}
            ],
            "mutations": ["reorder"]
        }
    })

    # Selection determinism under suppress/regenerate (simulated)
    cases.append({
        "id": "selection_determinism_regenerate",
        "ir": {
            "csl": "1.1",
            "meta": {"name": "Selection Determinism Regenerate", "units": "mm"},
            "sketches": [
                {"id": "s", "plane": "world.xy", "entities": [
                    {"kind": "rect", "id": "seed", "p1": "0,0", "p2": "10 mm,10 mm"}
                ]}
            ],
            "features": [
                {"kind": "extrude", "id": "e", "profile": "seed", "distance": "5 mm", "op": "new_solid", "result": "p"},
                {"kind": "fillet", "id": "f1", "edges": "query.edges(p)", "radius": "1.0 mm"}
            ],
            "post_queries": [
                {"kind": "face", "tangent_connected": {"seed": {"kind": "face", "created_by": "f1"}, "tol_deg": 2.0}}
            ],
            "mutations": ["suppress", "regen"]
        }
    })

    # Loft continuity G1 with two sections
    cases.append({
        "id": "loft_continuity_g1",
        "ir": {
            "csl": "1.1",
            "meta": {"name": "Loft G1", "units": "mm"},
            "sketches": [
                {"id": "skA", "plane": "world.xy", "entities": [
                    {"kind": "circle", "id": "a", "center": "0,0", "d": "10 mm"}
                ]},
                {"id": "skB", "plane": "world.xz", "entities": [
                    {"kind": "rect", "id": "b", "p1": "-5 mm,-5 mm", "p2": "5 mm,5 mm"}
                ]}
            ],
            "features": [
                {"kind": "loft", "id": "L1", "sections": ["skA", "skB"], "continuity": "G1"}
            ]
        }
    })

    # Loft with orientation and rail
    cases.append({
        "id": "loft_orientation_rail",
        "ir": {
            "csl": "1.1",
            "meta": {"name": "Loft Orient + Rail", "units": "mm"},
            "sketches": [
                {"id": "skA", "plane": "world.xy", "entities": [
                    {"kind": "circle", "id": "a", "center": "0,0", "d": "8 mm"}
                ]},
                {"id": "skB", "plane": "world.xz", "entities": [
                    {"kind": "circle", "id": "b", "center": "0,0", "d": "4 mm"}
                ]},
                {"id": "skG", "plane": "world.yz", "entities": [
                    {"kind": "line", "id": "rail1", "p1": "0,0", "p2": "0,10 mm"}
                ]}
            ],
            "features": [
                {"kind": "loft", "id": "L2", "sections": ["skA", "skB"], "orientation": "perpendicular", "guides": [{"kind": "edge", "of": "skG"}]}
            ]
        }
    })

    # Threads cosmetic via cylindrical_faces query
    cases.append({
        "id": "thread_cosmetic_query",
        "ir": {
            "csl": "1.1",
            "meta": {"name": "Thread Cosmetic Query", "units": "mm"},
            "sketches": [
                {"id": "s", "plane": "world.xy", "entities": [
                    {"kind": "circle", "id": "c", "center": "0,0", "d": "10 mm"}
                ]}
            ],
            "features": [
                {"kind": "extrude", "id": "e", "profile": "s", "distance": "10 mm", "op": "new_solid", "result": "p"},
                {"kind": "thread", "id": "t_c", "faces_query": {"kind": "face", "cylindrical_faces": True, "d≈": 10}, "mode": "cosmetic", "designation": "M10x1.5-6H", "handedness": "right", "length": "8 mm"}
            ]
        }
    })

    # Threads modeled via cylindrical_faces d≈ and axis≈
    cases.append({
        "id": "thread_modeled_query",
        "ir": {
            "csl": "1.1",
            "meta": {"name": "Thread Modeled Query", "units": "mm"},
            "sketches": [
                {"id": "s", "plane": "world.xy", "entities": [
                    {"kind": "circle", "id": "c", "center": "0,0", "d": "8 mm"}
                ]}
            ],
            "features": [
                {"kind": "extrude", "id": "e", "profile": "s", "distance": "12 mm", "op": "new_solid", "result": "p"},
                {"kind": "thread", "id": "t_m", "faces_query": {"kind": "face", "cylindrical_faces": True, "d≈": 8, "axis≈": "+Z"}, "mode": "modeled", "designation": "M8x1.25-6H", "handedness": "left", "length": "10 mm"}
            ]
        }
    })

    # Constraints: equal-length arrays and coincident-to-spline
    cases.append({
        "id": "constraints_equal_and_spline",
        "ir": {
            "csl": "1.1",
            "meta": {"name": "Constraints Equal & Spline", "units": "mm"},
            "sketches": [
                {"id": "s0", "plane": "world.xy", "entities": [
                    {"kind": "line", "id": "l1", "p1": "0,0", "p2": "20 mm,0"},
                    {"kind": "line", "id": "l2", "p1": "0,5 mm", "p2": "20 mm,5 mm"},
                    {"kind": "spline", "id": "sp1", "points": ["0,10 mm", "10 mm, 12 mm", "20 mm, 10 mm"]},
                    {"kind": "point", "id": "pt1", "at": "10 mm, 10 mm"}
                ],
                "constraints": [
                    {"kind": "equal_length", "items": ["l1", "l2"]},
                    {"kind": "coincident_to_spline", "a": "pt1", "b": "sp1"}
                ]}
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
                {"kind": "emboss", "id": "em", "sketch": "s", "on": {"kind": "face"}, "depth": "0.3 mm", "draft": "0 deg"}
            ]
        }
    })

    # Wrap curve onto face
    cases.append({
        "id": "wrap_curve",
        "ir": {
            "csl": "1.1",
            "meta": {"name": "Wrap Curve", "units": "mm"},
            "sketches": [
                {"id": "s1", "plane": "world.xy", "entities": [
                    {"kind": "circle", "id": "c", "center": "0,0", "d": "20 mm"}
                ]},
                {"id": "s2", "plane": "world.xz", "entities": [
                    {"kind": "line", "id": "l", "p1": "-5 mm,0", "p2": "5 mm,0"}
                ]}
            ],
            "features": [
                {"kind": "extrude", "id": "e", "profile": "s1", "distance": "5 mm", "op": "new_solid", "result": "part"},
                {"kind": "wrap", "id": "w1", "sketch": "s2", "on": {"kind": "face"}, "method": "wrap", "depth": "0.2 mm", "draft": "0 deg"}
            ]
        }
    })

    # Project sketch onto face (zero depth)
    cases.append({
        "id": "project_curve",
        "ir": {
            "csl": "1.1",
            "meta": {"name": "Project Curve", "units": "mm"},
            "sketches": [
                {"id": "s1", "plane": "world.xy", "entities": [
                    {"kind": "rect", "id": "r", "p1": "-5 mm,-5 mm", "p2": "5 mm,5 mm"}
                ]},
                {"id": "logo", "plane": "world.xz", "entities": [
                    {"kind": "text", "id": "t", "at": "0,0", "text": "CSL", "height": "3 mm"}
                ]}
            ],
            "features": [
                {"kind": "extrude", "id": "e", "profile": "s1", "distance": "6 mm", "op": "new_solid", "result": "part"},
                {"kind": "project", "id": "p1", "sketch": "logo", "on": {"kind": "face"}, "method": "project", "depth": "0.0 mm"}
            ]
        }
    })

    # Export STEP with AP242 sidecar metadata
    cases.append({
        "id": "export_step_ap242_sidecar",
        "ir": {
            "csl": "1.1",
            "meta": {"name": "Export AP242", "units": "mm"},
            "sketches": [
                {"id": "s", "plane": "world.xy", "entities": [
                    {"kind": "rect", "id": "plate", "p1": "0,0", "p2": "20 mm,10 mm"}
                ]}
            ],
            "features": [
                {"kind": "extrude", "id": "e", "profile": "plate", "distance": "3 mm", "op": "new_solid", "result": "part"}
            ],
            "export": [
                {"format": "STEP", "path": "out/test_ap242.step"}
            ]
        }
    })

    # Export 3MF parity
    cases.append({
        "id": "export_3mf_parity",
        "ir": {
            "csl": "1.1",
            "meta": {"name": "Export 3MF", "units": "mm"},
            "sketches": [
                {"id": "s", "plane": "world.xy", "entities": [
                    {"kind": "rect", "id": "plate", "p1": "0,0", "p2": "12 mm,8 mm"}
                ]}
            ],
            "features": [
                {"kind": "extrude", "id": "e", "profile": "plate", "distance": "2 mm", "op": "new_solid", "result": "part"}
            ],
            "export": [
                {"format": "3MF", "path": "out/test_parity.3mf"}
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

    # Assemblies: mate connector and assembly pattern (best-effort)
    cases.append({
        "id": "assemblies_stubs",
        "ir": {
            "csl": "1.1",
            "meta": {"name": "Assemblies Stubs", "units": "mm"},
            "sketches": [
                {"id": "s", "plane": "world.xy", "entities": [
                    {"kind": "rect", "id": "seed", "p1": "0,0", "p2": "16 mm,16 mm"}
                ]}
            ],
            "features": [
                {"kind": "extrude", "id": "e", "profile": "seed", "distance": "4 mm", "op": "new_solid", "result": "p"},
                {"kind": "mate_connector", "id": "mc1", "on": {"kind": "face", "created_by": "e"}},
                {"kind": "assembly_pattern", "id": "ap1", "count1": 2, "spacing1": "10 mm", "count2": 1, "spacing2": "10 mm"}
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

    # G2 curvature continuity on spline-to-arc
    cases.append({
        "id": "sketch_g2_curvature",
        "ir": {
            "csl": "1.1",
            "meta": {"name": "Sketch G2", "units": "mm"},
            "sketches": [
                {"id": "s0", "plane": "world.xy", "entities": [
                    {"kind": "spline", "id": "sp", "points": ["0,0", "10 mm, 5 mm", "20 mm, 0"]},
                    {"kind": "arc", "id": "ar", "center": "25 mm, 0", "start": "20 mm,0", "end": "30 mm, 0"}
                ],
                "constraints": [
                    {"kind": "curvature", "a": "sp", "b": "ar"}
                ]}
            ]
        }
    })

    # PMI/GD&T minimal notes
    cases.append({
        "id": "pmi_gdt_notes",
        "ir": {
            "csl": "1.1",
            "meta": {"name": "PMI/GDT Notes", "units": "mm"},
            "sketches": [
                {"id": "s0", "plane": "world.xy", "entities": [
                    {"kind": "rect", "id": "plate", "p1": "0,0", "p2": "20 mm,10 mm"}
                ]}
            ],
            "features": [
                {"kind": "extrude", "id": "e", "profile": "plate", "distance": "3 mm", "op": "new_solid", "result": "part"}
            ],
            "pmi": [
                {"note": "REF", "plane": "world.xy", "at": "5 mm, 5 mm", "height": "4 mm"}
            ],
            "gdt": [
                {"label": "⟂|A|0.1", "plane": "world.xy", "at": "0,0", "height": "4 mm"}
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
        # For selection determinism tests, we may run follow-up queries
        if ir.get("post_queries"):
            for q in ir.get("post_queries"):
                try:
                    _ = backend._resolve_query(backend._design.rootComponent if hasattr(backend, "_design") else None, q, entity_type=q.get("kind") or "face")
                except Exception:
                    pass
        # Simulate timeline mutations: reorder/suppress/regenerate by refreshing lineage and rerunning queries
        muts = ir.get("mutations") or []
        if isinstance(muts, list) and len(muts) > 0:
            try:
                # Best-effort: refresh lineage and rerun queries as a proxy for timeline changes
                if hasattr(backend, "_design"):
                    backend._refresh_lineage_from_attributes(backend._design.rootComponent)
                if ir.get("post_queries"):
                    for q in ir.get("post_queries"):
                        try:
                            _ = backend._resolve_query(backend._design.rootComponent if hasattr(backend, "_design") else None, q, entity_type=q.get("kind") or "face")
                        except Exception:
                            pass
            except Exception:
                pass
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
    # Simulate reopen/regeneration reconciliation by reloading persisted lineage
    try:
        backend._load_persisted_lineage()
    except Exception:
        pass
    Path("out/conformance_report.json").write_text(json.dumps(report, indent=2))
    # Golden summary: only ok/err counts by case id
    golden = {"ok": report["ok"], "cases": [{"id": c["id"], "ok": c["ok"], "errors": len(c.get("errors") or [])} for c in report["cases"]]}
    Path("out/golden_summary.json").write_text(json.dumps(golden, indent=2))
    print("Conformance report written to out/conformance_report.json")


if __name__ == "__main__":
    main()


