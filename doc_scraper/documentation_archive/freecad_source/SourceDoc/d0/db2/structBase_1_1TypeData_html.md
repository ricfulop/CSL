---
url: https://freecad.github.io/SourceDoc/d0/db2/structBase_1_1TypeData.html
scraped_at: 2025-09-08T15:17:34.152763
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [TypeData](../../d0/db2/structBase_1_1TypeData.html)

[List of all members](../../d2/d17/structBase_1_1TypeData-members.html) | Public Member Functions | Public Attributes

Base::TypeData Struct Reference

##  Public Member Functions  
  
---  
|
[TypeData](../../d0/db2/structBase_1_1TypeData.html#a00bd66b1c7da849993ff3480c52e2889)
(const char *theName, const [Type](../../dc/dee/classBase_1_1Type.html)
[type](../../d9/d98/classtype.html)=[Type::badType](../../dc/dee/classBase_1_1Type.html#ae37d20b54fb01b5d5490d5f7d5cd1e76)(),
const [Type](../../dc/dee/classBase_1_1Type.html)
theParent=[Type::badType](../../dc/dee/classBase_1_1Type.html#ae37d20b54fb01b5d5490d5f7d5cd1e76)(),
[Type::instantiationMethod](../../dc/dee/classBase_1_1Type.html#a10d2cdeee4a86a3e82a3d71e37a87495)
method=nullptr)  
  
##  Public Attributes  
  
---  
[Type::instantiationMethod](../../dc/dee/classBase_1_1Type.html#a10d2cdeee4a86a3e82a3d71e37a87495) | [instMethod](../../d0/db2/structBase_1_1TypeData.html#a27787bf76ead6cdc3659d7d6f4f737a6)  
std::string | [name](../../d0/db2/structBase_1_1TypeData.html#a51f0bd75ae1e7a4ab188ee080d0c4d1e)  
[Type](../../dc/dee/classBase_1_1Type.html) | [parent](../../d0/db2/structBase_1_1TypeData.html#a6ada83c8da6acf61582aa7dbf5857759)  
[Type](../../dc/dee/classBase_1_1Type.html) | [type](../../d0/db2/structBase_1_1TypeData.html#a2dac3341b32ea32dcf2887032463d030)  
  
## Constructor & Destructor Documentation

## ◆ TypeData()

Base::TypeData::TypeData  | ( | const char *  | _theName_ ,   
---|---|---|---  
|  | const [Type](../../dc/dee/classBase_1_1Type.html) | _type_ = `[Type::badType](../../dc/dee/classBase_1_1Type.html#ae37d20b54fb01b5d5490d5f7d5cd1e76)()`,   
|  | const [Type](../../dc/dee/classBase_1_1Type.html) | _theParent_ = `[Type::badType](../../dc/dee/classBase_1_1Type.html#ae37d20b54fb01b5d5490d5f7d5cd1e76)()`,   
|  | [Type::instantiationMethod](../../dc/dee/classBase_1_1Type.html#a10d2cdeee4a86a3e82a3d71e37a87495) | _method_ = `nullptr`  
| ) | |   
  
## Member Data Documentation

## ◆ instMethod

[Type::instantiationMethod](../../dc/dee/classBase_1_1Type.html#a10d2cdeee4a86a3e82a3d71e37a87495)
Base::TypeData::instMethod  
---  
  
## ◆ name

std::string Base::TypeData::name  
---  
  
Referenced by
[draftguitools.gui_groups.Ui_AddNamedGroup::accept()](../../d3/df7/classdraftguitools_1_1gui__groups_1_1Ui__AddNamedGroup.html#a9ea5973817eab7d74792f5b109a01466),
[prototype.Node::addtofreecad()](../../d2/d62/classprototype_1_1Node.html#adc095cc5636da029d1e0d9cef8859701),
[Addon.Addon::disable()](../../d8/d91/classAddon_1_1Addon.html#ae714705a38afe9f13cd2b17580178b31),
[Addon.Addon::enable()](../../d8/d91/classAddon_1_1Addon.html#a79d327ec9a0b4e85e9e96cfad4003ed6),
[addonmanager_macro.Macro::filename()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#a5de4e6a1f3c41dce24066111955cd706),
[gzip_utf8.GzipFile::filename()](../../d2/dbe/classgzip__utf8_1_1GzipFile.html#ab56fe84a4eb08c44e7a0026280c01229),
[addonmanager_macro.Macro::fill_details_from_code()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#a49b8d021a9b8255f8a490e880eb15489),
[addonmanager_macro.Macro::fill_details_from_wiki()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#afc7e62120da96fc1be9dd2b4bd28ddac),
[Addon.Addon::get_cached_icon_filename()](../../d8/d91/classAddon_1_1Addon.html#a7b026027a2904028032edbe3e99e2cbd),
[ifc4.ifcapproval::hasidentifierorname()](../../df/d91/classifc4_1_1ifcapproval.html#a54f558ba3b17fad5fc6579e9d5f50947),
[addonmanager_macro.Macro::install()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#ae770ab07dcecebae2b7414f278b227fe),
[Addon.Addon::is_disabled()](../../d8/d91/classAddon_1_1Addon.html#a5752a95fcf0c51ed06f9841b381d3e50),
[femsolver.elmer.sifio.Section::keys()](../../db/dab/classfemsolver_1_1elmer_1_1sifio_1_1Section.html#ab5b099447f66f33743850697f0e20de4),
[automotive_design.si_unit::named_unit_dimensions()](../../d5/d77/classautomotive__design_1_1si__unit.html#a68eb7954eb09daa334bc8f2c2abbe5f9),
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction::output()](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#aeedd5f59969cc27432880d1916f3d7f9),
[prototype.Node::pprint()](../../d2/d62/classprototype_1_1Node.html#a5ae181c34e48238d2364b0ba4960c252),
[prototype.Node::pprint2()](../../d2/d62/classprototype_1_1Node.html#aaedcc4ba1fb305c7ddcc025235043cd5),
[PathScripts.PathSetupSheetGui.OpTaskPanel::propertyGroup()](../../df/dbe/classPathScripts_1_1PathSetupSheetGui_1_1OpTaskPanel.html#a69cbbaadcb9cff7b526af2c743041d7b),
[PathScripts.PathSetupSheetGui.OpTaskPanel::propertyName()](../../df/dbe/classPathScripts_1_1PathSetupSheetGui_1_1OpTaskPanel.html#ad9bd0e0149d1bc42fc8e89a290de4910),
[PathScripts.PathJobGui.TaskPanel::reject()](../../dc/d2a/classPathScripts_1_1PathJobGui_1_1TaskPanel.html#a54fd97ba9b0060fa8fed8a43c360da0c),
[addonmanager_macro.Macro::remove()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#ad13245288f8beb62d92cb458a2d2ce05),
[Addon.Addon::to_cache()](../../d8/d91/classAddon_1_1Addon.html#aba84dd320889a7cb37c99a8b8cdc87f5),
[ifc2x3.ifcexternalreference::wr1()](../../dd/dec/classifc2x3_1_1ifcexternalreference.html#ae8dab59397d2468ff7fe0a10f42b75b2),
[ifc2x3.ifcdocumentreference::wr1()](../../df/dd6/classifc2x3_1_1ifcdocumentreference.html#a7d5fdb1cb0dee567c44834b868c5cdad),
[ifc4.ifcexternalreference::wr1()](../../d5/dd9/classifc4_1_1ifcexternalreference.html#a0e6ba5265c69b44700e8d9b179e9f240),
[ifc4.ifcdocumentreference::wr1()](../../d7/d2b/classifc4_1_1ifcdocumentreference.html#a8779d74c67e647441d1fb20c76f44f97),
and
[automotive_design.general_property_association::wr2()](../../d2/df3/classautomotive__design_1_1general__property__association.html#ae7f46462c59bc4e541a5d2511631eb65).

## ◆ parent

[Type](../../dc/dee/classBase_1_1Type.html) Base::TypeData::parent  
---  
  
Referenced by
[PathScripts.PathSimulatorGui.CAMSimTaskUi::accept()](../../d9/ddf/classPathScripts_1_1PathSimulatorGui_1_1CAMSimTaskUi.html#a4f458ca1ce80e66e440c5ac24dc22c8d),
[Mod.PartDesign.WizardShaft.Shaft.Shaft::equilibrium()](../../da/dd7/classMod_1_1PartDesign_1_1WizardShaft_1_1Shaft_1_1Shaft.html#abf673f8921374b011ced4c4a770d44e6),
[PathScripts.PathSimulatorGui.CAMSimTaskUi::reject()](../../d9/ddf/classPathScripts_1_1PathSimulatorGui_1_1CAMSimTaskUi.html#a3ab3f3b4e171363a14dc6cc0a5edd790),
and
[PathScripts.PathOpGui.TaskPanelPage::setParent()](../../d1/d18/classPathScripts_1_1PathOpGui_1_1TaskPanelPage.html#a98bc030e5415979bcaa07140a675a6e3).

## ◆ type

[Type](../../dc/dee/classBase_1_1Type.html) Base::TypeData::type  
---  
  
Referenced by
[ArchProfile.ProfileTaskPanel::accept()](../../dc/d9a/classArchProfile_1_1ProfileTaskPanel.html#a2506d93eee0ae9e8570d71e066425999),
and
[ArchProfile.ProfileTaskPanel::retranslateUi()](../../dc/d9a/classArchProfile_1_1ProfileTaskPanel.html#a8b6ffa229d56acdd0aabe8fb92de728b).

* * *

The documentation for this struct was generated from the following file:

  * FreeCAD/src/Base/Type.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

