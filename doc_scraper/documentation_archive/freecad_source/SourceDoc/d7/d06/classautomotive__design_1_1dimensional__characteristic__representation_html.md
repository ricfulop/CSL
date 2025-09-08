---
url: https://freecad.github.io/SourceDoc/d7/d06/classautomotive__design_1_1dimensional__characteristic__representation.html
scraped_at: 2025-09-08T15:03:52.704167
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [dimensional_characteristic_representation](../../d7/d06/classautomotive__design_1_1dimensional__characteristic__representation.html)

[List of all members](../../d2/da2/classautomotive__design_1_1dimensional__characteristic__representation-members.html) | Public Member Functions | Public Attributes

automotive_design.dimensional_characteristic_representation Class Reference

##  Public Member Functions  
  
---  
def | [dimension](../../d7/d06/classautomotive__design_1_1dimensional__characteristic__representation.html#a7e0a2beb19251139a59306d9249e9aa0) ()  
def | [representation](../../d7/d06/classautomotive__design_1_1dimensional__characteristic__representation.html#afeaba5e037a9f566917de7a2ec161ef8) ()  
  
##  Public Attributes  
  
---  
|
[dimension](../../d7/d06/classautomotive__design_1_1dimensional__characteristic__representation.html#a8850381c01e6695fc2333db3d91632a0)  
|
[representation](../../d7/d06/classautomotive__design_1_1dimensional__characteristic__representation.html#aef8c6d21bfbb31e6ab5b842c3ebbfe8a)  
  
## Detailed Description

    
    
    Entity dimensional_characteristic_representation definition.
    
        :param dimension
        :type dimension:dimensional_characteristic
    
        :param representation
        :type representation:shape_dimension_representation

## Member Function Documentation

## ◆ dimension()

def automotive_design.dimensional_characteristic_representation.dimension  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.dimensional_characteristic_representation._dimension,
automotive_design.dimensional_characteristic_representation._dimension, and
[automotive_design.dimensional_characteristic](../../d4/ddf/namespaceautomotive__design.html#af66ceeaf76d800b970df269cdbb56518).

Referenced by
[femtaskpanels.task_mesh_gmsh._TaskPanel.choose_dimension()](../../d6/d90/classfemtaskpanels_1_1task__mesh__gmsh_1_1__TaskPanel.html#a38fd2105dcbfe9ea0ed33aa09e7423f4),
[femmesh.gmshtools.GmshTools.get_boundary_layer_data()](../../d9/d7b/classfemmesh_1_1gmshtools_1_1GmshTools.html#a0440a1779567a3ab6a78f954107a00db),
[femmesh.gmshtools.GmshTools.get_dimension()](../../d9/d7b/classfemmesh_1_1gmshtools_1_1GmshTools.html#ac4f07e6d1b7f7f16ee1bbb2ad68a4542),
[femtaskpanels.task_mesh_gmsh._TaskPanel.set_mesh_params()](../../d6/d90/classfemtaskpanels_1_1task__mesh__gmsh_1_1__TaskPanel.html#a23ddf7b0852aa5fc2e9b156d40c10348),
[femtaskpanels.task_mesh_gmsh._TaskPanel.update()](../../d6/d90/classfemtaskpanels_1_1task__mesh__gmsh_1_1__TaskPanel.html#a684d236263b413e2d04839f3ce9cacb7),
and
[femmesh.gmshtools.GmshTools.write_geo()](../../d9/d7b/classfemmesh_1_1gmshtools_1_1GmshTools.html#a33c814384f75e15c1d5316754b9ff3bf).

## ◆ representation()

def automotive_design.dimensional_characteristic_representation.representation  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.dimensional_characteristic_representation._representation,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.action_property_representation._representation,
automotive_design.resource_property_representation._representation,
automotive_design.dimensional_characteristic_representation._representation,
automotive_design.action_property_representation._representation,
ifc2x3.ifcproduct._representation, and ifc4.ifcproduct._representation.

Referenced by
[ifc4.ifcproduct.placementforshaperepresentation()](../../d6/dab/classifc4_1_1ifcproduct.html#a8229715516a6f27af649dd71077e1311),
[automotive_design.motion_link_relationship.wr1()](../../db/df6/classautomotive__design_1_1motion__link__relationship.html#a2a143a9c64a2508fbd7e804fc705c05a),
[automotive_design.pcurve.wr1()](../../d4/d4b/classautomotive__design_1_1pcurve.html#a6c4a5ef371ff37f5f5e7135ec479d77c),
[automotive_design.degenerate_pcurve.wr1()](../../de/d21/classautomotive__design_1_1degenerate__pcurve.html#a3e59549e46796a2d3373707c359f962b),
[config_control_design.pcurve.wr1()](../../d8/d67/classconfig__control__design_1_1pcurve.html#a081b5cdb8f8e42e856b54ca97fe9ba05),
[config_control_design.degenerate_pcurve.wr1()](../../d3/d07/classconfig__control__design_1_1degenerate__pcurve.html#aae1772a95d3ed412ea932efd74ac2697),
[ifc2x3.ifcproduct.wr1()](../../d1/d19/classifc2x3_1_1ifcproduct.html#a1ae2bc8df067f80a59c11ffa956ba588),
[automotive_design.pcurve.wr2()](../../d4/d4b/classautomotive__design_1_1pcurve.html#a6c8a7a5f4d71cc2803cfbb42ae9b04c1),
[automotive_design.degenerate_pcurve.wr2()](../../de/d21/classautomotive__design_1_1degenerate__pcurve.html#a8e7be64a5c78f0540518110da63a3fd9),
[config_control_design.pcurve.wr2()](../../d8/d67/classconfig__control__design_1_1pcurve.html#a2748ae4c83d716e0e15781382f5fd9d7),
and
[config_control_design.degenerate_pcurve.wr2()](../../d3/d07/classconfig__control__design_1_1degenerate__pcurve.html#ac95757f1b795f22cd0ba44a1ffbb0474).

## Member Data Documentation

## ◆ dimension

automotive_design.dimensional_characteristic_representation.dimension  
---  
  
Referenced by
[femtaskpanels.task_mesh_gmsh._TaskPanel.choose_dimension()](../../d6/d90/classfemtaskpanels_1_1task__mesh__gmsh_1_1__TaskPanel.html#a38fd2105dcbfe9ea0ed33aa09e7423f4),
[femmesh.gmshtools.GmshTools.get_boundary_layer_data()](../../d9/d7b/classfemmesh_1_1gmshtools_1_1GmshTools.html#a0440a1779567a3ab6a78f954107a00db),
[femmesh.gmshtools.GmshTools.get_dimension()](../../d9/d7b/classfemmesh_1_1gmshtools_1_1GmshTools.html#ac4f07e6d1b7f7f16ee1bbb2ad68a4542),
[femtaskpanels.task_mesh_gmsh._TaskPanel.set_mesh_params()](../../d6/d90/classfemtaskpanels_1_1task__mesh__gmsh_1_1__TaskPanel.html#a23ddf7b0852aa5fc2e9b156d40c10348),
[femtaskpanels.task_mesh_gmsh._TaskPanel.update()](../../d6/d90/classfemtaskpanels_1_1task__mesh__gmsh_1_1__TaskPanel.html#a684d236263b413e2d04839f3ce9cacb7),
and
[femmesh.gmshtools.GmshTools.write_geo()](../../d9/d7b/classfemmesh_1_1gmshtools_1_1GmshTools.html#a33c814384f75e15c1d5316754b9ff3bf).

## ◆ representation

automotive_design.dimensional_characteristic_representation.representation  
---  
  
Referenced by
[ifc4.ifcproduct.placementforshaperepresentation()](../../d6/dab/classifc4_1_1ifcproduct.html#a8229715516a6f27af649dd71077e1311),
[automotive_design.motion_link_relationship.wr1()](../../db/df6/classautomotive__design_1_1motion__link__relationship.html#a2a143a9c64a2508fbd7e804fc705c05a),
[automotive_design.pcurve.wr1()](../../d4/d4b/classautomotive__design_1_1pcurve.html#a6c4a5ef371ff37f5f5e7135ec479d77c),
[automotive_design.degenerate_pcurve.wr1()](../../de/d21/classautomotive__design_1_1degenerate__pcurve.html#a3e59549e46796a2d3373707c359f962b),
[config_control_design.pcurve.wr1()](../../d8/d67/classconfig__control__design_1_1pcurve.html#a081b5cdb8f8e42e856b54ca97fe9ba05),
[config_control_design.degenerate_pcurve.wr1()](../../d3/d07/classconfig__control__design_1_1degenerate__pcurve.html#aae1772a95d3ed412ea932efd74ac2697),
[ifc2x3.ifcproduct.wr1()](../../d1/d19/classifc2x3_1_1ifcproduct.html#a1ae2bc8df067f80a59c11ffa956ba588),
[automotive_design.pcurve.wr2()](../../d4/d4b/classautomotive__design_1_1pcurve.html#a6c8a7a5f4d71cc2803cfbb42ae9b04c1),
[automotive_design.degenerate_pcurve.wr2()](../../de/d21/classautomotive__design_1_1degenerate__pcurve.html#a8e7be64a5c78f0540518110da63a3fd9),
[config_control_design.pcurve.wr2()](../../d8/d67/classconfig__control__design_1_1pcurve.html#a2748ae4c83d716e0e15781382f5fd9d7),
and
[config_control_design.degenerate_pcurve.wr2()](../../d3/d07/classconfig__control__design_1_1degenerate__pcurve.html#ac95757f1b795f22cd0ba44a1ffbb0474).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

