---
url: https://freecad.github.io/SourceDoc/de/df2/classautomotive__design_1_1point__on__surface__pair.html
scraped_at: 2025-09-08T15:09:52.174424
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [point_on_surface_pair](../../de/df2/classautomotive__design_1_1point__on__surface__pair.html)

[List of all members](../../d2/d17/classautomotive__design_1_1point__on__surface__pair-members.html) | Public Member Functions | Public Attributes

automotive_design.point_on_surface_pair Class Reference

##  Public Member Functions  
  
---  
def | [pair_surface](../../de/df2/classautomotive__design_1_1point__on__surface__pair.html#a366500c813e215e02f8f4e2619a92e1a) ()  
def | [wr1](../../de/df2/classautomotive__design_1_1point__on__surface__pair.html#a7d512562d6ed849a3c08ebfb80437cab) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.kinematic_pair](../../d4/d4f/classautomotive__design_1_1kinematic__pair.html)  
def | [joint](../../d4/d4f/classautomotive__design_1_1kinematic__pair.html#a3cc1a3fa91c668bc412ae98a6bb71801) ()  
def | [pair_placement_in_first_link_context](../../d4/d4f/classautomotive__design_1_1kinematic__pair.html#a4c2d01c20c5af49ab32473d657a4c064) ()  
def | [pair_placement_in_second_link_context](../../d4/d4f/classautomotive__design_1_1kinematic__pair.html#a95c998e19e5ff9bcc07073444b9a551a) ()  
def | [wr1](../../d4/d4f/classautomotive__design_1_1kinematic__pair.html#a5bf15e517acfe323d781527c74eb5100) (self)  
def | [wr2](../../d4/d4f/classautomotive__design_1_1kinematic__pair.html#a3974063d988bfa776fba5cd5dac1c369) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.item_defined_transformation](../../d4/d91/classautomotive__design_1_1item__defined__transformation.html)  
def | [description](../../d4/d91/classautomotive__design_1_1item__defined__transformation.html#aea7020e577c8aaa199bb53f3c4f76a19) ()  
def | [name](../../d4/d91/classautomotive__design_1_1item__defined__transformation.html#a677249d4b240467fd9f1f5cc5279b24d) ()  
def | [transform_item_1](../../d4/d91/classautomotive__design_1_1item__defined__transformation.html#aeb7769f338ddfe3f332b6f71eeff0231) ()  
def | [transform_item_2](../../d4/d91/classautomotive__design_1_1item__defined__transformation.html#a9cfdcfa5ee62b8db6be37ae3c542158d) ()  
  
##  Public Attributes  
  
---  
|
[pair_surface](../../de/df2/classautomotive__design_1_1point__on__surface__pair.html#a6f7148b8c5e1082476bc61cb4d2417ed)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.kinematic_pair](../../d4/d4f/classautomotive__design_1_1kinematic__pair.html)  
|
[joint](../../d4/d4f/classautomotive__design_1_1kinematic__pair.html#a129569b8355d19cee7527672b69b6258)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.item_defined_transformation](../../d4/d91/classautomotive__design_1_1item__defined__transformation.html)  
|
[description](../../d4/d91/classautomotive__design_1_1item__defined__transformation.html#a9639e4a7f29564c744654086b0613457)  
|
[name](../../d4/d91/classautomotive__design_1_1item__defined__transformation.html#a71cd4ea422a14c796ae2be07eef15da8)  
|
[transform_item_1](../../d4/d91/classautomotive__design_1_1item__defined__transformation.html#a35a6126264cb2506a21004dbfc053ac0)  
|
[transform_item_2](../../d4/d91/classautomotive__design_1_1item__defined__transformation.html#ae1905883f0ed10110e83ec393fbda4a4)  
  
## Detailed Description

    
    
    Entity point_on_surface_pair definition.
    
        :param pair_surface
        :type pair_surface:surface

## Member Function Documentation

## ◆ pair_surface()

def automotive_design.point_on_surface_pair.pair_surface  | ( | | ) |   
---|---|---|---|---  
  
References automotive_design.point_on_surface_pair._pair_surface.

Referenced by
[automotive_design.point_on_surface_pair.wr1()](../../de/df2/classautomotive__design_1_1point__on__surface__pair.html#a7d512562d6ed849a3c08ebfb80437cab).

## ◆ wr1()

def automotive_design.point_on_surface_pair.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[automotive_design.kinematic_pair](../../d4/d4f/classautomotive__design_1_1kinematic__pair.html#a5bf15e517acfe323d781527c74eb5100).

References
[automotive_design.frame_associated_to_background()](../../d4/ddf/namespaceautomotive__design.html#ad23b750ebd23bb0492d76afd3d5b1f43),
[automotive_design.point_on_surface_pair_value.pair_surface](../../dd/d39/classautomotive__design_1_1point__on__surface__pair__value.html#af87d48703d808468a39548ba8ad53886),
[automotive_design.point_on_surface_pair.pair_surface](../../de/df2/classautomotive__design_1_1point__on__surface__pair.html#a6f7148b8c5e1082476bc61cb4d2417ed),
[automotive_design.point_on_surface_pair_range.pair_surface](../../d6/d75/classautomotive__design_1_1point__on__surface__pair__range.html#a28794b851755b86fc4d55336cff06cfd),
App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

## Member Data Documentation

## ◆ pair_surface

automotive_design.point_on_surface_pair.pair_surface  
---  
  
Referenced by
[automotive_design.point_on_surface_pair.wr1()](../../de/df2/classautomotive__design_1_1point__on__surface__pair.html#a7d512562d6ed849a3c08ebfb80437cab).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

