---
url: https://freecad.github.io/SourceDoc/d5/d94/classautomotive__design_1_1gear__pair.html
scraped_at: 2025-09-08T15:05:50.173559
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [gear_pair](../../d5/d94/classautomotive__design_1_1gear__pair.html)

[List of all members](../../de/d4e/classautomotive__design_1_1gear__pair-members.html) | Public Member Functions | Public Attributes

automotive_design.gear_pair Class Reference

##  Public Member Functions  
  
---  
def | [bevel](../../d5/d94/classautomotive__design_1_1gear__pair.html#aec7bcb168c4995bd17e3f7caaedf724a) ()  
def | [gear_ratio](../../d5/d94/classautomotive__design_1_1gear__pair.html#ae9480b851a35c5235028bbcc79fd144a) ()  
def | [helical_angle](../../d5/d94/classautomotive__design_1_1gear__pair.html#a7f6d7db7a6573b5bf3a6314c8918c9c4) ()  
def | [radius_first_link](../../d5/d94/classautomotive__design_1_1gear__pair.html#a52b036c2166cbe0504504c06e35a65ab) ()  
def | [radius_second_link](../../d5/d94/classautomotive__design_1_1gear__pair.html#a22f39f8412d2c112fa8565f51801d1cd) ()  
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
[bevel](../../d5/d94/classautomotive__design_1_1gear__pair.html#a1384c4a33ed799c28265bd8269f2cd1f)  
|
[gear_ratio](../../d5/d94/classautomotive__design_1_1gear__pair.html#afffc94add7605c20246727496f924861)  
|
[helical_angle](../../d5/d94/classautomotive__design_1_1gear__pair.html#a5086a1cae731083bcb130e4cd5aafe6c)  
|
[radius_first_link](../../d5/d94/classautomotive__design_1_1gear__pair.html#a70543fe7bff03cdfe7eb526164ce5d3c)  
|
[radius_second_link](../../d5/d94/classautomotive__design_1_1gear__pair.html#a692ae8fcc4447825977c0e411ec9ec20)  
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

    
    
    Entity gear_pair definition.
    
        :param radius_first_link
        :type radius_first_link:length_measure
    
        :param radius_second_link
        :type radius_second_link:length_measure
    
        :param bevel
        :type bevel:plane_angle_measure
    
        :param helical_angle
        :type helical_angle:plane_angle_measure
    
        :param gear_ratio
        :type gear_ratio:REAL

## Member Function Documentation

## ◆ bevel()

def automotive_design.gear_pair.bevel  | ( | | ) |   
---|---|---|---|---  
  
References automotive_design.gear_pair._bevel.

## ◆ gear_ratio()

def automotive_design.gear_pair.gear_ratio  | ( | | ) |   
---|---|---|---|---  
  
References automotive_design.gear_pair._gear_ratio.

## ◆ helical_angle()

def automotive_design.gear_pair.helical_angle  | ( | | ) |   
---|---|---|---|---  
  
References automotive_design.gear_pair._helical_angle.

## ◆ radius_first_link()

def automotive_design.gear_pair.radius_first_link  | ( | | ) |   
---|---|---|---|---  
  
References automotive_design.gear_pair._radius_first_link.

## ◆ radius_second_link()

def automotive_design.gear_pair.radius_second_link  | ( | | ) |   
---|---|---|---|---  
  
References automotive_design.gear_pair._radius_second_link.

## Member Data Documentation

## ◆ bevel

automotive_design.gear_pair.bevel  
---  
  
## ◆ gear_ratio

automotive_design.gear_pair.gear_ratio  
---  
  
## ◆ helical_angle

automotive_design.gear_pair.helical_angle  
---  
  
## ◆ radius_first_link

automotive_design.gear_pair.radius_first_link  
---  
  
## ◆ radius_second_link

automotive_design.gear_pair.radius_second_link  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

