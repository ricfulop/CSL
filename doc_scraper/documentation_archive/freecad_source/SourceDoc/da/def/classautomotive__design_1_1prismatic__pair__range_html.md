---
url: https://freecad.github.io/SourceDoc/da/def/classautomotive__design_1_1prismatic__pair__range.html
scraped_at: 2025-09-08T15:10:31.360048
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [prismatic_pair_range](../../da/def/classautomotive__design_1_1prismatic__pair__range.html)

[List of all members](../../dc/dd8/classautomotive__design_1_1prismatic__pair__range-members.html) | Public Member Functions | Public Attributes

automotive_design.prismatic_pair_range Class Reference

##  Public Member Functions  
  
---  
def | [lower_limit_actual_translation](../../da/def/classautomotive__design_1_1prismatic__pair__range.html#aa05a3399bddaa72506620663593d3887) ()  
def | [simple_pair_range_applies_to_pair](../../da/def/classautomotive__design_1_1prismatic__pair__range.html#a71e0ad769879b989e68013bad8965546) ()  
def | [upper_limit_actual_translation](../../da/def/classautomotive__design_1_1prismatic__pair__range.html#a53eb0c0115855612c8245d7c44b77d75) ()  
def | [wr1](../../da/def/classautomotive__design_1_1prismatic__pair__range.html#ad3aecd0a050f3fbbe16ef2ae17c6cc12) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.simple_pair_range](../../d3/d35/classautomotive__design_1_1simple__pair__range.html)  
def | [applies_to_pair](../../d3/d35/classautomotive__design_1_1simple__pair__range.html#a34d466ba4abfc972eddb7542a66e3865) ()  
  
##  Public Attributes  
  
---  
|
[lower_limit_actual_translation](../../da/def/classautomotive__design_1_1prismatic__pair__range.html#aa777265830fda283668e469b5366bdcb)  
|
[simple_pair_range_applies_to_pair](../../da/def/classautomotive__design_1_1prismatic__pair__range.html#a98de87e8c2727300a39f74d625cc2098)  
|
[upper_limit_actual_translation](../../da/def/classautomotive__design_1_1prismatic__pair__range.html#a583c1e4baa6ec46d4f43b2483bc5e53a)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.simple_pair_range](../../d3/d35/classautomotive__design_1_1simple__pair__range.html)  
|
[applies_to_pair](../../d3/d35/classautomotive__design_1_1simple__pair__range.html#a482e1ee88d0745baefe27406e3b45d03)  
  
## Detailed Description

    
    
    Entity prismatic_pair_range definition.
    
        :param simple_pair_range_applies_to_pair
        :type simple_pair_range_applies_to_pair:prismatic_pair
    
        :param lower_limit_actual_translation
        :type lower_limit_actual_translation:translational_range_measure
    
        :param upper_limit_actual_translation
        :type upper_limit_actual_translation:translational_range_measure

## Member Function Documentation

## ◆ lower_limit_actual_translation()

def automotive_design.prismatic_pair_range.lower_limit_actual_translation  | ( | | ) |   
---|---|---|---|---  
  
References
automotive_design.cylindrical_pair_range._lower_limit_actual_translation,
automotive_design.prismatic_pair_range._lower_limit_actual_translation, and
[automotive_design.translational_range_measure](../../d4/ddf/namespaceautomotive__design.html#a8c20f8bd88dcd73e869e38b254a3f173).

Referenced by
[automotive_design.cylindrical_pair_range.wr1()](../../dc/d91/classautomotive__design_1_1cylindrical__pair__range.html#a9a68830e9ff227a60274416f40fc1c20),
and
[automotive_design.prismatic_pair_range.wr1()](../../da/def/classautomotive__design_1_1prismatic__pair__range.html#ad3aecd0a050f3fbbe16ef2ae17c6cc12).

## ◆ simple_pair_range_applies_to_pair()

def automotive_design.prismatic_pair_range.simple_pair_range_applies_to_pair  | ( | | ) |   
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

## ◆ upper_limit_actual_translation()

def automotive_design.prismatic_pair_range.upper_limit_actual_translation  | ( | | ) |   
---|---|---|---|---  
  
References
automotive_design.cylindrical_pair_range._upper_limit_actual_translation,
automotive_design.prismatic_pair_range._upper_limit_actual_translation, and
[automotive_design.translational_range_measure](../../d4/ddf/namespaceautomotive__design.html#a8c20f8bd88dcd73e869e38b254a3f173).

Referenced by
[automotive_design.cylindrical_pair_range.wr1()](../../dc/d91/classautomotive__design_1_1cylindrical__pair__range.html#a9a68830e9ff227a60274416f40fc1c20),
and
[automotive_design.prismatic_pair_range.wr1()](../../da/def/classautomotive__design_1_1prismatic__pair__range.html#ad3aecd0a050f3fbbe16ef2ae17c6cc12).

## ◆ wr1()

def automotive_design.prismatic_pair_range.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[automotive_design.cylindrical_pair_range.lower_limit_actual_translation](../../dc/d91/classautomotive__design_1_1cylindrical__pair__range.html#aa72f2d3a5a3a29ae2a85c8868e55fde9),
[automotive_design.prismatic_pair_range.lower_limit_actual_translation](../../da/def/classautomotive__design_1_1prismatic__pair__range.html#aa777265830fda283668e469b5366bdcb),
[automotive_design.cylindrical_pair_range.upper_limit_actual_translation](../../dc/d91/classautomotive__design_1_1cylindrical__pair__range.html#a24bbcb8ee5f569b222b406c620b459ad),
and
[automotive_design.prismatic_pair_range.upper_limit_actual_translation](../../da/def/classautomotive__design_1_1prismatic__pair__range.html#a583c1e4baa6ec46d4f43b2483bc5e53a).

## Member Data Documentation

## ◆ lower_limit_actual_translation

automotive_design.prismatic_pair_range.lower_limit_actual_translation  
---  
  
Referenced by
[automotive_design.cylindrical_pair_range.wr1()](../../dc/d91/classautomotive__design_1_1cylindrical__pair__range.html#a9a68830e9ff227a60274416f40fc1c20),
and
[automotive_design.prismatic_pair_range.wr1()](../../da/def/classautomotive__design_1_1prismatic__pair__range.html#ad3aecd0a050f3fbbe16ef2ae17c6cc12).

## ◆ simple_pair_range_applies_to_pair

automotive_design.prismatic_pair_range.simple_pair_range_applies_to_pair  
---  
  
## ◆ upper_limit_actual_translation

automotive_design.prismatic_pair_range.upper_limit_actual_translation  
---  
  
Referenced by
[automotive_design.cylindrical_pair_range.wr1()](../../dc/d91/classautomotive__design_1_1cylindrical__pair__range.html#a9a68830e9ff227a60274416f40fc1c20),
and
[automotive_design.prismatic_pair_range.wr1()](../../da/def/classautomotive__design_1_1prismatic__pair__range.html#ad3aecd0a050f3fbbe16ef2ae17c6cc12).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

