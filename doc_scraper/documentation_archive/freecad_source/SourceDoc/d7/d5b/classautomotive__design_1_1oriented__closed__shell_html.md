---
url: https://freecad.github.io/SourceDoc/d7/d5b/classautomotive__design_1_1oriented__closed__shell.html
scraped_at: 2025-09-08T15:08:54.960131
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [oriented_closed_shell](../../d7/d5b/classautomotive__design_1_1oriented__closed__shell.html)

[List of all members](../../d0/d59/classautomotive__design_1_1oriented__closed__shell-members.html) | Public Member Functions | Public Attributes

automotive_design.oriented_closed_shell Class Reference

##  Public Member Functions  
  
---  
def | [closed_shell_element](../../d7/d5b/classautomotive__design_1_1oriented__closed__shell.html#aced2341a33ff8ab1097125eecd7af051) ()  
def | [connected_face_set_cfs_faces](../../d7/d5b/classautomotive__design_1_1oriented__closed__shell.html#ad7d361e551523d0543f2e339ffc7d817) ()  
def | [orientation](../../d7/d5b/classautomotive__design_1_1oriented__closed__shell.html#a6bcea3dd1a473a511028d01e3257cf04) ()  
def | [wr1](../../d7/d5b/classautomotive__design_1_1oriented__closed__shell.html#a0da2258e93d513f58e218ae0054a8fda) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.connected_face_set](../../dd/d2e/classautomotive__design_1_1connected__face__set.html)  
def | [cfs_faces](../../dd/d2e/classautomotive__design_1_1connected__face__set.html#a5440cdb79795c6d848623bdc27901893) ()  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
def | [name](../../d3/d20/classautomotive__design_1_1representation__item.html#a33b5812d92aa0d107b4fd4274c17b9d9) ()  
def | [wr1](../../d3/d20/classautomotive__design_1_1representation__item.html#af350c19fc5e5763d4991494a99d979ed) (self)  
  
##  Public Attributes  
  
---  
|
[closed_shell_element](../../d7/d5b/classautomotive__design_1_1oriented__closed__shell.html#a5fe25dae72b7b147d968ac3a94e30f53)  
|
[orientation](../../d7/d5b/classautomotive__design_1_1oriented__closed__shell.html#a2756f072ec5167549d3efe595b496720)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.connected_face_set](../../dd/d2e/classautomotive__design_1_1connected__face__set.html)  
|
[cfs_faces](../../dd/d2e/classautomotive__design_1_1connected__face__set.html#a0ae248b4dc101ee5e9af9312e6d77a82)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
|
[name](../../d3/d20/classautomotive__design_1_1representation__item.html#a3d48fe912053adaf5f187b606fa81c87)  
  
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

def automotive_design.oriented_closed_shell.closed_shell_element  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.oriented_closed_shell._closed_shell_element,
automotive_design.oriented_closed_shell._closed_shell_element, and
config_control_design.oriented_closed_shell._closed_shell_element.

## ◆ connected_face_set_cfs_faces()

def automotive_design.oriented_closed_shell.connected_face_set_cfs_faces  | ( | | ) |   
---|---|---|---|---  
  
References
[automotive_design.conditional_reverse()](../../d4/ddf/namespaceautomotive__design.html#a0cf87f7c473043dddd4fa6ec17c949e9),
App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

## ◆ orientation()

def automotive_design.oriented_closed_shell.orientation  | ( | | ) |   
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

def automotive_design.oriented_closed_shell.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html#af350c19fc5e5763d4991494a99d979ed).

References App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

## Member Data Documentation

## ◆ closed_shell_element

automotive_design.oriented_closed_shell.closed_shell_element  
---  
  
## ◆ orientation

automotive_design.oriented_closed_shell.orientation  
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

