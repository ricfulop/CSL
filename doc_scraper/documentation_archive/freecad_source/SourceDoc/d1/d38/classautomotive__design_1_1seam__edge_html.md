---
url: https://freecad.github.io/SourceDoc/d1/d38/classautomotive__design_1_1seam__edge.html
scraped_at: 2025-09-08T15:12:22.846781
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [seam_edge](../../d1/d38/classautomotive__design_1_1seam__edge.html)

[List of all members](../../d8/dcc/classautomotive__design_1_1seam__edge-members.html) | Public Member Functions | Public Attributes

automotive_design.seam_edge Class Reference

##  Public Member Functions  
  
---  
def | [pcurve_reference](../../d1/d38/classautomotive__design_1_1seam__edge.html#a5101a344f2577c32823d96663463a417) ()  
def | [wr1](../../d1/d38/classautomotive__design_1_1seam__edge.html#a6867f7f7e20c40119163b629ca0b1573) (self)  
def | [wr2](../../d1/d38/classautomotive__design_1_1seam__edge.html#a3e9b6478fcf0b0635c010697146a0435) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.oriented_edge](../../df/d78/classautomotive__design_1_1oriented__edge.html)  
def | [edge_edge_end](../../df/d78/classautomotive__design_1_1oriented__edge.html#abd23cb2d3a06df7a099535c627a788ca) ()  
def | [edge_edge_start](../../df/d78/classautomotive__design_1_1oriented__edge.html#aae8227b4329f0ddc4b6b98af1785bbcc) ()  
def | [edge_element](../../df/d78/classautomotive__design_1_1oriented__edge.html#a86854020000731fe77a19ee0b7a5cba4) ()  
def | [orientation](../../df/d78/classautomotive__design_1_1oriented__edge.html#aa89cd8b5b8c38f3012b9cbc2541ec1c9) ()  
def | [wr1](../../df/d78/classautomotive__design_1_1oriented__edge.html#ab057e0e3b994112699bfee82400bb309) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.edge](../../d5/de3/classautomotive__design_1_1edge.html)  
def | [edge_end](../../d5/de3/classautomotive__design_1_1edge.html#adc21d6bea2bf55ae7403d64f2ccdf8ea) ()  
def | [edge_start](../../d5/de3/classautomotive__design_1_1edge.html#afe397bf57aa3052ba73da826700d8b38) ()  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
def | [name](../../d3/d20/classautomotive__design_1_1representation__item.html#a33b5812d92aa0d107b4fd4274c17b9d9) ()  
def | [wr1](../../d3/d20/classautomotive__design_1_1representation__item.html#af350c19fc5e5763d4991494a99d979ed) (self)  
  
##  Public Attributes  
  
---  
|
[pcurve_reference](../../d1/d38/classautomotive__design_1_1seam__edge.html#ae3ed385d9fbd89d384bb52031a84ff61)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.oriented_edge](../../df/d78/classautomotive__design_1_1oriented__edge.html)  
|
[edge_element](../../df/d78/classautomotive__design_1_1oriented__edge.html#a070e25d8dd72fffb2f7212b5f5d83635)  
|
[orientation](../../df/d78/classautomotive__design_1_1oriented__edge.html#acedf3b884b8f3bee4c3278a58b4fe976)  
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

    
    
    Entity seam_edge definition.
    
        :param pcurve_reference
        :type pcurve_reference:pcurve

## Member Function Documentation

## ◆ pcurve_reference()

def automotive_design.seam_edge.pcurve_reference  | ( | | ) |   
---|---|---|---|---  
  
References automotive_design.seam_edge._pcurve_reference.

Referenced by
[automotive_design.seam_edge.wr2()](../../d1/d38/classautomotive__design_1_1seam__edge.html#a3e9b6478fcf0b0635c010697146a0435).

## ◆ wr1()

def automotive_design.seam_edge.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[automotive_design.oriented_edge](../../df/d78/classautomotive__design_1_1oriented__edge.html#ab057e0e3b994112699bfee82400bb309).

References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.oriented_edge.edge_element,
[automotive_design.oriented_edge.edge_element](../../df/d78/classautomotive__design_1_1oriented__edge.html#a070e25d8dd72fffb2f7212b5f5d83635),
[config_control_design.oriented_edge.edge_element](../../da/d77/classconfig__control__design_1_1oriented__edge.html#aa5fcda4a46916e365c8d150b00baff30),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.edge_curve.edge_geometry,
[automotive_design.edge_curve.edge_geometry](../../d4/dea/classautomotive__design_1_1edge__curve.html#a1fe12d532a4e5cf61a469f18f8af544e),
and
[config_control_design.edge_curve.edge_geometry](../../d6/dce/classconfig__control__design_1_1edge__curve.html#ad846c5ec98b651c557b736c32944a8cf).

## ◆ wr2()

def automotive_design.seam_edge.wr2  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_curve.associated_geometry,
[automotive_design.surface_curve.associated_geometry](../../dd/dd4/classautomotive__design_1_1surface__curve.html#a0b784edb8e1c1c89cf424a0a84d7a15d),
[config_control_design.surface_curve.associated_geometry](../../db/d04/classconfig__control__design_1_1surface__curve.html#adc97ffd2c484d9b33e95ead595c77fd1),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.oriented_edge.edge_element,
[automotive_design.oriented_edge.edge_element](../../df/d78/classautomotive__design_1_1oriented__edge.html#a070e25d8dd72fffb2f7212b5f5d83635),
[config_control_design.oriented_edge.edge_element](../../da/d77/classconfig__control__design_1_1oriented__edge.html#aa5fcda4a46916e365c8d150b00baff30),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.edge_curve.edge_geometry,
[automotive_design.edge_curve.edge_geometry](../../d4/dea/classautomotive__design_1_1edge__curve.html#a1fe12d532a4e5cf61a469f18f8af544e),
[config_control_design.edge_curve.edge_geometry](../../d6/dce/classconfig__control__design_1_1edge__curve.html#ad846c5ec98b651c557b736c32944a8cf),
and
[automotive_design.seam_edge.pcurve_reference](../../d1/d38/classautomotive__design_1_1seam__edge.html#ae3ed385d9fbd89d384bb52031a84ff61).

## Member Data Documentation

## ◆ pcurve_reference

automotive_design.seam_edge.pcurve_reference  
---  
  
Referenced by
[automotive_design.seam_edge.wr2()](../../d1/d38/classautomotive__design_1_1seam__edge.html#a3e9b6478fcf0b0635c010697146a0435).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

