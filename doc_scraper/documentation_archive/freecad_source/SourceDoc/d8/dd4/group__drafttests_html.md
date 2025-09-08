---
url: https://freecad.github.io/SourceDoc/d8/dd4/group__drafttests.html
scraped_at: 2025-09-08T14:52:04.864422
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

Classes | Namespaces | Functions

drafttests

[Workbenches](../../d2/df2/group__WORKBENCHES.html) » [Python
workbenches](../../d1/d82/group__PYTHONWORKBENCHES.html) »
[Draft](../../d1/d35/group__DRAFT.html)

Modules that define classes used for unit testing the workbench. More...

##  Classes  
  
---  
class | [drafttests.test_airfoildat.DraftAirfoilDAT](../../db/d22/classdrafttests_1_1test__airfoildat_1_1DraftAirfoilDAT.html)  
class | [drafttests.test_creation.DraftCreation](../../d7/d8b/classdrafttests_1_1test__creation_1_1DraftCreation.html)  
class | [drafttests.test_dwg.DraftDWG](../../d6/d76/classdrafttests_1_1test__dwg_1_1DraftDWG.html)  
class | [drafttests.test_dxf.DraftDXF](../../df/de9/classdrafttests_1_1test__dxf_1_1DraftDXF.html)  
class | [drafttests.test_import.DraftImport](../../d0/d40/classdrafttests_1_1test__import_1_1DraftImport.html)  
class | [drafttests.test_import_gui.DraftGuiImport](../../db/d8b/classdrafttests_1_1test__import__gui_1_1DraftGuiImport.html)  
class | [drafttests.test_import_tools.DraftImportTools](../../df/d87/classdrafttests_1_1test__import__tools_1_1DraftImportTools.html)  
class | [drafttests.test_modification.DraftModification](../../d4/d33/classdrafttests_1_1test__modification_1_1DraftModification.html)  
class | [drafttests.test_oca.DraftOCA](../../d4/dbc/classdrafttests_1_1test__oca_1_1DraftOCA.html)  
class | [drafttests.test_pivy.DraftPivy](../../d9/d3a/classdrafttests_1_1test__pivy_1_1DraftPivy.html)  
class | [drafttests.test_svg.DraftSVG](../../db/d89/classdrafttests_1_1test__svg_1_1DraftSVG.html)  
  
##  Namespaces  
  
---  
namespace | [auxiliary](../../da/da9/namespaceauxiliary.html)  
| Auxiliary functions for the unit tests of the
[Draft](../../d4/d1a/namespaceDraft.html)
[Workbench](../../da/d26/classWorkbench.html).  
  
namespace | [draft_test_objects](../../d8/dd5/namespacedraft__test__objects.html)  
| Run this file to create a standard test document for
[Draft](../../d4/d1a/namespaceDraft.html) objects.  
  
namespace | [test_airfoildat](../../d3/d5d/namespacetest__airfoildat.html)  
| Unit tests for the [Draft](../../d4/d1a/namespaceDraft.html)
[Workbench](../../da/d26/classWorkbench.html), Airfoil DAT tests.  
  
namespace | [test_creation](../../d5/d78/namespacetest__creation.html)  
| Unit tests for the [Draft](../../d4/d1a/namespaceDraft.html)
[Workbench](../../da/d26/classWorkbench.html), object creation tests.  
  
namespace | [test_dwg](../../d2/d69/namespacetest__dwg.html)  
| Unit tests for the [Draft](../../d4/d1a/namespaceDraft.html)
[Workbench](../../da/d26/classWorkbench.html), DWG import and export tests.  
  
namespace | [test_dxf](../../d7/d0d/namespacetest__dxf.html)  
| Unit tests for the [Draft](../../d4/d1a/namespaceDraft.html)
[Workbench](../../da/d26/classWorkbench.html), DXF import and export tests.  
  
namespace | [test_import](../../da/d45/namespacetest__import.html)  
| Unit tests for the [Draft](../../d4/d1a/namespaceDraft.html)
[Workbench](../../da/d26/classWorkbench.html), import tests.  
  
namespace | [test_import_gui](../../d6/d2b/namespacetest__import__gui.html)  
| Unit tests for the [Draft](../../d4/d1a/namespaceDraft.html)
[Workbench](../../da/d26/classWorkbench.html), GUI import tests.  
  
namespace | [test_import_tools](../../d9/dbb/namespacetest__import__tools.html)  
| Unit tests for the [Draft](../../d4/d1a/namespaceDraft.html)
[Workbench](../../da/d26/classWorkbench.html), tools import tests.  
  
namespace | [test_modification](../../d8/dcb/namespacetest__modification.html)  
| Unit tests for the [Draft](../../d4/d1a/namespaceDraft.html)
[Workbench](../../da/d26/classWorkbench.html), object modification tests.  
  
namespace | [test_oca](../../d1/d41/namespacetest__oca.html)  
| Unit tests for the [Draft](../../d4/d1a/namespaceDraft.html)
[Workbench](../../da/d26/classWorkbench.html), OCA import and export tests.  
  
