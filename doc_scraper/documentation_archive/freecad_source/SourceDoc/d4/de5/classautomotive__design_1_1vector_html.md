---
url: https://freecad.github.io/SourceDoc/d4/de5/classautomotive__design_1_1vector.html
scraped_at: 2025-09-08T15:15:15.545512
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [vector](../../d4/de5/classautomotive__design_1_1vector.html)

[List of all members](../../dd/d1b/classautomotive__design_1_1vector-members.html) | Public Member Functions | Public Attributes

automotive_design.vector Class Reference

##  Public Member Functions  
  
---  
def | [magnitude](../../d4/de5/classautomotive__design_1_1vector.html#a2e1df9550ab5551fcfa44948fef63e1f) ()  
def | [orientation](../../d4/de5/classautomotive__design_1_1vector.html#a76ae461186bb39d06adbbe8b795ff273) ()  
def | [wr1](../../d4/de5/classautomotive__design_1_1vector.html#a2cb1e85a75d76e3ffed04d177f73b547) (self)  
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
[magnitude](../../d4/de5/classautomotive__design_1_1vector.html#a61cf6387b2b66578647daf650c615788)  
|
[orientation](../../d4/de5/classautomotive__design_1_1vector.html#af5c0217f6079aa2597a44ab968edbc15)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
|
[name](../../d3/d20/classautomotive__design_1_1representation__item.html#a3d48fe912053adaf5f187b606fa81c87)  
  
## Detailed Description

    
    
    Entity vector definition.
    
        :param orientation
        :type orientation:direction
    
        :param magnitude
        :type magnitude:length_measure

## Member Function Documentation

## ◆ magnitude()

def automotive_design.vector.magnitude  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.geometric_tolerance._magnitude,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.vector._magnitude,
automotive_design.geometric_tolerance._magnitude,
automotive_design.vector._magnitude, config_control_design.vector._magnitude,
ifc2x3.ifcvector._magnitude, and ifc4.ifcvector._magnitude.

Referenced by
[ifc4.ifcaxis2placement3d.axistorefdirposition()](../../d1/db1/classifc4_1_1ifcaxis2placement3d.html#a1ba847e352152530b214a783a8171193),
[ifc4.ifcvector.maggreaterorequalzero()](../../d0/d94/classifc4_1_1ifcvector.html#ab4962c7e746a132927dc6913315ffaab),
[automotive_design.geometric_tolerance.wr1()](../../d9/d7e/classautomotive__design_1_1geometric__tolerance.html#a2fce32370e842edeb4692d15bba8963e),
[automotive_design.vector.wr1()](../../d4/de5/classautomotive__design_1_1vector.html#a2cb1e85a75d76e3ffed04d177f73b547),
[config_control_design.vector.wr1()](../../dc/d96/classconfig__control__design_1_1vector.html#a3afca0b28ec6498757c78eeca7c67b63),
[ifc2x3.ifcvector.wr1()](../../d3/d7f/classifc2x3_1_1ifcvector.html#aadca39e08b21c072fdfe6fe035461bff),
[automotive_design.axis2_placement_3d.wr4()](../../d8/d42/classautomotive__design_1_1axis2__placement__3d.html#a958dfcfe4ab4e5a077320cb4e34bbb4d),
[config_control_design.axis2_placement_3d.wr4()](../../dd/d2a/classconfig__control__design_1_1axis2__placement__3d.html#a8bec18bae8e6717f6914141ff0f73deb),
and
[ifc2x3.ifcaxis2placement3d.wr4()](../../d8/dbf/classifc2x3_1_1ifcaxis2placement3d.html#af6680b5dd24bd5ec433f4dd35da87a91).

## ◆ orientation()

def automotive_design.vector.orientation  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.oriented_surface._orientation,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.face_bound._orientation,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.oriented_edge._orientation,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.oriented_open_shell._orientation,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.vector._orientation,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.oriented_face._orientation,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.light_source_directional._orientation,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.oriented_path._orientation,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.runout_zone_definition._orientation,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.light_source_spot._orientation,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.oriented_closed_shell._orientation,
automotive_design.surface_pair._orientation,
automotive_design.oriented_surface._orientation,
automotive_design.face_bound._orientation,
automotive_design.oriented_edge._orientation,
automotive_design.oriented_open_shell._orientation,
automotive_design.planar_curve_pair._orientation,
automotive_design.vector._orientation,
automotive_design.point_on_planar_curve_pair._orientation,
automotive_design.oriented_face._orientation,
automotive_design.light_source_directional._orientation,
automotive_design.oriented_path._orientation,
automotive_design.runout_zone_definition._orientation,
automotive_design.light_source_spot._orientation,
automotive_design.oriented_closed_shell._orientation,
config_control_design.face_bound._orientation,
config_control_design.oriented_edge._orientation,
config_control_design.oriented_open_shell._orientation,
config_control_design.vector._orientation,
config_control_design.oriented_face._orientation,
config_control_design.oriented_path._orientation,
config_control_design.oriented_closed_shell._orientation,
ifc2x3.ifcfacebound._orientation,
ifc2x3.ifclightsourcedirectional._orientation,
ifc2x3.ifcorientededge._orientation, ifc2x3.ifcvector._orientation,
ifc2x3.ifclightsourcespot._orientation, ifc4.ifcfacebound._orientation,
ifc4.ifclightsourcedirectional._orientation,
ifc4.ifcorientededge._orientation, ifc4.ifcvector._orientation, and
ifc4.ifclightsourcespot._orientation.

Referenced by
[ifc2x3.ifcvector.dim()](../../d3/d7f/classifc2x3_1_1ifcvector.html#acba206090ebaf1068c18b522050ab356),
[ifc4.ifcvector.dim()](../../d0/d94/classifc4_1_1ifcvector.html#a472491a5b13134e67210054e2ac45890),
[ifc2x3.ifcorientededge.ifcedge_edgeend()](../../de/d2d/classifc2x3_1_1ifcorientededge.html#a48ae1b77c8027eb94457c5b2f5ce9d57),
[ifc4.ifcorientededge.ifcedge_edgeend()](../../db/d8f/classifc4_1_1ifcorientededge.html#a7c669bd36e25635cb26bfb6d77c00868),
[ifc2x3.ifcorientededge.ifcedge_edgestart()](../../de/d2d/classifc2x3_1_1ifcorientededge.html#ad883a6cb358a09f6d01852c81a9fbb14),
and
[ifc4.ifcorientededge.ifcedge_edgestart()](../../db/d8f/classifc4_1_1ifcorientededge.html#af7e5ed22105ed5dc292ee815e78c50cd).

## ◆ wr1()

def automotive_design.vector.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[automotive_design.geometric_representation_item](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html#a9677d2be5fc5c7c8ccb6819380198bbc).

References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.geometric_tolerance.magnitude,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.vector.magnitude,
[automotive_design.geometric_tolerance.magnitude](../../d9/d7e/classautomotive__design_1_1geometric__tolerance.html#a87c87342f2c3ac1a069a3226c167ba27),
[automotive_design.vector.magnitude](../../d4/de5/classautomotive__design_1_1vector.html#a61cf6387b2b66578647daf650c615788),
[config_control_design.vector.magnitude](../../dc/d96/classconfig__control__design_1_1vector.html#ab59ccc1e3595befbb06507adde628f5c),
[ifc2x3.ifcvector.magnitude](../../d3/d7f/classifc2x3_1_1ifcvector.html#a03813aa97a694f2cf81c04000fb27404),
[ifc4.ifcvector.magnitude](../../d0/d94/classifc4_1_1ifcvector.html#a1b4e2585353e99743eeaf7e3b1370407),
[geoff_geometry::Vector2d.magnitude()](../../d2/d05/classgeoff__geometry_1_1Vector2d.html#afdd063cb0f49ced482f66374d68832dc),
and
[geoff_geometry::Vector3d.magnitude()](../../d1/d95/classgeoff__geometry_1_1Vector3d.html#a62b9732b6b8a1d50c7f3766f53c6a6e0).

## Member Data Documentation

## ◆ magnitude

automotive_design.vector.magnitude  
---  
  
Referenced by
[ifc4.ifcaxis2placement3d.axistorefdirposition()](../../d1/db1/classifc4_1_1ifcaxis2placement3d.html#a1ba847e352152530b214a783a8171193),
[ifc4.ifcvector.maggreaterorequalzero()](../../d0/d94/classifc4_1_1ifcvector.html#ab4962c7e746a132927dc6913315ffaab),
[automotive_design.geometric_tolerance.wr1()](../../d9/d7e/classautomotive__design_1_1geometric__tolerance.html#a2fce32370e842edeb4692d15bba8963e),
[automotive_design.vector.wr1()](../../d4/de5/classautomotive__design_1_1vector.html#a2cb1e85a75d76e3ffed04d177f73b547),
[config_control_design.vector.wr1()](../../dc/d96/classconfig__control__design_1_1vector.html#a3afca0b28ec6498757c78eeca7c67b63),
[ifc2x3.ifcvector.wr1()](../../d3/d7f/classifc2x3_1_1ifcvector.html#aadca39e08b21c072fdfe6fe035461bff),
[automotive_design.axis2_placement_3d.wr4()](../../d8/d42/classautomotive__design_1_1axis2__placement__3d.html#a958dfcfe4ab4e5a077320cb4e34bbb4d),
[config_control_design.axis2_placement_3d.wr4()](../../dd/d2a/classconfig__control__design_1_1axis2__placement__3d.html#a8bec18bae8e6717f6914141ff0f73deb),
and
[ifc2x3.ifcaxis2placement3d.wr4()](../../d8/dbf/classifc2x3_1_1ifcaxis2placement3d.html#af6680b5dd24bd5ec433f4dd35da87a91).

## ◆ orientation

automotive_design.vector.orientation  
---  
  
Referenced by
[ifc2x3.ifcvector.dim()](../../d3/d7f/classifc2x3_1_1ifcvector.html#acba206090ebaf1068c18b522050ab356),
[ifc4.ifcvector.dim()](../../d0/d94/classifc4_1_1ifcvector.html#a472491a5b13134e67210054e2ac45890),
[ifc2x3.ifcorientededge.ifcedge_edgeend()](../../de/d2d/classifc2x3_1_1ifcorientededge.html#a48ae1b77c8027eb94457c5b2f5ce9d57),
[ifc4.ifcorientededge.ifcedge_edgeend()](../../db/d8f/classifc4_1_1ifcorientededge.html#a7c669bd36e25635cb26bfb6d77c00868),
[ifc2x3.ifcorientededge.ifcedge_edgestart()](../../de/d2d/classifc2x3_1_1ifcorientededge.html#ad883a6cb358a09f6d01852c81a9fbb14),
and
[ifc4.ifcorientededge.ifcedge_edgestart()](../../db/d8f/classifc4_1_1ifcorientededge.html#af7e5ed22105ed5dc292ee815e78c50cd).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

