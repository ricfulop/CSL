---
url: https://freecad.github.io/SourceDoc/d4/dea/classautomotive__design_1_1edge__curve.html
scraped_at: 2025-09-08T15:04:38.907719
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [edge_curve](../../d4/dea/classautomotive__design_1_1edge__curve.html)

[List of all members](../../d1/dab/classautomotive__design_1_1edge__curve-members.html) | Public Member Functions | Public Attributes

automotive_design.edge_curve Class Reference

##  Public Member Functions  
  
---  
def | [edge_geometry](../../d4/dea/classautomotive__design_1_1edge__curve.html#ab06e494ab51494afb92ddd52531faac5) ()  
def | [same_sense](../../d4/dea/classautomotive__design_1_1edge__curve.html#addabd08b8a028b293867e0ce84d782ec) ()  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.edge](../../d5/de3/classautomotive__design_1_1edge.html)  
def | [edge_end](../../d5/de3/classautomotive__design_1_1edge.html#adc21d6bea2bf55ae7403d64f2ccdf8ea) ()  
def | [edge_start](../../d5/de3/classautomotive__design_1_1edge.html#afe397bf57aa3052ba73da826700d8b38) ()  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
def | [name](../../d3/d20/classautomotive__design_1_1representation__item.html#a33b5812d92aa0d107b4fd4274c17b9d9) ()  
def | [wr1](../../d3/d20/classautomotive__design_1_1representation__item.html#af350c19fc5e5763d4991494a99d979ed) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.geometric_representation_item](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html)  
def | [dim](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html#aef245618450610e88788dcaea46ad742) ()  
def | [wr1](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html#a9677d2be5fc5c7c8ccb6819380198bbc) (self)  
  
##  Public Attributes  
  
---  
|
[edge_geometry](../../d4/dea/classautomotive__design_1_1edge__curve.html#a1fe12d532a4e5cf61a469f18f8af544e)  
|
[same_sense](../../d4/dea/classautomotive__design_1_1edge__curve.html#aaf86a921c8311dc3f586b349125d9cbb)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.edge](../../d5/de3/classautomotive__design_1_1edge.html)  
|
[edge_end](../../d5/de3/classautomotive__design_1_1edge.html#af2dfde2eea876a40ced85b67041a6078)  
|
[edge_start](../../d5/de3/classautomotive__design_1_1edge.html#acea1eb826a678cc369a23d36bb3b6181)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
|
[name](../../d3/d20/classautomotive__design_1_1representation__item.html#a3d48fe912053adaf5f187b606fa81c87)  
  
## Detailed Description

    
    
    Entity edge_curve definition.
    
        :param edge_geometry
        :type edge_geometry:curve
    
        :param same_sense
        :type same_sense:BOOLEAN

## Member Function Documentation

## ◆ edge_geometry()

def automotive_design.edge_curve.edge_geometry  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.edge_curve._edge_geometry,
automotive_design.edge_curve._edge_geometry, and
config_control_design.edge_curve._edge_geometry.

Referenced by
[automotive_design.seam_edge.wr1()](../../d1/d38/classautomotive__design_1_1seam__edge.html#a6867f7f7e20c40119163b629ca0b1573),
and
[automotive_design.seam_edge.wr2()](../../d1/d38/classautomotive__design_1_1seam__edge.html#a3e9b6478fcf0b0635c010697146a0435).

## ◆ same_sense()

def automotive_design.edge_curve.same_sense  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.composite_curve_segment._same_sense,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.face_surface._same_sense,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.edge_curve._same_sense,
automotive_design.composite_curve_segment._same_sense,
automotive_design.face_surface._same_sense,
automotive_design.edge_curve._same_sense,
config_control_design.composite_curve_segment._same_sense,
config_control_design.face_surface._same_sense, and
config_control_design.edge_curve._same_sense.

## Member Data Documentation

## ◆ edge_geometry

automotive_design.edge_curve.edge_geometry  
---  
  
Referenced by
[automotive_design.seam_edge.wr1()](../../d1/d38/classautomotive__design_1_1seam__edge.html#a6867f7f7e20c40119163b629ca0b1573),
and
[automotive_design.seam_edge.wr2()](../../d1/d38/classautomotive__design_1_1seam__edge.html#a3e9b6478fcf0b0635c010697146a0435).

## ◆ same_sense

automotive_design.edge_curve.same_sense  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

