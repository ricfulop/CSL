---
url: https://wiki.freecad.org/Testing
title: Testing
scraped_at: 2025-09-08 16:45:58
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction
  * 2 Test menu
  * 3 Test functions Toggle Test functions subsection
    * 3.1 TestAPP.All
    * 3.2 BaseTests
    * 3.3 UnitTests
    * 3.4 Document
    * 3.5 UnicodeTests
    * 3.6 MeshTestsApp
    * 3.7 TestDraft
    * 3.8 TestSketcherApp
    * 3.9 TestPartApp
    * 3.10 TestPartDesignApp
    * 3.11 TestCAMApp
    * 3.12 Workbench
    * 3.13 Menu
    * 3.14 Menu.MenuDeleteCases
    * 3.15 Menu.MenuCreateCases
  * 4 Scripting Toggle Scripting subsection
    * 4.1 Get a list of all top-level test modules
    * 4.2 Run specific tests
    * 4.3 Example 1
  * 5 Additional Resources Toggle Additional Resources subsection
    * 5.1 Forum Topics

# Testing

  * [Page](/Testing "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Testing&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Testing)
  * [Edit](/index.php?title=Testing&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Testing&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Testing.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Testing&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Testing)
  * [Edit](/index.php?title=Testing&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Testing&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Testing&action=history)

General

  * [What links here](/Special:WhatLinksHere/Testing "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Testing "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Testing&oldid=1623592 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Testing&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Testing&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Testing&action=page&filter=&language=en)This is the approved revision of this
page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Testing&language=&task=view "Start translation for this language")
  * [Deutsch](/Testing/de "Erprobung \(98% translated\)")
  * English
  * [Türkçe](/Testing/tr "Testing \(2% translated\)")
  * [español](/Testing/es "Prueba \(37% translated\)")
  * [français](/Testing/fr "Atelier Test \(100% translated\)")
  * [italiano](/Testing/it "Testare FreeCAD \(100% translated\)")
  * [polski](/Testing/pl "Środowisko pracy Test \(100% translated\)")
  * [português do Brasil](/Testing/pt-br "Teste \(7% translated\)")
  * [română](/Testing/ro "Testing/Testare \(2% translated\)")
  * [svenska](/Testing/sv "Testing \(2% translated\)")
  * [русский](/Testing/ru "Верстак Test Framework \(22% translated\)")
  * [українська](/Testing/uk "Testing/uk \(2% translated\)")
  * [中文（中国大陆）](/Testing/zh-cn "Testing/zh-cn \(0% translated\)")
  * [日本語](/Testing/ja "テスト・フレームワーク・ワークベンチ \(2% translated\)")

![](/images/6/6f/Arrow-left.svg) [Debugging](/Debugging "Debugging")

