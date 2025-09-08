---
url: https://wiki.freecad.org/Document_structure
title: Document structure
scraped_at: 2025-09-08 16:45:48
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Application and User Interface
  * 2 Scripting

# Document structure

  * [Page](/Document_structure "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Document_structure&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Document_structure)
  * [Edit](/index.php?title=Document_structure&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Document_structure&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Document_structure.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Document_structure&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Document_structure)
  * [Edit](/index.php?title=Document_structure&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Document_structure&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Document_structure&action=history)

General

  * [What links here](/Special:WhatLinksHere/Document_structure "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Document_structure "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Document_structure&oldid=1536429 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Document_structure&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Document_structure&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Document+structure&action=page&filter=&language=en)This is the approved
revision of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Document+structure&language=&task=view "Start translation for this language")
  * [Bahasa Indonesia](/Document_structure/id "Document structure \(6% translated\)")
  * [Deutsch](/Document_structure/de "Dokumentstruktur \(100% translated\)")
  * English
  * [Türkçe](/Document_structure/tr "Belge yapısı \(72% translated\)")
  * [español](/Document_structure/es "Estructura del documento \(61% translated\)")
  * [français](/Document_structure/fr "Structure d'un document \(100% translated\)")
  * [hrvatski](/Document_structure/hr "FreeCAD-Dokument \(6% translated\)")
  * [italiano](/Document_structure/it "Struttura del documento \(100% translated\)")
  * [polski](/Document_structure/pl "Struktura dokumentu \(100% translated\)")
  * [português](/Document_structure/pt "Estrutura do documento \(56% translated\)")
  * [português do Brasil](/Document_structure/pt-br "Estrutura do documento \(100% translated\)")
  * [română](/Document_structure/ro "Structura unui document/fișier în FreeCAD \(72% translated\)")
  * [svenska](/Document_structure/sv "Document structure \(61% translated\)")
  * [čeština](/Document_structure/cs "Struktura dokumentu \(61% translated\)")
  * [български](/Document_structure/bg "Структура на документите \(56% translated\)")
  * [русский](/Document_structure/ru "Структура документа \(100% translated\)")
  * [українська](/Document_structure/uk "Document structure \(6% translated\)")
  * [中文](/Document_structure/zh "文档结构 \(72% translated\)")
  * [中文（中国大陆）](/Document_structure/zh-cn "文档结构 \(61% translated\)")
  * [日本語](/Document_structure/ja "FreeCADファイルの構造 \(17% translated\)")
  * [한국어](/Document_structure/ko "문서 구조 \(56% translated\)")

![](/images/6/6f/Arrow-left.svg) [Navigation Cube](/Navigation_Cube
"Navigation Cube")

