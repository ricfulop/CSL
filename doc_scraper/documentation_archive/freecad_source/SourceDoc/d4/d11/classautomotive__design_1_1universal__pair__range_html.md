---
url: https://freecad.github.io/SourceDoc/d4/d11/classautomotive__design_1_1universal__pair__range.html
scraped_at: 2025-09-08T15:15:06.517974
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [universal_pair_range](../../d4/d11/classautomotive__design_1_1universal__pair__range.html)

[List of all members](../../dc/d9e/classautomotive__design_1_1universal__pair__range-members.html) | Public Member Functions | Public Attributes

automotive_design.universal_pair_range Class Reference

##  Public Member Functions  
  
---  
def | [lower_limit_first_rotation](../../d4/d11/classautomotive__design_1_1universal__pair__range.html#a546a0e896f43a5c67041fddf9bc1614e) ()  
def | [lower_limit_second_rotation](../../d4/d11/classautomotive__design_1_1universal__pair__range.html#a87a1cc92bb3fe996fa341d8826a9b11e) ()  
def | [simple_pair_range_applies_to_pair](../../d4/d11/classautomotive__design_1_1universal__pair__range.html#aea8ae91e5f0388fc5c6d2f41a17d88ed) ()  
def | [upper_limit_first_rotation](../../d4/d11/classautomotive__design_1_1universal__pair__range.html#a0c184149b9a843bc49d1180dd45777f6) ()  
def | [upper_limit_second_rotation](../../d4/d11/classautomotive__design_1_1universal__pair__range.html#a3e1fc6aaa1fb94dfaf7bb4c8c9769d8b) ()  
def | [wr1](../../d4/d11/classautomotive__design_1_1universal__pair__range.html#abee69eecae737f501bc3c9507660fc47) (self)  
def | [wr2](../../d4/d11/classautomotive__design_1_1universal__pair__range.html#af8f68d53aa588dfd0ea1f1851c01ffbf) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.simple_pair_range](../../d3/d35/classautomotive__design_1_1simple__pair__range.html)  
def | [applies_to_pair](../../d3/d35/classautomotive__design_1_1simple__pair__range.html#a34d466ba4abfc972eddb7542a66e3865) ()  
  
##  Public Attributes  
  
---  
|
[lower_limit_first_rotation](../../d4/d11/classautomotive__design_1_1universal__pair__range.html#a05e76afc2c1b91d48ebf17af2619b719)  
|
[lower_limit_second_rotation](../../d4/d11/classautomotive__design_1_1universal__pair__range.html#af578cf4aafa4dad96fef8c55142a6621)  
|
[simple_pair_range_applies_to_pair](../../d4/d11/classautomotive__design_1_1universal__pair__range.html#a820e584562aaa356d8dccd24c812a734)  
|
[upper_limit_first_rotation](../../d4/d11/classautomotive__design_1_1universal__pair__range.html#ae2d6c017270453f9e079f85cb7773173)  
|
[upper_limit_second_rotation](../../d4/d11/classautomotive__design_1_1universal__pair__range.html#ab7d03f0a92ab79ee6d8c0f610af16326)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.simple_pair_range](../../d3/d35/classautomotive__design_1_1simple__pair__range.html)  
|
[applies_to_pair](../../d3/d35/classautomotive__design_1_1simple__pair__range.html#a482e1ee88d0745baefe27406e3b45d03)  
  
## Detailed Description

    
    
    Entity universal_pair_range definition.
    
        :param simple_pair_range_applies_to_pair
        :type simple_pair_range_applies_to_pair:universal_pair
    
        :param lower_limit_first_rotation
        :type lower_limit_first_rotation:rotational_range_measure
    
        :param upper_limit_first_rotation
        :type upper_limit_first_rotation:rotational_range_measure
    
        :param lower_limit_second_rotation
        :type lower_limit_second_rotation:rotational_range_measure
    
        :param upper_limit_second_rotation
        :type upper_limit_second_rotation:rotational_range_measure

## Member Function Documentation

## ◆ lower_limit_first_rotation()

def automotive_design.universal_pair_range.lower_limit_first_rotation  | ( | | ) |   
---|---|---|---|---  
  
References automotive_design.universal_pair_range._lower_limit_first_rotation,
and
[automotive_design.rotational_range_measure](../../d4/ddf/namespaceautomotive__design.html#af1663e07041fb01b2d9c1d995f3ae0dc).

Referenced by
[automotive_design.universal_pair_range.wr1()](../../d4/d11/classautomotive__design_1_1universal__pair__range.html#abee69eecae737f501bc3c9507660fc47).

## ◆ lower_limit_second_rotation()

def automotive_design.universal_pair_range.lower_limit_second_rotation  | ( | | ) |   
---|---|---|---|---  
  
References
automotive_design.universal_pair_range._lower_limit_second_rotation, and
[automotive_design.rotational_range_measure](../../d4/ddf/namespaceautomotive__design.html#af1663e07041fb01b2d9c1d995f3ae0dc).

Referenced by
[automotive_design.universal_pair_range.wr2()](../../d4/d11/classautomotive__design_1_1universal__pair__range.html#af8f68d53aa588dfd0ea1f1851c01ffbf).

## ◆ simple_pair_range_applies_to_pair()

def automotive_design.universal_pair_range.simple_pair_range_applies_to_pair  | ( | | ) |   
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

## ◆ upper_limit_first_rotation()

def automotive_design.universal_pair_range.upper_limit_first_rotation  | ( | | ) |   
---|---|---|---|---  
  
References automotive_design.universal_pair_range._upper_limit_first_rotation,
and
[automotive_design.rotational_range_measure](../../d4/ddf/namespaceautomotive__design.html#af1663e07041fb01b2d9c1d995f3ae0dc).

Referenced by
[automotive_design.universal_pair_range.wr1()](../../d4/d11/classautomotive__design_1_1universal__pair__range.html#abee69eecae737f501bc3c9507660fc47).

## ◆ upper_limit_second_rotation()

def automotive_design.universal_pair_range.upper_limit_second_rotation  | ( | | ) |   
---|---|---|---|---  
  
References
automotive_design.universal_pair_range._upper_limit_second_rotation, and
[automotive_design.rotational_range_measure](../../d4/ddf/namespaceautomotive__design.html#af1663e07041fb01b2d9c1d995f3ae0dc).

Referenced by
[automotive_design.universal_pair_range.wr2()](../../d4/d11/classautomotive__design_1_1universal__pair__range.html#af8f68d53aa588dfd0ea1f1851c01ffbf).

## ◆ wr1()

def automotive_design.universal_pair_range.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[automotive_design.universal_pair_range.lower_limit_first_rotation](../../d4/d11/classautomotive__design_1_1universal__pair__range.html#a05e76afc2c1b91d48ebf17af2619b719),
and
[automotive_design.universal_pair_range.upper_limit_first_rotation](../../d4/d11/classautomotive__design_1_1universal__pair__range.html#ae2d6c017270453f9e079f85cb7773173).

## ◆ wr2()

def automotive_design.universal_pair_range.wr2  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[automotive_design.universal_pair_range.lower_limit_second_rotation](../../d4/d11/classautomotive__design_1_1universal__pair__range.html#af578cf4aafa4dad96fef8c55142a6621),
and
[automotive_design.universal_pair_range.upper_limit_second_rotation](../../d4/d11/classautomotive__design_1_1universal__pair__range.html#ab7d03f0a92ab79ee6d8c0f610af16326).

## Member Data Documentation

## ◆ lower_limit_first_rotation

automotive_design.universal_pair_range.lower_limit_first_rotation  
---  
  
Referenced by
[automotive_design.universal_pair_range.wr1()](../../d4/d11/classautomotive__design_1_1universal__pair__range.html#abee69eecae737f501bc3c9507660fc47).

## ◆ lower_limit_second_rotation

automotive_design.universal_pair_range.lower_limit_second_rotation  
---  
  
Referenced by
[automotive_design.universal_pair_range.wr2()](../../d4/d11/classautomotive__design_1_1universal__pair__range.html#af8f68d53aa588dfd0ea1f1851c01ffbf).

## ◆ simple_pair_range_applies_to_pair

automotive_design.universal_pair_range.simple_pair_range_applies_to_pair  
---  
  
## ◆ upper_limit_first_rotation

automotive_design.universal_pair_range.upper_limit_first_rotation  
---  
  
Referenced by
[automotive_design.universal_pair_range.wr1()](../../d4/d11/classautomotive__design_1_1universal__pair__range.html#abee69eecae737f501bc3c9507660fc47).

## ◆ upper_limit_second_rotation

automotive_design.universal_pair_range.upper_limit_second_rotation  
---  
  
Referenced by
[automotive_design.universal_pair_range.wr2()](../../d4/d11/classautomotive__design_1_1universal__pair__range.html#af8f68d53aa588dfd0ea1f1851c01ffbf).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

