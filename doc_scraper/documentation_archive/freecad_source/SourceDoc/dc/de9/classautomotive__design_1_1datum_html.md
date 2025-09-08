---
url: https://freecad.github.io/SourceDoc/dc/de9/classautomotive__design_1_1datum.html
scraped_at: 2025-09-08T15:03:18.580671
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [datum](../../dc/de9/classautomotive__design_1_1datum.html)

[List of all members](../../d4/d62/classautomotive__design_1_1datum-members.html) | Public Member Functions | Public Attributes

automotive_design.datum Class Reference

##  Public Member Functions  
  
---  
def | [established_by_relationships](../../dc/de9/classautomotive__design_1_1datum.html#aa7f7d53441e7853f5722ca3c0571e775) ()  
def | [identification](../../dc/de9/classautomotive__design_1_1datum.html#a2d4964b40793238f8eec60b5ab7affa9) ()  
def | [wr1](../../dc/de9/classautomotive__design_1_1datum.html#a4872440557075e2b5b4131f5a5b67b55) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.shape_aspect](../../d5/d43/classautomotive__design_1_1shape__aspect.html)  
def | [description](../../d5/d43/classautomotive__design_1_1shape__aspect.html#a2d3cbacdee4b4a23c48e6e8682be5097) ()  
def | [id](../../d5/d43/classautomotive__design_1_1shape__aspect.html#a908575200aa127fee70d8efefc5ff7b2) ()  
def | [name](../../d5/d43/classautomotive__design_1_1shape__aspect.html#a3497533cc144728ba5eaedf0d315ef72) ()  
def | [of_shape](../../d5/d43/classautomotive__design_1_1shape__aspect.html#a4369599788e3702c80ccf6a2ed9d81fc) ()  
def | [product_definitional](../../d5/d43/classautomotive__design_1_1shape__aspect.html#ae2d34da10e91db476c7445b2525172d4) ()  
def | [wr1](../../d5/d43/classautomotive__design_1_1shape__aspect.html#afaf0ba0242d7b61388638ad5968f48f8) (self)  
  
##  Public Attributes  
  
---  
|
[identification](../../dc/de9/classautomotive__design_1_1datum.html#aa6233acd648bc30c52024fbe1db0a142)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.shape_aspect](../../d5/d43/classautomotive__design_1_1shape__aspect.html)  
|
[description](../../d5/d43/classautomotive__design_1_1shape__aspect.html#afbfbbcdbba354ef8f47480a40487c967)  
|
[name](../../d5/d43/classautomotive__design_1_1shape__aspect.html#a9f75336c7a542a886597e5c1f97e40a8)  
|
[of_shape](../../d5/d43/classautomotive__design_1_1shape__aspect.html#a8968baa97d9b01370bd48e9b013a9b5f)  
|
[product_definitional](../../d5/d43/classautomotive__design_1_1shape__aspect.html#a74f491d0f946e301a43bc04dc72dfd20)  
  
## Detailed Description

    
    
    Entity datum definition.
    
        :param identification
        :type identification:identifier
    
        :param established_by_relationships
        :type established_by_relationships:SET(1,None,'shape_aspect_relationship', scope = schema_scope)

## Member Function Documentation

## ◆ established_by_relationships()

def automotive_design.datum.established_by_relationships  | ( | | ) |   
---|---|---|---|---  
  
## ◆ identification()

def automotive_design.datum.identification  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.datum._identification,
automotive_design.property_process._identification,
automotive_design.product_definition_process._identification,
automotive_design.datum._identification, ifc4.ifctyperesource._identification,
ifc4.ifccontrol._identification, ifc4.ifcexternalreference._identification,
ifc4.ifctypeprocess._identification,
ifc4.ifcdocumentinformation._identification,
ifc4.ifcorganization._identification, ifc4.ifcprocess._identification,
ifc4.ifcresource._identification, ifc4.ifcperson._identification, and
ifc4.ifcasset._identification.

Referenced by
[ifc4.ifcperson.identifiableperson()](../../db/d15/classifc4_1_1ifcperson.html#a8b4262ca3c8e9347557fb1d1c776b7a0),
and
[ifc4.ifcexternalreference.wr1()](../../d5/dd9/classifc4_1_1ifcexternalreference.html#a0e6ba5265c69b44700e8d9b179e9f240).

## ◆ wr1()

def automotive_design.datum.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[automotive_design.shape_aspect](../../d5/d43/classautomotive__design_1_1shape__aspect.html#afaf0ba0242d7b61388638ad5968f48f8).

Reimplemented in
[automotive_design.common_datum](../../db/daa/classautomotive__design_1_1common__datum.html#a4275bf1041071a52c4bfc5220cff01ab).

## Member Data Documentation

## ◆ identification

automotive_design.datum.identification  
---  
  
Referenced by
[ifc4.ifcperson.identifiableperson()](../../db/d15/classifc4_1_1ifcperson.html#a8b4262ca3c8e9347557fb1d1c776b7a0),
and
[ifc4.ifcexternalreference.wr1()](../../d5/dd9/classifc4_1_1ifcexternalreference.html#a0e6ba5265c69b44700e8d9b179e9f240).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

