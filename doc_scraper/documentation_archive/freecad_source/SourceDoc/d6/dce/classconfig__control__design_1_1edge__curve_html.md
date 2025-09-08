---
url: https://freecad.github.io/SourceDoc/d6/dce/classconfig__control__design_1_1edge__curve.html
scraped_at: 2025-09-08T15:21:42.199944
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [config_control_design](../../d4/d07/namespaceconfig__control__design.html)
  * [edge_curve](../../d6/dce/classconfig__control__design_1_1edge__curve.html)

[List of all members](../../d0/d28/classconfig__control__design_1_1edge__curve-members.html) | Public Member Functions | Public Attributes

config_control_design.edge_curve Class Reference

##  Public Member Functions  
  
---  
def | [edge_geometry](../../d6/dce/classconfig__control__design_1_1edge__curve.html#a6ce08f83e9e7875bdbd23412fa66752f) ()  
def | [same_sense](../../d6/dce/classconfig__control__design_1_1edge__curve.html#a2a13af0815ac2da44b46594ceef79d12) ()  
![-](../../closed.png) Public Member Functions inherited from
[config_control_design.edge](../../d5/d3e/classconfig__control__design_1_1edge.html)  
def | [edge_end](../../d5/d3e/classconfig__control__design_1_1edge.html#a147b65a6978977430c46f8ab40b03c08) ()  
def | [edge_start](../../d5/d3e/classconfig__control__design_1_1edge.html#a81ec6e171ce1f0ea828cb717021e6e13) ()  
![-](../../closed.png) Public Member Functions inherited from
[config_control_design.representation_item](../../d9/d69/classconfig__control__design_1_1representation__item.html)  
def | [name](../../d9/d69/classconfig__control__design_1_1representation__item.html#a5ea878073c85170f328deff23a9c5732) ()  
def | [wr1](../../d9/d69/classconfig__control__design_1_1representation__item.html#a4cdc1db49341dedc8f271ec89801c713) (self)  
![-](../../closed.png) Public Member Functions inherited from
[config_control_design.geometric_representation_item](../../d3/d18/classconfig__control__design_1_1geometric__representation__item.html)  
def | [dim](../../d3/d18/classconfig__control__design_1_1geometric__representation__item.html#aac385fb99d009b699d0d77f10ebdc5f1) ()  
def | [wr1](../../d3/d18/classconfig__control__design_1_1geometric__representation__item.html#a779ebde9495ea4132b585e06aa418f13) (self)  
  
##  Public Attributes  
  
---  
|
[edge_geometry](../../d6/dce/classconfig__control__design_1_1edge__curve.html#ad846c5ec98b651c557b736c32944a8cf)  
|
[same_sense](../../d6/dce/classconfig__control__design_1_1edge__curve.html#ae5d3ca0b5b50ff54cd34d0f1e5a92629)  
![-](../../closed.png) Public Attributes inherited from
[config_control_design.edge](../../d5/d3e/classconfig__control__design_1_1edge.html)  
|
[edge_end](../../d5/d3e/classconfig__control__design_1_1edge.html#a888e6fd2eb49c977bb80e57e05e412f5)  
|
[edge_start](../../d5/d3e/classconfig__control__design_1_1edge.html#a59f8150252d3cbc8ffe465d2ecdb0e86)  
![-](../../closed.png) Public Attributes inherited from
[config_control_design.representation_item](../../d9/d69/classconfig__control__design_1_1representation__item.html)  
|
[name](../../d9/d69/classconfig__control__design_1_1representation__item.html#a0e8be677f8410825a46422f3c0e1c128)  
  
## Detailed Description

    
    
    Entity edge_curve definition.
    
        :param edge_geometry
        :type edge_geometry:curve
    
        :param same_sense
        :type same_sense:BOOLEAN

## Member Function Documentation

## ◆ edge_geometry()

def config_control_design.edge_curve.edge_geometry  | ( | | ) |   
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

def config_control_design.edge_curve.same_sense  | ( | | ) |   
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

config_control_design.edge_curve.edge_geometry  
---  
  
Referenced by
[automotive_design.seam_edge.wr1()](../../d1/d38/classautomotive__design_1_1seam__edge.html#a6867f7f7e20c40119163b629ca0b1573),
and
[automotive_design.seam_edge.wr2()](../../d1/d38/classautomotive__design_1_1seam__edge.html#a3e9b6478fcf0b0635c010697146a0435).

## ◆ same_sense

config_control_design.edge_curve.same_sense  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/config_control_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

