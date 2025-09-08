---
url: https://freecad.github.io/SourceDoc/d1/d4e/classautomotive__design_1_1oriented__face.html
scraped_at: 2025-09-08T15:08:56.963415
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [oriented_face](../../d1/d4e/classautomotive__design_1_1oriented__face.html)

[List of all members](../../db/df8/classautomotive__design_1_1oriented__face-members.html) | Public Member Functions | Public Attributes

automotive_design.oriented_face Class Reference

##  Public Member Functions  
  
---  
def | [face_bounds](../../d1/d4e/classautomotive__design_1_1oriented__face.html#a1132e0c6bcdc8e88cf907ebda78f9299) ()  
def | [face_element](../../d1/d4e/classautomotive__design_1_1oriented__face.html#a91da9e325d18ea20accd8c60e19b6818) ()  
def | [orientation](../../d1/d4e/classautomotive__design_1_1oriented__face.html#a645ffec37e77e2b3e6eb9cf616ac586a) ()  
def | [wr1](../../d1/d4e/classautomotive__design_1_1oriented__face.html#acbf7206d7c21e641627582b05ca53732) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.face](../../d4/d1b/classautomotive__design_1_1face.html)  
def | [bounds](../../d4/d1b/classautomotive__design_1_1face.html#af679fe2caae48769302c5f02959487bc) ()  
def | [wr1](../../d4/d1b/classautomotive__design_1_1face.html#a130adf47ee7912741b284ac0aa3f2208) (self)  
def | [wr2](../../d4/d1b/classautomotive__design_1_1face.html#a476bf9885f52fbbd7d6c683a16b44335) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
def | [name](../../d3/d20/classautomotive__design_1_1representation__item.html#a33b5812d92aa0d107b4fd4274c17b9d9) ()  
def | [wr1](../../d3/d20/classautomotive__design_1_1representation__item.html#af350c19fc5e5763d4991494a99d979ed) (self)  
  
##  Public Attributes  
  
---  
|
[face_element](../../d1/d4e/classautomotive__design_1_1oriented__face.html#aa769f97994c3743b48a76317090c4fbf)  
|
[orientation](../../d1/d4e/classautomotive__design_1_1oriented__face.html#abc96119bd3ed02606c37cdcf83a38fcd)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.face](../../d4/d1b/classautomotive__design_1_1face.html)  
|
[bounds](../../d4/d1b/classautomotive__design_1_1face.html#a78bfe1fdfc9d39b9e740428b5a355b4c)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
|
[name](../../d3/d20/classautomotive__design_1_1representation__item.html#a3d48fe912053adaf5f187b606fa81c87)  
  
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

def automotive_design.oriented_face.face_bounds  | ( | | ) |   
---|---|---|---|---  
  
References
[automotive_design.conditional_reverse()](../../d4/ddf/namespaceautomotive__design.html#a0cf87f7c473043dddd4fa6ec17c949e9),
App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

## ◆ face_element()

def automotive_design.oriented_face.face_element  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.oriented_face._face_element,
automotive_design.oriented_face._face_element, and
config_control_design.oriented_face._face_element.

## ◆ orientation()

def automotive_design.oriented_face.orientation  | ( | | ) |   
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

def automotive_design.oriented_face.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[automotive_design.face](../../d4/d1b/classautomotive__design_1_1face.html#a130adf47ee7912741b284ac0aa3f2208).

References App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

## Member Data Documentation

## ◆ face_element

automotive_design.oriented_face.face_element  
---  
  
## ◆ orientation

automotive_design.oriented_face.orientation  
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

