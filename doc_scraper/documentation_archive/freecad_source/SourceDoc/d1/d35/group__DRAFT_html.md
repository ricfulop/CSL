---
url: https://freecad.github.io/SourceDoc/d1/d35/group__DRAFT.html
scraped_at: 2025-09-08T14:51:57.793965
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

Namespaces | Modules | Variables

Draft

[Workbenches](../../d2/df2/group__WORKBENCHES.html) » [Python
workbenches](../../d1/d82/group__PYTHONWORKBENCHES.html)

Basic 2D drawing tools and other generic tools. More...

##  Namespaces  
  
---  
namespace | [DraftFillet](../../da/d91/namespaceDraftFillet.html)  
| Provides [Fillet](../../d4/db1/classDraftFillet_1_1Fillet.html) class for
objects created with a prototype version.  
  
namespace | [DraftGui](../../da/d99/namespaceDraftGui.html)  
| GUI elements and utilities of the [Draft](../../d4/d1a/namespaceDraft.html)
workbench.  
  
namespace | [DraftLayer](../../df/dc2/namespaceDraftLayer.html)  
| Provides the Layer object.  
  
namespace | [DraftTools](../../d7/d3a/namespaceDraftTools.html)  
| Provide GUI commands of the [Draft](../../d4/d1a/namespaceDraft.html)
workbench.  
  
namespace | [importAirfoilDAT](../../d8/dc7/namespaceimportAirfoilDAT.html)  
| Airfoil (.dat) file importer.  
  
namespace | [importDWG](../../d7/d18/namespaceimportDWG.html)  
| DWG file importer & exporter.  
  
namespace | [importDXF](../../d7/dbf/namespaceimportDXF.html)  
| DXF file importer & exporter.  
  
namespace | [importOCA](../../df/d03/namespaceimportOCA.html)  
| OCA (Open CAD Format) file importer & exporter.  
  
namespace | [importSVG](../../d1/d33/namespaceimportSVG.html)  
| SVG file importer and exporter.  
  
namespace | [WorkingPlane](../../d8/d4a/namespaceWorkingPlane.html)  
| This module handles the Working
[Plane](../../d3/d93/classWorkingPlane_1_1Plane.html) and grid of the
[Draft](../../d4/d1a/namespaceDraft.html) module.  
  
  
##  Modules  
  
---  
| [draftfunctions](../../d2/d57/group__draftfunctions.html)  
| Modules with functions for use with scripted objects and GuiCommands.  
  
| [draftgeoutils](../../d9/dfd/group__draftgeoutils.html)  
| Functions that are meant to handle different geometrical operations.  
  
| [draftguitools](../../db/d6d/group__draftguitools.html)  
| Modules that define the workbench GuiCommands to perform actions.  
  
| [draftmake](../../d5/d7f/group__draftmake.html)  
| Modules with functions to create the custom scripted objects.  
  
| [draftobjects](../../de/de1/group__draftobjects.html)  
| Modules that contain classes that define custom scripted objects.  
  
| [drafttaskpanels](../../d5/d89/group__drafttaskpanels.html)  
| Modules with classes that handle task panels of the GuiCommands.  
  
| [drafttests](../../d8/dd4/group__drafttests.html)  
| Modules that define classes used for unit testing the workbench.  
  
| [draftutils](../../de/d75/group__draftutils.html)  
| Utility modules that are used throughout the workbench.  
  
| [draftviewproviders](../../d5/d24/group__draftviewproviders.html)  
| Classes that define viewproviders for the scripted objects.  
  
  
##  Variables  
  
