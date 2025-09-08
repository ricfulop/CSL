---
url: https://freecad.github.io/SourceDoc/d1/dba/classautomotive__design_1_1torus.html
scraped_at: 2025-09-08T15:14:45.417134
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [torus](../../d1/dba/classautomotive__design_1_1torus.html)

[List of all members](../../d6/df2/classautomotive__design_1_1torus-members.html) | Public Member Functions | Public Attributes

automotive_design.torus Class Reference

##  Public Member Functions  
  
---  
def | [major_radius](../../d1/dba/classautomotive__design_1_1torus.html#ad2b1e8aeb7f20e4a679c8c90a8f0f8a8) ()  
def | [minor_radius](../../d1/dba/classautomotive__design_1_1torus.html#a2dde1f59989923b40d0a8cce493388fb) ()  
def | [position](../../d1/dba/classautomotive__design_1_1torus.html#a92c6e1de90ba66824732ac29b88a703e) ()  
def | [wr1](../../d1/dba/classautomotive__design_1_1torus.html#ae9a9ef7a7e5e4b865d2a9c3d1ed450bd) (self)  
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
[major_radius](../../d1/dba/classautomotive__design_1_1torus.html#a5907f2a419aea80d1863ee1fa5d26ed8)  
|
[minor_radius](../../d1/dba/classautomotive__design_1_1torus.html#a967d95189338f94dc03c429f307013fd)  
|
[position](../../d1/dba/classautomotive__design_1_1torus.html#a6119007b718c244c35b38052b3147d3d)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
|
[name](../../d3/d20/classautomotive__design_1_1representation__item.html#a3d48fe912053adaf5f187b606fa81c87)  
  
## Detailed Description

    
    
    Entity torus definition.
    
        :param position
        :type position:axis1_placement
    
        :param major_radius
        :type major_radius:positive_length_measure
    
        :param minor_radius
        :type minor_radius:positive_length_measure

## Member Function Documentation

## ◆ major_radius()

def automotive_design.torus.major_radius  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.toroidal_surface._major_radius,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.torus._major_radius,
automotive_design.toroidal_surface._major_radius,
automotive_design.torus._major_radius, and
config_control_design.toroidal_surface._major_radius.

Referenced by
[automotive_design.degenerate_toroidal_surface.wr1()](../../dc/d6e/classautomotive__design_1_1degenerate__toroidal__surface.html#ada91d37d93ce419c3d1e1cd1c372cef7),
[automotive_design.torus.wr1()](../../d1/dba/classautomotive__design_1_1torus.html#ae9a9ef7a7e5e4b865d2a9c3d1ed450bd),
and
[config_control_design.degenerate_toroidal_surface.wr1()](../../df/dad/classconfig__control__design_1_1degenerate__toroidal__surface.html#ace3808e03b5d62b58c8b281839737b57).

## ◆ minor_radius()

def automotive_design.torus.minor_radius  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.toroidal_surface._minor_radius,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.torus._minor_radius,
automotive_design.toroidal_surface._minor_radius,
automotive_design.torus._minor_radius, and
config_control_design.toroidal_surface._minor_radius.

Referenced by
[automotive_design.degenerate_toroidal_surface.wr1()](../../dc/d6e/classautomotive__design_1_1degenerate__toroidal__surface.html#ada91d37d93ce419c3d1e1cd1c372cef7),
[automotive_design.torus.wr1()](../../d1/dba/classautomotive__design_1_1torus.html#ae9a9ef7a7e5e4b865d2a9c3d1ed450bd),
and
[config_control_design.degenerate_toroidal_surface.wr1()](../../df/dad/classconfig__control__design_1_1degenerate__toroidal__surface.html#ace3808e03b5d62b58c8b281839737b57).

## ◆ position()

def automotive_design.torus.position  | ( | | ) |   
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

## ◆ wr1()

def automotive_design.torus.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[automotive_design.geometric_representation_item](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html#a9677d2be5fc5c7c8ccb6819380198bbc).

References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.toroidal_surface.major_radius,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.torus.major_radius,
[automotive_design.toroidal_surface.major_radius](../../dd/daf/classautomotive__design_1_1toroidal__surface.html#a49c468b596d4042fc69d35d3da9a26e0),
[automotive_design.torus.major_radius](../../d1/dba/classautomotive__design_1_1torus.html#a5907f2a419aea80d1863ee1fa5d26ed8),
[config_control_design.toroidal_surface.major_radius](../../d3/d7e/classconfig__control__design_1_1toroidal__surface.html#a78b546623eb8a989a8ae636b6c09a9e9),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.toroidal_surface.minor_radius,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.torus.minor_radius,
[automotive_design.toroidal_surface.minor_radius](../../dd/daf/classautomotive__design_1_1toroidal__surface.html#a867d306837362228ad9f822d18fb448d),
[automotive_design.torus.minor_radius](../../d1/dba/classautomotive__design_1_1torus.html#a967d95189338f94dc03c429f307013fd),
and
[config_control_design.toroidal_surface.minor_radius](../../d3/d7e/classconfig__control__design_1_1toroidal__surface.html#aaab59ff146369decf339d46680d2e8ab).

## Member Data Documentation

## ◆ major_radius

automotive_design.torus.major_radius  
---  
  
Referenced by
[automotive_design.degenerate_toroidal_surface.wr1()](../../dc/d6e/classautomotive__design_1_1degenerate__toroidal__surface.html#ada91d37d93ce419c3d1e1cd1c372cef7),
[automotive_design.torus.wr1()](../../d1/dba/classautomotive__design_1_1torus.html#ae9a9ef7a7e5e4b865d2a9c3d1ed450bd),
and
[config_control_design.degenerate_toroidal_surface.wr1()](../../df/dad/classconfig__control__design_1_1degenerate__toroidal__surface.html#ace3808e03b5d62b58c8b281839737b57).

## ◆ minor_radius

automotive_design.torus.minor_radius  
---  
  
Referenced by
[automotive_design.degenerate_toroidal_surface.wr1()](../../dc/d6e/classautomotive__design_1_1degenerate__toroidal__surface.html#ada91d37d93ce419c3d1e1cd1c372cef7),
[automotive_design.torus.wr1()](../../d1/dba/classautomotive__design_1_1torus.html#ae9a9ef7a7e5e4b865d2a9c3d1ed450bd),
and
[config_control_design.degenerate_toroidal_surface.wr1()](../../df/dad/classconfig__control__design_1_1degenerate__toroidal__surface.html#ace3808e03b5d62b58c8b281839737b57).

## ◆ position

automotive_design.torus.position  
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

