---
url: https://freecad.github.io/SourceDoc/df/d15/classautomotive__design_1_1text__literal__with__extent.html
scraped_at: 2025-09-08T15:14:19.309148
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [text_literal_with_extent](../../df/d15/classautomotive__design_1_1text__literal__with__extent.html)

[List of all members](../../d4/d65/classautomotive__design_1_1text__literal__with__extent-members.html) | Public Member Functions | Public Attributes

automotive_design.text_literal_with_extent Class Reference

##  Public Member Functions  
  
---  
def | [extent](../../df/d15/classautomotive__design_1_1text__literal__with__extent.html#a78beaae4352fc3c0f717984456b6b195) ()  
![-](../../closed.png) Public Member Functions inherited from
[automotive_design.text_literal](../../de/dfb/classautomotive__design_1_1text__literal.html)  
def | [alignment](../../de/dfb/classautomotive__design_1_1text__literal.html#aa2675337b9eda7b7ea840740ec38a47a) ()  
def | [font](../../de/dfb/classautomotive__design_1_1text__literal.html#aed39353fa2e4398ecee69c67492a3170) ()  
def | [literal](../../de/dfb/classautomotive__design_1_1text__literal.html#a4db19718e94198dfea502942e044d8d5) ()  
def | [path](../../de/dfb/classautomotive__design_1_1text__literal.html#acd2a033bf28ace72cf2b85f0326e79a1) ()  
def | [placement](../../de/dfb/classautomotive__design_1_1text__literal.html#a725817bcffdd6bf52cd03169bad00ba3) ()  
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
[extent](../../df/d15/classautomotive__design_1_1text__literal__with__extent.html#a1aad6dd8bd661049164b73c691eb2c1d)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.text_literal](../../de/dfb/classautomotive__design_1_1text__literal.html)  
|
[alignment](../../de/dfb/classautomotive__design_1_1text__literal.html#abc7286e3e9408a2f6fed3cc675ea95a8)  
|
[font](../../de/dfb/classautomotive__design_1_1text__literal.html#a29890fc906cb6fa89eea7e72cacb9299)  
|
[literal](../../de/dfb/classautomotive__design_1_1text__literal.html#a2c456be8702d39bb81baea7a57ba89c9)  
|
[path](../../de/dfb/classautomotive__design_1_1text__literal.html#a96a33a6b6c107db056cf729b53050c8a)  
|
[placement](../../de/dfb/classautomotive__design_1_1text__literal.html#a7ba2862a2dccefd6b2efc0728245f098)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
|
[name](../../d3/d20/classautomotive__design_1_1representation__item.html#a3d48fe912053adaf5f187b606fa81c87)  
  
## Detailed Description

    
    
    Entity text_literal_with_extent definition.
    
        :param extent
        :type extent:planar_extent

## Member Function Documentation

## ◆ extent()

def automotive_design.text_literal_with_extent.extent  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.composite_text_with_extent._extent,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.text_literal_with_extent._extent,
automotive_design.composite_text_with_extent._extent,
automotive_design.text_literal_with_extent._extent,
ifc2x3.ifctextliteralwithextent._extent, and
ifc4.ifctextliteralwithextent._extent.

Referenced by
[ifc2x3.ifctextliteralwithextent.wr31()](../../d2/d43/classifc2x3_1_1ifctextliteralwithextent.html#a9dfaf071245e0d0591b4ef4664d972cb),
and
[ifc4.ifctextliteralwithextent.wr31()](../../d1/de3/classifc4_1_1ifctextliteralwithextent.html#ac94fea7f9b37e2a5bb40b5e322e11de5).

## Member Data Documentation

## ◆ extent

automotive_design.text_literal_with_extent.extent  
---  
  
Referenced by
[ifc2x3.ifctextliteralwithextent.wr31()](../../d2/d43/classifc2x3_1_1ifctextliteralwithextent.html#a9dfaf071245e0d0591b4ef4664d972cb),
and
[ifc4.ifctextliteralwithextent.wr31()](../../d1/de3/classifc4_1_1ifctextliteralwithextent.html#ac94fea7f9b37e2a5bb40b5e322e11de5).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