---  
[bool](../../d9/db9/classbool.html) | [Draft.gui](../../d1/d35/group__DRAFT.html#ga3d0eb11d27efd5fe826ea1342a03d68c) = True  
  
## Detailed Description

Basic 2D drawing tools and other generic tools.

The [Draft](../../d4/d1a/namespaceDraft.html) workbench provides many tools
for building geometrical objects in a two-dimensional space, normally
supported by a working plane that includes a grid.

The grid serves as visual feedback of the coordinates and dimensions of the
geometrical elements that are created. Moreover, the vertices of the elements
can be attached to the grid intersections to precisely position them in the
plane.

The [Draft](../../d4/d1a/namespaceDraft.html) workbench also includes many
"Modifier" tools that can be used by most objects in the software because
these tools work on the internal
[Part::TopoShape](../../d8/ded/classPart_1_1TopoShape.html "The representation
for a CAD Shape.") property that most 2D and 3D objects have.

The [Draft](../../d4/d1a/namespaceDraft.html) workbench is similar to the
[Sketcher](../../d1/d23/namespaceSketcher.html) workbench in that both can be
used to create 2D objects in a planar surface. However, there is an important
difference:

  * The [Sketcher](../../d1/d23/namespaceSketcher.html) defines a local coordinate system; all geometrical elements created within it are referenced to this local origin. In addition, the position of those elements, as well as various relationships, are kept through the use of mathematical constraints (vertical, horizontal, parallelism, etc.).
  * On the other hand, the elements created with [Draft](../../d4/d1a/namespaceDraft.html) are placed in the global coordinate system. The elements in [Draft](../../d4/d1a/namespaceDraft.html) don't have constraints, they are freely placed in the 3D space.

The [Sketcher](../../d1/d23/namespaceSketcher.html)
[Workbench](../../da/d26/classWorkbench.html) is intended to be used together
with the [Part](../../d2/db9/namespacePart.html "AttachExtensionh, .cpp
contain a extension class to derive other features from, to make them
attachab...") and [PartDesign](../../df/d14/namespacePartDesign.html "Base
class of all additive features in PartDesign.") workbenches to create very
fine profiles that can be extruded to create complex 3D solids.

The [Draft](../../d4/d1a/namespaceDraft.html)
[Workbench](../../da/d26/classWorkbench.html) is more intended to draw
exclusively in a 2D plane placing points in a grid. Often this behavior is
better suited for drawing architectural plans, or for quick "drafting" that
doesn't need to keep mathematical constraints between its elements.

Due to this reason, the [Draft](../../d4/d1a/namespaceDraft.html)
[Workbench](../../da/d26/classWorkbench.html) is the foundation on which the
[Arch](../../df/dc6/namespaceArch.html)
[Workbench](../../da/d26/classWorkbench.html) sits. All tools of the
[Draft](../../d4/d1a/namespaceDraft.html)
[Workbench](../../da/d26/classWorkbench.html) are available in the
[Arch](../../df/dc6/namespaceArch.html)
[Workbench](../../da/d26/classWorkbench.html).

## Variable Documentation

## ◆ gui

[bool](../../d9/db9/classbool.html) Draft.gui = True  
---  
  
Referenced by
[StdCmdGroup.activated()](../../d0/de4/classStdCmdGroup.html#a44a9faa66df180f400cd830bb538771d),
[MeshGui::MeshSplit.cutMesh()](../../d9/de5/classMeshGui_1_1MeshSplit.html#aebb96b9863c72d1248d3372c0a3d6a65),
[Gui::Command.getObjectCmd()](../../d2/dff/classGui_1_1Command.html#a4335f72b8076a5ccb39a59694b8ddc01),
[Gui::MainWindow.insertFromMimeData()](../../d5/d2f/classGui_1_1MainWindow.html#a3b695bba64b1eead11c5bf3843c54790),
[MeshGui::MeshSplit.makeCopy()](../../d9/de5/classMeshGui_1_1MeshSplit.html#aae5f989f78a6a83f6f2f1f8dabfd1a56),
[MeshGui::DlgEvaluateMeshImp.on_refreshButton_clicked()](../../d6/d9b/classMeshGui_1_1DlgEvaluateMeshImp.html#a605469a13d795eb6e023070fd85ade67),
[Gui::TreeWidget.onCloseDoc()](../../de/de0/classGui_1_1TreeWidget.html#ae78b6342aabe626e970a4a5b6c17c243),
[Gui::Application.open()](../../d9/da8/classGui_1_1Application.html#a7035ec948a4d7a823668fb29d706faa8),
[MeshGui::MeshSplit.trimMesh()](../../d9/de5/classMeshGui_1_1MeshSplit.html#a3c2f778060142cb84e20ff69540da0a3),
and
[InspectionGui::VisualInspection.VisualInspection()](../../dd/d0b/classInspectionGui_1_1VisualInspection.html#aa13e595beac41fb1b077d794cd7fc0bc).

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

