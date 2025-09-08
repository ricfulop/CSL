---
url: https://freecad.github.io/SourceDoc/d8/d7a/classBase_1_1LogLevel.html
scraped_at: 2025-09-08T15:16:35.909052
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [LogLevel](../../d8/d7a/classBase_1_1LogLevel.html)

[List of all members](../../dd/d0a/classBase_1_1LogLevel-members.html) | Public Member Functions | Public Attributes

Base::LogLevel Class Reference

[LogLevel](../../d8/d7a/classBase_1_1LogLevel.html "LogLevel helper class.")
helper class. [More...](../../d8/d7a/classBase_1_1LogLevel.html#details)

`#include <Console.h>`

##  Public Member Functions  
  
---  
[bool](../../d9/db9/classbool.html) | [isEnabled](../../d8/d7a/classBase_1_1LogLevel.html#a1a82ada58b6ae3335acc4d6cff2067c6) ([int](../../d1/da0/classint.html) l)  
[int](../../d1/da0/classint.html) | [level](../../d8/d7a/classBase_1_1LogLevel.html#a6ccb16622078cef5ac6af025f55923a3) () const  
|
[LogLevel](../../d8/d7a/classBase_1_1LogLevel.html#a8c1f2c084cd7319c16d6d928a2d1dfcd)
(const char
*[tag](../../d8/d7a/classBase_1_1LogLevel.html#a7f243c49d1c7a3f60506f97721cebe5e),
[bool](../../d9/db9/classbool.html)
[print_tag](../../d8/d7a/classBase_1_1LogLevel.html#af05d7518ff1a3151f16c1664fd4f8072)=true,
[int](../../d1/da0/classint.html)
[print_src](../../d8/d7a/classBase_1_1LogLevel.html#ac1f8ec0c4774d69c7d6a810b041ea28f)=0,
[bool](../../d9/db9/classbool.html)
[print_time](../../d8/d7a/classBase_1_1LogLevel.html#aec173fcd395b177d991309593be87d25)=false,
[bool](../../d9/db9/classbool.html)
[add_eol](../../d8/d7a/classBase_1_1LogLevel.html#a09293aed2a4aebfd3311edfed59f32a3)=true,
[bool](../../d9/db9/classbool.html)
[refresh](../../d8/d7a/classBase_1_1LogLevel.html#a207186af3bd8cde8f2dc21b1face3fd2)=false)  
std::stringstream & | [prefix](../../d8/d7a/classBase_1_1LogLevel.html#a6d01232a67a9688b17fecaf18f7d41e1) (std::stringstream &[str](../../d9/d36/classstr.html), const char *src, [int](../../d1/da0/classint.html) line)  
  
##  Public Attributes  
  
---  
[bool](../../d9/db9/classbool.html) | [add_eol](../../d8/d7a/classBase_1_1LogLevel.html#a09293aed2a4aebfd3311edfed59f32a3)  
[int](../../d1/da0/classint.html) & | [lvl](../../d8/d7a/classBase_1_1LogLevel.html#a5e58408664c25af0b72f53aa221da884)  
[int](../../d1/da0/classint.html) | [print_src](../../d8/d7a/classBase_1_1LogLevel.html#ac1f8ec0c4774d69c7d6a810b041ea28f)  
[bool](../../d9/db9/classbool.html) | [print_tag](../../d8/d7a/classBase_1_1LogLevel.html#af05d7518ff1a3151f16c1664fd4f8072)  
[bool](../../d9/db9/classbool.html) | [print_time](../../d8/d7a/classBase_1_1LogLevel.html#aec173fcd395b177d991309593be87d25)  
[bool](../../d9/db9/classbool.html) | [refresh](../../d8/d7a/classBase_1_1LogLevel.html#a207186af3bd8cde8f2dc21b1face3fd2)  
std::string | [tag](../../d8/d7a/classBase_1_1LogLevel.html#a7f243c49d1c7a3f60506f97721cebe5e)  
  
## Detailed Description

[LogLevel](../../d8/d7a/classBase_1_1LogLevel.html "LogLevel helper class.")
helper class.

## Constructor & Destructor Documentation

## ◆ LogLevel()

Base::LogLevel::LogLevel  | ( | const char *  | _tag_ ,   
---|---|---|---  
|  | [bool](../../d9/db9/classbool.html) | _print_tag_ = `true`,   
|  | [int](../../d1/da0/classint.html) | _print_src_ = `0`,   
|  | [bool](../../d9/db9/classbool.html) | _print_time_ = `false`,   
|  | [bool](../../d9/db9/classbool.html) | _add_eol_ = `true`,   
|  | [bool](../../d9/db9/classbool.html) | _refresh_ = `false`  
| ) | |   
  
## Member Function Documentation

## ◆ isEnabled()

[bool](../../d9/db9/classbool.html) Base::LogLevel::isEnabled  | ( | [int](../../d1/da0/classint.html) | _l_| ) |   
---|---|---|---|---|---  
  
Referenced by
[draftguitools.gui_snapper.Snapper::setArchDims()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#afc73b5c84f318a3a47a0e64301e29247),
[draftguitools.gui_snapper.Snapper::snapToAngles()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#a8bd58fe1d7c754dd4fd5968f67072a93),
[draftguitools.gui_snapper.Snapper::snapToCenter()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#a5e21123330ac04a1c88c35450c7d6e45),
[draftguitools.gui_snapper.Snapper::snapToCenterFace()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#ae2e7de8ed53fbfd8c824bb822ea688fb),
[draftguitools.gui_snapper.Snapper::snapToCrossExtensions()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#acee40380387892206a064e5b4b878275),
[draftguitools.gui_snapper.Snapper::snapToElines()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#a8f1b7e3457e225dd4dcb2dac341f0c41),
[draftguitools.gui_snapper.Snapper::snapToEndpoints()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#ad38fed6fa78da1aef31deefb69ca1922),
[draftguitools.gui_snapper.Snapper::snapToExtensions()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#ae1f59975a9ed59a52c5c72b11a89e8c3),
[draftguitools.gui_snapper.Snapper::snapToExtOrtho()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#a2a9a200849141003e5be747ada4c4374),
[draftguitools.gui_snapper.Snapper::snapToExtPerpendicular()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#a71ff5dbb89eff26bc03c68957d66537a),
[draftguitools.gui_snapper.Snapper::snapToGrid()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#ad33d36f945a15ec39fba7d0d5184dfbc),
[draftguitools.gui_snapper.Snapper::snapToHold()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#a6db0f4aacea9c6e9501927b7c0e3235c),
[draftguitools.gui_snapper.Snapper::snapToIntersection()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#a43d4ae56da45a12afec22a53ae97cc74),
[draftguitools.gui_snapper.Snapper::snapToMidpoint()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#a5ebebdc5bf65d99c1b2bfca4f0e3de65),
[draftguitools.gui_snapper.Snapper::snapToNear()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#acea18aa0a1778d9fcefa86a01d33dabf),
[draftguitools.gui_snapper.Snapper::snapToNearFace()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#a9f8f81d85b83328d136b0eafd9ec3950),
[draftguitools.gui_snapper.Snapper::snapToObject()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#a2c5eb552fed1dc7a61c628dc393ae869),
[draftguitools.gui_snapper.Snapper::snapToOrtho()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#ab98374e00b2c719ed3331a2c4b3afe29),
[draftguitools.gui_snapper.Snapper::snapToPerpendicular()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#af64c2d0a3df89214c36dbe93423147f6),
[draftguitools.gui_snapper.Snapper::snapToPerpendicularFace()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#a5bb701a695185f8fed89490cd0532936),
[draftguitools.gui_snapper.Snapper::snapToPolar()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#a5a30c9877875867157703325b090e21f),
[draftguitools.gui_snapper.Snapper::snapToPolygon()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#afe31e4ec19118e3c7bd0c85efd6fdfce),
[draftguitools.gui_snapper.Snapper::snapToSpecials()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#acf474608c7500cd7fbf50ba8ae6fa808),
[draftguitools.gui_snapper.Snapper::snapToVertex()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#aff36d8b552b2a47683e8758bc0d73556),
and
[draftguitools.gui_snapper.Snapper::toWP()](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#a8477ccc10f74707df160dcec8b70124b).

## ◆ level()

[int](../../d1/da0/classint.html) Base::LogLevel::level  | ( | | ) |  const  
---|---|---|---|---  
  
References
[Base::Console()](../../db/d07/namespaceBase.html#a968fb30e59145eaaa8b1da98680bd729),
and
[Base::ConsoleSingleton::LogLevel()](../../df/dca/classBase_1_1ConsoleSingleton.html#a90e43022cf609ba385f4c05ecebad58d).

## ◆ prefix()

std::stringstream & LogLevel::prefix  | ( | std::stringstream & | _str_ ,   
---|---|---|---  
|  | const char *  | _src_ ,   
|  | [int](../../d1/da0/classint.html) | _line_  
| ) | |   
  
References
[print_src](../../d8/d7a/classBase_1_1LogLevel.html#ac1f8ec0c4774d69c7d6a810b041ea28f),
[print_tag](../../d8/d7a/classBase_1_1LogLevel.html#af05d7518ff1a3151f16c1664fd4f8072),
[print_time](../../d8/d7a/classBase_1_1LogLevel.html#aec173fcd395b177d991309593be87d25),
and
[tag](../../d8/d7a/classBase_1_1LogLevel.html#a7f243c49d1c7a3f60506f97721cebe5e).

Referenced by
[automotive_design.si_unit::wr1()](../../d5/d77/classautomotive__design_1_1si__unit.html#a11f3f199cb57673aba404a85f4e7b2d8).

## Member Data Documentation

## ◆ add_eol

[bool](../../d9/db9/classbool.html) Base::LogLevel::add_eol  
---  
  
## ◆ lvl

[int](../../d1/da0/classint.html)& Base::LogLevel::lvl  
---  
  
## ◆ print_src

[int](../../d1/da0/classint.html) Base::LogLevel::print_src  
---  
  
Referenced by
[prefix()](../../d8/d7a/classBase_1_1LogLevel.html#a6d01232a67a9688b17fecaf18f7d41e1).

## ◆ print_tag

[bool](../../d9/db9/classbool.html) Base::LogLevel::print_tag  
---  
  
Referenced by
[prefix()](../../d8/d7a/classBase_1_1LogLevel.html#a6d01232a67a9688b17fecaf18f7d41e1).

## ◆ print_time

[bool](../../d9/db9/classbool.html) Base::LogLevel::print_time  
---  
  
Referenced by
[prefix()](../../d8/d7a/classBase_1_1LogLevel.html#a6d01232a67a9688b17fecaf18f7d41e1).

## ◆ refresh

[bool](../../d9/db9/classbool.html) Base::LogLevel::refresh  
---  
  
Referenced by
[PathScripts.PathToolBitEdit.ToolBitEditor::accept()](../../d6/d36/classPathScripts_1_1PathToolBitEdit_1_1ToolBitEditor.html#a86ad4f706046e1634bf67ceb587e5a27),
[PathScripts.PathToolEdit.ToolEditor::accept()](../../d2/df8/classPathScripts_1_1PathToolEdit_1_1ToolEditor.html#a869c5580bbfbe7addd963c5de1c9fb1f),
[PathScripts.PathToolBitEdit.ToolBitEditor::setupUI()](../../d6/d36/classPathScripts_1_1PathToolBitEdit_1_1ToolBitEditor.html#ac6ca422dac09ad140db418319c2c05e2),
[PathScripts.PathToolControllerGui.ToolControllerEditor::setupUi()](../../d2/db6/classPathScripts_1_1PathToolControllerGui_1_1ToolControllerEditor.html#ac65d1c5c0d0e29af0184084c6b0924e7),
and
[PathScripts.PathToolEdit.ToolEditor::setupUI()](../../d2/df8/classPathScripts_1_1PathToolEdit_1_1ToolEditor.html#a1f8ad48742a24a6b9a1d1b0ce191252f).

## ◆ tag

std::string Base::LogLevel::tag  
---  
  
Referenced by
[PathScripts.PathDressupHoldingTags.MapWireToTag::add()](../../dd/dd7/classPathScripts_1_1PathDressupHoldingTags_1_1MapWireToTag.html#a635a31c3648c89f099d5fe6f97368237),
[PathScripts.PathDressupHoldingTags.MapWireToTag::cleanupEdges()](../../dd/dd7/classPathScripts_1_1PathDressupHoldingTags_1_1MapWireToTag.html#ad67774cf1b6aa1f4bb6bc52fa932df83),
[PathScripts.PathDressupHoldingTags.MapWireToTag::commandsForEdges()](../../dd/dd7/classPathScripts_1_1PathDressupHoldingTags_1_1MapWireToTag.html#a198fbf1f749b551d10e292784e5921cf),
[Dice3DS.dom3ds.ChunkBase::document_html()](../../da/da5/classDice3DS_1_1dom3ds_1_1ChunkBase.html#abdc79325208ba093e3b508c646b3a4ba),
[Dice3DS.dom3ds.ChunkBase::dump_header()](../../da/da5/classDice3DS_1_1dom3ds_1_1ChunkBase.html#a64b07f8bfad61e851b2c2fb3c2974d9a),
[ArchPanel.PanelCut::getWires()](../../d6/dbd/classArchPanel_1_1PanelCut.html#a61534af5c2a0125dde05e08a22025195),
[prefix()](../../d8/d7a/classBase_1_1LogLevel.html#a6d01232a67a9688b17fecaf18f7d41e1),
[PathScripts.PathDressupHoldingTags.MapWireToTag::shell()](../../dd/dd7/classPathScripts_1_1PathDressupHoldingTags_1_1MapWireToTag.html#a2f0df7770665a77dc3ec39aad49a7a58),
and
[FreeCADInit.FCADLogger::trace()](../../d2/d1e/classFreeCADInit_1_1FCADLogger.html#a9e5cc4f866ef7f6e4699ad1b481d7879).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/Base/Console.h
  * FreeCAD/src/Base/ConsoleObserver.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

