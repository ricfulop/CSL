---
url: https://freecad.github.io/SourceDoc/d3/dd3/classautomotive__design_1_1screw__pair.html
scraped_at: 2025-09-08T15:12:18.792648
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [screw_pair](../../d3/dd3/classautomotive__design_1_1screw__pair.html)

[List of all members](../../d5/da3/classautomotive__design_1_1screw__pair-members.html) | Public Member Functions | Public Attributes

automotive_design.screw_pair Class Reference

##  Public Member Functions  
  
---  
def | [pitch](../../d3/dd3/classautomotive__design_1_1screw__pair.html#ad611fccd7f5687f7938967f4a61c0384) ()  
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
[pitch](../../d3/dd3/classautomotive__design_1_1screw__pair.html#ac8dcf88cd1eb99b872b4f2aaf2eb49e7)  
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

    
    
    Entity screw_pair definition.
    
        :param pitch
        :type pitch:length_measure

## Member Function Documentation

## ◆ pitch()

def automotive_design.screw_pair.pitch  | ( | | ) |   
---|---|---|---|---  
  
References automotive_design.screw_pair._pitch.

Referenced by
[threadmilling_generator._Thread.adjustX()](../../de/d4b/classthreadmilling__generator_1_1__Thread.html#a046f65bdc336489f468899152ebbc9cb),
[PathScripts.PathThreadMillingGui.TaskPanelOpPage.getFields()](../../df/d59/classPathScripts_1_1PathThreadMillingGui_1_1TaskPanelOpPage.html#a15f1fd1b14c164dd424dc7750972b656),
[threadmilling_generator._Thread.isUp()](../../de/d4b/classthreadmilling__generator_1_1__Thread.html#aab0dd2f0f9fb405ce6fc4e553f8fd864),
[threadmilling_generator._Thread.overshoots()](../../de/d4b/classthreadmilling__generator_1_1__Thread.html#a6190eb0b1cf8b8d1f7921a2eb6738bd8),
and
[PathScripts.PathThreadMillingGui.TaskPanelOpPage.setFields()](../../df/d59/classPathScripts_1_1PathThreadMillingGui_1_1TaskPanelOpPage.html#a0546b64219e91a87f17a4474bc465c52).

## Member Data Documentation

## ◆ pitch

automotive_design.screw_pair.pitch  
---  
  
Referenced by
[threadmilling_generator._Thread.adjustX()](../../de/d4b/classthreadmilling__generator_1_1__Thread.html#a046f65bdc336489f468899152ebbc9cb),
[PathScripts.PathThreadMillingGui.TaskPanelOpPage.getFields()](../../df/d59/classPathScripts_1_1PathThreadMillingGui_1_1TaskPanelOpPage.html#a15f1fd1b14c164dd424dc7750972b656),
[threadmilling_generator._Thread.isUp()](../../de/d4b/classthreadmilling__generator_1_1__Thread.html#aab0dd2f0f9fb405ce6fc4e553f8fd864),
[threadmilling_generator._Thread.overshoots()](../../de/d4b/classthreadmilling__generator_1_1__Thread.html#a6190eb0b1cf8b8d1f7921a2eb6738bd8),
and
[PathScripts.PathThreadMillingGui.TaskPanelOpPage.setFields()](../../df/d59/classPathScripts_1_1PathThreadMillingGui_1_1TaskPanelOpPage.html#a0546b64219e91a87f17a4474bc465c52).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

