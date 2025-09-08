---
url: https://freecad.github.io/SourceDoc/de/dfb/classautomotive__design_1_1text__literal.html
scraped_at: 2025-09-08T15:14:15.288591
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [text_literal](../../de/dfb/classautomotive__design_1_1text__literal.html)

[List of all members](../../d2/d5e/classautomotive__design_1_1text__literal-members.html) | Public Member Functions | Public Attributes

automotive_design.text_literal Class Reference

##  Public Member Functions  
  
---  
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

    
    
    Entity text_literal definition.
    
        :param literal
        :type literal:presentable_text
    
        :param placement
        :type placement:axis2_placement
    
        :param alignment
        :type alignment:text_alignment
    
        :param path
        :type path:text_path
    
        :param font
        :type font:font_select

## Member Function Documentation

## ◆ alignment()

def automotive_design.text_literal.alignment  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.annotation_text_character._alignment,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.text_literal._alignment,
automotive_design.annotation_text_character._alignment, and
automotive_design.text_literal._alignment.

## ◆ font()

def automotive_design.text_literal.font  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.text_literal._font,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.character_glyph_font_usage._font,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.text_font_in_family._font,
automotive_design.text_literal._font, and
[automotive_design.font_select](../../d4/ddf/namespaceautomotive__design.html#a8ab51516aac4cad6435dbd9f75f288d4).

Referenced by
[draftviewproviders.view_dimension.ViewProviderLinearDimension.onChanged()](../../dc/d15/classdraftviewproviders_1_1view__dimension_1_1ViewProviderLinearDimension.html#a811de5a9bc446762fba4a970fa19139e),
[draftviewproviders.view_dimension.ViewProviderAngularDimension.onChanged()](../../d5/d88/classdraftviewproviders_1_1view__dimension_1_1ViewProviderAngularDimension.html#a087daa2336d84802959135e0da541289),
[draftviewproviders.view_label.ViewProviderLabel.onChanged()](../../d1/d88/classdraftviewproviders_1_1view__label_1_1ViewProviderLabel.html#a0c2d2d99716b94c14f16529079f8d06c),
[draftviewproviders.view_text.ViewProviderText.onChanged()](../../db/dd9/classdraftviewproviders_1_1view__text_1_1ViewProviderText.html#a798abb26aface6f3a7c06d0da2e6d15f),
[draftviewproviders.view_label.ViewProviderLabel.update_frame()](../../d1/d88/classdraftviewproviders_1_1view__label_1_1ViewProviderLabel.html#a91b172318f8d77c8aaab8ac2d20ae0c0),
and
[draftviewproviders.view_label.ViewProviderLabel.update_label()](../../d1/d88/classdraftviewproviders_1_1view__label_1_1ViewProviderLabel.html#aeff559615650631a8995d5cc799dc2c2).

## ◆ literal()

def automotive_design.text_literal.literal  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.text_literal._literal,
automotive_design.text_literal._literal, ifc2x3.ifctextliteral._literal, and
ifc4.ifctextliteral._literal.

## ◆ path()

def automotive_design.text_literal.path  | ( | | ) |   
---|---|---|---|---  
  
References Gui::PreferencePack._path,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.dimensional_location_with_path._path,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.text_literal._path,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.dimensional_size_with_path._path,
automotive_design.dimensional_location_with_path._path,
automotive_design.text_literal._path,
automotive_design.dimensional_size_with_path._path,
ifc2x3.ifctextliteral._path, ifc4.ifctextliteral._path, and
zipios::FilePath._path.

Referenced by
[PathScripts.PathToolBitLibraryGui.ToolBitLibrary.librarySave()](../../dd/d3a/classPathScripts_1_1PathToolBitLibraryGui_1_1ToolBitLibrary.html#a78e1b668521bdf525ca26a7be60ac80e),
[PathScripts.PathToolBitLibraryGui.ToolBitLibrary.librarySaveAs()](../../dd/d3a/classPathScripts_1_1PathToolBitLibraryGui_1_1ToolBitLibrary.html#aacc6b835c3257775d5683ff5c4494b27),
and
[PathScripts.PathToolBitLibraryGui.ToolBitLibrary.loadData()](../../dd/d3a/classPathScripts_1_1PathToolBitLibraryGui_1_1ToolBitLibrary.html#ae2616669ba6b30e1833ff2d498cc2d6a).

## ◆ placement()

def automotive_design.text_literal.placement  | ( | | ) |   
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

## Member Data Documentation

## ◆ alignment

automotive_design.text_literal.alignment  
---  
  
## ◆ font

automotive_design.text_literal.font  
---  
  
Referenced by
[draftviewproviders.view_dimension.ViewProviderLinearDimension.onChanged()](../../dc/d15/classdraftviewproviders_1_1view__dimension_1_1ViewProviderLinearDimension.html#a811de5a9bc446762fba4a970fa19139e),
[draftviewproviders.view_dimension.ViewProviderAngularDimension.onChanged()](../../d5/d88/classdraftviewproviders_1_1view__dimension_1_1ViewProviderAngularDimension.html#a087daa2336d84802959135e0da541289),
[draftviewproviders.view_label.ViewProviderLabel.onChanged()](../../d1/d88/classdraftviewproviders_1_1view__label_1_1ViewProviderLabel.html#a0c2d2d99716b94c14f16529079f8d06c),
[draftviewproviders.view_text.ViewProviderText.onChanged()](../../db/dd9/classdraftviewproviders_1_1view__text_1_1ViewProviderText.html#a798abb26aface6f3a7c06d0da2e6d15f),
[draftviewproviders.view_label.ViewProviderLabel.update_frame()](../../d1/d88/classdraftviewproviders_1_1view__label_1_1ViewProviderLabel.html#a91b172318f8d77c8aaab8ac2d20ae0c0),
and
[draftviewproviders.view_label.ViewProviderLabel.update_label()](../../d1/d88/classdraftviewproviders_1_1view__label_1_1ViewProviderLabel.html#aeff559615650631a8995d5cc799dc2c2).

## ◆ literal

automotive_design.text_literal.literal  
---  
  
## ◆ path

automotive_design.text_literal.path  
---  
  
Referenced by
[PathScripts.PathToolBitLibraryGui.ToolBitLibrary.librarySave()](../../dd/d3a/classPathScripts_1_1PathToolBitLibraryGui_1_1ToolBitLibrary.html#a78e1b668521bdf525ca26a7be60ac80e),
[PathScripts.PathToolBitLibraryGui.ToolBitLibrary.librarySaveAs()](../../dd/d3a/classPathScripts_1_1PathToolBitLibraryGui_1_1ToolBitLibrary.html#aacc6b835c3257775d5683ff5c4494b27),
and
[PathScripts.PathToolBitLibraryGui.ToolBitLibrary.loadData()](../../dd/d3a/classPathScripts_1_1PathToolBitLibraryGui_1_1ToolBitLibrary.html#ae2616669ba6b30e1833ff2d498cc2d6a).

## ◆ placement

automotive_design.text_literal.placement  
---  
  
Referenced by
[draftguitools.gui_trimex.Trimex.trimObject()](../../da/df7/classdraftguitools_1_1gui__trimex_1_1Trimex.html#a5e72e325ef0a53c3fde6c75c2eb56ba6).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

