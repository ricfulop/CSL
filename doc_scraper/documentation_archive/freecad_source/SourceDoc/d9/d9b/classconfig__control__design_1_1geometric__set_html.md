---
url: https://freecad.github.io/SourceDoc/d9/d9b/classconfig__control__design_1_1geometric__set.html
scraped_at: 2025-09-08T15:22:00.256032
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [config_control_design](../../d4/d07/namespaceconfig__control__design.html)
  * [geometric_set](../../d9/d9b/classconfig__control__design_1_1geometric__set.html)

[List of all members](../../d6/d68/classconfig__control__design_1_1geometric__set-members.html) | Public Member Functions | Public Attributes

config_control_design.geometric_set Class Reference

##  Public Member Functions  
  
---  
def | [elements](../../d9/d9b/classconfig__control__design_1_1geometric__set.html#a32edf54f7a2c95fab79e6942221dce89) ()  
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
[elements](../../d9/d9b/classconfig__control__design_1_1geometric__set.html#a7340f5f8a0bcbcb9c626e8b79717e667)  
![-](../../closed.png) Public Attributes inherited from
[config_control_design.representation_item](../../d9/d69/classconfig__control__design_1_1representation__item.html)  
|
[name](../../d9/d69/classconfig__control__design_1_1representation__item.html#a0e8be677f8410825a46422f3c0e1c128)  
  
## Detailed Description

    
    
    Entity geometric_set definition.
    
        :param elements
        :type elements:SET(1,None,'geometric_set_select', scope = schema_scope)

## Member Function Documentation

## ◆ elements()

def config_control_design.geometric_set.elements  | ( | | ) |   
---|---|---|---|---  
  
References SMESH_ProxyMesh::SubMesh._elements, ElementBndBoxTree._elements,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.derived_unit._elements,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.data_environment._elements,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.procedural_representation_sequence._elements,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.annotation_plane._elements,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.geometric_set._elements,
automotive_design.data_environment._elements,
automotive_design.derived_unit._elements,
automotive_design.annotation_plane._elements,
automotive_design.geometric_set._elements,
config_control_design.geometric_set._elements,
ifc2x3.ifcgeometricset._elements, ifc2x3.ifcderivedunit._elements,
ifc4.ifcgeometricset._elements, and ifc4.ifcderivedunit._elements.

Referenced by
[ifc2x3.ifcgeometricset.dim()](../../dc/dab/classifc2x3_1_1ifcgeometricset.html#af569a780b93b69b4dce81b08ddd66f89),
[ifc4.ifcgeometricset.dim()](../../d1/d95/classifc4_1_1ifcgeometricset.html#a795b14ef2879e9acc0c066d66e122b9b),
[ifc2x3.ifcderivedunit.dimensions()](../../d1/d87/classifc2x3_1_1ifcderivedunit.html#abfb7d2614cbad7ba363d5b3c5eb5d470),
[ifc4.ifcderivedunit.dimensions()](../../d3/d76/classifc4_1_1ifcderivedunit.html#aa316302961670925c24a6da591f61b31),
[automotive_design.derived_unit.wr1()](../../dc/d0d/classautomotive__design_1_1derived__unit.html#a0f657919a22adecb60367513268f0487),
[ifc2x3.ifcderivedunit.wr1()](../../d1/d87/classifc2x3_1_1ifcderivedunit.html#a9187776e238d15570720320bf6875864),
and
[ifc4.ifcderivedunit.wr1()](../../d3/d76/classifc4_1_1ifcderivedunit.html#a3c29186705cf96c60831affaf117186e).

## Member Data Documentation

## ◆ elements

config_control_design.geometric_set.elements  
---  
  
Referenced by
[ifc2x3.ifcgeometricset.dim()](../../dc/dab/classifc2x3_1_1ifcgeometricset.html#af569a780b93b69b4dce81b08ddd66f89),
[ifc4.ifcgeometricset.dim()](../../d1/d95/classifc4_1_1ifcgeometricset.html#a795b14ef2879e9acc0c066d66e122b9b),
[ifc2x3.ifcderivedunit.dimensions()](../../d1/d87/classifc2x3_1_1ifcderivedunit.html#abfb7d2614cbad7ba363d5b3c5eb5d470),
[ifc4.ifcderivedunit.dimensions()](../../d3/d76/classifc4_1_1ifcderivedunit.html#aa316302961670925c24a6da591f61b31),
[automotive_design.derived_unit.wr1()](../../dc/d0d/classautomotive__design_1_1derived__unit.html#a0f657919a22adecb60367513268f0487),
[ifc2x3.ifcderivedunit.wr1()](../../d1/d87/classifc2x3_1_1ifcderivedunit.html#a9187776e238d15570720320bf6875864),
and
[ifc4.ifcderivedunit.wr1()](../../d3/d76/classifc4_1_1ifcderivedunit.html#a3c29186705cf96c60831affaf117186e).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/config_control_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

