---
url: https://freecad.github.io/SourceDoc/da/d77/classconfig__control__design_1_1oriented__edge.html
scraped_at: 2025-09-08T15:22:40.446975
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [config_control_design](../../d4/d07/namespaceconfig__control__design.html)
  * [oriented_edge](../../da/d77/classconfig__control__design_1_1oriented__edge.html)

[List of all members](../../df/d9e/classconfig__control__design_1_1oriented__edge-members.html) | Public Member Functions | Public Attributes

config_control_design.oriented_edge Class Reference

##  Public Member Functions  
  
---  
def | [edge_edge_end](../../da/d77/classconfig__control__design_1_1oriented__edge.html#afa053dc7239adea71e6113d333811cd2) ()  
def | [edge_edge_start](../../da/d77/classconfig__control__design_1_1oriented__edge.html#aeb73c053a5bb785d85e9113a7bfcb7f4) ()  
def | [edge_element](../../da/d77/classconfig__control__design_1_1oriented__edge.html#ae7817eef745d88cc45318c18168e7852) ()  
def | [orientation](../../da/d77/classconfig__control__design_1_1oriented__edge.html#a0ea04f0b3edc7b9b24f4b74db0065f7b) ()  
def | [wr1](../../da/d77/classconfig__control__design_1_1oriented__edge.html#aa08dfa584a2620146072363818fea9f4) (self)  
![-](../../closed.png) Public Member Functions inherited from
[config_control_design.edge](../../d5/d3e/classconfig__control__design_1_1edge.html)  
def | [edge_end](../../d5/d3e/classconfig__control__design_1_1edge.html#a147b65a6978977430c46f8ab40b03c08) ()  
def | [edge_start](../../d5/d3e/classconfig__control__design_1_1edge.html#a81ec6e171ce1f0ea828cb717021e6e13) ()  
![-](../../closed.png) Public Member Functions inherited from
[config_control_design.representation_item](../../d9/d69/classconfig__control__design_1_1representation__item.html)  
def | [name](../../d9/d69/classconfig__control__design_1_1representation__item.html#a5ea878073c85170f328deff23a9c5732) ()  
def | [wr1](../../d9/d69/classconfig__control__design_1_1representation__item.html#a4cdc1db49341dedc8f271ec89801c713) (self)  
  
##  Public Attributes  
  
---  
|
[edge_element](../../da/d77/classconfig__control__design_1_1oriented__edge.html#aa5fcda4a46916e365c8d150b00baff30)  
|
[orientation](../../da/d77/classconfig__control__design_1_1oriented__edge.html#adc861f50a975c03a1691cd8d55846415)  
![-](../../closed.png) Public Attributes inherited from
[config_control_design.edge](../../d5/d3e/classconfig__control__design_1_1edge.html)  
|
[edge_end](../../d5/d3e/classconfig__control__design_1_1edge.html#a888e6fd2eb49c977bb80e57e05e412f5)  
|
[edge_start](../../d5/d3e/classconfig__control__design_1_1edge.html#a59f8150252d3cbc8ffe465d2ecdb0e86)  
![-](../../closed.png) Public Attributes inherited from
[config_control_design.representation_item](../../d9/d69/classconfig__control__design_1_1representation__item.html)  
|
[name](../../d9/d69/classconfig__control__design_1_1representation__item.html#a0e8be677f8410825a46422f3c0e1c128)  
  
## Detailed Description

    
    
    Entity oriented_edge definition.
    
        :param edge_element
        :type edge_element:edge
    
        :param orientation
        :type orientation:BOOLEAN
    
        :param edge_edge_start
        :type edge_edge_start:vertex
    
        :param edge_edge_end
        :type edge_edge_end:vertex

## Member Function Documentation

## ◆ edge_edge_end()

def config_control_design.oriented_edge.edge_edge_end  | ( | | ) |   
---|---|---|---|---  
  
References
[config_control_design.boolean_choose()](../../d4/d07/namespaceconfig__control__design.html#a63e562d2d39fdf2eb0d0e8f22c968177),
App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

## ◆ edge_edge_start()

def config_control_design.oriented_edge.edge_edge_start  | ( | | ) |   
---|---|---|---|---  
  
References
[config_control_design.boolean_choose()](../../d4/d07/namespaceconfig__control__design.html#a63e562d2d39fdf2eb0d0e8f22c968177),
App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

## ◆ edge_element()

def config_control_design.oriented_edge.edge_element  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.oriented_edge._edge_element,
automotive_design.oriented_edge._edge_element, and
config_control_design.oriented_edge._edge_element.

Referenced by
[automotive_design.seam_edge.wr1()](../../d1/d38/classautomotive__design_1_1seam__edge.html#a6867f7f7e20c40119163b629ca0b1573),
and
[automotive_design.seam_edge.wr2()](../../d1/d38/classautomotive__design_1_1seam__edge.html#a3e9b6478fcf0b0635c010697146a0435).

## ◆ orientation()

def config_control_design.oriented_edge.orientation  | ( | | ) |   
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

def config_control_design.oriented_edge.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[config_control_design.representation_item](../../d9/d69/classconfig__control__design_1_1representation__item.html#a4cdc1db49341dedc8f271ec89801c713).

References App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

## Member Data Documentation

## ◆ edge_element

config_control_design.oriented_edge.edge_element  
---  
  
Referenced by
[automotive_design.seam_edge.wr1()](../../d1/d38/classautomotive__design_1_1seam__edge.html#a6867f7f7e20c40119163b629ca0b1573),
and
[automotive_design.seam_edge.wr2()](../../d1/d38/classautomotive__design_1_1seam__edge.html#a3e9b6478fcf0b0635c010697146a0435).

## ◆ orientation

config_control_design.oriented_edge.orientation  
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

  * FreeCAD/src/Mod/Import/App/config_control_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

