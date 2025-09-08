---
url: https://freecad.github.io/SourceDoc/d6/d5b/classautomotive__design_1_1point__on__planar__curve__pair.html
scraped_at: 2025-09-08T15:09:48.159761
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [point_on_planar_curve_pair](../../d6/d5b/classautomotive__design_1_1point__on__planar__curve__pair.html)

[List of all members](../../d1/d57/classautomotive__design_1_1point__on__planar__curve__pair-members.html) | Public Member Functions | Public Attributes

automotive_design.point_on_planar_curve_pair Class Reference

##  Public Member Functions  
  
---  
def | [orientation](../../d6/d5b/classautomotive__design_1_1point__on__planar__curve__pair.html#a6809787964bb5e46d4d4968e02146194) ()  
def | [pair_curve](../../d6/d5b/classautomotive__design_1_1point__on__planar__curve__pair.html#ad2ee11d0c4f42343c0c95404e2f6c25c) ()  
def | [wr1](../../d6/d5b/classautomotive__design_1_1point__on__planar__curve__pair.html#acaf537b23b8ca4d04b0a3b8df4656a07) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.kinematic_pair](../../d4/d4f/classautomotive__design_1_1kinematic__pair.html)  
def | [joint](../../d4/d4f/classautomotive__design_1_1kinematic__pair.html#a3cc1a3fa91c668bc412ae98a6bb71801) ()  
def | [pair_placement_in_first_link_context](../../d4/d4f/classautomotive__design_1_1kinematic__pair.html#a4c2d01c20c5af49ab32473d657a4c064) ()  
def | [pair_placement_in_second_link_context](../../d4/d4f/classautomotive__design_1_1kinematic__pair.html#a95c998e19e5ff9bcc07073444b9a551a) ()  
def | [wr1](../../d4/d4f/classautomotive__design_1_1kinematic__pair.html#a5bf15e517acfe323d781527c74eb5100) (self)  
def | [wr2](../../d4/d4f/classautomotive__design_1_1kinematic__pair.html#a3974063d988bfa776fba5cd5dac1c369) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.item_defined_transformation](../../d4/d91/classautomotive__design_1_1item__defined__transformation.html)  
def | [description](../../d4/d91/classautomotive__design_1_1item__defined__transformation.html#aea7020e577c8aaa199bb53f3c4f76a19) ()  
def | [name](../../d4/d91/classautomotive__design_1_1item__defined__transformation.html#a677249d4b240467fd9f1f5cc5279b24d) ()  
def | [transform_item_1](../../d4/d91/classautomotive__design_1_1item__defined__transformation.html#aeb7769f338ddfe3f332b6f71eeff0231) ()  
def | [transform_item_2](../../d4/d91/classautomotive__design_1_1item__defined__transformation.html#a9cfdcfa5ee62b8db6be37ae3c542158d) ()  
  
##  Public Attributes  
  
---  
|
[orientation](../../d6/d5b/classautomotive__design_1_1point__on__planar__curve__pair.html#a1a1097a31c3405955826472a4e77cb47)  
|
[pair_curve](../../d6/d5b/classautomotive__design_1_1point__on__planar__curve__pair.html#ad3518de5164a8e6fe8131c227e4b55db)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.kinematic_pair](../../d4/d4f/classautomotive__design_1_1kinematic__pair.html)  
|
[joint](../../d4/d4f/classautomotive__design_1_1kinematic__pair.html#a129569b8355d19cee7527672b69b6258)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.item_defined_transformation](../../d4/d91/classautomotive__design_1_1item__defined__transformation.html)  
|
[description](../../d4/d91/classautomotive__design_1_1item__defined__transformation.html#a9639e4a7f29564c744654086b0613457)  
|
[name](../../d4/d91/classautomotive__design_1_1item__defined__transformation.html#a71cd4ea422a14c796ae2be07eef15da8)  
|
[transform_item_1](../../d4/d91/classautomotive__design_1_1item__defined__transformation.html#a35a6126264cb2506a21004dbfc053ac0)  
|
[transform_item_2](../../d4/d91/classautomotive__design_1_1item__defined__transformation.html#ae1905883f0ed10110e83ec393fbda4a4)  
  
## Detailed Description

    
    
    Entity point_on_planar_curve_pair definition.
    
        :param pair_curve
        :type pair_curve:curve
    
        :param orientation
        :type orientation:BOOLEAN

## Member Function Documentation

## ◆ orientation()

def automotive_design.point_on_planar_curve_pair.orientation  | ( | | ) |   
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

## ◆ pair_curve()

def automotive_design.point_on_planar_curve_pair.pair_curve  | ( | | ) |   
---|---|---|---|---  
  
References automotive_design.point_on_planar_curve_pair._pair_curve.

Referenced by
[automotive_design.point_on_planar_curve_pair.wr1()](../../d6/d5b/classautomotive__design_1_1point__on__planar__curve__pair.html#acaf537b23b8ca4d04b0a3b8df4656a07).

## ◆ wr1()

def automotive_design.point_on_planar_curve_pair.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[automotive_design.kinematic_pair](../../d4/d4f/classautomotive__design_1_1kinematic__pair.html#a5bf15e517acfe323d781527c74eb5100).

References
[automotive_design.frame_associated_to_background()](../../d4/ddf/namespaceautomotive__design.html#ad23b750ebd23bb0492d76afd3d5b1f43),
[automotive_design.point_on_planar_curve_pair_range.pair_curve](../../db/d33/classautomotive__design_1_1point__on__planar__curve__pair__range.html#a15852a8665246c9106d97e892dd84670),
[automotive_design.point_on_planar_curve_pair.pair_curve](../../d6/d5b/classautomotive__design_1_1point__on__planar__curve__pair.html#ad3518de5164a8e6fe8131c227e4b55db),
[automotive_design.point_on_planar_curve_pair_value.pair_curve](../../dc/dee/classautomotive__design_1_1point__on__planar__curve__pair__value.html#a8b0cacbf2eba4cc170d7ee9bb0fba130),
App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

## Member Data Documentation

## ◆ orientation

automotive_design.point_on_planar_curve_pair.orientation  
---  
  
Referenced by
[ifc2x3.ifcvector.dim()](../../d3/d7f/classifc2x3_1_1ifcvector.html#acba206090ebaf1068c18b522050ab356),
[ifc4.ifcvector.dim()](../../d0/d94/classifc4_1_1ifcvector.html#a472491a5b13134e67210054e2ac45890),
[ifc2x3.ifcorientededge.ifcedge_edgeend()](../../de/d2d/classifc2x3_1_1ifcorientededge.html#a48ae1b77c8027eb94457c5b2f5ce9d57),
[ifc4.ifcorientededge.ifcedge_edgeend()](../../db/d8f/classifc4_1_1ifcorientededge.html#a7c669bd36e25635cb26bfb6d77c00868),
[ifc2x3.ifcorientededge.ifcedge_edgestart()](../../de/d2d/classifc2x3_1_1ifcorientededge.html#ad883a6cb358a09f6d01852c81a9fbb14),
and
[ifc4.ifcorientededge.ifcedge_edgestart()](../../db/d8f/classifc4_1_1ifcorientededge.html#af7e5ed22105ed5dc292ee815e78c50cd).

## ◆ pair_curve

automotive_design.point_on_planar_curve_pair.pair_curve  
---  
  
Referenced by
[automotive_design.point_on_planar_curve_pair.wr1()](../../d6/d5b/classautomotive__design_1_1point__on__planar__curve__pair.html#acaf537b23b8ca4d04b0a3b8df4656a07).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

