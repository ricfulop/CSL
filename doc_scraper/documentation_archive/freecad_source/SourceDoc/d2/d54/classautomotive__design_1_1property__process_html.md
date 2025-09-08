---
url: https://freecad.github.io/SourceDoc/d2/d54/classautomotive__design_1_1property__process.html
scraped_at: 2025-09-08T15:11:17.544440
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [property_process](../../d2/d54/classautomotive__design_1_1property__process.html)

[List of all members](../../d5/ddc/classautomotive__design_1_1property__process-members.html) | Public Member Functions | Public Attributes

automotive_design.property_process Class Reference

##  Public Member Functions  
  
---  
def | [identification](../../d2/d54/classautomotive__design_1_1property__process.html#aea5ee4187db0bd27a6351a08d0849926) ()  
def | [properties](../../d2/d54/classautomotive__design_1_1property__process.html#a8347efb908cc07c9a8bc61313a4aa318) ()  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.action](../../dd/db7/classautomotive__design_1_1action.html)  
def | [chosen_method](../../dd/db7/classautomotive__design_1_1action.html#a0bb4218ffaae2f91ad8c5eb3aaebb861) ()  
def | [description](../../dd/db7/classautomotive__design_1_1action.html#a053f3af55213aa3b721567d2a49c2148) ()  
def | [id](../../dd/db7/classautomotive__design_1_1action.html#a289e01eb20d53e6824c40daad04dfc4b) ()  
def | [name](../../dd/db7/classautomotive__design_1_1action.html#a2ec9ee5bbd2e3eceb2d51d8ac569fefb) ()  
def | [wr1](../../dd/db7/classautomotive__design_1_1action.html#a394a5335bf93418126ac4f7fec339dcd) (self)  
  
##  Public Attributes  
  
---  
|
[identification](../../d2/d54/classautomotive__design_1_1property__process.html#af7dbe7c221218666ca2bc845b5b60e97)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.action](../../dd/db7/classautomotive__design_1_1action.html)  
|
[chosen_method](../../dd/db7/classautomotive__design_1_1action.html#a6aa732474ae1ebb9e3175228f8113d68)  
|
[description](../../dd/db7/classautomotive__design_1_1action.html#a0f88db2350cbe07e6455946f9a3b02de)  
|
[name](../../dd/db7/classautomotive__design_1_1action.html#a6f5d021b7324a85dc2714abbdb31ca63)  
  
## Detailed Description

    
    
    Entity property_process definition.
    
        :param identification
        :type identification:identifier
    
        :param properties
        :type properties:SET(1,None,'process_property_association', scope = schema_scope)

## Member Function Documentation

## ◆ identification()

def automotive_design.property_process.identification  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.datum._identification,
automotive_design.property_process._identification,
automotive_design.product_definition_process._identification,
automotive_design.datum._identification, ifc4.ifctyperesource._identification,
ifc4.ifccontrol._identification, ifc4.ifcexternalreference._identification,
ifc4.ifctypeprocess._identification,
ifc4.ifcdocumentinformation._identification,
ifc4.ifcorganization._identification, ifc4.ifcprocess._identification,
ifc4.ifcresource._identification, ifc4.ifcperson._identification, and
ifc4.ifcasset._identification.

Referenced by
[ifc4.ifcperson.identifiableperson()](../../db/d15/classifc4_1_1ifcperson.html#a8b4262ca3c8e9347557fb1d1c776b7a0),
and
[ifc4.ifcexternalreference.wr1()](../../d5/dd9/classifc4_1_1ifcexternalreference.html#a0e6ba5265c69b44700e8d9b179e9f240).

## ◆ properties()

def automotive_design.property_process.properties  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_style_rendering_with_properties._properties,
automotive_design.surface_style_rendering_with_properties._properties, and
ifc4.ifcextendedproperties._properties.

Referenced by
[PathScripts.PathProperty.OpPrototype.addProperty()](../../da/db1/classPathScripts_1_1PathProperty_1_1OpPrototype.html#ab1ea9a80158b9467baca886a5a3f15fd),
[PathScripts.PathSetupSheetOpPrototype.OpPrototype.addProperty()](../../db/df0/classPathScripts_1_1PathSetupSheetOpPrototype_1_1OpPrototype.html#a82c2c615868fbdb7cfa1ed3612fd43f2),
[OfflineRenderingUtils.FreeCADGuiHandler.endElement()](../../d6/dc4/classOfflineRenderingUtils_1_1FreeCADGuiHandler.html#a5af207d468e4861e0996effc1f9bc188),
[PathScripts.PathProperty.OpPrototype.getProperty()](../../da/db1/classPathScripts_1_1PathProperty_1_1OpPrototype.html#a83afc43ef8f685a1504acbd44f614ad9),
[PathScripts.PathSetupSheetOpPrototype.OpPrototype.getProperty()](../../db/df0/classPathScripts_1_1PathSetupSheetOpPrototype_1_1OpPrototype.html#ace4dbb0a390fba2b97804ec1ddf57b99),
[PathScripts.PathProperty.OpPrototype.setEditorMode()](../../da/db1/classPathScripts_1_1PathProperty_1_1OpPrototype.html#ae7eab72dba66b6278f772009aaf87c56),
[PathScripts.PathSetupSheetOpPrototype.OpPrototype.setEditorMode()](../../db/df0/classPathScripts_1_1PathSetupSheetOpPrototype_1_1OpPrototype.html#a1567f9243bc70d4420360dec7977cc09),
[PathScripts.PathProperty.OpPrototype.setupProperties()](../../da/db1/classPathScripts_1_1PathProperty_1_1OpPrototype.html#ae3fbbc1559c14cb3c6d16735c898de0d),
and
[PathScripts.PathSetupSheetOpPrototype.OpPrototype.setupProperties()](../../db/df0/classPathScripts_1_1PathSetupSheetOpPrototype_1_1OpPrototype.html#a6743d2263bf821e155b4e4bf8b1e989a).

## Member Data Documentation

## ◆ identification

automotive_design.property_process.identification  
---  
  
Referenced by
[ifc4.ifcperson.identifiableperson()](../../db/d15/classifc4_1_1ifcperson.html#a8b4262ca3c8e9347557fb1d1c776b7a0),
and
[ifc4.ifcexternalreference.wr1()](../../d5/dd9/classifc4_1_1ifcexternalreference.html#a0e6ba5265c69b44700e8d9b179e9f240).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

