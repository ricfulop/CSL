---
url: https://wiki.freecad.org/Object_name
title: Object name
scraped_at: 2025-09-08 16:45:44
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction
  * 2 Names
  * 3 Labels Toggle Labels subsection
    * 3.1 Label2
  * 4 Scripting Toggle Scripting subsection
    * 4.1 Name
    * 4.2 Label
    * 4.3 Getting an object by Name or Label

# Object name

  * [Page](/Object_name "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Object_name&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Object_name)
  * [Edit](/index.php?title=Object_name&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Object_name&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Object_name.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Object_name&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Object_name)
  * [Edit](/index.php?title=Object_name&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Object_name&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Object_name&action=history)

General

  * [What links here](/Special:WhatLinksHere/Object_name "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Object_name "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Object_name&oldid=1560799 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Object_name&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Object_name&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Object+name&action=page&filter=&language=en)This is the approved revision of
this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Object+name&language=&task=view "Start translation for this language")
  * [Deutsch](/Object_name/de "Objektname \(54% translated\)")
  * English
  * [español](/Object_name/es "Nombre del objeto \(21% translated\)")
  * [français](/Object_name/fr "Objet name \(100% translated\)")
  * [italiano](/Object_name/it "Nome dell'oggetto \(100% translated\)")
  * [polski](/Object_name/pl "Nazwa obiektu \(100% translated\)")
  * [português do Brasil](/Object_name/pt-br "Nome do objeto \(12% translated\)")
  * [русский](/Object_name/ru "Object name/ru \(4% translated\)")
  * [日本語](/Object_name/ja "オブジェクトの名前 \(8% translated\)")
  * [한국어](/Object_name/ko "대상물 명칭 \(25% translated\)")

## Introduction

All objects in the program have an object name that uniquely identifies them
in a given document.

This information applies to all objects derived from [App
DocumentObject](/App_DocumentObject "App DocumentObject")
(`App::DocumentObject` class), which essentially comprises all objects that
are possible to create in a document.

## Names

There are various properties for Names:

  * The `Name` can only include simple alphanumeric characters, and the underscore, `[_0-9a-zA-Z]`.
  * The `Name` cannot start with a number; it must start with a letter or the underscore, `[_a-zA-Z]`.
  * The `Name` is assigned at the creation time of the object; afterwards it is no longer editable. The object can never be renamed.
  * The `Name` must be unique in the entire document. It doesn't matter if two objects are of completely different types, for example, one is a [PartDesign Pocket](/PartDesign_Pocket "PartDesign Pocket") and the other is an [Arch Wall](/Arch_Wall "Arch Wall"). They must have different names.
  * When creating an object of the same type, normally the name is increased with a sequential number, thus `Box`, `Box001`, `Box002`, etc. This prevents naming collision.
  * Once the object is deleted, its `Name` becomes available to be used by a newly created object. This means that if `Box`, `Box001`, and `Box002` exist, and we delete the first item, the next box created with [Part Box](/Part_Box "Part Box") will not be `Box003`, it will be `Box` again, because this string is available to be used once more. Notice that it is not possible to rename `Box001` or `Box002` to `Box` since their names are fixed.

In summary, the `Name` essentially acts like a unique identifier (UID) for an
object. Since a unique `Name` is very restrictive, all objects also have a
`Label` property which allows "renaming" the object to something more
descriptive. The internal `Name` actually remains fixed, but the user editable
`Label` can be used in most situations where the `Name` would be used. In
common usage in the program and the documentation, "renaming" means changing
the `Label` and not the actual `Name` of the object.

## Labels

