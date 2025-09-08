"""Fusion 360 Backend Adapter (stub)

Implements the minimal BackendAdapter shape for Fusion-first development.
If Fusion's `adsk` modules are unavailable, methods will no-op or print guidance.
"""
from __future__ import annotations

import os
import re
from typing import Dict, List, Any, Optional, Tuple
import time


class FusionBackend:
    """Minimal Fusion backend adapter stub."""

    def __init__(self, session_config: Dict[str, Any] | None = None) -> None:
        self.session_config = session_config or {}
        self._fusion_available = self._check_fusion()
        # Lineage map for basic stable selection: featureId -> { bodies|faces|edges : [entityTokens] }
        self._lineage: Dict[str, Dict[str, List[str]]] = {}
        # Diagnostics store
        self._errors: List[Dict[str, Any]] = []
        # Persisted lineage cache (cross-session)
        self._persisted_lineage: Dict[str, Dict[str, List[str]]] = {}

    def _check_fusion(self) -> bool:
        try:
            import adsk.core  # type: ignore
            import adsk.fusion  # type: ignore
            _ = adsk.core  # silence lints
            _ = adsk.fusion
            return True
        except Exception:
            return False

    def get_capabilities(self) -> Dict[str, Any]:
        # Include version and environment metadata for determinism/debugging
        ver = os.getenv("CSL_VERSION") or "v0.3.0"
        git = os.getenv("GIT_COMMIT") or os.getenv("CI_COMMIT_SHA") or "unknown"
        fusion_build = os.getenv("FUSION_BUILD") or ("available" if self._fusion_available else "dry-run")
        return {
            "csl": "1.1",
            "backend": "fusion",
            "version": ver,
            "commit": git,
            "fusion_build": fusion_build,
            "supports": {
                "brep": True,
                "mesh": True,
                "params": True,
                "queries": True,
                "features": {
                    "extrude": True,
                    "fillet": {"variable": True, "setbacks": True},
                    "hole": True,
                    "loft": {"continuity": ["G1", "G2"], "orientation": ["perpendicular", "fixed_normal", "binormal"], "rails": True},
                    "shell": True,
                    "draft": True,
                    "pattern": {"linear": {"axis1": True, "axis2": True}, "circular": {"axis": True, "angle": True, "axis_query": True}, "path": {"spacing": True}, "table": True},
                    "boolean": ["union", "subtract", "intersect"],
                    "thread_cosmetic": True,
                    "thread_modeled": True,
                    "surface_ops": {"patch": True, "extend": True, "trim": True, "knit": True},
                    "assemblies": {"mate_connectors": True, "patterns": True},
                    "sheet_metal": {"base_flange": True, "edge_flange": True, "bend": True, "unfold": True, "refold": True},
                },
                "export": {"formats": ["STEP", "STL", "IGES", "3MF", "OBJ"], "stl": {"units": ["mm", "cm", "in"], "resolution": ["low", "medium", "high"], "tessellation": {"deviation": True, "angular": True, "aspect_ratio": True, "max_edge": True}}},
                "thumbnail": {"enabled": True, "views": ["iso", "top", "front", "right"], "styles": ["shaded", "wireframe"]},
            },
            "queries": {
                "predicates_supported": [
                    "created_by",
                    "owner_feature==",
                    "pattern_instances",
                    "tangent_connected",
                    "largest_by",
                    "largest",
                    "curvature≈",
                    "radius≈",
                    "area≈",
                    "by_material",
                    "by_tag",
                    "by_id",
                    "faces_parallel",
                    "normal==",
                    "cylindrical_faces",
                    "loop_edges",
                    "of",
                    "owner_body"
                ],
                "stable_id": "entityToken (session-scoped)",
                "lineage": "feature->(bodies,faces,edges) tokens",
                "determinism": {"ordering": "sorted_tokens", "persisted_normalization": True},
                "persistence": {"attributes": True, "persisted_file": True}
            },
            "diagnostics": {
                "codes": {"E12xx": "input/validation", "E23xx": "feature/selection", "E3xxx": "environment/runtime"},
                "recent": self._errors[-10:],
            },
            "aps": {
                "enabled": bool(self.session_config.get("aps_client_id")),
                "bucket": self.session_config.get("aps_bucket"),
                "scopes": self.session_config.get("aps_scopes") or "data:read data:write",
            },
        }

    def open_session(self, session_config: Dict[str, Any] | None = None) -> None:
        if session_config:
            self.session_config.update(session_config)
        # Load APS env if provided (for future cloud ops)
        self.session_config.setdefault("aps_client_id", os.getenv("APS_CLIENT_ID"))
        self.session_config.setdefault("aps_client_secret", os.getenv("APS_CLIENT_SECRET"))
        self.session_config.setdefault("aps_scopes", os.getenv("APS_SCOPES") or "data:read data:write")
        # Optional APS bucket default
        if not self.session_config.get("aps_bucket"):
            env_suffix = (os.getenv("CSL_ENV") or "local").lower()
            self.session_config["aps_bucket"] = f"csl-artifacts-{env_suffix}"
        # Default lineage path
        self.session_config.setdefault("lineage_path", os.path.abspath(self.session_config.get("lineage_path") or "csl_lineage.json"))
        # Load persisted lineage
        try:
            self._load_persisted_lineage()
        except Exception:
            pass
        # Opportunistically refresh lineage from attributes when available
        try:
            if self._fusion_available:
                app, ui, design = self._ensure_design()
                root = design.rootComponent
                self._refresh_lineage_from_attributes(root)
        except Exception:
            pass
        if not self._fusion_available:
            print("[FusionBackend] Fusion API not available in this environment; running in dry-run mode.")
            try:
                self._diag("E3000", where="env", message="Fusion API unavailable; dry-run mode.")
            except Exception:
                pass

    def close_session(self) -> None:
        return

    def realize(self, csl_ir: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a minimal subset: create extrude from first sketch profile, add holes/fillets if present.

        Stub: when Fusion is not available, return a plausible mapping.
        """
        import time
        load_time = time.strftime("%H:%M:%S")
        print(f"[FusionBackend.realize] VERSION: v10-debug-{load_time}")
        print(f"[FusionBackend.realize] Starting with IR: {list(csl_ir.keys())}")
        print(f"[FusionBackend.realize] Fusion available: {self._fusion_available}")
        mapping: Dict[str, str] = {"_version": f"v16-debug-{load_time}"}
        if not self._fusion_available:
            # Return a minimal stable mapping for CI/doc examples.
            for feat in csl_ir.get("features", []):
                if isinstance(feat, dict) and "id" in feat:
                    mapping[feat["id"]] = f"fusion:{feat['id']}"
            try:
                self._diag("E3000", where="realize", message="Fusion API unavailable; returned dry-run mapping.")
            except Exception:
                pass
            return mapping

        try:
            import adsk.core  # type: ignore
            import adsk.fusion  # type: ignore

            app, ui, design = self._ensure_design()
            root: adsk.fusion.Component = design.rootComponent

            # Create sketches (limited support: rect, circle)
            sketch_map: Dict[str, Any] = {}
            entity_to_sketch: Dict[str, Any] = {}  # Map entity IDs to their parent sketch
            
            sketches_list = csl_ir.get("sketches", []) or []
            print(f"[FusionBackend.realize] Processing {len(sketches_list)} sketches")
            mapping["debug_sketches_count"] = len(sketches_list)
            
            for sk in sketches_list:
                if not isinstance(sk, dict):
                    continue
                sk_id = sk.get("id", "sketch")
                mapping[f"debug_sketch_{sk_id}"] = f"entities={len(sk.get('entities', []))}"
                plane_name = (sk.get("plane") or "world.xy").lower()
                # Resolve construction plane and add sketch
                try:
                    plane_obj = self._plane_from_name(root, plane_name)
                except Exception:
                    plane_obj = root.xYConstructionPlane
                sketch = root.sketches.add(plane_obj)
                try:
                    if hasattr(sketch, "name"):
                        sketch.name = str(sk_id)
                except Exception:
                    pass
                ent_objects: Dict[str, Any] = {}
                # Entities
                for ent in sk.get("entities", []) or []:
                    kind = (ent.get("type") or ent.get("kind") or "").lower()
                    print(f"[DEBUG] Processing entity type: '{kind}', entity: {ent}")
                    mapping[f"debug_entity_{ent.get('id', 'unknown')}"] = f"type={kind}"
                    if kind == "rect" or kind == "rectangle":
                        mapping[f"debug_rect_{ent.get('id', 'unknown')}_start"] = "processing"
                        # Handle both formats: p1/p2 or center/w/h
                        p1 = self._parse_point(ent.get("p1"))
                        p2 = self._parse_point(ent.get("p2"))
                        print(f"[DEBUG] Rectangle p1={p1}, p2={p2}")
                        mapping[f"debug_rect_{ent.get('id', 'unknown')}_p1"] = str(p1)
                        mapping[f"debug_rect_{ent.get('id', 'unknown')}_p2"] = str(p2)
                        
                        # If p1/p2 not provided, try center/width/height format
                        if not (p1 and p2):
                            center = self._parse_point(ent.get("center"))
                            # Try both "w"/"h" and "width"/"height"
                            w_mm = self._parse_length_mm(ent.get("w") or ent.get("width"))
                            h_mm = self._parse_length_mm(ent.get("h") or ent.get("height"))
                            if center and w_mm and h_mm:
                                # Convert center/w/h to p1/p2 (keeping in mm for now)
                                p1 = (center[0] - w_mm/2, center[1] - h_mm/2, 0)
                                p2 = (center[0] + w_mm/2, center[1] + h_mm/2, 0)
                        
                        if p1 and p2:
                            # Convert mm to cm (Fusion uses cm internally)
                            p1_cm = (p1[0]/10.0, p1[1]/10.0, p1[2]/10.0) if len(p1) > 2 else (p1[0]/10.0, p1[1]/10.0, 0)
                            p2_cm = (p2[0]/10.0, p2[1]/10.0, p2[2]/10.0) if len(p2) > 2 else (p2[0]/10.0, p2[1]/10.0, 0)
                            print(f"[DEBUG] Creating rectangle from p1_cm={p1_cm}, p2_cm={p2_cm}")
                            rect_obj = sketch.sketchCurves.sketchLines.addTwoPointRectangle(
                                adsk.core.Point3D.create(p1_cm[0], p1_cm[1], 0),
                                adsk.core.Point3D.create(p2_cm[0], p2_cm[1], 0),
                            )
                            print(f"[DEBUG] Rectangle created, type: {type(rect_obj)}")
                            mapping[f"debug_rect_{ent.get('id', 'unknown')}_created"] = "success"
                            try:
                                if bool(ent.get("construction") or ent.get("is_construction") or ent.get("construction_geometry")):
                                    # addTwoPointRectangle returns a collection of lines in many API versions
                                    if hasattr(rect_obj, "count") and hasattr(rect_obj, "item"):
                                        for i in range(getattr(rect_obj, "count", 0)):
                                            try:
                                                rect_obj.item(i).isConstruction = True
                                            except Exception:
                                                pass
                                    else:
                                        try:
                                            rect_obj.isConstruction = True
                                        except Exception:
                                            pass
                            except Exception:
                                pass
                            if ent.get("id") is not None:
                                ent_objects[ent.get("id")] = rect_obj
                                entity_to_sketch[ent.get("id")] = sketch
                    elif kind == "circle":
                        c = self._parse_point(ent.get("center"))
                        d_mm = self._parse_length_mm(ent.get("d"))
                        if c and d_mm:
                            r_cm = (d_mm / 2.0) / 10.0
                            circle_obj = sketch.sketchCurves.sketchCircles.addByCenterRadius(
                                adsk.core.Point3D.create(c[0], c[1], 0), r_cm
                            )
                            try:
                                if bool(ent.get("construction") or ent.get("is_construction") or ent.get("construction_geometry")):
                                    circle_obj.isConstruction = True
                            except Exception:
                                pass
                            if ent.get("id") is not None:
                                ent_objects[ent.get("id")] = circle_obj
                                entity_to_sketch[ent.get("id")] = sketch
                    elif kind == "point":
                        at = self._parse_point(ent.get("at"))
                        if at:
                            pt_obj = sketch.sketchPoints.add(adsk.core.Point3D.create(at[0], at[1], 0))
                            try:
                                if bool(ent.get("construction") or ent.get("is_construction") or ent.get("construction_geometry")):
                                    # SketchPoint may not support construction flag; best-effort
                                    setattr(pt_obj, "isConstruction", True)  # may no-op on some versions
                            except Exception:
                                pass
                            if ent.get("id") is not None:
                                ent_objects[ent.get("id")] = pt_obj
                                entity_to_sketch[ent.get("id")] = sketch
                    elif kind == "line":
                        p1 = self._parse_point(ent.get("p1"))
                        p2 = self._parse_point(ent.get("p2"))
                        if p1 and p2:
                            line_obj = sketch.sketchCurves.sketchLines.addByTwoPoints(
                                adsk.core.Point3D.create(p1[0], p1[1], 0),
                                adsk.core.Point3D.create(p2[0], p2[1], 0),
                            )
                            try:
                                if bool(ent.get("construction") or ent.get("is_construction") or ent.get("construction_geometry")):
                                    line_obj.isConstruction = True
                            except Exception:
                                pass
                            if ent.get("id") is not None:
                                ent_objects[ent.get("id")] = line_obj
                                entity_to_sketch[ent.get("id")] = sketch
                    elif kind == "arc":
                        ctr = self._parse_point(ent.get("center"))
                        ps = self._parse_point(ent.get("start"))
                        pe = self._parse_point(ent.get("end"))
                        if ctr and ps and pe:
                            try:
                                arc_obj = sketch.sketchCurves.sketchArcs.addByCenterStartEnd(
                                    adsk.core.Point3D.create(ctr[0], ctr[1], 0),
                                    adsk.core.Point3D.create(ps[0], ps[1], 0),
                                    adsk.core.Point3D.create(pe[0], pe[1], 0),
                                )
                                try:
                                    if bool(ent.get("construction") or ent.get("is_construction") or ent.get("construction_geometry")):
                                        arc_obj.isConstruction = True
                                except Exception:
                                    pass
                                if ent.get("id") is not None:
                                    ent_objects[ent.get("id")] = arc_obj
                                    entity_to_sketch[ent.get("id")] = sketch
                            except Exception:
                                pass
                    elif kind == "spline":
                        pts = ent.get("points") or []
                        if isinstance(pts, list) and len(pts) >= 2:
                            try:
                                col = adsk.core.ObjectCollection.create()
                                for p in pts:
                                    pp = self._parse_point(p if isinstance(p, str) else None)
                                    if pp:
                                        col.add(adsk.core.Point3D.create(pp[0], pp[1], 0))
                                if col.count >= 2:
                                    spline_obj = sketch.sketchCurves.sketchFittedSplines.add(col)
                                    try:
                                        if bool(ent.get("construction") or ent.get("is_construction") or ent.get("construction_geometry")):
                                            spline_obj.isConstruction = True
                                    except Exception:
                                        pass
                                    if ent.get("id") is not None:
                                        ent_objects[ent.get("id")] = spline_obj
                            except Exception:
                                pass
                    elif kind == "ellipse":
                        ctr = self._parse_point(ent.get("center"))
                        major = self._parse_point(ent.get("major"))
                        minor_r_mm = self._parse_length_mm(ent.get("minor_r"))
                        if ctr and major and minor_r_mm is not None:
                            try:
                                cpt = adsk.core.Point3D.create(ctr[0], ctr[1], 0)
                                maj = adsk.core.Point3D.create(major[0], major[1], 0)
                                # Compute a perpendicular minor axis point at distance minor_r
                                vx = maj.x - cpt.x
                                vy = maj.y - cpt.y
                                vlen = (vx * vx + vy * vy) ** 0.5 or 1.0
                                ux = -vy / vlen
                                uy = vx / vlen
                                mr_cm = (minor_r_mm / 10.0)
                                min_pt = adsk.core.Point3D.create(cpt.x + ux * mr_cm, cpt.y + uy * mr_cm, 0)
                                ell_obj = sketch.sketchCurves.sketchEllipses.add(cpt, maj, min_pt)
                                try:
                                    if bool(ent.get("construction") or ent.get("is_construction") or ent.get("construction_geometry")):
                                        ell_obj.isConstruction = True
                                except Exception:
                                    pass
                                if ent.get("id") is not None:
                                    ent_objects[ent.get("id")] = ell_obj
                                    entity_to_sketch[ent.get("id")] = sketch
                            except Exception:
                                pass
                    elif kind == "elliptical_arc":
                        ctr = self._parse_point(ent.get("center"))
                        major = self._parse_point(ent.get("major"))
                        minor_r_mm = self._parse_length_mm(ent.get("minor_r"))
                        sa_deg = self._parse_length_mm(str(ent.get("start_angle") or "0"))
                        ea_deg = self._parse_length_mm(str(ent.get("end_angle") or "90"))
                        if ctr and major and minor_r_mm is not None and sa_deg is not None and ea_deg is not None:
                            try:
                                cpt = adsk.core.Point3D.create(ctr[0], ctr[1], 0)
                                maj = adsk.core.Point3D.create(major[0], major[1], 0)
                                # Build orthonormal basis from center->major
                                vx = maj.x - cpt.x
                                vy = maj.y - cpt.y
                                vlen = (vx * vx + vy * vy) ** 0.5 or 1.0
                                ux = vx / vlen
                                uy = vy / vlen
                                # Minor axis unit
                                mx = -uy
                                my = ux
                                # Radii in cm
                                a = vlen
                                b = (minor_r_mm / 10.0)
                                import math
                                sa = (sa_deg / 180.0) * math.pi
                                ea = (ea_deg / 180.0) * math.pi
                                sp = adsk.core.Point3D.create(cpt.x + a * math.cos(sa) * ux + b * math.sin(sa) * mx,
                                                              cpt.y + a * math.cos(sa) * uy + b * math.sin(sa) * my, 0)
                                ep = adsk.core.Point3D.create(cpt.x + a * math.cos(ea) * ux + b * math.sin(ea) * mx,
                                                              cpt.y + a * math.cos(ea) * uy + b * math.sin(ea) * my, 0)
                                try:
                                    ellarc_obj = sketch.sketchCurves.sketchEllipticalArcs.add(cpt, maj, adsk.core.Point3D.create(cpt.x + mx * b, cpt.y + my * b, 0), sp, ep)
                                    try:
                                        if bool(ent.get("construction") or ent.get("is_construction") or ent.get("construction_geometry")):
                                            ellarc_obj.isConstruction = True
                                    except Exception:
                                        pass
                                    if ent.get("id") is not None:
                                        ent_objects[ent.get("id")] = ellarc_obj
                                except Exception:
                                    # Fallback: approximate with fitted spline through 16 points
                                    col = adsk.core.ObjectCollection.create()
                                    steps = 16
                                    for i in range(steps + 1):
                                        t = sa + (ea - sa) * (i / steps)
                                        px = cpt.x + a * math.cos(t) * ux + b * math.sin(t) * mx
                                        py = cpt.y + a * math.cos(t) * uy + b * math.sin(t) * my
                                        col.add(adsk.core.Point3D.create(px, py, 0))
                                    spline_obj = sketch.sketchCurves.sketchFittedSplines.add(col)
                                    try:
                                        if bool(ent.get("construction") or ent.get("is_construction") or ent.get("construction_geometry")):
                                            spline_obj.isConstruction = True
                                    except Exception:
                                        pass
                                    if ent.get("id") is not None:
                                        ent_objects[ent.get("id")] = spline_obj
                            except Exception:
                                pass
                    elif kind == "text":
                        txt = ent.get("text") or ""
                        at = self._parse_point(ent.get("at"))
                        h_mm = self._parse_length_mm(ent.get("height") or "5") or 5.0
                        ang_deg = self._parse_length_mm(str(ent.get("angle") or "0")) or 0.0
                        if at:
                            try:
                                height_cm = h_mm / 10.0
                                pos = adsk.core.Point3D.create(at[0], at[1], 0)
                                # Preferred API: create input then add
                                try:
                                    ti = sketch.sketchTexts.createInput(txt, height_cm)
                                    ti.setAsMultiLine(pos, 0.0, adsk.core.HorizontalAlignments.LeftHorizontalAlignment, adsk.core.VerticalAlignments.TopVerticalAlignment, 0.0)
                                    txt_obj = sketch.sketchTexts.add(ti)
                                except Exception:
                                    # Fallback older API
                                    txt_obj = sketch.sketchTexts.add(txt, pos, height_cm)
                                if ent.get("id") is not None:
                                    ent_objects[ent.get("id")] = txt_obj
                            except Exception:
                                pass
                sketch_map[sk_id] = sketch
                # Constraints
                try:
                    for cst in sk.get("constraints", []) or []:
                        ckind = (cst.get("kind") or cst.get("type") or "").lower()
                        a = ent_objects.get(cst.get("a")) if isinstance(cst.get("a"), str) else None
                        b = ent_objects.get(cst.get("b")) if isinstance(cst.get("b"), str) else None
                        cons = sketch.geometricConstraints
                        dims = sketch.sketchDimensions
                        if ckind == "coincident" and a and b:
                            cons.addCoincident(a, b)
                        elif ckind in ("coincident_to_spline", "point_on_spline") and a and b:
                            # Alias to coincident; Fusion allows point-on-curve via coincident
                            try:
                                cons.addCoincident(a, b)
                            except Exception:
                                pass
                        elif ckind in ("point_on", "point_on_curve", "point_on_line", "point_on_circle", "point_on_arc", "coincident_to_curve") and a and b:
                            try:
                                cons.addCoincident(a, b)
                            except Exception:
                                pass
                        elif ckind == "colinear" and a and b:
                            cons.addCollinear(a, b)
                        elif ckind == "parallel" and a and b:
                            cons.addParallel(a, b)
                        elif ckind == "perpendicular" and a and b:
                            cons.addPerpendicular(a, b)
                        elif ckind == "concentric" and a and b:
                            cons.addConcentric(a, b)
                        elif ckind == "equal" and a and b:
                            cons.addEqual(a, b)
                        elif ckind in ("equal_length", "equal_lengths"):
                            # Apply equal across an array of entities: items: [id1, id2, id3...]
                            try:
                                items = cst.get("items") or cst.get("entities") or []
                                if isinstance(items, list) and len(items) >= 2:
                                    prev = None
                                    for ent_id in items:
                                        ent_obj = ent_objects.get(ent_id) if isinstance(ent_id, str) else None
                                        if ent_obj is None:
                                            continue
                                        if prev is not None:
                                            try:
                                                cons.addEqual(prev, ent_obj)
                                            except Exception:
                                                pass
                                        prev = ent_obj
                            except Exception:
                                pass
                        elif ckind == "horizontal" and a:
                            cons.addHorizontal(a)
                        elif ckind == "vertical" and a:
                            cons.addVertical(a)
                        elif ckind == "symmetric" and a and b and cst.get("about"):
                            about = ent_objects.get(cst.get("about"))
                            if about:
                                cons.addSymmetry(a, b, about)
                        elif ckind == "tangent" and a and b:
                            cons.addTangent(a, b)
                        elif ckind in ("curvature", "curvature_continuity", "g2") and a and b:
                            # Attempt curvature continuity (G2) using any available API; fall back to tangent with info diagnostic
                            try:
                                ent_a = a
                                ent_b = b
                                try:
                                    if hasattr(ent_a, "parentCurve") and getattr(ent_a, "parentCurve") is not None:
                                        ent_a = ent_a.parentCurve
                                except Exception:
                                    pass
                                try:
                                    if hasattr(ent_b, "parentCurve") and getattr(ent_b, "parentCurve") is not None:
                                        ent_b = ent_b.parentCurve
                                except Exception:
                                    pass
                                applied = False
                                for m in ("addCurvature", "addCurvatureConstraint", "addG2", "addCurvatureContinuous"):
                                    try:
                                        fn = getattr(cons, m)
                                        if callable(fn):
                                            fn(ent_a, ent_b)
                                            applied = True
                                            break
                                    except Exception:
                                        continue
                                if not applied:
                                    try:
                                        cons.addTangent(ent_a, ent_b)
                                        self._diag("E1205I", where="sketch", message="Curvature continuity unavailable; applied tangent as best-effort")
                                    except Exception:
                                        self._diag("E1205", where="sketch", message="Curvature constraint not supported by this Fusion version; consider tangent + smoothing")
                            except Exception:
                                try:
                                    self._diag("E1205", where="sketch", message="Curvature constraint failed to apply on these entities")
                                except Exception:
                                    pass
                        elif ckind == "midpoint" and a and b:
                            cons.addMidPoint(a, b)
                        elif ckind in ("lock", "fix") and a:
                            cons.addFixed(a)
                        elif ckind == "distance" and a and b:
                            d_mm = self._parse_length_mm(cst.get("value") or cst.get("d") or cst.get("distance")) or 0.0
                            orient_str = (cst.get("orientation") or cst.get("orient") or "aligned").lower()
                            try:
                                # Prefer orientation signature when available
                                dd = None
                                orient_enum = None
                                try:
                                    import adsk.fusion  # type: ignore
                                    enum_t = getattr(adsk.fusion, "SketchDimensionOrientations", None) or getattr(adsk.fusion, "DimensionOrientations", None)
                                    if enum_t:
                                        if orient_str.startswith("hor"):
                                            orient_enum = getattr(enum_t, "HorizontalDimensionOrientation", None)
                                        elif orient_str.startswith("ver"):
                                            orient_enum = getattr(enum_t, "VerticalDimensionOrientation", None)
                                        else:
                                            orient_enum = getattr(enum_t, "AlignedDimensionOrientation", None)
                                except Exception:
                                    orient_enum = None
                                if orient_enum is not None:
                                    try:
                                        dd = dims.addDistanceDimension(a, b, orient_enum, adsk.core.Point3D.create(0, 0, 0))
                                    except Exception:
                                        dd = None
                                if dd is None:
                                    dd = dims.addDistanceDimension(a, b, adsk.core.Point3D.create(0, 0, 0))
                                # Set value in cm units
                                try:
                                    dd.parameter.value = (d_mm / 10.0)
                                except Exception:
                                    pass
                                # Driven/reference flags
                                try:
                                    driven = cst.get("driven")
                                    if driven is None:
                                        driven = cst.get("reference")
                                    if driven is not None:
                                        for attr in ("isDriving", "isReference"):
                                            if hasattr(dd, attr):
                                                try:
                                                    setattr(dd, attr, False if attr == "isDriving" and bool(driven) else (True if attr == "isReference" and bool(driven) else getattr(dd, attr)))
                                                except Exception:
                                                    pass
                                        try:
                                            if hasattr(dd, "parameter") and hasattr(dd.parameter, "isDriving"):
                                                dd.parameter.isDriving = (not bool(driven))
                                        except Exception:
                                            pass
                                        try:
                                            if hasattr(dd, "parameter") and hasattr(dd.parameter, "isDriven"):
                                                dd.parameter.isDriven = bool(driven)
                                        except Exception:
                                            pass
                                except Exception:
                                    pass
                            except Exception:
                                pass
                        elif ckind in ("equal_radius", "equal_radii") and a and b:
                            # Equal radius for arcs/circles maps to Equal constraint in Fusion
                            try:
                                cons.addEqual(a, b)
                            except Exception:
                                pass
                        elif ckind == "angle" and a and b:
                            ang_deg = self._parse_length_mm(cst.get("value") or cst.get("angle")) or 0.0
                            try:
                                ad = dims.addAngleDimension(a, b, adsk.core.Point3D.create(0, 0, 0))
                                ad.parameter.value = (ang_deg / 180.0) * 3.141592653589793
                                try:
                                    driven = cst.get("driven")
                                    if driven is None:
                                        driven = cst.get("reference")
                                    if driven is not None:
                                        try:
                                            ad.isDriving = (not bool(driven))
                                        except Exception:
                                            pass
                                        try:
                                            ad.isReference = bool(driven)
                                        except Exception:
                                            pass
                                        try:
                                            ad.parameter.isDriving = (not bool(driven))
                                        except Exception:
                                            pass
                                        try:
                                            ad.parameter.isDriven = bool(driven)
                                        except Exception:
                                            pass
                                except Exception:
                                    pass
                            except Exception:
                                pass
                        elif ckind in ("radius", "radial") and a:
                            # Radius dimension for arcs/circles
                            try:
                                dim_pt = adsk.core.Point3D.create(0, 0, 0)
                                rd = None
                                if hasattr(dims, "addRadiusDimension"):
                                    rd = dims.addRadiusDimension(a, dim_pt)
                                elif hasattr(dims, "addRadialDimension"):
                                    rd = dims.addRadialDimension(a, dim_pt)
                                if rd is not None and cst.get("value") is not None:
                                    r_mm = self._parse_length_mm(cst.get("value")) or 0.0
                                    try:
                                        rd.parameter.value = (r_mm / 10.0)
                                    except Exception:
                                        pass
                                # Reference/driven handling
                                try:
                                    driven = cst.get("driven")
                                    if driven is None:
                                        driven = cst.get("reference")
                                    if driven is not None and rd is not None:
                                        for attr in ("isDriving", "isReference"):
                                            if hasattr(rd, attr):
                                                try:
                                                    setattr(rd, attr, False if attr == "isDriving" and bool(driven) else (True if attr == "isReference" and bool(driven) else getattr(rd, attr)))
                                                except Exception:
                                                    pass
                                        try:
                                            if hasattr(rd, "parameter") and hasattr(rd.parameter, "isDriving"):
                                                rd.parameter.isDriving = (not bool(driven))
                                        except Exception:
                                            pass
                                except Exception:
                                    pass
                            except Exception:
                                pass
                        elif ckind in ("diameter", "dia") and a:
                            # Diameter dimension for circles
                            try:
                                dim_pt = adsk.core.Point3D.create(0, 0, 0)
                                dd = None
                                if hasattr(dims, "addDiameterDimension"):
                                    dd = dims.addDiameterDimension(a, dim_pt)
                                if dd is not None and cst.get("value") is not None:
                                    d_mm = self._parse_length_mm(cst.get("value")) or 0.0
                                    try:
                                        dd.parameter.value = (d_mm / 10.0)
                                    except Exception:
                                        pass
                                try:
                                    driven = cst.get("driven")
                                    if driven is None:
                                        driven = cst.get("reference")
                                    if driven is not None and dd is not None:
                                        for attr in ("isDriving", "isReference"):
                                            if hasattr(dd, attr):
                                                try:
                                                    setattr(dd, attr, False if attr == "isDriving" and bool(driven) else (True if attr == "isReference" and bool(driven) else getattr(dd, attr)))
                                                except Exception:
                                                    pass
                                        try:
                                            if hasattr(dd, "parameter") and hasattr(dd.parameter, "isDriving"):
                                                dd.parameter.isDriving = (not bool(driven))
                                        except Exception:
                                            pass
                                except Exception:
                                    pass
                            except Exception:
                                pass
                except Exception:
                    pass

                # Dimensions (driving/reference)
                try:
                    dims = sketch.sketchDimensions
                    for dim in sk.get("dimensions", []) or []:
                        dkind = (dim.get("kind") or dim.get("type") or "").lower()
                        target = ent_objects.get(dim.get("on")) if isinstance(dim.get("on"), str) else None
                        val_mm = self._parse_length_mm(dim.get("value"))
                        if dkind in ("diameter", "radius") and target is not None and val_mm is not None:
                            if dkind == "diameter":
                                dd = dims.addDiameterDimension(target, adsk.core.Point3D.create(0, 0, 0))
                                try:
                                    dd.parameter.value = (val_mm / 10.0)
                                except Exception:
                                    pass
                                try:
                                    driven = dim.get("driven")
                                    if driven is None:
                                        driven = dim.get("reference")
                                    if driven is not None:
                                        try:
                                            dd.isDriving = (not bool(driven))
                                        except Exception:
                                            pass
                                        try:
                                            dd.isReference = bool(driven)
                                        except Exception:
                                            pass
                                        try:
                                            dd.parameter.isDriving = (not bool(driven))
                                        except Exception:
                                            pass
                                        try:
                                            dd.parameter.isDriven = bool(driven)
                                        except Exception:
                                            pass
                                except Exception:
                                    pass
                            else:
                                rd = dims.addRadialDimension(target, adsk.core.Point3D.create(0, 0, 0))
                                try:
                                    rd.parameter.value = (val_mm / 10.0)
                                except Exception:
                                    pass
                                try:
                                    driven = dim.get("driven")
                                    if driven is None:
                                        driven = dim.get("reference")
                                    if driven is not None:
                                        try:
                                            rd.isDriving = (not bool(driven))
                                        except Exception:
                                            pass
                                        try:
                                            rd.isReference = bool(driven)
                                        except Exception:
                                            pass
                                        try:
                                            rd.parameter.isDriving = (not bool(driven))
                                        except Exception:
                                            pass
                                        try:
                                            rd.parameter.isDriven = bool(driven)
                                        except Exception:
                                            pass
                                except Exception:
                                    pass
                        elif dkind == "distance" and target is not None and isinstance(dim.get("to"), str):
                            t2 = ent_objects.get(dim.get("to"))
                            if t2 and val_mm is not None:
                                dd = dims.addDistanceDimension(target, t2, adsk.core.Point3D.create(0, 0, 0))
                                try:
                                    dd.parameter.value = (val_mm / 10.0)
                                except Exception:
                                    pass
                                try:
                                    driven = dim.get("driven")
                                    if driven is None:
                                        driven = dim.get("reference")
                                    if driven is not None:
                                        try:
                                            dd.isDriving = (not bool(driven))
                                        except Exception:
                                            pass
                                        try:
                                            dd.isReference = bool(driven)
                                        except Exception:
                                            pass
                                        try:
                                            dd.parameter.isDriving = (not bool(driven))
                                        except Exception:
                                            pass
                                        try:
                                            dd.parameter.isDriven = bool(driven)
                                        except Exception:
                                            pass
                                except Exception:
                                    pass
                        elif dkind == "angle" and target is not None and isinstance(dim.get("to"), str):
                            t2 = ent_objects.get(dim.get("to"))
                            ang_deg = self._parse_length_mm(dim.get("value"))
                            if t2 and ang_deg is not None:
                                ad = dims.addAngleDimension(target, t2, adsk.core.Point3D.create(0, 0, 0))
                                try:
                                    ad.parameter.value = (ang_deg / 180.0) * 3.141592653589793
                                except Exception:
                                    pass
                                try:
                                    driven = dim.get("driven")
                                    if driven is None:
                                        driven = dim.get("reference")
                                    if driven is not None:
                                        try:
                                            ad.isDriving = (not bool(driven))
                                        except Exception:
                                            pass
                                        try:
                                            ad.isReference = bool(driven)
                                        except Exception:
                                            pass
                                        try:
                                            ad.parameter.isDriving = (not bool(driven))
                                        except Exception:
                                            pass
                                        try:
                                            ad.parameter.isDriven = bool(driven)
                                        except Exception:
                                            pass
                                except Exception:
                                    pass
                except Exception:
                    pass

            # Execute features (limited: extrude, fillet)
            print(f"[DEBUG] Processing {len(csl_ir.get('features', []))} features")
            features_list = csl_ir.get("features", []) or []
            print(f"[FusionBackend.realize] Processing {len(features_list)} features")
            
            for feat in features_list:
                if not isinstance(feat, dict):
                    continue
                kind = (feat.get("type") or feat.get("kind") or "").lower()
                feat_id = feat.get("id") or kind
                print(f"[FusionBackend.realize] Processing feature kind: {kind}, id: {feat_id}")
                
                # Special debug for chamfer
                if kind == "chamfer":
                    print(f"[CHAMFER DEBUG] About to process chamfer: {feat_id}")
                    print(f"[CHAMFER DEBUG] Feature data: {feat}")
                
                # Add to mapping immediately to track what we're trying to process
                mapping[feat_id] = f"processing_{kind}"
                mapping[f"debug_feat_{feat_id}_kind"] = kind
                if kind == "extrude":
                    # Resolve profile from feature specification
                    profile = None
                    profile_spec = feat.get("profile")
                    
                    # Try to find the profile based on the profile specification
                    print(f"[DEBUG] Looking for profile: {profile_spec}")
                    print(f"[DEBUG] entity_to_sketch keys: {list(entity_to_sketch.keys())}")
                    print(f"[DEBUG] sketch_map keys: {list(sketch_map.keys())}")
                    if profile_spec and isinstance(profile_spec, str):
                        # Check if profile_spec is an entity ID that we tracked
                        if profile_spec in entity_to_sketch:
                            # Get the sketch that contains this entity
                            target_sketch = entity_to_sketch[profile_spec]
                            print(f"[DEBUG] Found sketch for entity {profile_spec}, profiles: {target_sketch.profiles.count}")
                            if target_sketch.profiles.count > 0:
                                # Use the first profile from this sketch
                                # TODO: Better profile selection if multiple profiles exist
                                profile = target_sketch.profiles.item(0)
                                print(f"[DEBUG] Using profile from entity's sketch")
                        
                        # If not found, check if it's a sketch ID
                        elif profile_spec in sketch_map:
                            target_sketch = sketch_map[profile_spec]
                            print(f"[DEBUG] Found sketch {profile_spec}, profiles: {target_sketch.profiles.count}")
                            if target_sketch.profiles.count > 0:
                                profile = target_sketch.profiles.item(0)
                                print(f"[DEBUG] Using profile from sketch ID")
                    
                    # If no profile found yet, use the most recently created sketch with profiles
                    if profile is None and root.sketches.count > 0:
                        # Iterate backwards through sketches (most recent first)
                        for i in range(root.sketches.count - 1, -1, -1):
                            sk = root.sketches.item(i)
                            if sk.profiles.count > 0:
                                profile = sk.profiles.item(0)
                                break
                    
                    # Final fallback to first available profile
                    if profile is None:
                        profile = self._first_profile(root)
                    
                    if profile is None:
                        error_msg = f"No profile found for extrude '{feat_id}'"
                        print(f"ERROR: {error_msg}")
                        mapping[feat_id] = f"error:no_profile"
                        continue
                        
                    dist_mm = self._parse_length_mm(feat.get("distance")) or 10.0
                    dist_cm = dist_mm / 10.0
                    distance = adsk.core.ValueInput.createByReal(dist_cm)
                    ext_feats = root.features.extrudeFeatures
                    op = self._feature_operation(feat.get("operation") or feat.get("op"))
                    try:
                        ext_input = ext_feats.createInput(profile, op)
                        ext_input.setDistanceExtent(False, distance)
                        ext = ext_feats.add(ext_input)
                        mapping[feat_id] = f"fusion:extrude:{ext.entityToken}"
                    except Exception as e:
                        error_msg = f"Extrude '{feat_id}' failed: {str(e)}"
                        print(f"ERROR: {error_msg}")
                        mapping[feat_id] = f"error:{error_msg}"
                        # Re-raise to make failure visible
                        raise Exception(error_msg)
                elif kind == "fillet":
                    mapping[feat_id] = "fillet:starting"
                    print(f"[DEBUG] Processing fillet feature: {feat_id}")
                    rad_mm = self._parse_length_mm(feat.get("radius")) or 1.0
                    rad_cm = rad_mm / 10.0
                    print(f"[DEBUG] Fillet radius: {rad_mm}mm ({rad_cm}cm)")
                    mapping[feat_id] = f"fillet:radius_{rad_mm}mm"
                    
                    # Resolve edges via query if provided; else use all edges
                    edges = None
                    try:
                        q_spec = feat.get("edges_query") or (feat.get("edges") if isinstance(feat.get("edges"), dict) else None)
                        if q_spec:
                            edges = self._resolve_query(root, q_spec, entity_type="edge")
                    except Exception as e:
                        mapping[feat_id] = f"error:edge_query_failed:{str(e)}"
                        edges = None
                    
                    edges = edges or self._all_body_edges(root)
                    edge_count = edges.count if edges else 0
                    print(f"[DEBUG] Found {edge_count} edges to fillet")
                    mapping[feat_id] = f"fillet:found_{edge_count}_edges"
                    
                    # Check if we have edges
                    if not edges or edges.count == 0:
                        print(f"[ERROR] No edges found for fillet")
                        mapping[feat_id] = f"error:no_edges_found:bodies={root.bRepBodies.count}"
                        continue
                    
                    # Transitions: support 'setback' at feature level when possible
                    if feat.get("transitions"):
                        mapping[feat_id] = "fillet:checking_transitions"
                        try:
                            trans = feat.get("transitions")
                            # Alias: transitions.setbacks or transitions.setback -> feature-level setbacks
                            if isinstance(trans, dict) and (trans.get("setbacks") or trans.get("setback") or trans.get("d")):
                                # Prefer explicit vertex list if provided, else apply uniform setback to all vertices of target edges
                                explicit_list = trans.get("setbacks") if isinstance(trans.get("setbacks"), list) else None
                                target_query = feat.get("edges_query") or feat.get("edges")
                                fil_feats = root.features.filletFeatures
                                if explicit_list and (isinstance(target_query, dict)):
                                    grp = {"edges_query": target_query, "setbacks": explicit_list}
                                    var_feat = self._apply_variable_fillet(root, fil_feats, grp)
                                    if var_feat:
                                        mapping[f"{feat_id}:setbacks"] = f"fusion:fillet:{var_feat.entityToken}"
                                        # Continue with remaining logic but skip default constant fillet when variable handled
                                        continue
                                # Uniform setback distance
                                d_mm = self._parse_length_mm(trans.get("setback") or trans.get("d") or trans.get("distance"))
                                if d_mm is not None:
                                    try:
                                        import adsk.core  # type: ignore
                                        # Build edge collection from query or all edges
                                        ecol = None
                                        if isinstance(target_query, dict):
                                            ecol = self._resolve_query(root, target_query, entity_type="edge")
                                        ecol = ecol or self._all_body_edges(root)
                                        if ecol and ecol.count > 0 and hasattr(fil_feats, "createSetbackFilletDefinition"):
                                            sdef = fil_feats.createSetbackFilletDefinition(ecol)
                                            # Collect unique corner vertices from the edges
                                            seen = set()
                                            for i in range(ecol.count):
                                                try:
                                                    e = ecol.item(i)
                                                    for v in (getattr(e, "startVertex", None), getattr(e, "endVertex", None)):
                                                        if v is None:
                                                            continue
                                                        vid = getattr(v, "entityToken", None) or id(v)
                                                        if vid in seen:
                                                            continue
                                                        seen.add(vid)
                                                        sdef.setSetbackDistance(v, adsk.core.ValueInput.createByReal(d_mm/10.0))
                                                except Exception:
                                                    continue
                                            sf = fil_feats.add(sdef)
                                            mapping[f"{feat_id}:setbacks"] = f"fusion:fillet:{sf.entityToken}"
                                            # Skip the default constant fillet when setback applied
                                            continue
                                    except Exception:
                                        pass
                            else:
                                # Unknown transition type -> diagnostic only
                                self._diag("E2320", where="fillet", message="Requested fillet transitions not supported; proceeding without transitions")
                        except Exception:
                            pass
                    # Feature-level setbacks across provided edges (requires edges_query/q spec)
                    if isinstance(feat.get("setbacks"), list) and (isinstance(feat.get("edges"), dict) or isinstance(feat.get("edges_query"), dict)):
                        mapping[feat_id] = "fillet:checking_setbacks"
                        try:
                            grp = {"edges_query": (feat.get("edges_query") or feat.get("edges")), "setbacks": feat.get("setbacks")}
                            var_feat = self._apply_variable_fillet(root, fil_feats, grp)
                            if var_feat:
                                mapping[f"{feat_id}:setbacks"] = f"fusion:fillet:{var_feat.entityToken}"
                                continue
                        except Exception:
                            pass
                    if edges.count > 0:
                        mapping[feat_id] = f"fillet:processing_{edges.count}_edges"
                        print(f"[DEBUG] Creating fillet with {edges.count} edges")
                        fil_feats = root.features.filletFeatures
                        edge_col = adsk.core.ObjectCollection.create()
                        for i in range(edges.count):
                            e = edges.item(i)
                            edge_col.add(e)
                        print(f"[DEBUG] Edge collection created with {edge_col.count} edges")
                        # If per-edge groups provided, create separate constant fillets for each group
                        try:
                            per_groups = feat.get("edges") or []
                            print(f"[DEBUG] per_groups: {per_groups}, is list: {isinstance(per_groups, list)}, len: {len(per_groups) if isinstance(per_groups, list) else 'N/A'}")
                            if isinstance(per_groups, list) and len(per_groups) > 0:
                                # Attempt variable radius or vertex setbacks if provided
                                used_variable = False
                                for grp in per_groups:
                                    if not isinstance(grp, dict):
                                        continue
                                    if grp.get("points") or grp.get("setbacks"):
                                        try:
                                            var_feat = self._apply_variable_fillet(root, fil_feats, grp)
                                            if var_feat:
                                                mapping[f"{feat_id}:var"] = f"fusion:fillet:{var_feat.entityToken}"
                                                used_variable = True
                                            continue
                                        except Exception:
                                            pass
                                if used_variable:
                                    continue
                                for grp in per_groups:
                                    if not isinstance(grp, dict):
                                        continue
                                    r_mm = self._parse_length_mm(grp.get("r") or grp.get("radius")) or rad_mm
                                    r_cm = (r_mm / 10.0)
                                    is_tc = bool(grp.get("tangent_chain") or grp.get("tangent") or False)
                                    grp_edges = None
                                    try:
                                        qg = grp.get("q") or grp.get("edges_query") or grp.get("edges")
                                        if qg:
                                            grp_edges = self._resolve_query(root, qg, entity_type="edge")
                                    except Exception:
                                        grp_edges = None
                                    grp_edges = grp_edges or edge_col
                                    const_def = fil_feats.createConstantRadiusFilletDefinition(grp_edges, adsk.core.ValueInput.createByReal(r_cm), is_tc)
                                    # Apply per-group transition options (corner type / chordal) if provided
                                    try:
                                        trans = grp.get("transitions") or grp.get("transition") or {}
                                        if isinstance(trans, dict):
                                            # Corner type mapping
                                            corner = str(trans.get("corner") or trans.get("corner_type") or trans.get("type") or "").lower()
                                            if corner and hasattr(const_def, "cornerType"):
                                                try:
                                                    import adsk.fusion  # type: ignore
                                                    enum_t = getattr(adsk.fusion, "FilletCornerTypes", None)
                                                    if enum_t:
                                                        pick = None
                                                        if "roll" in corner:
                                                            pick = getattr(enum_t, "RollingBallCornerType", None)
                                                        elif "setback" in corner:
                                                            pick = getattr(enum_t, "SetbackCornerType", None)
                                                        if pick is not None:
                                                            const_def.cornerType = pick
                                                except Exception:
                                                    pass
                                            # Chordal radius mode best-effort
                                            mode = str(trans.get("mode") or trans.get("radius_mode") or "").lower()
                                            if mode and ("chord" in mode or "chordal" in mode):
                                                for attr in ("isChordalRadius", "useChordLength", "isUsingChordalRadius"):
                                                    if hasattr(const_def, attr):
                                                        try:
                                                            setattr(const_def, attr, True)
                                                            break
                                                        except Exception:
                                                            pass
                                    except Exception:
                                        pass
                                    fil = fil_feats.add(const_def)
                                    mapping[f"{feat_id}:grp"] = f"fusion:fillet:{fil.entityToken}"
                                # Skip the single-feature path when per-groups are processed
                                continue
                        except Exception:
                            pass
                        mapping[feat_id] = f"fillet:creating_main_fillet_{rad_cm}cm"
                        print(f"[DEBUG] Creating main fillet with radius {rad_cm}cm")
                        is_tc_global = bool(feat.get("tangent_chain") or feat.get("tangent") or False)
                        # Use createInput instead of createConstantRadiusFilletDefinition
                        const_def = fil_feats.createInput()
                        const_def.addConstantRadiusEdgeSet(edge_col, adsk.core.ValueInput.createByReal(rad_cm), is_tc_global)
                        print(f"[DEBUG] Fillet definition created")
                        # Apply feature-level transition options on the constant def as well
                        try:
                            trans = feat.get("transitions") or {}
                            if isinstance(trans, dict):
                                corner = str(trans.get("corner") or trans.get("corner_type") or trans.get("type") or "").lower()
                                if corner and hasattr(const_def, "cornerType"):
                                    try:
                                        import adsk.fusion  # type: ignore
                                        enum_t = getattr(adsk.fusion, "FilletCornerTypes", None)
                                        if enum_t:
                                            pick = None
                                            if "roll" in corner:
                                                pick = getattr(enum_t, "RollingBallCornerType", None)
                                            elif "setback" in corner:
                                                pick = getattr(enum_t, "SetbackCornerType", None)
                                            if pick is not None:
                                                const_def.cornerType = pick
                                    except Exception:
                                        pass
                                mode = str(trans.get("mode") or trans.get("radius_mode") or "").lower()
                                if mode and ("chord" in mode or "chordal" in mode):
                                    for attr in ("isChordalRadius", "useChordLength", "isUsingChordalRadius"):
                                        if hasattr(const_def, attr):
                                            try:
                                                setattr(const_def, attr, True)
                                                break
                                            except Exception:
                                                pass
                        except Exception:
                            pass
                        print(f"[DEBUG] Adding fillet to features...")
                        try:
                            fil = fil_feats.add(const_def)
                            print(f"[DEBUG] Fillet added successfully: {fil.entityToken}")
                            mapping[feat_id] = f"fusion:fillet:{fil.entityToken}"
                            try:
                                self._record_lineage(feat_id, fil, root)
                            except Exception:
                                pass
                        except Exception as e:
                            print(f"[ERROR] Failed to add fillet: {str(e)}")
                            mapping[feat_id] = f"error:fillet_failed:{str(e)}"
                    # End of if edges.count > 0 for fillet
                    else:
                        # If fillet has no edges, record error
                        mapping[feat_id] = f"error:fillet_no_edges"
                # End of fillet block completely
                elif kind == "chamfer":
                    print(f"[CHAMFER BLOCK ENTERED] Starting chamfer processing for {feat_id}")
                    mapping[feat_id] = "chamfer:entered_block"
                    print(f"[DEBUG] Starting chamfer processing for {feat_id}")
                    d_mm = self._parse_length_mm(feat.get("distance")) or 1.0
                    d_cm = d_mm / 10.0
                    print(f"[DEBUG] Chamfer distance: {d_mm}mm ({d_cm}cm)")
                    ang_deg_global = None
                    if feat.get("angle") is not None:
                        try:
                            ang_deg_global = float(self._parse_length_mm(str(feat.get("angle"))) or 0.0)
                        except Exception:
                            ang_deg_global = None
                    edges = None
                    try:
                        q_spec = feat.get("edges_query") or (feat.get("edges") if isinstance(feat.get("edges"), dict) else None)
                        print(f"[DEBUG] Chamfer query spec: {q_spec}")
                        if q_spec:
                            edges = self._resolve_query(root, q_spec, entity_type="edge")
                    except Exception as e:
                        print(f"[DEBUG] Edge query exception: {e}")
                        edges = None
                    # If no edges specified, get edges from the most recent body
                    if not edges:
                        # Get the last created body (should be our extruded box)
                        if root.bRepBodies.count > 0:
                            last_body = root.bRepBodies.item(root.bRepBodies.count - 1)
                            print(f"[DEBUG] Using edges from last body: {last_body.name if hasattr(last_body, 'name') else 'Body'}")
                            edges = adsk.core.ObjectCollection.create()
                            for edge in last_body.edges:
                                edges.add(edge)
                        else:
                            edges = self._all_body_edges(root)
                    
                    # Check if we have edges
                    edge_count = edges.count if edges else 0
                    print(f"[DEBUG] Found {edge_count} edges for chamfer from {root.bRepBodies.count} bodies")
                    if not edges or edges.count == 0:
                        mapping[feat_id] = f"error:no_edges_for_chamfer"
                        continue
                    
                    # Simple chamfer path - if no transitions or groups, create chamfer immediately
                    if not feat.get("transitions") and not feat.get("edges"):
                        print(f"[DEBUG] Taking simple chamfer path")
                        try:
                            chf = root.features.chamferFeatures
                            edge_col = adsk.core.ObjectCollection.create()
                            
                            # Filter edges to avoid corner conflicts - only take top edges or a subset
                            # Try to identify top edges by checking Z coordinate
                            top_edges = []
                            max_z = -float('inf')
                            
                            # First pass: find the max Z
                            for i in range(edges.count):
                                edge = edges.item(i)
                                z_start = edge.startVertex.geometry.z
                                z_end = edge.endVertex.geometry.z
                                max_z = max(max_z, z_start, z_end)
                            
                            print(f"[DEBUG] Max Z coordinate found: {max_z}cm")
                            
                            # Second pass: collect edges at max Z (top edges)
                            for i in range(edges.count):
                                edge = edges.item(i)
                                z_start = edge.startVertex.geometry.z
                                z_end = edge.endVertex.geometry.z
                                # Check if both vertices are at the top (horizontal edge)
                                if abs(z_start - max_z) < 0.001 and abs(z_end - max_z) < 0.001:
                                    # This is a horizontal edge at the top
                                    start_pt = edge.startVertex.geometry
                                    end_pt = edge.endVertex.geometry
                                    # Double-check it's horizontal (Z values are same, X or Y differs)
                                    if abs(start_pt.z - end_pt.z) < 0.001:
                                        print(f"[DEBUG] Top edge {len(top_edges)}: Start({start_pt.x:.2f}, {start_pt.y:.2f}, {start_pt.z:.2f}) -> End({end_pt.x:.2f}, {end_pt.y:.2f}, {end_pt.z:.2f}), Length={edge.length:.2f}cm")
                                        top_edges.append(edge)
                            
                            # Use top edges if we found them, selecting opposite edges to avoid conflicts
                            if len(top_edges) > 0:
                                print(f"[DEBUG] Found {len(top_edges)} top edges at Z={max_z}")
                                mapping[f"debug_top_edges_found"] = f"{len(top_edges)} edges at Z={max_z:.2f}cm"
                                # Select opposite edges (0 and 2, or just first 2 if less than 4)
                                if len(top_edges) >= 4:
                                    # Select opposite edges to avoid corner conflicts
                                    selected_indices = [0, 2]  # Opposite edges
                                    print(f"[DEBUG] Selecting opposite edges to avoid corner conflicts")
                                else:
                                    # If less than 4, take what we have
                                    selected_indices = range(min(2, len(top_edges)))
                                    print(f"[DEBUG] Only {len(top_edges)} edges found, selecting first {min(2, len(top_edges))}")
                                
                                edge_info = []
                                for idx in selected_indices:
                                    edge = top_edges[idx]
                                    edge_col.add(edge)
                                    edge_detail = f"Edge {idx}: length={edge.length:.2f}cm"
                                    print(f"[DEBUG] Added top {edge_detail}")
                                    edge_info.append(edge_detail)
                                mapping[f"debug_chamfer_edges"] = f"Selected: {', '.join(edge_info)}"
                            else:
                                print(f"[DEBUG] Could not identify top edges, using alternating edges")
                                # Use alternating edges to avoid conflicts
                                for i in range(0, min(8, edges.count), 2):  # Take every other edge, max 4
                                    if edge_col.count >= 2:  # Limit to 2 edges
                                        break
                                    edge = edges.item(i)
                                    edge_col.add(edge)
                                    print(f"[DEBUG] Added edge {i}: Z_start={edge.startVertex.geometry.z}, Z_end={edge.endVertex.geometry.z}, length={edge.length}cm")
                            
                            # Create chamfer definition
                            defn = None
                            if ang_deg_global is not None and hasattr(chf, "createDistanceAndAngleChamferDefinition"):
                                try:
                                    defn = chf.createDistanceAndAngleChamferDefinition(
                                        edge_col,
                                        adsk.core.ValueInput.createByReal(d_cm),
                                        adsk.core.ValueInput.createByReal((ang_deg_global / 180.0) * 3.141592653589793),
                                        False
                                    )
                                except Exception:
                                    defn = None
                            
                            if defn is None:
                                # Try creating chamfer - testing different approaches
                                print(f"[DEBUG] Trying chamfer creation with {edge_col.count} edges")
                                
                                # Use the modern API with createInput2
                                try:
                                    print(f"[DEBUG] Edge collection has {edge_col.count} edges")
                                    # Validate edges
                                    for i in range(min(3, edge_col.count)):
                                        edge = edge_col.item(i)
                                        print(f"[DEBUG] Edge {i}: isValid={edge.isValid}, length={edge.length}")
                                    
                                    # Create the chamfer input using the modern createInput2 method
                                    chamfer_input = chf.createInput2()
                                    print(f"[DEBUG] Created chamfer input with createInput2()")
                                    
                                    # Add the edge set with equal distance chamfer
                                    # The third parameter is isTangentChain - set to False to handle edges independently
                                    distance_value = adsk.core.ValueInput.createByReal(d_cm)
                                    chamfer_input.chamferEdgeSets.addEqualDistanceChamferEdgeSet(edge_col, distance_value, False)
                                    print(f"[DEBUG] Added equal distance edge set: {d_cm}cm ({d_cm * 10}mm) with isTangentChain=False")
                                    
                                    # Check body count before chamfer
                                    bodies_before = root.bRepBodies.count
                                    print(f"[DEBUG] Bodies before chamfer: {bodies_before}")
                                    mapping[f"debug_bodies_before_chamfer"] = f"{bodies_before}"
                                    
                                    # Now add it
                                    ch = chf.add(chamfer_input)
                                    print(f"[DEBUG] Chamfer created successfully!")
                                    print(f"[DEBUG] Chamfer type: {ch.chamferType if hasattr(ch, 'chamferType') else 'unknown'}")
                                    print(f"[DEBUG] Chamfer has {ch.edgeSets.count if hasattr(ch, 'edgeSets') else 0} edge sets")
                                    
                                    # Check if chamfer modified existing body or created new one
                                    bodies_after = root.bRepBodies.count
                                    print(f"[DEBUG] Bodies after chamfer: {bodies_after}")
                                    mapping[f"debug_bodies_after_chamfer"] = f"{bodies_after}"
                                    if bodies_after > bodies_before:
                                        print(f"[WARNING] Chamfer created NEW body instead of modifying existing!")
                                        mapping[f"debug_chamfer_issue"] = f"NEW BODY CREATED! {bodies_before} -> {bodies_after}"
                                    else:
                                        print(f"[DEBUG] Chamfer modified existing body (good)")
                                        mapping[f"debug_chamfer_behavior"] = f"Modified existing body (good)"
                                    
                                    # Force update/refresh
                                    try:
                                        if hasattr(ch, 'isValid') and ch.isValid:
                                            print(f"[DEBUG] Chamfer is valid")
                                            # Check affected bodies
                                            if hasattr(ch, 'bodies'):
                                                print(f"[DEBUG] Chamfer affects {ch.bodies.count} bodies")
                                    except Exception as ex:
                                        print(f"[DEBUG] Could not check chamfer details: {ex}")
                                    
                                    mapping[feat_id] = f"fusion:chamfer:{ch.entityToken}"
                                    print(f"[DEBUG] Chamfer succeeded: {ch.entityToken}")
                                    continue  # Skip the rest
                                except Exception as e1:
                                    error_msg = str(e1)
                                    print(f"[DEBUG] Modern API (createInput2) failed: {error_msg}")
                                    import traceback
                                    print(f"[DEBUG] Traceback: {traceback.format_exc()}")
                                    # Record the error and don't fall back to old API
                                    mapping[feat_id] = f"error:simple_chamfer_failed:2 : {error_msg}"
                                    continue  # Skip this feature and move to next
                            
                            # If we get here, defn should be set from the angle-based method above
                            if defn:
                                # Add the chamfer
                                ch = chf.add(defn)
                                mapping[feat_id] = f"fusion:chamfer:{ch.entityToken}"
                                print(f"[DEBUG] Angle-based chamfer created: {ch.entityToken}")
                                
                                # Record lineage and continue to next feature
                                try:
                                    self._record_lineage(feat_id, ch, root)
                                except Exception:
                                    pass
                                continue
                            
                        except Exception as e:
                            print(f"[DEBUG] Simple chamfer failed: {str(e)}")
                            mapping[feat_id] = f"error:simple_chamfer_failed:{str(e)}"
                            continue
                    
                    # Transitions: support feature-level distance/angle variants across groups
                    if feat.get("transitions") and isinstance(feat.get("transitions"), dict):
                        try:
                            trans = feat.get("transitions")
                            d1 = self._parse_length_mm(trans.get("d") or trans.get("distance"))
                            d2 = self._parse_length_mm(trans.get("d2") or trans.get("distance2")) if trans.get("d2") or trans.get("distance2") else None
                            ang_deg = None
                            if trans.get("angle") is not None:
                                try:
                                    ang_deg = float(self._parse_length_mm(str(trans.get("angle"))) or 0.0)
                                except Exception:
                                    ang_deg = None
                            if (d1 is not None or d2 is not None or ang_deg is not None):
                                chf = root.features.chamferFeatures
                                # Apply on all edges when no per-groups present
                                def _apply_feature_def(edge_set):
                                    try:
                                        if d2 is not None and hasattr(chf, "createTwoDistancesChamferDefinition"):
                                            return chf.createTwoDistancesChamferDefinition(
                                                edge_set,
                                                adsk.core.ValueInput.createByReal((d1 or d_mm) / 10.0),
                                                adsk.core.ValueInput.createByReal((d2 or d_mm) / 10.0),
                                                False,
                                            )
                                        if (ang_deg is not None or ang_deg_global is not None) and hasattr(chf, "createDistanceAndAngleChamferDefinition"):
                                            ang = ang_deg if ang_deg is not None else (ang_deg_global if ang_deg_global is not None else 45.0)
                                            return chf.createDistanceAndAngleChamferDefinition(
                                                edge_set,
                                                adsk.core.ValueInput.createByReal((d1 or d_mm) / 10.0),
                                                adsk.core.ValueInput.createByReal(((ang) / 180.0) * 3.141592653589793),
                                                False,
                                            )
                                        return chf.createEqualDistanceChamferDefinition(edge_set, adsk.core.ValueInput.createByReal((d1 or d_mm) / 10.0), False)
                                    except Exception:
                                        return None
                                # Prefer groups when provided
                                per_groups = feat.get("edges") or []
                                applied_any = False
                                if isinstance(per_groups, list) and len(per_groups) > 0:
                                    for grp in per_groups:
                                        if not isinstance(grp, dict):
                                            continue
                                        grp_edges = None
                                        try:
                                            qg = grp.get("q") or grp.get("edges_query") or grp.get("edges")
                                            if qg:
                                                grp_edges = self._resolve_query(root, qg, entity_type="edge")
                                        except Exception:
                                            grp_edges = None
                                        grp_edges = grp_edges or edge_col
                                        defn = _apply_feature_def(grp_edges)
                                        if defn is not None:
                                            try:
                                                ch = chf.add(defn)
                                                mapping[f"{feat_id}:grp"] = f"fusion:chamfer:{ch.entityToken}"
                                                applied_any = True
                                            except Exception:
                                                pass
                                if not applied_any:
                                    defn = _apply_feature_def(edge_col)
                                    if defn is not None:
                                        try:
                                            ch = chf.add(defn)
                                            mapping[feat_id] = f"fusion:chamfer:{ch.entityToken}"
                                            # Skip default block
                                            continue
                                        except Exception:
                                            pass
                        except Exception:
                            pass
                    if edges.count > 0:
                        print(f"[DEBUG] Entering main chamfer creation block with {edges.count} edges")
                        chf = root.features.chamferFeatures
                        edge_col = adsk.core.ObjectCollection.create()
                        for i in range(edges.count):
                            e = edges.item(i)
                            edge_col.add(e)
                        print(f"[DEBUG] Created edge collection with {edge_col.count} edges")
                        # If groups provided, create separate chamfers per group
                        try:
                            per_groups = feat.get("edges") or []
                            if isinstance(per_groups, list) and len(per_groups) > 0:
                                # Attempt variable chamfer per group if definition exists
                                used_variable = False
                                for grp in per_groups:
                                    if not isinstance(grp, dict):
                                        continue
                                    if grp.get("points"):
                                        try:
                                            var_ch = self._apply_variable_chamfer(root, chf, grp)
                                            if var_ch:
                                                mapping[f"{feat_id}:var"] = f"fusion:chamfer:{var_ch.entityToken}"
                                                used_variable = True
                                            continue
                                        except Exception:
                                            pass
                                if used_variable:
                                    continue
                                for grp in per_groups:
                                    if not isinstance(grp, dict):
                                        continue
                                    # Choose definition: two distances, distance+angle, or equal distance
                                    d1_mm = self._parse_length_mm(grp.get("d") or grp.get("distance")) or d_mm
                                    d2_mm = self._parse_length_mm(grp.get("d2") or grp.get("distance2")) if grp.get("d2") or grp.get("distance2") else None
                                    g_angle_deg = None
                                    if grp.get("angle") is not None:
                                        try:
                                            g_angle_deg = float(self._parse_length_mm(str(grp.get("angle"))) or 0.0)
                                        except Exception:
                                            g_angle_deg = None
                                    grp_edges = None
                                    try:
                                        qg = grp.get("q") or grp.get("edges_query") or grp.get("edges")
                                        if qg:
                                            grp_edges = self._resolve_query(root, qg, entity_type="edge")
                                    except Exception:
                                        grp_edges = None
                                    grp_edges = grp_edges or edge_col
                                    defn = None
                                    try:
                                        if d2_mm is not None and hasattr(chf, "createTwoDistancesChamferDefinition"):
                                            defn = chf.createTwoDistancesChamferDefinition(
                                                grp_edges,
                                                adsk.core.ValueInput.createByReal((d1_mm/10.0)),
                                                adsk.core.ValueInput.createByReal((d2_mm/10.0)),
                                                False,
                                            )
                                        elif (g_angle_deg is not None or ang_deg_global is not None) and hasattr(chf, "createDistanceAndAngleChamferDefinition"):
                                            ang = g_angle_deg if g_angle_deg is not None else ang_deg_global
                                            defn = chf.createDistanceAndAngleChamferDefinition(
                                                grp_edges,
                                                adsk.core.ValueInput.createByReal((d1_mm/10.0)),
                                                adsk.core.ValueInput.createByReal(((ang or 45.0) / 180.0) * 3.141592653589793),
                                                False,
                                            )
                                    except Exception:
                                        defn = None
                                    if defn is None:
                                        defn = chf.createEqualDistanceChamferDefinition(grp_edges, adsk.core.ValueInput.createByReal((d1_mm/10.0)), False)
                                    ch = chf.add(defn)
                                    mapping[f"{feat_id}:grp"] = f"fusion:chamfer:{ch.entityToken}"
                                continue
                        except Exception:
                            pass
                        # Global definition selection (angle or equal distance)
                        defn = None
                        try:
                            if ang_deg_global is not None and hasattr(chf, "createDistanceAndAngleChamferDefinition"):
                                defn = chf.createDistanceAndAngleChamferDefinition(
                                    edge_col,
                                    adsk.core.ValueInput.createByReal(d_cm),
                                    adsk.core.ValueInput.createByReal((ang_deg_global / 180.0) * 3.141592653589793),
                                    False,
                                )
                        except Exception:
                            defn = None
                        if defn is None:
                            print(f"[DEBUG] Creating equal distance chamfer definition with {d_cm}cm")
                            try:
                                # Create the chamfer input
                                chamfer_input = chf.createInput(edge_col, False)  # False for isTangentChain
                                # Use the correct API method!
                                chamfer_input.setToEqualDistance(adsk.core.ValueInput.createByReal(d_cm))
                                defn = chamfer_input
                            except Exception as ex:
                                print(f"[DEBUG] Main chamfer creation error: {str(ex)}")
                                # Fallback - try without distance
                                chamfer_input = chf.createInput(edge_col, False)
                                defn = chamfer_input
                        try:
                            print(f"[DEBUG] Adding chamfer to feature collection...")
                            ch = chf.add(defn)
                            print(f"[DEBUG] Chamfer created successfully: {ch.entityToken}")
                            mapping[feat_id] = f"fusion:chamfer:{ch.entityToken}"
                        except Exception as e:
                            print(f"[DEBUG] Chamfer creation failed: {str(e)}")
                            mapping[feat_id] = f"error:chamfer_failed:{str(e)}"
                        try:
                            self._record_lineage(feat_id, ch, root)
                        except Exception:
                            pass
                elif kind == "thin_extrude":
                    try:
                        prof = self._first_profile(root)
                        if prof is None:
                            mapping[feat_id] = "fusion:thin_extrude:E2305"
                        else:
                            ext_feats = root.features.extrudeFeatures
                            op = self._feature_operation(feat.get("operation") or feat.get("op"))
                            ext_input = ext_feats.createInput(prof, op)
                            # Extent: distance (default) or to-face/through-all if exposed
                            dist_mm = self._parse_length_mm(feat.get("distance") or feat.get("depth") or feat.get("thickness") or "10") or 10.0
                            dist_cm = dist_mm / 10.0
                            try:
                                # To-face extent if requested
                                to_face = None
                                if feat.get("to_face_query"):
                                    try:
                                        fc = self._resolve_query(root, feat.get("to_face_query"), entity_type="face")
                                        if fc and fc.count > 0:
                                            to_face = fc.item(0)
                                    except Exception:
                                        to_face = None
                                if to_face is not None and hasattr(ext_input, "setToExtent"):
                                    ext_input.setToExtent(to_face)
                                else:
                                    # Through all extent
                                    if str(feat.get("through_all") or "").lower() in ("1", "true", "yes") and hasattr(ext_input, "setAllExtent"):
                                        ext_input.setAllExtent(False)
                                    else:
                                        ext_input.setDistanceExtent(False, adsk.core.ValueInput.createByReal(dist_cm))
                            except Exception:
                                ext_input.setDistanceExtent(False, adsk.core.ValueInput.createByReal(dist_cm))
                            # Thin wall parameters
                            wall_mm = self._parse_length_mm(feat.get("wall") or feat.get("wall_thickness") or "2") or 2.0
                            wall_cm = wall_mm / 10.0
                            side = (feat.get("side") or feat.get("wall_side") or "center").lower()
                            wall2_mm = self._parse_length_mm(feat.get("wall2") or feat.get("wall_thickness2"))
                            wall2_cm = None if wall2_mm is None else (wall2_mm / 10.0)
                            try:
                                # Newer API supports setThinExtrude
                                ext_input.isThinFeature = True
                                ext_input.thickness = adsk.core.ValueInput.createByReal(wall_cm)
                                if hasattr(ext_input, "thinDirection"):
                                    # 0: center, 1: oneSide, 2: twoSides (example mapping)
                                    if side in ("center", "symmetric", "centre"):
                                        ext_input.thinDirection = 0
                                    elif side in ("outward", "outside", "one_side_out", "one_side"):
                                        ext_input.thinDirection = 1
                                    else:
                                        ext_input.thinDirection = 2
                                # If API supports separate second thickness
                                for attr in ("thickness2", "secondThickness"):
                                    if wall2_cm is not None and hasattr(ext_input, attr):
                                        try:
                                            setattr(ext_input, attr, adsk.core.ValueInput.createByReal(wall2_cm))
                                        except Exception:
                                            pass
                            except Exception:
                                # Fallbacks for older APIs: try surface extrude + thicken or non-solid with thickness
                                try:
                                    # Try non-solid thin extrude if supported
                                    if hasattr(ext_input, "isSolid"):
                                        ext_input.isSolid = False
                                        if hasattr(ext_input, "thickness"):
                                            ext_input.thickness = adsk.core.ValueInput.createByReal(wall_cm)
                                except Exception:
                                    pass
                            ext = ext_feats.add(ext_input)
                            # If still not a thin solid and a thicken feature exists, try to thicken
                            try:
                                if str(feat.get("ensure_solid") or "").lower() in ("1", "true", "yes"):
                                    bodies = self._all_bodies(root)
                                    last = bodies.item(bodies.count - 1) if bodies.count > 0 else None
                                    if last and getattr(last, "isSolid", True) is False:
                                        thick = root.features.thickenFeatures if hasattr(root.features, "thickenFeatures") else None
                                        if thick:
                                            ti = thick.createInput(last.faces, adsk.core.ValueInput.createByReal(wall_cm), True)
                                            tf = thick.add(ti)
                                            mapping[f"{feat_id}:thicken"] = f"fusion:thicken:{tf.entityToken}"
                            except Exception:
                                pass
                            mapping[feat_id] = f"fusion:thin_extrude:{ext.entityToken}"
                            try:
                                self._record_lineage(feat_id, ext, root)
                            except Exception:
                                pass
                    except Exception:
                        mapping[feat_id] = "fusion:thin_extrude:E2305"
                elif kind == "rib":
                    try:
                        ribs = root.features.ribFeatures
                        # Build path: prefer a sketch chain name or edges query
                        path = None
                        try:
                            if isinstance(feat.get("path_sketch"), str):
                                for sk in root.sketches:
                                    if getattr(sk, "name", "") == feat.get("path_sketch") and sk.sketchCurves.count > 0:
                                        path = sk.sketchCurves
                                        break
                            if path is None and feat.get("edges_query"):
                                path = self._resolve_query(root, feat.get("edges_query"), entity_type="edge")
                        except Exception:
                            path = None
                        if path is None:
                            mapping[feat_id] = "fusion:rib:E2306"
                        else:
                            th_mm = self._parse_length_mm(feat.get("thickness") or "3") or 3.0
                            th_cm = th_mm / 10.0
                            draft_deg = self._parse_length_mm(str(feat.get("draft") or "0")) or 0.0
                            rib_in = ribs.createInput(path, adsk.core.ValueInput.createByReal(th_cm), adsk.core.ValueInput.createByReal((draft_deg/180.0)*3.141592653589793))
                            rib = ribs.add(rib_in)
                            mapping[feat_id] = f"fusion:rib:{rib.entityToken}"
                            try:
                                self._record_lineage(feat_id, rib, root)
                            except Exception:
                                pass
                    except Exception:
                        mapping[feat_id] = "fusion:rib:E2306"
                elif kind in ("wrap", "emboss", "project"):
                    try:
                        import adsk.core  # type: ignore
                        import adsk.fusion  # type: ignore
                        emb = getattr(root.features, "embossFeatures", None)
                        if not emb:
                            self._diag("E2311", where=kind, message="Emboss/Wrap not available in this Fusion version")
                        else:
                            src_sk = None
                            # Accept alias for sketch name
                            sk_name = feat.get("sketch") or feat.get("source_sketch")
                            if isinstance(sk_name, str):
                                for sk in root.sketches:
                                    if getattr(sk, "name", "") == sk_name:
                                        src_sk = sk
                                        break
                            # Inline text → create temp sketch with text content
                            if src_sk is None and isinstance(feat.get("text"), str):
                                try:
                                    txt_str = str(feat.get("text"))
                                    txt_h_mm = self._parse_length_mm(feat.get("text_height") or "5 mm") or 5.0
                                    sk_tmp = root.sketches.add(root.xYConstructionPlane)
                                    pos = adsk.core.Point3D.create(0, 0, 0)
                                    height_cm = adsk.core.ValueInput.createByReal(txt_h_mm / 10.0)
                                    try:
                                        ti = sk_tmp.sketchTexts.createInput(txt_str, height_cm)
                                        ti.setAsMultiLine(pos, 0.0, adsk.core.HorizontalAlignments.LeftHorizontalAlignment, adsk.core.VerticalAlignments.TopVerticalAlignment, 0.0)
                                        sk_tmp.sketchTexts.add(ti)
                                    except Exception:
                                        sk_tmp.sketchTexts.add(txt_str, pos, height_cm)
                                    src_sk = sk_tmp
                                except Exception:
                                    pass
                            if src_sk is None and root.sketches.count > 0:
                                src_sk = root.sketches.item(0)
                            # Allow 'onto' alias for target
                            tgt_faces = self._resolve_query(root, feat.get("on") or feat.get("onto") or {"kind": "face"}, entity_type="face")
                            if not tgt_faces or tgt_faces.count == 0:
                                self._diag("E2312", where=kind, message="Missing source sketch or target faces for emboss/wrap.")
                            else:
                                # Map parameters
                                depth_mm = self._parse_length_mm(feat.get("depth") or ("0.0" if kind == "project" else "1.0")) or (0.0 if kind == "project" else 1.0)
                                angle_deg = None
                                if feat.get("draft") is not None:
                                    try:
                                        angle_deg = float(self._parse_length_mm(str(feat.get("draft"))) or 0.0)
                                    except Exception:
                                        angle_deg = None
                                depth = adsk.core.ValueInput.createByReal(depth_mm / 10.0)
                                draft = adsk.core.ValueInput.createByReal(((angle_deg or 0.0) / 180.0) * 3.141592653589793)
                                method = str(feat.get("method") or ("wrap" if kind == "wrap" else ("project" if kind == "project" else "emboss"))).lower()
                                is_wrap = (method == "wrap")
                                is_project = (method == "project") or (kind == "project") or (depth_mm == 0.0)
                                reverse_dir = bool(feat.get("reverse") or feat.get("reverse_direction"))
                                geodesic = (method == "geodesic")
                                project_dir = None
                                try:
                                    if feat.get("direction"):
                                        v = self._parse_point(str(feat.get("direction")))
                                        if v:
                                            project_dir = adsk.core.Vector3D.create(float(v[0]), float(v[1]), float((v[2] if len(v) > 2 else 1.0)))
                                except Exception:
                                    project_dir = None
                                ein = None
                                # Attempt multiple API signatures
                                for api_variant in ("createInput", "createEmbossFeatureInput", "createWrapFeatureInput"):
                                    try:
                                        if hasattr(emb, api_variant):
                                            if api_variant == "createInput":
                                                # (sketch, faces, isWrap?, depth, angle?)
                                                try:
                                                    ein = emb.createInput(src_sk, tgt_faces, is_wrap)
                                                    try:
                                                        if hasattr(ein, "depth"):
                                                            ein.depth = depth
                                                        if hasattr(ein, "draftAngle") and angle_deg is not None:
                                                            ein.draftAngle = draft
                                                        if project_dir and hasattr(ein, "direction"):
                                                            ein.direction = project_dir
                                                        if hasattr(ein, "isWrap"):
                                                            ein.isWrap = is_wrap
                                                        if hasattr(ein, "isProject"):
                                                            ein.isProject = is_project
                                                        if hasattr(ein, "isDirectionFlipped") and reverse_dir:
                                                            ein.isDirectionFlipped = True
                                                    except Exception:
                                                        pass
                                                except Exception:
                                                    ein = None
                                            else:
                                                try:
                                                    # Prefer depth/angle overload if available
                                                    ein = getattr(emb, api_variant)(src_sk, tgt_faces, depth, is_wrap)
                                                    try:
                                                        if angle_deg is not None and hasattr(ein, "draftAngle"):
                                                            ein.draftAngle = draft
                                                        if project_dir and hasattr(ein, "direction"):
                                                            ein.direction = project_dir
                                                        if hasattr(ein, "isProject"):
                                                            ein.isProject = is_project
                                                        if hasattr(ein, "isDirectionFlipped") and reverse_dir:
                                                            ein.isDirectionFlipped = True
                                                        if hasattr(ein, "isWrap"):
                                                            ein.isWrap = is_wrap
                                                    except Exception:
                                                        pass
                                                except Exception:
                                                    try:
                                                        ein = getattr(emb, api_variant)(src_sk, tgt_faces, is_wrap)
                                                    except Exception:
                                                        ein = None
                                    except Exception:
                                        ein = None
                                    if ein is not None:
                                        break
                                if ein is None:
                                    self._diag("E2313", where=kind, message="Emboss/Wrap API call failed on this Fusion version.")
                                else:
                                    try:
                                        ef = emb.add(ein)
                                        mapping[feat_id] = f"fusion:{kind}:{ef.entityToken}"
                                        try:
                                            self._record_lineage(feat_id, ef, root)
                                        except Exception:
                                            pass
                                        if geodesic:
                                            try:
                                                self._diag("E2314", where=kind, message="Geodesic mode requested; applied best-effort if supported.")
                                            except Exception:
                                                pass
                                    except Exception:
                                        self._diag("E2313", where=kind, message="Emboss/Wrap add failed.")
                    except Exception:
                        self._diag("E2311", where=kind, message="Emboss/Wrap not available in this environment")
                elif kind == "hole":
                    try:
                        hole_feats = root.features.holeFeatures
                        h_type = (feat.get("type") or "simple").lower()
                        d_mm = self._parse_length_mm(feat.get("d") or feat.get("diameter")) or 5.0
                        d_cm = d_mm / 10.0
                        dia = adsk.core.ValueInput.createByReal(d_cm)
                        # Position using a sketch, prefer face query if provided
                        face = None
                        try:
                            fq = feat.get("face_query") or feat.get("faces_query")
                            if fq:
                                fcol = self._resolve_query(root, fq, entity_type="face")
                                face = fcol.item(0) if fcol and fcol.count > 0 else None
                        except Exception:
                            face = None
                        # Allow placement by body centroid when body_query supplied
                        if face is None:
                            try:
                                bq = feat.get("body_query")
                                if bq:
                                    bcol = self._resolve_query(root, bq, entity_type="body")
                                    if bcol and bcol.count > 0:
                                        b = bcol.item(0)
                                        # Create a temporary sketch on XY and project centroid (best-effort)
                                        face = root.xYConstructionPlane
                                        cx, cy = 0.0, 0.0
                            except Exception:
                                pass
                        if face is None:
                            # Allow plane selection by name when no face query provided
                            try:
                                plane_key = (feat.get("plane") or "").lower()
                                if plane_key:
                                    if "xz" in plane_key:
                                        face = root.xZConstructionPlane
                                    elif "yz" in plane_key:
                                        face = root.yZConstructionPlane
                                    else:
                                        face = root.xYConstructionPlane
                            except Exception:
                                face = None
                        face = face or self._first_planar_face(root)
                        if face is None:
                            mapping[feat_id] = "fusion:hole:skipped"
                        else:
                            sk = root.sketches.add(face)
                            pts = adsk.core.ObjectCollection.create()
                            
                            # Handle single position or multiple points
                            positions = feat.get("points", [])
                            if not positions and feat.get("position"):
                                positions = [feat.get("position")]
                            
                            for pt in positions:
                                p = self._parse_point(pt)  # Now handles both lists and strings
                                if p and len(p) >= 2:
                                    # Convert mm to cm
                                    sp = sk.sketchPoints.add(adsk.core.Point3D.create(p[0]/10.0, p[1]/10.0, 0))
                                    pts.add(sp)
                            
                            if pts.count == 0:
                                sp = sk.sketchPoints.add(adsk.core.Point3D.create(0, 0, 0))
                                pts.add(sp)
                            if h_type == "counterbore":
                                cb_d_mm = self._parse_length_mm(feat.get("cb_d") or feat.get("counterbore_d")) or (d_mm * 2)
                                cb_depth_mm = self._parse_length_mm(feat.get("cb_depth") or feat.get("counterbore_depth")) or (d_mm)
                                cb_d = adsk.core.ValueInput.createByReal(cb_d_mm / 10.0)
                                cb_depth = adsk.core.ValueInput.createByReal(cb_depth_mm / 10.0)
                                try:
                                    h_input = hole_feats.createCounterboreInput(dia, cb_d, cb_depth)
                                except Exception:
                                    h_input = hole_feats.createSimpleInput(dia)
                            elif h_type == "countersink":
                                cs_d_mm = self._parse_length_mm(feat.get("cs_d") or feat.get("countersink_d")) or (d_mm * 2)
                                cs_angle_deg = self._parse_length_mm(str(feat.get("cs_angle") or feat.get("countersink_angle") or "90")) or 90.0
                                cs_d = adsk.core.ValueInput.createByReal(cs_d_mm / 10.0)
                                cs_ang = adsk.core.ValueInput.createByReal((cs_angle_deg / 180.0) * 3.141592653589793)
                                try:
                                    h_input = hole_feats.createCountersinkInput(dia, cs_d, cs_ang)
                                except Exception:
                                    h_input = hole_feats.createSimpleInput(dia)
                            elif h_type == "taper":
                                taper_deg = self._parse_length_mm(str(feat.get("taper") or feat.get("taper_angle") or "3")) or 3.0
                                depth_mm = self._parse_length_mm(feat.get("depth")) or (d_mm * 2)
                                h_input = hole_feats.createSimpleInput(dia)
                                try:
                                    h_input.taperAngle = adsk.core.ValueInput.createByReal((taper_deg / 180.0) * 3.141592653589793)
                                except Exception:
                                    pass
                            else:
                                h_input = hole_feats.createSimpleInput(dia)
                            drill_angle_deg = self._parse_length_mm(str(feat.get("drill_angle") or feat.get("drillAngle") or "118"))
                            if drill_angle_deg is not None:
                                try:
                                    h_input.holeTipAngle = adsk.core.ValueInput.createByReal((drill_angle_deg / 180.0) * 3.141592653589793)
                                except Exception:
                                    pass
                            # Depth/extent handling: depth distance or through_all
                            depth_spec = feat.get("depth")
                            through_all = bool(feat.get("through_all") or (isinstance(depth_spec, str) and str(depth_spec).lower() == "through_all"))
                            if through_all:
                                for attr in ("isAllExtent", "isThroughAll"):
                                    if hasattr(h_input, attr):
                                        try:
                                            setattr(h_input, attr, True)
                                            break
                                        except Exception:
                                            continue
                            else:
                                depth_mm2 = self._parse_length_mm(depth_spec) if depth_spec is not None else None
                                if depth_mm2 is not None:
                                    val = adsk.core.ValueInput.createByReal((depth_mm2 / 10.0))
                                    applied = False
                                    # Try common properties/methods across versions
                                    for attr in ("extentDistance", "distance", "holeDepth"):
                                        if hasattr(h_input, attr):
                                            try:
                                                setattr(h_input, attr, val)
                                                applied = True
                                                break
                                            except Exception:
                                                continue
                                    if not applied:
                                        for meth in ("setDistanceExtent",):
                                            if hasattr(h_input, meth):
                                                try:
                                                    getattr(h_input, meth)(val)
                                                    applied = True
                                                    break
                                                except Exception:
                                                    continue
                            h_input.setPositionBySketchPoints(pts)
                            h = hole_feats.add(h_input)
                            mapping[feat_id] = f"fusion:hole:{h.entityToken}:{h_type}"
                            # Optional callout text (best-effort diagnostic)
                            if isinstance(feat.get("callout"), str):
                                try:
                                    self._diag("E2300I", where="hole", message=f"Callout: {feat.get('callout')}")
                                except Exception:
                                    pass
                            try:
                                self._record_lineage(feat_id, h, root)
                            except Exception:
                                pass
                    except Exception:
                        mapping[feat_id] = "fusion:hole:E2301"
                        try:
                            self._diag("E2301", where="hole", message="Failed to create hole feature", data={"id": feat_id})
                        except Exception:
                            pass
                elif kind == "revolve":
                    # Resolve profile similar to extrude
                    profile = None
                    profile_spec = feat.get("profile")
                    
                    if profile_spec and isinstance(profile_spec, str):
                        if profile_spec in entity_to_sketch:
                            target_sketch = entity_to_sketch[profile_spec]
                            if target_sketch.profiles.count > 0:
                                profile = target_sketch.profiles.item(0)
                        elif profile_spec in sketch_map:
                            target_sketch = sketch_map[profile_spec]
                            if target_sketch.profiles.count > 0:
                                profile = target_sketch.profiles.item(0)
                    
                    if profile is None:
                        profile = self._first_profile(root)
                    
                    if profile is None:
                        mapping[feat_id] = f"error:no_profile_for_revolve"
                        continue
                    
                    # Get axis
                    axis_spec = feat.get("axis", "z").lower()
                    if axis_spec == "x":
                        axis = root.xConstructionAxis
                    elif axis_spec == "y":
                        axis = root.yConstructionAxis
                    else:
                        axis = root.zConstructionAxis
                    
                    # Get angle
                    angle_deg = feat.get("angle", 360)
                    angle_rad = (angle_deg * 3.141592653589793) / 180.0
                    
                    try:
                        rev_feats = root.features.revolveFeatures
                        angle_input = adsk.core.ValueInput.createByReal(angle_rad)
                        rev_input = rev_feats.createInput(profile, axis, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
                        rev_input.setAngleExtent(False, angle_input)
                        rev = rev_feats.add(rev_input)
                        mapping[feat_id] = f"fusion:revolve:{rev.entityToken}"
                    except Exception as e:
                        mapping[feat_id] = f"error:revolve_failed:{str(e)}"
                    try:
                        self._record_lineage(feat_id, rev, root)
                    except Exception:
                        pass
                elif kind == "sweep":
                    # Sweep profile along path with orientation/rail/twist/scale best-effort
                    # Resolve profile
                    prof = None
                    try:
                        pq = feat.get("profile_query") or feat.get("profile")
                        if pq:
                            pcol = self._resolve_query(root, pq, entity_type="profile")
                            if pcol and pcol.count > 0:
                                prof = pcol.item(0)
                    except Exception:
                        prof = None
                    prof = prof or self._first_profile(root)
                    # Resolve path
                    path = None
                    try:
                        path_q = feat.get("path_query") or feat.get("path")
                        if path_q:
                            pcol2 = self._resolve_query(root, path_q, entity_type="edge")
                            if pcol2 and pcol2.count > 0:
                                path = pcol2.item(0)
                    except Exception:
                        path = None
                    path = path or self._first_path(root)
                    if prof and path:
                        sw = root.features.sweepFeatures
                        sw_input = sw.createInput(prof, path, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
                        # Orientation: frenet|fixed_normal|binormal
                        try:
                            orient = (feat.get("orientation") or "frenet").lower()
                            if hasattr(sw_input, "orientation"):
                                if orient in ("fixed_normal", "path"):
                                    sw_input.orientation = adsk.fusion.SweepOrientationTypes.PathOrientationType
                                elif orient in ("binormal", "guide", "guide_rail"):
                                    sw_input.orientation = adsk.fusion.SweepOrientationTypes.GuideRailOrientationType
                                else:
                                    sw_input.orientation = adsk.fusion.SweepOrientationTypes.PerpendicularOrientationType
                        except Exception:
                            pass
                        # Optional guide rail via query
                        try:
                            if feat.get("guide_query"):
                                gcol = self._resolve_query(root, feat.get("guide_query"), entity_type="edge")
                                if gcol and hasattr(sw_input, "guideRail") and gcol.count > 0:
                                    sw_input.guideRail = gcol.item(0)
                        except Exception:
                            pass
                        # Optional twist angle (deg)
                        try:
                            tw_deg = None
                            if feat.get("twist") is not None:
                                tw_deg = float(self._parse_length_mm(str(feat.get("twist"))) or 0.0)
                            if tw_deg is not None and hasattr(sw_input, "twistAngle"):
                                sw_input.twistAngle = adsk.core.ValueInput.createByReal((tw_deg / 180.0) * 3.141592653589793)
                        except Exception:
                            pass
                        # Optional profile scaling
                        try:
                            scale = None
                            if feat.get("scale") is not None:
                                scale = float(self._parse_length_mm(str(feat.get("scale"))) or 1.0)
                            if scale is not None:
                                for attr in ("profileScaling", "scale"):
                                    if hasattr(sw_input, attr):
                                        try:
                                            setattr(sw_input, attr, scale)
                                            break
                                        except Exception:
                                            pass
                        except Exception:
                            pass
                        # Solid/operation override
                        try:
                            if hasattr(sw_input, "isSolid") and feat.get("is_solid") is not None:
                                sw_input.isSolid = bool(feat.get("is_solid"))
                        except Exception:
                            pass
                        sw_feat = sw.add(sw_input)
                        mapping[feat_id] = f"fusion:sweep:{sw_feat.entityToken}"
                        try:
                            self._record_lineage(feat_id, sw_feat, root)
                        except Exception:
                            pass
                elif kind == "loft":
                    # Loft across available profiles in sketches (first 2)
                    profiles = self._collect_profiles(root, max_count=3)
                    if len(profiles) >= 2:
                        lf = root.features.loftFeatures
                        sections = adsk.core.ObjectCollection.create()
                        for p in profiles:
                            sections.add(p)
                        lf_input = lf.createInput(adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
                        for i in range(sections.count):
                            lf_input.loftSections.add(sections.item(i))
                        # Continuity and orientation enforcement (no fallback)
                        try:
                            cont = (feat.get("continuity") or "").upper()
                            if cont in ("G1", "G2"):
                                # Attempt to set continuity if API provides a mechanism; otherwise, hard fail with diagnostic
                                applied = False
                                try:
                                    import adsk.fusion  # type: ignore
                                    enum_val = None
                                    for tname in ("SurfaceContinuityTypes", "ContinuityTypes", "LoftSectionContinuityTypes"):
                                        enum_t = getattr(adsk.fusion, tname, None)
                                        if not enum_t:
                                            continue
                                        candidates = [n for n in dir(enum_t) if not n.startswith("_")]
                                        pick = None
                                        if cont == "G1":
                                            for n in candidates:
                                                if "G1" in n or "Tangent" in n:
                                                    pick = n
                                                    break
                                        elif cont == "G2":
                                            for n in candidates:
                                                if "G2" in n or "Curvature" in n:
                                                    pick = n
                                                    break
                                        if pick and hasattr(enum_t, pick):
                                            enum_val = getattr(enum_t, pick)
                                            break
                                    for attr in ("sectionContinuity", "continuity", "edgeContinuity"):
                                        if hasattr(lf_input, attr) and enum_val is not None:
                                            try:
                                                setattr(lf_input, attr, enum_val)
                                                applied = True
                                                break
                                            except Exception:
                                                continue
                                except Exception:
                                    applied = False
                                if not applied:
                                    self._diag("E2315", where="loft", message=f"Requested continuity {cont} not supported by this Fusion version.")
                                    mapping[feat_id] = f"fusion:loft:E2315"
                                    continue
                            # Optional per-section continuity array: sections_continuity: ["G1","G2",...]
                            try:
                                sec_cont = feat.get("sections_continuity") or []
                                if isinstance(sec_cont, list) and len(sec_cont) == sections.count:
                                    try:
                                        import adsk.fusion  # type: ignore
                                        for i, c in enumerate(sec_cont):
                                            cc = (str(c) or "").upper()
                                            if cc not in ("G0", "G1", "G2"):
                                                continue
                                            enum_val = None
                                            for tname in ("SurfaceContinuityTypes", "ContinuityTypes", "LoftSectionContinuityTypes"):
                                                enum_t = getattr(adsk.fusion, tname, None)
                                                if not enum_t:
                                                    continue
                                                candidates = [n for n in dir(enum_t) if not n.startswith("_")]
                                                pick = None
                                                if cc == "G1":
                                                    for n in candidates:
                                                        if "G1" in n or "Tangent" in n:
                                                            pick = n
                                                            break
                                                elif cc == "G2":
                                                    for n in candidates:
                                                        if "G2" in n or "Curvature" in n:
                                                            pick = n
                                                            break
                                                else:
                                                    for n in candidates:
                                                        if "G0" in n or "Position" in n or n == "None":
                                                            pick = n
                                                            break
                                                if pick and hasattr(enum_t, pick):
                                                    enum_val = getattr(enum_t, pick)
                                                    break
                                            if hasattr(lf_input, "setSectionContinuity") and enum_val is not None:
                                                try:
                                                    lf_input.setSectionContinuity(i, enum_val)
                                                except Exception:
                                                    pass
                                    except Exception:
                                        pass
                            except Exception:
                                pass
                            orient = (feat.get("orientation") or "").lower()
                            if orient:
                                # If orientation control is not supported on loft, hard fail when explicitly requested
                                supported = False
                                try:
                                    import adsk.fusion  # type: ignore
                                    enum_val = None
                                    for tname in ("LoftOrientationTypes", "ProfileOrientationTypes", "SweepOrientationTypes"):
                                        enum_t = getattr(adsk.fusion, tname, None)
                                        if not enum_t:
                                            continue
                                        if orient == "fixed_normal":
                                            pick = "PathOrientationType"
                                        elif orient == "binormal":
                                            pick = "GuideRailOrientationType"
                                        else:
                                            pick = "PerpendicularOrientationType"
                                        if hasattr(enum_t, pick):
                                            enum_val = getattr(enum_t, pick)
                                            break
                                    for attr in ("orientation", "loftOrientation"):
                                        if hasattr(lf_input, attr) and enum_val is not None:
                                            try:
                                                setattr(lf_input, attr, enum_val)
                                                supported = True
                                                break
                                            except Exception:
                                                continue
                                except Exception:
                                    supported = False
                                if not supported:
                                    self._diag("E2316", where="loft", message=f"Requested orientation '{orient}' not supported by this Fusion version.")
                                    mapping[feat_id] = f"fusion:loft:E2316"
                                    continue
                        except Exception:
                            pass
                        # Optional guide rails or centerline from queries/sketch
                        try:
                            guides = feat.get("guides") or feat.get("guides_query") or []
                            if isinstance(guides, list) and len(guides) > 0:
                                rails = adsk.core.ObjectCollection.create()
                                for g in guides:
                                    if isinstance(g, (dict, str)):
                                        try:
                                            gc = self._resolve_query(root, g, entity_type="edge")
                                        except Exception:
                                            gc = None
                                        if gc and gc.count > 0:
                                            rails.add(gc.item(0))
                                if rails.count > 0 and hasattr(lf_input, "centerLineOrRails"):
                                    lf_input.centerLineOrRails = rails
                            # Single rail/centerline via 'rail' or 'centerline' key
                            single = feat.get("rail") or feat.get("centerline") or feat.get("rail_query") or feat.get("centerline_query")
                            if single:
                                try:
                                    scol = self._resolve_query(root, single, entity_type="edge") if isinstance(single, (dict, str)) else None
                                except Exception:
                                    scol = None
                                if scol and scol.count > 0 and hasattr(lf_input, "centerLineOrRails"):
                                    rails = adsk.core.ObjectCollection.create()
                                    rails.add(scol.item(0))
                                    lf_input.centerLineOrRails = rails
                        except Exception:
                            pass
                        loft = lf.add(lf_input)
                        mapping[feat_id] = f"fusion:loft:{loft.entityToken}"
                        try:
                            self._record_lineage(feat_id, loft, root)
                        except Exception:
                            pass
                elif kind == "shell":
                    bodies = self._all_bodies(root)
                    if bodies.count > 0:
                        shell = root.features.shellFeatures
                        faces = bodies.item(bodies.count - 1).faces
                        face_col = adsk.core.ObjectCollection.create()
                        # Faces to remove can be provided via query or default to all (hollow)
                        try:
                            rm = feat.get("remove_faces_query") or feat.get("remove")
                            if rm:
                                rcol = self._resolve_query(root, rm, entity_type="face")
                                if rcol and rcol.count > 0:
                                    face_col = rcol
                        except Exception:
                            pass
                        if face_col.count == 0:
                            for f in faces:
                                face_col.add(f)
                        t_mm = self._parse_length_mm(feat.get("thickness") or feat.get("t") or "2") or 2.0
                        t_cm = t_mm / 10.0
                        s_in = shell.createShellFeatureInput(face_col, adsk.core.ValueInput.createByReal(t_cm))
                        # Inside/outside direction if supported
                        try:
                            if hasattr(s_in, "isInsideThickness") and feat.get("inside") is not None:
                                s_in.isInsideThickness = bool(feat.get("inside"))
                        except Exception:
                            pass
                        s = shell.add(s_in)
                        mapping[feat_id] = f"fusion:shell:{s.entityToken}"
                        try:
                            self._record_lineage(feat_id, s, root)
                        except Exception:
                            pass
                elif kind == "draft":
                    try:
                        draft = root.features.draftFeatures
                        bodies = self._all_bodies(root)
                        if bodies.count > 0:
                            # Resolve target faces
                            face_col = None
                            try:
                                q_spec = feat.get("faces_query") or (feat.get("faces") if isinstance(feat.get("faces"), dict) else None)
                                if q_spec:
                                    face_col = self._resolve_query(root, q_spec, entity_type="face")
                            except Exception:
                                face_col = None
                            if face_col is None:
                                faces = bodies.item(bodies.count - 1).faces
                                face_col = adsk.core.ObjectCollection.create()
                                for f in faces:
                                    face_col.add(f)
                            # Neutral plane selection (by name, query, or face/plane token)
                            neutral = root.xYConstructionPlane
                            n_spec = feat.get("neutral_plane") or feat.get("plane") or "world.xy"
                            try:
                                if isinstance(n_spec, dict):
                                    ncol = self._resolve_query(root, n_spec, entity_type="face")
                                    if ncol and ncol.count > 0:
                                        neutral = ncol.item(0)
                                else:
                                    neutral_key = str(n_spec).lower()
                                    if "xz" in neutral_key:
                                        neutral = root.xZConstructionPlane
                                    elif "yz" in neutral_key:
                                        neutral = root.yZConstructionPlane
                                    else:
                                        neutral = root.xYConstructionPlane
                            except Exception:
                                pass
                            ang_deg = self._parse_length_mm(str(feat.get("angle") or "2")) or 2.0
                            ang_rad = (ang_deg / 180.0) * 3.141592653589793
                            angle = adsk.core.ValueInput.createByReal(ang_rad)
                            # Pull direction: +X/+Y/+Z/-X/-Y/-Z or vector [x,y,z]
                            pull = adsk.fusion.DraftDirectionsType.PullDirectionType
                            try:
                                pd = feat.get("pull_dir") or feat.get("pull_direction")
                                if isinstance(pd, str):
                                    key = pd.strip().lower()
                                    if key in ("+x", "x"):
                                        pull = adsk.fusion.DraftDirectionsType.PullDirectionType
                                    elif key in ("+y", "y"):
                                        pull = adsk.fusion.DraftDirectionsType.PullDirectionType
                                    elif key in ("+z", "z"):
                                        pull = adsk.fusion.DraftDirectionsType.PullDirectionType
                                    elif key.startswith("-"):
                                        pull = adsk.fusion.DraftDirectionsType.PushDirectionType
                                elif isinstance(pd, (list, tuple)) and len(pd) == 3:
                                    # Not all versions support vector pull; record diagnostic if not
                                    try:
                                        _ = [float(pd[0]), float(pd[1]), float(pd[2])]
                                        # Leave as default and emit a diagnostic to indicate best-effort
                                        self._diag("E2302A", where="draft", message="Vector pull_dir not natively supported; using default pull direction.")
                                    except Exception:
                                        pass
                            except Exception:
                                pass
                            # Set faces as fixed (optional) if supported
                            fixed_faces = None
                            try:
                                if feat.get("fixed_faces_query"):
                                    fcol = self._resolve_query(root, feat.get("fixed_faces_query"), entity_type="face")
                                    if fcol and fcol.count > 0:
                                        fixed_faces = fcol
                            except Exception:
                                fixed_faces = None
                            d_in = draft.createInput(face_col, neutral, angle, False, pull)
                            try:
                                if fixed_faces is not None and hasattr(d_in, "setFixedFaces"):
                                    d_in.setFixedFaces(fixed_faces)
                            except Exception:
                                pass
                            d = draft.add(d_in)
                            mapping[feat_id] = f"fusion:draft:{d.entityToken}"
                            try:
                                self._record_lineage(feat_id, d, root)
                            except Exception:
                                pass
                    except Exception:
                        mapping[feat_id] = "fusion:draft:E2302"
                        try:
                            self._diag("E2302", where="draft", message="Failed to create draft feature", data={"id": feat_id})
                        except Exception:
                            pass
                elif kind == "thread":
                    try:
                        thr = root.features.threadFeatures
                        bodies = self._all_bodies(root)
                        target_faces = adsk.core.ObjectCollection.create()
                        # Prefer explicit face query if provided
                        try:
                            fq = feat.get("faces_query") or feat.get("face_query")
                            if fq:
                                fcol = self._resolve_query(root, fq, entity_type="face")
                                if fcol and fcol.count > 0:
                                    for i in range(fcol.count):
                                        target_faces.add(fcol.item(i))
                        except Exception:
                            pass
                        # If not provided, attempt cylindrical_faces(d≈/axis≈) helper
                        if target_faces.count == 0:
                            try:
                                cq = feat.get("cyl_faces_query") or feat.get("cylindrical_faces")
                                if isinstance(cq, dict):
                                    ccol = self._resolve_query(root, {"kind": "face", "cylindrical_faces": True, **cq}, entity_type="face")
                                    if ccol and ccol.count > 0:
                                        for i in range(ccol.count):
                                            target_faces.add(ccol.item(i))
                            except Exception:
                                pass
                        if target_faces.count == 0 and bodies.count > 0:
                            cyl_faces = bodies.item(bodies.count - 1).faces
                            for f in cyl_faces:
                                try:
                                    if getattr(f.geometry, "surfaceType", None) == 1:
                                        target_faces.add(f)
                                except Exception:
                                    pass
                        if target_faces.count > 0:
                            is_modeled = (feat.get("mode") or feat.get("modeled") or "cosmetic").lower() == "modeled"
                            # Prefer query object when exposed; fallback to basic info object
                            t_in = None
                            try:
                                if hasattr(thr, "createThreadInfo"):
                                    t_in = thr.createThreadInfo(False)  # cosmetic default
                            except Exception:
                                t_in = None
                            if t_in is None:
                                try:
                                    t_in = getattr(thr, "createThreadInfoUsingPredefined", None) or getattr(thr, "createThreadInfo", None)
                                    if callable(t_in):
                                        t_in = thr.createThreadInfo(False)
                                except Exception:
                                    t_in = None
                            if t_in is None:
                                mapping[feat_id] = "fusion:thread:E2304"
                                try:
                                    self._diag("E2304", where="thread", message="Thread info creation unavailable in this Fusion version", data={"id": feat_id})
                                except Exception:
                                    pass
                                continue
                            # Map designation/class/handedness/length best-effort
                            try:
                                des = (feat.get("designation") or "").upper()
                                cls = (feat.get("class") or "").upper()
                                hand = (feat.get("hand") or feat.get("handedness") or "right").lower()
                                if hasattr(t_in, "threadDesignation") and des:
                                    t_in.threadDesignation = des
                                if hasattr(t_in, "class") and cls:
                                    setattr(t_in, "class", cls)
                                if hasattr(t_in, "isRightHanded"):
                                    t_in.isRightHanded = (hand != "left")
                                if feat.get("length") is not None and hasattr(t_in, "length"):
                                    try:
                                        ln_mm = self._parse_length_mm(feat.get("length"))
                                        if ln_mm is not None:
                                            t_in.length = adsk.core.ValueInput.createByReal((ln_mm/10.0))
                                    except Exception:
                                        pass
                                # Optional: pitch or size when provided
                                try:
                                    if hasattr(t_in, "diameter") and feat.get("diameter") is not None:
                                        d_mm = self._parse_length_mm(feat.get("diameter"))
                                        if d_mm is not None:
                                            t_in.diameter = adsk.core.ValueInput.createByReal((d_mm/10.0))
                                except Exception:
                                    pass
                            except Exception:
                                pass
                            # Mode: cosmetic/modeled
                            tfeat_in = thr.createInput(target_faces, t_in)
                            tfeat_in.isModeled = is_modeled
                            tfeat = thr.add(tfeat_in)
                            mapping[feat_id] = f"fusion:thread:{tfeat.entityToken}:{'modeled' if is_modeled else 'cosmetic'}"
                            try:
                                self._record_lineage(feat_id, tfeat, root)
                            except Exception:
                                pass
                        else:
                            mapping[feat_id] = "fusion:thread:E2303"
                            try:
                                self._diag("E2303", where="thread", message="No target cylindrical faces found for thread.", data={"id": feat_id})
                            except Exception:
                                pass
                    except Exception:
                        mapping[feat_id] = "fusion:thread:E2304"
                        try:
                            self._diag("E2304", where="thread", message="Failed to create thread feature", data={"id": feat_id})
                        except Exception:
                            pass
                elif kind == "pattern":
                    # Simple linear pattern along +X using last body
                    bodies = self._all_bodies(root)
                    if bodies.count > 0:
                        obj_col = adsk.core.ObjectCollection.create()
                        # Seed selection: allow query; fallback to last body
                        seed_q = feat.get("seed_query") or feat.get("seed")
                        if seed_q:
                            try:
                                # Try bodies first
                                sqc = self._resolve_query(root, seed_q, entity_type="body")
                                if sqc and sqc.count > 0:
                                    for i in range(sqc.count):
                                        obj_col.add(sqc.item(i))
                                else:
                                    # Try faces if bodies not present
                                    fqc = self._resolve_query(root, seed_q, entity_type="face")
                                    if fqc and fqc.count > 0:
                                        for i in range(fqc.count):
                                            obj_col.add(fqc.item(i))
                            except Exception:
                                pass
                        if obj_col.count == 0:
                            obj_col.add(bodies.item(bodies.count - 1))
                        kind_sub = (feat.get("kind") or "linear").lower()
                        if kind_sub == "circular":
                            circ = root.features.circularPatternFeatures
                            # Axis selection: axis (X|Y|Z) or axis_query (edge)
                            axis = root.zConstructionAxis
                            ax_name = (feat.get("axis") or "").upper()
                            if ax_name.startswith("X"):
                                axis = root.xConstructionAxis
                            elif ax_name.startswith("Y"):
                                axis = root.yConstructionAxis
                            # Best-effort: allow axis_query to supply an edge as axis
                            try:
                                if feat.get("axis_query"):
                                    acol = self._resolve_query(root, feat.get("axis_query"), entity_type="edge")
                                    if acol and acol.count > 0:
                                        axis = acol.item(0)
                            except Exception:
                                pass
                            qty = adsk.core.ValueInput.createByString(str(int(feat.get("count") or 6)))
                            # Angle: default 360 deg; support degrees input
                            ang_deg = self._parse_length_mm(str(feat.get("angle") or "360")) or 360.0
                            ang = adsk.core.ValueInput.createByReal((ang_deg / 180.0) * 3.141592653589793)
                            c_in = circ.createInput(obj_col, axis, qty, ang)
                            # Optional: rotate direction and compute options if available
                            try:
                                if hasattr(c_in, "isSymmetric") and feat.get("symmetric") is not None:
                                    c_in.isSymmetric = bool(feat.get("symmetric"))
                            except Exception:
                                pass
                            cp = circ.add(c_in)
                            mapping[feat_id] = f"fusion:pattern_circular:{cp.entityToken}"
                            try:
                                self._record_lineage(feat_id, cp, root)
                            except Exception:
                                pass
                            # Try native per-instance element transforms if provided and supported
                            try:
                                if isinstance(feat.get("instances"), list) and len(feat.get("instances")) > 0:
                                    self._apply_per_instance_pattern(cp, feat.get("instances"))
                            except Exception:
                                pass
                        elif kind_sub == "path":
                            try:
                                ppf = root.features.pathPatternFeatures
                                # Resolve a path from query; fallback to first sketch line/arc
                                path = None
                                if feat.get("path_query"):
                                    path_col = self._resolve_query(root, feat.get("path_query"), entity_type="edge")
                                    if path_col and path_col.count > 0:
                                        path = path_col.item(0)
                                if path is None:
                                    path = self._first_path(root)
                                if path is not None:
                                    count = int(feat.get("count") or 3)
                                    qty = adsk.core.ValueInput.createByString(str(count))
                                    spacing_mm = self._parse_length_mm(feat.get("spacing") or "10") or 10.0
                                    d1 = adsk.core.ValueInput.createByReal(spacing_mm / 10.0)
                                    p_in = ppf.createInput(obj_col, path, qty, d1, False)
                                    # Align to path direction if exposed
                                    try:
                                        if hasattr(p_in, "isAlignToPath") and feat.get("align_to_path") is not None:
                                            p_in.isAlignToPath = bool(feat.get("align_to_path"))
                                    except Exception:
                                        pass
                                    pp = ppf.add(p_in)
                                    mapping[feat_id] = f"fusion:pattern_path:{pp.entityToken}"
                                    try:
                                        self._record_lineage(feat_id, pp, root)
                                    except Exception:
                                        pass
                                    # Try native per-instance transforms if supported
                                    try:
                                        if isinstance(feat.get("instances"), list) and len(feat.get("instances")) > 0:
                                            self._apply_per_instance_pattern(pp, feat.get("instances"))
                                    except Exception:
                                        pass
                                    continue
                            except Exception:
                                pass
                        else:
                            patt = root.features.rectangularPatternFeatures
                            # Direction 1
                            dir1 = root.xConstructionAxis
                            ax1 = (feat.get("dir1") or feat.get("axis1") or "").upper()
                            if ax1.startswith("Y"):
                                dir1 = root.yConstructionAxis
                            elif ax1.startswith("Z"):
                                dir1 = root.zConstructionAxis
                            count1 = int(feat.get("count1") or feat.get("count") or 2)
                            spacing1_mm = self._parse_length_mm(feat.get("spacing1") or feat.get("spacing") or "10") or 10.0
                            mode1 = (feat.get("mode1") or feat.get("distance_type1") or "spacing").lower()
                            # Direction 2 (optional for grid)
                            dir2 = root.yConstructionAxis
                            ax2 = (feat.get("dir2") or feat.get("axis2") or "").upper()
                            if ax2.startswith("X"):
                                dir2 = root.xConstructionAxis
                            elif ax2.startswith("Z"):
                                dir2 = root.zConstructionAxis
                            count2 = int(feat.get("count2") or 1)
                            spacing2_mm = self._parse_length_mm(feat.get("spacing2") or "10") or 10.0
                            mode2 = (feat.get("mode2") or feat.get("distance_type2") or "spacing").lower()
                            # Table-driven fallback with per-instance transforms (also supports 'instances')
                            per_inst = None
                            if isinstance(feat.get("table"), list) and len(feat.get("table")) > 0:
                                per_inst = feat.get("table")
                            elif isinstance(feat.get("instances"), list) and len(feat.get("instances")) > 0:
                                per_inst = feat.get("instances")
                            if per_inst is not None:
                                try:
                                    mv = root.features.moveFeatures
                                    for row in per_inst:
                                        if not isinstance(row, dict):
                                            continue
                                        dx = (self._parse_length_mm(row.get("dx") or "0") or 0.0) / 10.0
                                        dy = (self._parse_length_mm(row.get("dy") or "0") or 0.0) / 10.0
                                        dz = (self._parse_length_mm(row.get("dz") or "0") or 0.0) / 10.0
                                        angle_deg = None
                                        axis = (row.get("axis") or "Z").upper()
                                        try:
                                            angle_deg = float(self._parse_length_mm(str(row.get("angle"))) or 0.0)
                                        except Exception:
                                            angle_deg = None
                                        qty = int(row.get("count") or 1)
                                        for i in range(qty):
                                            trans = adsk.core.Matrix3D.create()
                                            # Rotation first (optional)
                                            if angle_deg is not None and angle_deg != 0.0:
                                                try:
                                                    theta = (angle_deg / 180.0) * 3.141592653589793
                                                    if axis.startswith("X"):
                                                        rot = adsk.core.Matrix3D.create()
                                                        rot.setToRotation(theta, adsk.core.Vector3D.create(1,0,0), adsk.core.Point3D.create(0,0,0))
                                                        trans.transformBy(rot)
                                                    elif axis.startswith("Y"):
                                                        rot = adsk.core.Matrix3D.create()
                                                        rot.setToRotation(theta, adsk.core.Vector3D.create(0,1,0), adsk.core.Point3D.create(0,0,0))
                                                        trans.transformBy(rot)
                                                    else:
                                                        rot = adsk.core.Matrix3D.create()
                                                        rot.setToRotation(theta, adsk.core.Vector3D.create(0,0,1), adsk.core.Point3D.create(0,0,0))
                                                        trans.transformBy(rot)
                                                except Exception:
                                                    pass
                                            # Then translation
                                            try:
                                                vec = adsk.core.Vector3D.create(dx, dy, dz)
                                                trans.translation = vec
                                            except Exception:
                                                pass
                                            input_def = mv.createInput(obj_col, trans)
                                            mv.add(input_def)
                                        mapping[feat_id] = f"fusion:pattern_table:fallback"
                                        continue
                                except Exception:
                                    pass
                            qty1 = adsk.core.ValueInput.createByString(str(count1))
                            dist1 = adsk.core.ValueInput.createByReal((spacing1_mm / 10.0))
                            dist_type1 = adsk.fusion.PatternDistanceType.SpacingPatternDistanceType
                            try:
                                if "extent" in mode1 and hasattr(adsk.fusion.PatternDistanceType, "ExtentPatternDistanceType"):
                                    dist_type1 = adsk.fusion.PatternDistanceType.ExtentPatternDistanceType
                            except Exception:
                                pass
                            input_def = patt.createInput(obj_col, dir1, qty1, dist1, dist_type1)
                            if count2 > 1:
                                qty2 = adsk.core.ValueInput.createByString(str(count2))
                                dist2 = adsk.core.ValueInput.createByReal((spacing2_mm / 10.0))
                                try:
                                    dist_type2 = adsk.fusion.PatternDistanceType.SpacingPatternDistanceType
                                    if "extent" in mode2 and hasattr(adsk.fusion.PatternDistanceType, "ExtentPatternDistanceType"):
                                        dist_type2 = adsk.fusion.PatternDistanceType.ExtentPatternDistanceType
                                    if hasattr(input_def, "setDirectionTwoWithDistanceType"):
                                        input_def.setDirectionTwoWithDistanceType(dir2, qty2, dist2, dist_type2)
                                    else:
                                        input_def.setDirectionTwo(dir2, qty2, dist2)
                                except Exception:
                                    input_def.setDirectionTwo(dir2, qty2, dist2)
                            # Optional symmetry flags
                            try:
                                if hasattr(input_def, "isSymmetricInDirectionOne") and feat.get("symmetric1") is not None:
                                    input_def.isSymmetricInDirectionOne = bool(feat.get("symmetric1"))
                            except Exception:
                                pass
                            try:
                                if hasattr(input_def, "isSymmetricInDirectionTwo") and feat.get("symmetric2") is not None:
                                    input_def.isSymmetricInDirectionTwo = bool(feat.get("symmetric2"))
                            except Exception:
                                pass
                            pat = patt.add(input_def)
                            mapping[feat_id] = f"fusion:pattern_linear:{pat.entityToken}"
                            try:
                                self._record_lineage(feat_id, pat, root)
                            except Exception:
                                pass
                            # Try native per-instance element transforms if provided and supported
                            try:
                                if isinstance(feat.get("instances"), list) and len(feat.get("instances")) > 0:
                                    self._apply_per_instance_pattern(pat, feat.get("instances"))
                            except Exception:
                                pass
                elif kind == "mirror":
                    bodies = self._all_bodies(root)
                    if bodies.count > 0:
                        obj_col = adsk.core.ObjectCollection.create()
                        # Optional target query for bodies/components
                        try:
                            tq = feat.get("target_query") or feat.get("bodies_query")
                            if tq:
                                tcol = self._resolve_query(root, tq, entity_type="body")
                                for i in range(tcol.count):
                                    obj_col.add(tcol.item(i))
                        except Exception:
                            pass
                        if obj_col.count == 0:
                            obj_col.add(bodies.item(bodies.count - 1))
                        mirror = root.features.mirrorFeatures
                        # Plane can come from query or named plane
                        plane = root.yZConstructionPlane
                        try:
                            pq = feat.get("plane_query") or feat.get("plane")
                            if pq:
                                if isinstance(pq, dict):
                                    pcol = self._resolve_query(root, pq, entity_type="face")
                                    if pcol and pcol.count > 0:
                                        plane = pcol.item(0)
                                elif isinstance(pq, str):
                                    pname = pq.lower()
                                    if "xy" in pname:
                                        plane = root.xYConstructionPlane
                                    elif "xz" in pname:
                                        plane = root.xZConstructionPlane
                                    elif "yz" in pname or "zy" in pname:
                                        plane = root.yZConstructionPlane
                        except Exception:
                            pass
                        m_input = mirror.createInput(obj_col, plane)
                        mf = mirror.add(m_input)
                        mapping[feat_id] = f"fusion:mirror:{mf.entityToken}"
                        try:
                            self._record_lineage(feat_id, mf, root)
                        except Exception:
                            pass
                elif kind == "boolean":
                    # Combine last two bodies
                    bodies = self._all_bodies(root)
                    if bodies.count >= 1:
                        # Allow target body query
                        target = None
                        try:
                            t_query = feat.get("target_query") or feat.get("target")
                            if t_query:
                                tcol = self._resolve_query(root, t_query, entity_type="body")
                                target = tcol.item(0) if tcol and tcol.count > 0 else None
                        except Exception:
                            target = None
                        if target is None:
                            target = bodies.item(bodies.count - 1 if bodies.count > 1 else 0)
                        # Tool bodies from query or default to last others
                        tool = bodies.item(bodies.count - 1)
                        combine = root.features.combineFeatures
                        tool_col = adsk.core.ObjectCollection.create()
                        # Allow multi-tool via query
                        tools_q = feat.get("tools_query") or feat.get("tools")
                        if tools_q:
                            try:
                                tq = self._resolve_query(root, tools_q, entity_type="body")
                                for i in range(tq.count):
                                    tool_col.add(tq.item(i))
                            except Exception:
                                pass
                        if tool_col.count == 0:
                            tool_col.add(tool)
                        c_in = combine.createInput(target, tool_col)
                        op = (feat.get("op") or feat.get("operation") or "union").lower()
                        if op == "subtract":
                            c_in.operation = adsk.fusion.FeatureOperations.CutFeatureOperation
                        elif op == "intersect":
                            c_in.operation = adsk.fusion.FeatureOperations.IntersectFeatureOperation
                        else:
                            c_in.operation = adsk.fusion.FeatureOperations.JoinFeatureOperation
                        c_in.isKeepToolBodies = bool(feat.get("keep_tools") or feat.get("keep_tool_bodies") or False)
                        cb = combine.add(c_in)
                        mapping[feat_id] = f"fusion:boolean:{cb.entityToken}"
                        try:
                            self._record_lineage(feat_id, cb, root)
                        except Exception:
                            pass
                elif kind in ("move_face", "offset_face"):
                    # Move/Offset face support (native where possible; offset fallback)
                    bodies = self._all_bodies(root)
                    if bodies.count > 0:
                        # Resolve faces via query if any
                        face_col = None
                        try:
                            q_spec = feat.get("faces_query") or (feat.get("faces") if isinstance(feat.get("faces"), dict) else None)
                            if q_spec:
                                face_col = self._resolve_query(root, q_spec, entity_type="face")
                        except Exception:
                            face_col = None
                        if face_col is None:
                            faces = bodies.item(bodies.count - 1).faces
                            face_col = adsk.core.ObjectCollection.create()
                            for f in faces:
                                face_col.add(f)
                        if kind == "move_face":
                            try:
                                mv = root.features.moveFeatures
                                minput = mv.createInput(face_col)
                                # Translate
                                dx = self._parse_length_mm(feat.get("dx") or "0") or 0.0
                                dy = self._parse_length_mm(feat.get("dy") or "0") or 0.0
                                dz = self._parse_length_mm(feat.get("dz") or "0") or 0.0
                                if abs(dx) > 0 or abs(dy) > 0 or abs(dz) > 0:
                                    vec = adsk.core.Vector3D.create(dx/10.0, dy/10.0, dz/10.0)
                                    try:
                                        minput.defineAsTranslate(vec)
                                    except Exception:
                                        pass
                                # Rotate
                                ang_deg = None
                                if feat.get("angle") is not None:
                                    try:
                                        ang_deg = float(self._parse_length_mm(str(feat.get("angle"))) or 0.0)
                                    except Exception:
                                        ang_deg = None
                                if ang_deg is not None and hasattr(minput, "defineAsRotate"):
                                    axis_name = (feat.get("axis") or "Z").upper()
                                    axis = root.zConstructionAxis
                                    if axis_name.startswith("X"): axis = root.xConstructionAxis
                                    elif axis_name.startswith("Y"): axis = root.yConstructionAxis
                                    try:
                                        minput.defineAsRotate(axis, adsk.core.ValueInput.createByReal((ang_deg/180.0)*3.141592653589793))
                                    except Exception:
                                        pass
                                mf = mv.add(minput)
                                mapping[feat_id] = f"fusion:move_face:{mf.entityToken}"
                                try:
                                    self._record_lineage(feat_id, mf, root)
                                except Exception:
                                    pass
                                continue
                            except Exception:
                                pass
                        # Offset faces (negative offsets allowed)
                        offs = root.features.offsetFacesFeatures
                        off_val_mm = self._parse_length_mm(feat.get("offset") or feat.get("distance") or "0.5") or 0.5
                        off_val = adsk.core.ValueInput.createByReal(off_val_mm / 10.0)
                        of = offs.add(face_col, off_val)
                        mapping[feat_id] = f"fusion:offset_face:{of.entityToken}"
                        try:
                            self._record_lineage(feat_id, of, root)
                        except Exception:
                            pass
                elif kind == "replace_face":
                    # Replace faces with plane or arbitrary face/surface (best-effort)
                    bodies = self._all_bodies(root)
                    if bodies.count > 0:
                        face_col = None
                        try:
                            q_spec = feat.get("faces_query") or (feat.get("faces") if isinstance(feat.get("faces"), dict) else None)
                            if q_spec:
                                face_col = self._resolve_query(root, q_spec, entity_type="face")
                        except Exception:
                            face_col = None
                        if face_col is None:
                            faces = bodies.item(bodies.count - 1).faces
                            face_col = adsk.core.ObjectCollection.create()
                            for f in faces:
                                face_col.add(f)
                        rep = root.features.replaceFaceFeatures
                        surf = root.xYConstructionPlane
                        try:
                            rq = feat.get("replacement_face_query") or feat.get("surface_query")
                            if rq:
                                rcol = self._resolve_query(root, rq, entity_type="face")
                                if rcol and rcol.count > 0:
                                    surf = rcol.item(0)
                        except Exception:
                            pass
                        keep_geom = bool(feat.get("keep_geometry") or False)
                        rf = rep.add(face_col, surf, keep_geom)
                        mapping[feat_id] = f"fusion:replace_face:{rf.entityToken}"
                        try:
                            self._record_lineage(feat_id, rf, root)
                        except Exception:
                            pass
                elif kind == "split":
                    bodies = self._all_bodies(root)
                    if bodies.count > 0:
                        split = root.features.splitBodyFeatures
                        body = bodies.item(bodies.count - 1)
                        tool = root.yZConstructionPlane
                        # Prefer tool from face or sketch profile query
                        try:
                            fq = feat.get("tool_face_query") or feat.get("face_query")
                            if fq:
                                fcol = self._resolve_query(root, fq, entity_type="face")
                                if fcol and fcol.count > 0:
                                    tool = fcol.item(0)
                            elif isinstance(feat.get("tool_sketch"), str):
                                # Use first profile from named sketch if available
                                for sk in root.sketches:
                                    if getattr(sk, "name", "") == feat.get("tool_sketch") and sk.profiles.count > 0:
                                        tool = sk.profiles.item(0)
                                        break
                        except Exception:
                            pass
                        sb_in = split.createInput(body, tool, True)
                        sb = split.add(sb_in)
                        mapping[feat_id] = f"fusion:split:{sb.entityToken}"
                        try:
                            self._record_lineage(feat_id, sb, root)
                        except Exception:
                            pass
                elif kind == "patch":
                    # Surface patch: create a patch from a closed edge loop (best-effort)
                    try:
                        import adsk.core  # type: ignore
                        surf_feats = root.features.patchFeatures
                    except Exception:
                        surf_feats = None
                    if surf_feats:
                        try:
                            loop_q = feat.get("edges_query") or feat.get("loop_query")
                            edges = self._resolve_query(root, loop_q, entity_type="edge") if loop_q else self._all_body_edges(root)
                        except Exception:
                            edges = self._all_body_edges(root)
                        try:
                            pf_in = surf_feats.createInput(edges)
                            # Optional parameters: tangent/merge if exposed
                            try:
                                if bool(feat.get("tangent")) and hasattr(pf_in, "isTangentPropagationEnabled"):
                                    pf_in.isTangentPropagationEnabled = True
                                if hasattr(pf_in, "isMergeEnabled") and feat.get("merge") is not None:
                                    pf_in.isMergeEnabled = bool(feat.get("merge"))
                            except Exception:
                                pass
                            pf = surf_feats.add(pf_in)
                            mapping[feat_id] = f"fusion:patch:{pf.entityToken}"
                            try:
                                self._record_lineage(feat_id, pf, root)
                            except Exception:
                                pass
                        except Exception:
                            mapping[feat_id] = "fusion:patch:E2601"
                elif kind == "extend":
                    # Extend surface faces by distance (best-effort)
                    try:
                        import adsk.core  # type: ignore
                        ext_feats = root.features.extendFeatures
                    except Exception:
                        ext_feats = None
                    if ext_feats:
                        try:
                            face_q = feat.get("faces_query") or feat.get("face_query")
                            faces = self._resolve_query(root, face_q, entity_type="face") if face_q else self._get_all_faces(root)
                        except Exception:
                            faces = self._get_all_faces(root)
                        try:
                            d_mm = self._parse_length_mm(feat.get("distance") or feat.get("offset") or "2.0") or 2.0
                            d = adsk.core.ValueInput.createByReal(d_mm / 10.0)
                            ei = ext_feats.createInput(faces, d)
                            # Optional: extend side/natural if supported
                            try:
                                side = (feat.get("side") or "natural").lower()
                                if hasattr(ei, "extensionType"):
                                    # API-specific enum mapping guarded via getattr
                                    import adsk.fusion  # type: ignore
                                    if side in ("natural", "default"):
                                        pass
                                    elif side in ("both", "symmetric") and hasattr(adsk.fusion, "SurfaceExtendTypes"):
                                        # Placeholder if API exposes symmetric; otherwise ignore
                                        ei.extensionType = getattr(adsk.fusion.SurfaceExtendTypes, "NaturalExtendType", ei.extensionType)
                            except Exception:
                                pass
                            ef = ext_feats.add(ei)
                            mapping[feat_id] = f"fusion:extend:{ef.entityToken}"
                            try:
                                self._record_lineage(feat_id, ef, root)
                            except Exception:
                                pass
                        except Exception:
                            mapping[feat_id] = "fusion:extend:E2602"
                elif kind == "trim":
                    # Trim faces by tool (face/plane) best-effort
                    try:
                        tr_feats = root.features.trimSurfaces
                    except Exception:
                        tr_feats = None
                    if tr_feats:
                        try:
                            target_q = feat.get("target_query") or feat.get("faces_query")
                            targets = self._resolve_query(root, target_q, entity_type="face") if target_q else self._get_all_faces(root)
                        except Exception:
                            targets = self._get_all_faces(root)
                        tool = None
                        try:
                            tool_q = feat.get("tool_query") or feat.get("plane_query")
                            if tool_q:
                                tcol = self._resolve_query(root, tool_q, entity_type="face")
                                tool = tcol.item(0) if tcol and tcol.count > 0 else None
                        except Exception:
                            tool = None
                        if tool is None:
                            tool = root.xZConstructionPlane
                        try:
                            keep = True if str(feat.get("keep" or "true")).lower() != "false" else False
                            ti = tr_feats.createInput(targets, tool, keep)
                            tf = tr_feats.add(ti)
                            mapping[feat_id] = f"fusion:trim:{tf.entityToken}"
                            try:
                                self._record_lineage(feat_id, tf, root)
                            except Exception:
                                pass
                        except Exception:
                            mapping[feat_id] = "fusion:trim:E2603"
                elif kind == "knit":
                    # Knit surfaces into a solid/single surface (best-effort)
                    try:
                        import adsk.core  # type: ignore
                        kn_feats = root.features.stitchFeatures
                    except Exception:
                        kn_feats = None
                    if kn_feats:
                        try:
                            face_q = feat.get("faces_query") or feat.get("surfaces_query")
                            faces = self._resolve_query(root, face_q, entity_type="face") if face_q else self._get_all_faces(root)
                        except Exception:
                            faces = self._get_all_faces(root)
                        try:
                            tol_mm = self._parse_length_mm(feat.get("tolerance") or "0.1") or 0.1
                            tol = adsk.core.ValueInput.createByReal(tol_mm / 10.0)
                            to_solid = bool(feat.get("is_solid") or feat.get("to_solid"))
                            ki = kn_feats.createInput(faces, tol, to_solid)
                            kf = kn_feats.add(ki)
                            mapping[feat_id] = f"fusion:knit:{kf.entityToken}"
                            try:
                                self._record_lineage(feat_id, kf, root)
                            except Exception:
                                pass
                        except Exception:
                            mapping[feat_id] = "fusion:knit:E2604"
                elif kind == "joint":
                    try:
                        app, ui, design = self._ensure_design()
                        root_comp = design.rootComponent
                        joints = root_comp.joints
                        # Resolve two entities (components/bodies) for the joint
                        a = None
                        b = None
                        try:
                            aq = feat.get("a") or feat.get("a_query")
                            bq = feat.get("b") or feat.get("b_query")
                            if aq:
                                ac = self._resolve_query(root, aq, entity_type="body")
                                a = ac.item(0) if ac and ac.count > 0 else None
                            if bq:
                                bc = self._resolve_query(root, bq, entity_type="body")
                                b = bc.item(0) if bc and bc.count > 0 else None
                        except Exception:
                            pass
                        if a is None or b is None:
                            mapping[feat_id] = "fusion:joint:E2401"
                        else:
                            # Determine joint origin/axes via planar face center as default
                            def _geom_for_body(body):
                                try:
                                    f = body.faces.item(0)
                                    return adsk.fusion.JointGeometry.createByPlanarFace(f, None, adsk.fusion.JointKeyPointTypes.CenterKeyPoint)
                                except Exception:
                                    return None
                            j_geo = _geom_for_body(a)
                            j_geo2 = _geom_for_body(b)
                            if not j_geo or not j_geo2:
                                mapping[feat_id] = "fusion:joint:E2402"
                            else:
                                j_in = joints.createInput(j_geo, j_geo2)
                                # Axis selection
                                axis_name = (feat.get("axis") or "Z").upper()
                                axis_dir = adsk.fusion.JointDirections.ZAxisJointDirection
                                if axis_name.startswith("X"):
                                    axis_dir = adsk.fusion.JointDirections.XAxisJointDirection
                                elif axis_name.startswith("Y"):
                                    axis_dir = adsk.fusion.JointDirections.YAxisJointDirection
                                jtype = (feat.get("type") or "revolute").lower()
                                if jtype == "slider":
                                    j_in.setAsSliderJointMotion(axis_dir)
                                elif jtype == "rigid":
                                    j_in.setAsRigidJointMotion()
                                elif jtype == "cylindrical" and hasattr(j_in, "setAsCylindricalJointMotion"):
                                    j_in.setAsCylindricalJointMotion(axis_dir)
                                elif jtype == "planar" and hasattr(j_in, "setAsPlanarJointMotion"):
                                    j_in.setAsPlanarJointMotion()
                                elif jtype == "ball" and hasattr(j_in, "setAsBallJointMotion"):
                                    j_in.setAsBallJointMotion()
                                elif jtype in ("pinslot", "pin_slot") and hasattr(j_in, "setAsPinSlotJointMotion"):
                                    j_in.setAsPinSlotJointMotion(axis_dir)
                                else:
                                    j_in.setAsRevoluteJointMotion(axis_dir)
                                # Limits/damping/preload
                                try:
                                    lim = feat.get("limits") or {}
                                    if isinstance(lim, dict):
                                        # Linear
                                        lmin = self._parse_length_mm(lim.get("linear_min") or lim.get("min_linear") or lim.get("min"))
                                        lmax = self._parse_length_mm(lim.get("linear_max") or lim.get("max_linear") or lim.get("max"))
                                        # Angular (deg)
                                        amin = self._parse_length_mm(lim.get("angular_min") or lim.get("min_angular"))
                                        amax = self._parse_length_mm(lim.get("angular_max") or lim.get("max_angular"))
                                        if jtype == "slider" and (lmin is not None or lmax is not None):
                                            jm = j_in.jointMotion
                                            try:
                                                jm.slideLimits.isRestValueRequired = False
                                                if lmin is not None:
                                                    jm.slideLimits.isMinimumValueEnabled = True
                                                    jm.slideLimits.minimumValue = (lmin / 10.0)  # cm
                                                if lmax is not None:
                                                    jm.slideLimits.isMaximumValueEnabled = True
                                                    jm.slideLimits.maximumValue = (lmax / 10.0)
                                            except Exception:
                                                self._diag("E2410", where="joint", message="Slider limits not supported")
                                        if jtype == "revolute" and (amin is not None or amax is not None):
                                            jm = j_in.jointMotion
                                            try:
                                                if amin is not None:
                                                    jm.rotationLimits.isMinimumValueEnabled = True
                                                    jm.rotationLimits.minimumValue = (amin / 180.0) * 3.141592653589793
                                                if amax is not None:
                                                    jm.rotationLimits.isMaximumValueEnabled = True
                                                    jm.rotationLimits.maximumValue = (amax / 180.0) * 3.141592653589793
                                            except Exception:
                                                self._diag("E2411", where="joint", message="Revolute limits not supported")
                                        # Cylindrical: both slide and rotation if supported
                                        if jtype == "cylindrical":
                                            jm = j_in.jointMotion
                                            try:
                                                if lmin is not None or lmax is not None:
                                                    jm.slideLimits.isRestValueRequired = False
                                                    if lmin is not None:
                                                        jm.slideLimits.isMinimumValueEnabled = True
                                                        jm.slideLimits.minimumValue = (lmin / 10.0)
                                                    if lmax is not None:
                                                        jm.slideLimits.isMaximumValueEnabled = True
                                                        jm.slideLimits.maximumValue = (lmax / 10.0)
                                            except Exception:
                                                pass
                                            try:
                                                if amin is not None or amax is not None:
                                                    if hasattr(jm, "rotationLimits"):
                                                        if amin is not None:
                                                            jm.rotationLimits.isMinimumValueEnabled = True
                                                            jm.rotationLimits.minimumValue = (amin / 180.0) * 3.141592653589793
                                                        if amax is not None:
                                                            jm.rotationLimits.isMaximumValueEnabled = True
                                                            jm.rotationLimits.maximumValue = (amax / 180.0) * 3.141592653589793
                                            except Exception:
                                                pass
                                    # Damping/preload (best-effort)
                                    if feat.get("damping") is not None:
                                        try:
                                            _ = float(feat.get("damping"))
                                            # Fusion API may not expose; record diagnostic if unsupported
                                            self._diag("E2412", where="joint", message="Damping specified but not settable in this Fusion API; ignoring.")
                                        except Exception:
                                            pass
                                    if feat.get("preload") is not None:
                                        try:
                                            _ = float(feat.get("preload"))
                                            self._diag("E2413", where="joint", message="Preload specified but not settable in this Fusion API; ignoring.")
                                        except Exception:
                                            pass
                                except Exception:
                                    pass
                                j = joints.add(j_in)
                                mapping[feat_id] = f"fusion:joint:{j.entityToken}"
                    except Exception:
                        mapping[feat_id] = "fusion:joint:E2401"
                elif kind == "mate_connector":
                    # Best-effort: create a construction point and oriented axis to serve as a connector
                    try:
                        import adsk.core  # type: ignore
                        target_q = feat.get("on") or feat.get("target") or {"kind": "face"}
                        fcol = self._resolve_query(root, target_q, entity_type="face")
                        face = fcol.item(0) if fcol and fcol.count > 0 else None
                        if face is None:
                            bodies = self._all_bodies(root)
                            face = bodies.item(bodies.count - 1).faces.item(0) if bodies.count > 0 else None
                        # Parse optional origin and axes from CSL
                        origin_cm = None
                        try:
                            origin_cm = self._parse_point3d(feat.get("origin") if isinstance(feat.get("origin"), str) else None)
                        except Exception:
                            origin_cm = None
                        # Determine orientation triad vectors from axes mapping
                        dir_vec = None
                        x_vec = None
                        y_vec = None
                        z_vec = None
                        try:
                            axes_spec = feat.get("axes") or {}
                            # Expect keys like "X","Y","Z" with values of form "+X","-Z", etc.
                            x_map = str(axes_spec.get("X") or axes_spec.get("x") or "").strip()
                            y_map = str(axes_spec.get("Y") or axes_spec.get("y") or "").strip()
                            z_map = str(axes_spec.get("Z") or axes_spec.get("z") or "").strip()
                            x_vec = self._vector_from_axis_map(x_map) if x_map else None
                            y_vec = self._vector_from_axis_map(y_map) if y_map else None
                            z_vec = self._vector_from_axis_map(z_map) if z_map else None
                            # Backwards-compat: dir_vec is used for the construction axis line direction
                            if z_vec is not None:
                                dir_vec = z_vec
                        except Exception:
                            dir_vec = None
                            x_vec = None
                            y_vec = None
                            z_vec = None
                        axes = root.constructionAxes
                        ai = axes.createInput()
                        try:
                            if origin_cm is not None and dir_vec is not None:
                                p = adsk.core.Point3D.create(origin_cm[0], origin_cm[1], origin_cm[2])
                                v = adsk.core.Vector3D.create(dir_vec[0], dir_vec[1], dir_vec[2])
                                ai.setByLine(adsk.core.InfiniteLine3D.create(p, v))
                            elif face is not None:
                                ai.setByNormalToSurface(face, face.pointOnFace)
                            else:
                                # Fallback: world Z at origin
                                z = adsk.core.Vector3D.create(0, 0, 1)
                                p = adsk.core.Point3D.create(0, 0, 0)
                                ai.setByLine(adsk.core.InfiniteLine3D.create(p, z))
                        except Exception:
                            # Final fallback
                            z = adsk.core.Vector3D.create(0, 0, 1)
                            p = adsk.core.Point3D.create(0, 0, 0)
                            ai.setByLine(adsk.core.InfiniteLine3D.create(p, z))
                        ax = axes.add(ai)
                        # Add construction point at origin if provided
                        try:
                            if origin_cm is not None:
                                cpts = root.constructionPoints
                                cpts.addFixed(adsk.core.Point3D.create(origin_cm[0], origin_cm[1], origin_cm[2]))
                        except Exception:
                            pass
                        # Tag attributes for traceability, tags, and full basis
                        try:
                            self._tag_attribute(ax, "csl_feat", feat_id)
                            tags_val = feat.get("tags") or feat.get("tag")
                            if isinstance(tags_val, list):
                                self._tag_attribute(ax, "csl_tags", ",".join([str(t) for t in tags_val]))
                            elif isinstance(tags_val, str):
                                self._tag_attribute(ax, "csl_tags", tags_val)
                            # Record basis and origin for downstream use
                            try:
                                import json  # type: ignore
                                basis = {
                                    "origin_cm": origin_cm if origin_cm is not None else [0.0, 0.0, 0.0],
                                    "x_dir": list(x_vec) if x_vec is not None else [1.0, 0.0, 0.0],
                                    "y_dir": list(y_vec) if y_vec is not None else [0.0, 1.0, 0.0],
                                    "z_dir": list(z_vec) if z_vec is not None else ([dir_vec[0], dir_vec[1], dir_vec[2]] if dir_vec is not None else [0.0, 0.0, 1.0])
                                }
                                self._tag_attribute(ax, "csl_basis", json.dumps(basis))
                            except Exception:
                                pass
                        except Exception:
                            pass
                        mapping[feat_id] = f"fusion:mate_connector:{ax.entityToken}"
                    except Exception:
                        mapping[feat_id] = "fusion:mate_connector:E2701"
                elif kind == "assembly_pattern":
                    # Best-effort: pattern occurrences/bodies similar to linear pattern
                    try:
                        import adsk.core  # type: ignore
                        pats = root.features.rectangularPatternFeatures
                        bodies = self._all_bodies(root)
                        if bodies.count > 0:
                            obj = adsk.core.ObjectCollection.create()
                            obj.add(bodies.item(bodies.count - 1))
                            count1 = int(feat.get("count1") or 2)
                            count2 = int(feat.get("count2") or 1)
                            sp1_mm = self._parse_length_mm(feat.get("spacing1") or "10 mm") or 10.0
                            sp2_mm = self._parse_length_mm(feat.get("spacing2") or "10 mm") or 10.0
                            X = root.xConstructionAxis
                            Y = root.yConstructionAxis
                            pi = pats.createInput(obj, X, adsk.core.ValueInput.createByReal(sp1_mm/10.0), adsk.core.ValueInput.createByString(str(count1)),
                                                   Y, adsk.core.ValueInput.createByReal(sp2_mm/10.0), adsk.core.ValueInput.createByString(str(count2)))
                            pf = pats.add(pi)
                            mapping[feat_id] = f"fusion:assembly_pattern:{pf.entityToken}"
                            try:
                                self._record_lineage(feat_id, pf, root)
                            except Exception:
                                pass
                            # Compute and tag per-occurrence transforms (translation + optional rotation)
                            try:
                                import json  # type: ignore
                                occs = []
                                angle_deg = None
                                try:
                                    angle_deg = float(self._parse_length_mm(str(feat.get("angle"))) or 0.0)
                                except Exception:
                                    angle_deg = None
                                for i in range(count1):
                                    for j in range(count2):
                                        tx_cm = (sp1_mm / 10.0) * i
                                        ty_cm = (sp2_mm / 10.0) * j
                                        entry = {"i": i, "j": j, "translate_cm": [tx_cm, ty_cm, 0.0]}
                                        if angle_deg is not None and angle_deg != 0.0:
                                            entry["rotate_deg_z"] = angle_deg
                                        occs.append(entry)
                                self._tag_attribute(pf, "csl_occ_transforms", json.dumps(occs))
                            except Exception:
                                pass
                            # If explicit per-instance overrides provided, attempt native application
                            try:
                                if isinstance(feat.get("instances"), list) and len(feat.get("instances")) > 0:
                                    self._apply_per_instance_pattern(pf, feat.get("instances"))
                            except Exception:
                                pass
                    except Exception:
                        mapping[feat_id] = "fusion:assembly_pattern:E2702"
                elif kind == "sheet_base_flange":
                    # Sheet metal base feature (try SheetMetal API; fallback to thin extrude)
                    try:
                        import adsk.core  # type: ignore
                        import adsk.fusion  # type: ignore
                        # Try native SheetMetal base feature
                        try:
                            app, ui, design = self._ensure_design()
                            sm_root = design.rootComponent
                            sm_feats = getattr(sm_root.features, "sheetMetalFeatures", None)
                            base_feats = getattr(sm_feats, "baseFeatures", None)
                            if base_feats and hasattr(base_feats, "add"):
                                th_mm = self._parse_length_mm(feat.get("thickness") or "1.5 mm") or 1.5
                                th = adsk.core.ValueInput.createByReal(th_mm / 10.0)
                                # Assume first sketch profile if not named
                                profile = None
                                sk_name = feat.get("profile") or None
                                if isinstance(sk_name, str):
                                    for sk in sm_root.sketches:
                                        if getattr(sk, "name", "") == sk_name and sk.profiles.count > 0:
                                            profile = sk.profiles.item(0)
                                            break
                                if profile is None:
                                    try:
                                        profile = sm_root.sketches.item(0).profiles.item(0)
                                    except Exception:
                                        profile = None
                                if profile is not None:
                                    bf_in = base_feats.createInput(profile, th)
                                    bf = base_feats.add(bf_in)
                                    mapping[feat_id] = f"fusion:sheet_base_flange:{bf.entityToken}"
                                    try:
                                        self._record_lineage(feat_id, bf, root)
                                    except Exception:
                                        pass
                                    # K-factor/relief diagnostics
                                    try:
                                        if feat.get("k_factor") is not None:
                                            self._diag("E2805", where="sheet_metal", message="K-factor not settable via this API version; recorded as diagnostic")
                                        if feat.get("relief"):
                                            self._diag("E2806", where="sheet_metal", message=f"Relief '{feat.get('relief')}' requested; not directly supported in this stub")
                                    except Exception:
                                        pass
                                    break
                        except Exception:
                            pass
                        # Fallback: create thin extrude from profile with thickness
                        th_mm = self._parse_length_mm(feat.get("thickness") or "1.5 mm") or 1.5
                        dist_mm = self._parse_length_mm(feat.get("length") or "20 mm") or 20.0
                        sk_name = feat.get("profile") or None
                        profile = None
                        if isinstance(sk_name, str):
                            for sk in root.sketches:
                                if getattr(sk, "name", "") == sk_name and sk.profiles.count > 0:
                                    profile = sk.profiles.item(0)
                                    break
                        if profile is None:
                            bodies = self._all_bodies(root)
                            profile = bodies.item(bodies.count - 1).faces.item(0) if bodies.count > 0 else None
                        ext = root.features.extrudeFeatures
                        ext_input = ext.createInput(profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
                        ext_input.isSolid = False
                        ext_input.thickness = adsk.core.ValueInput.createByReal(th_mm / 10.0)
                        ext_input.setDistanceExtent(False, adsk.core.ValueInput.createByReal(dist_mm / 10.0))
                        ef = ext.add(ext_input)
                        mapping[feat_id] = f"fusion:sheet_base_flange:{ef.entityToken}"
                        try:
                            self._record_lineage(feat_id, ef, root)
                        except Exception:
                            pass
                    except Exception:
                        mapping[feat_id] = "fusion:sheet_base_flange:E2801"
                elif kind == "sheet_edge_flange":
                    # Attempt native edge flange; fallback to offset/thin extrude
                    try:
                        import adsk.core  # type: ignore
                        import adsk.fusion  # type: ignore
                        app, ui, design = self._ensure_design()
                        sm_root = design.rootComponent
                        sm_feats = getattr(sm_root.features, "sheetMetalFeatures", None)
                        ef_feats = getattr(sm_feats, "flangeFeatures", None) if sm_feats else None
                        edge = None
                        try:
                            edges = self._resolve_query(root, feat.get("on") or {"kind": "edge"}, entity_type="edge")
                            edge = edges.item(0) if edges and edges.count > 0 else None
                        except Exception:
                            edge = None
                        height_mm = self._parse_length_mm(feat.get("height") or "10 mm") or 10.0
                        angle_deg = None
                        if feat.get("angle") is not None:
                            try:
                                angle_deg = float(self._parse_length_mm(str(feat.get("angle"))) or 90.0)
                            except Exception:
                                angle_deg = None
                        relief = str(feat.get("relief") or "").lower() or None
                        if ef_feats and edge and hasattr(ef_feats, "add") and hasattr(ef_feats, "createInput"):
                            try:
                                h = adsk.core.ValueInput.createByReal(height_mm / 10.0)
                                ein = ef_feats.createInput(edge, h)
                                try:
                                    if angle_deg is not None and hasattr(ein, "angle"):
                                        ein.angle = adsk.core.ValueInput.createByReal((angle_deg / 180.0) * 3.141592653589793)
                                except Exception:
                                    pass
                                try:
                                    if relief and hasattr(ein, "reliefType"):
                                        # Best-effort mapping of relief types
                                        rt = getattr(adsk.fusion, "SheetMetalReliefTypes", None)
                                        if rt:
                                            pick = None
                                            for cand in ("RoundReliefType", "TearReliefType", "SquareReliefType"):
                                                if relief in cand.lower() and hasattr(rt, cand):
                                                    pick = getattr(rt, cand)
                                                    break
                                            if pick is None and hasattr(rt, "RoundReliefType"):
                                                pick = getattr(rt, "RoundReliefType")
                                            if pick is not None:
                                                ein.reliefType = pick
                                except Exception:
                                    pass
                                ef = ef_feats.add(ein)
                                mapping[feat_id] = f"fusion:sheet_edge_flange:{ef.entityToken}"
                                continue
                            except Exception:
                                pass
                        # Fallback
                        try:
                            offs = root.features.offsetFacesFeatures
                            off_val = adsk.core.ValueInput.createByReal((height_mm)/10.0)
                            of = offs.add(self._get_all_faces(root), off_val)
                            mapping[feat_id] = f"fusion:sheet_edge_flange:{of.entityToken}"
                            if angle_deg is not None or relief is not None:
                                self._diag("E2807", where="sheet_metal", message="Edge flange angle/relief not supported in stub mode")
                        except Exception:
                            mapping[feat_id] = "fusion:sheet_edge_flange:E2802"
                    except Exception:
                        mapping[feat_id] = "fusion:sheet_edge_flange:E2802"
                elif kind == "sheet_bend":
                    # Native bend if available; fallback to draft
                    try:
                        import adsk.core  # type: ignore
                        import adsk.fusion  # type: ignore
                        app, ui, design = self._ensure_design()
                        sm_root = design.rootComponent
                        sm_feats = getattr(sm_root.features, "sheetMetalFeatures", None)
                        bend_feats = getattr(sm_feats, "bendFeatures", None) if sm_feats else None
                        edge = None
                        try:
                            eq = feat.get("on") or feat.get("edge_query") or {"kind": "edge"}
                            ecol = self._resolve_query(root, eq, entity_type="edge")
                            edge = ecol.item(0) if ecol and ecol.count > 0 else None
                        except Exception:
                            edge = None
                        angle_deg = float(self._parse_length_mm(feat.get("angle") or "90") or 90.0)
                        angle = adsk.core.ValueInput.createByReal((angle_deg/180.0)*3.141592653589793)
                        if bend_feats and edge is not None and hasattr(bend_feats, "add"):
                            try:
                                bi = bend_feats.createInput(edge, angle)
                                # Relief type best-effort
                                rel = str(feat.get("relief") or "").lower()
                                try:
                                    rt = getattr(adsk.fusion, "SheetMetalReliefTypes", None)
                                    if rt and hasattr(bi, "reliefType"):
                                        pick = None
                                        for cand in ("RoundReliefType", "TearReliefType", "SquareReliefType"):
                                            if rel in cand.lower() and hasattr(rt, cand):
                                                pick = getattr(rt, cand)
                                                break
                                        if pick is not None:
                                            bi.reliefType = pick
                                except Exception:
                                    pass
                                bf = bend_feats.add(bi)
                                mapping[feat_id] = f"fusion:sheet_bend:{bf.entityToken}"
                            except Exception:
                                mapping[feat_id] = "fusion:sheet_bend:E2803"
                        else:
                            # Fallback: draft faces near an edge to simulate bend
                            dft = root.features.draftFeatures
                            faces = self._get_all_faces(root)
                            di = dft.createInput(faces, root.xZConstructionPlane, angle, adsk.fusion.DraftDirectionsType.PullDirectionType)
                            df = dft.add(di)
                            mapping[feat_id] = f"fusion:sheet_bend:{df.entityToken}"
                        # Best-effort: set K-factor if rule exposure exists
                        try:
                            if feat.get("k_factor") is not None and hasattr(design, "activeSheetMetalRule"):
                                rule = getattr(design, "activeSheetMetalRule", None)
                                if rule and hasattr(rule, "kFactor"):
                                    kf = float(self._parse_length_mm(str(feat.get("k_factor"))) or 0.5)
                                    rule.kFactor = kf
                        except Exception:
                            pass
                    except Exception:
                        mapping[feat_id] = "fusion:sheet_bend:E2803"
                elif kind == "sheet_unfold" or kind == "sheet_refold":
                    # Native unfold/refold when supported; conservative fallbacks otherwise
                    try:
                        import adsk.core  # type: ignore
                        import adsk.fusion  # type: ignore
                        feats = root.features
                        if kind == "sheet_unfold":
                            unfold_feats = getattr(feats, "unfoldFeatures", None)
                            if unfold_feats and (hasattr(unfold_feats, "add") or hasattr(unfold_feats, "createInput")):
                                # Stationary face selection (required). Accept 'stationary' or 'on' query.
                                stat_faces = None
                                try:
                                    stat_faces = self._resolve_query(root, feat.get("stationary") or feat.get("on") or {"kind": "face"}, entity_type="face")
                                except Exception:
                                    stat_faces = None
                                stat = stat_faces.item(0) if stat_faces and getattr(stat_faces, "count", 0) > 0 else None
                                # Optional bends selection. If absent, attempt unfold-all when API permits.
                                bends_col = adsk.core.ObjectCollection.create()
                                added_any_bend = False
                                try:
                                    bq = feat.get("bends_query") or feat.get("bends")
                                    if bq is not None:
                                        # Try faces first
                                        bfaces = None
                                        try:
                                            bfaces = self._resolve_query(root, bq, entity_type="face")
                                        except Exception:
                                            bfaces = None
                                        if bfaces and getattr(bfaces, "count", 0) > 0:
                                            for i in range(bfaces.count):
                                                bends_col.add(bfaces.item(i))
                                            added_any_bend = True
                                        else:
                                            # Try edges as bend identifiers
                                            bedges = None
                                            try:
                                                bedges = self._resolve_query(root, bq, entity_type="edge")
                                            except Exception:
                                                bedges = None
                                            if bedges and getattr(bedges, "count", 0) > 0:
                                                for i in range(bedges.count):
                                                    bends_col.add(bedges.item(i))
                                                added_any_bend = True
                                except Exception:
                                    pass
                                # Build input using available signatures
                                uf = None
                                try:
                                    if hasattr(unfold_feats, "createInput"):
                                        try:
                                            # Common signature: (stationaryFace, bends, unfoldAllBends: bool)
                                            inp = unfold_feats.createInput(stat, bends_col, (not added_any_bend))
                                        except Exception:
                                            # Some versions: (stationaryFace, bends)
                                            try:
                                                inp = unfold_feats.createInput(stat, bends_col)
                                            except Exception:
                                                inp = None
                                        if inp is not None:
                                            uf = unfold_feats.add(inp)
                                    if uf is None and hasattr(unfold_feats, "add"):
                                        # Last-resort: try direct add with (stationaryFace, bends)
                                        try:
                                            uf = unfold_feats.add(stat, bends_col)
                                        except Exception:
                                            uf = None
                                except Exception:
                                    uf = None
                                if uf:
                                    mapping[feat_id] = f"fusion:sheet_unfold:{uf.entityToken}"
                                    try:
                                        self._record_lineage(feat_id, uf, root)
                                    except Exception:
                                        pass
                                else:
                                    try:
                                        self._diag("E2808", where="sheet_metal", message="Unfold features API not available or call failed; kept diagnostic only")
                                    except Exception:
                                        pass
                            else:
                                try:
                                    self._diag("E2808", where="sheet_metal", message="Unfold features not exposed in this Fusion version")
                                except Exception:
                                    pass
                        else:  # sheet_refold
                            refold_feats = getattr(feats, "refoldFeatures", None)
                            rf = None
                            if refold_feats and (hasattr(refold_feats, "add") or hasattr(refold_feats, "createInput")):
                                try:
                                    rinp = None
                                    if hasattr(refold_feats, "createInput"):
                                        try:
                                            rinp = refold_feats.createInput()
                                        except Exception:
                                            rinp = None
                                    rf = refold_feats.add(rinp) if rinp is not None else refold_feats.add()
                                except Exception:
                                    rf = None
                            # Fallback: if a prior Unfold exists, try toggling by adding an empty refold or by suppress/unsuppress
                            if rf is None:
                                try:
                                    unfold_feats = getattr(feats, "unfoldFeatures", None)
                                    if unfold_feats and hasattr(unfold_feats, "count") and unfold_feats.count > 0:
                                        # Attempt to add a refold without explicit input
                                        if refold_feats and hasattr(refold_feats, "add"):
                                            try:
                                                rf = refold_feats.add()
                                            except Exception:
                                                rf = None
                                except Exception:
                                    rf = None
                            if rf:
                                mapping[feat_id] = f"fusion:sheet_refold:{rf.entityToken}"
                                try:
                                    self._record_lineage(feat_id, rf, root)
                                except Exception:
                                    pass
                            else:
                                try:
                                    self._diag("E2809", where="sheet_metal", message="Refold features API not available or call failed; kept diagnostic only")
                                except Exception:
                                    pass
                    except Exception:
                        try:
                            self._diag("E2804", where="sheet_metal", message=f"{kind} not supported or failed; stub/diagnostic only")
                        except Exception:
                            pass

            # Optionally export and thumbnails
            if csl_ir.get("export"):
                self.export(csl_ir.get("export", []))
            if csl_ir.get("thumbnail"):
                self.thumbnail(csl_ir.get("thumbnail", []))
            # Materials/PMI (lightweight)
            try:
                self._apply_materials_and_pmi(csl_ir)
            except Exception:
                pass
            # After realization, refresh lineage from attributes for robustness
            try:
                self._refresh_lineage_from_attributes(root)
            except Exception:
                pass

        except Exception as ex:  # pragma: no cover - defensive
            try:
                self._diag("E3001", where="realize", message=f"Realize failed: {ex}")
            except Exception:
                pass
            print(f"[FusionBackend] realize failed: {ex}")

        return mapping

    def export(self, export_ops: List[Dict[str, Any]]) -> None:
        if not self._fusion_available:
            print(f"[FusionBackend] Dry-run export: {export_ops}")
            try:
                self._diag("E3000", where="export", message="Fusion API unavailable; dry-run export.")
            except Exception:
                pass
            return
        try:
            import adsk.core  # type: ignore
            import adsk.fusion  # type: ignore
            app, ui, design = self._ensure_design()
            root: adsk.fusion.Component = design.rootComponent
            exp: adsk.fusion.ExportManager = design.exportManager
            for op in export_ops:
                fmt = (op.get("format") or "").upper()
                path = op.get("path") or "out/export"
                # Optional target selection
                target_obj = root
                try:
                    tq = op.get("target_query") or op.get("target")
                    if tq:
                        tcol = self._resolve_query(root, tq, entity_type="body")
                        if tcol and tcol.count > 0:
                            target_obj = tcol
                except Exception:
                    pass
                if fmt == "STEP":
                    opts = exp.createSTEPExportOptions(path)
                    # Attempt AP242 selection
                    try:
                        ap = (op.get("ap") or op.get("protocol") or op.get("application_protocol") or "").upper()
                        if ap in ("AP242", "AP242ED1", "AP242ED2"):
                            import adsk.fusion as _f  # type: ignore
                            enum_val = None
                            for enum_name in ("StepApplicationProtocolType", "StepProtocolTypes", "ApplicationProtocolTypes"):
                                enum_t = getattr(_f, enum_name, None)
                                if not enum_t:
                                    continue
                                for cand in ("AP242StandardApplicationProtocolType", "AP242ProtocolType", "AP242"):
                                    if hasattr(enum_t, cand):
                                        enum_val = getattr(enum_t, cand)
                                        break
                                if enum_val is not None:
                                    break
                            for attr in ("applicationProtocolType", "stepApplicationProtocolType", "protocolType"):
                                if hasattr(opts, attr) and enum_val is not None:
                                    try:
                                        setattr(opts, attr, enum_val)
                                        break
                                    except Exception:
                                        continue
                    except Exception:
                        pass
                    exp.execute(opts)
                    # Sidecar AP242 metadata (for downstream)
                    try:
                        meta = {
                            "schema": "AP242-sidecar",
                            "csl_version": "1.1",
                            "backend": "fusion",
                            "commit": self.get_capabilities().get("commit"),
                            "fusion_build": self.get_capabilities().get("fusion_build"),
                        }
                        sidecar = path + ".ap242.json"
                        import json as _json
                        with open(sidecar, "w", encoding="utf-8") as f:
                            f.write(_json.dumps(meta, indent=2))
                        if self.session_config.get("aps_bucket"):
                            self._aps_upload(sidecar)
                    except Exception:
                        pass
                elif fmt == "STL":
                    try:
                        opts = exp.createSTLExportOptions(root, path)
                    except Exception:
                        opts = exp.createSTLExportOptions(root.bRepBodies, path)
                    # Options: resolution and units parity (best-effort)
                    try:
                        res = (op.get("resolution") or "high").lower()
                        if hasattr(opts, "meshRefinement"):
                            if res == "low":
                                opts.meshRefinement = adsk.fusion.MeshRefinementSettings.MeshRefinementLow
                            elif res == "medium":
                                opts.meshRefinement = adsk.fusion.MeshRefinementSettings.MeshRefinementMedium
                            else:
                                opts.meshRefinement = adsk.fusion.MeshRefinementSettings.MeshRefinementHigh
                        if isinstance(op.get("binary"), bool) and hasattr(opts, "isBinaryFormat"):
                            opts.isBinaryFormat = bool(op.get("binary"))
                        # Advanced mesh controls
                        if hasattr(opts, "surfaceDeviation") and op.get("deviation"):
                            dev_mm = self._parse_length_mm(op.get("deviation"))
                            if dev_mm is not None:
                                opts.surfaceDeviation = float(dev_mm) / 10.0
                        if hasattr(opts, "maximumEdgeLength") and (op.get("max_edge") or op.get("max_edge_length")):
                            me_val = op.get("max_edge") or op.get("max_edge_length")
                            me_mm = self._parse_length_mm(me_val)
                            if me_mm is not None:
                                opts.maximumEdgeLength = float(me_mm) / 10.0
                        if hasattr(opts, "aspectRatio") and op.get("aspect_ratio"):
                            try:
                                opts.aspectRatio = float(op.get("aspect_ratio"))
                            except Exception:
                                pass
                        ang_key = None
                        for k in ("normal_deviation_deg", "angular_tolerance_deg", "angular"):
                            if op.get(k) is not None:
                                ang_key = k
                                break
                        if ang_key is not None:
                            try:
                                ang_deg = float(self._parse_length_mm(str(op.get(ang_key))) or 0.0)
                                ang_rad = (ang_deg / 180.0) * 3.141592653589793
                                for attr in ("normalTolerance", "angularTolerance"):
                                    if hasattr(opts, attr):
                                        try:
                                            setattr(opts, attr, ang_rad)
                                        except Exception:
                                            pass
                            except Exception:
                                pass
                        # Units
                        req_units = (op.get("units") or "").lower()
                        applied_units = False
                        for attr in ("meshUnits", "stlUnits", "units"):
                            if hasattr(opts, attr):
                                try:
                                    val = None
                                    if req_units in ("mm", "millimeter", "millimetre"):
                                        val = getattr(adsk.fusion, "StlUnitsMillimeter", None) or getattr(adsk.fusion, "UnitsMillimeter", None)
                                    elif req_units in ("cm", "centimeter"):
                                        val = getattr(adsk.fusion, "StlUnitsCentimeter", None) or getattr(adsk.fusion, "UnitsCentimeter", None)
                                    elif req_units in ("in", "inch", "inches"):
                                        val = getattr(adsk.fusion, "StlUnitsInch", None) or getattr(adsk.fusion, "UnitsInch", None)
                                    if val is not None:
                                        setattr(opts, attr, val)
                                        applied_units = True
                                        break
                                except Exception:
                                    continue
                        if req_units and not applied_units:
                            self._diag("E3004", where="export", message=f"STL units '{req_units}' not directly supported by this Fusion version; proceeding with document units.")
                    except Exception:
                        pass
                    exp.execute(opts)
                elif fmt == "IGES":
                    opts = exp.createIGESExportOptions(path)
                    exp.execute(opts)
                elif fmt in ("3MF", "OBJ"):
                    # Use generic export manager; not all formats may be available
                    opts = exp.createOBJExportOptions(path) if fmt == "OBJ" else exp.createMF3DExportOptions(path)
                    # 3MF: units/binary/appearance (best-effort)
                    if fmt == "3MF":
                        try:
                            req_units = (op.get("units") or op.get("meshUnits") or "").lower()
                            unit_map = {
                                "mm": (getattr(adsk.fusion, "UnitsMillimeter", None) or getattr(adsk.fusion, "StlUnitsMillimeter", None)),
                                "cm": (getattr(adsk.fusion, "UnitsCentimeter", None) or getattr(adsk.fusion, "StlUnitsCentimeter", None)),
                                "inch": (getattr(adsk.fusion, "UnitsInch", None) or getattr(adsk.fusion, "StlUnitsInch", None)),
                            }
                            if hasattr(opts, "units") and req_units in unit_map and unit_map[req_units] is not None:
                                opts.units = unit_map[req_units]
                        except Exception:
                            pass
                        try:
                            if hasattr(opts, "isBinary") and op.get("binary") is not None:
                                opts.isBinary = bool(op.get("binary"))
                        except Exception:
                            pass
                        try:
                            if hasattr(opts, "exportAppearance") and op.get("appearance") is not None:
                                opts.exportAppearance = bool(op.get("appearance"))
                        except Exception:
                            pass
                    exp.execute(opts)
                # Upload artifact to APS if configured
                try:
                    if self.session_config.get("aps_bucket"):
                        self._aps_upload(path)
                except Exception:
                    pass
        except Exception as ex:
            try:
                self._diag("E3002", where="export", message=f"Export failed: {ex}")
            except Exception:
                pass
            print(f"[FusionBackend] export failed: {ex}")
        return

    def thumbnail(self, thumb_ops: List[Dict[str, Any]]) -> None:
        if not self._fusion_available:
            print(f"[FusionBackend] Dry-run thumbnail: {thumb_ops}")
            try:
                self._diag("E3000", where="thumbnail", message="Fusion API unavailable; dry-run thumbnail.")
            except Exception:
                pass
            return
        try:
            import adsk.core  # type: ignore
            app = adsk.core.Application.get()
            vp = app.activeViewport
            for op in thumb_ops:
                path = op.get("path") or "out/preview.png"
                w = int(op.get("width") or 800)
                h = int(op.get("height") or 600)
                view = (op.get("view") or "iso").lower()
                style = (op.get("style") or "shaded").lower()
                bg = (op.get("background") or "solid").lower()
                # Configure camera deterministically
                try:
                    cam = vp.camera
                    if view == "top":
                        cam.viewOrientation = adsk.core.ViewOrientations.TopViewOrientation
                    elif view == "front":
                        cam.viewOrientation = adsk.core.ViewOrientations.FrontViewOrientation
                    elif view == "right":
                        cam.viewOrientation = adsk.core.ViewOrientations.RightViewOrientation
                    else:
                        cam.viewOrientation = adsk.core.ViewOrientations.IsometricViewOrientation
                    vp.camera = cam
                except Exception:
                    pass
                try:
                    if style == "wireframe":
                        vp.displayStyle = adsk.core.DisplayStyles.WireframeDisplayStyle
                    else:
                        vp.displayStyle = adsk.core.DisplayStyles.ShadedDisplayStyle
                except Exception:
                    pass
                # Attempt viewport save; name differs across versions
                saved = False
                try:
                    vp.saveAsImageFile(path, w, h)
                    saved = True
                except Exception:
                    pass
                if not saved:
                    img = vp.tiledRendering
                    try:
                        vp.saveAsImageFile(path)
                    except Exception:
                        pass
                # Upload thumbnail to APS if configured
                try:
                    if self.session_config.get("aps_bucket"):
                        self._aps_upload(path)
                except Exception:
                    pass
        except Exception as ex:
            try:
                self._diag("E3003", where="thumbnail", message=f"Thumbnail failed: {ex}")
            except Exception:
                pass
            print(f"[FusionBackend] thumbnail failed: {ex}")
        return

    # ------------------------
    # Helpers
    # ------------------------
    def _ensure_design(self):
        import adsk.core  # type: ignore
        import adsk.fusion  # type: ignore
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = adsk.fusion.Design.cast(app.activeProduct)
        if not design:
            app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
            design = adsk.fusion.Design.cast(app.activeProduct)
        return app, ui, design

    def _plane_from_name(self, root, plane_name: str):
        import adsk.fusion  # type: ignore
        if "xz" in plane_name:
            return root.xZConstructionPlane
        if "yz" in plane_name:
            return root.yZConstructionPlane
        return root.xYConstructionPlane

    def _parse_point(self, value: Optional[Any]) -> Optional[List[float]]:
        if not value:
            return None
        # Handle list/tuple input (CSL format)
        if isinstance(value, (list, tuple)):
            if len(value) < 2:
                return None
            # Values are in mm, return as-is (will be converted to cm later if needed)
            return list(value)
        # Handle string input (legacy format)
        if isinstance(value, str):
            # Expect formats like "x, y" or "15 mm, 15 mm"
            parts = [p.strip() for p in value.split(",")]
            if len(parts) < 2:
                return None
            x = self._parse_length_cm(parts[0])
            y = self._parse_length_cm(parts[1])
            if x is None or y is None:
                return None
            return [x, y]
        return None

    def _parse_point3d(self, value: Optional[str]) -> Optional[List[float]]:
        if not value:
            return None
        # Expect formats like "x, y, z" with units allowed per component
        parts = [p.strip() for p in value.split(",")]
        if len(parts) < 3:
            # Allow 2D input, infer z=0
            pt2 = self._parse_point(value)
            if pt2 is None:
                return None
            return [pt2[0], pt2[1], 0.0]
        x = self._parse_length_cm(parts[0])
        y = self._parse_length_cm(parts[1])
        z = self._parse_length_cm(parts[2])
        if x is None or y is None or z is None:
            return None
        return [x, y, z]

    def _vector_from_axis_map(self, axis_map: str) -> Optional[Tuple[float, float, float]]:
        try:
            s = axis_map.strip()
            if not s:
                return None
            sign = -1.0 if s.startswith("-") else 1.0
            base = s[-1:].upper()
            if base == "X":
                return (sign, 0.0, 0.0)
            if base == "Y":
                return (0.0, sign, 0.0)
            return (0.0, 0.0, sign)
        except Exception:
            return None

    def _parse_length_mm(self, value: Optional[str]) -> Optional[float]:
        if value is None:
            return None
        # Extract first float; default units mm if specified
        m = re.search(r"[-+]?[0-9]*\.?[0-9]+", str(value))
        if not m:
            return None
        return float(m.group(0))

    def _parse_length_cm(self, value: Optional[str]) -> Optional[float]:
        mm = self._parse_length_mm(value)
        return None if mm is None else mm / 10.0

    def _first_profile(self, root) -> Optional[Any]:
        # Return the first available profile from any sketch
        for sk in root.sketches:
            if sk.profiles.count > 0:
                return sk.profiles.item(0)
        return None
    
    def _feature_operation(self, op_str: Optional[str]) -> Any:
        """Convert operation string to Fusion FeatureOperation enum"""
        import adsk.fusion  # type: ignore
        
        if not op_str:
            op_str = "new_solid"
        
        op_str = op_str.lower()
        
        if op_str in ("new_solid", "new", "new_body"):
            return adsk.fusion.FeatureOperations.NewBodyFeatureOperation
        elif op_str in ("join", "union", "add"):
            return adsk.fusion.FeatureOperations.JoinFeatureOperation
        elif op_str in ("cut", "subtract", "difference"):
            return adsk.fusion.FeatureOperations.CutFeatureOperation
        elif op_str in ("intersect", "intersection"):
            return adsk.fusion.FeatureOperations.IntersectFeatureOperation
        else:
            # Default to new body
            return adsk.fusion.FeatureOperations.NewBodyFeatureOperation

    def _collect_profiles(self, root, max_count: int = 3) -> List[Any]:
        profiles: List[Any] = []
        for sk in root.sketches:
            for i in range(sk.profiles.count):
                profiles.append(sk.profiles.item(i))
                if len(profiles) >= max_count:
                    return profiles
        return profiles

    def _first_path(self, root) -> Optional[Any]:
        # Return first curve (line/arc) as a path for sweep
        for sk in root.sketches:
            curves = sk.sketchCurves
            if curves.sketchLines.count > 0:
                return curves.sketchLines.item(0)
            if curves.sketchArcs.count > 0:
                return curves.sketchArcs.item(0)
        return None

    def _all_body_edges(self, root):
        import adsk.core  # type: ignore
        import adsk.fusion  # type: ignore
        col = adsk.core.ObjectCollection.create()  # type: ignore
        for b in root.bRepBodies:
            for e in b.edges:
                col.add(e)
        return col

    def _all_bodies(self, root):
        return root.bRepBodies


    def _first_planar_face(self, root):
        try:
            import adsk.core  # type: ignore
            bodies = self._all_bodies(root)
            if bodies.count == 0:
                return None
            last = bodies.item(bodies.count - 1)
            for f in last.faces:
                try:
                    surf = f.geometry
                    # 0 == Plane in some API versions
                    if getattr(surf, "surfaceType", None) == 0:
                        return f
                except Exception:
                    continue
            # Fallback: return first face
            return last.faces.item(0) if last.faces.count > 0 else None
        except Exception:
            return None

    def _record_lineage(self, feature_id: str, feature_obj: Any, root) -> None:
        """Record basic lineage tokens for bodies/faces/edges produced by a feature.

        This is a best-effort placeholder toward stable selection. Tokens are session-stable.
        """
        try:
            import adsk.core  # type: ignore
            design = root.parentDesign
            tokens: Dict[str, List[str]] = {"bodies": [], "faces": [], "edges": []}
            # Bodies created by feature (if available)
            try:
                bodies = getattr(feature_obj, "bodies", None) or getattr(feature_obj, "occurrence", None)
                if bodies and hasattr(bodies, "count"):
                    for i in range(bodies.count):
                        b = bodies.item(i)
                        tokens["bodies"].append(b.entityToken)
                        # Tag body with CSL attributes
                        try:
                            self._tag_attribute(b, "csl_feat", feature_id)
                        except Exception:
                            pass
                        # Collect faces/edges for that body
                        try:
                            for f in b.faces:
                                tokens["faces"].append(f.entityToken)
                                try:
                                    self._tag_attribute(f, "csl_feat", feature_id)
                                except Exception:
                                    pass
                            for e in b.edges:
                                tokens["edges"].append(e.entityToken)
                                try:
                                    self._tag_attribute(e, "csl_feat", feature_id)
                                except Exception:
                                    pass
                        except Exception:
                            pass
            except Exception:
                pass
            # Normalize deterministically (unique + sorted by token)
            for k in ("bodies", "faces", "edges"):
                seen = set()
                norm: List[str] = []
                for t in tokens.get(k, []):
                    if t and t not in seen:
                        seen.add(t)
                        norm.append(t)
                tokens[k] = sorted(norm)
            self._lineage[feature_id] = tokens
            # Persist lineage (merge)
            try:
                self._persisted_lineage.setdefault(feature_id, {"bodies": [], "faces": [], "edges": []})
                for k in ("bodies", "faces", "edges"):
                    exist = set(self._persisted_lineage[feature_id].get(k, []))
                    for t in tokens.get(k, []):
                        if t and t not in exist:
                            self._persisted_lineage[feature_id].setdefault(k, []).append(t)
                    # Normalize persisted as well
                    cur = [t for t in self._persisted_lineage[feature_id].get(k, []) if t]
                    self._persisted_lineage[feature_id][k] = sorted(list(dict.fromkeys(cur)))
                self._save_persisted_lineage()
            except Exception:
                pass
        except Exception:
            # Ignore if not in Fusion environment
            return

    def _resolve_query(self, root, query_spec: Any, entity_type: str = "face"):
        """Resolve a minimal subset of CSL queries to Fusion ObjectCollection.

        Supported (initial):
        - created_by: feature_id (uses lineage map)
        - largest_by: axis (X|Y|Z) [best-effort: returns largest area face]
        - owner_feature==: alias to created_by
        - pattern_instances: select entities created by a pattern feature
        - tangent_connected: faces tangent-flood from a seed with tolerance
        - curvature≈ / radius≈ / area≈: approximate numeric matching with tolerance
        - by_material: filter by appearance/material name

        Extended (deterministic best-effort):
        - largest: True (faces → largest area; edges → longest length)
        - normal== / faces_parallel(direction): planar faces by normal within tol_deg
        - cylindrical_faces: by radius/diameter tolerance and optional axis≈
        - loop_edges(seed, boundary): outer loop edges of faces, or all loop edges
        - of: expand operator (edges/faces/vertices of bodies/faces)
        - owner_body: map any entity to its owning body
        - by_tag: entities with CSL tag attribute
        - by_id: entityToken(s) direct lookup
        """
        import adsk.core  # type: ignore
        col = adsk.core.ObjectCollection.create()

        def add_entity_by_token(token: str) -> None:
            try:
                # Modern API: findEntityByToken on design
                design = root.parentDesign
                ent = design.findEntityByToken(token)
                if ent:
                    col.add(ent)
            except Exception:
                pass

        kind = (query_spec.get("kind") or query_spec.get("type") or entity_type).lower()
        created_by = query_spec.get("created_by") or query_spec.get("owner_feature")
        largest_by = query_spec.get("largest_by") or query_spec.get("largest")
        owner_feature = query_spec.get("owner_feature==") or query_spec.get("owner_feature_eq")
        pat = query_spec.get("pattern_instances")
        tangent = query_spec.get("tangent_connected")
        curv_approx = query_spec.get("curvature≈") or query_spec.get("curvature_approx")
        radius_approx = query_spec.get("radius≈") or query_spec.get("radius_approx")
        area_approx = query_spec.get("area≈") or query_spec.get("area_approx")
        tol = query_spec.get("tol") or query_spec.get("tolerance")
        by_material = query_spec.get("by_material") or query_spec.get("appearance")
        largest_flag = True if isinstance(query_spec.get("largest"), bool) and query_spec.get("largest") else False
        by_tag = query_spec.get("by_tag") or query_spec.get("tag")
        by_id = query_spec.get("by_id") or query_spec.get("id_token")
        of_query = query_spec.get("of") or query_spec.get("from")
        normal_eq = query_spec.get("normal==") or query_spec.get("normal_eq") or query_spec.get("by_normal")
        faces_parallel = query_spec.get("faces_parallel") or None
        boundary = bool(query_spec.get("boundary"))
        cyl_kind = (query_spec.get("cylindrical_faces") or (query_spec.get("kind") == "cylindrical_faces"))
        diam_approx = query_spec.get("d≈") or query_spec.get("diameter≈")
        axis_approx = query_spec.get("axis≈") or query_spec.get("axis_eq")

        # Small helpers local to query resolution
        def _axis_from_str(ax: Any):
            try:
                s = str(ax or "Z").upper()
                if s.startswith("+Z") or s == "Z":
                    return (0.0, 0.0, 1.0)
                if s.startswith("-Z"):
                    return (0.0, 0.0, -1.0)
                if s.startswith("+X") or s == "X":
                    return (1.0, 0.0, 0.0)
                if s.startswith("-X"):
                    return (-1.0, 0.0, 0.0)
                if s.startswith("+Y") or s == "Y":
                    return (0.0, 1.0, 0.0)
                if s.startswith("-Y"):
                    return (0.0, -1.0, 0.0)
            except Exception:
                pass
            return (0.0, 0.0, 1.0)

        def _v_dot(a, b):
            return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

        def _v_len(a):
            import math
            return math.sqrt(max(1e-12, a[0]*a[0] + a[1]*a[1] + a[2]*a[2]))

        def _is_parallel(nv, dirv, tol_deg: float = 2.0) -> bool:
            try:
                import math
                d = abs(_v_dot(nv, dirv) / (_v_len(nv) * _v_len(dirv)))
                d = max(0.0, min(1.0, d))
                ang = math.degrees(math.acos(d))
                return ang <= tol_deg
            except Exception:
                return False

        def _collect_edges_from_of(of_col, only_boundary: bool) -> Any:
            res = adsk.core.ObjectCollection.create()
            try:
                for i in range(getattr(of_col, "count", 0)):
                    ent = of_col.item(i)
                    # Faces → loops/edges
                    if hasattr(ent, "loops"):
                        try:
                            loops = ent.loops
                            for li in range(getattr(loops, "count", 0)):
                                lp = loops.item(li)
                                if only_boundary and hasattr(lp, "isOuter") and not lp.isOuter:
                                    continue
                                for ei in range(getattr(lp, "edges", None).count if hasattr(lp, "edges") else 0):
                                    try:
                                        e = lp.edges.item(ei)
                                        res.add(e)
                                    except Exception:
                                        pass
                        except Exception:
                            # Fallback to all edges of face
                            for e in getattr(ent, "edges", []) or []:
                                res.add(e)
                    # Bodies → all edges
                    elif hasattr(ent, "edges"):
                        for e in ent.edges:
                            res.add(e)
            except Exception:
                pass
            return res

        # created_by: use lineage tokens (session or persisted) deterministically
        fid_lookup = created_by or owner_feature
        if fid_lookup and (fid_lookup in self._lineage or fid_lookup in self._persisted_lineage):
            tokens = self._lineage.get(fid_lookup) or self._persisted_lineage.get(fid_lookup) or {}
            token_list = [t for t in (tokens.get(f"{kind}s") or []) if t]
            for t in sorted(dict.fromkeys(token_list)):
                add_entity_by_token(t)
            # If empty, fall back to bodies/faces of last body
            if col.count == 0 and kind == "face":
                faces = self._get_all_faces(root)
                for f in faces:
                    col.add(f)
            return col

        # created_by via attribute tags if lineage missing
        if fid_lookup and col.count == 0:
            tagged = self._find_entities_by_attr(root, kind, "csl_feat", fid_lookup)
            for i in range(tagged.count):
                col.add(tagged.item(i))
            if col.count > 0:
                return col

        # largest_by(axis): best-effort selection of largest area faces
        if kind == "face" and largest_by:
            try:
                faces = self._get_all_faces(root)
                max_f = None
                max_area = -1.0
                for f in faces:
                    try:
                        a = getattr(f, "area", 0.0)
                        if a > max_area:
                            max_area = a
                            max_f = f
                    except Exception:
                        continue
                if max_f:
                    col.add(max_f)
                    return col
            except Exception:
                pass

        # largest flag (faces → largest area; edges → longest length)
        if largest_flag:
            try:
                if kind == "face":
                    faces = self._get_all_faces(root)
                    max_f = None
                    max_area = -1.0
                    for f in faces:
                        try:
                            a = getattr(f, "area", 0.0)
                            if a > max_area:
                                max_area = a
                                max_f = f
                        except Exception:
                            continue
                    if max_f:
                        col.add(max_f)
                        return col
                elif kind == "edge":
                    bodies = self._all_bodies(root)
                    best = None
                    best_len = -1.0
                    for i in range(bodies.count):
                        for e in bodies.item(i).edges:
                            try:
                                ln = getattr(e, "length", 0.0)
                                if ln > best_len:
                                    best_len = ln
                                    best = e
                            except Exception:
                                continue
                    if best:
                        col.add(best)
                        return col
            except Exception:
                pass

        # pattern_instances: select from lineage for a given pattern feature deterministically
        if pat and isinstance(pat, dict):
            feature_id = pat.get("feature") or pat.get("id")
            if feature_id and feature_id in self._lineage:
                type_key = (pat.get("type") or kind or "face").lower()
                tokens = self._lineage[feature_id]
                token_list = [t for t in tokens.get(f"{type_key}s", []) if t]
                for t in sorted(dict.fromkeys(token_list)):
                    add_entity_by_token(t)
            return col

        # of (expand operator): e.g., edges of body/face selection; loop_edges via boundary flag
        if of_query and kind in ("edge", "faces", "face"):
            try:
                base_kind = "face" if kind == "edge" else ("body" if query_spec.get("of_kind") == "body" else "face")
                base = self._resolve_query(root, of_query, entity_type=base_kind)
                if kind == "edge":
                    return _collect_edges_from_of(base, boundary)
                if kind == "face":
                    # passthrough
                    for i in range(base.count):
                        col.add(base.item(i))
                    return col
            except Exception:
                pass

        # loop_edges(seed, boundary)
        if kind == "edge" and query_spec.get("loop_edges") or (kind == "loop_edges"):
            try:
                seed_q = query_spec.get("seed") if isinstance(query_spec.get("loop_edges"), dict) else query_spec.get("seed")
                seeds = self._resolve_query(root, seed_q or {"kind": "face"}, entity_type="face")
                return _collect_edges_from_of(seeds, boundary)
            except Exception:
                pass

        # by_material: filter by appearance/material name on faces/bodies
        if by_material:
            name = str(by_material)
            try:
                if kind == "body":
                    bodies = self._all_bodies(root)
                    for i in range(bodies.count):
                        b = bodies.item(i)
                        try:
                            ap = getattr(b, "appearance", None)
                            if ap and getattr(ap, "name", "") == name:
                                col.add(b)
                        except Exception:
                            pass
                    return col
                if kind == "face":
                    faces = self._get_all_faces(root)
                    for f in faces:
                        try:
                            ap = getattr(f, "appearance", None)
                            if ap and getattr(ap, "name", "") == name:
                                col.add(f)
                        except Exception:
                            pass
                    return col
            except Exception:
                pass

        # tangent_connected: flood neighboring faces tangent to seed
        if kind == "face" and tangent:
            try:
                seed_q = tangent.get("seed") if isinstance(tangent, dict) else None
                tdeg = float(tangent.get("tol_deg") or 5.0) if isinstance(tangent, dict) else 5.0
                import math
                t_rad = (tdeg / 180.0) * math.pi
                seeds = self._resolve_query(root, seed_q, entity_type="face") if seed_q else self._get_all_faces(root)
                visited = set()
                queue = []
                for i in range(seeds.count):
                    f = seeds.item(i)
                    queue.append(f)
                    visited.add(f.entityToken)
                while queue:
                    f = queue.pop(0)
                    col.add(f)
                    try:
                        # Explore adjacent faces via edges
                        for e in f.edges:
                            for of in e.faces:
                                if of.entityToken in visited:
                                    continue
                                try:
                                    ang = abs(f.getAngleTo(of)) if hasattr(f, "getAngleTo") else 0.0
                                except Exception:
                                    ang = 0.0
                                if ang <= t_rad:
                                    visited.add(of.entityToken)
                                    queue.append(of)
                    except Exception:
                        continue
                return col
            except Exception:
                return col

        # curvature≈ / radius≈ / area≈ filters with tolerance
        if kind == "face" and (curv_approx is not None or radius_approx is not None or area_approx is not None):
            try:
                faces = self._get_all_faces(root)
                targ = float(curv_approx or radius_approx or area_approx)
                tol_v = float(tol or 1e-3)
                for f in faces:
                    try:
                        val = None
                        surf = f.geometry
                        # Prefer radius when cylinder/sphere
                        if hasattr(surf, "radius"):
                            val = float(getattr(surf, "radius"))
                        elif area_approx is not None and hasattr(f, "area"):
                            val = float(f.area)
                        if val is not None and abs(val - targ) <= tol_v:
                            col.add(f)
                    except Exception:
                        continue
                return col
            except Exception:
                return col

        # by_material / appearance filter (substring)
        if by_material:
            try:
                name = str(by_material).lower()
                if kind == "body":
                    bodies = self._all_bodies(root)
                    for i in range(bodies.count):
                        b = bodies.item(i)
                        try:
                            app = getattr(b, "appearance", None)
                            if app and name in app.name.lower():
                                col.add(b)
                        except Exception:
                            pass
                else:
                    faces = self._get_all_faces(root)
                    for f in faces:
                        try:
                            app = getattr(f, "appearance", None) or getattr(f.body, "appearance", None)
                            if app and name in app.name.lower():
                                col.add(f)
                        except Exception:
                            pass
                return col
            except Exception:
                return col

        # by_tag: attribute-based selection (group: CSL, name: csl_tag == value)
        if by_tag:
            try:
                tagged = self._find_entities_by_attr(root, kind, "csl_tag", str(by_tag))
                for i in range(tagged.count):
                    col.add(tagged.item(i))
                return col
            except Exception:
                return col

        # by_id / direct tokens
        if by_id:
            try:
                tokens = by_id if isinstance(by_id, list) else [by_id]
                for t in tokens:
                    if isinstance(t, str):
                        add_entity_by_token(t)
                return col
            except Exception:
                return col

        # faces_parallel / normal== filters (planar faces)
        if kind == "face" and (faces_parallel is not None or normal_eq is not None):
            try:
                dirv = _axis_from_str((faces_parallel.get("direction") if isinstance(faces_parallel, dict) else faces_parallel) or normal_eq)
                tol_deg = float((faces_parallel.get("tol_deg") if isinstance(faces_parallel, dict) else query_spec.get("tol_deg")) or 2.0)
                faces = self._get_all_faces(root)
                for f in faces:
                    try:
                        geom = getattr(f, "geometry", None)
                        n = None
                        if geom and hasattr(geom, "normal"):
                            nvec = geom.normal
                            n = (float(getattr(nvec, "x", 0.0)), float(getattr(nvec, "y", 0.0)), float(getattr(nvec, "z", 0.0)))
                        if n and _is_parallel(n, dirv, tol_deg):
                            col.add(f)
                    except Exception:
                        continue
                return col
            except Exception:
                return col

        # cylindrical_faces with optional diameter/radius and axis≈
        if kind in ("face", "cylindrical_faces") and (cyl_kind or query_spec.get("cylindrical") or diam_approx is not None or radius_approx is not None or axis_approx is not None):
            try:
                faces = self._get_all_faces(root)
                tol_v = float(tol or 1e-3)
                axis_v = _axis_from_str(axis_approx) if axis_approx else None
                for f in faces:
                    try:
                        surf = getattr(f, "geometry", None)
                        if not surf or not hasattr(surf, "radius"):
                            continue
                        ok = True
                        if radius_approx is not None:
                            ok = ok and abs(float(getattr(surf, "radius")) - float(radius_approx)) <= tol_v
                        if diam_approx is not None:
                            ok = ok and abs((2.0 * float(getattr(surf, "radius"))) - float(diam_approx)) <= tol_v
                        if axis_v is not None:
                            # Try surf.axis or surf.direction
                            ax = None
                            for attr in ("axis", "direction", "axisVector"):
                                try:
                                    av = getattr(surf, attr)
                                    ax = (float(getattr(av, "x", 0.0)), float(getattr(av, "y", 0.0)), float(getattr(av, "z", 0.0)))
                                    break
                                except Exception:
                                    ax = None
                            if ax is None or not _is_parallel(ax, axis_v, float(query_spec.get("tol_deg") or 5.0)):
                                ok = False
                        if ok:
                            col.add(f)
                    except Exception:
                        continue
                return col
            except Exception:
                return col

        # owner_body: map entity/entities to their body
        if kind == "body" and query_spec.get("owner_body"):
            try:
                src_q = query_spec.get("owner_body")
                src = self._resolve_query(root, src_q, entity_type="face") if isinstance(src_q, dict) else None
                seen = set()
                if src:
                    for i in range(src.count):
                        try:
                            b = src.item(i).body
                            if b and b.entityToken not in seen:
                                seen.add(b.entityToken)
                                col.add(b)
                        except Exception:
                            continue
                return col
            except Exception:
                return col

        # Fallback: return nothing
        return col

    def _get_all_faces(self, root):
        # Deterministic face ordering: sort by entityToken when available
        import adsk.core  # type: ignore
        col = adsk.core.ObjectCollection.create()  # type: ignore
        try:
            tmp: List[Any] = []
            bodies = self._all_bodies(root)
            for i in range(getattr(bodies, "count", 0)):
                b = bodies.item(i)
                for f in getattr(b, "faces", []) or []:
                    try:
                        tok = getattr(f, "entityToken", None)
                        if tok:
                            tmp.append((str(tok), f))
                        else:
                            tmp.append((f"z_{i:06d}", f))
                    except Exception:
                        tmp.append((f"z_{i:06d}", f))
            for _, face in sorted(tmp, key=lambda x: x[0]):
                col.add(face)
            return col
        except Exception:
            # Fallback to unsorted enumeration
            bodies = self._all_bodies(root)
            for i in range(bodies.count):
                b = bodies.item(i)
                for f in b.faces:
                    col.add(f)
            return col

    def _diag(self, code: str, *, where: str, message: str, hint: Optional[str] = None, data: Optional[Dict[str, Any]] = None) -> None:
        entry: Dict[str, Any] = {"code": code, "where": where, "message": message}
        if hint:
            entry["hint"] = hint
        if data is not None:
            entry["data"] = data
        # Auto-hints for common classes
        try:
            if code.startswith("E12") and not hint:
                if where in ("sketch", "query"):
                    entry["hint"] = "Add created_by/owner_feature== and tolerances (tol/tol_deg) to disambiguate."
                elif where in ("loft", "sweep"):
                    entry["hint"] = "Specify continuity/orientation or add rails/guide to reduce ambiguity."
            if code.startswith("E23") and not entry.get("hint"):
                entry["hint"] = "Strengthen selection via queries (created_by, pattern_instances, by_material) or apply tags."
        except Exception:
            pass
        self._errors.append(entry)

    def get_diagnostics(self) -> Dict[str, Any]:
        return {"errors": list(self._errors)}

    # ------------------------
    # APS Helpers
    # ------------------------
    def _aps_token(self) -> Optional[str]:
        # Token caching with naive expiry buffer
        now = time.time()
        cached = self.session_config.get("_aps_token_cache")
        if isinstance(cached, dict):
            tok = cached.get("token")
            exp = cached.get("expires_at", 0)
            if tok and now < (exp - 60):  # 60s buffer
                return tok
        try:
            import requests  # type: ignore
            cid = self.session_config.get("aps_client_id")
            csec = self.session_config.get("aps_client_secret")
            scopes = self.session_config.get("aps_scopes") or "data:read data:write"
            if not cid or not csec:
                return None
            url = "https://developer.api.autodesk.com/authentication/v2/token"
            data = {"grant_type":"client_credentials","client_id":cid,"client_secret":csec,"scope":scopes}
            resp = requests.post(url, data=data, timeout=20)
            if resp.status_code != 200:
                self._diag("E3101", where="aps", message=f"Auth failed: {resp.status_code}")
                return None
            js = resp.json()
            tok = js.get("access_token")
            expires_in = int(js.get("expires_in") or 1800)
            self.session_config["_aps_token_cache"] = {"token": tok, "expires_at": now + expires_in}
            return tok
        except Exception:
            return None

    def _http_with_retries(self, method: str, url: str, *, headers: Dict[str, str] | None = None, json: Any | None = None, data: Any | None = None, timeout: int = 30, max_attempts: int = 4, backoff_base: float = 0.5) -> Optional[Any]:
        try:
            import requests  # type: ignore
        except Exception:
            return None
        attempts = 0
        while attempts < max_attempts:
            attempts += 1
            try:
                resp = requests.request(method, url, headers=headers, json=json, data=data, timeout=timeout)
                if resp.status_code >= 500 and attempts < max_attempts:
                    time.sleep(backoff_base * (2 ** (attempts - 1)))
                    continue
                return resp
            except Exception:
                if attempts >= max_attempts:
                    return None
                time.sleep(backoff_base * (2 ** (attempts - 1)))
        return None

    def _aps_ensure_bucket(self, token: str, bucket: str) -> None:
        try:
            hdr = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
            base = "https://developer.api.autodesk.com/oss/v2/buckets"
            payload = {"bucketKey": bucket, "policyKey": "transient"}
            resp = self._http_with_retries("POST", base, headers=hdr, json=payload, timeout=20)
            if not resp or resp.status_code not in (200, 409):
                self._diag("E3102", where="aps", message=f"Bucket ensure failed: {getattr(resp, 'status_code', 'no_resp')}")
        except Exception:
            pass

    def _aps_upload(self, file_path: str) -> None:
        token = self._aps_token()
        bucket = self.session_config.get("aps_bucket")
        if not token or not bucket:
            return
        self._aps_ensure_bucket(token, bucket)
        try:
            hdr = {"Authorization": f"Bearer {token}", "Content-Type": "application/octet-stream"}
            import os as _os
            name = _os.path.basename(file_path)
            with open(file_path, "rb") as f:
                data = f.read()
            url = f"https://developer.api.autodesk.com/oss/v2/buckets/{bucket}/objects/{name}"
            resp = self._http_with_retries("PUT", url, headers=hdr, data=data, timeout=60)
            if not resp or resp.status_code not in (200, 201):
                self._diag("E3103", where="aps", message=f"Upload failed: {getattr(resp, 'status_code', 'no_resp')}")
        except Exception:
            pass

    # ------------------------
    # APS Orchestration (local/hosted agent compatible)
    # ------------------------
    def orchestrate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """Run an orchestration plan locally and upload artifacts if APS is configured.

        Plan schema (example):
        {
          "export": [ { "format":"STL", "path":"out/part.stl", "resolution":"high" } ],
          "thumbnail": [ { "path":"out/preview.png", "view":"iso", "style":"shaded" } ],
          "aps_bucket": "csl-artifacts-<env>"
        }

        Returns { "ok": bool, "uploaded": [paths], "errors": [...] }
        """
        results: Dict[str, Any] = {"ok": True, "uploaded": [], "errors": [], "telemetry": {}}
        t0 = time.time()
        # Allow overriding bucket from plan
        if plan.get("aps_bucket"):
            self.session_config["aps_bucket"] = plan.get("aps_bucket")
        # Execute steps with simple retries
        def _try(fn, arg, name: str) -> None:
            for attempt in range(2):
                try:
                    fn(arg)
                    return
                except Exception as ex:
                    if attempt == 1:
                        results["ok"] = False
                        results["errors"].append({"step": name, "error": str(ex)})
                        try:
                            self._diag("E3201", where="orchestrate", message=f"{name} failed: {ex}")
                        except Exception:
                            pass
        if plan.get("export"):
            t = time.time()
            _try(self.export, plan.get("export"), "export")
            results["telemetry"]["export_ms"] = int((time.time() - t) * 1000)
        if plan.get("thumbnail"):
            t = time.time()
            _try(self.thumbnail, plan.get("thumbnail"), "thumbnail")
            results["telemetry"]["thumbnail_ms"] = int((time.time() - t) * 1000)
        # If APS configured, report uploads were attempted by hooks
        try:
            if self.session_config.get("aps_bucket"):
                # We cannot know remote URNs here without OSS response; report local paths
                for op in (plan.get("export") or []):
                    if isinstance(op, dict) and op.get("path"):
                        results["uploaded"].append(op.get("path"))
                for op in (plan.get("thumbnail") or []):
                    if isinstance(op, dict) and op.get("path"):
                        results["uploaded"].append(op.get("path"))
        except Exception:
            pass
        results["telemetry"]["total_ms"] = int((time.time() - t0) * 1000)
        return results

    # ------------------------
    # Persistence & Attributes for Stable IDs
    # ------------------------
    def _lineage_path(self) -> str:
        return str(self.session_config.get("lineage_path") or os.path.abspath("csl_lineage.json"))

    def _load_persisted_lineage(self) -> None:
        path = self._lineage_path()
        try:
            if os.path.exists(path):
                import json as _json
                with open(path, "r", encoding="utf-8") as f:
                    self._persisted_lineage = _json.load(f)
            # Attempt reconciliation in Fusion: refresh tokens by scanning attributes
            try:
                app, ui, design = self._ensure_design()
                root = design.rootComponent
                # For each feature id, find bodies/faces/edges tagged with CSL:csl_feat
                for fid, entry in list(self._persisted_lineage.items()):
                    refreshed = {"bodies": [], "faces": [], "edges": []}
                    try:
                        tagged_b = self._find_entities_by_attr(root, "body", "csl_feat", fid)
                        for i in range(tagged_b.count):
                            b = tagged_b.item(i)
                            refreshed["bodies"].append(b.entityToken)
                        tagged_f = self._find_entities_by_attr(root, "face", "csl_feat", fid)
                        for i in range(tagged_f.count):
                            f = tagged_f.item(i)
                            refreshed["faces"].append(f.entityToken)
                        tagged_e = self._find_entities_by_attr(root, "edge", "csl_feat", fid)
                        for i in range(tagged_e.count):
                            e = tagged_e.item(i)
                            refreshed["edges"].append(e.entityToken)
                        # Normalize and replace persisted tokens with refreshed ones when found; else normalize existing
                        if any(len(v) > 0 for v in refreshed.values()):
                            for k in ("bodies", "faces", "edges"):
                                cur = [t for t in refreshed.get(k, []) if t]
                                refreshed[k] = sorted(list(dict.fromkeys(cur)))
                            self._persisted_lineage[fid] = refreshed
                        else:
                            for k in ("bodies", "faces", "edges"):
                                cur = [t for t in self._persisted_lineage.get(fid, {}).get(k, []) if t]
                                self._persisted_lineage[fid][k] = sorted(list(dict.fromkeys(cur)))
                    except Exception:
                        continue
            except Exception:
                pass
        except Exception:
            self._persisted_lineage = {}

    def _save_persisted_lineage(self) -> None:
        try:
            import json as _json
            with open(self._lineage_path(), "w", encoding="utf-8") as f:
                _json.dump(self._persisted_lineage, f)
        except Exception:
            pass

    def _refresh_lineage_from_attributes(self, root) -> None:
        """Populate in-memory lineage by scanning CSL attributes on entities.

        This helps reconcile selections after rename/reorder/regenerate and across sessions.
        """
        try:
            fids: Dict[str, Dict[str, List[str]]] = {}
            # Bodies
            bodies = self._all_bodies(root)
            for i in range(getattr(bodies, "count", 0)):
                b = bodies.item(i)
                try:
                    attrs = getattr(b, "attributes", None)
                    a = attrs.itemByName("CSL", "csl_feat") if attrs else None
                    if a:
                        fid = str(a.value)
                        fids.setdefault(fid, {"bodies": [], "faces": [], "edges": []})
                        fids[fid]["bodies"].append(b.entityToken)
                        # Faces and edges for this body
                        for f in getattr(b, "faces", []) or []:
                            try:
                                fids[fid]["faces"].append(f.entityToken)
                            except Exception:
                                pass
                        for e in getattr(b, "edges", []) or []:
                            try:
                                fids[fid]["edges"].append(e.entityToken)
                            except Exception:
                                pass
                except Exception:
                    continue
            # Normalize and merge into in-memory lineage
            for fid, tokens in fids.items():
                for k in ("bodies", "faces", "edges"):
                    lst = [t for t in tokens.get(k, []) if t]
                    tokens[k] = sorted(list(dict.fromkeys(lst)))
                self._lineage[fid] = tokens
        except Exception:
            pass

    def _tag_attribute(self, entity: Any, name: str, value: str) -> None:
        try:
            # Attributes: group "CSL"
            attrs = getattr(entity, "attributes", None)
            if attrs:
                # Remove any previous value to avoid duplicates
                try:
                    old = attrs.itemByName("CSL", name)
                    if old:
                        old.deleteMe()
                except Exception:
                    pass
                attrs.add("CSL", name, str(value))
        except Exception:
            pass

    def _find_entities_by_attr(self, root, kind: str, name: str, value: str):
        import adsk.core  # type: ignore
        col = adsk.core.ObjectCollection.create()
        try:
            if kind == "body":
                bodies = self._all_bodies(root)
                for i in range(bodies.count):
                    b = bodies.item(i)
                    try:
                        attrs = getattr(b, "attributes", None)
                        a = attrs.itemByName("CSL", name) if attrs else None
                        if a and a.value == value:
                            col.add(b)
                    except Exception:
                        pass
            elif kind == "face":
                faces = self._get_all_faces(root)
                for f in faces:
                    try:
                        attrs = getattr(f, "attributes", None)
                        a = attrs.itemByName("CSL", name) if attrs else None
                        if a and a.value == value:
                            col.add(f)
                    except Exception:
                        pass
            elif kind == "edge":
                bodies = self._all_bodies(root)
                for i in range(bodies.count):
                    b = bodies.item(i)
                    for e in b.edges:
                        try:
                            attrs = getattr(e, "attributes", None)
                            a = attrs.itemByName("CSL", name) if attrs else None
                            if a and a.value == value:
                                col.add(e)
                        except Exception:
                            pass
        except Exception:
            pass
        return col

    def _apply_materials_and_pmi(self, csl_ir: Dict[str, Any]) -> None:
        try:
            import adsk.core  # type: ignore
            import adsk.fusion  # type: ignore
            app, ui, design = self._ensure_design()
            root_comp = design.rootComponent

            # Materials: library refs + overrides (best-effort)
            mats = csl_ir.get("materials") or []
            if isinstance(mats, list):
                # Cache library handles once
                material_libs = []
                appearance_libs = []
                try:
                    for i in range(app.materialLibraries.count):
                        material_libs.append(app.materialLibraries.item(i))
                except Exception:
                    material_libs = []
                try:
                    for i in range(app.appearanceLibraries.count):
                        appearance_libs.append(app.appearanceLibraries.item(i))
                except Exception:
                    appearance_libs = []

                for m in mats:
                    if not isinstance(m, dict):
                        continue

                    # Find material by ref: "Library:Material" or just name
                    target_material = None
                    ref = m.get("ref") or m.get("name")
                    if ref:
                        ref_lib = None
                        ref_name = str(ref)
                        if ":" in ref_name:
                            parts = ref_name.split(":", 1)
                            ref_lib = parts[0].strip()
                            ref_name = parts[1].strip()
                        # Document materials first
                        try:
                            target_material = design.materials.itemByName(ref_name)
                        except Exception:
                            target_material = None
                        if not target_material:
                            try:
                                for lib in material_libs:
                                    if ref_lib and getattr(lib, "name", "") != ref_lib:
                                        continue
                                    mm = lib.materials.itemByName(ref_name)
                                    if mm:
                                        target_material = mm
                                        break
                            except Exception:
                                target_material = None
                    if target_material:
                        try:
                            # Apply to specific targets if provided; else all bodies
                            targets: List[Any] = []
                            try:
                                tq = m.get("targets_query") or m.get("target_query")
                                if tq:
                                    tcol = self._resolve_query(root_comp, tq, entity_type="body")
                                    if tcol and tcol.count > 0:
                                        for i in range(tcol.count):
                                            targets.append(tcol.item(i))
                            except Exception:
                                targets = []
                            if not targets:
                                for b in root_comp.bRepBodies:
                                    targets.append(b)
                            for b in targets:
                                try:
                                    b.material = target_material
                                except Exception:
                                    pass
                        except Exception:
                            pass

                    # Appearance override by name or color
                    overrides = m.get("overrides") or {}
                    ap = m.get("appearance") or m.get("color") or overrides.get("color")
                    if ap:
                        appearance_obj = None
                        is_hex = False
                        try:
                            s = str(ap).lstrip('#')
                            _ = int(s, 16)
                            is_hex = True
                        except Exception:
                            is_hex = False
                        try:
                            for lib in appearance_libs:
                                obj = lib.appearances.itemByName(str(ap))
                                if obj:
                                    appearance_obj = obj
                                    break
                        except Exception:
                            appearance_obj = None
                        if appearance_obj:
                            try:
                                targets: List[Any] = []
                                tq2 = m.get("targets_query") or m.get("target_query")
                                if tq2:
                                    try:
                                        tcol = self._resolve_query(root_comp, tq2, entity_type="body")
                                        if tcol and tcol.count > 0:
                                            for i in range(tcol.count):
                                                targets.append(tcol.item(i))
                                    except Exception:
                                        targets = []
                                if not targets:
                                    for b in root_comp.bRepBodies:
                                        targets.append(b)
                                for b in targets:
                                    try:
                                        b.appearance = appearance_obj
                                    except Exception:
                                        pass
                            except Exception:
                                pass
                        elif is_hex:
                            # Cannot synthesize arbitrary appearance reliably; emit diagnostic
                            try:
                                self._diag("E2511", where="materials", message=f"Hex color '{ap}' requested; no matching appearance found; leaving default")
                            except Exception:
                                pass

                    # Density override diagnostic (Fusion generally doesn't allow direct override)
                    if overrides.get("density") is not None:
                        try:
                            dens_val = str(overrides.get("density"))
                            self._diag("E2510", where="materials", message=f"Density override '{dens_val}' not settable in this API; using library density")
                        except Exception:
                            pass

            # PMI: notes placed on face or named construction plane, with rotation and size
            pmi_list = csl_ir.get("pmi") or []
            if isinstance(pmi_list, list) and len(pmi_list) > 0:
                def _plane_by_name(name: str):
                    n = (name or "").lower()
                    if "xz" in n:
                        return root_comp.xZConstructionPlane
                    if "yz" in n:
                        return root_comp.yZConstructionPlane
                    return root_comp.xYConstructionPlane

                for note in pmi_list:
                    if not isinstance(note, dict) or not note.get("note"):
                        continue
                    try:
                        txt = str(note.get("note"))
                        height_mm = self._parse_length_mm(note.get("height") or "5") or 5.0
                        height = height_mm / 10.0
                        # angle in degrees (number or string), default 0
                        try:
                            rot_deg = float(note.get("angle") or 0.0)
                        except Exception:
                            rot_deg = 0.0
                        pos_str = note.get("at") or "0,0"
                        pt = self._parse_point(pos_str) or [0.0, 0.0]

                        # Face placement takes precedence over plane
                        sketch = None
                        face_target = None
                        if note.get("on"):
                            try:
                                fcol = self._resolve_query(root_comp, note.get("on"), entity_type="face")
                                if fcol and fcol.count > 0:
                                    face_target = fcol.item(0)
                            except Exception:
                                face_target = None
                        if face_target is not None:
                            sketch = root_comp.sketches.add(face_target)
                        else:
                            plane_name = note.get("plane") or "world.xy"
                            sketch = root_comp.sketches.add(_plane_by_name(plane_name))

                        ti = sketch.sketchTexts.createInput(txt, height)
                        p = adsk.core.Point3D.create(pt[0], pt[1], 0)
                        radians = (rot_deg/180.0) * 3.141592653589793
                        ti.setAsMultiLine(p, radians, adsk.core.HorizontalAlignments.LeftHorizontalAlignment, adsk.core.VerticalAlignments.TopVerticalAlignment, 0.0)
                        sketch.sketchTexts.add(ti)
                        # Optional: draw a simple rectangular frame
                        try:
                            if bool(note.get("frame")):
                                lines = sketch.sketchCurves.sketchLines
                                w = float(note.get("frame_w") or 1.2) * height
                                h = float(note.get("frame_h") or 0.6) * height
                                x0, y0 = pt[0], pt[1]
                                p0 = adsk.core.Point3D.create(x0, y0, 0)
                                p1 = adsk.core.Point3D.create(x0 + w, y0, 0)
                                p2 = adsk.core.Point3D.create(x0 + w, y0 - h, 0)
                                p3 = adsk.core.Point3D.create(x0, y0 - h, 0)
                                lines.addByTwoPoints(p0, p1); lines.addByTwoPoints(p1, p2); lines.addByTwoPoints(p2, p3); lines.addByTwoPoints(p3, p0)
                        except Exception:
                            pass
                    except Exception:
                        # Best-effort: ignore any one PMI failure without stopping others
                        pass

            # Minimal GD&T: place rectangular frame text; best-effort mapping
            gdt_list = csl_ir.get("gdt") or csl_ir.get("gd&t") or []
            if isinstance(gdt_list, list) and len(gdt_list) > 0:
                for frame in gdt_list:
                    if not isinstance(frame, dict):
                        continue
                    try:
                        # Build frame string like |⟂|A|0.1(M)|
                        label = str(frame.get("label") or frame.get("feature_control_frame") or "")
                        if not label:
                            comps = []
                            sym = frame.get("symbol") or frame.get("feature") or ""
                            datum = frame.get("datum") or frame.get("primary") or ""
                            tol = frame.get("tolerance") or frame.get("tol") or ""
                            mod = frame.get("modifier") or frame.get("mat_mod") or ""
                            if sym:
                                comps.append(str(sym))
                            if datum:
                                comps.append(str(datum))
                            if tol:
                                if mod:
                                    comps.append(f"{tol}({mod})")
                                else:
                                    comps.append(str(tol))
                            if comps:
                                label = "|" + "|".join(comps) + "|"
                        if not label:
                            continue
                        # Use top-level XY plane unless a face is provided via 'on'
                        face_target = None
                        plane = root_comp.xYConstructionPlane
                        try:
                            if frame.get("on"):
                                fcol = self._resolve_query(root_comp, frame.get("on"), entity_type="face")
                                if fcol and fcol.count > 0:
                                    face_target = fcol.item(0)
                            if frame.get("plane") and face_target is None:
                                n = str(frame.get("plane")).lower()
                                if "xz" in n:
                                    plane = root_comp.xZConstructionPlane
                                elif "yz" in n:
                                    plane = root_comp.yZConstructionPlane
                        except Exception:
                            pass
                        sk = root_comp.sketches.add(face_target or plane)
                        h_mm = self._parse_length_mm(frame.get("height") or "4") or 4.0
                        pos = self._parse_point(frame.get("at") or "0,0") or [0.0, 0.0]
                        inp = sk.sketchTexts.createInput(label, h_mm / 10.0)
                        p = adsk.core.Point3D.create(pos[0], pos[1], 0)
                        inp.setAsMultiLine(p, 0.0, adsk.core.HorizontalAlignments.LeftHorizontalAlignment, adsk.core.VerticalAlignments.TopVerticalAlignment, 0.0)
                        sk.sketchTexts.add(inp)
                        # Optional datum callouts linked to frame (visual only)
                        try:
                            datums = frame.get("datums") or []
                            if isinstance(datums, list) and len(datums) > 0:
                                lines = sk.sketchCurves.sketchLines
                                for i, d in enumerate(datums):
                                    if not isinstance(d, dict):
                                        continue
                                    name = str(d.get("name") or d.get("id") or "D")
                                    dx = float(d.get("dx") or 0.0)
                                    dy = float(d.get("dy") or -((i+1) * (h_mm / 10.0)))
                                    pt2 = adsk.core.Point3D.create(pos[0] + dx, pos[1] + dy, 0)
                                    ti2 = sk.sketchTexts.createInput(f"⟂ {name}", h_mm / 10.0)
                                    ti2.setAsSingleLine(pt2, 0.0, adsk.core.HorizontalAlignments.LeftHorizontalAlignment, adsk.core.VerticalAlignments.MiddleVerticalAlignment)
                                    sk.sketchTexts.add(ti2)
                                    try:
                                        p1 = adsk.core.Point3D.create(pos[0], pos[1], 0)
                                        lines.addByTwoPoints(p1, pt2)
                                    except Exception:
                                        pass
                        except Exception:
                            pass
                    except Exception:
                        continue
        except Exception:
            # Entire materials/PMI block is best-effort; ignore in headless or API-limited environments
            pass

    def _apply_variable_fillet(self, root, fil_feats, grp: Dict[str, Any]):
        """Attempt variable radius or setback fillet using Fusion API when available.

        grp may contain:
          - q / edges_query: target edges
          - points: [{t:0..1, r:"mm"}, ...] control points along edge
          - setbacks: [{vertex_query:..., d:"mm"}, ...] per-vertex setbacks
        """
        import adsk.core  # type: ignore
        # Resolve edges
        edges = None
        try:
            qg = grp.get("q") or grp.get("edges_query") or grp.get("edges")
            if qg:
                edges = self._resolve_query(root, qg, entity_type="edge")
        except Exception:
            edges = None
        if not edges or edges.count == 0:
            return None
        # Variable radius path
        if grp.get("points") and hasattr(fil_feats, "createVariableRadiusFilletDefinition"):
            pts = grp.get("points")
            try:
                # Build arrays for radii and parameters if API expects them; fallback to first/last
                rads = []
                params = []
                for p in pts:
                    if not isinstance(p, dict):
                        continue
                    r_mm = self._parse_length_mm(p.get("r") or p.get("radius"))
                    t = p.get("t")
                    if r_mm is not None and t is not None:
                        rads.append(adsk.core.ValueInput.createByReal((r_mm/10.0)))
                        params.append(float(t))
                if len(rads) >= 2 and len(params) == len(rads):
                    vdef = fil_feats.createVariableRadiusFilletDefinition(edges, rads, params, False)
                    return fil_feats.add(vdef)
            except Exception:
                self._diag("E2322", where="fillet", message="Variable fillet API not available or failed; applied constant groups.")
                return None
        # Setbacks at vertices (best-effort)
        if grp.get("setbacks") and hasattr(fil_feats, "createSetbackFilletDefinition"):
            try:
                sdef = fil_feats.createSetbackFilletDefinition(edges)
                for sb in (grp.get("setbacks") or []):
                    if not isinstance(sb, dict):
                        continue
                    d_mm = self._parse_length_mm(sb.get("d") or sb.get("distance"))
                    vq = sb.get("vertex_query")
                    if d_mm is None or not vq:
                        continue
                    vcol = self._resolve_query(root, vq, entity_type="vertex")
                    if vcol and vcol.count > 0:
                        try:
                            sdef.setSetbackDistance(vcol.item(0), adsk.core.ValueInput.createByReal(d_mm/10.0))
                        except Exception:
                            pass
                return fil_feats.add(sdef)
            except Exception:
                self._diag("E2323", where="fillet", message="Setback fillet not supported by this Fusion version.")
                return None
        # Nothing applied
        return None

    def _apply_variable_chamfer(self, root, chf, grp: Dict[str, Any]):
        """Attempt variable chamfer distances if API supports it.

        grp may contain:
          - q / edges_query: edges
          - points: [{t:0..1, d:"mm"}]
        """
        import adsk.core  # type: ignore
        edges = None
        try:
            qg = grp.get("q") or grp.get("edges_query") or grp.get("edges")
            if qg:
                edges = self._resolve_query(root, qg, entity_type="edge")
        except Exception:
            edges = None
        if not edges or edges.count == 0:
            return None
        if grp.get("points") and hasattr(chf, "createVariableDistanceChamferDefinition"):
            try:
                ds = []
                ts = []
                for p in grp.get("points"):
                    if not isinstance(p, dict):
                        continue
                    d_mm = self._parse_length_mm(p.get("d") or p.get("distance"))
                    t = p.get("t")
                    if d_mm is not None and t is not None:
                        ds.append(adsk.core.ValueInput.createByReal(d_mm/10.0))
                        ts.append(float(t))
                if len(ds) >= 2 and len(ts) == len(ds):
                    vdef = chf.createVariableDistanceChamferDefinition(edges, ds, ts, False)
                    return chf.add(vdef)
            except Exception:
                self._diag("E2324", where="chamfer", message="Variable chamfer API not available or failed; applied constant groups.")
                return None
        return None


    def _apply_per_instance_pattern(self, pattern_obj: Any, instances: List[Dict[str, Any]]) -> None:
        """Best-effort native per-instance adjustment if API exposes pattern elements.

        On some versions, pattern features expose patternElements; we can tweak transforms.
        Fallback is already handled via moveFeatures.
        """
        try:
            elements = getattr(pattern_obj, "patternElements", None)
            if not elements or not hasattr(elements, "count"):
                return
            count = min(elements.count, len(instances))
            import adsk.core  # type: ignore
            for i in range(count):
                inst = instances[i]
                el = elements.item(i)
                # Apply a simple additional transform (translation + optional rotation around Z)
                try:
                    dx = float((self._parse_length_mm(inst.get("dx") or "0") or 0.0) / 10.0)
                    dy = float((self._parse_length_mm(inst.get("dy") or "0") or 0.0) / 10.0)
                    dz = float((self._parse_length_mm(inst.get("dz") or "0") or 0.0) / 10.0)
                    angle_deg = None
                    try:
                        angle_deg = float(self._parse_length_mm(str(inst.get("angle"))) or 0.0)
                    except Exception:
                        angle_deg = None
                    trans = adsk.core.Matrix3D.create()
                    if angle_deg is not None and angle_deg != 0.0:
                        theta = (angle_deg / 180.0) * 3.141592653589793
                        rot = adsk.core.Matrix3D.create()
                        rot.setToRotation(theta, adsk.core.Vector3D.create(0, 0, 1), adsk.core.Point3D.create(0, 0, 0))
                        trans.transformBy(rot)
                    vec = adsk.core.Vector3D.create(dx, dy, dz)
                    trans.translation = vec
                    # Common properties that may exist: elementTransform or setTransform
                    if hasattr(el, "elementTransform"):
                        try:
                            el.elementTransform = trans
                        except Exception:
                            pass
                    if hasattr(el, "setTransform"):
                        try:
                            el.setTransform(trans)
                        except Exception:
                            pass
                except Exception:
                    continue
        except Exception:
            return

