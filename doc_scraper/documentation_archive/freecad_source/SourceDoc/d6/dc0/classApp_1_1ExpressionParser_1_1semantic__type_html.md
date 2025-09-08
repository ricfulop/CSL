---
url: https://freecad.github.io/SourceDoc/d6/dc0/classApp_1_1ExpressionParser_1_1semantic__type.html
scraped_at: 2025-09-08T14:53:32.191564
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [ExpressionParser](../../d1/d21/namespaceApp_1_1ExpressionParser.html)
  * [semantic_type](../../d6/dc0/classApp_1_1ExpressionParser_1_1semantic__type.html)

[List of all members](../../d7/dab/classApp_1_1ExpressionParser_1_1semantic__type-members.html) | Public Member Functions | Public Attributes

App::ExpressionParser::semantic_type Class Reference

The
[semantic_type](../../d6/dc0/classApp_1_1ExpressionParser_1_1semantic__type.html
"The semantic_type class encapsulates the value in the parse tree during
parsing.") class encapsulates the value in the parse tree during parsing.
[More...](../../d6/dc0/classApp_1_1ExpressionParser_1_1semantic__type.html#details)

`#include <ExpressionParser.h>`

##  Public Member Functions  
  
---  
|
[semantic_type](../../d6/dc0/classApp_1_1ExpressionParser_1_1semantic__type.html#a08a7a6fced36287e50d8dfad9ee19919)
()  
  
##  Public Attributes  
  
---  
std::vector< [Expression](../../dc/d5c/classApp_1_1Expression.html) * > | [arguments](../../d6/dc0/classApp_1_1ExpressionParser_1_1semantic__type.html#a29f0d0ccf3e770e26833ea5fe6242c10)  
[Expression::Component](../../d5/df9/structApp_1_1Expression_1_1Component.html) * | [component](../../d6/dc0/classApp_1_1ExpressionParser_1_1semantic__type.html#a863bad108b953f4c88fa45141ddcfd67)  
std::deque< [ObjectIdentifier::Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html) > | [components](../../d6/dc0/classApp_1_1ExpressionParser_1_1semantic__type.html#aea8ff7eab2d6b53d95e5c3b2a2ceb452)  
struct {  
double
[fvalue](../../d6/dc0/classApp_1_1ExpressionParser_1_1semantic__type.html#ad8c3f1cdca23c84a44fb0d82a231bf02)
= 0  
const char *
[name](../../d6/dc0/classApp_1_1ExpressionParser_1_1semantic__type.html#ace4cc35a7d6ab60d12196ca6118335e0)
= ""  
} | [constant](../../d6/dc0/classApp_1_1ExpressionParser_1_1semantic__type.html#ad615977f8ff0e6306b8769463d2846cd)  
[Expression](../../dc/d5c/classApp_1_1Expression.html) * | [expr](../../d6/dc0/classApp_1_1ExpressionParser_1_1semantic__type.html#a032b7fd4075a1062b0a67cc1df674fb2)  
std::pair< [FunctionExpression::Function](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658), std::string > | [func](../../d6/dc0/classApp_1_1ExpressionParser_1_1semantic__type.html#a3cff16a795f00758ca3b7363e83e4ef9)  
double | [fvalue](../../d6/dc0/classApp_1_1ExpressionParser_1_1semantic__type.html#ad8c3f1cdca23c84a44fb0d82a231bf02) = 0  
long long [int](../../d1/da0/classint.html) | [ivalue](../../d6/dc0/classApp_1_1ExpressionParser_1_1semantic__type.html#aa41a173d5494ec1751f790c92ebd3865)  
std::vector< [Expression](../../dc/d5c/classApp_1_1Expression.html) * > | [list](../../d6/dc0/classApp_1_1ExpressionParser_1_1semantic__type.html#a985763e99cfba13a8679263e30f4f055)  
[ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) | [path](../../d6/dc0/classApp_1_1ExpressionParser_1_1semantic__type.html#ae8309a95951e76f5387e709188b0f537)  
struct {  
[Base::Quantity](../../d8/d18/classBase_1_1Quantity.html)
[scaler](../../d6/dc0/classApp_1_1ExpressionParser_1_1semantic__type.html#a5d7e03d39875d96959e135e05942ef18)  
std::string
[unitStr](../../d6/dc0/classApp_1_1ExpressionParser_1_1semantic__type.html#a6be20fb5713bd32d82a669a6bbccbda7)  
} | [quantity](../../d6/dc0/classApp_1_1ExpressionParser_1_1semantic__type.html#a7e78033f7fd4478c5b67f625c5fa9e4f)  
std::string | [string](../../d6/dc0/classApp_1_1ExpressionParser_1_1semantic__type.html#ac7106d96c5c7135c2f9d97290564ca4f)  
[ObjectIdentifier::String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html) | [string_or_identifier](../../d6/dc0/classApp_1_1ExpressionParser_1_1semantic__type.html#a55b4bcd3b4512af0291f8348201f8fb6)  
  
## Detailed Description

The
[semantic_type](../../d6/dc0/classApp_1_1ExpressionParser_1_1semantic__type.html
"The semantic_type class encapsulates the value in the parse tree during
parsing.") class encapsulates the value in the parse tree during parsing.

## Constructor & Destructor Documentation

## ◆ semantic_type()

App::ExpressionParser::semantic_type::semantic_type  | ( | | ) |   
---|---|---|---|---  
  
References
[App::FunctionExpression::NONE](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a2bbe942c44dc7bdda86ce170aad0b4fa).

## Member Data Documentation

## ◆ arguments

std::vector<[Expression](../../dc/d5c/classApp_1_1Expression.html)*>
App::ExpressionParser::semantic_type::arguments  
---  
  
Referenced by
[prototype.Node::addtofreecad()](../../d2/d62/classprototype_1_1Node.html#adc095cc5636da029d1e0d9cef8859701),
[prototype.Node::pprint()](../../d2/d62/classprototype_1_1Node.html#a5ae181c34e48238d2364b0ba4960c252),
and
[prototype.Node::pprint2()](../../d2/d62/classprototype_1_1Node.html#aaedcc4ba1fb305c7ddcc025235043cd5).

## ◆ component

[Expression::Component](../../d5/df9/structApp_1_1Expression_1_1Component.html)*
App::ExpressionParser::semantic_type::component  
---  
  
## ◆ components

std::deque<[ObjectIdentifier::Component](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html)>
App::ExpressionParser::semantic_type::components  
---  
  
## ◆

struct { ... } App::ExpressionParser::semantic_type::constant  
---  
  
## ◆ expr

[Expression](../../dc/d5c/classApp_1_1Expression.html)*
App::ExpressionParser::semantic_type::expr  
---  
  
## ◆ func

std::pair<[FunctionExpression::Function](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658),std::string>
App::ExpressionParser::semantic_type::func  
---  
  
## ◆ fvalue

double App::ExpressionParser::semantic_type::fvalue = 0  
---  
  
## ◆ ivalue

long long [int](../../d1/da0/classint.html)
App::ExpressionParser::semantic_type::ivalue  
---  
  
## ◆ list

std::vector<[Expression](../../dc/d5c/classApp_1_1Expression.html)*>
App::ExpressionParser::semantic_type::list  
---  
  
## ◆ name

const char* App::ExpressionParser::semantic_type::name = ""  
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

## ◆ path

[ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html)
App::ExpressionParser::semantic_type::path  
---  
  
Referenced by
[PathScripts.PathToolBitLibraryGui.ToolBitLibrary::librarySave()](../../dd/d3a/classPathScripts_1_1PathToolBitLibraryGui_1_1ToolBitLibrary.html#a78e1b668521bdf525ca26a7be60ac80e),
[PathScripts.PathToolBitLibraryGui.ToolBitLibrary::librarySaveAs()](../../dd/d3a/classPathScripts_1_1PathToolBitLibraryGui_1_1ToolBitLibrary.html#aacc6b835c3257775d5683ff5c4494b27),
and
[PathScripts.PathToolBitLibraryGui.ToolBitLibrary::loadData()](../../dd/d3a/classPathScripts_1_1PathToolBitLibraryGui_1_1ToolBitLibrary.html#ae2616669ba6b30e1833ff2d498cc2d6a).

## ◆

struct { ... } App::ExpressionParser::semantic_type::quantity  
---  
  
Referenced by
[automotive_design.quantified_assembly_component_usage::wr1()](../../d5/d9b/classautomotive__design_1_1quantified__assembly__component__usage.html#aed6cc3626acff4dc91ea150e4b3ddc3a),
and
[automotive_design.make_from_usage_option::wr1()](../../d9/d86/classautomotive__design_1_1make__from__usage__option.html#a32bfd0779e9f4db34925c1de0d9bf66a).

## ◆ scaler

[Base::Quantity](../../d8/d18/classBase_1_1Quantity.html)
App::ExpressionParser::semantic_type::scaler  
---  
  
## ◆ string

std::string App::ExpressionParser::semantic_type::string  
---  
  
Referenced by
[Spreadsheet_legacy.MathParser::hasNext()](../../d8/d8b/classSpreadsheet__legacy_1_1MathParser.html#a880d2d2a50b45fc7d1a43f93920d7543),
and
[Spreadsheet_legacy.MathParser::peek()](../../d8/d8b/classSpreadsheet__legacy_1_1MathParser.html#a56d2b8422c194d4440df5d1ae85e04ef).

## ◆ string_or_identifier

[ObjectIdentifier::String](../../dd/d98/classApp_1_1ObjectIdentifier_1_1String.html)
App::ExpressionParser::semantic_type::string_or_identifier  
---  
  
## ◆ unitStr

std::string App::ExpressionParser::semantic_type::unitStr  
---  
  
* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/App/ExpressionParser.h

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

