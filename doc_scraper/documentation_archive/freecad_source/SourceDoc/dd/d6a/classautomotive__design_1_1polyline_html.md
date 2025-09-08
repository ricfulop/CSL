---
url: https://freecad.github.io/SourceDoc/dd/d6a/classautomotive__design_1_1polyline.html
scraped_at: 2025-09-08T15:09:59.199784
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [polyline](../../dd/d6a/classautomotive__design_1_1polyline.html)

[List of all members](../../d9/d00/classautomotive__design_1_1polyline-members.html) | Public Member Functions | Public Attributes

automotive_design.polyline Class Reference

##  Public Member Functions  
  
---  
def | [points](../../dd/d6a/classautomotive__design_1_1polyline.html#aeca1629410c11b6e4b6fe3f15ec33971) ()  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.geometric_representation_item](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html)  
def | [dim](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html#aef245618450610e88788dcaea46ad742) ()  
def | [wr1](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html#a9677d2be5fc5c7c8ccb6819380198bbc) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
def | [name](../../d3/d20/classautomotive__design_1_1representation__item.html#a33b5812d92aa0d107b4fd4274c17b9d9) ()  
def | [wr1](../../d3/d20/classautomotive__design_1_1representation__item.html#af350c19fc5e5763d4991494a99d979ed) (self)  
  
##  Public Attributes  
  
---  
|
[points](../../dd/d6a/classautomotive__design_1_1polyline.html#a7869ee5769747722642e5c95fd978000)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
|
[name](../../d3/d20/classautomotive__design_1_1representation__item.html#a3d48fe912053adaf5f187b606fa81c87)  
  
## Detailed Description

    
    
    Entity polyline definition.
    
        :param points
        :type points:LIST(2,None,'cartesian_point', scope = schema_scope)

## Member Function Documentation

## ◆ points()

def automotive_design.polyline.points  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.polyline._points,
automotive_design.polyline._points, config_control_design.polyline._points,
ifc2x3.ifcpolyline._points, ifc4.ifcpolyline._points,
MeshCore::MeshBuilder._points, and
MeshCore::AbstractPolygonTriangulator._points.

Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[draftguitools.gui_arcs.Arc_3Points.drawArc()](../../d4/d32/classdraftguitools_1_1gui__arcs_1_1Arc__3Points.html#ad2b5ab087c3acf911c62b7d6816bd083),
[draftguitools.gui_arcs.Arc_3Points.getPoint()](../../d4/d32/classdraftguitools_1_1gui__arcs_1_1Arc__3Points.html#addd65326b504c7bf765526ef2db14321),
[ArchCurtainWall.CommandArchCurtainWall.getPoint()](../../d3/d55/classArchCurtainWall_1_1CommandArchCurtainWall.html#ae21c6277cadac9992ad426960f203392),
[ArchTruss.CommandArchTruss.getPoint()](../../dc/d2c/classArchTruss_1_1CommandArchTruss.html#aee560d06232a65dbd5f410bcac5c0318),
[draftguitools.gui_trackers.bsplineTracker.recompute()](../../d4/d09/classdraftguitools_1_1gui__trackers_1_1bsplineTracker.html#a5d3df8a04be660bfc6a6e6613285c145),
[draftguitools.gui_trackers.bezcurveTracker.recompute()](../../d5/da5/classdraftguitools_1_1gui__trackers_1_1bezcurveTracker.html#abb21c673d4078ec0eafdaa2ce727520d),
[draftguitools.gui_trackers.bsplineTracker.update()](../../d4/d09/classdraftguitools_1_1gui__trackers_1_1bsplineTracker.html#a780d90044fb459aa47487afc9d7979c9),
[draftguitools.gui_trackers.bezcurveTracker.update()](../../d5/da5/classdraftguitools_1_1gui__trackers_1_1bezcurveTracker.html#a768d7d59cf62a7cfe8fbdc4486a17a63),
[automotive_design.advanced_face.wr10()](../../d1/d62/classautomotive__design_1_1advanced__face.html#aa08adf112660acfb17f4847e837bdf6d),
and
[config_control_design.advanced_face.wr10()](../../db/d65/classconfig__control__design_1_1advanced__face.html#a0118e22d47858317fa0dff7407854d05).

## Member Data Documentation

## ◆ points

automotive_design.polyline.points  
---  
  
Referenced by
[ArchStructure.CommandStructuralSystem.Activated()](../../d7/da2/classArchStructure_1_1CommandStructuralSystem.html#ad9fb6a22ed31e00ef9c24c49d987d59c),
[draftguitools.gui_arcs.Arc_3Points.drawArc()](../../d4/d32/classdraftguitools_1_1gui__arcs_1_1Arc__3Points.html#ad2b5ab087c3acf911c62b7d6816bd083),
[draftguitools.gui_arcs.Arc_3Points.getPoint()](../../d4/d32/classdraftguitools_1_1gui__arcs_1_1Arc__3Points.html#addd65326b504c7bf765526ef2db14321),
[ArchCurtainWall.CommandArchCurtainWall.getPoint()](../../d3/d55/classArchCurtainWall_1_1CommandArchCurtainWall.html#ae21c6277cadac9992ad426960f203392),
[ArchTruss.CommandArchTruss.getPoint()](../../dc/d2c/classArchTruss_1_1CommandArchTruss.html#aee560d06232a65dbd5f410bcac5c0318),
[draftguitools.gui_trackers.bsplineTracker.recompute()](../../d4/d09/classdraftguitools_1_1gui__trackers_1_1bsplineTracker.html#a5d3df8a04be660bfc6a6e6613285c145),
[draftguitools.gui_trackers.bezcurveTracker.recompute()](../../d5/da5/classdraftguitools_1_1gui__trackers_1_1bezcurveTracker.html#abb21c673d4078ec0eafdaa2ce727520d),
[draftguitools.gui_trackers.bsplineTracker.update()](../../d4/d09/classdraftguitools_1_1gui__trackers_1_1bsplineTracker.html#a780d90044fb459aa47487afc9d7979c9),
[draftguitools.gui_trackers.bezcurveTracker.update()](../../d5/da5/classdraftguitools_1_1gui__trackers_1_1bezcurveTracker.html#a768d7d59cf62a7cfe8fbdc4486a17a63),
[automotive_design.advanced_face.wr10()](../../d1/d62/classautomotive__design_1_1advanced__face.html#aa08adf112660acfb17f4847e837bdf6d),
and
[config_control_design.advanced_face.wr10()](../../db/d65/classconfig__control__design_1_1advanced__face.html#a0118e22d47858317fa0dff7407854d05).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

