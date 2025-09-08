---
url: https://freecad.github.io/SourceDoc/d0/d0a/classautomotive__design_1_1sliding__surface__pair__value.html
scraped_at: 2025-09-08T15:12:55.961183
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [sliding_surface_pair_value](../../d0/d0a/classautomotive__design_1_1sliding__surface__pair__value.html)

[List of all members](../../d5/d6c/classautomotive__design_1_1sliding__surface__pair__value-members.html) | Public Member Functions | Public Attributes

automotive_design.sliding_surface_pair_value Class Reference

##  Public Member Functions  
  
---  
def | [actual_point_on_surface_1](../../d0/d0a/classautomotive__design_1_1sliding__surface__pair__value.html#a0cfa43d532cb335ac8fc627462a5534a) ()  
def | [actual_point_on_surface_2](../../d0/d0a/classautomotive__design_1_1sliding__surface__pair__value.html#abe5d090a9b901e7130f370ce3dde915a) ()  
def | [actual_rotation](../../d0/d0a/classautomotive__design_1_1sliding__surface__pair__value.html#a99ef0c47956f88346521af711f5d8f81) ()  
def | [pair_value_applies_to_pair](../../d0/d0a/classautomotive__design_1_1sliding__surface__pair__value.html#a60090794485bfa9f21d815038848b721) ()  
def | [wr1](../../d0/d0a/classautomotive__design_1_1sliding__surface__pair__value.html#a6db0e794c25df693f4b2a904a45dccfa) (self)  
def | [wr2](../../d0/d0a/classautomotive__design_1_1sliding__surface__pair__value.html#a85dc5d776df4073b7db2b172f30d5afb) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.pair_value](../../db/de8/classautomotive__design_1_1pair__value.html)  
def | [applies_to_pair](../../db/de8/classautomotive__design_1_1pair__value.html#ac72d51f14b9a115645f17d03853905b0) ()  
  
##  Public Attributes  
  
---  
|
[actual_point_on_surface_1](../../d0/d0a/classautomotive__design_1_1sliding__surface__pair__value.html#a2c3fb069d1cd620fdc9f29428a00322f)  
|
[actual_point_on_surface_2](../../d0/d0a/classautomotive__design_1_1sliding__surface__pair__value.html#a9e2cb0826f374afbffcfd45abf02d4ca)  
|
[actual_rotation](../../d0/d0a/classautomotive__design_1_1sliding__surface__pair__value.html#adaa57bee87d2f908452c500b1f4204fa)  
|
[pair_value_applies_to_pair](../../d0/d0a/classautomotive__design_1_1sliding__surface__pair__value.html#adf15f6d9932019df2a945dfe93c7501a)  
|
[surface_1](../../d0/d0a/classautomotive__design_1_1sliding__surface__pair__value.html#adc83a9ddcba0766605d9d795791d3afd)  
|
[surface_2](../../d0/d0a/classautomotive__design_1_1sliding__surface__pair__value.html#a84074875831f92befc31e35634a64011)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.pair_value](../../db/de8/classautomotive__design_1_1pair__value.html)  
|
[applies_to_pair](../../db/de8/classautomotive__design_1_1pair__value.html#a106ebf8650036d6170ceb14ab03178be)  
  
## Detailed Description

    
    
    Entity sliding_surface_pair_value definition.
    
        :param pair_value_applies_to_pair
        :type pair_value_applies_to_pair:sliding_surface_pair
    
        :param actual_point_on_surface_1
        :type actual_point_on_surface_1:point_on_surface
    
        :param actual_point_on_surface_2
        :type actual_point_on_surface_2:point_on_surface
    
        :param actual_rotation
        :type actual_rotation:plane_angle_measure

## Member Function Documentation

## ◆ actual_point_on_surface_1()

def automotive_design.sliding_surface_pair_value.actual_point_on_surface_1  | ( | | ) |   
---|---|---|---|---  
  
References
automotive_design.sliding_surface_pair_value._actual_point_on_surface_1.

## ◆ actual_point_on_surface_2()

def automotive_design.sliding_surface_pair_value.actual_point_on_surface_2  | ( | | ) |   
---|---|---|---|---  
  
References
automotive_design.sliding_surface_pair_value._actual_point_on_surface_2.

## ◆ actual_rotation()

def automotive_design.sliding_surface_pair_value.actual_rotation  | ( | | ) |   
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

def automotive_design.sliding_surface_pair_value.pair_value_applies_to_pair  | ( | | ) |   
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

def automotive_design.sliding_surface_pair_value.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
## ◆ wr2()

def automotive_design.sliding_surface_pair_value.wr2  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
## Member Data Documentation

## ◆ actual_point_on_surface_1

automotive_design.sliding_surface_pair_value.actual_point_on_surface_1  
---  
  
## ◆ actual_point_on_surface_2

automotive_design.sliding_surface_pair_value.actual_point_on_surface_2  
---  
  
## ◆ actual_rotation

automotive_design.sliding_surface_pair_value.actual_rotation  
---  
  
Referenced by
[automotive_design.screw_pair_value.actual_translation()](../../de/d90/classautomotive__design_1_1screw__pair__value.html#a8669a1a3468644eae5316a4e8da63891).

## ◆ pair_value_applies_to_pair

automotive_design.sliding_surface_pair_value.pair_value_applies_to_pair  
---  
  
## ◆ surface_1

automotive_design.sliding_surface_pair_value.surface_1  
---  
  
Referenced by
[automotive_design.surface_pair.wr1()](../../d3/d78/classautomotive__design_1_1surface__pair.html#a4e29aa1ef1ee68a84f0448f2535103e1).

## ◆ surface_2

automotive_design.sliding_surface_pair_value.surface_2  
---  
  
Referenced by
[automotive_design.surface_pair.wr2()](../../d3/d78/classautomotive__design_1_1surface__pair.html#ac70a19c48959c1ce8a4b2423f45373fc).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

