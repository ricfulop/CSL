---
url: https://freecad.github.io/SourceDoc/d5/d71/classconfig__control__design_1_1trimmed__curve.html
scraped_at: 2025-09-08T15:24:20.882116
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [config_control_design](../../d4/d07/namespaceconfig__control__design.html)
  * [trimmed_curve](../../d5/d71/classconfig__control__design_1_1trimmed__curve.html)

[List of all members](../../da/dff/classconfig__control__design_1_1trimmed__curve-members.html) | Public Member Functions | Public Attributes

config_control_design.trimmed_curve Class Reference

##  Public Member Functions  
  
---  
def | [basis_curve](../../d5/d71/classconfig__control__design_1_1trimmed__curve.html#ad1f9959e91bd9828c0265a819559656a) ()  
def | [master_representation](../../d5/d71/classconfig__control__design_1_1trimmed__curve.html#aa801294bfac004f548606b163e747859) ()  
def | [sense_agreement](../../d5/d71/classconfig__control__design_1_1trimmed__curve.html#a7afc78d53787dad74f4343dce42ced49) ()  
def | [trim_1](../../d5/d71/classconfig__control__design_1_1trimmed__curve.html#ab63983ae56e6fb446a669d026acd1dff) ()  
def | [trim_2](../../d5/d71/classconfig__control__design_1_1trimmed__curve.html#a6342ec0c6833700114f184b7d65ffcfe) ()  
def | [wr1](../../d5/d71/classconfig__control__design_1_1trimmed__curve.html#a2b4039eecdc53fc8dcb5cf94498f84dc) (self)  
def | [wr2](../../d5/d71/classconfig__control__design_1_1trimmed__curve.html#a1248d552b60bd615bc5608f122396e95) (self)  
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
[basis_curve](../../d5/d71/classconfig__control__design_1_1trimmed__curve.html#a454dbd238ce913de37ca96f05e35eaf9)  
|
[master_representation](../../d5/d71/classconfig__control__design_1_1trimmed__curve.html#aee6252fd9df82fdbfd382ed861d09b61)  
|
[sense_agreement](../../d5/d71/classconfig__control__design_1_1trimmed__curve.html#a0050c0eac57e6d5a21373f6fa1d721ff)  
|
[trim_1](../../d5/d71/classconfig__control__design_1_1trimmed__curve.html#a3febe37dcb3f5b273a3347ed29bf3ec6)  
|
[trim_2](../../d5/d71/classconfig__control__design_1_1trimmed__curve.html#a4b77b6124d1c00a3bd80b22441b5e23e)  
![-](../../closed.png) Public Attributes inherited from
[config_control_design.representation_item](../../d9/d69/classconfig__control__design_1_1representation__item.html)  
|
[name](../../d9/d69/classconfig__control__design_1_1representation__item.html#a0e8be677f8410825a46422f3c0e1c128)  
  
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

def config_control_design.trimmed_curve.basis_curve  | ( | | ) |   
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

def config_control_design.trimmed_curve.master_representation  | ( | | ) |   
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

def config_control_design.trimmed_curve.sense_agreement  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.trimmed_curve._sense_agreement,
automotive_design.trimmed_curve._sense_agreement, and
config_control_design.trimmed_curve._sense_agreement.

## ◆ trim_1()

def config_control_design.trimmed_curve.trim_1  | ( | | ) |   
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

def config_control_design.trimmed_curve.trim_2  | ( | | ) |   
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

def config_control_design.trimmed_curve.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[config_control_design.geometric_representation_item](../../d3/d18/classconfig__control__design_1_1geometric__representation__item.html#a779ebde9495ea4132b585e06aa418f13).

References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.trimmed_curve.trim_1,
[automotive_design.trimmed_curve.trim_1](../../de/d2b/classautomotive__design_1_1trimmed__curve.html#a9ca12d95a60745a932eb146b710ed287),
and
[config_control_design.trimmed_curve.trim_1](../../d5/d71/classconfig__control__design_1_1trimmed__curve.html#a3febe37dcb3f5b273a3347ed29bf3ec6).

## ◆ wr2()

def config_control_design.trimmed_curve.wr2  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.trimmed_curve.trim_2,
[automotive_design.trimmed_curve.trim_2](../../de/d2b/classautomotive__design_1_1trimmed__curve.html#a64f1227e4475762bd811e5f60be764ad),
and
[config_control_design.trimmed_curve.trim_2](../../d5/d71/classconfig__control__design_1_1trimmed__curve.html#a4b77b6124d1c00a3bd80b22441b5e23e).

## Member Data Documentation

## ◆ basis_curve

config_control_design.trimmed_curve.basis_curve  
---  
  
## ◆ master_representation

config_control_design.trimmed_curve.master_representation  
---  
  
Referenced by
[automotive_design.surface_curve.wr2()](../../dd/dd4/classautomotive__design_1_1surface__curve.html#a666ba9430333277fdc71387682655a19),
[config_control_design.surface_curve.wr2()](../../db/d04/classconfig__control__design_1_1surface__curve.html#ac972c456bb3b774f17987a843b62ac1f),
[automotive_design.surface_curve.wr3()](../../dd/dd4/classautomotive__design_1_1surface__curve.html#a2b1b167aaad85df93f2693542797516b),
and
[config_control_design.surface_curve.wr3()](../../db/d04/classconfig__control__design_1_1surface__curve.html#a82693e1b45e4ec57fe4baf615b283d12).

## ◆ sense_agreement

config_control_design.trimmed_curve.sense_agreement  
---  
  
## ◆ trim_1

config_control_design.trimmed_curve.trim_1  
---  
  
Referenced by
[automotive_design.trimmed_curve.wr1()](../../de/d2b/classautomotive__design_1_1trimmed__curve.html#ae29181ff818c1daacb9da2795108b9f3),
and
[config_control_design.trimmed_curve.wr1()](../../d5/d71/classconfig__control__design_1_1trimmed__curve.html#a2b4039eecdc53fc8dcb5cf94498f84dc).

## ◆ trim_2

config_control_design.trimmed_curve.trim_2  
---  
  
Referenced by
[automotive_design.trimmed_curve.wr2()](../../de/d2b/classautomotive__design_1_1trimmed__curve.html#a1295bbb45cec079b9ef7726b527d33d2),
and
[config_control_design.trimmed_curve.wr2()](../../d5/d71/classconfig__control__design_1_1trimmed__curve.html#a1248d552b60bd615bc5608f122396e95).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/config_control_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

