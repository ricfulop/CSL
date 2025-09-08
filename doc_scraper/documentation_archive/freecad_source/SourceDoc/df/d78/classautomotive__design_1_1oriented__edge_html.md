---
url: https://freecad.github.io/SourceDoc/df/d78/classautomotive__design_1_1oriented__edge.html
scraped_at: 2025-09-08T15:08:55.966084
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [oriented_edge](../../df/d78/classautomotive__design_1_1oriented__edge.html)

[List of all members](../../d2/d48/classautomotive__design_1_1oriented__edge-members.html) | Public Member Functions | Public Attributes

automotive_design.oriented_edge Class Reference

##  Public Member Functions  
  
---  
def | [edge_edge_end](../../df/d78/classautomotive__design_1_1oriented__edge.html#abd23cb2d3a06df7a099535c627a788ca) ()  
def | [edge_edge_start](../../df/d78/classautomotive__design_1_1oriented__edge.html#aae8227b4329f0ddc4b6b98af1785bbcc) ()  
def | [edge_element](../../df/d78/classautomotive__design_1_1oriented__edge.html#a86854020000731fe77a19ee0b7a5cba4) ()  
def | [orientation](../../df/d78/classautomotive__design_1_1oriented__edge.html#aa89cd8b5b8c38f3012b9cbc2541ec1c9) ()  
def | [wr1](../../df/d78/classautomotive__design_1_1oriented__edge.html#ab057e0e3b994112699bfee82400bb309) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.edge](../../d5/de3/classautomotive__design_1_1edge.html)  
def | [edge_end](../../d5/de3/classautomotive__design_1_1edge.html#adc21d6bea2bf55ae7403d64f2ccdf8ea) ()  
def | [edge_start](../../d5/de3/classautomotive__design_1_1edge.html#afe397bf57aa3052ba73da826700d8b38) ()  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
def | [name](../../d3/d20/classautomotive__design_1_1representation__item.html#a33b5812d92aa0d107b4fd4274c17b9d9) ()  
def | [wr1](../../d3/d20/classautomotive__design_1_1representation__item.html#af350c19fc5e5763d4991494a99d979ed) (self)  
  
##  Public Attributes  
  
---  
|
[edge_element](../../df/d78/classautomotive__design_1_1oriented__edge.html#a070e25d8dd72fffb2f7212b5f5d83635)  
|
[orientation](../../df/d78/classautomotive__design_1_1oriented__edge.html#acedf3b884b8f3bee4c3278a58b4fe976)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.edge](../../d5/de3/classautomotive__design_1_1edge.html)  
|
[edge_end](../../d5/de3/classautomotive__design_1_1edge.html#af2dfde2eea876a40ced85b67041a6078)  
|
[edge_start](../../d5/de3/classautomotive__design_1_1edge.html#acea1eb826a678cc369a23d36bb3b6181)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
|
[name](../../d3/d20/classautomotive__design_1_1representation__item.html#a3d48fe912053adaf5f187b606fa81c87)  
  
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

def automotive_design.oriented_edge.edge_edge_end  | ( | | ) |   
---|---|---|---|---  
  
References
[automotive_design.boolean_choose()](../../d4/ddf/namespaceautomotive__design.html#ac1347f0fa3880f1ace10b5893c890a68),
App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

## ◆ edge_edge_start()

def automotive_design.oriented_edge.edge_edge_start  | ( | | ) |   
---|---|---|---|---  
  
References
[automotive_design.boolean_choose()](../../d4/ddf/namespaceautomotive__design.html#ac1347f0fa3880f1ace10b5893c890a68),
App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

## ◆ edge_element()

def automotive_design.oriented_edge.edge_element  | ( | | ) |   
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

def automotive_design.oriented_edge.orientation  | ( | | ) |   
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

def automotive_design.oriented_edge.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html#af350c19fc5e5763d4991494a99d979ed).

Reimplemented in
[automotive_design.seam_edge](../../d1/d38/classautomotive__design_1_1seam__edge.html#a6867f7f7e20c40119163b629ca0b1573).

References App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

## Member Data Documentation

## ◆ edge_element

automotive_design.oriented_edge.edge_element  
---  
  
Referenced by
[automotive_design.seam_edge.wr1()](../../d1/d38/classautomotive__design_1_1seam__edge.html#a6867f7f7e20c40119163b629ca0b1573),
and
[automotive_design.seam_edge.wr2()](../../d1/d38/classautomotive__design_1_1seam__edge.html#a3e9b6478fcf0b0635c010697146a0435).

## ◆ orientation

automotive_design.oriented_edge.orientation  
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