namespace | [test_pivy](../../dc/d93/namespacetest__pivy.html)  
| Unit tests for the [Draft](../../d4/d1a/namespaceDraft.html)
[Workbench](../../da/d26/classWorkbench.html), Coin (Pivy) tests.  
  
namespace | [test_svg](../../d2/d81/namespacetest__svg.html)  
| Unit tests for the [Draft](../../d4/d1a/namespaceDraft.html)
[Workbench](../../da/d26/classWorkbench.html), SVG import and export tests.  
  
  
##  Functions  
  
---  
def | [drafttests.draft_test_objects.create_test_file](../../d8/dd4/group__drafttests.html#ga639df062fe02e8983bebaa00a57a5563) (font_file=App.getHomePath()+"data/Mod/TechDraw/Resources/fonts/osifont-lgpl3fe.ttf", hatch_file=App.getHomePath()+"data/Mod/TechDraw/PAT/FCPAT.pat", hatch_name="Horizontal5")  
def | [drafttests.auxiliary.draw_header](../../d8/dd4/group__drafttests.html#ga56b40d22babb20ebb3d3787f7472a42d) ()  
def | [drafttests.auxiliary.fake_function](../../d8/dd4/group__drafttests.html#gafd3d9af09fff9945e365effd84d738af) (p1=None, p2=None, p3=None, p4=None, p5=None)  
def | [drafttests.auxiliary.import_test](../../d8/dd4/group__drafttests.html#gadc45eeecafa08a7a4c908e397d94cd8a) (module)  
def | [drafttests.auxiliary.no_gui](../../d8/dd4/group__drafttests.html#gaa00d92103cbec70b93d6e7a318825ddd) (module)  
def | [drafttests.auxiliary.no_test](../../d8/dd4/group__drafttests.html#gab859dc9ade6e6e974cf5d4929d807c63) ()  
  
## Detailed Description

Modules that define classes used for unit testing the workbench.

## Function Documentation

## ◆ create_test_file()

def drafttests.draft_test_objects.create_test_file  | ( |  | _font_file_ = `App.getHomePath()+"data/Mod/TechDraw/Resources/fonts/osifont-lgpl3fe.ttf"`,   
---|---|---|---  
|  |  | _hatch_file_ = `App.getHomePath()+"data/Mod/TechDraw/PAT/FCPAT.pat"`,   
|  |  | _hatch_name_ = `"Horizontal5"`  
| ) | |   
      
    
    Create a complete test file of Draft objects.
    
    It draws a frame with information on the software used to create
    the test document, and fills it with every object that can be created.
    
    Parameters
    ----------
    font_file: str, optional
        It defaults to `App.getHomePath()+"data/Mod/TechDraw/Resources/fonts/osifont-lgpl3fe.ttf"`
        It is the full path of a font file to be used to create a `Draft ShapeString`.
        If the file is not found, this object is not created.
    
    hatch_file: str, optional
        It defaults to `App.getHomePath()+"data/Mod/TechDraw/PAT/FCPAT.pat"`
        It is the full path of a PAT file to be used to create a `Draft Hatch`.
        If the file is not found, this object is not created.
    
    hatch_name: str, optional
        It defaults to `"Horizontal5"`
        It is the name of a hatch pattern in the hatch_file.
    
    Returns
    -------
    App::Document
        A reference to the test document that was created.
    

References
[drafttests.draft_test_objects.create_test_file()](../../d8/dd4/group__drafttests.html#ga639df062fe02e8983bebaa00a57a5563).

Referenced by
[drafttests.draft_test_objects.create_test_file()](../../d8/dd4/group__drafttests.html#ga639df062fe02e8983bebaa00a57a5563).

## ◆ draw_header()

def drafttests.auxiliary.draw_header  | ( | | ) |   
---|---|---|---|---  
      
    
    Draw a header for the tests.

## ◆ fake_function()

def drafttests.auxiliary.fake_function  | ( |  | _p1_ = `None`,   
---|---|---|---  
|  |  | _p2_ = `None`,   
|  |  | _p3_ = `None`,   
|  |  | _p4_ = `None`,   
|  |  | _p5_ = `None`  
| ) | |   
      
    
    Print a message for a test that doesn't actually exist.

References
[drafttests.auxiliary.no_test()](../../d8/dd4/group__drafttests.html#gab859dc9ade6e6e974cf5d4929d807c63).

## ◆ import_test()

def drafttests.auxiliary.import_test  | ( |  | _module_| ) |   
---|---|---|---|---|---  
      
    
    Try importing a module.

## ◆ no_gui()

def drafttests.auxiliary.no_gui  | ( |  | _module_| ) |   
---|---|---|---|---|---  
      
    
    Print a message that there is no user interface.

## ◆ no_test()

def drafttests.auxiliary.no_test  | ( | | ) |   
---|---|---|---|---  
      
    
    Print a message that the test is not currently implemented.

Referenced by
[drafttests.auxiliary.fake_function()](../../d8/dd4/group__drafttests.html#gafd3d9af09fff9945e365effd84d738af).

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