There are various properties for Labels:

  * The `Label` can accept any UTF8 string, including accents and spaces.
  * The [tree view](/Tree_view "Tree view") actually displays the `Label` of the object, not the `Name`. Therefore, whenever a new object is created, it is a good practice to change the `Label` to a more descriptive string. To rename (relabel) the object, select it in the tree view and press F2 (or rather Return on macOS), or open the context menu (right-click) and choose **Rename**.
  * Even after an object was renamed (relabelled), the internal `Name` will still be reported in many places, for example, in the [status bar](/Status_bar "Status bar") or in the [selection view](/Selection_view "Selection view"), when the object is selected.
  * Since the internal functions of the program refer to the objects by `Name`, many dialogs will display the `Name` first, followed by the user editable `Label` in parentheses, for example, `Box (Extruded piece)`.
  * By default the `Label` is unique, just like the `Name`. However, this behavior can be changed in the [preferences editor](/Preferences_Editor "Preferences Editor"), **Edit → Preferences → General → Document → Allow duplicate object labels in one document**. This means that in general the `Label` is not unique in the document, and may actually be repeated. However, the recommendation is to keep the `Label` unique, as this is probably what is most useful to identify different objects. When writing custom functions that manipulate objects, the methods should use the `Name` of the object rather than its `Label` to guarantee that the correct object is used.
  * When using [expressions](/Expressions "Expressions"), for example, in the [property editor](/Property_editor "Property editor") or in a [spreadsheet](/Spreadsheet "Spreadsheet"), the Label can be referenced using double brackets made of the less than and greater than symbols.

    
    
    <<Custom Label With Spaces>>.Height
    <<Label may use UTF8 characters>>.Width
    

### Label2

It is a simple string that can contain arbitrary text, and therefore can be
used for documenting (describing with more detail) the created object.

  * In the [tree view](/Tree_view "Tree view") edit the field next to the icon, under "Description", by clicking on it and pressing F2 (or rather Return on macOS).
  * You can also change this property by modifying the `Label2` attribute from the [Python console](/Python_console "Python console").
  * The Data**Label2** attribute is normally hidden in the [property editor](/Property_editor "Property editor") but can be made visible by opening the context menu (right click) and selecting **Show hidden**.

## Scripting

