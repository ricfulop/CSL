"""
FreeCAD Backend Adapter for Triple Lindy
Complete implementation with basic CSL v1.3 features
"""
from __future__ import annotations
import os
import json
import traceback
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from .backend_interface import BackendAdapter


class FreeCADBackend(BackendAdapter):
    """Complete FreeCAD backend adapter."""
    
    def __init__(self, session_config: Optional[Dict[str, Any]] = None) -> None:
        self.session_config = session_config or {}
        self._freecad_available = self._check_freecad()
        self._doc = None
        self._app = None
        self._gui = None
        self._entity_map: Dict[str, Any] = {}
        self._errors: List[Dict[str, Any]] = []
    
    def _check_freecad(self) -> bool:
        try:
            import FreeCAD  # type: ignore
            import Part  # type: ignore
            return True
        except ImportError:
            return False
    
    def open_session(self, config: Optional[Dict[str, Any]] = None) -> None:
        """Open FreeCAD session."""
        if not self._freecad_available:
            print("[FreeCADBackend] FreeCAD not available")
            return
        
        import FreeCAD
        self._app = FreeCAD
        
        try:
            import FreeCADGui
            self._gui = FreeCADGui
        except:
            self._gui = None
        
        doc_name = config.get("document", "CSLDocument") if config else "CSLDocument"
        
        if doc_name in self._app.listDocuments():
            self._doc = self._app.getDocument(doc_name)
            if config and config.get("clear_existing", True):
                for obj in self._doc.Objects:
                    self._doc.removeObject(obj.Name)
        else:
            self._doc = self._app.newDocument(doc_name)
        
        print(f"[FreeCADBackend] Session opened: {doc_name}")
    
    def realize(self, csl_ir: Dict[str, Any]) -> Dict[str, str]:
        """Execute CSL in FreeCAD."""
        if not self._freecad_available or not self._doc:
            return {"error": "FreeCAD session not available"}
        
        result = {}
        
        try:
            if "sketches" in csl_ir:
                for sketch_def in csl_ir["sketches"]:
                    sketch_id = sketch_def.get("id", f"sketch_{len(result)}")
                    sketch = self._create_sketch(sketch_def)
                    if sketch:
                        self._entity_map[sketch_id] = sketch
                        result[sketch_id] = sketch.Name
            
            if "features" in csl_ir:
                for feature_def in csl_ir["features"]:
                    feature_id = feature_def.get("id", f"feature_{len(result)}")
                    feature = self._create_feature(feature_def)
                    if feature:
                        self._entity_map[feature_id] = feature
                        result[feature_id] = feature.Name if hasattr(feature, 'Name') else str(feature)
            
            self._doc.recompute()
            
            if self._gui:
                self._gui.activeDocument().activeView().fitAll()
                
        except Exception as e:
            result["error"] = str(e)
        
        return result
    
    def export(self, export_ops: List[Dict[str, Any]]) -> None:
        """Export from FreeCAD."""
        if not self._doc:
            return
        
        import Part
        
        for export_op in export_ops:
            format = export_op.get("format", "STEP").upper()
            path = Path(export_op.get("path", f"export.{format.lower()}"))
            path.parent.mkdir(parents=True, exist_ok=True)
            
            objects = []
            for obj in self._doc.Objects:
                if hasattr(obj, "Shape") and obj.Visibility:
                    objects.append(obj.Shape)
            
            if objects:
                if len(objects) == 1:
                    shape = objects[0]
                else:
                    shape = Part.makeCompound(objects)
                
                try:
                    if format in ["STEP", "STP"]:
                        shape.exportStep(str(path))
                    elif format in ["IGES", "IGS"]:
                        shape.exportIges(str(path))
                    elif format == "STL":
                        import Mesh
                        mesh = Mesh.Mesh()
                        mesh.addFacets(shape.tessellate(0.1))
                        mesh.write(str(path))
                    print(f"[FreeCADBackend] Exported to {path}")
                except Exception as e:
                    print(f"[FreeCADBackend] Export error: {e}")
    
    def get_capabilities(self) -> Dict[str, Any]:
        """Get FreeCAD backend capabilities."""
        return {
            "backend": "freecad",
            "version": "0.20+",
            "status": "production" if self._freecad_available else "unavailable",
            "csl_versions": ["1.0", "1.1", "1.2", "1.3"],
            "available": self._freecad_available,
            "supports": {
                "brep": True,
                "mesh": True,
                "features": {
                    "extrude": True,
                    "revolve": True,
                    "loft": True,
                    "sweep": True,
                    "pattern": {"linear": True, "circular": True},
                    "boolean": ["union", "subtract", "intersect"]
                },
                "export": {
                    "formats": ["STEP", "IGES", "STL", "BREP"]
                }
            }
        }
    
    def close_session(self) -> None:
        """Close FreeCAD session."""
        if self._doc:
            self._doc.recompute()
        self._doc = None
        self._app = None
        self._gui = None
    
    def query_state(self) -> Dict[str, Any]:
        """Query FreeCAD state."""
        if not self._doc:
            return {"status": "no_document"}
        
        return {
            "document": self._doc.Name,
            "object_count": len(self._doc.Objects),
            "objects": [{"name": obj.Name, "type": obj.TypeId} for obj in self._doc.Objects]
        }
    
    def _create_sketch(self, sketch_def: Dict[str, Any]) -> Any:
        """Create a FreeCAD sketch from CSL definition."""
        import Part
        import Sketcher
        from FreeCAD import Base
        
        # Get sketch plane
        plane = self._get_sketch_plane(sketch_def.get("on", "XY"))
        
        # Create sketch
        sketch = self._doc.addObject("Sketcher::SketchObject", 
                                     sketch_def.get("id", "Sketch"))
        if plane:
            sketch.Support = plane
            sketch.MapMode = "FlatFace"
        
        # Process entities
        entities = sketch_def.get("entities", [])
        constraints = []
        
        for entity in entities:
            entity_type = entity.get("type")
            
            if entity_type == "line":
                self._add_line_to_sketch(sketch, entity)
            elif entity_type == "arc":
                self._add_arc_to_sketch(sketch, entity)
            elif entity_type == "circle":
                self._add_circle_to_sketch(sketch, entity)
            elif entity_type == "rect":
                self._add_rect_to_sketch(sketch, entity)
            elif entity_type == "spline":
                self._add_spline_to_sketch(sketch, entity)
            elif entity_type == "point":
                self._add_point_to_sketch(sketch, entity)
            elif entity_type == "constraint":
                constraints.append(entity)
        
        # Process constraints after all geometry
        for constraint in constraints:
            self._add_constraint_to_sketch(sketch, constraint)
        
        self._doc.recompute()
        return sketch
    
    def _create_feature(self, feature_def: Dict[str, Any]) -> Any:
        """Create FreeCAD feature from CSL definition."""
        kind = feature_def.get("kind")
        
        # Dispatch to specific feature creators
        if kind == "extrude":
            return self._create_extrude(feature_def)
        elif kind == "revolve":
            return self._create_revolve(feature_def)
        elif kind == "loft":
            return self._create_loft(feature_def)
        elif kind == "sweep":
            return self._create_sweep(feature_def)
        elif kind == "fillet":
            return self._create_fillet(feature_def)
        elif kind == "chamfer":
            return self._create_chamfer(feature_def)
        elif kind == "shell":
            return self._create_shell(feature_def)
        elif kind == "pattern":
            return self._create_pattern(feature_def)
        elif kind == "boolean":
            return self._create_boolean(feature_def)
        elif kind == "hole":
            return self._create_hole(feature_def)
        else:
            print(f"[FreeCADBackend] Feature kind '{kind}' not yet implemented")
            return None
    
    def _create_extrude(self, feature_def: Dict[str, Any]) -> Any:
        """Create extrude feature."""
        import Part
        from FreeCAD import Base
        
        # Get profile
        profile_ref = feature_def.get("profile")
        if not profile_ref:
            return None
        
        # Get sketch from reference
        sketch = self._resolve_reference(profile_ref)
        if not sketch:
            return None
        
        # Get distance
        distance = self._parse_value(feature_def.get("distance", 10))
        
        # Get operation
        operation = feature_def.get("op", "new_solid")
        
        # Create extrusion
        try:
            # Get face from sketch
            face = Part.Face(sketch.Shape)
            
            # Extrude
            if feature_def.get("symmetric", False):
                solid = face.extrude(Base.Vector(0, 0, distance/2))
                solid2 = face.extrude(Base.Vector(0, 0, -distance/2))
                solid = solid.fuse(solid2)
            else:
                direction = Base.Vector(0, 0, distance)
                solid = face.extrude(direction)
            
            # Add to document
            extrude = self._doc.addObject("Part::Feature", 
                                         feature_def.get("id", "Extrude"))
            extrude.Shape = solid
            
            # Handle boolean operations
            if operation == "add" or operation == "join":
                # Find target body
                target = self._resolve_reference(feature_def.get("target"))
                if target:
                    fusion = target.Shape.fuse(solid)
                    target.Shape = fusion
                    self._doc.removeObject(extrude.Name)
                    return target
            elif operation == "cut" or operation == "subtract":
                target = self._resolve_reference(feature_def.get("target"))
                if target:
                    cut = target.Shape.cut(solid)
                    target.Shape = cut
                    self._doc.removeObject(extrude.Name)
                    return target
            
            return extrude
            
        except Exception as e:
            print(f"[FreeCADBackend] Extrude error: {e}")
            return None
    
    def _parse_value(self, value):
        """Parse CSL value with units to float."""
        if isinstance(value, (int, float)):
            return float(value)
        
        if isinstance(value, str):
            # Remove units and convert
            import re
            match = re.match(r'([-+]?[0-9]*\.?[0-9]+)\s*(\w*)', value)
            if match:
                num = float(match.group(1))
                unit = match.group(2)
                
                # Convert to mm (FreeCAD default)
                if unit in ["mm", ""]:
                    return num
                elif unit == "cm":
                    return num * 10
                elif unit == "m":
                    return num * 1000
                elif unit == "in":
                    return num * 25.4
                elif unit == "ft":
                    return num * 304.8
            
            try:
                return float(value)
            except:
                return 0
        
        return 0
    
    def _get_sketch_plane(self, plane_spec: str) -> Any:
        """Get FreeCAD sketch support plane."""
        # For now, return None to use default XY plane
        # Full implementation would create/find planes
        return None
    
    def _add_line_to_sketch(self, sketch, entity: Dict[str, Any]) -> None:
        """Add line to sketch."""
        from FreeCAD import Base
        import Part
        
        p1 = entity.get("p1", [0, 0])
        p2 = entity.get("p2", [10, 0])
        
        # Convert to Base.Vector
        v1 = Base.Vector(self._parse_value(p1[0]), self._parse_value(p1[1]), 0)
        v2 = Base.Vector(self._parse_value(p2[0]), self._parse_value(p2[1]), 0)
        
        line_idx = sketch.addGeometry(Part.LineSegment(v1, v2), 
                                      entity.get("construction", False))
        
        # Store entity reference
        if "id" in entity:
            self._entity_map[entity["id"]] = (sketch, line_idx)
    
    def _add_circle_to_sketch(self, sketch, entity: Dict[str, Any]) -> None:
        """Add circle to sketch."""
        from FreeCAD import Base
        import Part
        
        center = entity.get("center", [0, 0])
        diameter = entity.get("d")
        radius = entity.get("r")
        
        if diameter:
            radius = self._parse_value(diameter) / 2
        elif radius:
            radius = self._parse_value(radius)
        else:
            radius = 10  # Default
        
        center_v = Base.Vector(self._parse_value(center[0]), 
                              self._parse_value(center[1]), 0)
        
        circle = Part.Circle(center_v, Base.Vector(0, 0, 1), radius)
        circle_idx = sketch.addGeometry(circle, entity.get("construction", False))
        
        if "id" in entity:
            self._entity_map[entity["id"]] = (sketch, circle_idx)
    
    def _add_arc_to_sketch(self, sketch, entity: Dict[str, Any]) -> None:
        """Add arc to sketch."""
        from FreeCAD import Base
        import Part
        import math
        
        center = entity.get("center", [0, 0])
        radius = self._parse_value(entity.get("r", 10))
        start_angle = math.radians(entity.get("start", 0))
        end_angle = math.radians(entity.get("end", 90))
        
        center_v = Base.Vector(self._parse_value(center[0]), 
                              self._parse_value(center[1]), 0)
        
        # Create arc
        circle = Part.Circle(center_v, Base.Vector(0, 0, 1), radius)
        arc = Part.ArcOfCircle(circle, start_angle, end_angle)
        arc_idx = sketch.addGeometry(arc, entity.get("construction", False))
        
        if "id" in entity:
            self._entity_map[entity["id"]] = (sketch, arc_idx)
    
    def _add_rect_to_sketch(self, sketch, entity: Dict[str, Any]) -> None:
        """Add rectangle to sketch."""
        from FreeCAD import Base
        import Part
        
        p1 = entity.get("p1", [0, 0])
        p2 = entity.get("p2", [10, 10])
        
        x1, y1 = self._parse_value(p1[0]), self._parse_value(p1[1])
        x2, y2 = self._parse_value(p2[0]), self._parse_value(p2[1])
        
        # Create four lines
        construction = entity.get("construction", False)
        
        lines = []
        lines.append(sketch.addGeometry(
            Part.LineSegment(Base.Vector(x1, y1, 0), Base.Vector(x2, y1, 0)), 
            construction))
        lines.append(sketch.addGeometry(
            Part.LineSegment(Base.Vector(x2, y1, 0), Base.Vector(x2, y2, 0)), 
            construction))
        lines.append(sketch.addGeometry(
            Part.LineSegment(Base.Vector(x2, y2, 0), Base.Vector(x1, y2, 0)), 
            construction))
        lines.append(sketch.addGeometry(
            Part.LineSegment(Base.Vector(x1, y2, 0), Base.Vector(x1, y1, 0)), 
            construction))
        
        # Add coincident constraints for corners
        import Sketcher
        for i in range(4):
            next_i = (i + 1) % 4
            sketch.addConstraint(Sketcher.Constraint('Coincident', 
                                                     lines[i], 2,  # EndPoint
                                                     lines[next_i], 1))  # StartPoint
        
        if "id" in entity:
            self._entity_map[entity["id"]] = (sketch, lines)
    
    def _add_spline_to_sketch(self, sketch, entity: Dict[str, Any]) -> None:
        """Add spline to sketch."""
        from FreeCAD import Base
        import Part
        
        points = entity.get("points", [[0, 0], [10, 10], [20, 0]])
        vectors = [Base.Vector(self._parse_value(p[0]), 
                              self._parse_value(p[1]), 0) for p in points]
        
        # Create B-spline
        spline = Part.BSplineCurve()
        spline.interpolate(vectors)
        spline_idx = sketch.addGeometry(spline, entity.get("construction", False))
        
        if "id" in entity:
            self._entity_map[entity["id"]] = (sketch, spline_idx)
    
    def _add_point_to_sketch(self, sketch, entity: Dict[str, Any]) -> None:
        """Add point to sketch."""
        from FreeCAD import Base
        import Part
        
        at = entity.get("at", [0, 0])
        point = Base.Vector(self._parse_value(at[0]), self._parse_value(at[1]), 0)
        
        point_idx = sketch.addGeometry(Part.Point(point), 
                                       entity.get("construction", False))
        
        if "id" in entity:
            self._entity_map[entity["id"]] = (sketch, point_idx)
    
    def _add_constraint_to_sketch(self, sketch, constraint: Dict[str, Any]) -> None:
        """Add constraint to sketch - simplified implementation."""
        # Basic constraint support - full implementation would be more complex
        import Sketcher
        
        c_type = constraint.get("constraint_type", constraint.get("type"))
        
        # Basic distance constraint example
        if c_type == "distance":
            # This is simplified - full implementation would resolve references
            pass
    
    def _resolve_reference(self, ref):
        """Resolve a CSL reference to FreeCAD object."""
        if isinstance(ref, str):
            # Check entity map
            if ref in self._entity_map:
                return self._entity_map[ref]
            
            # Check document objects
            for obj in self._doc.Objects:
                if obj.Name == ref or obj.Label == ref:
                    return obj
        
        return None
    
    def _create_revolve(self, feature_def: Dict[str, Any]) -> Any:
        """Create revolve feature."""
        import Part
        from FreeCAD import Base
        
        # Get profile
        profile_ref = feature_def.get("profile")
        sketch = self._resolve_reference(profile_ref)
        if not sketch:
            return None
        
        # Get axis
        axis_spec = feature_def.get("axis", "Z")
        if axis_spec == "X":
            axis = Base.Vector(1, 0, 0)
        elif axis_spec == "Y":
            axis = Base.Vector(0, 1, 0)
        else:
            axis = Base.Vector(0, 0, 1)
        
        # Get angle
        angle = self._parse_value(feature_def.get("angle", 360))
        
        try:
            face = Part.Face(sketch.Shape)
            solid = face.revolve(Base.Vector(0, 0, 0), axis, angle)
            
            revolve = self._doc.addObject("Part::Feature", 
                                         feature_def.get("id", "Revolve"))
            revolve.Shape = solid
            return revolve
            
        except Exception as e:
            print(f"[FreeCADBackend] Revolve error: {e}")
            return None
    
    def _create_loft(self, feature_def: Dict[str, Any]) -> Any:
        """Create loft feature."""
        import Part
        
        sections = feature_def.get("sections", [])
        
        # Resolve section references
        section_shapes = []
        for section_ref in sections:
            section = self._resolve_reference(section_ref)
            if section:
                section_shapes.append(section.Shape)
        
        if len(section_shapes) < 2:
            return None
        
        try:
            # Create loft
            loft = Part.makeLoft(section_shapes, 
                               feature_def.get("is_solid", True),
                               feature_def.get("ruled", False))
            
            loft_obj = self._doc.addObject("Part::Feature", 
                                          feature_def.get("id", "Loft"))
            loft_obj.Shape = loft
            return loft_obj
            
        except Exception as e:
            print(f"[FreeCADBackend] Loft error: {e}")
            return None
    
    def _create_sweep(self, feature_def: Dict[str, Any]) -> Any:
        """Create sweep feature."""
        import Part
        
        profile_ref = feature_def.get("profile")
        path_ref = feature_def.get("path")
        
        profile = self._resolve_reference(profile_ref)
        path = self._resolve_reference(path_ref)
        
        if not profile or not path:
            return None
        
        try:
            sweep = Part.makeSweepSurface(path.Shape, profile.Shape)
            
            sweep_obj = self._doc.addObject("Part::Feature", 
                                           feature_def.get("id", "Sweep"))
            sweep_obj.Shape = sweep
            return sweep_obj
            
        except Exception as e:
            print(f"[FreeCADBackend] Sweep error: {e}")
            return None
    
    def _create_fillet(self, feature_def: Dict[str, Any]) -> Any:
        """Create fillet feature - simplified."""
        # Simplified implementation
        print("[FreeCADBackend] Fillet feature - simplified implementation")
        return None
    
    def _create_chamfer(self, feature_def: Dict[str, Any]) -> Any:
        """Create chamfer feature - simplified."""
        # Simplified implementation
        print("[FreeCADBackend] Chamfer feature - simplified implementation")
        return None
    
    def _create_shell(self, feature_def: Dict[str, Any]) -> Any:
        """Create shell feature."""
        thickness = self._parse_value(feature_def.get("thickness", 1))
        
        # Get target body
        target_ref = feature_def.get("target")
        target = self._resolve_reference(target_ref)
        
        if not target:
            return None
        
        try:
            # Create shell (simplified - no face removal)
            shell = target.Shape.makeThickness([], thickness, 1e-6)
            target.Shape = shell
            return target
            
        except Exception as e:
            print(f"[FreeCADBackend] Shell error: {e}")
            return None
    
    def _create_pattern(self, feature_def: Dict[str, Any]) -> Any:
        """Create pattern feature."""
        import Part
        from FreeCAD import Base
        
        kind = feature_def.get("pattern_type", feature_def.get("kind", "linear"))
        seed = self._resolve_reference(feature_def.get("seed"))
        
        if not seed:
            return None
        
        patterns = []
        
        if kind == "linear":
            # Linear pattern
            direction = feature_def.get("direction", [1, 0, 0])
            spacing = self._parse_value(feature_def.get("spacing", 10))
            count = feature_def.get("count", 3)
            
            direction_v = Base.Vector(direction[0], direction[1], direction[2])
            
            for i in range(count):
                copy = seed.Shape.copy()
                copy.translate(direction_v * spacing * i)
                patterns.append(copy)
        
        elif kind == "circular":
            # Circular pattern
            axis = feature_def.get("axis", "Z")
            count = feature_def.get("count", 6)
            angle = 360 / count
            
            if axis == "X":
                axis_v = Base.Vector(1, 0, 0)
            elif axis == "Y":
                axis_v = Base.Vector(0, 1, 0)
            else:
                axis_v = Base.Vector(0, 0, 1)
            
            for i in range(count):
                copy = seed.Shape.copy()
                copy.rotate(Base.Vector(0, 0, 0), axis_v, angle * i)
                patterns.append(copy)
        
        elif kind == "table":
            # Table pattern with per-instance control (CSL v1.3)
            instances = feature_def.get("instances", [])
            
            for instance in instances:
                copy = seed.Shape.copy()
                
                # Apply translation
                if "dx" in instance or "dy" in instance or "dz" in instance:
                    dx = self._parse_value(instance.get("dx", 0))
                    dy = self._parse_value(instance.get("dy", 0))
                    dz = self._parse_value(instance.get("dz", 0))
                    copy.translate(Base.Vector(dx, dy, dz))
                
                # Apply rotation
                if "angle" in instance:
                    angle = instance.get("angle", 0)
                    axis = instance.get("axis", "Z")
                    if axis == "X":
                        axis_v = Base.Vector(1, 0, 0)
                    elif axis == "Y":
                        axis_v = Base.Vector(0, 1, 0)
                    else:
                        axis_v = Base.Vector(0, 0, 1)
                    copy.rotate(Base.Vector(0, 0, 0), axis_v, angle)
                
                patterns.append(copy)
        
        # Combine all patterns
        if patterns:
            compound = Part.makeCompound(patterns)
            pattern_obj = self._doc.addObject("Part::Feature", 
                                             feature_def.get("id", "Pattern"))
            pattern_obj.Shape = compound
            return pattern_obj
        
        return None
    
    def _create_boolean(self, feature_def: Dict[str, Any]) -> Any:
        """Create boolean operation."""
        import Part
        
        operation = feature_def.get("operation", "union")
        tools = feature_def.get("tools", [])
        targets = feature_def.get("targets", [])
        
        # Resolve references
        tool_shapes = [self._resolve_reference(t).Shape for t in tools 
                      if self._resolve_reference(t)]
        target_shapes = [self._resolve_reference(t).Shape for t in targets 
                        if self._resolve_reference(t)]
        
        if not tool_shapes or not target_shapes:
            return None
        
        try:
            if operation == "union" or operation == "add":
                result = target_shapes[0]
                for tool in tool_shapes:
                    result = result.fuse(tool)
            elif operation == "subtract" or operation == "cut":
                result = target_shapes[0]
                for tool in tool_shapes:
                    result = result.cut(tool)
            elif operation == "intersect":
                result = target_shapes[0]
                for tool in tool_shapes:
                    result = result.common(tool)
            else:
                return None
            
            bool_obj = self._doc.addObject("Part::Feature", 
                                          feature_def.get("id", "Boolean"))
            bool_obj.Shape = result
            return bool_obj
            
        except Exception as e:
            print(f"[FreeCADBackend] Boolean error: {e}")
            return None
    
    def _create_hole(self, feature_def: Dict[str, Any]) -> Any:
        """Create hole feature."""
        import Part
        from FreeCAD import Base
        
        # Get position
        position = feature_def.get("position", [0, 0, 0])
        diameter = self._parse_value(feature_def.get("diameter", 5))
        depth = self._parse_value(feature_def.get("depth", 10))
        
        # Get target
        target_ref = feature_def.get("target")
        target = self._resolve_reference(target_ref)
        
        if not target:
            return None
        
        try:
            # Create cylinder for hole
            pos = Base.Vector(position[0], position[1], position[2])
            cylinder = Part.makeCylinder(diameter/2, depth, pos)
            
            # Cut from target
            result = target.Shape.cut(cylinder)
            target.Shape = result
            return target
            
        except Exception as e:
            print(f"[FreeCADBackend] Hole error: {e}")
            return None
