---
url: https://freecad.github.io/SourceDoc/dd/d39/classautomotive__design_1_1point__on__surface__pair__value.html
scraped_at: 2025-09-08T15:09:54.187135
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [point_on_surface_pair_value](../../dd/d39/classautomotive__design_1_1point__on__surface__pair__value.html)

[List of all members](../../df/d97/classautomotive__design_1_1point__on__surface__pair__value-members.html) | Public Member Functions | Public Attributes

automotive_design.point_on_surface_pair_value Class Reference

##  Public Member Functions  
  
---  
def | [actual_orientation](../../dd/d39/classautomotive__design_1_1point__on__surface__pair__value.html#a2aece238cda38df267731bcd16ec51e0) ()  
def | [actual_point_on_surface](../../dd/d39/classautomotive__design_1_1point__on__surface__pair__value.html#a9514470ebdf414f63b3eb92ba7b9b544) ()  
def | [input_orientation](../../dd/d39/classautomotive__design_1_1point__on__surface__pair__value.html#aada0a916f217a547638ece0549bab809) ()  
def | [pair_value_applies_to_pair](../../dd/d39/classautomotive__design_1_1point__on__surface__pair__value.html#a5812e7ccc335fcc1cc37c445f638ac65) ()  
def | [wr1](../../dd/d39/classautomotive__design_1_1point__on__surface__pair__value.html#a2454872ed4ed456e2eb7ab538da2cd51) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.pair_value](../../db/de8/classautomotive__design_1_1pair__value.html)  
def | [applies_to_pair](../../db/de8/classautomotive__design_1_1pair__value.html#ac72d51f14b9a115645f17d03853905b0) ()  
  
##  Public Attributes  
  
---  
|
[actual_point_on_surface](../../dd/d39/classautomotive__design_1_1point__on__surface__pair__value.html#a49d3bb3ca88b2c701be909e83ea828ed)  
|
[input_orientation](../../dd/d39/classautomotive__design_1_1point__on__surface__pair__value.html#a6322bdd3334a8c1a25ec7750c8d4e1c3)  
|
[pair_surface](../../dd/d39/classautomotive__design_1_1point__on__surface__pair__value.html#af87d48703d808468a39548ba8ad53886)  
|
[pair_value_applies_to_pair](../../dd/d39/classautomotive__design_1_1point__on__surface__pair__value.html#aa09e83582742ea5d62547c64c8eb7f31)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.pair_value](../../db/de8/classautomotive__design_1_1pair__value.html)  
|
[applies_to_pair](../../db/de8/classautomotive__design_1_1pair__value.html#a106ebf8650036d6170ceb14ab03178be)  
  
## Detailed Description

    
    
    Entity point_on_surface_pair_value definition.
    
        :param pair_value_applies_to_pair
        :type pair_value_applies_to_pair:point_on_surface_pair
    
        :param actual_point_on_surface
        :type actual_point_on_surface:point_on_surface
    
        :param input_orientation
        :type input_orientation:spatial_rotation
    
        :param actual_orientation
        :type actual_orientation:ARRAY(ypr_index(yaw),ypr_index(roll),'REAL', scope = schema_scope)

## Member Function Documentation

## ◆ actual_orientation()

def automotive_design.point_on_surface_pair_value.actual_orientation  | ( | | ) |   
---|---|---|---|---  
  
References
[automotive_design.convert_spatial_to_ypr_rotation()](../../d4/ddf/namespaceautomotive__design.html#a058754fa239e16337e2523ca8c701635),
[automotive_design.point_on_surface_pair_value.input_orientation](../../dd/d39/classautomotive__design_1_1point__on__surface__pair__value.html#a6322bdd3334a8c1a25ec7750c8d4e1c3),
[automotive_design.spherical_pair_value.input_orientation](../../d9/df0/classautomotive__design_1_1spherical__pair__value.html#af4fd63cd49a310a5071f88d152c0ca28),
[automotive_design.point_on_planar_curve_pair_value.input_orientation](../../dc/dee/classautomotive__design_1_1point__on__planar__curve__pair__value.html#a52a70702a4cbd3d0e34f276424f21edd),
App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

## ◆ actual_point_on_surface()

def automotive_design.point_on_surface_pair_value.actual_point_on_surface  | ( | | ) |   
---|---|---|---|---  
  
References
automotive_design.point_on_surface_pair_value._actual_point_on_surface, and
automotive_design.rolling_surface_pair_value._actual_point_on_surface.

## ◆ input_orientation()

def automotive_design.point_on_surface_pair_value.input_orientation  | ( | | ) |   
---|---|---|---|---  
  
References automotive_design.point_on_surface_pair_value._input_orientation,
automotive_design.spherical_pair_value._input_orientation,
automotive_design.point_on_planar_curve_pair_value._input_orientation, and
[automotive_design.spatial_rotation](../../d4/ddf/namespaceautomotive__design.html#a00cc3839c4b44d3392ff28931c351a7f).

Referenced by
[automotive_design.point_on_surface_pair_value.actual_orientation()](../../dd/d39/classautomotive__design_1_1point__on__surface__pair__value.html#a2aece238cda38df267731bcd16ec51e0),
[automotive_design.spherical_pair_value.actual_orientation()](../../d9/df0/classautomotive__design_1_1spherical__pair__value.html#a526bffde5dcdfec8691f40b2a8bf8206),
and
[automotive_design.point_on_planar_curve_pair_value.actual_orientation()](../../dc/dee/classautomotive__design_1_1point__on__planar__curve__pair__value.html#ae3306548683e440284d6329395beb9a6).

## ◆ pair_value_applies_to_pair()

def automotive_design.point_on_surface_pair_value.pair_value_applies_to_pair  | ( | | ) |   
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

def automotive_design.point_on_surface_pair_value.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
## Member Data Documentation

## ◆ actual_point_on_surface

automotive_design.point_on_surface_pair_value.actual_point_on_surface  
---  
  
## ◆ input_orientation

automotive_design.point_on_surface_pair_value.input_orientation  
---  
  
Referenced by
[automotive_design.point_on_surface_pair_value.actual_orientation()](../../dd/d39/classautomotive__design_1_1point__on__surface__pair__value.html#a2aece238cda38df267731bcd16ec51e0),
[automotive_design.spherical_pair_value.actual_orientation()](../../d9/df0/classautomotive__design_1_1spherical__pair__value.html#a526bffde5dcdfec8691f40b2a8bf8206),
and
[automotive_design.point_on_planar_curve_pair_value.actual_orientation()](../../dc/dee/classautomotive__design_1_1point__on__planar__curve__pair__value.html#ae3306548683e440284d6329395beb9a6).

## ◆ pair_surface

automotive_design.point_on_surface_pair_value.pair_surface  
---  
  
Referenced by
[automotive_design.point_on_surface_pair.wr1()](../../de/df2/classautomotive__design_1_1point__on__surface__pair.html#a7d512562d6ed849a3c08ebfb80437cab).

## ◆ pair_value_applies_to_pair

automotive_design.point_on_surface_pair_value.pair_value_applies_to_pair  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

