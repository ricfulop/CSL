---
url: https://freecad.github.io/SourceDoc/dc/d04/structApp_1_1Meta_1_1Contact.html
scraped_at: 2025-09-08T14:53:34.187955
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [Meta](../../d9/dcf/namespaceApp_1_1Meta.html)
  * [Contact](../../dc/d04/structApp_1_1Meta_1_1Contact.html)

[List of all members](../../da/db9/structApp_1_1Meta_1_1Contact-members.html) | Public Member Functions | Public Attributes

App::Meta::Contact Struct Reference

A person or company representing a point of contact for the package (either
author or maintainer).
[More...](../../dc/d04/structApp_1_1Meta_1_1Contact.html#details)

`#include <Metadata.h>`

##  Public Member Functions  
  
---  
|
[Contact](../../dc/d04/structApp_1_1Meta_1_1Contact.html#a608a3ecfe453fa1df150c1545927b47a)
()=default  
|
[Contact](../../dc/d04/structApp_1_1Meta_1_1Contact.html#aae845979c66dd68c83fb5754d591b4be)
(const std::string
&[name](../../dc/d04/structApp_1_1Meta_1_1Contact.html#a1fe70f5bf5e4a9d53a96ba71586b4f19),
const std::string
&[email](../../dc/d04/structApp_1_1Meta_1_1Contact.html#a7f18a7762edb2f42863b8f8fa526b131))  
|
[Contact](../../dc/d04/structApp_1_1Meta_1_1Contact.html#acbaeb112379720d2bc2163f73dc25cb5)
(const XERCES_CPP_NAMESPACE::DOMElement *e)  
  
##  Public Attributes  
  
---  
std::string | [email](../../dc/d04/structApp_1_1Meta_1_1Contact.html#a7f18a7762edb2f42863b8f8fa526b131)  
std::string | [name](../../dc/d04/structApp_1_1Meta_1_1Contact.html#a1fe70f5bf5e4a9d53a96ba71586b4f19)  
  
## Detailed Description

A person or company representing a point of contact for the package (either
author or maintainer).

## Constructor & Destructor Documentation

## ◆ Contact() [1/3]

| App::Meta::Contact::Contact  | ( | | ) |   
---|---|---|---|---  
default  
  
## ◆ Contact() [2/3]

Meta::Contact::Contact  | ( | const std::string & | _name_ ,   
---|---|---|---  
|  | const std::string & | _email_  
| ) | |   
  
## ◆ Contact() [3/3]

| Meta::Contact::Contact  | ( | const XERCES_CPP_NAMESPACE::DOMElement *  | _e_| ) |   
---|---|---|---|---|---  
explicit  
  
References
[StrXUTF8::str](../../d7/d9a/classStrXUTF8.html#ab8f96bd3cf6c91dc259c03328034c44b).

## Member Data Documentation

## ◆ email

std::string App::Meta::Contact::email  
---  
  
## ◆ name

std::string App::Meta::Contact::name  
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

* * *

The documentation for this struct was generated from the following files:

  * FreeCAD/src/App/Metadata.h
  * FreeCAD/src/App/Metadata.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

