---
url: https://freecad.github.io/SourceDoc/d5/d14/classautomotive__design_1_1rack__and__pinion__pair__value.html
scraped_at: 2025-09-08T15:11:25.569922
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [rack_and_pinion_pair_value](../../d5/d14/classautomotive__design_1_1rack__and__pinion__pair__value.html)

[List of all members](../../d7/dd2/classautomotive__design_1_1rack__and__pinion__pair__value-members.html) | Public Member Functions | Public Attributes

automotive_design.rack_and_pinion_pair_value Class Reference

##  Public Member Functions  
  
---  
def | [actual_displacement](../../d5/d14/classautomotive__design_1_1rack__and__pinion__pair__value.html#a3726da7f960d77da4c65ff701ad39e4d) ()  
def | [actual_rotation](../../d5/d14/classautomotive__design_1_1rack__and__pinion__pair__value.html#ab2d1c19d9196115e4cbeddd485fd10eb) ()  
def | [pair_value_applies_to_pair](../../d5/d14/classautomotive__design_1_1rack__and__pinion__pair__value.html#a01b3969f94ee767c8b3ddb1ecbfdc205) ()  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.pair_value](../../db/de8/classautomotive__design_1_1pair__value.html)  
def | [applies_to_pair](../../db/de8/classautomotive__design_1_1pair__value.html#ac72d51f14b9a115645f17d03853905b0) ()  
  
##  Public Attributes  
  
---  
|
[actual_displacement](../../d5/d14/classautomotive__design_1_1rack__and__pinion__pair__value.html#ab0c5ca4ff38b4e39763e3fb7f008a2ab)  
|
[pair_value_applies_to_pair](../../d5/d14/classautomotive__design_1_1rack__and__pinion__pair__value.html#a37033c03f74b6fa534e439e33e430dd8)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.pair_value](../../db/de8/classautomotive__design_1_1pair__value.html)  
|
[applies_to_pair](../../db/de8/classautomotive__design_1_1pair__value.html#a106ebf8650036d6170ceb14ab03178be)  
  
## Detailed Description

    
    
    Entity rack_and_pinion_pair_value definition.
    
        :param pair_value_applies_to_pair
        :type pair_value_applies_to_pair:rack_and_pinion_pair
    
        :param actual_displacement
        :type actual_displacement:length_measure
    
        :param actual_rotation
        :type actual_rotation:plane_angle_measure

## Member Function Documentation

## ◆ actual_displacement()

def automotive_design.rack_and_pinion_pair_value.actual_displacement  | ( | | ) |   
---|---|---|---|---  
  
References automotive_design.rack_and_pinion_pair_value._actual_displacement.

Referenced by
[automotive_design.rack_and_pinion_pair_value.actual_rotation()](../../d5/d14/classautomotive__design_1_1rack__and__pinion__pair__value.html#ab2d1c19d9196115e4cbeddd485fd10eb).

## ◆ actual_rotation()

def automotive_design.rack_and_pinion_pair_value.actual_rotation  | ( | | ) |   
---|---|---|---|---  
  
References
[automotive_design.rack_and_pinion_pair_value.actual_displacement](../../d5/d14/classautomotive__design_1_1rack__and__pinion__pair__value.html#ab0c5ca4ff38b4e39763e3fb7f008a2ab),
[automotive_design.convert_plane_angle_for_pair_from_radian()](../../d4/ddf/namespaceautomotive__design.html#ad3aa88c015a8618774d701c4ca5a797a),
App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

Referenced by
[automotive_design.screw_pair_value.actual_translation()](../../de/d90/classautomotive__design_1_1screw__pair__value.html#a8669a1a3468644eae5316a4e8da63891).

## ◆ pair_value_applies_to_pair()

def automotive_design.rack_and_pinion_pair_value.pair_value_applies_to_pair  | ( | | ) |   
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

## ◆ actual_displacement

automotive_design.rack_and_pinion_pair_value.actual_displacement  
---  
  
Referenced by
[automotive_design.rack_and_pinion_pair_value.actual_rotation()](../../d5/d14/classautomotive__design_1_1rack__and__pinion__pair__value.html#ab2d1c19d9196115e4cbeddd485fd10eb).

## ◆ pair_value_applies_to_pair

automotive_design.rack_and_pinion_pair_value.pair_value_applies_to_pair  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

