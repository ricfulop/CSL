---
url: https://freecad.github.io/SourceDoc/dc/d91/classautomotive__design_1_1cylindrical__pair__range.html
scraped_at: 2025-09-08T15:03:06.537532
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [cylindrical_pair_range](../../dc/d91/classautomotive__design_1_1cylindrical__pair__range.html)

[List of all members](../../d3/d6f/classautomotive__design_1_1cylindrical__pair__range-members.html) | Public Member Functions | Public Attributes

automotive_design.cylindrical_pair_range Class Reference

##  Public Member Functions  
  
---  
def | [lower_limit_actual_rotation](../../dc/d91/classautomotive__design_1_1cylindrical__pair__range.html#a0f96bb0ec9a8729b7f9ac46a57e34992) ()  
def | [lower_limit_actual_translation](../../dc/d91/classautomotive__design_1_1cylindrical__pair__range.html#af3e20fc63219fe8e1366b822d8821d54) ()  
def | [simple_pair_range_applies_to_pair](../../dc/d91/classautomotive__design_1_1cylindrical__pair__range.html#a0426855e41c3606109e8364c7e34a740) ()  
def | [upper_limit_actual_rotation](../../dc/d91/classautomotive__design_1_1cylindrical__pair__range.html#ab678e13e8834ba242971e99b9a972359) ()  
def | [upper_limit_actual_translation](../../dc/d91/classautomotive__design_1_1cylindrical__pair__range.html#a56484167f9bddd010d9ea4094d79693b) ()  
def | [wr1](../../dc/d91/classautomotive__design_1_1cylindrical__pair__range.html#a9a68830e9ff227a60274416f40fc1c20) (self)  
def | [wr2](../../dc/d91/classautomotive__design_1_1cylindrical__pair__range.html#a1fe3024941fa140a1c58b2750a0f1dcd) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.simple_pair_range](../../d3/d35/classautomotive__design_1_1simple__pair__range.html)  
def | [applies_to_pair](../../d3/d35/classautomotive__design_1_1simple__pair__range.html#a34d466ba4abfc972eddb7542a66e3865) ()  
  
##  Public Attributes  
  
---  
|
[lower_limit_actual_rotation](../../dc/d91/classautomotive__design_1_1cylindrical__pair__range.html#a53fd0c0e0a31071bf0c74186f1cc71fe)  
|
[lower_limit_actual_translation](../../dc/d91/classautomotive__design_1_1cylindrical__pair__range.html#aa72f2d3a5a3a29ae2a85c8868e55fde9)  
|
[simple_pair_range_applies_to_pair](../../dc/d91/classautomotive__design_1_1cylindrical__pair__range.html#a1017f11050a5bf0bc64c296fa6a426fa)  
|
[upper_limit_actual_rotation](../../dc/d91/classautomotive__design_1_1cylindrical__pair__range.html#a952e189891bb61b5824e527b5e37289f)  
|
[upper_limit_actual_translation](../../dc/d91/classautomotive__design_1_1cylindrical__pair__range.html#a24bbcb8ee5f569b222b406c620b459ad)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.simple_pair_range](../../d3/d35/classautomotive__design_1_1simple__pair__range.html)  
|
[applies_to_pair](../../d3/d35/classautomotive__design_1_1simple__pair__range.html#a482e1ee88d0745baefe27406e3b45d03)  
  
## Detailed Description

    
    
    Entity cylindrical_pair_range definition.
    
        :param simple_pair_range_applies_to_pair
        :type simple_pair_range_applies_to_pair:cylindrical_pair
    
        :param lower_limit_actual_translation
        :type lower_limit_actual_translation:translational_range_measure
    
        :param upper_limit_actual_translation
        :type upper_limit_actual_translation:translational_range_measure
    
        :param lower_limit_actual_rotation
        :type lower_limit_actual_rotation:rotational_range_measure
    
        :param upper_limit_actual_rotation
        :type upper_limit_actual_rotation:rotational_range_measure

## Member Function Documentation

## ◆ lower_limit_actual_rotation()

def automotive_design.cylindrical_pair_range.lower_limit_actual_rotation  | ( | | ) |   
---|---|---|---|---  
  
References automotive_design.planar_pair_range._lower_limit_actual_rotation,
automotive_design.cylindrical_pair_range._lower_limit_actual_rotation,
automotive_design.screw_pair_range._lower_limit_actual_rotation,
automotive_design.surface_pair_range._lower_limit_actual_rotation,
automotive_design.revolute_pair_range._lower_limit_actual_rotation, and
[automotive_design.rotational_range_measure](../../d4/ddf/namespaceautomotive__design.html#af1663e07041fb01b2d9c1d995f3ae0dc).

Referenced by
[automotive_design.planar_pair_range.wr1()](../../d3/d63/classautomotive__design_1_1planar__pair__range.html#adcd88f48425fab30949f3b9529eb3b04),
[automotive_design.screw_pair_range.wr1()](../../de/d80/classautomotive__design_1_1screw__pair__range.html#ad2fe9f4702583a8a058b1551d1b8e809),
[automotive_design.revolute_pair_range.wr1()](../../d5/d6a/classautomotive__design_1_1revolute__pair__range.html#a1755019153af246320f72625d1a3ab1a),
[automotive_design.cylindrical_pair_range.wr2()](../../dc/d91/classautomotive__design_1_1cylindrical__pair__range.html#a1fe3024941fa140a1c58b2750a0f1dcd),
and
[automotive_design.surface_pair_range.wr3()](../../d2/d05/classautomotive__design_1_1surface__pair__range.html#ab8a260e1da765fa896e1341d5625b849).

## ◆ lower_limit_actual_translation()

def automotive_design.cylindrical_pair_range.lower_limit_actual_translation  | ( | | ) |   
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

def automotive_design.cylindrical_pair_range.simple_pair_range_applies_to_pair  | ( | | ) |   
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

## ◆ upper_limit_actual_rotation()

def automotive_design.cylindrical_pair_range.upper_limit_actual_rotation  | ( | | ) |   
---|---|---|---|---  
  
References automotive_design.planar_pair_range._upper_limit_actual_rotation,
automotive_design.cylindrical_pair_range._upper_limit_actual_rotation,
automotive_design.screw_pair_range._upper_limit_actual_rotation,
automotive_design.surface_pair_range._upper_limit_actual_rotation,
automotive_design.revolute_pair_range._upper_limit_actual_rotation, and
[automotive_design.rotational_range_measure](../../d4/ddf/namespaceautomotive__design.html#af1663e07041fb01b2d9c1d995f3ae0dc).

Referenced by
[automotive_design.planar_pair_range.wr1()](../../d3/d63/classautomotive__design_1_1planar__pair__range.html#adcd88f48425fab30949f3b9529eb3b04),
[automotive_design.screw_pair_range.wr1()](../../de/d80/classautomotive__design_1_1screw__pair__range.html#ad2fe9f4702583a8a058b1551d1b8e809),
[automotive_design.revolute_pair_range.wr1()](../../d5/d6a/classautomotive__design_1_1revolute__pair__range.html#a1755019153af246320f72625d1a3ab1a),
[automotive_design.cylindrical_pair_range.wr2()](../../dc/d91/classautomotive__design_1_1cylindrical__pair__range.html#a1fe3024941fa140a1c58b2750a0f1dcd),
and
[automotive_design.surface_pair_range.wr3()](../../d2/d05/classautomotive__design_1_1surface__pair__range.html#ab8a260e1da765fa896e1341d5625b849).

## ◆ upper_limit_actual_translation()

def automotive_design.cylindrical_pair_range.upper_limit_actual_translation  | ( | | ) |   
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

def automotive_design.cylindrical_pair_range.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[automotive_design.cylindrical_pair_range.lower_limit_actual_translation](../../dc/d91/classautomotive__design_1_1cylindrical__pair__range.html#aa72f2d3a5a3a29ae2a85c8868e55fde9),
[automotive_design.prismatic_pair_range.lower_limit_actual_translation](../../da/def/classautomotive__design_1_1prismatic__pair__range.html#aa777265830fda283668e469b5366bdcb),
[automotive_design.cylindrical_pair_range.upper_limit_actual_translation](../../dc/d91/classautomotive__design_1_1cylindrical__pair__range.html#a24bbcb8ee5f569b222b406c620b459ad),
and
[automotive_design.prismatic_pair_range.upper_limit_actual_translation](../../da/def/classautomotive__design_1_1prismatic__pair__range.html#a583c1e4baa6ec46d4f43b2483bc5e53a).

## ◆ wr2()

def automotive_design.cylindrical_pair_range.wr2  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[automotive_design.planar_pair_range.lower_limit_actual_rotation](../../d3/d63/classautomotive__design_1_1planar__pair__range.html#aa94241d907a80c44cda4cf20560c2c25),
[automotive_design.cylindrical_pair_range.lower_limit_actual_rotation](../../dc/d91/classautomotive__design_1_1cylindrical__pair__range.html#a53fd0c0e0a31071bf0c74186f1cc71fe),
[automotive_design.screw_pair_range.lower_limit_actual_rotation](../../de/d80/classautomotive__design_1_1screw__pair__range.html#a0a70e633c8457d29f4ed92ed0f9de748),
[automotive_design.surface_pair_range.lower_limit_actual_rotation](../../d2/d05/classautomotive__design_1_1surface__pair__range.html#a02ac8840f95c70c90b4680bb4fa92d94),
[automotive_design.revolute_pair_range.lower_limit_actual_rotation](../../d5/d6a/classautomotive__design_1_1revolute__pair__range.html#afbf29d85aeacc28ea9e3c65f23c9bec9),
[automotive_design.planar_pair_range.upper_limit_actual_rotation](../../d3/d63/classautomotive__design_1_1planar__pair__range.html#ad09fa125d01307d879a193b32e268d3c),
[automotive_design.cylindrical_pair_range.upper_limit_actual_rotation](../../dc/d91/classautomotive__design_1_1cylindrical__pair__range.html#a952e189891bb61b5824e527b5e37289f),
[automotive_design.screw_pair_range.upper_limit_actual_rotation](../../de/d80/classautomotive__design_1_1screw__pair__range.html#a9b3432c3ed50a3f6ba8c178d4fe01c3e),
[automotive_design.surface_pair_range.upper_limit_actual_rotation](../../d2/d05/classautomotive__design_1_1surface__pair__range.html#aa63ca05bffb19167ab66561b17ee7123),
and
[automotive_design.revolute_pair_range.upper_limit_actual_rotation](../../d5/d6a/classautomotive__design_1_1revolute__pair__range.html#acbcd4d05df1ac629d9d0fe7a5a9baa5f).

## Member Data Documentation

## ◆ lower_limit_actual_rotation

automotive_design.cylindrical_pair_range.lower_limit_actual_rotation  
---  
  
Referenced by
[automotive_design.planar_pair_range.wr1()](../../d3/d63/classautomotive__design_1_1planar__pair__range.html#adcd88f48425fab30949f3b9529eb3b04),
[automotive_design.screw_pair_range.wr1()](../../de/d80/classautomotive__design_1_1screw__pair__range.html#ad2fe9f4702583a8a058b1551d1b8e809),
[automotive_design.revolute_pair_range.wr1()](../../d5/d6a/classautomotive__design_1_1revolute__pair__range.html#a1755019153af246320f72625d1a3ab1a),
[automotive_design.cylindrical_pair_range.wr2()](../../dc/d91/classautomotive__design_1_1cylindrical__pair__range.html#a1fe3024941fa140a1c58b2750a0f1dcd),
and
[automotive_design.surface_pair_range.wr3()](../../d2/d05/classautomotive__design_1_1surface__pair__range.html#ab8a260e1da765fa896e1341d5625b849).

## ◆ lower_limit_actual_translation

automotive_design.cylindrical_pair_range.lower_limit_actual_translation  
---  
  
Referenced by
[automotive_design.cylindrical_pair_range.wr1()](../../dc/d91/classautomotive__design_1_1cylindrical__pair__range.html#a9a68830e9ff227a60274416f40fc1c20),
and
[automotive_design.prismatic_pair_range.wr1()](../../da/def/classautomotive__design_1_1prismatic__pair__range.html#ad3aecd0a050f3fbbe16ef2ae17c6cc12).

## ◆ simple_pair_range_applies_to_pair

automotive_design.cylindrical_pair_range.simple_pair_range_applies_to_pair  
---  
  
## ◆ upper_limit_actual_rotation

automotive_design.cylindrical_pair_range.upper_limit_actual_rotation  
---  
  
Referenced by
[automotive_design.planar_pair_range.wr1()](../../d3/d63/classautomotive__design_1_1planar__pair__range.html#adcd88f48425fab30949f3b9529eb3b04),
[automotive_design.screw_pair_range.wr1()](../../de/d80/classautomotive__design_1_1screw__pair__range.html#ad2fe9f4702583a8a058b1551d1b8e809),
[automotive_design.revolute_pair_range.wr1()](../../d5/d6a/classautomotive__design_1_1revolute__pair__range.html#a1755019153af246320f72625d1a3ab1a),
[automotive_design.cylindrical_pair_range.wr2()](../../dc/d91/classautomotive__design_1_1cylindrical__pair__range.html#a1fe3024941fa140a1c58b2750a0f1dcd),
and
[automotive_design.surface_pair_range.wr3()](../../d2/d05/classautomotive__design_1_1surface__pair__range.html#ab8a260e1da765fa896e1341d5625b849).

## ◆ upper_limit_actual_translation

automotive_design.cylindrical_pair_range.upper_limit_actual_translation  
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

