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
        }

    def open_session(self, session_config: Dict[str, Any] | None = None) -> None:
        if session_config:
            self.session_config.update(session_config)
        # Load APS env if provided (for future cloud ops)
        self.session_config.setdefault("aps_client_id", os.getenv("APS_CLIENT_ID"))
        self.session_config.setdefault("aps_client_secret", os.getenv("APS_CLIENT_SECRET"))
        if not self._fusion_available:
            print("[FusionBackend] Fusion API not available in this environment; running in dry-run mode.")

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
                plane = self._plane_from_name(root, plane_name)
                sketch = root.sketches.add(plane)
                # Entities
                for ent in sk.get("entities", []) or []:
                    kind = (ent.get("kind") or "").lower()
                    if kind == "rect":
                        p1 = self._parse_point(ent.get("p1"))
                        p2 = self._parse_point(ent.get("p2"))
                        if p1 and p2:
                            sketch.sketchCurves.sketchLines.addTwoPointRectangle(
                                adsk.core.Point3D.create(p1[0], p1[1], 0),
                                adsk.core.Point3D.create(p2[0], p2[1], 0),
                            )
                    elif kind == "circle":
                        c = self._parse_point(ent.get("center"))
                        d_mm = self._parse_length_mm(ent.get("d"))
                        if c and d_mm:
                            r_cm = (d_mm / 2.0) / 10.0
                            sketch.sketchCurves.sketchCircles.addByCenterRadius(
                                adsk.core.Point3D.create(c[0], c[1], 0), r_cm
                            )
                sketch_map[sk_id] = sketch

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
                    edges = self._all_body_edges(root)
                    if edges.count > 0:
                        fil_feats = root.features.filletFeatures
                        edge_col = adsk.core.ObjectCollection.create()
                        for e in edges:
                            edge_col.add(e)
                        const_def = fil_feats.createConstantRadiusFilletDefinition(edge_col, adsk.core.ValueInput.createByReal(rad_cm), False)
                        fil = fil_feats.add(const_def)
                        mapping[feat_id] = f"fusion:fillet:{fil.entityToken}"
                elif kind == "chamfer":
                    d_mm = self._parse_length_mm(feat.get("distance")) or 1.0
                    d_cm = d_mm / 10.0
                    edges = self._all_body_edges(root)
                    if edges.count > 0:
                        chf = root.features.chamferFeatures
                        edge_col = adsk.core.ObjectCollection.create()
                        for e in edges:
                            edge_col.add(e)
                        defn = chf.createEqualDistanceChamferDefinition(edge_col, adsk.core.ValueInput.createByReal(d_cm), False)
                        ch = chf.add(defn)
                        mapping[feat_id] = f"fusion:chamfer:{ch.entityToken}"
                elif kind == "hole":
                    try:
                        hole_feats = root.features.holeFeatures
                        d_mm = self._parse_length_mm(feat.get("d") or feat.get("diameter")) or 5.0
                        d_cm = d_mm / 10.0
                        dia = adsk.core.ValueInput.createByReal(d_cm)
                        # Position using a sketch on the first planar face
                        face = self._first_planar_face(root)
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
                                # Fallback: place one at origin
                                sp = sk.sketchPoints.add(adsk.core.Point3D.create(0, 0, 0))
                                pts.add(sp)
                            h_input = hole_feats.createSimpleInput(dia)
                            h_input.setPositionBySketchPoints(pts)
                            h = hole_feats.add(h_input)
                            mapping[feat_id] = f"fusion:hole:{h.entityToken}"
                    except Exception:
                        mapping[feat_id] = "fusion:hole:error"
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
                elif kind == "draft":
                    try:
                        draft = root.features.draftFeatures
                        bodies = self._all_bodies(root)
                        if bodies.count > 0:
                            faces = bodies.item(bodies.count - 1).faces
                            face_col = adsk.core.ObjectCollection.create()
                            for f in faces:
                                face_col.add(f)
                            neutral = root.xYConstructionPlane
                            ang_deg = self._parse_length_mm(str(feat.get("angle") or "2")) or 2.0
                            ang_rad = (ang_deg / 180.0) * 3.141592653589793
                            angle = adsk.core.ValueInput.createByReal(ang_rad)
                            d_in = draft.createInput(face_col, neutral, angle, False, adsk.fusion.DraftDirectionsType.PullDirectionType)
                            d = draft.add(d_in)
                            mapping[feat_id] = f"fusion:draft:{d.entityToken}"
                    except Exception:
                        mapping[feat_id] = "fusion:draft:error"
                elif kind == "pattern":
                    # Simple linear pattern along +X using last body
                    bodies = self._all_bodies(root)
                    if bodies.count > 0:
                        obj_col = adsk.core.ObjectCollection.create()
                        # Pattern the last body
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
                        else:
                            patt = root.features.rectangularPatternFeatures
                            dir_vec = root.xConstructionAxis
                            count = int(feat.get("count") or 2)
                            spacing_mm = self._parse_length_mm(feat.get("spacing")) or 10.0
                            spacing_cm = spacing_mm / 10.0
                            qty = adsk.core.ValueInput.createByString(str(count))
                            dist = adsk.core.ValueInput.createByReal(spacing_cm)
                            input_def = patt.createInput(obj_col, dir_vec, qty, dist, adsk.fusion.PatternDistanceType.SpacingPatternDistanceType)
                            pat = patt.add(input_def)
                            mapping[feat_id] = f"fusion:pattern_linear:{pat.entityToken}"
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
                elif kind == "boolean":
                    # Combine last two bodies
                    bodies = self._all_bodies(root)
                    if bodies.count >= 2:
                        target = bodies.item(bodies.count - 2)
                        tool = bodies.item(bodies.count - 1)
                        combine = root.features.combineFeatures
                        c_in = combine.createInput(target, adsk.core.ObjectCollection.create())
                        c_in.toolBodies.add(tool)
                        op = (feat.get("op") or feat.get("operation") or "union").lower()
                        if op == "subtract":
                            c_in.operation = adsk.fusion.FeatureOperations.CutFeatureOperation
                        elif op == "intersect":
                            c_in.operation = adsk.fusion.FeatureOperations.IntersectFeatureOperation
                        else:
                            c_in.operation = adsk.fusion.FeatureOperations.JoinFeatureOperation
                        c_in.isKeepToolBodies = False
                        cb = combine.add(c_in)
                        mapping[feat_id] = f"fusion:boolean:{cb.entityToken}"

            # Optionally export and thumbnails
            if csl_ir.get("export"):
                self.export(csl_ir.get("export", []))
            if csl_ir.get("thumbnail"):
                self.thumbnail(csl_ir.get("thumbnail", []))

        except Exception as ex:  # pragma: no cover - defensive
            print(f"[FusionBackend] realize failed: {ex}")

        return mapping

    def export(self, export_ops: List[Dict[str, Any]]) -> None:
        if not self._fusion_available:
            print(f"[FusionBackend] Dry-run export: {export_ops}")
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
                if fmt == "STEP":
                    opts = exp.createSTEPExportOptions(path)
                    exp.execute(opts)
                elif fmt == "STL":
                    try:
                        opts = exp.createSTLExportOptions(root, path)
                    except Exception:
                        opts = exp.createSTLExportOptions(root.bRepBodies, path)
                    exp.execute(opts)
                elif fmt == "IGES":
                    opts = exp.createIGESExportOptions(path)
                    exp.execute(opts)
                elif fmt in ("3MF", "OBJ"):
                    # Use generic export manager; not all formats may be available
                    opts = exp.createOBJExportOptions(path) if fmt == "OBJ" else exp.createMF3DExportOptions(path)
                    exp.execute(opts)
        except Exception as ex:
            print(f"[FusionBackend] export failed: {ex}")
        return

    def thumbnail(self, thumb_ops: List[Dict[str, Any]]) -> None:
        if not self._fusion_available:
            print(f"[FusionBackend] Dry-run thumbnail: {thumb_ops}")
            return
        try:
            import adsk.core  # type: ignore
            app = adsk.core.Application.get()
            vp = app.activeViewport
            for op in thumb_ops:
                path = op.get("path") or "out/preview.png"
                w = int(op.get("width") or 800)
                h = int(op.get("height") or 600)
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
        except Exception as ex:
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

    def _all_body_edges(self, root):
        import adsk.fusion  # type: ignore
        col = adsk.core.ObjectCollection.create()  # type: ignore
        for b in root.bRepBodies:
            for e in b.edges:
                col.add(e)
        return col

    def _all_bodies(self, root):
        return root.bRepBodies


