---
url: https://freecad.github.io/SourceDoc/d3/d96/classCommands_1_1SphereCreator.html
scraped_at: 2025-09-08T15:19:33.700147
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Commands](../../da/d2d/namespaceCommands.html)
  * [SphereCreator](../../d3/d96/classCommands_1_1SphereCreator.html)

[List of all members](../../d3/dbf/classCommands_1_1SphereCreator-members.html) | Public Member Functions | Public Attributes

Commands.SphereCreator Class Reference

##  Public Member Functions  
  
---  
def | [create](../../d3/d96/classCommands_1_1SphereCreator.html#a883a01e86dd4330a4d6e5bbb28cdc226) (self, info)  
def | [enter](../../d3/d96/classCommands_1_1SphereCreator.html#ae5b24979792d6df49166c303bac5e35e) (self)  
def | [exit](../../d3/d96/classCommands_1_1SphereCreator.html#a063ea748fef14a096b19022231b8ade7) (self, info)  
def | [leave](../../d3/d96/classCommands_1_1SphereCreator.html#afa6deb8b50c7d0fb04a44305664e0b59) (self)  
  
##  Public Attributes  
  
---  
|
[av](../../d3/d96/classCommands_1_1SphereCreator.html#ad7947752d4ce77f11c52ae39be6d63a7)  
|
[cb](../../d3/d96/classCommands_1_1SphereCreator.html#a222f6d32ead74c727a1936def421f6c8)  
|
[ex](../../d3/d96/classCommands_1_1SphereCreator.html#a68b850641adc01b51c4806714eb3584f)  
|
[mode](../../d3/d96/classCommands_1_1SphereCreator.html#a786d7d1f4d3369798c28e9ed094841f1)  
|
[pt](../../d3/d96/classCommands_1_1SphereCreator.html#a75d4f6db49e0debfa869c971ecc9998b)  
  
## Member Function Documentation

## ◆ create()

def Commands.SphereCreator.create  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _info_  
| ) | |   
  
References
[Commands.SphereCreator.av](../../d3/d96/classCommands_1_1SphereCreator.html#ad7947752d4ce77f11c52ae39be6d63a7),
[draftguitools.gui_tool_utils.getPoint](../../db/d6d/group__draftguitools.html#gadee75025c45db326c9f3be5a22f96eaf),
[draftguitools.gui_snapper.Snapper.pt](../../d9/de9/classdraftguitools_1_1gui__snapper_1_1Snapper.html#a1a8587e2d246e5f3a67b462c2c89ed9d),
[draftviewproviders.view_wire.ViewProviderWire.pt](../../da/dd2/classdraftviewproviders_1_1view__wire_1_1ViewProviderWire.html#a1b1c9195ce27f205df5cd92736e0ecdb),
[WireJoiner::VertexInfo.pt()](../../de/daa/structWireJoiner_1_1VertexInfo.html#a0f8b95c715e4de169ed17ef1c96a2245),
[PathScripts.PathDressupDogbone.Marker.pt](../../d9/dd1/classPathScripts_1_1PathDressupDogbone_1_1Marker.html#a3d2b3e2cd9145ddc1702632cce7decd1),
[PathScripts.PathDressupTagGui.PathDressupTagTaskPanel.pt](../../d9/d7b/classPathScripts_1_1PathDressupTagGui_1_1PathDressupTagTaskPanel.html#a44ef627446fcaf266b3de41aef5d47e9),
[PathScripts.PathGetPoint.TaskPanel.pt](../../d8/d28/classPathScripts_1_1PathGetPoint_1_1TaskPanel.html#a5a83ce88ef048e74b70a2f7bf4fabd82),
and
[Commands.SphereCreator.pt](../../d3/d96/classCommands_1_1SphereCreator.html#a75d4f6db49e0debfa869c971ecc9998b).

Referenced by
[draftguitools.gui_labels.Label.action()](../../d4/d3a/classdraftguitools_1_1gui__labels_1_1Label.html#a31d95b9c0428e8e5e2fc2c0e5ba1f9cf).

## ◆ enter()

def Commands.SphereCreator.enter  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References Base::gzstreambuf.mode,
[Gui::FileChooser.mode](../../d3/de4/classGui_1_1FileChooser.html#a70902b233736fd75a243b67bf9bc222a),
[Gui::SoSkipBoundingGroup.mode](../../d4/d8e/classGui_1_1SoSkipBoundingGroup.html#a7c30e76c4e037c7342a65590a83a84cf),
[draftguitools.gui_offset.Offset.mode](../../d8/ddd/classdraftguitools_1_1gui__offset_1_1Offset.html#a9bed863d42929e3dddb59c901b4eed82),
[draftguitools.gui_trackers.archDimTracker.mode](../../df/d81/classdraftguitools_1_1gui__trackers_1_1archDimTracker.html#a073b4b49fbde09e3e9f1975e048d8f42),
[ifc2x3.ifctexturecoordinategenerator.mode](../../d6/daf/classifc2x3_1_1ifctexturecoordinategenerator.html#a69ec296e4345f543305f35ed696cd909),
[ifc4.ifcsurfacetexture.mode](../../d2/dec/classifc4_1_1ifcsurfacetexture.html#aefb7f7d283453f3046c63d7935ca5858),
[ifc4.ifctexturecoordinategenerator.mode](../../d9/d5b/classifc4_1_1ifctexturecoordinategenerator.html#a809d1f110c539e54fd4aa19993f5d3c3),
Import::ImportOCAF2.mode,
[gzip_utf8.GzipFile.mode](../../d2/dbe/classgzip__utf8_1_1GzipFile.html#a7da072db1626eef38982980be74ec06f),
PartGui::Location.mode,
[PartGui::ShapeSelection.mode](../../d2/d24/classPartGui_1_1ShapeSelection.html#a0e53daefeb3a306ac5f08454baf047e9),
[CAreaPocketParams.mode](../../dd/d2a/structCAreaPocketParams.html#a8525fa44bbb9dede8c7a2c9a3c3bc385),
SketcherGui::DrawSketchHandlerEllipse.mode,
SurfaceGui::FillingPanel::ShapeSelection.mode,
SurfaceGui::FillingEdgePanel::ShapeSelection.mode,
SurfaceGui::FillingVertexPanel::VertexSelection.mode,
SurfaceGui::SectionsPanel::ShapeSelection.mode, and
[Commands.SphereCreator.mode](../../d3/d96/classCommands_1_1SphereCreator.html#a786d7d1f4d3369798c28e9ed094841f1).

## ◆ exit()

def Commands.SphereCreator.exit  | ( |  | _self_ ,   
---|---|---|---  
|  |  | _info_  
| ) | |   
  
References
[Commands.SphereCreator.leave()](../../d3/d96/classCommands_1_1SphereCreator.html#afa6deb8b50c7d0fb04a44305664e0b59).

Referenced by
[PathScripts.PathDressupHoldingTags.MapWireToTag.add()](../../dd/dd7/classPathScripts_1_1PathDressupHoldingTags_1_1MapWireToTag.html#a635a31c3648c89f099d5fe6f97368237),
[PathScripts.PathDressupHoldingTags.MapWireToTag.cleanupEdges()](../../dd/dd7/classPathScripts_1_1PathDressupHoldingTags_1_1MapWireToTag.html#ad67774cf1b6aa1f4bb6bc52fa932df83),
[PathScripts.PathDressupHoldingTags.MapWireToTag.isEntryOrExitStrut()](../../dd/dd7/classPathScripts_1_1PathDressupHoldingTags_1_1MapWireToTag.html#a00604413eda3d6379b5b81511110b4f3),
and
[PathScripts.PathDressupHoldingTags.MapWireToTag.orderAndFlipEdges()](../../dd/dd7/classPathScripts_1_1PathDressupHoldingTags_1_1MapWireToTag.html#ab12d7dbae1777316e69045e8d3129339).

## ◆ leave()

def Commands.SphereCreator.leave  | ( |  | _self_| ) |   
---|---|---|---|---|---  
  
References
[Commands.SphereCreator.av](../../d3/d96/classCommands_1_1SphereCreator.html#ad7947752d4ce77f11c52ae39be6d63a7),
[PathScripts.PathToolLibraryEditor.EditorPanel.cb](../../d0/d92/classPathScripts_1_1PathToolLibraryEditor_1_1EditorPanel.html#a436ac1c149cbc14609175dbe73828ac4),
[Commands.SphereCreator.cb](../../d3/d96/classCommands_1_1SphereCreator.html#a222f6d32ead74c727a1936def421f6c8),
[Commands.SphereCreator.ex](../../d3/d96/classCommands_1_1SphereCreator.html#a68b850641adc01b51c4806714eb3584f),
Base::gzstreambuf.mode,
[Gui::FileChooser.mode](../../d3/de4/classGui_1_1FileChooser.html#a70902b233736fd75a243b67bf9bc222a),
[Gui::SoSkipBoundingGroup.mode](../../d4/d8e/classGui_1_1SoSkipBoundingGroup.html#a7c30e76c4e037c7342a65590a83a84cf),
[draftguitools.gui_offset.Offset.mode](../../d8/ddd/classdraftguitools_1_1gui__offset_1_1Offset.html#a9bed863d42929e3dddb59c901b4eed82),
[draftguitools.gui_trackers.archDimTracker.mode](../../df/d81/classdraftguitools_1_1gui__trackers_1_1archDimTracker.html#a073b4b49fbde09e3e9f1975e048d8f42),
[ifc2x3.ifctexturecoordinategenerator.mode](../../d6/daf/classifc2x3_1_1ifctexturecoordinategenerator.html#a69ec296e4345f543305f35ed696cd909),
[ifc4.ifcsurfacetexture.mode](../../d2/dec/classifc4_1_1ifcsurfacetexture.html#aefb7f7d283453f3046c63d7935ca5858),
[ifc4.ifctexturecoordinategenerator.mode](../../d9/d5b/classifc4_1_1ifctexturecoordinategenerator.html#a809d1f110c539e54fd4aa19993f5d3c3),
Import::ImportOCAF2.mode,
[gzip_utf8.GzipFile.mode](../../d2/dbe/classgzip__utf8_1_1GzipFile.html#a7da072db1626eef38982980be74ec06f),
PartGui::Location.mode,
[PartGui::ShapeSelection.mode](../../d2/d24/classPartGui_1_1ShapeSelection.html#a0e53daefeb3a306ac5f08454baf047e9),
[CAreaPocketParams.mode](../../dd/d2a/structCAreaPocketParams.html#a8525fa44bbb9dede8c7a2c9a3c3bc385),
SketcherGui::DrawSketchHandlerEllipse.mode,
SurfaceGui::FillingPanel::ShapeSelection.mode,
SurfaceGui::FillingEdgePanel::ShapeSelection.mode,
SurfaceGui::FillingVertexPanel::VertexSelection.mode,
SurfaceGui::SectionsPanel::ShapeSelection.mode, and
[Commands.SphereCreator.mode](../../d3/d96/classCommands_1_1SphereCreator.html#a786d7d1f4d3369798c28e9ed094841f1).

Referenced by
[Commands.SphereCreator.exit()](../../d3/d96/classCommands_1_1SphereCreator.html#a063ea748fef14a096b19022231b8ade7).

## Member Data Documentation

## ◆ av

Commands.SphereCreator.av  
---  
  
Referenced by
[Commands.SphereCreator.create()](../../d3/d96/classCommands_1_1SphereCreator.html#a883a01e86dd4330a4d6e5bbb28cdc226),
and
[Commands.SphereCreator.leave()](../../d3/d96/classCommands_1_1SphereCreator.html#afa6deb8b50c7d0fb04a44305664e0b59).

## ◆ cb

Commands.SphereCreator.cb  
---  
  
Referenced by
[PathScripts.PathToolLibraryEditor.EditorPanel.copyTools()](../../d0/d92/classPathScripts_1_1PathToolLibraryEditor_1_1EditorPanel.html#a7a220589b29f57010e038397eed16a6e),
and
[Commands.SphereCreator.leave()](../../d3/d96/classCommands_1_1SphereCreator.html#afa6deb8b50c7d0fb04a44305664e0b59).

## ◆ ex

Commands.SphereCreator.ex  
---  
  
Referenced by
[Commands.SphereCreator.leave()](../../d3/d96/classCommands_1_1SphereCreator.html#afa6deb8b50c7d0fb04a44305664e0b59).

## ◆ mode

Commands.SphereCreator.mode  
---  
  
Referenced by
[draftguitools.gui_offset.Offset.action()](../../d8/ddd/classdraftguitools_1_1gui__offset_1_1Offset.html#af6fe1d529ed82fe117bb430a75844ec5),
[gzip_utf8.GzipFile.close()](../../d2/dbe/classgzip__utf8_1_1GzipFile.html#a5c40910b0ce0286256128c6dae8a2c9b),
[Commands.SphereCreator.enter()](../../d3/d96/classCommands_1_1SphereCreator.html#ae5b24979792d6df49166c303bac5e35e),
[gzip_utf8.GzipFile.filename()](../../d2/dbe/classgzip__utf8_1_1GzipFile.html#ab56fe84a4eb08c44e7a0026280c01229),
[gzip_utf8.GzipFile.flush()](../../d2/dbe/classgzip__utf8_1_1GzipFile.html#ae5623fe01da68b05e54f3855e0ef26bc),
[Commands.SphereCreator.leave()](../../d3/d96/classCommands_1_1SphereCreator.html#afa6deb8b50c7d0fb04a44305664e0b59),
[draftguitools.gui_offset.Offset.numericRadius()](../../d8/ddd/classdraftguitools_1_1gui__offset_1_1Offset.html#ae08617dcd80297f9e33139b0cfb5589f),
[gzip_utf8.GzipFile.read()](../../d2/dbe/classgzip__utf8_1_1GzipFile.html#a1997270eadc9247814e6a68f6a8a3ba1),
[gzip_utf8.GzipFile.readable()](../../d2/dbe/classgzip__utf8_1_1GzipFile.html#a21bb7341b2bda31a03e6e605fbf504ab),
[gzip_utf8.GzipFile.rewind()](../../d2/dbe/classgzip__utf8_1_1GzipFile.html#aee93e6718f3bf10452ff5254970d7886),
[gzip_utf8.GzipFile.seek()](../../d2/dbe/classgzip__utf8_1_1GzipFile.html#ac5b53848e16b6ba800ed9ac8d3f737c3),
[draftguitools.gui_trackers.archDimTracker.setString()](../../df/d81/classdraftguitools_1_1gui__trackers_1_1archDimTracker.html#a9959440fd5125f6e431706300d55e79c),
[gzip_utf8.GzipFile.writable()](../../d2/dbe/classgzip__utf8_1_1GzipFile.html#a7adb1a84422e54a6481809a7547c176f),
and
[gzip_utf8.GzipFile.write()](../../d2/dbe/classgzip__utf8_1_1GzipFile.html#a3148c5b71cccbdfce05d52d31114810e).

## ◆ pt

Commands.SphereCreator.pt  
---  
  
Referenced by
[Commands.SphereCreator.create()](../../d3/d96/classCommands_1_1SphereCreator.html#a883a01e86dd4330a4d6e5bbb28cdc226),
[PathScripts.PathGetPoint.TaskPanel.getPoint()](../../d8/d28/classPathScripts_1_1PathGetPoint_1_1TaskPanel.html#a887ab8742a503f9a0c4c177498f518f4),
[draftviewproviders.view_wire.ViewProviderWire.onChanged()](../../da/dd2/classdraftviewproviders_1_1view__wire_1_1ViewProviderWire.html#a45511b113b62eba083c491b40c7fe3e8),
[PathScripts.PathGetPoint.TaskPanel.pointFinish()](../../d8/d28/classPathScripts_1_1PathGetPoint_1_1TaskPanel.html#a66a2e82f61a502b21a93fb058cb15e2e),
and
[PathScripts.PathGetPoint.TaskPanel.updatePoint()](../../d8/d28/classPathScripts_1_1PathGetPoint_1_1TaskPanel.html#a803c8c22e7d07808de83c36eac90d91f).

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Mod/TemplatePyMod/Commands.py

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

