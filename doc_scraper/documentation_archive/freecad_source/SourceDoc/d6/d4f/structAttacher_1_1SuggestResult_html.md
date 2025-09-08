---
url: https://freecad.github.io/SourceDoc/d6/d4f/structAttacher_1_1SuggestResult.html
scraped_at: 2025-09-08T14:58:49.459142
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Attacher](../../d2/d62/namespaceAttacher.html)
  * [SuggestResult](../../d6/d4f/structAttacher_1_1SuggestResult.html)

[List of all members](../../da/d8a/structAttacher_1_1SuggestResult-members.html) | Public Types | Public Attributes

Attacher::SuggestResult Struct Reference

The [SuggestResult](../../d6/d4f/structAttacher_1_1SuggestResult.html "The
SuggestResult struct is a container for output information of AttachEngine
mode suggesting routin...") struct is a container for output information of
[AttachEngine](../../d2/d85/classAttacher_1_1AttachEngine.html "The
AttachEngine class is the placement calculation routine, modes, hints and so
on.") mode suggesting routine.
[More...](../../d6/d4f/structAttacher_1_1SuggestResult.html#details)

`#include <Attacher.h>`

##  Public Types  
  
---  
enum | [eSuggestResult](../../d6/d4f/structAttacher_1_1SuggestResult.html#aafe8cf61ae39477fc953a35da1e8df0e) {   
[srOK](../../d6/d4f/structAttacher_1_1SuggestResult.html#aafe8cf61ae39477fc953a35da1e8df0ea072ce366fcfb69c28680b9673c3f765d)
,
[srLinkBroken](../../d6/d4f/structAttacher_1_1SuggestResult.html#aafe8cf61ae39477fc953a35da1e8df0ea01ae847eda7c703e82a60b7795913123)
,
[srUnexpectedError](../../d6/d4f/structAttacher_1_1SuggestResult.html#aafe8cf61ae39477fc953a35da1e8df0eaa360684672c8456a7b9d4afe2a13e5e7)
,
[srNoModesFit](../../d6/d4f/structAttacher_1_1SuggestResult.html#aafe8cf61ae39477fc953a35da1e8df0eaea3cb6f66abac565559cb3437ab1bfee)
,  
[srIncompatibleGeometry](../../d6/d4f/structAttacher_1_1SuggestResult.html#aafe8cf61ae39477fc953a35da1e8df0ea205b288c2244f00b6759c8cb9b20980c)  
}  
| message contains overall verdict of suggestor on current reference set
[More...](../../d6/d4f/structAttacher_1_1SuggestResult.html#aafe8cf61ae39477fc953a35da1e8df0e)  
  
  
##  Public Attributes  
  
---  
std::vector< [eMapMode](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82) > | [allApplicableModes](../../d6/d4f/structAttacher_1_1SuggestResult.html#a2b53686a980fb5e70f23b46df970c274)  
| allApplicableModes.
[More...](../../d6/d4f/structAttacher_1_1SuggestResult.html#a2b53686a980fb5e70f23b46df970c274)  
  
[eMapMode](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82) | [bestFitMode](../../d6/d4f/structAttacher_1_1SuggestResult.html#a41713e84809db40031ff1a5635ed90ba)  
| bestFitMode is the mode that is the most specific to current references.
[More...](../../d6/d4f/structAttacher_1_1SuggestResult.html#a41713e84809db40031ff1a5635ed90ba)  
  
[Base::RuntimeError](../../db/d57/classBase_1_1RuntimeError.html) | [error](../../d6/d4f/structAttacher_1_1SuggestResult.html#aadeab6c862d197962f42938354aa1362)  
[eSuggestResult](../../d6/d4f/structAttacher_1_1SuggestResult.html#aafe8cf61ae39477fc953a35da1e8df0e) | [message](../../d6/d4f/structAttacher_1_1SuggestResult.html#ab2b1b860a530404df8eec712ff873ce9)  
std::set< [eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738) > | [nextRefTypeHint](../../d6/d4f/structAttacher_1_1SuggestResult.html#a1f1f3ffbadebe645b5bc7ff89e12dc10)  
| nextRefTypeHint: a hint of what can be added to references to achieve other
modes.
[More...](../../d6/d4f/structAttacher_1_1SuggestResult.html#a1f1f3ffbadebe645b5bc7ff89e12dc10)  
  
std::map< [eMapMode](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82), [refTypeStringList](../../d2/d62/namespaceAttacher.html#a1e956a433ed003aff07cf368d39f79ba) > | [reachableModes](../../d6/d4f/structAttacher_1_1SuggestResult.html#a2e4e2b9b847adf72af09a9678d45d94e)  
| reachableModes.
[More...](../../d6/d4f/structAttacher_1_1SuggestResult.html#a2e4e2b9b847adf72af09a9678d45d94e)  
  
[refTypeString](../../d2/d62/namespaceAttacher.html#ab10eb3fb47de29cebdefbedf740a4849) | [references_Types](../../d6/d4f/structAttacher_1_1SuggestResult.html#aa5016813324f848cc4b65669d625d3b8)  
| references_Types: list of types of references, as queried when running
suggesting routine.
[More...](../../d6/d4f/structAttacher_1_1SuggestResult.html#aa5016813324f848cc4b65669d625d3b8)  
  
  
## Detailed Description

The [SuggestResult](../../d6/d4f/structAttacher_1_1SuggestResult.html "The
SuggestResult struct is a container for output information of AttachEngine
mode suggesting routin...") struct is a container for output information of
[AttachEngine](../../d2/d85/classAttacher_1_1AttachEngine.html "The
AttachEngine class is the placement calculation routine, modes, hints and so
on.") mode suggesting routine.

## Member Enumeration Documentation

## ◆ eSuggestResult

enum
[Attacher::SuggestResult::eSuggestResult](../../d6/d4f/structAttacher_1_1SuggestResult.html#aafe8cf61ae39477fc953a35da1e8df0e)  
---  
  
message contains overall verdict of suggestor on current reference set

Enumerator  
---  
srOK |   
srLinkBroken |   
srUnexpectedError |   
srNoModesFit |   
srIncompatibleGeometry |   
  
## Member Data Documentation

## ◆ allApplicableModes

std::vector<[eMapMode](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82)>
Attacher::SuggestResult::allApplicableModes  
---  
  
allApplicableModes.

Vector array that will receive the list of all modes that are applicable to
current set of references. It doesn't guarantee that all modes will work, it
only checks that subelemnts are of right type.

Referenced by
[SketcherGui::SuggestAutoMapMode()](../../d6/d44/namespaceSketcherGui.html#a21c0eeb3a6a37afe433d190fc7a22c18).

## ◆ bestFitMode

[eMapMode](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82)
Attacher::SuggestResult::bestFitMode  
---  
  
bestFitMode is the mode that is the most specific to current references.

Note that the mode may not be valid for current references; check if it's
listed in allApplicableModes, or test if message == srOK.

Referenced by
[PartGui::TaskAttacher::getActiveMapMode()](../../df/d45/classPartGui_1_1TaskAttacher.html#a8f9f3aff4d0d9699ef0fa0484f4407a3),
and
[SketcherGui::SuggestAutoMapMode()](../../d6/d44/namespaceSketcherGui.html#a21c0eeb3a6a37afe433d190fc7a22c18).

## ◆ error

[Base::RuntimeError](../../db/d57/classBase_1_1RuntimeError.html)
Attacher::SuggestResult::error  
---  
  
Referenced by
[femmesh.gmshtools.GmshTools::read_and_set_new_mesh()](../../d9/d7b/classfemmesh_1_1gmshtools_1_1GmshTools.html#a5ef3ad4b8ff477c0c3b13c11b9a9062e),
[FreeCADInit.FCADLogger::report()](../../d2/d1e/classFreeCADInit_1_1FCADLogger.html#a53ca47c23bb6061489b47ab9c2e19512),
and
[femmesh.gmshtools.GmshTools::run_gmsh_with_geo()](../../d9/d7b/classfemmesh_1_1gmshtools_1_1GmshTools.html#a37e8a08f6afd2d35a718d51070fd4f35).

## ◆ message

[eSuggestResult](../../d6/d4f/structAttacher_1_1SuggestResult.html#aafe8cf61ae39477fc953a35da1e8df0e)
Attacher::SuggestResult::message  
---  
  
Referenced by
[PartGui::TaskAttacher::getActiveMapMode()](../../df/d45/classPartGui_1_1TaskAttacher.html#a8f9f3aff4d0d9699ef0fa0484f4407a3),
[SketcherGui::SuggestAutoMapMode()](../../d6/d44/namespaceSketcherGui.html#a21c0eeb3a6a37afe433d190fc7a22c18),
and
[addonmanager_workers.GitProgressMonitor::update()](../../d9/da2/classaddonmanager__workers_1_1GitProgressMonitor.html#a792da2433df991c6af7f84aa5d557918).

## ◆ nextRefTypeHint

std::set<[eRefType](../../d2/d62/namespaceAttacher.html#ac788788c72a3396c7aa2b53398579738)>
Attacher::SuggestResult::nextRefTypeHint  
---  
  
nextRefTypeHint: a hint of what can be added to references to achieve other
modes.

## ◆ reachableModes

std::map<[eMapMode](../../d2/d62/namespaceAttacher.html#a4f0174280b63a9c200fad27ade65ce82),
[refTypeStringList](../../d2/d62/namespaceAttacher.html#a1e956a433ed003aff07cf368d39f79ba)>
Attacher::SuggestResult::reachableModes  
---  
  
reachableModes.

List of modes that can be reached by selecting more references. Is a map,
where key is the mode that can be reached, and value is a list of reference
sequences that can be added to reach the mode (stuff already linked is omitted
from these lists; only extra links needed are listed)

## ◆ references_Types

[refTypeString](../../d2/d62/namespaceAttacher.html#ab10eb3fb47de29cebdefbedf740a4849)
Attacher::SuggestResult::references_Types  
---  
  
references_Types: list of types of references, as queried when running
suggesting routine.

* * *

The documentation for this struct was generated from the following file:

  * FreeCAD/src/Mod/Part/App/Attacher.h

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

