---
url: https://freecad.github.io/SourceDoc/d7/d09/classautomotive__design_1_1cylindrical__pair__value.html
scraped_at: 2025-09-08T15:03:07.530416
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [cylindrical_pair_value](../../d7/d09/classautomotive__design_1_1cylindrical__pair__value.html)

[List of all members](../../dc/d24/classautomotive__design_1_1cylindrical__pair__value-members.html) | Public Member Functions | Public Attributes

automotive_design.cylindrical_pair_value Class Reference

##  Public Member Functions  
  
---  
def | [actual_rotation](../../d7/d09/classautomotive__design_1_1cylindrical__pair__value.html#a3b6cbe800db5738da6a8ce55942c20ca) ()  
def | [actual_translation](../../d7/d09/classautomotive__design_1_1cylindrical__pair__value.html#a2c064f127108b02a76a76bb6de4d5a2e) ()  
def | [pair_value_applies_to_pair](../../d7/d09/classautomotive__design_1_1cylindrical__pair__value.html#a6272e17b7ae9ea1c8ccb8c28810facbf) ()  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.pair_value](../../db/de8/classautomotive__design_1_1pair__value.html)  
def | [applies_to_pair](../../db/de8/classautomotive__design_1_1pair__value.html#ac72d51f14b9a115645f17d03853905b0) ()  
  
##  Public Attributes  
  
---  
|
[actual_rotation](../../d7/d09/classautomotive__design_1_1cylindrical__pair__value.html#a874d32ac5acf68a824db53729be5fcb9)  
|
[actual_translation](../../d7/d09/classautomotive__design_1_1cylindrical__pair__value.html#acc41da1eac616cf10d5ae998b249591e)  
|
[pair_value_applies_to_pair](../../d7/d09/classautomotive__design_1_1cylindrical__pair__value.html#aefe2a32dc5927ed28b722588d7992d1f)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.pair_value](../../db/de8/classautomotive__design_1_1pair__value.html)  
|
[applies_to_pair](../../db/de8/classautomotive__design_1_1pair__value.html#a106ebf8650036d6170ceb14ab03178be)  
  
## Detailed Description

    
    
    Entity cylindrical_pair_value definition.
    
        :param pair_value_applies_to_pair
        :type pair_value_applies_to_pair:cylindrical_pair
    
        :param actual_translation
        :type actual_translation:length_measure
    
        :param actual_rotation
        :type actual_rotation:plane_angle_measure

## Member Function Documentation

## ◆ actual_rotation()

def automotive_design.cylindrical_pair_value.actual_rotation  | ( | | ) |   
---|---|---|---|---  
  
References automotive_design.rolling_surface_pair_value._actual_rotation,
automotive_design.planar_pair_value._actual_rotation,
automotive_design.screw_pair_value._actual_rotation,
automotive_design.cylindrical_pair_value._actual_rotation,
automotive_design.sliding_surface_pair_value._actual_rotation, and
automotive_design.revolute_pair_value._actual_rotation.

Referenced by
[automotive_design.screw_pair_value.actual_translation()](../../de/d90/classautomotive__design_1_1screw__pair__value.html#a8669a1a3468644eae5316a4e8da63891).

## ◆ actual_translation()

def automotive_design.cylindrical_pair_value.actual_translation  | ( | | ) |   
---|---|---|---|---  
  
References automotive_design.prismatic_pair_value._actual_translation, and
automotive_design.cylindrical_pair_value._actual_translation.

## ◆ pair_value_applies_to_pair()

def automotive_design.cylindrical_pair_value.pair_value_applies_to_pair  | ( | | ) |   
---|---|---|---|---  
  
References
automotive_design.point_on_surface_pair_value._pair_value_applies_to_pair,
automotive_design.prismatic_pair_value._pair_value_applies_to_pair,
automotive_design.rolling_surface_pair_value._pair_value_applies_to_pair,
automotive_design.rack_and_pinion_pair_value._pair_value_applies_to_pair,
automotive_design.planar_pair_value._pair_value_applies_to_pair,
automotive_design.screw_pair_value._pair_value_applies_to_pair,
automotive_design.cylindrical_pair_value._pair_value_applies_to_pair,
automotive_design.sliding_surface_pair_value._pair_value_applies_to_pair,
automotive_design.revolute_pair_value._pair_value_applies_to_pair,
automotive_design.spherical_pair_value._pair_value_applies_to_pair,
automotive_design.sliding_curve_pair_value._pair_value_applies_to_pair,
automotive_design.gear_pair_value._pair_value_applies_to_pair,
automotive_design.unconstrained_pair_value._pair_value_applies_to_pair,
automotive_design.rolling_curve_pair_value._pair_value_applies_to_pair,
automotive_design.point_on_planar_curve_pair_value._pair_value_applies_to_pair,
and automotive_design.universal_pair_value._pair_value_applies_to_pair.

## Member Data Documentation

## ◆ actual_rotation

automotive_design.cylindrical_pair_value.actual_rotation  
---  
  
Referenced by
[automotive_design.screw_pair_value.actual_translation()](../../de/d90/classautomotive__design_1_1screw__pair__value.html#a8669a1a3468644eae5316a4e8da63891).

## ◆ actual_translation

automotive_design.cylindrical_pair_value.actual_translation  
---  
  
## ◆ pair_value_applies_to_pair

automotive_design.cylindrical_pair_value.pair_value_applies_to_pair  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

