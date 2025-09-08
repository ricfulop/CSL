---
url: https://freecad.github.io/SourceDoc/db/d17/classconfig__control__design_1_1polyline.html
scraped_at: 2025-09-08T15:23:05.547605
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [config_control_design](../../d4/d07/namespaceconfig__control__design.html)
  * [polyline](../../db/d17/classconfig__control__design_1_1polyline.html)

[List of all members](../../d1/d59/classconfig__control__design_1_1polyline-members.html) | Public Member Functions | Public Attributes

config_control_design.polyline Class Reference

##  Public Member Functions  
  
---  
def | [points](../../db/d17/classconfig__control__design_1_1polyline.html#a6f56c8a51a84f02e7acefb7e8f332d0a) ()  
![-](../../closed.png) Public Member Functions inherited from
[config_control_design.geometric_representation_item](../../d3/d18/classconfig__control__design_1_1geometric__representation__item.html)  
def | [dim](../../d3/d18/classconfig__control__design_1_1geometric__representation__item.html#aac385fb99d009b699d0d77f10ebdc5f1) ()  
def | [wr1](../../d3/d18/classconfig__control__design_1_1geometric__representation__item.html#a779ebde9495ea4132b585e06aa418f13) (self)  
![-](../../closed.png) Public Member Functions inherited from
[config_control_design.representation_item](../../d9/d69/classconfig__control__design_1_1representation__item.html)  
def | [name](../../d9/d69/classconfig__control__design_1_1representation__item.html#a5ea878073c85170f328deff23a9c5732) ()  
def | [wr1](../../d9/d69/classconfig__control__design_1_1representation__item.html#a4cdc1db49341dedc8f271ec89801c713) (self)  
  
##  Public Attributes  
  
---  
|
[points](../../db/d17/classconfig__control__design_1_1polyline.html#a9f08e8c099ff25df034677ca60852e89)  
![-](../../closed.png) Public Attributes inherited from
[config_control_design.representation_item](../../d9/d69/classconfig__control__design_1_1representation__item.html)  
|
[name](../../d9/d69/classconfig__control__design_1_1representation__item.html#a0e8be677f8410825a46422f3c0e1c128)  
  
## Detailed Description

    
    
    Entity polyline definition.
    
        :param points
        :type points:LIST(2,None,'cartesian_point', scope = schema_scope)

## Member Function Documentation

## ◆ points()

def config_control_design.polyline.points  | ( | | ) |   
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

config_control_design.polyline.points  
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

  * FreeCAD/src/Mod/Import/App/config_control_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