[Property editor](/Property_editor "Property editor") ![](/images/a/af/Arrow-
right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

[![](/images/d/d5/Screenshot_treeview.jpg)](/index.php?title=File:Screenshot_treeview.jpg&filetimestamp=20181210181422&)

A FreeCAD document contains all the objects of your scene. It can contain
groups, and objects made with any workbench. You can therefore switch between
workbenches, and still work on the same document. The document is what gets
saved to disk when you save your work. You can also open several documents at
the same time in FreeCAD, and open several views of the same document.

Inside the document, the objects can be moved into groups, and have a unique
name. Managing groups, objects and object names is done mainly from the [Tree
view](/Tree_view "Tree view"). **Note:** It can also be done, of course, like
everything in FreeCAD, from the [Python](/Python "Python") interpreter. In the
[Tree view](/Tree_view "Tree view"), you can create
[![](/images/c/cd/Std_Group.svg)](/index.php?title=File:Std_Group.svg&filetimestamp=20240528082502&)
[groups](/Std_Group "Std Group"), move objects to groups, delete objects or
groups, by right-clicking in the [tree view](/Tree_view "Tree view") or on an
object, rename objects by double-clicking on their names, or possibly other
operations, depending on the current workbench.

The objects inside a FreeCAD document can be of different types. Each
workbench can create its own types of objects, for example the
[![](/images/8/84/Workbench_Mesh.svg)](/index.php?title=File:Workbench_Mesh.svg&filetimestamp=20200404173024&)
[Mesh Workbench](/Mesh_Workbench "Mesh Workbench") creates mesh objects, the
[![](/images/0/04/Workbench_Part.svg)](/index.php?title=File:Workbench_Part.svg&filetimestamp=20240712190040&)
[Part Workbench](/Part_Workbench "Part Workbench") create Part objects, the
[![](/images/9/91/Workbench_Draft.svg)](/index.php?title=File:Workbench_Draft.svg&filetimestamp=20200404172706&)
[Draft Workbench](/Draft_Workbench "Draft Workbench") also creates Part
objects, etc.

If there is at least one document open in FreeCAD, there is always one and
only one active document. That's the document that appears in the current 3D
view, the document you are currently working on.

## Application and User Interface

Like almost everything else in FreeCAD, the graphical user interface part
(GUI) is separated from the base application part (App). This is also valid
for documents. The documents are also made of two parts: the Application
document, which contains our objects, and the View document, which contains
the representation on screen of our objects.

Think of it as two spaces, where the objects are defined. Their constructive
parameters (is it a cube? a cone? which size?) are stored in the Application
document, while their graphical representation (is it drawn with black lines?
with blue faces?) are stored in the View document. Why is that? Because
FreeCAD can also be used _without_ graphical interface, for example, inside
other programs, and we must still be able to manipulate our objects, even if
nothing is drawn on the screen.

Another thing that is contained inside the View document are 3D views. One
document can have several views opened, so you can inspect your document from
several points of view at the same time. Maybe you would want to see a top
view and a front view of your work at the same time? Then, you will have two
views of the same document, both stored in the View document. Creating new
views or closing views can be done from the View menu or by right-clicking on
a view tab.

## Scripting

Documents can be easily created, accessed and modified from the
[Python](/Python "Python") interpreter. For example:

    
    
    FreeCAD.ActiveDocument
    

Will return the current (active) document

    
    
    FreeCAD.ActiveDocument.Blob
    

Would access an object called "Blob" inside your document

    
    
    FreeCADGui.ActiveDocument
    

Will return the view document associated to the current document

    
    
    FreeCADGui.ActiveDocument.Blob
    

Would access the graphical representation (view) part of our Blob object

    
    
    FreeCADGui.ActiveDocument.ActiveView
    

Will return the current view

  

![](/images/6/6f/Arrow-left.svg) [Navigation Cube](/Navigation_Cube
"Navigation Cube")

[Property editor](/Property_editor "Property editor") ![](/images/a/af/Arrow-
right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

Expand[![](/images/thumb/9/94/User_hub.png/24px-
User_hub.png)](/index.php?title=File:User_hub.png&filetimestamp=20190221145008&)
[User documentation](/User_hub "User hub")

  * **[Getting started](/Getting_started "Getting started")**
  * **Installation:** [Download](/Download "Download"), [Windows](/Installing_on_Windows "Installing on Windows"), [Linux](/Installing_on_Linux "Installing on Linux"), [Mac](/Installing_on_Mac "Installing on Mac"), [Additional components](/Installing_additional_components "Installing additional components"), [Docker](/Compile_on_Docker "Compile on Docker"), [AppImage](/AppImage "AppImage"), [Ubuntu Snap](/Ubuntu_Snap "Ubuntu Snap")
  * **Basics:** [About FreeCAD](/About_FreeCAD "About FreeCAD"), [Interface](/Interface "Interface"), [Mouse navigation](/Mouse_navigation "Mouse navigation"), [Selection methods](/Selection_methods "Selection methods"), [Object name](/Object_name "Object name"), [Preferences](/Preferences_Editor "Preferences Editor"), [Workbenches](/Workbenches "Workbenches"), Document structure, [Properties](/Property "Property"), [Help FreeCAD](/Help_FreeCAD "Help FreeCAD"), [Donate](/Donate "Donate")

* * *

  * **Help:** [Tutorials](/Tutorials "Tutorials"), [Video tutorials](/Video_tutorials "Video tutorials")
  * **[Workbenches](/Workbenches "Workbenches"):** [Std Base](/Std_Base "Std Base"), [Assembly](/Assembly_Workbench "Assembly Workbench"), [BIM](/BIM_Workbench "BIM Workbench"), [CAM](/CAM_Workbench "CAM Workbench"), [Draft](/Draft_Workbench "Draft Workbench"), [FEM](/FEM_Workbench "FEM Workbench"), [Inspection](/Inspection_Workbench "Inspection Workbench"), [Material](/Material_Workbench "Material Workbench"), [Mesh](/Mesh_Workbench "Mesh Workbench"), [OpenSCAD](/OpenSCAD_Workbench "OpenSCAD Workbench"), [Part](/Part_Workbench "Part Workbench"), [PartDesign](/PartDesign_Workbench "PartDesign Workbench"), [Points](/Points_Workbench "Points Workbench"), [Reverse Engineering](/Reverse_Engineering_Workbench "Reverse Engineering Workbench"), [Robot](/Robot_Workbench "Robot Workbench"), [Sketcher](/Sketcher_Workbench "Sketcher Workbench"), [Spreadsheet](/Spreadsheet_Workbench "Spreadsheet Workbench"), [Surface](/Surface_Workbench "Surface Workbench"), [TechDraw](/TechDraw_Workbench "TechDraw Workbench"), [Test Framework](/Testing "Testing")

* * *

  * **[Addons](/Addon "Addon"):** [Addon Manager](/Std_AddonMgr "Std AddonMgr"), [External workbenches](/External_workbenches "External workbenches"), [Scripting and macros](/Scripting_and_macros "Scripting and macros")

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

