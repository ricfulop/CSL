---
url: https://freecad.github.io/SourceDoc/de/d90/classautomotive__design_1_1screw__pair__value.html
scraped_at: 2025-09-08T15:12:20.811059
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [screw_pair_value](../../de/d90/classautomotive__design_1_1screw__pair__value.html)

[List of all members](../../db/db3/classautomotive__design_1_1screw__pair__value-members.html) | Public Member Functions | Public Attributes

automotive_design.screw_pair_value Class Reference

##  Public Member Functions  
  
---  
def | [actual_rotation](../../de/d90/classautomotive__design_1_1screw__pair__value.html#ac3eff584338a59ddd7bd69c1d666b11d) ()  
def | [actual_translation](../../de/d90/classautomotive__design_1_1screw__pair__value.html#a8669a1a3468644eae5316a4e8da63891) ()  
def | [pair_value_applies_to_pair](../../de/d90/classautomotive__design_1_1screw__pair__value.html#acedcc561de419f47edd9158621279aa6) ()  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.pair_value](../../db/de8/classautomotive__design_1_1pair__value.html)  
def | [applies_to_pair](../../db/de8/classautomotive__design_1_1pair__value.html#ac72d51f14b9a115645f17d03853905b0) ()  
  
##  Public Attributes  
  
---  
|
[actual_rotation](../../de/d90/classautomotive__design_1_1screw__pair__value.html#acd5d77d398057aa7252901c868198fa2)  
|
[pair_value_applies_to_pair](../../de/d90/classautomotive__design_1_1screw__pair__value.html#a67e5b5d6eb0991cd0035d71ce3de8f19)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.pair_value](../../db/de8/classautomotive__design_1_1pair__value.html)  
|
[applies_to_pair](../../db/de8/classautomotive__design_1_1pair__value.html#a106ebf8650036d6170ceb14ab03178be)  
  
## Detailed Description

    
    
    Entity screw_pair_value definition.
    
        :param pair_value_applies_to_pair
        :type pair_value_applies_to_pair:screw_pair
    
        :param actual_rotation
        :type actual_rotation:plane_angle_measure
    
        :param actual_translation
        :type actual_translation:length_measure

## Member Function Documentation

## ◆ actual_rotation()

def automotive_design.screw_pair_value.actual_rotation  | ( | | ) |   
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

def automotive_design.screw_pair_value.actual_translation  | ( | | ) |   
---|---|---|---|---  
  
References
[automotive_design.rolling_surface_pair_value.actual_rotation](../../df/dc4/classautomotive__design_1_1rolling__surface__pair__value.html#a0464168ca9e3418916299f632d383d7f),
[automotive_design.rack_and_pinion_pair_value.actual_rotation()](../../d5/d14/classautomotive__design_1_1rack__and__pinion__pair__value.html#ab2d1c19d9196115e4cbeddd485fd10eb),
[automotive_design.planar_pair_value.actual_rotation](../../d6/de0/classautomotive__design_1_1planar__pair__value.html#a5dc0f39cc7c6c739e28c66ace1fdb947),
[automotive_design.screw_pair_value.actual_rotation](../../de/d90/classautomotive__design_1_1screw__pair__value.html#acd5d77d398057aa7252901c868198fa2),
[automotive_design.cylindrical_pair_value.actual_rotation](../../d7/d09/classautomotive__design_1_1cylindrical__pair__value.html#a874d32ac5acf68a824db53729be5fcb9),
[automotive_design.sliding_surface_pair_value.actual_rotation](../../d0/d0a/classautomotive__design_1_1sliding__surface__pair__value.html#adaa57bee87d2f908452c500b1f4204fa),
[automotive_design.revolute_pair_value.actual_rotation](../../d4/d40/classautomotive__design_1_1revolute__pair__value.html#a1b69d82c00c31cef3fc11561200a6d15),
[automotive_design.plane_angle_for_pair_in_radian()](../../d4/ddf/namespaceautomotive__design.html#ae43d1d591ca1096682f01120db64f388),
App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

## ◆ pair_value_applies_to_pair()

def automotive_design.screw_pair_value.pair_value_applies_to_pair  | ( | | ) |   
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

automotive_design.screw_pair_value.actual_rotation  
---  
  
Referenced by
[automotive_design.screw_pair_value.actual_translation()](../../de/d90/classautomotive__design_1_1screw__pair__value.html#a8669a1a3468644eae5316a4e8da63891).

## ◆ pair_value_applies_to_pair

automotive_design.screw_pair_value.pair_value_applies_to_pair  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