_See also:_ [FreeCAD Scripting Basics](/FreeCAD_Scripting_Basics "FreeCAD
Scripting Basics"), and [scripted objects](/Scripted_objects "Scripted
objects").

Any object in the software is internally created with the `addObject()` method
of the document. The majority of 2D and 3D objects that the user will see in
the [3D view](/3D_view "3D view") are derived from a [Part
Feature](/Part_Feature "Part Feature"). In the following example, the object
created is a [Part Box](/Part_Box "Part Box").

    
    
    import FreeCAD as App
    
    doc = App.newDocument()
    obj = doc.addObject("Part::Box", "Name")
    obj.Label = "Custom label"
    

### Name

The `addObject` function has two basic string arguments.

  * The first argument indicates the type of object, in this case, `"Part::Box"`.
  * The second argument is a string that defines the `Name` attribute. If it is not provided, it defaults to the same name as the class of the object, that is, `"Part__Box"`, where the two invalid symbols, the colons `::`, are replaced by two underscores `__`. 
    * The `Name` can only include simple alphanumeric characters, and the underscore, `[_0-9a-zA-Z]`. If other symbols are given, these will be converted to underscores; for example, `"A+B:C*"` is converted to `"A_B_C_"`.
    * The `Name` cannot start with a number; it must start with a letter or the underscore, `[_a-zA-Z]`. For example, `"123ABC"` is converted to `"_23ABC"`.
    * The `Name` is fixed at creation time; it cannot be modified afterwards.
    * The `Name` must be unique in the entire document. If the same `"Name"` is used, a sequential number will be appended automatically so that the resulting names are unique; for example, if `"Name"` already exists, then new objects will be called `"Name001"`, `"Name002"`, `"Name003"`, etc.

### Label

The `Label` is a property of the created object and can be changed to a more
meaningful text.

  * Upon creating the object, the `Label` is the same as the `Name`.
  * However, unlike the `Name`, the `Label` can accept any UTF8 string, including accents and spaces.
  * The `Label` can be changed at any point in time just by assigning the desired string, `obj.Label = "New label"`

### Getting an object by Name or Label

All objects in a document are data attributes of the corresponding
[Document](/App_DocumentObject "App DocumentObject") object. The attribute's
name correspond to the internal `Name` of the object.

    
    
    import FreeCAD as App
    
    obj1 = App.ActiveDocument.Box
    obj2 = App.ActiveDocument.Box001
    obj3 = App.ActiveDocument.Box002
    

This is equivalent to using the `getObject` method of the Document.

    
    
    import FreeCAD as App
    
    obj1 = App.ActiveDocument.getObject('Box')
    obj2 = App.ActiveDocument.getObject('Box001')
    obj3 = App.ActiveDocument.getObject('Box002')
    

However, it is also possible to get the object by the more descriptive
`Label`.

    
    
    import FreeCAD as App
    
    obj1 = App.ActiveDocument.getObjectsByLabel("Concrete wall")[0]
    obj2 = App.ActiveDocument.getObjectsByLabel("Custom parallelepiped")[0]
    obj3 = App.ActiveDocument.getObjectsByLabel("Some special name for this cube__002")[0]
    

Given that the `Label` is in general not unique, the `getObjectsByLabel`
method returns a list with all objects found with that `Label`. However, if
the `Label` is unique in the document then the first element in that list
should be the desired object.

Expand[![](/images/thumb/9/94/User_hub.png/24px-
User_hub.png)](/index.php?title=File:User_hub.png&filetimestamp=20190221145008&)
[User documentation](/User_hub "User hub")

  * **[Getting started](/Getting_started "Getting started")**
  * **Installation:** [Download](/Download "Download"), [Windows](/Installing_on_Windows "Installing on Windows"), [Linux](/Installing_on_Linux "Installing on Linux"), [Mac](/Installing_on_Mac "Installing on Mac"), [Additional components](/Installing_additional_components "Installing additional components"), [Docker](/Compile_on_Docker "Compile on Docker"), [AppImage](/AppImage "AppImage"), [Ubuntu Snap](/Ubuntu_Snap "Ubuntu Snap")
  * **Basics:** [About FreeCAD](/About_FreeCAD "About FreeCAD"), [Interface](/Interface "Interface"), [Mouse navigation](/Mouse_navigation "Mouse navigation"), [Selection methods](/Selection_methods "Selection methods"), Object name, [Preferences](/Preferences_Editor "Preferences Editor"), [Workbenches](/Workbenches "Workbenches"), [Document structure](/Document_structure "Document structure"), [Properties](/Property "Property"), [Help FreeCAD](/Help_FreeCAD "Help FreeCAD"), [Donate](/Donate "Donate")

* * *

  * **Help:** [Tutorials](/Tutorials "Tutorials"), [Video tutorials](/Video_tutorials "Video tutorials")
  * **[Workbenches](/Workbenches "Workbenches"):** [Std Base](/Std_Base "Std Base"), [Assembly](/Assembly_Workbench "Assembly Workbench"), [BIM](/BIM_Workbench "BIM Workbench"), [CAM](/CAM_Workbench "CAM Workbench"), [Draft](/Draft_Workbench "Draft Workbench"), [FEM](/FEM_Workbench "FEM Workbench"), [Inspection](/Inspection_Workbench "Inspection Workbench"), [Material](/Material_Workbench "Material Workbench"), [Mesh](/Mesh_Workbench "Mesh Workbench"), [OpenSCAD](/OpenSCAD_Workbench "OpenSCAD Workbench"), [Part](/Part_Workbench "Part Workbench"), [PartDesign](/PartDesign_Workbench "PartDesign Workbench"), [Points](/Points_Workbench "Points Workbench"), [Reverse Engineering](/Reverse_Engineering_Workbench "Reverse Engineering Workbench"), [Robot](/Robot_Workbench "Robot Workbench"), [Sketcher](/Sketcher_Workbench "Sketcher Workbench"), [Spreadsheet](/Spreadsheet_Workbench "Spreadsheet Workbench"), [Surface](/Surface_Workbench "Surface Workbench"), [TechDraw](/TechDraw_Workbench "TechDraw Workbench"), [Test Framework](/Testing "Testing")

* * *

  * **[Addons](/Addon "Addon"):** [Addon Manager](/Std_AddonMgr "Std AddonMgr"), [External workbenches](/External_workbenches "External workbenches"), [Scripting and macros](/Scripting_and_macros "Scripting and macros")

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

