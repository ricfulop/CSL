---
url: https://freecad.github.io/SourceDoc/d7/d22/classautomotive__design_1_1context__dependent__over__riding__styled__item.html
scraped_at: 2025-09-08T15:02:42.430631
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [context_dependent_over_riding_styled_item](../../d7/d22/classautomotive__design_1_1context__dependent__over__riding__styled__item.html)

[List of all members](../../dc/da5/classautomotive__design_1_1context__dependent__over__riding__styled__item-members.html) | Public Member Functions | Public Attributes

automotive_design.context_dependent_over_riding_styled_item Class Reference

##  Public Member Functions  
  
---  
def | [style_context](../../d7/d22/classautomotive__design_1_1context__dependent__over__riding__styled__item.html#a0d3a0c9ff3ab21fb9126d6b8e4783581) ()  
def | [wr1](../../d7/d22/classautomotive__design_1_1context__dependent__over__riding__styled__item.html#a35512624313535625bdfa25941399755) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.over_riding_styled_item](../../dc/d78/classautomotive__design_1_1over__riding__styled__item.html)  
def | [over_ridden_style](../../dc/d78/classautomotive__design_1_1over__riding__styled__item.html#a3ae496f68e45a1fe29a4f91db8fcd756) ()  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.styled_item](../../dd/d39/classautomotive__design_1_1styled__item.html)  
def | [item](../../dd/d39/classautomotive__design_1_1styled__item.html#a1ca47f0662afee60e3d092187972d692) ()  
def | [styles](../../dd/d39/classautomotive__design_1_1styled__item.html#adddc1c1e338ae95a29f5e9525d5d24f7) ()  
def | [wr1](../../dd/d39/classautomotive__design_1_1styled__item.html#a150262e278f8248839d7cddb3ade3d26) (self)  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
def | [name](../../d3/d20/classautomotive__design_1_1representation__item.html#a33b5812d92aa0d107b4fd4274c17b9d9) ()  
def | [wr1](../../d3/d20/classautomotive__design_1_1representation__item.html#af350c19fc5e5763d4991494a99d979ed) (self)  
  
##  Public Attributes  
  
---  
|
[style_context](../../d7/d22/classautomotive__design_1_1context__dependent__over__riding__styled__item.html#ab648d438ca062f4affd17e05d3d56a6c)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.over_riding_styled_item](../../dc/d78/classautomotive__design_1_1over__riding__styled__item.html)  
|
[over_ridden_style](../../dc/d78/classautomotive__design_1_1over__riding__styled__item.html#a142292dfab9b577c4ac77733f8d05a97)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.styled_item](../../dd/d39/classautomotive__design_1_1styled__item.html)  
|
[item](../../dd/d39/classautomotive__design_1_1styled__item.html#aad87aa33fdbad670cc9dfcfdbe866d79)  
|
[styles](../../dd/d39/classautomotive__design_1_1styled__item.html#a715f59d8d13c21ae1a5c704b0dbdbebb)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
|
[name](../../d3/d20/classautomotive__design_1_1representation__item.html#a3d48fe912053adaf5f187b606fa81c87)  
  
## Detailed Description

    
    
    Entity context_dependent_over_riding_styled_item definition.
    
        :param style_context
        :type style_context:LIST(1,None,'style_context_select', scope = schema_scope)

## Member Function Documentation

## ◆ style_context()

def automotive_design.context_dependent_over_riding_styled_item.style_context  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.context_dependent_over_riding_styled_item._style_context,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.presentation_style_by_context._style_context,
automotive_design.context_dependent_over_riding_styled_item._style_context,
and automotive_design.presentation_style_by_context._style_context.

Referenced by
[automotive_design.context_dependent_over_riding_styled_item.wr1()](../../d7/d22/classautomotive__design_1_1context__dependent__over__riding__styled__item.html#a35512624313535625bdfa25941399755).

## ◆ wr1()

def automotive_design.context_dependent_over_riding_styled_item.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[automotive_design.styled_item](../../dd/d39/classautomotive__design_1_1styled__item.html#a150262e278f8248839d7cddb3ade3d26).

Reimplemented in
[automotive_design.hidden_element_over_riding_styled_item](../../da/d95/classautomotive__design_1_1hidden__element__over__riding__styled__item.html#ad2d609783c0ef43800f6255ed6844ddc).

References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.context_dependent_over_riding_styled_item.style_context,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.presentation_style_by_context.style_context,
[automotive_design.context_dependent_over_riding_styled_item.style_context](../../d7/d22/classautomotive__design_1_1context__dependent__over__riding__styled__item.html#ab648d438ca062f4affd17e05d3d56a6c),
and
[automotive_design.presentation_style_by_context.style_context](../../d8/d43/classautomotive__design_1_1presentation__style__by__context.html#abf4eac364a04932b914189fc9b4fd058).

## Member Data Documentation

## ◆ style_context

automotive_design.context_dependent_over_riding_styled_item.style_context  
---  
  
Referenced by
[automotive_design.context_dependent_over_riding_styled_item.wr1()](../../d7/d22/classautomotive__design_1_1context__dependent__over__riding__styled__item.html#a35512624313535625bdfa25941399755).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

