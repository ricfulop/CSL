---
url: https://freecad.github.io/SourceDoc/d6/de0/classautomotive__design_1_1planar__pair__value.html
scraped_at: 2025-09-08T15:09:36.117045
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [planar_pair_value](../../d6/de0/classautomotive__design_1_1planar__pair__value.html)

[List of all members](../../d0/ddf/classautomotive__design_1_1planar__pair__value-members.html) | Public Member Functions | Public Attributes

automotive_design.planar_pair_value Class Reference

##  Public Member Functions  
  
---  
def | [actual_rotation](../../d6/de0/classautomotive__design_1_1planar__pair__value.html#adaf514df6ded1e8fd3f4ff254a9b3ea4) ()  
def | [actual_translation_x](../../d6/de0/classautomotive__design_1_1planar__pair__value.html#a5b08312c113e64a14df48333debd38fa) ()  
def | [actual_translation_y](../../d6/de0/classautomotive__design_1_1planar__pair__value.html#aa0e1964748697f4ff8aff49854723a51) ()  
def | [pair_value_applies_to_pair](../../d6/de0/classautomotive__design_1_1planar__pair__value.html#add0412247b7e559018bd6fcbd06a73c0) ()  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.pair_value](../../db/de8/classautomotive__design_1_1pair__value.html)  
def | [applies_to_pair](../../db/de8/classautomotive__design_1_1pair__value.html#ac72d51f14b9a115645f17d03853905b0) ()  
  
##  Public Attributes  
  
---  
|
[actual_rotation](../../d6/de0/classautomotive__design_1_1planar__pair__value.html#a5dc0f39cc7c6c739e28c66ace1fdb947)  
|
[actual_translation_x](../../d6/de0/classautomotive__design_1_1planar__pair__value.html#aa1324dd7a6e63a7901545c9faae2b7f3)  
|
[actual_translation_y](../../d6/de0/classautomotive__design_1_1planar__pair__value.html#a4f52ca9adcbb3efc791b2839bdf3c495)  
|
[pair_value_applies_to_pair](../../d6/de0/classautomotive__design_1_1planar__pair__value.html#aae07e52fd63690ed79ed5e5b86b16bb1)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.pair_value](../../db/de8/classautomotive__design_1_1pair__value.html)  
|
[applies_to_pair](../../db/de8/classautomotive__design_1_1pair__value.html#a106ebf8650036d6170ceb14ab03178be)  
  
## Detailed Description

    
    
    Entity planar_pair_value definition.
    
        :param pair_value_applies_to_pair
        :type pair_value_applies_to_pair:planar_pair
    
        :param actual_rotation
        :type actual_rotation:plane_angle_measure
    
        :param actual_translation_x
        :type actual_translation_x:length_measure
    
        :param actual_translation_y
        :type actual_translation_y:length_measure

## Member Function Documentation

## ◆ actual_rotation()

def automotive_design.planar_pair_value.actual_rotation  | ( | | ) |   
---|---|---|---|---  
  
References automotive_design.rolling_surface_pair_value._actual_rotation,
automotive_design.planar_pair_value._actual_rotation,
automotive_design.screw_pair_value._actual_rotation,
automotive_design.cylindrical_pair_value._actual_rotation,
automotive_design.sliding_surface_pair_value._actual_rotation, and
automotive_design.revolute_pair_value._actual_rotation.

Referenced by
[automotive_design.screw_pair_value.actual_translation()](../../de/d90/classautomotive__design_1_1screw__pair__value.html#a8669a1a3468644eae5316a4e8da63891).

## ◆ actual_translation_x()

def automotive_design.planar_pair_value.actual_translation_x  | ( | | ) |   
---|---|---|---|---  
  
References automotive_design.planar_pair_value._actual_translation_x.

## ◆ actual_translation_y()

def automotive_design.planar_pair_value.actual_translation_y  | ( | | ) |   
---|---|---|---|---  
  
References automotive_design.planar_pair_value._actual_translation_y.

## ◆ pair_value_applies_to_pair()

def automotive_design.planar_pair_value.pair_value_applies_to_pair  | ( | | ) |   
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

automotive_design.planar_pair_value.actual_rotation  
---  
  
Referenced by
[automotive_design.screw_pair_value.actual_translation()](../../de/d90/classautomotive__design_1_1screw__pair__value.html#a8669a1a3468644eae5316a4e8da63891).

## ◆ actual_translation_x

automotive_design.planar_pair_value.actual_translation_x  
---  
  
## ◆ actual_translation_y

automotive_design.planar_pair_value.actual_translation_y  
---  
  
## ◆ pair_value_applies_to_pair

automotive_design.planar_pair_value.pair_value_applies_to_pair  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

