---
url: https://freecad.github.io/SourceDoc/d7/d9c/classconfig__control__design_1_1oriented__open__shell.html
scraped_at: 2025-09-08T15:22:42.453285
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [config_control_design](../../d4/d07/namespaceconfig__control__design.html)
  * [oriented_open_shell](../../d7/d9c/classconfig__control__design_1_1oriented__open__shell.html)

[List of all members](../../df/d11/classconfig__control__design_1_1oriented__open__shell-members.html) | Public Member Functions | Public Attributes

config_control_design.oriented_open_shell Class Reference

##  Public Member Functions  
  
---  
def | [connected_face_set_cfs_faces](../../d7/d9c/classconfig__control__design_1_1oriented__open__shell.html#a946c3b5dd1d66218ba5c8a9c510e6408) ()  
def | [open_shell_element](../../d7/d9c/classconfig__control__design_1_1oriented__open__shell.html#a06b7cdd52a3070aa0375b1d6aa27716d) ()  
def | [orientation](../../d7/d9c/classconfig__control__design_1_1oriented__open__shell.html#a0d38d864942e2654d81bcfd88c7ef037) ()  
def | [wr1](../../d7/d9c/classconfig__control__design_1_1oriented__open__shell.html#a9b90e70c840525977fd4347c9f1490d4) (self)  
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
[open_shell_element](../../d7/d9c/classconfig__control__design_1_1oriented__open__shell.html#a84d60b2eabb85232d7e8bd722e9490c6)  
|
[orientation](../../d7/d9c/classconfig__control__design_1_1oriented__open__shell.html#acc161561140b7905390f0045ea52b4f0)  
![-](../../closed.png) Public Attributes inherited from
[config_control_design.connected_face_set](../../d5/d72/classconfig__control__design_1_1connected__face__set.html)  
|
[cfs_faces](../../d5/d72/classconfig__control__design_1_1connected__face__set.html#abc38d49c2f1ba0d5014592f081abf07a)  
![-](../../closed.png) Public Attributes inherited from
[config_control_design.representation_item](../../d9/d69/classconfig__control__design_1_1representation__item.html)  
|
[name](../../d9/d69/classconfig__control__design_1_1representation__item.html#a0e8be677f8410825a46422f3c0e1c128)  
  
## Detailed Description

    
    
    Entity oriented_open_shell definition.
    
        :param open_shell_element
        :type open_shell_element:open_shell
    
        :param orientation
        :type orientation:BOOLEAN
    
        :param connected_face_set_cfs_faces
        :type connected_face_set_cfs_faces:SET(1,None,'face', scope = schema_scope)

## Member Function Documentation

## ◆ connected_face_set_cfs_faces()

def config_control_design.oriented_open_shell.connected_face_set_cfs_faces  | ( | | ) |   
---|---|---|---|---  
  
References
[config_control_design.conditional_reverse()](../../d4/d07/namespaceconfig__control__design.html#acfc4ecb160dfb8077be5a52b6e5b962a),
App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

## ◆ open_shell_element()

def config_control_design.oriented_open_shell.open_shell_element  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.oriented_open_shell._open_shell_element,
automotive_design.oriented_open_shell._open_shell_element, and
config_control_design.oriented_open_shell._open_shell_element.

## ◆ orientation()

def config_control_design.oriented_open_shell.orientation  | ( | | ) |   
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

def config_control_design.oriented_open_shell.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[config_control_design.representation_item](../../d9/d69/classconfig__control__design_1_1representation__item.html#a4cdc1db49341dedc8f271ec89801c713).

References App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

## Member Data Documentation

## ◆ open_shell_element

config_control_design.oriented_open_shell.open_shell_element  
---  
  
## ◆ orientation

config_control_design.oriented_open_shell.orientation  
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

