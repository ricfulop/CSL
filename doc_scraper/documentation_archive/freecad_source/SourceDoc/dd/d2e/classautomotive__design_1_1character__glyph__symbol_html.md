---
url: https://freecad.github.io/SourceDoc/dd/d2e/classautomotive__design_1_1character__glyph__symbol.html
scraped_at: 2025-09-08T15:01:40.180610
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [character_glyph_symbol](../../dd/d2e/classautomotive__design_1_1character__glyph__symbol.html)

[List of all members](../../d7/d8b/classautomotive__design_1_1character__glyph__symbol-members.html) | Public Member Functions | Public Attributes

automotive_design.character_glyph_symbol Class Reference

##  Public Member Functions  
  
---  
def | [baseline_ratio](../../dd/d2e/classautomotive__design_1_1character__glyph__symbol.html#a9d9e310ba3bb8db586ee288ea2165380) ()  
def | [box_height](../../dd/d2e/classautomotive__design_1_1character__glyph__symbol.html#afc897ef3f1eaa10efc7fbc6ab345e61f) ()  
def | [character_box](../../dd/d2e/classautomotive__design_1_1character__glyph__symbol.html#aa8f53b461741c7587e7736a2b534e947) ()  
def | [wr1](../../dd/d2e/classautomotive__design_1_1character__glyph__symbol.html#adb5dd89c573e888f866702e019470a97) (self)  
def | [wr2](../../dd/d2e/classautomotive__design_1_1character__glyph__symbol.html#aae3260a0cd7acc93ef9d2fdbd525d4a7) (self)  
def | [wr3](../../dd/d2e/classautomotive__design_1_1character__glyph__symbol.html#af3449a9200eff0ddda05829f17ad9839) (self)  
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
[baseline_ratio](../../dd/d2e/classautomotive__design_1_1character__glyph__symbol.html#a428b2a90d98c8b83601c74870b23ec15)  
|
[character_box](../../dd/d2e/classautomotive__design_1_1character__glyph__symbol.html#ae6e9c4aecbe7f0aab071778c291fd626)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.representation](../../d8/de0/classautomotive__design_1_1representation.html)  
|
[context_of_items](../../d8/de0/classautomotive__design_1_1representation.html#aaf5fe9839e199ab5390651177efcc497)  
|
[items](../../d8/de0/classautomotive__design_1_1representation.html#aa8058fe959724be16897e4409e870128)  
|
[name](../../d8/de0/classautomotive__design_1_1representation.html#add191f3372f9224b28aa809871533b65)  
  
## Detailed Description

    
    
    Entity character_glyph_symbol definition.
    
        :param character_box
        :type character_box:planar_extent
    
        :param baseline_ratio
        :type baseline_ratio:ratio_measure
    
        :param box_height
        :type box_height:length_measure

## Member Function Documentation

## ◆ baseline_ratio()

def automotive_design.character_glyph_symbol.baseline_ratio  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.character_glyph_symbol._baseline_ratio,
and automotive_design.character_glyph_symbol._baseline_ratio.

Referenced by
[automotive_design.character_glyph_symbol.wr1()](../../dd/d2e/classautomotive__design_1_1character__glyph__symbol.html#adb5dd89c573e888f866702e019470a97).

## ◆ box_height()

def automotive_design.character_glyph_symbol.box_height  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.character_glyph_symbol.character_box,
[automotive_design.character_glyph_symbol.character_box](../../dd/d2e/classautomotive__design_1_1character__glyph__symbol.html#ae6e9c4aecbe7f0aab071778c291fd626),
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.planar_extent.size_in_y,
and
[automotive_design.planar_extent.size_in_y](../../d0/df3/classautomotive__design_1_1planar__extent.html#a9f83ecf7580afa26873ec5a8fa0dec69).

## ◆ character_box()

def automotive_design.character_glyph_symbol.character_box  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.character_glyph_symbol._character_box,
and automotive_design.character_glyph_symbol._character_box.

Referenced by
[automotive_design.character_glyph_symbol.box_height()](../../dd/d2e/classautomotive__design_1_1character__glyph__symbol.html#afc897ef3f1eaa10efc7fbc6ab345e61f).

## ◆ wr1()

def automotive_design.character_glyph_symbol.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[automotive_design.representation](../../d8/de0/classautomotive__design_1_1representation.html#a167ca694a87f2233508375472af08fb1).

References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.character_glyph_symbol.baseline_ratio,
and
[automotive_design.character_glyph_symbol.baseline_ratio](../../dd/d2e/classautomotive__design_1_1character__glyph__symbol.html#a428b2a90d98c8b83601c74870b23ec15).

## ◆ wr2()

def automotive_design.character_glyph_symbol.wr2  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[automotive_design.representation](../../d8/de0/classautomotive__design_1_1representation.html#ab3c63c6621183d774bb49cd3605f4358).

References
[automotive_design.item_in_context()](../../d4/ddf/namespaceautomotive__design.html#a0c9efe9adbd645c876466ea788d299de),
App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

## ◆ wr3()

def automotive_design.character_glyph_symbol.wr3  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

## Member Data Documentation

## ◆ baseline_ratio

automotive_design.character_glyph_symbol.baseline_ratio  
---  
  
Referenced by
[automotive_design.character_glyph_symbol.wr1()](../../dd/d2e/classautomotive__design_1_1character__glyph__symbol.html#adb5dd89c573e888f866702e019470a97).

## ◆ character_box

automotive_design.character_glyph_symbol.character_box  
---  
  
Referenced by
[automotive_design.character_glyph_symbol.box_height()](../../dd/d2e/classautomotive__design_1_1character__glyph__symbol.html#afc897ef3f1eaa10efc7fbc6ab345e61f).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

