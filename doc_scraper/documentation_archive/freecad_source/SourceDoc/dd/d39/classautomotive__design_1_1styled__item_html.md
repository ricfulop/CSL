---
url: https://freecad.github.io/SourceDoc/dd/d39/classautomotive__design_1_1styled__item.html
scraped_at: 2025-09-08T15:13:21.075063
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [styled_item](../../dd/d39/classautomotive__design_1_1styled__item.html)

[List of all members](../../dd/d28/classautomotive__design_1_1styled__item-members.html) | Public Member Functions | Public Attributes

automotive_design.styled_item Class Reference

##  Public Member Functions  
  
---  
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
[item](../../dd/d39/classautomotive__design_1_1styled__item.html#aad87aa33fdbad670cc9dfcfdbe866d79)  
|
[styles](../../dd/d39/classautomotive__design_1_1styled__item.html#a715f59d8d13c21ae1a5c704b0dbdbebb)  
![-](../../closed.png) Public Attributes inherited from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html)  
|
[name](../../d3/d20/classautomotive__design_1_1representation__item.html#a3d48fe912053adaf5f187b606fa81c87)  
  
## Detailed Description

    
    
    Entity styled_item definition.
    
        :param styles
        :type styles:SET(1,None,'presentation_style_assignment', scope = schema_scope)
    
        :param item
        :type item:representation_item

## Member Function Documentation

## ◆ item()

def automotive_design.styled_item.item  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.styled_item._item,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.presented_item_representation._item,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.applied_name_assignment._item,
automotive_design.styled_item._item,
automotive_design.presented_item_representation._item,
ifc2x3.ifcstyleditem._item, ifc2x3.ifcannotationsurface._item, and
ifc4.ifcstyleditem._item.

Referenced by
[ifc4.ifcstyleditem.applicableitem()](../../da/db5/classifc4_1_1ifcstyleditem.html#afec413ef4925a0303b2e0c64d84e197f),
[ifc2x3.ifcannotationsurface.wr01()](../../df/d68/classifc2x3_1_1ifcannotationsurface.html#aa6d5b4a9fe9a7e62c5b7c2e0b12743af),
[ifc2x3.ifctexturemap.wr11()](../../d9/d8d/classifc2x3_1_1ifctexturemap.html#a3c56daddbe67369ba327071ae2944d11),
and
[ifc2x3.ifcstyleditem.wr12()](../../d4/d21/classifc2x3_1_1ifcstyleditem.html#adc38774be3dfdfb65c5d857877be88be).

## ◆ styles()

def automotive_design.styled_item.styles  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.styled_item._styles,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.presentation_style_assignment._styles,
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.surface_side_style._styles,
automotive_design.styled_item._styles,
automotive_design.presentation_style_assignment._styles,
automotive_design.surface_side_style._styles, ifc2x3.ifcstyleditem._styles,
ifc2x3.ifcpresentationstyleassignment._styles, ifc2x3.ifcsurfacestyle._styles,
ifc4.ifcpresentationstyleassignment._styles, ifc4.ifcstyleditem._styles, and
ifc4.ifcsurfacestyle._styles.

Referenced by
[draftguitools.gui_annotationstyleeditor.AnnotationStyleEditor.Activated()](../../d6/d03/classdraftguitools_1_1gui__annotationstyleeditor_1_1AnnotationStyleEditor.html#ac7fe745faef8d402397cb0641e130965),
[draftguitools.gui_annotationstyleeditor.AnnotationStyleEditor.fill_editor()](../../d6/d03/classdraftguitools_1_1gui__annotationstyleeditor_1_1AnnotationStyleEditor.html#a82c7c22dfe901c7297d64f3a715ffc11),
[draftguitools.gui_annotationstyleeditor.AnnotationStyleEditor.on_delete()](../../d6/d03/classdraftguitools_1_1gui__annotationstyleeditor_1_1AnnotationStyleEditor.html#af3669f24c57e597f1625c82f67d0cdb2),
[draftguitools.gui_annotationstyleeditor.AnnotationStyleEditor.on_export()](../../d6/d03/classdraftguitools_1_1gui__annotationstyleeditor_1_1AnnotationStyleEditor.html#abeb21907d72e91df6fbfff1259c769a0),
[draftguitools.gui_annotationstyleeditor.AnnotationStyleEditor.on_import()](../../d6/d03/classdraftguitools_1_1gui__annotationstyleeditor_1_1AnnotationStyleEditor.html#aa4ea57c767b4f551ad3f7ba88fee61b8),
[draftguitools.gui_annotationstyleeditor.AnnotationStyleEditor.on_rename()](../../d6/d03/classdraftguitools_1_1gui__annotationstyleeditor_1_1AnnotationStyleEditor.html#a1c19fb58b4db3cb77344af3217075ea4),
[draftguitools.gui_annotationstyleeditor.AnnotationStyleEditor.on_style_changed()](../../d6/d03/classdraftguitools_1_1gui__annotationstyleeditor_1_1AnnotationStyleEditor.html#ac5183cb3d37565f9de75e2aa006e48e6),
[draftguitools.gui_annotationstyleeditor.AnnotationStyleEditor.update_style()](../../d6/d03/classdraftguitools_1_1gui__annotationstyleeditor_1_1AnnotationStyleEditor.html#a498ea0c29ad69561734096f882857154),
[ifc2x3.ifcstyleditem.wr11()](../../d4/d21/classifc2x3_1_1ifcstyleditem.html#acbf3a0ec75ea5e8ddd4efe38fd13683c),
[automotive_design.annotation_plane.wr3()](../../df/dcb/classautomotive__design_1_1annotation__plane.html#a8666f515b5da47a5476219736f39a010),
and
[automotive_design.annotation_plane.wr4()](../../df/dcb/classautomotive__design_1_1annotation__plane.html#a9c405c226390be9640e929de515a3e39).

## ◆ wr1()

def automotive_design.styled_item.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
Reimplemented from
[automotive_design.representation_item](../../d3/d20/classautomotive__design_1_1representation__item.html#af350c19fc5e5763d4991494a99d979ed).

Reimplemented in
[automotive_design.annotation_occurrence](../../d1/d82/classautomotive__design_1_1annotation__occurrence.html#a1d53f8edfd0b54fd137032bdf5e7a508),
[automotive_design.leader_terminator](../../d5/d4f/classautomotive__design_1_1leader__terminator.html#a1ca5e19116c0e49ef4914cd46ea8eab6),
[automotive_design.annotation_subfigure_occurrence](../../d2/df6/classautomotive__design_1_1annotation__subfigure__occurrence.html#a5a53a1426b232c9c8fe4aadfc19a7ae9),
[automotive_design.draughting_annotation_occurrence](../../d6/d4b/classautomotive__design_1_1draughting__annotation__occurrence.html#acbf44c99018ea6474afd704d0e25d07e),
[automotive_design.context_dependent_over_riding_styled_item](../../d7/d22/classautomotive__design_1_1context__dependent__over__riding__styled__item.html#a35512624313535625bdfa25941399755),
[automotive_design.hidden_element_over_riding_styled_item](../../da/d95/classautomotive__design_1_1hidden__element__over__riding__styled__item.html#ad2d609783c0ef43800f6255ed6844ddc),
[automotive_design.dimension_curve_terminator](../../d8/d02/classautomotive__design_1_1dimension__curve__terminator.html#a28f4e7e1479454418453a5641f038596),
[automotive_design.annotation_plane](../../df/dcb/classautomotive__design_1_1annotation__plane.html#ad19475f567f313205f1412f9e01e5c5f),
[automotive_design.leader_curve](../../dd/d24/classautomotive__design_1_1leader__curve.html#a2acb4f5befb39915f826f8bb5c0cef4a),
and
[automotive_design.dimension_curve](../../d1/d19/classautomotive__design_1_1dimension__curve.html#ab918ed2328a732795aee5421c50084c9).

References App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

## Member Data Documentation

## ◆ item

automotive_design.styled_item.item  
---  
  
Referenced by
[ifc4.ifcstyleditem.applicableitem()](../../da/db5/classifc4_1_1ifcstyleditem.html#afec413ef4925a0303b2e0c64d84e197f),
[ifc2x3.ifcannotationsurface.wr01()](../../df/d68/classifc2x3_1_1ifcannotationsurface.html#aa6d5b4a9fe9a7e62c5b7c2e0b12743af),
[ifc2x3.ifctexturemap.wr11()](../../d9/d8d/classifc2x3_1_1ifctexturemap.html#a3c56daddbe67369ba327071ae2944d11),
and
[ifc2x3.ifcstyleditem.wr12()](../../d4/d21/classifc2x3_1_1ifcstyleditem.html#adc38774be3dfdfb65c5d857877be88be).

## ◆ styles

automotive_design.styled_item.styles  
---  
  
Referenced by
[draftguitools.gui_annotationstyleeditor.AnnotationStyleEditor.Activated()](../../d6/d03/classdraftguitools_1_1gui__annotationstyleeditor_1_1AnnotationStyleEditor.html#ac7fe745faef8d402397cb0641e130965),
[draftguitools.gui_annotationstyleeditor.AnnotationStyleEditor.fill_editor()](../../d6/d03/classdraftguitools_1_1gui__annotationstyleeditor_1_1AnnotationStyleEditor.html#a82c7c22dfe901c7297d64f3a715ffc11),
[draftguitools.gui_annotationstyleeditor.AnnotationStyleEditor.on_delete()](../../d6/d03/classdraftguitools_1_1gui__annotationstyleeditor_1_1AnnotationStyleEditor.html#af3669f24c57e597f1625c82f67d0cdb2),
[draftguitools.gui_annotationstyleeditor.AnnotationStyleEditor.on_export()](../../d6/d03/classdraftguitools_1_1gui__annotationstyleeditor_1_1AnnotationStyleEditor.html#abeb21907d72e91df6fbfff1259c769a0),
[draftguitools.gui_annotationstyleeditor.AnnotationStyleEditor.on_import()](../../d6/d03/classdraftguitools_1_1gui__annotationstyleeditor_1_1AnnotationStyleEditor.html#aa4ea57c767b4f551ad3f7ba88fee61b8),
[draftguitools.gui_annotationstyleeditor.AnnotationStyleEditor.on_rename()](../../d6/d03/classdraftguitools_1_1gui__annotationstyleeditor_1_1AnnotationStyleEditor.html#a1c19fb58b4db3cb77344af3217075ea4),
[draftguitools.gui_annotationstyleeditor.AnnotationStyleEditor.on_style_changed()](../../d6/d03/classdraftguitools_1_1gui__annotationstyleeditor_1_1AnnotationStyleEditor.html#ac5183cb3d37565f9de75e2aa006e48e6),
[draftguitools.gui_annotationstyleeditor.AnnotationStyleEditor.update_style()](../../d6/d03/classdraftguitools_1_1gui__annotationstyleeditor_1_1AnnotationStyleEditor.html#a498ea0c29ad69561734096f882857154),
[ifc2x3.ifcstyleditem.wr11()](../../d4/d21/classifc2x3_1_1ifcstyleditem.html#acbf3a0ec75ea5e8ddd4efe38fd13683c),
[automotive_design.annotation_plane.wr3()](../../df/dcb/classautomotive__design_1_1annotation__plane.html#a8666f515b5da47a5476219736f39a010),
and
[automotive_design.annotation_plane.wr4()](../../df/dcb/classautomotive__design_1_1annotation__plane.html#a9c405c226390be9640e929de515a3e39).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