[FreeCAD Build Tool](/FreeCAD_Build_Tool "FreeCAD Build Tool")
![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

[![](/images/b/bf/Workbench_Test.svg)](/index.php?title=File:Workbench_Test.svg&filetimestamp=20200404174253&)Test
workbench icon

## Introduction

The Test Framework Workbench is not really a modelling workbench, but it
contains a set of [Python](/Python "Python") scripts to perform different
tests on the core components of FreeCAD, in order to debug problems. See also
[debugging](/Debugging "Debugging").

You can run the tests from the command line, by using the `-t` or `--run-test`
options.

Run all tests:

    
    
    freecad --run-test 0
    

Run only some the specified unit test, for example:

    
    
    freecad -t TestDraft
    

If a test does not need the GUI, it can also be executed in console mode by
setting the `-c` or `--console` option in addition. This usually results in
much faster startup time as the GUI is not loaded. For example:

    
    
    freecad -c -t TestPartDesignApp
    

Files generated by the testing procedure (e.g. input files from TestFemApp
stored in the FEM_unittests folder) are written to the temp directory used by
FreeCAD that can be located by entering this in the [Python
console](/Python_console "Python console"):

    
    
    App.getTempPath()
    

They might be useful for debugging.

## Test menu

Each top level directory in FreeCAD should have a file with the tests that can
be run for that particular workbench or module. The file usually starts with
the word `Test`.

To run a test from within FreeCAD, switch to the Test Workbench, then **Test
commands → TestToolsGui → Self test → Select test name** , then enter the name
of the Python file with the tests; for example, for the [Draft
Workbench](/Draft_Workbench "Draft Workbench"), this would be **TestDraft** ,
then press Start.

## Test functions

This is the list of test apps as of 0.15 git 4207:

### TestAPP.All

Add test function

### BaseTests

Add test function

### UnitTests

Add test function

### Document

Add test function

### UnicodeTests

Add test function

### MeshTestsApp

Add test function

### TestDraft

Add test function

### TestSketcherApp

Add test function

### TestPartApp

Add test function

### TestPartDesignApp

Add test function

### TestCAMApp

Path workbench test cases:

  * depthTestCases:
  * PathTestUtils:
  * TestDressupDogbone: Test functionality of Dogbone dressup.
  * TestHoldingTags: Test functionality of Holding Tags dressup.
  * TestPathAdaptive: Test selection capability of Adaptive operation.
  * TestPathCore: Test core functionality of Path workbench.
  * TestPathDeburr: Test general functionality of Deburr operation.
  * TestPathGeom: Test various functions available in the PathGeom module.
  * TestPathHelix: Test general functionality of Helix operation.
  * TestPathLog: Test various functions available in the PathLog debugging and feedback module.
  * TestPathOpTools:
  * TestPathPreferences: Test various functions available in the PathPreferences module.
  * TestPathPropertyBag:
  * TestPathSetupSheet:
  * TestPathStock:
  * TestPathThreadMilling:
  * TestPathTool:
  * TestPathToolBit:
  * TestPathToolController:
  * TestPathTooltable:
  * TestPathUtil: Test various functions available in the PathUtil module.
  * TestPathVcarve: Test general functionality of Vcarve operation.
  * TestPathVoronoi:

### Workbench

Add test function

### Menu

Add test function

### Menu.MenuDeleteCases

Add test function

### Menu.MenuCreateCases

Add test function

## Scripting

_See also:_ [FreeCAD Scripting Basics](/FreeCAD_Scripting_Basics "FreeCAD
Scripting Basics").

### Get a list of all top-level test modules

    
    
    FreeCAD.__unit_test__
    

Note that the test modules returned here depend on whether a GUI available or
not. I.e. when executed in console mode, various tests ending in "Gui" are
missing.

### Run specific tests

There are various ways of running tests using [Python's unittest
library](https://docs.python.org/3/library/unittest.html). FreeCAD's test
framework removes some of the boiler plate for the most common cases.

Run all tests defined in a Python module:

    
    
    import Test, TestFemApp
    Test.runTestsFromModule(TestFemApp)
    

Run all tests defined in a Python class:

    
    
    import Test, femtest.app.test_solver_calculix
    Test.runTestsFromClass(femtest.app.test_solver_calculix.TestSolverCalculix)
    

### Example 1

Within the Python Console of FreeCAD, the following code format may be used to
run built-in tests. Replace the red "**TestFem** " text in the code below with
the desired module test name.

  * For example, use "**TestPathApp** " to run all unit tests for the Path workbench unit test framework.
  * Submodules are available using dot notation, like "**TestPathApp.TestPathAdaptive** " to only run the Adaptive unit tests within the greater Path workbench test framework.
  * Multiple test modules or submodules may be combined by adding another `**suite.addTest(...)** ` method call just like the one in the code below, but with a different module or submodule reference.
  * Output for the code below will be in the Report View panel within the FreeCAD GUI.
  * Code source is copied from post by FreeCAD forum user, _sgrogan_ , in the [unit tests per python](https://forum.freecad.org/viewtopic.php?style=3&p=153251#p153251) topic, with credit there given to forum user, _wmayer_.

    
    
    import unittest
    suite = unittest.TestSuite()
    suite.addTest(unittest.defaultTestLoader.loadTestsFromName("TestFem"))
    r = unittest.TextTestRunner()
    r.run(suite)
    

## Additional Resources

### Forum Topics

  * [Support for running specific unit tests with --run-test #331](https://forum.freecad.org/viewtopic.php?style=3&f=27&t=18379)

  

![](/images/6/6f/Arrow-left.svg) [Debugging](/Debugging "Debugging")

[FreeCAD Build Tool](/FreeCAD_Build_Tool "FreeCAD Build Tool")
![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

Expand[![](/images/thumb/9/94/User_hub.png/24px-
User_hub.png)](/index.php?title=File:User_hub.png&filetimestamp=20190221145008&)
[User documentation](/User_hub "User hub")

  * **[Getting started](/Getting_started "Getting started")**
  * **Installation:** [Download](/Download "Download"), [Windows](/Installing_on_Windows "Installing on Windows"), [Linux](/Installing_on_Linux "Installing on Linux"), [Mac](/Installing_on_Mac "Installing on Mac"), [Additional components](/Installing_additional_components "Installing additional components"), [Docker](/Compile_on_Docker "Compile on Docker"), [AppImage](/AppImage "AppImage"), [Ubuntu Snap](/Ubuntu_Snap "Ubuntu Snap")
  * **Basics:** [About FreeCAD](/About_FreeCAD "About FreeCAD"), [Interface](/Interface "Interface"), [Mouse navigation](/Mouse_navigation "Mouse navigation"), [Selection methods](/Selection_methods "Selection methods"), [Object name](/Object_name "Object name"), [Preferences](/Preferences_Editor "Preferences Editor"), [Workbenches](/Workbenches "Workbenches"), [Document structure](/Document_structure "Document structure"), [Properties](/Property "Property"), [Help FreeCAD](/Help_FreeCAD "Help FreeCAD"), [Donate](/Donate "Donate")

* * *

  * **Help:** [Tutorials](/Tutorials "Tutorials"), [Video tutorials](/Video_tutorials "Video tutorials")
  * **[Workbenches](/Workbenches "Workbenches"):** [Std Base](/Std_Base "Std Base"), [Assembly](/Assembly_Workbench "Assembly Workbench"), [BIM](/BIM_Workbench "BIM Workbench"), [CAM](/CAM_Workbench "CAM Workbench"), [Draft](/Draft_Workbench "Draft Workbench"), [FEM](/FEM_Workbench "FEM Workbench"), [Inspection](/Inspection_Workbench "Inspection Workbench"), [Material](/Material_Workbench "Material Workbench"), [Mesh](/Mesh_Workbench "Mesh Workbench"), [OpenSCAD](/OpenSCAD_Workbench "OpenSCAD Workbench"), [Part](/Part_Workbench "Part Workbench"), [PartDesign](/PartDesign_Workbench "PartDesign Workbench"), [Points](/Points_Workbench "Points Workbench"), [Reverse Engineering](/Reverse_Engineering_Workbench "Reverse Engineering Workbench"), [Robot](/Robot_Workbench "Robot Workbench"), [Sketcher](/Sketcher_Workbench "Sketcher Workbench"), [Spreadsheet](/Spreadsheet_Workbench "Spreadsheet Workbench"), [Surface](/Surface_Workbench "Surface Workbench"), [TechDraw](/TechDraw_Workbench "TechDraw Workbench"), Test Framework

* * *

  * **[Addons](/Addon "Addon"):** [Addon Manager](/Std_AddonMgr "Std AddonMgr"), [External workbenches](/External_workbenches "External workbenches"), [Scripting and macros](/Scripting_and_macros "Scripting and macros")

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

