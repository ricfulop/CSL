---
url: https://freecad.github.io/SourceDoc/d3/d96/classconfig__control__design_1_1oriented__path.html
scraped_at: 2025-09-08T15:22:43.452258
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [config_control_design](../../d4/d07/namespaceconfig__control__design.html)
  * [oriented_path](../../d3/d96/classconfig__control__design_1_1oriented__path.html)

[List of all members](../../de/dc9/classconfig__control__design_1_1oriented__path-members.html) | Public Member Functions | Public Attributes

config_control_design.oriented_path Class Reference

##  Public Member Functions  
  
---  
def | [orientation](../../d3/d96/classconfig__control__design_1_1oriented__path.html#ac1592fd9fa615f9aa68970bce5a64283) ()  
def | [path_edge_list](../../d3/d96/classconfig__control__design_1_1oriented__path.html#a44334a264b3c5fbb0ea2d5ddd44e9040) ()  
def | [path_element](../../d3/d96/classconfig__control__design_1_1oriented__path.html#acf35c50535adde1b835d6507cd1b0b98) ()  
def | [wr1](../../d3/d96/classconfig__control__design_1_1oriented__path.html#a0ae7092eaa6a8c7b13c99557653a9ab1) (self)  
![-](../../closed.png) Public Member Functions inherited from
[config_control_design.path](../../dc/da4/classconfig__control__design_1_1path.html)  
def | [edge_list](../../dc/da4/classconfig__control__design_1_1path.html#ac959a1b80fdd2d38f27b91be3bd88f1d) ()  
def | [wr1](../../dc/da4/classconfig__control__design_1_1path.html#a17ae038fef1b2ddd0c2d569328cb44e1) (self)  
![-](../../closed.png) Public Member Functions inherited from
[config_control_design.representation_item](../../d9/d69/classconfig__control__design_1_1representation__item.html)  
def | [name](../../d9/d69/classconfig__control__design_1_1representation__item.html#a5ea878073c85170f328deff23a9c5732) ()  
def | [wr1](../../d9/d69/classconfig__control__design_1_1representation__item.html#a4cdc1db49341dedc8f271ec89801c713) (self)  
  
##  Public Attributes  
  
---  
|
[orientation](../../d3/d96/classconfig__control__design_1_1oriented__path.html#a381b5d7027573633ea5258fede9ffbc8)  
|
[path_element](../../d3/d96/classconfig__control__design_1_1oriented__path.html#afd7d7c0d37a6c8dc103aacaf5fffe6d1)  
![-](../../closed.png) Public Attributes inherited from
[config_control_design.path](../../dc/da4/classconfig__control__design_1_1path.html)  
|
[edge_list](../../dc/da4/classconfig__control__design_1_1path.html#a8bf66ee213db36b5e0876773535bf7d9)  
![-](../../closed.png) Public Attributes inherited from
[config_control_design.representation_item](../../d9/d69/classconfig__control__design_1_1representation__item.html)  
|
[name](../../d9/d69/classconfig__control__design_1_1representation__item.html#a0e8be677f8410825a46422f3c0e1c128)  
  
## Detailed Description

    
    
    Entity oriented_path definition.
    
        :param path_element
        :type path_element:path
    
        :param orientation
        :type orientation:BOOLEAN
    
        :param path_edge_list
        :type path_edge_list:LIST(1,None,'oriented_edge', scope = schema_scope)

## Member Function Documentation

## ◆ orientation()

def config_control_design.oriented_path.orientation  | ( | | ) |   
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

## ◆ path_edge_list()

def config_control_design.oriented_path.path_edge_list  | ( | | ) |   
---|---|---|---|---  
  
References
[config_control_design.conditional_reverse()](../../d4/d07/namespaceconfig__control__design.html#acfc4ecb160dfb8077be5a52b6e5b962a),
App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

## ◆ path_element()

def config_control_design.oriented_path.path_element  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.oriented_path._path_element,
automotive_design.oriented_path._path_element, and
config_control_design.oriented_path._path_element.

## ◆ wr1()

def config_control_design.oriented_path.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[config_control_design.path](../../dc/da4/classconfig__control__design_1_1path.html#a17ae038fef1b2ddd0c2d569328cb44e1).

References App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

## Member Data Documentation

## ◆ orientation

config_control_design.oriented_path.orientation  
---  
  
Referenced by
[ifc2x3.ifcvector.dim()](../../d3/d7f/classifc2x3_1_1ifcvector.html#acba206090ebaf1068c18b522050ab356),
[ifc4.ifcvector.dim()](../../d0/d94/classifc4_1_1ifcvector.html#a472491a5b13134e67210054e2ac45890),
[ifc2x3.ifcorientededge.ifcedge_edgeend()](../../de/d2d/classifc2x3_1_1ifcorientededge.html#a48ae1b77c8027eb94457c5b2f5ce9d57),
[ifc4.ifcorientededge.ifcedge_edgeend()](../../db/d8f/classifc4_1_1ifcorientededge.html#a7c669bd36e25635cb26bfb6d77c00868),
[ifc2x3.ifcorientededge.ifcedge_edgestart()](../../de/d2d/classifc2x3_1_1ifcorientededge.html#ad883a6cb358a09f6d01852c81a9fbb14),
and
[ifc4.ifcorientededge.ifcedge_edgestart()](../../db/d8f/classifc4_1_1ifcorientededge.html#af7e5ed22105ed5dc292ee815e78c50cd).

## ◆ path_element

config_control_design.oriented_path.path_element  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/config_control_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

