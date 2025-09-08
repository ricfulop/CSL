---
url: https://freecad.github.io/SourceDoc/d9/da1/classautomotive__design_1_1founded__kinematic__path.html
scraped_at: 2025-09-08T15:05:47.196971
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [founded_kinematic_path](../../d9/da1/classautomotive__design_1_1founded__kinematic__path.html)

[List of all members](../../dd/de3/classautomotive__design_1_1founded__kinematic__path-members.html) | Public Member Functions | Public Attributes

automotive_design.founded_kinematic_path Class Reference

##  Public Member Functions  
  
---  
def | [founding](../../d9/da1/classautomotive__design_1_1founded__kinematic__path.html#a810aa4e3d26fb71b4a93eb544af1e7ce) ()  
def | [paths](../../d9/da1/classautomotive__design_1_1founded__kinematic__path.html#a728a0e1979da657da771af10e789c66f) ()  
def | [representation_context_of_items](../../d9/da1/classautomotive__design_1_1founded__kinematic__path.html#adc445c9841b2ed980075e8cbe5b96ac5) ()  
def | [representation_items](../../d9/da1/classautomotive__design_1_1founded__kinematic__path.html#a1ebbb6710820fce907bf617841ef0755) ()  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.representation](../../d8/de0/classautomotive__design_1_1representation.html)  
def | [context_of_items](../../d8/de0/classautomotive__design_1_1representation.html#a84aa53a72cb77281167d77185bedab5e) ()  
def | [description](../../d8/de0/classautomotive__design_1_1representation.html#a1d35c39d45f16f922cf4360da4ec3778) ()  
def | [id](../../d8/de0/classautomotive__design_1_1representation.html#a85343890335f87c91cff60e7988263d8) ()  
def | [items](../../d8/de0/classautomotive__design_1_1representation.html#a84b16fedad2273190b6dd316673d9752) ()  
def | [name](../../d8/de0/classautomotive__design_1_1representation.html#af640f954805b1a2b3d1a4a4ee9c55d24) ()  
def | [wr1](../../d8/de0/classautomotive__design_1_1representation.html#a167ca694a87f2233508375472af08fb1) (self)  
def | [wr2](../../d8/de0/classautomotive__design_1_1representation.html#ab3c63c6621183d774bb49cd3605f4358) (self)  
  
##  Public Attributes  
  
---  
|
[representation_context_of_items](../../d9/da1/classautomotive__design_1_1founded__kinematic__path.html#ae743cdf0cd415c97493673fa904cd27c)  
|
[representation_items](../../d9/da1/classautomotive__design_1_1founded__kinematic__path.html#ae1e9eaf92d1dda5d3121e8d3cf7fa201)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.representation](../../d8/de0/classautomotive__design_1_1representation.html)  
|
[context_of_items](../../d8/de0/classautomotive__design_1_1representation.html#aaf5fe9839e199ab5390651177efcc497)  
|
[items](../../d8/de0/classautomotive__design_1_1representation.html#aa8058fe959724be16897e4409e870128)  
|
[name](../../d8/de0/classautomotive__design_1_1representation.html#add191f3372f9224b28aa809871533b65)  
  
## Detailed Description

    
    
    Entity founded_kinematic_path definition.
    
        :param representation_items
        :type representation_items:SET(1,None,'kinematic_path', scope = schema_scope)
    
        :param representation_context_of_items
        :type representation_context_of_items:geometric_representation_context
    
        :param paths
        :type paths:SET(1,None,'kinematic_path', scope = schema_scope)
    
        :param founding
        :type founding:geometric_representation_context

## Member Function Documentation

## ◆ founding()

def automotive_design.founded_kinematic_path.founding  | ( | | ) |   
---|---|---|---|---  
  
References App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

## ◆ paths()

def automotive_design.founded_kinematic_path.paths  | ( | | ) |   
---|---|---|---|---  
  
References App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

## ◆ representation_context_of_items()

def automotive_design.founded_kinematic_path.representation_context_of_items  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.presentation_representation._representation_context_of_items,
automotive_design.founded_kinematic_path._representation_context_of_items,
automotive_design.presentation_representation._representation_context_of_items,
automotive_design.kinematic_link_representation._representation_context_of_items,
and
automotive_design.kinematic_frame_background_representation._representation_context_of_items.

## ◆ representation_items()

def automotive_design.founded_kinematic_path.representation_items  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.mechanical_design_geometric_presentation_representation._representation_items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.draughting_model._representation_items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.mechanical_design_geometric_presentation_area._representation_items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.text_string_representation._representation_items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.procedural_representation._representation_items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.procedural_shape_representation._representation_items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.structured_text_representation._representation_items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.picture_representation._representation_items,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.mechanical_design_presentation_representation_with_draughting._representation_items,
automotive_design.founded_kinematic_path._representation_items,
automotive_design.text_string_representation._representation_items, and
automotive_design.kinematic_frame_background_representation._representation_items.

## Member Data Documentation

## ◆ representation_context_of_items

automotive_design.founded_kinematic_path.representation_context_of_items  
---  
  
## ◆ representation_items

automotive_design.founded_kinematic_path.representation_items  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

