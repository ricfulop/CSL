---
url: https://freecad.github.io/SourceDoc/df/dc4/classautomotive__design_1_1rolling__surface__pair__value.html
scraped_at: 2025-09-08T15:12:09.770304
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [rolling_surface_pair_value](../../df/dc4/classautomotive__design_1_1rolling__surface__pair__value.html)

[List of all members](../../d3/d19/classautomotive__design_1_1rolling__surface__pair__value-members.html) | Public Member Functions | Public Attributes

automotive_design.rolling_surface_pair_value Class Reference

##  Public Member Functions  
  
---  
def | [actual_point_on_surface](../../df/dc4/classautomotive__design_1_1rolling__surface__pair__value.html#a7115526c4e896bec1a1124976d22b67b) ()  
def | [actual_rotation](../../df/dc4/classautomotive__design_1_1rolling__surface__pair__value.html#a377f371c0a0a9529ca28812f21b276f6) ()  
def | [pair_value_applies_to_pair](../../df/dc4/classautomotive__design_1_1rolling__surface__pair__value.html#ac90b852f2e63e440cc82cf163d808eb6) ()  
def | [wr1](../../df/dc4/classautomotive__design_1_1rolling__surface__pair__value.html#a0fae8e17ab9784f13d10b293ea53f9b7) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.pair_value](../../db/de8/classautomotive__design_1_1pair__value.html)  
def | [applies_to_pair](../../db/de8/classautomotive__design_1_1pair__value.html#ac72d51f14b9a115645f17d03853905b0) ()  
  
##  Public Attributes  
  
---  
|
[actual_point_on_surface](../../df/dc4/classautomotive__design_1_1rolling__surface__pair__value.html#a70cbbbff441b1662b962422432abefa8)  
|
[actual_rotation](../../df/dc4/classautomotive__design_1_1rolling__surface__pair__value.html#a0464168ca9e3418916299f632d383d7f)  
|
[pair_value_applies_to_pair](../../df/dc4/classautomotive__design_1_1rolling__surface__pair__value.html#a70067888a64c4e4efe315945fcf32c1a)  
|
[surface_1](../../df/dc4/classautomotive__design_1_1rolling__surface__pair__value.html#abfb4a64b5c7f2fa34f2c2118f81d8a9c)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.pair_value](../../db/de8/classautomotive__design_1_1pair__value.html)  
|
[applies_to_pair](../../db/de8/classautomotive__design_1_1pair__value.html#a106ebf8650036d6170ceb14ab03178be)  
  
## Detailed Description

    
    
    Entity rolling_surface_pair_value definition.
    
        :param pair_value_applies_to_pair
        :type pair_value_applies_to_pair:rolling_surface_pair
    
        :param actual_point_on_surface
        :type actual_point_on_surface:point_on_surface
    
        :param actual_rotation
        :type actual_rotation:plane_angle_measure

## Member Function Documentation

## ◆ actual_point_on_surface()

def automotive_design.rolling_surface_pair_value.actual_point_on_surface  | ( | | ) |   
---|---|---|---|---  
  
References
automotive_design.point_on_surface_pair_value._actual_point_on_surface, and
automotive_design.rolling_surface_pair_value._actual_point_on_surface.

## ◆ actual_rotation()

def automotive_design.rolling_surface_pair_value.actual_rotation  | ( | | ) |   
---|---|---|---|---  
  
References automotive_design.rolling_surface_pair_value._actual_rotation,
automotive_design.planar_pair_value._actual_rotation,
automotive_design.screw_pair_value._actual_rotation,
automotive_design.cylindrical_pair_value._actual_rotation,
automotive_design.sliding_surface_pair_value._actual_rotation, and
automotive_design.revolute_pair_value._actual_rotation.

Referenced by
[automotive_design.screw_pair_value.actual_translation()](../../de/d90/classautomotive__design_1_1screw__pair__value.html#a8669a1a3468644eae5316a4e8da63891).

## ◆ pair_value_applies_to_pair()

def automotive_design.rolling_surface_pair_value.pair_value_applies_to_pair  | ( | | ) |   
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

## ◆ wr1()

def automotive_design.rolling_surface_pair_value.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
## Member Data Documentation

## ◆ actual_point_on_surface

automotive_design.rolling_surface_pair_value.actual_point_on_surface  
---  
  
## ◆ actual_rotation

automotive_design.rolling_surface_pair_value.actual_rotation  
---  
  
Referenced by
[automotive_design.screw_pair_value.actual_translation()](../../de/d90/classautomotive__design_1_1screw__pair__value.html#a8669a1a3468644eae5316a4e8da63891).

## ◆ pair_value_applies_to_pair

automotive_design.rolling_surface_pair_value.pair_value_applies_to_pair  
---  
  
## ◆ surface_1

automotive_design.rolling_surface_pair_value.surface_1  
---  
  
Referenced by
[automotive_design.surface_pair.wr1()](../../d3/d78/classautomotive__design_1_1surface__pair.html#a4e29aa1ef1ee68a84f0448f2535103e1).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

