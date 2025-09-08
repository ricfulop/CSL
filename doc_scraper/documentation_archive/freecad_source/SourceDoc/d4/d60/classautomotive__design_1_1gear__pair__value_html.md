---
url: https://freecad.github.io/SourceDoc/d4/d60/classautomotive__design_1_1gear__pair__value.html
scraped_at: 2025-09-08T15:05:52.186029
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [gear_pair_value](../../d4/d60/classautomotive__design_1_1gear__pair__value.html)

[List of all members](../../d7/dd2/classautomotive__design_1_1gear__pair__value-members.html) | Public Member Functions | Public Attributes

automotive_design.gear_pair_value Class Reference

##  Public Member Functions  
  
---  
def | [actual_rotation_1](../../d4/d60/classautomotive__design_1_1gear__pair__value.html#afa6fcff1339fa334098d68b00b91d49c) ()  
def | [actual_rotation_2](../../d4/d60/classautomotive__design_1_1gear__pair__value.html#a6356cedeec4231374b1e6ea9761183b6) ()  
def | [pair_value_applies_to_pair](../../d4/d60/classautomotive__design_1_1gear__pair__value.html#af65441c45226371759d9caea821e84d8) ()  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.pair_value](../../db/de8/classautomotive__design_1_1pair__value.html)  
def | [applies_to_pair](../../db/de8/classautomotive__design_1_1pair__value.html#ac72d51f14b9a115645f17d03853905b0) ()  
  
##  Public Attributes  
  
---  
|
[actual_rotation_1](../../d4/d60/classautomotive__design_1_1gear__pair__value.html#a76f406e5fa715b0239b42babf6b09501)  
|
[pair_value_applies_to_pair](../../d4/d60/classautomotive__design_1_1gear__pair__value.html#aeb274380e2209bc761d774efda269b44)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.pair_value](../../db/de8/classautomotive__design_1_1pair__value.html)  
|
[applies_to_pair](../../db/de8/classautomotive__design_1_1pair__value.html#a106ebf8650036d6170ceb14ab03178be)  
  
## Detailed Description

    
    
    Entity gear_pair_value definition.
    
        :param pair_value_applies_to_pair
        :type pair_value_applies_to_pair:gear_pair
    
        :param actual_rotation_1
        :type actual_rotation_1:plane_angle_measure
    
        :param actual_rotation_2
        :type actual_rotation_2:plane_angle_measure

## Member Function Documentation

## ◆ actual_rotation_1()

def automotive_design.gear_pair_value.actual_rotation_1  | ( | | ) |   
---|---|---|---|---  
  
References automotive_design.gear_pair_value._actual_rotation_1.

Referenced by
[automotive_design.gear_pair_value.actual_rotation_2()](../../d4/d60/classautomotive__design_1_1gear__pair__value.html#a6356cedeec4231374b1e6ea9761183b6).

## ◆ actual_rotation_2()

def automotive_design.gear_pair_value.actual_rotation_2  | ( | | ) |   
---|---|---|---|---  
  
References
[automotive_design.gear_pair_value.actual_rotation_1](../../d4/d60/classautomotive__design_1_1gear__pair__value.html#a76f406e5fa715b0239b42babf6b09501),
App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

## ◆ pair_value_applies_to_pair()

def automotive_design.gear_pair_value.pair_value_applies_to_pair  | ( | | ) |   
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

## ◆ actual_rotation_1

automotive_design.gear_pair_value.actual_rotation_1  
---  
  
Referenced by
[automotive_design.gear_pair_value.actual_rotation_2()](../../d4/d60/classautomotive__design_1_1gear__pair__value.html#a6356cedeec4231374b1e6ea9761183b6).

## ◆ pair_value_applies_to_pair

automotive_design.gear_pair_value.pair_value_applies_to_pair  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

