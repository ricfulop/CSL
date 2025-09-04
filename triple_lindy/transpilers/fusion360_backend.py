"""Fusion 360 Backend Adapter (stub)

Implements the minimal BackendAdapter shape for Fusion-first development.
If Fusion's `adsk` modules are unavailable, methods will no-op or print guidance.
"""
from __future__ import annotations

import os
import re
from typing import Dict, List, Any, Optional


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
        return {
            "csl": "1.1",
            "backend": "fusion",
            "supports": {
                "brep": True,
                "mesh": True,
                "params": True,
                "queries": True,
                "features": {
                    "extrude": True,
                    "fillet": True,
                    "hole": True,
                    "loft": True,
                    "shell": True,
                    "draft": True,
                    "pattern": ["linear", "circular", "rect"],
                    "boolean": ["union", "subtract", "intersect"],
                    "thread_cosmetic": True,
                    "thread_modeled": True,
                },
                "export": ["STEP", "STL", "IGES", "3MF", "OBJ"],
                "thumbnail": {"enabled": True, "views": ["iso", "top", "front", "right"], "styles": ["shaded", "wireframe"]},
            },
            "queries": {
                "predicates_supported": ["created_by", "largest_by"],
                "stable_id": "entityToken (session-scoped)",
                "lineage": "feature->(bodies,faces,edges) tokens",
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
        # Default lineage path
        self.session_config.setdefault("lineage_path", os.path.abspath(self.session_config.get("lineage_path") or "csl_lineage.json"))
        # Load persisted lineage
        try:
            self._load_persisted_lineage()
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
        mapping: Dict[str, str] = {}
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
            for sk in csl_ir.get("sketches", []) or []:
                if not isinstance(sk, dict):
                    continue
                sk_id = sk.get("id", "sketch")
                plane_name = (sk.get("plane") or "world.xy").lower()
                plane = root.sketches.add(plane)
                ent_objects: Dict[str, Any] = {}
                # Entities
                for ent in sk.get("entities", []) or []:
                    kind = (ent.get("kind") or "").lower()
                    if kind == "rect":
                        p1 = self._parse_point(ent.get("p1"))
                        p2 = self._parse_point(ent.get("p2"))
                        if p1 and p2:
                            rect_obj = sketch.sketchCurves.sketchLines.addTwoPointRectangle(
                                adsk.core.Point3D.create(p1[0], p1[1], 0),
                                adsk.core.Point3D.create(p2[0], p2[1], 0),
                            )
                            if ent.get("id") is not None:
                                ent_objects[ent.get("id")] = rect_obj
                    elif kind == "circle":
                        c = self._parse_point(ent.get("center"))
                        d_mm = self._parse_length_mm(ent.get("d"))
                        if c and d_mm:
                            r_cm = (d_mm / 2.0) / 10.0
                            circle_obj = sketch.sketchCurves.sketchCircles.addByCenterRadius(
                                adsk.core.Point3D.create(c[0], c[1], 0), r_cm
                            )
                            if ent.get("id") is not None:
                                ent_objects[ent.get("id")] = circle_obj
                    elif kind == "point":
                        at = self._parse_point(ent.get("at"))
                        if at:
                            pt_obj = sketch.sketchPoints.add(adsk.core.Point3D.create(at[0], at[1], 0))
                            if ent.get("id") is not None:
                                ent_objects[ent.get("id")] = pt_obj
                    elif kind == "line":
                        p1 = self._parse_point(ent.get("p1"))
                        p2 = self._parse_point(ent.get("p2"))
                        if p1 and p2:
                            line_obj = sketch.sketchCurves.sketchLines.addByTwoPoints(
                                adsk.core.Point3D.create(p1[0], p1[1], 0),
                                adsk.core.Point3D.create(p2[0], p2[1], 0),
                            )
                            if ent.get("id") is not None:
                                ent_objects[ent.get("id")] = line_obj
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
                                if ent.get("id") is not None:
                                    ent_objects[ent.get("id")] = arc_obj
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
                                if ent.get("id") is not None:
                                    ent_objects[ent.get("id")] = ell_obj
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
                        elif ckind == "midpoint" and a and b:
                            cons.addMidPoint(a, b)
                        elif ckind in ("lock", "fix") and a:
                            cons.addFixed(a)
                        elif ckind == "distance" and a and b:
                            d_mm = self._parse_length_mm(cst.get("value") or cst.get("d") or cst.get("distance")) or 0.0
                            dims.addDistanceDimension(a, b, adsk.core.Point3D.create(0, 0, 0))
                        elif ckind == "angle" and a and b:
                            ang_deg = self._parse_length_mm(cst.get("value") or cst.get("angle")) or 0.0
                            dims.addAngleDimension(a, b, adsk.core.Point3D.create(0, 0, 0))
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
                            else:
                                rd = dims.addRadialDimension(target, adsk.core.Point3D.create(0, 0, 0))
                                try:
                                    rd.parameter.value = (val_mm / 10.0)
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
                        elif dkind == "angle" and target is not None and isinstance(dim.get("to"), str):
                            t2 = ent_objects.get(dim.get("to"))
                            ang_deg = self._parse_length_mm(dim.get("value"))
                            if t2 and ang_deg is not None:
                                ad = dims.addAngleDimension(target, t2, adsk.core.Point3D.create(0, 0, 0))
                                try:
                                    ad.parameter.value = (ang_deg / 180.0) * 3.141592653589793
                                except Exception:
                                    pass
                except Exception:
                    pass

            # Execute features (limited: extrude, fillet)
            for feat in csl_ir.get("features", []) or []:
                if not isinstance(feat, dict):
                    continue
                kind = (feat.get("kind") or "").lower()
                feat_id = feat.get("id") or kind
                if kind == "extrude":
                    # Use first available profile if profile string is ambiguous
                    profile = self._first_profile(root)
                    if profile is None:
                        continue
                    dist_mm = self._parse_length_mm(feat.get("distance")) or 10.0
                    dist_cm = dist_mm / 10.0
                    distance = adsk.core.ValueInput.createByReal(dist_cm)
                    ext_feats = root.features.extrudeFeatures
                    op = self._feature_operation(feat.get("operation") or feat.get("op"))
                    ext_input = ext_feats.createInput(profile, op)
                    ext_input.setDistanceExtent(False, distance)
                    ext = ext_feats.add(ext_input)
                    mapping[feat_id] = f"fusion:extrude:{ext.entityToken}"
                elif kind == "fillet":
                    rad_mm = self._parse_length_mm(feat.get("radius")) or 1.0
                    rad_cm = rad_mm / 10.0
                    # Resolve edges via query if provided; else use all edges
                    edges = None
                    try:
                        q_spec = feat.get("edges_query") or (feat.get("edges") if isinstance(feat.get("edges"), dict) else None)
                        if q_spec:
                            edges = self._resolve_query(root, q_spec, entity_type="edge")
                    except Exception:
                        edges = None
                    edges = edges or self._all_body_edges(root)
                    # Transitions/setbacks not mapped yet
                    if feat.get("transitions") or feat.get("setback"):
                        try:
                            self._diag("E2320", where="fillet", message="Transitions/setbacks not mapped; applying per-group constants where possible.")
                        except Exception:
                            pass
                    if edges.count > 0:
                        fil_feats = root.features.filletFeatures
                        edge_col = adsk.core.ObjectCollection.create()
                        for e in edges:
                            edge_col.add(e)
                        # If per-edge groups provided, create separate constant fillets for each group
                        try:
                            per_groups = feat.get("edges") or []
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
                                    grp_edges = None
                                    try:
                                        qg = grp.get("q") or grp.get("edges_query") or grp.get("edges")
                                        if qg:
                                            grp_edges = self._resolve_query(root, qg, entity_type="edge")
                                    except Exception:
                                        grp_edges = None
                                    grp_edges = grp_edges or edge_col
                                    const_def = fil_feats.createConstantRadiusFilletDefinition(grp_edges, adsk.core.ValueInput.createByReal(r_cm), False)
                                    fil = fil_feats.add(const_def)
                                    mapping[f"{feat_id}:grp"] = f"fusion:fillet:{fil.entityToken}"
                                # Skip the single-feature path when per-groups are processed
                                continue
                        except Exception:
                            pass
                        const_def = fil_feats.createConstantRadiusFilletDefinition(edge_col, adsk.core.ValueInput.createByReal(rad_cm), False)
                        fil = fil_feats.add(const_def)
                        mapping[feat_id] = f"fusion:fillet:{fil.entityToken}"
                        try:
                            self._record_lineage(feat_id, fil, root)
                        except Exception:
                            pass
                elif kind == "chamfer":
                    d_mm = self._parse_length_mm(feat.get("distance")) or 1.0
                    d_cm = d_mm / 10.0
                    edges = None
                    try:
                        q_spec = feat.get("edges_query") or (feat.get("edges") if isinstance(feat.get("edges"), dict) else None)
                        if q_spec:
                            edges = self._resolve_query(root, q_spec, entity_type="edge")
                    except Exception:
                        edges = None
                    edges = edges or self._all_body_edges(root)
                    # Transitions not mapped yet
                    if feat.get("transitions") or feat.get("setback"):
                        try:
                            self._diag("E2321", where="chamfer", message="Transitions/setbacks not mapped; applying per-group constants where possible.")
                        except Exception:
                            pass
                    if edges.count > 0:
                        chf = root.features.chamferFeatures
                        edge_col = adsk.core.ObjectCollection.create()
                        for e in edges:
                            edge_col.add(e)
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
                                    gd_mm = self._parse_length_mm(grp.get("d") or grp.get("distance")) or d_mm
                                    gd_cm = gd_mm / 10.0
                                    grp_edges = None
                                    try:
                                        qg = grp.get("q") or grp.get("edges_query") or grp.get("edges")
                                        if qg:
                                            grp_edges = self._resolve_query(root, qg, entity_type="edge")
                                    except Exception:
                                        grp_edges = None
                                    grp_edges = grp_edges or edge_col
                                    defn = chf.createEqualDistanceChamferDefinition(grp_edges, adsk.core.ValueInput.createByReal(gd_cm), False)
                                    ch = chf.add(defn)
                                    mapping[f"{feat_id}:grp"] = f"fusion:chamfer:{ch.entityToken}"
                                continue
                        except Exception:
                            pass
                        defn = chf.createEqualDistanceChamferDefinition(edge_col, adsk.core.ValueInput.createByReal(d_cm), False)
                        ch = chf.add(defn)
                        mapping[feat_id] = f"fusion:chamfer:{ch.entityToken}"
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
                            dist_mm = self._parse_length_mm(feat.get("distance") or feat.get("thickness") or "10") or 10.0
                            dist_cm = dist_mm / 10.0
                            ext_input.setDistanceExtent(False, adsk.core.ValueInput.createByReal(dist_cm))
                            # Thin wall parameters
                            wall_mm = self._parse_length_mm(feat.get("wall") or feat.get("wall_thickness") or "2") or 2.0
                            wall_cm = wall_mm / 10.0
                            side = (feat.get("side") or "center").lower()
                            try:
                                # Newer API supports setThinExtrude
                                ext_input.isThinFeature = True
                                ext_input.thickness = adsk.core.ValueInput.createByReal(wall_cm)
                                if hasattr(ext_input, "thinDirection"):
                                    # 0: center, 1: oneSide, 2: twoSides (example mapping)
                                    if side in ("center", "symmetric"):
                                        ext_input.thinDirection = 0
                                    elif side in ("outward", "one_side_out"):
                                        ext_input.thinDirection = 1
                                    else:
                                        ext_input.thinDirection = 2
                            except Exception:
                                pass
                            ext = ext_feats.add(ext_input)
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
                        if kind == "project":
                            # Project sketch curves onto a target face/direction
                            tgt = None
                            try:
                                fq = feat.get("onto") or feat.get("face_query")
                                if fq:
                                    fcol = self._resolve_query(root, fq, entity_type="face")
                                    tgt = fcol.item(0) if fcol and fcol.count > 0 else None
                            except Exception:
                                tgt = None
                            if tgt is not None:
                                # Create a new sketch on the face and copy curves from source sketch
                                sk = root.sketches.add(tgt)
                                mapping[feat_id] = f"fusion:project:{sk.entityToken}"
                            else:
                                mapping[feat_id] = "fusion:project:E2310"
                                self._diag("E2310", where="project", message="No target face for project.")
                        else:
                            # Native emboss/wrap using EmbossFeatures if available
                            emb = getattr(root.features, "embossFeatures", None)
                            if emb is None:
                                mapping[feat_id] = f"fusion:{kind}:E2311"
                                self._diag("E2311", where=kind, message="Emboss/Wrap not available in this Fusion version")
                            else:
                                # Source curves from a named sketch (from_sketch) or last created sketch
                                src_sk = None
                                src_name = feat.get("from_sketch") or feat.get("sketch") or feat.get("source")
                                if src_name and isinstance(src_name, str):
                                    src_sk = sketch_map.get(src_name) or None
                                    if src_sk is None:
                                        # scan by name
                                        try:
                                            for s in root.sketches:
                                                if getattr(s, "name", "") == src_name:
                                                    src_sk = s
                                                    break
                                        except Exception:
                                            pass
                                if src_sk is None and len(sketch_map) > 0:
                                    # fallback to any existing sketch if not specified
                                    try:
                                        src_sk = next(iter(sketch_map.values()))
                                    except Exception:
                                        src_sk = None
                                # Target faces
                                tgt_faces = None
                                face_q = feat.get("onto") or feat.get("face_query")
                                if face_q:
                                    fcol = self._resolve_query(root, face_q, entity_type="face")
                                    if fcol and fcol.count > 0:
                                        tgt_faces = fcol
                                if src_sk is None or tgt_faces is None or tgt_faces.count == 0:
                                    mapping[feat_id] = f"fusion:{kind}:E2312"
                                    self._diag("E2312", where=kind, message="Missing source sketch or target faces for emboss/wrap.")
                                else:
                                    # Depth/angle parameters
                                    depth_mm = self._parse_length_mm(feat.get("depth") or "1") or 1.0
                                    depth = adsk.core.ValueInput.createByReal(depth_mm / 10.0)
                                    angle_deg = self._parse_length_mm(str(feat.get("angle") or "0")) or 0.0
                                    angle = adsk.core.ValueInput.createByReal((angle_deg / 180.0) * 3.141592653589793)
                                    # Mode: emboss vs wrap; engrave if negative depth requested
                                    is_wrap = (kind == "wrap") or str(feat.get("method") or "").lower() == "wrap"
                                    is_engrave = bool(feat.get("engrave") or (depth_mm < 0))
                                    # Attempt API variations
                                    created = None
                                    for api_variant in ("createInput", "createEmbossFeatureInput"):
                                        try:
                                            if hasattr(emb, api_variant):
                                                # Common signature guesses: (sketch, faces, isWrap?, depth, angle?)
                                                if api_variant == "createInput":
                                                    ein = emb.createInput(src_sk, tgt_faces, is_wrap)
                                                    # Optional params on input
                                                    for attr, val in (("depth", depth), ("angle", angle), ("isEngrave", is_engrave)):
                                                        if hasattr(ein, attr):
                                                            try:
                                                                setattr(ein, attr, val)
                                                            except Exception:
                                                                pass
                                                    created = emb.add(ein)
                                                else:
                                                    ein = emb.createEmbossFeatureInput(src_sk, tgt_faces, depth, is_wrap)
                                                    if hasattr(ein, "isEngrave"):
                                                        try:
                                                            ein.isEngrave = is_engrave
                                                        except Exception:
                                                            pass
                                                    created = emb.add(ein)
                                                if created:
                                                    break
                                        except Exception:
                                            created = None
                                    if created:
                                        mapping[feat_id] = f"fusion:{kind}:{created.entityToken}"
                                        try:
                                            self._record_lineage(feat_id, created, root)
                                        except Exception:
                                            pass
                                    else:
                                        mapping[feat_id] = f"fusion:{kind}:E2313"
                                        self._diag("E2313", where=kind, message="Emboss/Wrap API call failed on this Fusion version.")
                    except Exception:
                        mapping[feat_id] = f"fusion:{kind}:E2311"
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
                        face = face or self._first_planar_face(root)
                        if face is None:
                            mapping[feat_id] = "fusion:hole:skipped"
                        else:
                            sk = root.sketches.add(face)
                            pts = adsk.core.ObjectCollection.create()
                            for pt in (feat.get("points") or []):
                                p = self._parse_point(pt if isinstance(pt, str) else None)
                                if p:
                                    sp = sk.sketchPoints.add(adsk.core.Point3D.create(p[0], p[1], 0))
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
                            h_input.setPositionBySketchPoints(pts)
                            h = hole_feats.add(h_input)
                            mapping[feat_id] = f"fusion:hole:{h.entityToken}:{h_type}"
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
                    profile = self._first_profile(root)
                    if profile is None:
                        continue
                    axis = root.zConstructionAxis
                    rev_feats = root.features.revolveFeatures
                    angle = adsk.core.ValueInput.createByReal(2 * 3.141592653589793)  # 360 rad units in cm space
                    rev_input = rev_feats.createInput(profile, axis, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
                    rev_input.setAngleExtent(False, angle)
                    rev = rev_feats.add(rev_input)
                    mapping[feat_id] = f"fusion:revolve:{rev.entityToken}"
                    try:
                        self._record_lineage(feat_id, rev, root)
                    except Exception:
                        pass
                elif kind == "sweep":
                    # Sweep first profile along first sketch curve found
                    prof = self._first_profile(root)
                    path = self._first_path(root)
                    if prof and path:
                        sw = root.features.sweepFeatures
                        sw_input = sw.createInput(prof, path, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
                        # Orientation: frenet|fixed_normal|binormal
                        try:
                            orient = (feat.get("orientation") or "frenet").lower()
                            if hasattr(sw_input, "orientation"):
                                if orient == "fixed_normal":
                                    sw_input.orientation = adsk.fusion.SweepOrientationTypes.PathOrientationType
                                elif orient == "binormal":
                                    sw_input.orientation = adsk.fusion.SweepOrientationTypes.GuideRailOrientationType
                                else:
                                    sw_input.orientation = adsk.fusion.SweepOrientationTypes.PerpendicularOrientationType
                        except Exception:
                            pass
                        # Optional guide surface/rail via query
                        try:
                            if feat.get("guide_query"):
                                gcol = self._resolve_query(root, feat.get("guide_query"), entity_type="edge")
                                if gcol and hasattr(sw_input, "guideRail"):
                                    sw_input.guideRail = gcol.item(0)
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
                                for attr in ("sectionContinuity", "continuity", "edgeContinuity"):
                                    if hasattr(lf_input, attr):
                                        try:
                                            setattr(lf_input, attr, cont)
                                            applied = True
                                            break
                                        except Exception:
                                            continue
                                if not applied:
                                    self._diag("E2315", where="loft", message=f"Requested continuity {cont} not supported by this Fusion version.")
                                    mapping[feat_id] = f"fusion:loft:E2315"
                                    continue
                            orient = (feat.get("orientation") or "").lower()
                            if orient:
                                # If orientation control is not supported on loft, hard fail when explicitly requested
                                supported = False
                                for attr in ("orientation", "loftOrientation"):
                                    if hasattr(lf_input, attr):
                                        try:
                                            setattr(lf_input, attr, orient)
                                            supported = True
                                            break
                                        except Exception:
                                            continue
                                if not supported:
                                    self._diag("E2316", where="loft", message=f"Requested orientation '{orient}' not supported by this Fusion version.")
                                    mapping[feat_id] = f"fusion:loft:E2316"
                                    continue
                        except Exception:
                            pass
                        # Optional guide rails from queries/sketch
                        try:
                            guides = feat.get("guides") or []
                            if isinstance(guides, list) and len(guides) > 0:
                                rails = adsk.core.ObjectCollection.create()
                                for g in guides:
                                    if isinstance(g, dict):
                                        gc = self._resolve_query(root, g, entity_type="edge")
                                        if gc and gc.count > 0:
                                            rails.add(gc.item(0))
                                if rails.count > 0 and hasattr(lf_input, "centerLineOrRails"):
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
                        # As a placeholder, shell entire body inward by thickness if provided
                        for f in faces:
                            face_col.add(f)
                        t_mm = self._parse_length_mm(feat.get("thickness")) or 2.0
                        t_cm = t_mm / 10.0
                        s_in = shell.createShellFeatureInput(face_col, adsk.core.ValueInput.createByReal(t_cm))
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
                            # Neutral plane selection
                            neutral = root.xYConstructionPlane
                            neutral_key = (feat.get("neutral_plane") or "world.xy").lower()
                            if "xz" in neutral_key:
                                neutral = root.xZConstructionPlane
                            elif "yz" in neutral_key:
                                neutral = root.yZConstructionPlane
                            ang_deg = self._parse_length_mm(str(feat.get("angle") or "2")) or 2.0
                            ang_rad = (ang_deg / 180.0) * 3.141592653589793
                            angle = adsk.core.ValueInput.createByReal(ang_rad)
                            d_in = draft.createInput(face_col, neutral, angle, False, adsk.fusion.DraftDirectionsType.PullDirectionType)
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
                        if bodies.count > 0:
                            cyl_faces = bodies.item(bodies.count - 1).faces
                            target_faces = adsk.core.ObjectCollection.create()
                            for f in cyl_faces:
                                if f.geometry.surfaceType == 1:  # cylindrical surface type
                                    target_faces.add(f)
                            if target_faces.count > 0:
                                is_modeled = (feat.get("mode") or feat.get("modeled") or "cosmetic").lower() == "modeled"
                                t_in = thr.createThreadInfo(False)  # False => cosmetic by default
                                # Map designation/class/handedness best-effort
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
                                    self._diag("E2303", where="thread", message="No cylindrical faces found for thread.", data={"id": feat_id})
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
                                sqc = self._resolve_query(root, seed_q, entity_type="body")
                                if sqc and sqc.count > 0:
                                    for i in range(sqc.count):
                                        obj_col.add(sqc.item(i))
                            except Exception:
                                pass
                        if obj_col.count == 0:
                            obj_col.add(bodies.item(bodies.count - 1))
                        kind_sub = (feat.get("kind") or "linear").lower()
                        if kind_sub == "circular":
                            circ = root.features.circularPatternFeatures
                            axis = root.zConstructionAxis
                            qty = adsk.core.ValueInput.createByString(str(int(feat.get("count") or 6)))
                            angle = adsk.core.ValueInput.createByReal(2 * 3.141592653589793)
                            c_in = circ.createInput(obj_col, axis, qty, angle)
                            cp = circ.add(c_in)
                            mapping[feat_id] = f"fusion:pattern_circular:{cp.entityToken}"
                            try:
                                self._record_lineage(feat_id, cp, root)
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
                                    d1 = adsk.core.ValueInput.createByReal(1.0)
                                    p_in = ppf.createInput(obj_col, path, qty, d1, False)
                                    pp = ppf.add(p_in)
                                    mapping[feat_id] = f"fusion:pattern_path:{pp.entityToken}"
                                    try:
                                        self._record_lineage(feat_id, pp, root)
                                    except Exception:
                                        pass
                                    continue
                            except Exception:
                                pass
                        else:
                            patt = root.features.rectangularPatternFeatures
                            # Direction 1
                            dir1 = root.xConstructionAxis
                            count1 = int(feat.get("count1") or feat.get("count") or 2)
                            spacing1_mm = self._parse_length_mm(feat.get("spacing1") or feat.get("spacing") or "10") or 10.0
                            # Direction 2 (optional for grid)
                            dir2 = root.yConstructionAxis
                            count2 = int(feat.get("count2") or 1)
                            spacing2_mm = self._parse_length_mm(feat.get("spacing2") or "10") or 10.0
                            # Table-driven fallback
                            if isinstance(feat.get("table"), list) and len(feat.get("table")) > 0:
                                try:
                                    mv = root.features.moveFeatures
                                    for row in feat.get("table"):
                                        if not isinstance(row, dict):
                                            continue
                                        dx = (self._parse_length_mm(row.get("dx") or "0") or 0.0) / 10.0
                                        dy = (self._parse_length_mm(row.get("dy") or "0") or 0.0) / 10.0
                                        qty = int(row.get("count") or 1)
                                        for i in range(qty):
                                            vec = adsk.core.Vector3D.create(dx, dy, 0)
                                            trans = adsk.core.Matrix3D.create()
                                            trans.translation = vec
                                            input_def = mv.createInput(obj_col, trans)
                                            mv.add(input_def)
                                        mapping[feat_id] = f"fusion:pattern_table:fallback"
                                        continue
                                except Exception:
                                    pass
                            qty1 = adsk.core.ValueInput.createByString(str(count1))
                            dist1 = adsk.core.ValueInput.createByReal((spacing1_mm / 10.0))
                            input_def = patt.createInput(obj_col, dir1, qty1, dist1, adsk.fusion.PatternDistanceType.SpacingPatternDistanceType)
                            if count2 > 1:
                                qty2 = adsk.core.ValueInput.createByString(str(count2))
                                dist2 = adsk.core.ValueInput.createByReal((spacing2_mm / 10.0))
                                input_def.setDirectionTwo(dir2, qty2, dist2)
                            pat = patt.add(input_def)
                            mapping[feat_id] = f"fusion:pattern_linear:{pat.entityToken}"
                            try:
                                self._record_lineage(feat_id, pat, root)
                            except Exception:
                                pass
                elif kind == "mirror":
                    bodies = self._all_bodies(root)
                    if bodies.count > 0:
                        obj_col = adsk.core.ObjectCollection.create()
                        obj_col.add(bodies.item(bodies.count - 1))
                        mirror = root.features.mirrorFeatures
                        plane = root.yZConstructionPlane
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
                    if bodies.count >= 2:
                        target = bodies.item(bodies.count - 2)
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
                    # Offset faces of last body as a proxy for move/offset face
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
                    # Replace faces with a plane (approximate) using construction plane
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
                        rf = rep.add(face_col, surf, False)
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
                    # No per-body export in all versions; export whole component
                    exp.execute(opts)
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
                        # Binary/text format
                        if isinstance(op.get("binary"), bool) and hasattr(opts, "isBinaryFormat"):
                            opts.isBinaryFormat = bool(op.get("binary"))
                        # Advanced mesh controls if available
                        if hasattr(opts, "surfaceDeviation") and op.get("deviation"):
                            dev_mm = self._parse_length_mm(op.get("deviation"))
                            if dev_mm is not None:
                                opts.surfaceDeviation = float(dev_mm) / 10.0
                        if hasattr(opts, "maximumEdgeLength") and op.get("max_edge"):
                            me_mm = self._parse_length_mm(op.get("max_edge"))
                            if me_mm is not None:
                                opts.maximumEdgeLength = float(me_mm) / 10.0
                        if hasattr(opts, "aspectRatio") and op.get("aspect_ratio"):
                            try:
                                opts.aspectRatio = float(op.get("aspect_ratio"))
                            except Exception:
                                pass
                        # Units
                        req_units = (op.get("units") or "").lower()
                        applied_units = False
                        # Some Fusion versions expose units selection
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

    def _parse_point(self, value: Optional[str]) -> Optional[List[float]]:
        if not value:
            return None
        # Expect formats like "x, y" or "15 mm, 15 mm"
        parts = [p.strip() for p in value.split(",")]
        if len(parts) < 2:
            return None
        x = self._parse_length_cm(parts[0])
        y = self._parse_length_cm(parts[1])
        if x is None or y is None:
            return None
        return [x, y]

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
            self._lineage[feature_id] = tokens
            # Persist lineage (merge)
            try:
                self._persisted_lineage.setdefault(feature_id, {"bodies": [], "faces": [], "edges": []})
                for k in ("bodies", "faces", "edges"):
                    exist = set(self._persisted_lineage[feature_id].get(k, []))
                    for t in tokens.get(k, []):
                        if t not in exist:
                            self._persisted_lineage[feature_id].setdefault(k, []).append(t)
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

        # created_by: use lineage tokens (session or persisted)
        fid_lookup = created_by or owner_feature
        if fid_lookup and (fid_lookup in self._lineage or fid_lookup in self._persisted_lineage):
            tokens = self._lineage.get(fid_lookup) or self._persisted_lineage.get(fid_lookup) or {}
            token_list = tokens.get(f"{kind}s") or []
            for t in token_list:
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

        # pattern_instances: select from lineage for a given pattern feature
        if pat and isinstance(pat, dict):
            feature_id = pat.get("feature") or pat.get("id")
            if feature_id and feature_id in self._lineage:
                type_key = (pat.get("type") or kind or "face").lower()
                tokens = self._lineage[feature_id]
                for t in tokens.get(f"{type_key}s", []):
                    add_entity_by_token(t)
            return col

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

        # by_material / appearance filter
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

        # Fallback: return nothing
        return col

    def _get_all_faces(self, root):
        import adsk.core  # type: ignore
        col = adsk.core.ObjectCollection.create()  # type: ignore
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
        self._errors.append(entry)

    def get_diagnostics(self) -> Dict[str, Any]:
        return {"errors": list(self._errors)}

    # ------------------------
    # APS Helpers
    # ------------------------
    def _aps_token(self) -> Optional[str]:
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
            return resp.json().get("access_token")
        except Exception:
            return None

    def _aps_ensure_bucket(self, token: str, bucket: str) -> None:
        try:
            import requests  # type: ignore
            hdr = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
            base = "https://developer.api.autodesk.com/oss/v2/buckets"
            # Try create; if exists, ignore
            payload = {"bucketKey": bucket, "policyKey": "transient"}
            resp = requests.post(base, headers=hdr, json=payload, timeout=20)
            if resp.status_code not in (200, 409):
                self._diag("E3102", where="aps", message=f"Bucket ensure failed: {resp.status_code}")
        except Exception:
            pass

    def _aps_upload(self, file_path: str) -> None:
        token = self._aps_token()
        bucket = self.session_config.get("aps_bucket")
        if not token or not bucket:
            return
        self._aps_ensure_bucket(token, bucket)
        try:
            import requests  # type: ignore
            hdr = {"Authorization": f"Bearer {token}", "Content-Type": "application/octet-stream"}
            import os as _os
            name = _os.path.basename(file_path)
            with open(file_path, "rb") as f:
                data = f.read()
            url = f"https://developer.api.autodesk.com/oss/v2/buckets/{bucket}/objects/{name}"
            resp = requests.put(url, headers=hdr, data=data, timeout=60)
            if resp.status_code not in (200, 201):
                self._diag("E3103", where="aps", message=f"Upload failed: {resp.status_code}")
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
        results: Dict[str, Any] = {"ok": True, "uploaded": [], "errors": []}
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
            _try(self.export, plan.get("export"), "export")
        if plan.get("thumbnail"):
            _try(self.thumbnail, plan.get("thumbnail"), "thumbnail")
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
        except Exception:
            self._persisted_lineage = {}

    def _save_persisted_lineage(self) -> None:
        try:
            import json as _json
            with open(self._lineage_path(), "w", encoding="utf-8") as f:
                _json.dump(self._persisted_lineage, f)
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
        import adsk.core  # type: ignore
        import adsk.fusion  # type: ignore
        app, ui, design = self._ensure_design()
        root_comp = design.rootComponent
        # Materials
        try:
            mats = csl_ir.get("materials") or []
            if isinstance(mats, list):
                # Build search across material libraries
                libraries = []
                try:
                    for i in range(app.materialLibraries.count):
                        libraries.append(app.materialLibraries.item(i))
                except Exception:
                    pass
                for m in mats:
                    if not isinstance(m, dict):
                        continue
                    ref = m.get("ref") or m.get("name")
                    target_mat = None
                    if ref:
                        # Search in design materials first
                        try:
                            target_mat = design.materials.itemByName(ref)
                        except Exception:
                            target_mat = None
                        if not target_mat:
                            try:
                                for lib in libraries:
                                    mm = lib.materials.itemByName(ref)
                                    if mm:
                                        target_mat = mm
                                        break
                            except Exception:
                                pass
                    # Apply to all bodies if found
                    if target_mat:
                        try:
                            for b in root_comp.bRepBodies:
                                b.material = target_mat
                        except Exception:
                            pass
                    # Appearance overrides by color name or hex
                    ap = m.get("appearance") or m.get("color")
                    if ap:
                        app_obj = None
                        try:
                            # search appearances
                            for i in range(app.appearanceLibraries.count):
                                lib = app.appearanceLibraries.item(i)
                                app_obj = lib.appearances.itemByName(str(ap))
                                if app_obj:
                                    break
                        except Exception:
                            app_obj = None
                        if app_obj:
                            try:
                                for b in root_comp.bRepBodies:
                                    b.appearance = app_obj
                            except Exception:
                                pass
        except Exception:
            pass
        # PMI notes
        try:
            pmi_list = csl_ir.get("pmi") or []
            if isinstance(pmi_list, list) and len(pmi_list) > 0:
                sk = root_comp.sketches.add(root_comp.xYConstructionPlane)
                for note in pmi_list:
                    if not isinstance(note, dict) or not note.get("note"):
                        continue
                    txt = str(note.get("note"))
                    pos = note.get("at") or "0,0"
                    pt = self._parse_point(pos) or [0.0, 0.0]
                    height_mm = self._parse_length_mm(note.get("height") or "5") or 5.0
                    height = height_mm / 10.0
                    try:
                        ti = sk.sketchTexts.createInput(txt, height)
                        p = adsk.core.Point3D.create(pt[0], pt[1], 0)
                        ti.setAsMultiLine(p, 0.0, adsk.core.HorizontalAlignments.LeftHorizontalAlignment, adsk.core.VerticalAlignments.TopVerticalAlignment, 0.0)
                        sk.sketchTexts.add(ti)
                    except Exception:
                        pass
        except Exception:
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


