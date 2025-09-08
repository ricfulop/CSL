---
url: https://freecad.github.io/SourceDoc/d1/d77/classautomotive__design_1_1symbol__target.html
scraped_at: 2025-09-08T15:14:03.245229
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [symbol_target](../../d1/d77/classautomotive__design_1_1symbol__target.html)

[List of all members](../../db/d28/classautomotive__design_1_1symbol__target-members.html) | Public Member Functions | Public Attributes

automotive_design.symbol_target Class Reference

##  Public Member Functions  
  
---  
def | [placement](../../d1/d77/classautomotive__design_1_1symbol__target.html#aee75b74f24e75120beb2aa0e5f6732c4) ()  
def | [x_scale](../../d1/d77/classautomotive__design_1_1symbol__target.html#a0f552a94259358a990019284dd01da1b) ()  
def | [y_scale](../../d1/d77/classautomotive__design_1_1symbol__target.html#a5cb227098e347bebbdbfc1926c1d211e) ()  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.geometric_representation_item](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html)  
def | [dim](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html#aef245618450610e88788dcaea46ad742) ()  
def | [wr1](../../de/d5e/classautomotive__design_1_1geometric__representation__item.html#a9677d2be5fc5c7c8ccb6819380198bbc) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
def | [name](../../d3/d20/classautomotive__design_1_1representation__item.html#a33b5812d92aa0d107b4fd4274c17b9d9) ()  
def | [wr1](../../d3/d20/classautomotive__design_1_1representation__item.html#af350c19fc5e5763d4991494a99d979ed) (self)  
  
##  Public Attributes  
  
---  
|
[placement](../../d1/d77/classautomotive__design_1_1symbol__target.html#a047612adc4981941f5e8a3447e142e02)  
|
[x_scale](../../d1/d77/classautomotive__design_1_1symbol__target.html#a054dac198021785db75351743df11c4a)  
|
[y_scale](../../d1/d77/classautomotive__design_1_1symbol__target.html#a528c7f7d38ee74443f49f79c6ff7acb1)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
|
[name](../../d3/d20/classautomotive__design_1_1representation__item.html#a3d48fe912053adaf5f187b606fa81c87)  
  
## Detailed Description

    
    
    Entity symbol_target definition.
    
        :param placement
        :type placement:axis2_placement
    
        :param x_scale
        :type x_scale:positive_ratio_measure
    
        :param y_scale
        :type y_scale:positive_ratio_measure

## Member Function Documentation

## ◆ placement()

def automotive_design.symbol_target.placement  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.text_literal._placement,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.planar_box._placement,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.symbol_target._placement,
automotive_design.text_literal._placement,
automotive_design.planar_box._placement,
automotive_design.defined_character_glyph._placement,
automotive_design.symbol_target._placement, ifc2x3.ifcplanarbox._placement,
ifc2x3.ifctextliteral._placement, ifc4.ifcplanarbox._placement,
ifc4.ifctextliteral._placement, and
[automotive_design.axis2_placement](../../d4/ddf/namespaceautomotive__design.html#a0301850a614764907b76f5483678a929).

Referenced by
[draftguitools.gui_trimex.Trimex.trimObject()](../../da/df7/classdraftguitools_1_1gui__trimex_1_1Trimex.html#a5e72e325ef0a53c3fde6c75c2eb56ba6).

## ◆ x_scale()

def automotive_design.symbol_target.x_scale  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.symbol_target._x_scale,
and automotive_design.symbol_target._x_scale.

## ◆ y_scale()

def automotive_design.symbol_target.y_scale  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.symbol_target._y_scale,
and automotive_design.symbol_target._y_scale.

## Member Data Documentation

## ◆ placement

automotive_design.symbol_target.placement  
---  
  
Referenced by
[draftguitools.gui_trimex.Trimex.trimObject()](../../da/df7/classdraftguitools_1_1gui__trimex_1_1Trimex.html#a5e72e325ef0a53c3fde6c75c2eb56ba6).

## ◆ x_scale

automotive_design.symbol_target.x_scale  
---  
  
## ◆ y_scale

automotive_design.symbol_target.y_scale  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

