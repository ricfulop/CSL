---
url: https://freecad.github.io/SourceDoc/d8/de5/classautomotive__design_1_1light__source__positional.html
scraped_at: 2025-09-08T15:07:24.568507
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [light_source_positional](../../d8/de5/classautomotive__design_1_1light__source__positional.html)

[List of all members](../../da/dd7/classautomotive__design_1_1light__source__positional-members.html) | Public Member Functions | Public Attributes

automotive_design.light_source_positional Class Reference

##  Public Member Functions  
  
---  
def | [constant_attenuation](../../d8/de5/classautomotive__design_1_1light__source__positional.html#a4281f0ee04cc3d075ef90cce531d886a) ()  
def | [distance_attenuation](../../d8/de5/classautomotive__design_1_1light__source__positional.html#a6b958200cf96fcf773860a30e8bbb9bb) ()  
def | [position](../../d8/de5/classautomotive__design_1_1light__source__positional.html#a8129fd9fcf351c77d8902fd37491ac7d) ()  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.light_source](../../db/db0/classautomotive__design_1_1light__source.html)  
def | [light_colour](../../db/db0/classautomotive__design_1_1light__source.html#a170507ec942d8d2edcb9ef18be96c462) ()  
def | [wr1](../../db/db0/classautomotive__design_1_1light__source.html#a95d6334708a04c815dcbf732603845ad) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.geometric_representation_item](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html)  
def | [dim](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html#aef245618450610e88788dcaea46ad742) ()  
def | [wr1](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html#a9677d2be5fc5c7c8ccb6819380198bbc) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
def | [name](../../d3/d20/classautomotive__design_1_1representation__item.html#a33b5812d92aa0d107b4fd4274c17b9d9) ()  
def | [wr1](../../d3/d20/classautomotive__design_1_1representation__item.html#af350c19fc5e5763d4991494a99d979ed) (self)  
  
##  Public Attributes  
  
---  
|
[constant_attenuation](../../d8/de5/classautomotive__design_1_1light__source__positional.html#a6b50ece25b2aab413dc4a37622158e49)  
|
[distance_attenuation](../../d8/de5/classautomotive__design_1_1light__source__positional.html#a9c3f1f3e9c7dd843c07e54891160eeb7)  
|
[position](../../d8/de5/classautomotive__design_1_1light__source__positional.html#aa821386498bf0c4f34f21f6902df1c20)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.light_source](../../db/db0/classautomotive__design_1_1light__source.html)  
|
[light_colour](../../db/db0/classautomotive__design_1_1light__source.html#a1fa139f1d16478cad7c34a61e2001562)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
|
[name](../../d3/d20/classautomotive__design_1_1representation__item.html#a3d48fe912053adaf5f187b606fa81c87)  
  
## Detailed Description

    
    
    Entity light_source_positional definition.
    
        :param position
        :type position:cartesian_point
    
        :param constant_attenuation
        :type constant_attenuation:REAL
    
        :param distance_attenuation
        :type distance_attenuation:REAL

## Member Function Documentation

## ◆ constant_attenuation()

def automotive_design.light_source_positional.constant_attenuation  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.light_source_positional._constant_attenuation,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.light_source_spot._constant_attenuation,
automotive_design.light_source_positional._constant_attenuation, and
automotive_design.light_source_spot._constant_attenuation.

## ◆ distance_attenuation()

def automotive_design.light_source_positional.distance_attenuation  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.light_source_positional._distance_attenuation,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.light_source_spot._distance_attenuation,
automotive_design.light_source_positional._distance_attenuation, and
automotive_design.light_source_spot._distance_attenuation.

## ◆ position()

def automotive_design.light_source_positional.position  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.conic._position,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.light_source_positional._position,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.elementary_surface._position,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.right_circular_cylinder._position,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.right_angular_wedge._position,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.torus._position,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.right_circular_cone._position,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.light_source_spot._position,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.block._position,
automotive_design.conic._position,
automotive_design.light_source_positional._position,
automotive_design.elementary_surface._position,
automotive_design.right_circular_cylinder._position,
automotive_design.right_angular_wedge._position,
automotive_design.torus._position,
automotive_design.right_circular_cone._position,
automotive_design.light_source_spot._position,
automotive_design.block._position, config_control_design.conic._position,
config_control_design.elementary_surface._position,
ifc2x3.ifcsweptsurface._position, ifc2x3.ifcparameterizedprofiledef._position,
ifc2x3.ifcsweptareasolid._position, ifc2x3.ifccsgprimitive3d._position,
ifc2x3.ifcconic._position, ifc2x3.ifcpolygonalboundedhalfspace._position,
ifc2x3.ifcelementarysurface._position,
ifc2x3.ifclightsourcepositional._position,
ifc2x3.ifclightsourcegoniometric._position, ifc4.ifcsweptsurface._position,
ifc4.ifcparameterizedprofiledef._position, ifc4.ifcsweptareasolid._position,
ifc4.ifccsgprimitive3d._position, ifc4.ifcconic._position,
ifc4.ifcpolygonalboundedhalfspace._position,
ifc4.ifcelementarysurface._position, ifc4.ifclightsourcepositional._position,
ifc4.ifclightsourcegoniometric._position, and
ifc4.ifcrecurrencepattern._position.

Referenced by
[WorkingPlane.Plane.alignToPointAndAxis()](../../d3/d93/classWorkingPlane_1_1Plane.html#ab85860830e3debec48d3cdb58d30621a),
[WorkingPlane.Plane.alignToPointAndAxis_SVG()](../../d3/d93/classWorkingPlane_1_1Plane.html#a53cb561d317b813ea9a22ef8e319104d),
[WorkingPlane.Plane.copy()](../../d3/d93/classWorkingPlane_1_1Plane.html#ad5a25c4e17593442d7a38bd51cf7167a),
[ifc2x3.ifcsweptsurface.dim()](../../d6/df8/classifc2x3_1_1ifcsweptsurface.html#a5eb3187a1e204615771d1c71c0e05346),
[ifc2x3.ifcelementarysurface.dim()](../../dc/d78/classifc2x3_1_1ifcelementarysurface.html#aa9fc1e4bb64357615bba0ad16fa6bc10),
[WorkingPlane.Plane.getGlobalCoords()](../../d3/d93/classWorkingPlane_1_1Plane.html#a1b8410be9ee2eefb1e5c3902d4d1a230),
[WorkingPlane.Plane.getLocalCoords()](../../d3/d93/classWorkingPlane_1_1Plane.html#ab4027587aa29bc4393a52df8159376e1),
[WorkingPlane.Plane.getParameters()](../../d3/d93/classWorkingPlane_1_1Plane.html#a22bffbf8caab92f815500ed57b857427),
[WorkingPlane.Plane.getPlacement()](../../d3/d93/classWorkingPlane_1_1Plane.html#aeb4cd9d5da24076f5984cfd0994ed75f),
[WorkingPlane.Plane.offsetToPoint()](../../d3/d93/classWorkingPlane_1_1Plane.html#accc43f410bbe85c53bfad80b68903c6c),
[WorkingPlane.Plane.projectPoint()](../../d3/d93/classWorkingPlane_1_1Plane.html#a1918c0d5d231f78520826f24326111e6),
[WorkingPlane.Plane.restore()](../../d3/d93/classWorkingPlane_1_1Plane.html#abe9dafedd4a855a65c40666b5391f4a3),
[WorkingPlane.Plane.save()](../../d3/d93/classWorkingPlane_1_1Plane.html#a5f765f888050e49b7ee71785e689d0fd),
[WorkingPlane.Plane.setFromParameters()](../../d3/d93/classWorkingPlane_1_1Plane.html#a417c10c501c570723b1c6b471da3fa13),
and
[WorkingPlane.Plane.setFromPlacement()](../../d3/d93/classWorkingPlane_1_1Plane.html#ab9f10a2a72fa2ba198adbfad26ec26c2).

## Member Data Documentation

## ◆ constant_attenuation

automotive_design.light_source_positional.constant_attenuation  
---  
  
## ◆ distance_attenuation

automotive_design.light_source_positional.distance_attenuation  
---  
  
## ◆ position

automotive_design.light_source_positional.position  
---  
  
Referenced by
[WorkingPlane.Plane.alignToPointAndAxis()](../../d3/d93/classWorkingPlane_1_1Plane.html#ab85860830e3debec48d3cdb58d30621a),
[WorkingPlane.Plane.alignToPointAndAxis_SVG()](../../d3/d93/classWorkingPlane_1_1Plane.html#a53cb561d317b813ea9a22ef8e319104d),
[WorkingPlane.Plane.copy()](../../d3/d93/classWorkingPlane_1_1Plane.html#ad5a25c4e17593442d7a38bd51cf7167a),
[ifc2x3.ifcsweptsurface.dim()](../../d6/df8/classifc2x3_1_1ifcsweptsurface.html#a5eb3187a1e204615771d1c71c0e05346),
[ifc2x3.ifcelementarysurface.dim()](../../dc/d78/classifc2x3_1_1ifcelementarysurface.html#aa9fc1e4bb64357615bba0ad16fa6bc10),
[WorkingPlane.Plane.getGlobalCoords()](../../d3/d93/classWorkingPlane_1_1Plane.html#a1b8410be9ee2eefb1e5c3902d4d1a230),
[WorkingPlane.Plane.getLocalCoords()](../../d3/d93/classWorkingPlane_1_1Plane.html#ab4027587aa29bc4393a52df8159376e1),
[WorkingPlane.Plane.getParameters()](../../d3/d93/classWorkingPlane_1_1Plane.html#a22bffbf8caab92f815500ed57b857427),
[WorkingPlane.Plane.getPlacement()](../../d3/d93/classWorkingPlane_1_1Plane.html#aeb4cd9d5da24076f5984cfd0994ed75f),
[WorkingPlane.Plane.offsetToPoint()](../../d3/d93/classWorkingPlane_1_1Plane.html#accc43f410bbe85c53bfad80b68903c6c),
[WorkingPlane.Plane.projectPoint()](../../d3/d93/classWorkingPlane_1_1Plane.html#a1918c0d5d231f78520826f24326111e6),
[WorkingPlane.Plane.restore()](../../d3/d93/classWorkingPlane_1_1Plane.html#abe9dafedd4a855a65c40666b5391f4a3),
[WorkingPlane.Plane.save()](../../d3/d93/classWorkingPlane_1_1Plane.html#a5f765f888050e49b7ee71785e689d0fd),
[WorkingPlane.Plane.setFromParameters()](../../d3/d93/classWorkingPlane_1_1Plane.html#a417c10c501c570723b1c6b471da3fa13),
and
[WorkingPlane.Plane.setFromPlacement()](../../d3/d93/classWorkingPlane_1_1Plane.html#ab9f10a2a72fa2ba198adbfad26ec26c2).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

