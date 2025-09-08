---
url: https://freecad.github.io/SourceDoc/dd/d28/classautomotive__design_1_1gear__pair__range.html
scraped_at: 2025-09-08T15:05:51.185861
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [gear_pair_range](../../dd/d28/classautomotive__design_1_1gear__pair__range.html)

[List of all members](../../d5/d2b/classautomotive__design_1_1gear__pair__range-members.html) | Public Member Functions | Public Attributes

automotive_design.gear_pair_range Class Reference

##  Public Member Functions  
  
---  
def | [lower_limit_actual_rotation_1](../../dd/d28/classautomotive__design_1_1gear__pair__range.html#a9520c3409a063de8696d6782eff6ed4c) ()  
def | [simple_pair_range_applies_to_pair](../../dd/d28/classautomotive__design_1_1gear__pair__range.html#a10ec3569adb7f117ab2bc65339a0cb98) ()  
def | [upper_limit_actual_rotation_1](../../dd/d28/classautomotive__design_1_1gear__pair__range.html#acb5eb002ee7efc52be2599335c6901be) ()  
def | [wr1](../../dd/d28/classautomotive__design_1_1gear__pair__range.html#ac99c26ae4556797b93317565210d6c96) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.simple_pair_range](../../d3/d35/classautomotive__design_1_1simple__pair__range.html)  
def | [applies_to_pair](../../d3/d35/classautomotive__design_1_1simple__pair__range.html#a34d466ba4abfc972eddb7542a66e3865) ()  
  
##  Public Attributes  
  
---  
|
[lower_limit_actual_rotation_1](../../dd/d28/classautomotive__design_1_1gear__pair__range.html#a009bc4ece3925f52d9cb289d29cfef7d)  
|
[simple_pair_range_applies_to_pair](../../dd/d28/classautomotive__design_1_1gear__pair__range.html#acf9949c8076fcd2c5fd436ba9b6054e1)  
|
[upper_limit_actual_rotation_1](../../dd/d28/classautomotive__design_1_1gear__pair__range.html#afbc0b62c839efc5dada1c1a8c948cdfb)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.simple_pair_range](../../d3/d35/classautomotive__design_1_1simple__pair__range.html)  
|
[applies_to_pair](../../d3/d35/classautomotive__design_1_1simple__pair__range.html#a482e1ee88d0745baefe27406e3b45d03)  
  
## Detailed Description

    
    
    Entity gear_pair_range definition.
    
        :param simple_pair_range_applies_to_pair
        :type simple_pair_range_applies_to_pair:gear_pair
    
        :param lower_limit_actual_rotation_1
        :type lower_limit_actual_rotation_1:rotational_range_measure
    
        :param upper_limit_actual_rotation_1
        :type upper_limit_actual_rotation_1:rotational_range_measure

## Member Function Documentation

## ◆ lower_limit_actual_rotation_1()

def automotive_design.gear_pair_range.lower_limit_actual_rotation_1  | ( | | ) |   
---|---|---|---|---  
  
References automotive_design.gear_pair_range._lower_limit_actual_rotation_1,
and
[automotive_design.rotational_range_measure](../../d4/ddf/namespaceautomotive__design.html#af1663e07041fb01b2d9c1d995f3ae0dc).

Referenced by
[automotive_design.gear_pair_range.wr1()](../../dd/d28/classautomotive__design_1_1gear__pair__range.html#ac99c26ae4556797b93317565210d6c96).

## ◆ simple_pair_range_applies_to_pair()

def automotive_design.gear_pair_range.simple_pair_range_applies_to_pair  | ( | | ) |   
---|---|---|---|---  
  
References
automotive_design.planar_curve_pair_range._simple_pair_range_applies_to_pair,
automotive_design.point_on_planar_curve_pair_range._simple_pair_range_applies_to_pair,
automotive_design.planar_pair_range._simple_pair_range_applies_to_pair,
automotive_design.cylindrical_pair_range._simple_pair_range_applies_to_pair,
automotive_design.universal_pair_range._simple_pair_range_applies_to_pair,
automotive_design.spherical_pair_range._simple_pair_range_applies_to_pair,
automotive_design.gear_pair_range._simple_pair_range_applies_to_pair,
automotive_design.screw_pair_range._simple_pair_range_applies_to_pair,
automotive_design.surface_pair_range._simple_pair_range_applies_to_pair,
automotive_design.rack_and_pinion_pair_range._simple_pair_range_applies_to_pair,
automotive_design.point_on_surface_pair_range._simple_pair_range_applies_to_pair,
automotive_design.prismatic_pair_range._simple_pair_range_applies_to_pair, and
automotive_design.revolute_pair_range._simple_pair_range_applies_to_pair.

## ◆ upper_limit_actual_rotation_1()

def automotive_design.gear_pair_range.upper_limit_actual_rotation_1  | ( | | ) |   
---|---|---|---|---  
  
References automotive_design.gear_pair_range._upper_limit_actual_rotation_1,
and
[automotive_design.rotational_range_measure](../../d4/ddf/namespaceautomotive__design.html#af1663e07041fb01b2d9c1d995f3ae0dc).

Referenced by
[automotive_design.gear_pair_range.wr1()](../../dd/d28/classautomotive__design_1_1gear__pair__range.html#ac99c26ae4556797b93317565210d6c96).

## ◆ wr1()

def automotive_design.gear_pair_range.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[automotive_design.gear_pair_range.lower_limit_actual_rotation_1](../../dd/d28/classautomotive__design_1_1gear__pair__range.html#a009bc4ece3925f52d9cb289d29cfef7d),
and
[automotive_design.gear_pair_range.upper_limit_actual_rotation_1](../../dd/d28/classautomotive__design_1_1gear__pair__range.html#afbc0b62c839efc5dada1c1a8c948cdfb).

## Member Data Documentation

## ◆ lower_limit_actual_rotation_1

automotive_design.gear_pair_range.lower_limit_actual_rotation_1  
---  
  
Referenced by
[automotive_design.gear_pair_range.wr1()](../../dd/d28/classautomotive__design_1_1gear__pair__range.html#ac99c26ae4556797b93317565210d6c96).

## ◆ simple_pair_range_applies_to_pair

automotive_design.gear_pair_range.simple_pair_range_applies_to_pair  
---  
  
## ◆ upper_limit_actual_rotation_1

automotive_design.gear_pair_range.upper_limit_actual_rotation_1  
---  
  
Referenced by
[automotive_design.gear_pair_range.wr1()](../../dd/d28/classautomotive__design_1_1gear__pair__range.html#ac99c26ae4556797b93317565210d6c96).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

