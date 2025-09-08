---
url: https://freecad.github.io/SourceDoc/d3/d78/classautomotive__design_1_1surface__pair.html
scraped_at: 2025-09-08T15:13:31.114468
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [surface_pair](../../d3/d78/classautomotive__design_1_1surface__pair.html)

[List of all members](../../d4/d18/classautomotive__design_1_1surface__pair-members.html) | Public Member Functions | Public Attributes

automotive_design.surface_pair Class Reference

##  Public Member Functions  
  
---  
def | [orientation](../../d3/d78/classautomotive__design_1_1surface__pair.html#ad0b958e6a55e01fc7525ea587b613b51) ()  
def | [surface_1](../../d3/d78/classautomotive__design_1_1surface__pair.html#a48f0f198f45b80dbe518c78860712ae5) ()  
def | [surface_2](../../d3/d78/classautomotive__design_1_1surface__pair.html#ac8d80a4ca6005f88509106754060fc47) ()  
def | [wr1](../../d3/d78/classautomotive__design_1_1surface__pair.html#a4e29aa1ef1ee68a84f0448f2535103e1) (self)  
def | [wr2](../../d3/d78/classautomotive__design_1_1surface__pair.html#ac70a19c48959c1ce8a4b2423f45373fc) (self)  
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
[orientation](../../d3/d78/classautomotive__design_1_1surface__pair.html#a66aa7a3b348dd806c1ec2c22a375a0c9)  
|
[surface_1](../../d3/d78/classautomotive__design_1_1surface__pair.html#afdb181c4b711025cc28cb016481e702b)  
|
[surface_2](../../d3/d78/classautomotive__design_1_1surface__pair.html#ab1c01bc42a0e5cc8fe047c9ae3db640d)  
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

    
    
    Entity surface_pair definition.
    
        :param surface_1
        :type surface_1:surface
    
        :param surface_2
        :type surface_2:surface
    
        :param orientation
        :type orientation:BOOLEAN

## Member Function Documentation

## ◆ orientation()

def automotive_design.surface_pair.orientation  | ( | | ) |   
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

## ◆ surface_1()

def automotive_design.surface_pair.surface_1  | ( | | ) |   
---|---|---|---|---  
  
References automotive_design.surface_pair._surface_1.

Referenced by
[automotive_design.surface_pair.wr1()](../../d3/d78/classautomotive__design_1_1surface__pair.html#a4e29aa1ef1ee68a84f0448f2535103e1).

## ◆ surface_2()

def automotive_design.surface_pair.surface_2  | ( | | ) |   
---|---|---|---|---  
  
References automotive_design.surface_pair._surface_2.

Referenced by
[automotive_design.surface_pair.wr2()](../../d3/d78/classautomotive__design_1_1surface__pair.html#ac70a19c48959c1ce8a4b2423f45373fc).

## ◆ wr1()

def automotive_design.surface_pair.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[automotive_design.kinematic_pair](../../d4/d4f/classautomotive__design_1_1kinematic__pair.html#a5bf15e517acfe323d781527c74eb5100).

References
[automotive_design.frame_associated_to_background()](../../d4/ddf/namespaceautomotive__design.html#ad23b750ebd23bb0492d76afd3d5b1f43),
App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, Gui::Dialog::DownloadManager.self,
[automotive_design.surface_pair.surface_1](../../d3/d78/classautomotive__design_1_1surface__pair.html#afdb181c4b711025cc28cb016481e702b),
[automotive_design.rolling_surface_pair_value.surface_1](../../df/dc4/classautomotive__design_1_1rolling__surface__pair__value.html#abfb4a64b5c7f2fa34f2c2118f81d8a9c),
[automotive_design.sliding_surface_pair_value.surface_1](../../d0/d0a/classautomotive__design_1_1sliding__surface__pair__value.html#adc83a9ddcba0766605d9d795791d3afd),
and
[automotive_design.surface_pair_range.surface_1](../../d2/d05/classautomotive__design_1_1surface__pair__range.html#a48c41a35950032be3399a07414ff431c).

## ◆ wr2()

def automotive_design.surface_pair.wr2  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[automotive_design.kinematic_pair](../../d4/d4f/classautomotive__design_1_1kinematic__pair.html#a3974063d988bfa776fba5cd5dac1c369).

References
[automotive_design.frame_associated_to_background()](../../d4/ddf/namespaceautomotive__design.html#ad23b750ebd23bb0492d76afd3d5b1f43),
App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, Gui::Dialog::DownloadManager.self,
[automotive_design.surface_pair.surface_2](../../d3/d78/classautomotive__design_1_1surface__pair.html#ab1c01bc42a0e5cc8fe047c9ae3db640d),
[automotive_design.sliding_surface_pair_value.surface_2](../../d0/d0a/classautomotive__design_1_1sliding__surface__pair__value.html#a84074875831f92befc31e35634a64011),
and
[automotive_design.surface_pair_range.surface_2](../../d2/d05/classautomotive__design_1_1surface__pair__range.html#a3fd626a9aa1ba32080840d6732f9f431).

## Member Data Documentation

## ◆ orientation

automotive_design.surface_pair.orientation  
---  
  
Referenced by
[ifc2x3.ifcvector.dim()](../../d3/d7f/classifc2x3_1_1ifcvector.html#acba206090ebaf1068c18b522050ab356),
[ifc4.ifcvector.dim()](../../d0/d94/classifc4_1_1ifcvector.html#a472491a5b13134e67210054e2ac45890),
[ifc2x3.ifcorientededge.ifcedge_edgeend()](../../de/d2d/classifc2x3_1_1ifcorientededge.html#a48ae1b77c8027eb94457c5b2f5ce9d57),
[ifc4.ifcorientededge.ifcedge_edgeend()](../../db/d8f/classifc4_1_1ifcorientededge.html#a7c669bd36e25635cb26bfb6d77c00868),
[ifc2x3.ifcorientededge.ifcedge_edgestart()](../../de/d2d/classifc2x3_1_1ifcorientededge.html#ad883a6cb358a09f6d01852c81a9fbb14),
and
[ifc4.ifcorientededge.ifcedge_edgestart()](../../db/d8f/classifc4_1_1ifcorientededge.html#af7e5ed22105ed5dc292ee815e78c50cd).

## ◆ surface_1

automotive_design.surface_pair.surface_1  
---  
  
Referenced by
[automotive_design.surface_pair.wr1()](../../d3/d78/classautomotive__design_1_1surface__pair.html#a4e29aa1ef1ee68a84f0448f2535103e1).

## ◆ surface_2

automotive_design.surface_pair.surface_2  
---  
  
Referenced by
[automotive_design.surface_pair.wr2()](../../d3/d78/classautomotive__design_1_1surface__pair.html#ac70a19c48959c1ce8a4b2423f45373fc).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

