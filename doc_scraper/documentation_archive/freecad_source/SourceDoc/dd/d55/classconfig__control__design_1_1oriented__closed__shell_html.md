---
url: https://freecad.github.io/SourceDoc/dd/d55/classconfig__control__design_1_1oriented__closed__shell.html
scraped_at: 2025-09-08T15:22:39.443840
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [config_control_design](../../d4/d07/namespaceconfig__control__design.html)
  * [oriented_closed_shell](../../dd/d55/classconfig__control__design_1_1oriented__closed__shell.html)

[List of all members](../../d8/de5/classconfig__control__design_1_1oriented__closed__shell-members.html) | Public Member Functions | Public Attributes

config_control_design.oriented_closed_shell Class Reference

##  Public Member Functions  
  
---  
def | [closed_shell_element](../../dd/d55/classconfig__control__design_1_1oriented__closed__shell.html#a59a717d2c9a962ce1d39156d4a1b5af3) ()  
def | [connected_face_set_cfs_faces](../../dd/d55/classconfig__control__design_1_1oriented__closed__shell.html#a0dd5f9be39a04824c09789a3ef70a4a1) ()  
def | [orientation](../../dd/d55/classconfig__control__design_1_1oriented__closed__shell.html#a974a57d793bc6092d21ac03d8a5c30a7) ()  
def | [wr1](../../dd/d55/classconfig__control__design_1_1oriented__closed__shell.html#a2313b7609fe7500486b5690cad185eb8) (self)  
![-](../../closed.png) Public Member Functions inherited from
[config_control_design.connected_face_set](../../d5/d72/classconfig__control__design_1_1connected__face__set.html)  
def | [cfs_faces](../../d5/d72/classconfig__control__design_1_1connected__face__set.html#a256a0268c099dc46a56f32e9c453604f) ()  
![-](../../closed.png) Public Member Functions inherited from
[config_control_design.representation_item](../../d9/d69/classconfig__control__design_1_1representation__item.html)  
def | [name](../../d9/d69/classconfig__control__design_1_1representation__item.html#a5ea878073c85170f328deff23a9c5732) ()  
def | [wr1](../../d9/d69/classconfig__control__design_1_1representation__item.html#a4cdc1db49341dedc8f271ec89801c713) (self)  
  
##  Public Attributes  
  
---  
|
[closed_shell_element](../../dd/d55/classconfig__control__design_1_1oriented__closed__shell.html#a6e90d93bd2e39fab853e49710ea31bf8)  
|
[orientation](../../dd/d55/classconfig__control__design_1_1oriented__closed__shell.html#a2d05607735a94a32df7295a87a57c750)  
![-](../../closed.png) Public Attributes inherited from
[config_control_design.connected_face_set](../../d5/d72/classconfig__control__design_1_1connected__face__set.html)  
|
[cfs_faces](../../d5/d72/classconfig__control__design_1_1connected__face__set.html#abc38d49c2f1ba0d5014592f081abf07a)  
![-](../../closed.png) Public Attributes inherited from
[config_control_design.representation_item](../../d9/d69/classconfig__control__design_1_1representation__item.html)  
|
[name](../../d9/d69/classconfig__control__design_1_1representation__item.html#a0e8be677f8410825a46422f3c0e1c128)  
  
## Detailed Description

    
    
    Entity oriented_closed_shell definition.
    
        :param closed_shell_element
        :type closed_shell_element:closed_shell
    
        :param orientation
        :type orientation:BOOLEAN
    
        :param connected_face_set_cfs_faces
        :type connected_face_set_cfs_faces:SET(1,None,'face', scope = schema_scope)

## Member Function Documentation

## ◆ closed_shell_element()

def config_control_design.oriented_closed_shell.closed_shell_element  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.oriented_closed_shell._closed_shell_element,
automotive_design.oriented_closed_shell._closed_shell_element, and
config_control_design.oriented_closed_shell._closed_shell_element.

## ◆ connected_face_set_cfs_faces()

def config_control_design.oriented_closed_shell.connected_face_set_cfs_faces  | ( | | ) |   
---|---|---|---|---  
  
References
[config_control_design.conditional_reverse()](../../d4/d07/namespaceconfig__control__design.html#acfc4ecb160dfb8077be5a52b6e5b962a),
App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

## ◆ orientation()

def config_control_design.oriented_closed_shell.orientation  | ( | | ) |   
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

def config_control_design.oriented_closed_shell.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[config_control_design.representation_item](../../d9/d69/classconfig__control__design_1_1representation__item.html#a4cdc1db49341dedc8f271ec89801c713).

References App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

## Member Data Documentation

## ◆ closed_shell_element

config_control_design.oriented_closed_shell.closed_shell_element  
---  
  
## ◆ orientation

config_control_design.oriented_closed_shell.orientation  
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

