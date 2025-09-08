---
url: https://freecad.github.io/SourceDoc/df/d13/classconfig__control__design_1_1oriented__face.html
scraped_at: 2025-09-08T15:22:41.468485
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [config_control_design](../../d4/d07/namespaceconfig__control__design.html)
  * [oriented_face](../../df/d13/classconfig__control__design_1_1oriented__face.html)

[List of all members](../../d5/d7f/classconfig__control__design_1_1oriented__face-members.html) | Public Member Functions | Public Attributes

config_control_design.oriented_face Class Reference

##  Public Member Functions  
  
---  
def | [face_bounds](../../df/d13/classconfig__control__design_1_1oriented__face.html#a0c9bee0e6dbab6620d88f43e05433cdb) ()  
def | [face_element](../../df/d13/classconfig__control__design_1_1oriented__face.html#a642a413ed0cb535f1f97466bfcdb952f) ()  
def | [orientation](../../df/d13/classconfig__control__design_1_1oriented__face.html#a30e25aa3274b6cc1d02a3d989fc55aef) ()  
def | [wr1](../../df/d13/classconfig__control__design_1_1oriented__face.html#a02dac2e1235628092f8fbe4e2e5cd28a) (self)  
![-](../../closed.png) Public Member Functions inherited from
[config_control_design.face](../../d3/d78/classconfig__control__design_1_1face.html)  
def | [bounds](../../d3/d78/classconfig__control__design_1_1face.html#a313840aa2d165b012db67959d15aa6d2) ()  
def | [wr1](../../d3/d78/classconfig__control__design_1_1face.html#a047aab57b192ef6ce0bb7924eafc9bd4) (self)  
def | [wr2](../../d3/d78/classconfig__control__design_1_1face.html#ac882f231c3972a4f8938f97eecbf0774) (self)  
![-](../../closed.png) Public Member Functions inherited from
[config_control_design.representation_item](../../d9/d69/classconfig__control__design_1_1representation__item.html)  
def | [name](../../d9/d69/classconfig__control__design_1_1representation__item.html#a5ea878073c85170f328deff23a9c5732) ()  
def | [wr1](../../d9/d69/classconfig__control__design_1_1representation__item.html#a4cdc1db49341dedc8f271ec89801c713) (self)  
  
##  Public Attributes  
  
---  
|
[face_element](../../df/d13/classconfig__control__design_1_1oriented__face.html#aae731c788bb0d19eae08e891e38f3244)  
|
[orientation](../../df/d13/classconfig__control__design_1_1oriented__face.html#a58c2c26d1d2cb953b4a7812c794e2605)  
![-](../../closed.png) Public Attributes inherited from
[config_control_design.face](../../d3/d78/classconfig__control__design_1_1face.html)  
|
[bounds](../../d3/d78/classconfig__control__design_1_1face.html#acd48bf7a8d0eb03155bb61c39a19cbc8)  
![-](../../closed.png) Public Attributes inherited from
[config_control_design.representation_item](../../d9/d69/classconfig__control__design_1_1representation__item.html)  
|
[name](../../d9/d69/classconfig__control__design_1_1representation__item.html#a0e8be677f8410825a46422f3c0e1c128)  
  
## Detailed Description

    
    
    Entity oriented_face definition.
    
        :param face_element
        :type face_element:face
    
        :param orientation
        :type orientation:BOOLEAN
    
        :param face_bounds
        :type face_bounds:SET(1,None,'face_bound', scope = schema_scope)

## Member Function Documentation

## ◆ face_bounds()

def config_control_design.oriented_face.face_bounds  | ( | | ) |   
---|---|---|---|---  
  
References
[config_control_design.conditional_reverse()](../../d4/d07/namespaceconfig__control__design.html#acfc4ecb160dfb8077be5a52b6e5b962a),
App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

## ◆ face_element()

def config_control_design.oriented_face.face_element  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.oriented_face._face_element,
automotive_design.oriented_face._face_element, and
config_control_design.oriented_face._face_element.

## ◆ orientation()

def config_control_design.oriented_face.orientation  | ( | | ) |   
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

def config_control_design.oriented_face.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[config_control_design.face](../../d3/d78/classconfig__control__design_1_1face.html#a047aab57b192ef6ce0bb7924eafc9bd4).

References App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

## Member Data Documentation

## ◆ face_element

config_control_design.oriented_face.face_element  
---  
  
## ◆ orientation

config_control_design.oriented_face.orientation  
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

