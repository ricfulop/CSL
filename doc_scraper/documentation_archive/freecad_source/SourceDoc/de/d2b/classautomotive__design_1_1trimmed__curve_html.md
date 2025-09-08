---
url: https://freecad.github.io/SourceDoc/de/d2b/classautomotive__design_1_1trimmed__curve.html
scraped_at: 2025-09-08T15:14:49.518038
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [trimmed_curve](../../de/d2b/classautomotive__design_1_1trimmed__curve.html)

[List of all members](../../d3/d58/classautomotive__design_1_1trimmed__curve-members.html) | Public Member Functions | Public Attributes

automotive_design.trimmed_curve Class Reference

##  Public Member Functions  
  
---  
def | [basis_curve](../../de/d2b/classautomotive__design_1_1trimmed__curve.html#a7d1764310ae496f6f35bfa986f679235) ()  
def | [master_representation](../../de/d2b/classautomotive__design_1_1trimmed__curve.html#aa3b30a4516bdc5926fc1c4fc6c0f1a50) ()  
def | [sense_agreement](../../de/d2b/classautomotive__design_1_1trimmed__curve.html#aa0b132a57f35812891082d165bb1ae2b) ()  
def | [trim_1](../../de/d2b/classautomotive__design_1_1trimmed__curve.html#aaebda641ab7dd81a10c6a13ae25f9748) ()  
def | [trim_2](../../de/d2b/classautomotive__design_1_1trimmed__curve.html#aa13d7fb0007d39869605af8fbeb5e23d) ()  
def | [wr1](../../de/d2b/classautomotive__design_1_1trimmed__curve.html#ae29181ff818c1daacb9da2795108b9f3) (self)  
def | [wr2](../../de/d2b/classautomotive__design_1_1trimmed__curve.html#a1295bbb45cec079b9ef7726b527d33d2) (self)  
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
[basis_curve](../../de/d2b/classautomotive__design_1_1trimmed__curve.html#ab90f49454fe89df19f98aa7dc7611d87)  
|
[master_representation](../../de/d2b/classautomotive__design_1_1trimmed__curve.html#a797c92353e1bdbf0490bdecc4bb923e8)  
|
[sense_agreement](../../de/d2b/classautomotive__design_1_1trimmed__curve.html#a6830f09637d24b3cd419627b19e5f592)  
|
[trim_1](../../de/d2b/classautomotive__design_1_1trimmed__curve.html#a9ca12d95a60745a932eb146b710ed287)  
|
[trim_2](../../de/d2b/classautomotive__design_1_1trimmed__curve.html#a64f1227e4475762bd811e5f60be764ad)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
|
[name](../../d3/d20/classautomotive__design_1_1representation__item.html#a3d48fe912053adaf5f187b606fa81c87)  
  
## Detailed Description

    
    
    Entity trimmed_curve definition.
    
        :param basis_curve
        :type basis_curve:curve
    
        :param trim_1
        :type trim_1:SET(1,2,'trimming_select', scope = schema_scope)
    
        :param trim_2
        :type trim_2:SET(1,2,'trimming_select', scope = schema_scope)
    
        :param sense_agreement
        :type sense_agreement:BOOLEAN
    
        :param master_representation
        :type master_representation:trimming_preference

## Member Function Documentation

## ◆ basis_curve()

def automotive_design.trimmed_curve.basis_curve  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.offset_curve_3d._basis_curve,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.trimmed_curve._basis_curve,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.point_on_curve._basis_curve,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.offset_curve_2d._basis_curve,
automotive_design.offset_curve_3d._basis_curve,
automotive_design.trimmed_curve._basis_curve,
automotive_design.point_on_curve._basis_curve,
automotive_design.offset_curve_2d._basis_curve,
config_control_design.offset_curve_3d._basis_curve,
config_control_design.trimmed_curve._basis_curve, and
config_control_design.point_on_curve._basis_curve.

## ◆ master_representation()

def automotive_design.trimmed_curve.master_representation  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_curve._master_representation,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.trimmed_curve._master_representation,
automotive_design.surface_curve._master_representation,
automotive_design.trimmed_curve._master_representation,
config_control_design.surface_curve._master_representation, and
config_control_design.trimmed_curve._master_representation.

Referenced by
[automotive_design.surface_curve.wr2()](../../dd/dd4/classautomotive__design_1_1surface__curve.html#a666ba9430333277fdc71387682655a19),
[config_control_design.surface_curve.wr2()](../../db/d04/classconfig__control__design_1_1surface__curve.html#ac972c456bb3b774f17987a843b62ac1f),
[automotive_design.surface_curve.wr3()](../../dd/dd4/classautomotive__design_1_1surface__curve.html#a2b1b167aaad85df93f2693542797516b),
and
[config_control_design.surface_curve.wr3()](../../db/d04/classconfig__control__design_1_1surface__curve.html#a82693e1b45e4ec57fe4baf615b283d12).

## ◆ sense_agreement()

def automotive_design.trimmed_curve.sense_agreement  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.trimmed_curve._sense_agreement,
automotive_design.trimmed_curve._sense_agreement, and
config_control_design.trimmed_curve._sense_agreement.

## ◆ trim_1()

def automotive_design.trimmed_curve.trim_1  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.trimmed_curve._trim_1,
automotive_design.trimmed_curve._trim_1, and
config_control_design.trimmed_curve._trim_1.

Referenced by
[automotive_design.trimmed_curve.wr1()](../../de/d2b/classautomotive__design_1_1trimmed__curve.html#ae29181ff818c1daacb9da2795108b9f3),
and
[config_control_design.trimmed_curve.wr1()](../../d5/d71/classconfig__control__design_1_1trimmed__curve.html#a2b4039eecdc53fc8dcb5cf94498f84dc).

## ◆ trim_2()

def automotive_design.trimmed_curve.trim_2  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.trimmed_curve._trim_2,
automotive_design.trimmed_curve._trim_2, and
config_control_design.trimmed_curve._trim_2.

Referenced by
[automotive_design.trimmed_curve.wr2()](../../de/d2b/classautomotive__design_1_1trimmed__curve.html#a1295bbb45cec079b9ef7726b527d33d2),
and
[config_control_design.trimmed_curve.wr2()](../../d5/d71/classconfig__control__design_1_1trimmed__curve.html#a1248d552b60bd615bc5608f122396e95).

## ◆ wr1()

def automotive_design.trimmed_curve.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[automotive_design.geometric_representation_item](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html#a9677d2be5fc5c7c8ccb6819380198bbc).

References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.trimmed_curve.trim_1,
[automotive_design.trimmed_curve.trim_1](../../de/d2b/classautomotive__design_1_1trimmed__curve.html#a9ca12d95a60745a932eb146b710ed287),
and
[config_control_design.trimmed_curve.trim_1](../../d5/d71/classconfig__control__design_1_1trimmed__curve.html#a3febe37dcb3f5b273a3347ed29bf3ec6).

## ◆ wr2()

def automotive_design.trimmed_curve.wr2  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.trimmed_curve.trim_2,
[automotive_design.trimmed_curve.trim_2](../../de/d2b/classautomotive__design_1_1trimmed__curve.html#a64f1227e4475762bd811e5f60be764ad),
and
[config_control_design.trimmed_curve.trim_2](../../d5/d71/classconfig__control__design_1_1trimmed__curve.html#a4b77b6124d1c00a3bd80b22441b5e23e).

## Member Data Documentation

## ◆ basis_curve

automotive_design.trimmed_curve.basis_curve  
---  
  
## ◆ master_representation

automotive_design.trimmed_curve.master_representation  
---  
  
Referenced by
[automotive_design.surface_curve.wr2()](../../dd/dd4/classautomotive__design_1_1surface__curve.html#a666ba9430333277fdc71387682655a19),
[config_control_design.surface_curve.wr2()](../../db/d04/classconfig__control__design_1_1surface__curve.html#ac972c456bb3b774f17987a843b62ac1f),
[automotive_design.surface_curve.wr3()](../../dd/dd4/classautomotive__design_1_1surface__curve.html#a2b1b167aaad85df93f2693542797516b),
and
[config_control_design.surface_curve.wr3()](../../db/d04/classconfig__control__design_1_1surface__curve.html#a82693e1b45e4ec57fe4baf615b283d12).

## ◆ sense_agreement

automotive_design.trimmed_curve.sense_agreement  
---  
  
## ◆ trim_1

automotive_design.trimmed_curve.trim_1  
---  
  
Referenced by
[automotive_design.trimmed_curve.wr1()](../../de/d2b/classautomotive__design_1_1trimmed__curve.html#ae29181ff818c1daacb9da2795108b9f3),
and
[config_control_design.trimmed_curve.wr1()](../../d5/d71/classconfig__control__design_1_1trimmed__curve.html#a2b4039eecdc53fc8dcb5cf94498f84dc).

## ◆ trim_2

automotive_design.trimmed_curve.trim_2  
---  
  
Referenced by
[automotive_design.trimmed_curve.wr2()](../../de/d2b/classautomotive__design_1_1trimmed__curve.html#a1295bbb45cec079b9ef7726b527d33d2),
and
[config_control_design.trimmed_curve.wr2()](../../d5/d71/classconfig__control__design_1_1trimmed__curve.html#a1248d552b60bd615bc5608f122396e95).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

