---
url: https://freecad.github.io/SourceDoc/d6/df4/classautomotive__design_1_1context__dependent__shape__representation.html
scraped_at: 2025-09-08T15:02:43.435007
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [automotive_design](../../d4/ddf/namespaceautomotive__design.html)
  * [context_dependent_shape_representation](../../d6/df4/classautomotive__design_1_1context__dependent__shape__representation.html)

[List of all members](../../df/d58/classautomotive__design_1_1context__dependent__shape__representation-members.html) | Public Member Functions | Public Attributes

automotive_design.context_dependent_shape_representation Class Reference

##  Public Member Functions  
  
---  
def | [description](../../d6/df4/classautomotive__design_1_1context__dependent__shape__representation.html#ab56920fc519f1ddafc402ba65b4c257b) ()  
def | [name](../../d6/df4/classautomotive__design_1_1context__dependent__shape__representation.html#a68681ed2fd8236e409b4c400de7c02d6) ()  
def | [representation_relation](../../d6/df4/classautomotive__design_1_1context__dependent__shape__representation.html#a9e2d6f53a1e1b42c273e7caddafb1554) ()  
def | [represented_product_relation](../../d6/df4/classautomotive__design_1_1context__dependent__shape__representation.html#ab45c0b2e3a2242d5a9239bea8f64810c) ()  
def | [wr1](../../d6/df4/classautomotive__design_1_1context__dependent__shape__representation.html#a715d04697f7157e60f5ea37e36823235) (self)  
def | [wr2](../../d6/df4/classautomotive__design_1_1context__dependent__shape__representation.html#ae2544c3b4e8a37c58d4fb316ad39b900) (self)  
def | [wr3](../../d6/df4/classautomotive__design_1_1context__dependent__shape__representation.html#ae7a9c72f1c1098a0f68cd151445409e3) (self)  
  
##  Public Attributes  
  
---  
|
[representation_relation](../../d6/df4/classautomotive__design_1_1context__dependent__shape__representation.html#a2c3653e498aedff6ad0b7e51778cbd28)  
|
[represented_product_relation](../../d6/df4/classautomotive__design_1_1context__dependent__shape__representation.html#a8032070905282d0f55c9b69d4a3f9346)  
  
## Detailed Description

    
    
    Entity context_dependent_shape_representation definition.
    
        :param representation_relation
        :type representation_relation:shape_representation_relationship
    
        :param represented_product_relation
        :type represented_product_relation:product_definition_shape
    
        :param description
        :type description:text
    
        :param name
        :type name:label

## Member Function Documentation

## ◆ description()

def automotive_design.context_dependent_shape_representation.description  | ( | | ) |   
---|---|---|---|---  
  
References
[automotive_design.get_description_value()](../../d4/ddf/namespaceautomotive__design.html#a7894d555e3f25a436366bbbf328b1bf2).

Referenced by
[Addon.Addon.set_metadata()](../../d8/d91/classAddon_1_1Addon.html#a799523f4861c30f1516a59602d5b77cd),
and
[Addon.Addon.to_cache()](../../d8/d91/classAddon_1_1Addon.html#aba84dd320889a7cb37c99a8b8cdc87f5).

## ◆ name()

def automotive_design.context_dependent_shape_representation.name  | ( | | ) |   
---|---|---|---|---  
  
References
[automotive_design.get_name_value()](../../d4/ddf/namespaceautomotive__design.html#ae730b907f9032c797025ed6d3d4fb54e).

Referenced by
[draftguitools.gui_groups.Ui_AddNamedGroup.accept()](../../d3/df7/classdraftguitools_1_1gui__groups_1_1Ui__AddNamedGroup.html#a9ea5973817eab7d74792f5b109a01466),
[prototype.Node.addtofreecad()](../../d2/d62/classprototype_1_1Node.html#adc095cc5636da029d1e0d9cef8859701),
[Addon.Addon.disable()](../../d8/d91/classAddon_1_1Addon.html#ae714705a38afe9f13cd2b17580178b31),
[Addon.Addon.enable()](../../d8/d91/classAddon_1_1Addon.html#a79d327ec9a0b4e85e9e96cfad4003ed6),
[addonmanager_macro.Macro.filename()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#a5de4e6a1f3c41dce24066111955cd706),
[gzip_utf8.GzipFile.filename()](../../d2/dbe/classgzip__utf8_1_1GzipFile.html#ab56fe84a4eb08c44e7a0026280c01229),
[addonmanager_macro.Macro.fill_details_from_code()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#a49b8d021a9b8255f8a490e880eb15489),
[addonmanager_macro.Macro.fill_details_from_wiki()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#afc7e62120da96fc1be9dd2b4bd28ddac),
[Addon.Addon.get_cached_icon_filename()](../../d8/d91/classAddon_1_1Addon.html#a7b026027a2904028032edbe3e99e2cbd),
[ifc4.ifcapproval.hasidentifierorname()](../../df/d91/classifc4_1_1ifcapproval.html#a54f558ba3b17fad5fc6579e9d5f50947),
[addonmanager_macro.Macro.install()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#ae770ab07dcecebae2b7414f278b227fe),
[Addon.Addon.is_disabled()](../../d8/d91/classAddon_1_1Addon.html#a5752a95fcf0c51ed06f9841b381d3e50),
[femsolver.elmer.sifio.Section.keys()](../../db/dab/classfemsolver_1_1elmer_1_1sifio_1_1Section.html#ab5b099447f66f33743850697f0e20de4),
[automotive_design.si_unit.named_unit_dimensions()](../../d5/d77/classautomotive__design_1_1si__unit.html#a68eb7954eb09daa334bc8f2c2abbe5f9),
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction.output()](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#aeedd5f59969cc27432880d1916f3d7f9),
[prototype.Node.pprint()](../../d2/d62/classprototype_1_1Node.html#a5ae181c34e48238d2364b0ba4960c252),
[prototype.Node.pprint2()](../../d2/d62/classprototype_1_1Node.html#aaedcc4ba1fb305c7ddcc025235043cd5),
[PathScripts.PathSetupSheetGui.OpTaskPanel.propertyGroup()](../../df/dbe/classPathScripts_1_1PathSetupSheetGui_1_1OpTaskPanel.html#a69cbbaadcb9cff7b526af2c743041d7b),
[PathScripts.PathSetupSheetGui.OpTaskPanel.propertyName()](../../df/dbe/classPathScripts_1_1PathSetupSheetGui_1_1OpTaskPanel.html#ad9bd0e0149d1bc42fc8e89a290de4910),
[PathScripts.PathJobGui.TaskPanel.reject()](../../dc/d2a/classPathScripts_1_1PathJobGui_1_1TaskPanel.html#a54fd97ba9b0060fa8fed8a43c360da0c),
[addonmanager_macro.Macro.remove()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#ad13245288f8beb62d92cb458a2d2ce05),
[Addon.Addon.to_cache()](../../d8/d91/classAddon_1_1Addon.html#aba84dd320889a7cb37c99a8b8cdc87f5),
[ifc2x3.ifcexternalreference.wr1()](../../dd/dec/classifc2x3_1_1ifcexternalreference.html#ae8dab59397d2468ff7fe0a10f42b75b2),
[ifc2x3.ifcdocumentreference.wr1()](../../df/dd6/classifc2x3_1_1ifcdocumentreference.html#a7d5fdb1cb0dee567c44834b868c5cdad),
[ifc4.ifcexternalreference.wr1()](../../d5/dd9/classifc4_1_1ifcexternalreference.html#a0e6ba5265c69b44700e8d9b179e9f240),
[ifc4.ifcdocumentreference.wr1()](../../d7/d2b/classifc4_1_1ifcdocumentreference.html#a8779d74c67e647441d1fb20c76f44f97),
and
[automotive_design.general_property_association.wr2()](../../d2/df3/classautomotive__design_1_1general__property__association.html#ae7f46462c59bc4e541a5d2511631eb65).

## ◆ representation_relation()

def automotive_design.context_dependent_shape_representation.representation_relation  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.context_dependent_shape_representation._representation_relation,
automotive_design.context_dependent_shape_representation._representation_relation,
and
config_control_design.context_dependent_shape_representation._representation_relation.

## ◆ represented_product_relation()

def automotive_design.context_dependent_shape_representation.represented_product_relation  | ( | | ) |   
---|---|---|---|---  
  
References
ap203_configuration_controlled_3d_design_of_mechanical_parts_and_assemblies_mim_lf.context_dependent_shape_representation._represented_product_relation,
automotive_design.context_dependent_shape_representation._represented_product_relation,
and
config_control_design.context_dependent_shape_representation._represented_product_relation.

## ◆ wr1()

def automotive_design.context_dependent_shape_representation.wr1  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References App::TransactionFactory.self, Py::PythonExtension< T >.self(),
Py::PythonClass< T >.self(), Py::PythonExtensionBase.self(),
Gui::AutoSaver.self, and Gui::Dialog::DownloadManager.self.

## ◆ wr2()

def automotive_design.context_dependent_shape_representation.wr2  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
## ◆ wr3()

def automotive_design.context_dependent_shape_representation.wr3  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
## Member Data Documentation

## ◆ representation_relation

automotive_design.context_dependent_shape_representation.representation_relation  
---  
  
## ◆ represented_product_relation

automotive_design.context_dependent_shape_representation.represented_product_relation  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/Import/App/automotive_design.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

