---
url: https://wiki.freecad.org/Viewprovider
title: Viewprovider
scraped_at: 2025-09-08 16:41:43
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction
  * 2 Python view providers
  * 3 Custom icons

# Viewprovider

  * [Page](/Viewprovider "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Viewprovider&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Viewprovider)
  * [Edit](/index.php?title=Viewprovider&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Viewprovider&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Viewprovider.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Viewprovider&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Viewprovider)
  * [Edit](/index.php?title=Viewprovider&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Viewprovider&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Viewprovider&action=history)

General

  * [What links here](/Special:WhatLinksHere/Viewprovider "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Viewprovider "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Viewprovider&oldid=1073142 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Viewprovider&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Viewprovider&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Viewprovider&action=page&filter=&language=en)This is the approved revision of
this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Viewprovider&language=&task=view "Start translation for this language")
  * [Deutsch](/Viewprovider/de "Viewprovider \(100% translated\)")
  * English
  * [français](/Viewprovider/fr "Viewprovider \(100% translated\)")
  * [italiano](/Viewprovider/it "Viewprovider \(100% translated\)")
  * [polski](/Viewprovider/pl "Dostawca widoku \(100% translated\)")
  * [русский](/Viewprovider/ru "Viewprovider - ПоставщикВида \(100% translated\)")

## Introduction

Viewproviders are classes that define the way objects will look like in the
[tree view](/Tree_view "Tree view") and the [3D view](/3D_view "3D view"), and
how they will interact with certain graphical actions such as
[selection](/Selection_methods "Selection methods").

They complement the [scripted objects](/Scripted_objects "Scripted objects").
While the base class of the scripted object defines its _data_
[properties](/Property "Property"), the viewprovider defines it _view_
[properties](/Property "Property"). These view properties are not essential
information of the object, as they only indicate superficial information like
line width, line color, face color, etc. In a terminal only session, the
viewprovider is not loaded because there will be no interface to manipulate
those visible properties.

Like with data properties, view properties are accessible from the [property
editor](/Property_editor "Property editor").

## Python view providers

The viewproviders classes usually include `ViewProvider` in their name. They
are assigned on the `ViewObject` attribute of the base object.

In this example, we define two properties for the viewprovider, only if the
properties don't already exist, and assign their default values. We also
define the `onChanged` method that runs every time a property changes. We need
to test the property by name, and then we will call one of two methods that
will do the actual work of updating the pattern or setting its size.

    
    
    # views/view_custom.py
    class ViewProviderCustom:
        """Viewprovider of the custom object."""
    
        def __init__(self, vobj):
            self.Object = vobj.Object
    
            self._set_properties(vobj)
            vobj.Proxy = self
    
        def _set_properties(self, vobj):
            if not hasattr(vobj, "Pattern"):
                vobj.addProperty("App::PropertyEnumeration",
                                 "Pattern",
                                 "Custom",
                                 "Defines a hatch pattern for this object.")
                vobj.Pattern = ["None", "diagonals", "cross", "brick"]
    
            if not hasattr(vobj, "PatternSize"):
                vobj.addProperty("App::PropertyFloat",
                                 "PatternSize",
                                 "Custom",
                                 "Defines the size of the hatch pattern.")
                vobj.PatternSize = 1
    
        def onChanged(self, vobj, prop):
            if prop in "Pattern":
                self._set_pattern(vobj.Pattern)
            if prop in "PatternSize":
                self._set_size(vobj.PatternSize)
    
        def _set_pattern(self, pattern):
            ...
    
        def _set_size(self, size):
            ...
    

The normal workflow is to first add the object proxy class, for example,
`CustomObject`, and then the viewprovider, for example, `ViewProviderCustom`.
The viewprovider can only be assigned when we have verified that the graphical
interface is available, as otherwise the `ViewObject` attribute doesn't exist,
and it will be an error to use this element as input for our class.

    
    
    import FreeCAD as App
    import objects.custom as custom
    import views.view_custom as view_custom
    
    doc = App.newDocument()
    obj = doc.addObject("Part::FeaturePython", "Custom")
    
    custom.CustomObject(obj)
    
    if App.GuiUp:
        view_custom.ViewProviderCustom(obj.ViewObject)
    

## Custom icons

By implementing the `getIcon` method, you can specify the icon that will be
shown in the [tree view](/Tree_view "Tree view") in the upper part of the
[combo view](/Combo_view "Combo view").

The return value can be the full path to an icon.

    
    
    import os
    some_path = "/home/user/.FreeCAD/custom_icons"
    
    class ViewProviderCustom:
        ...
    
        def getIcon(self):
            return os.path.join(some_path, "my_icon.svg")
    

The relative path to an icon inside a compiled resource file.

    
    
    import MyModule_rc.py
    
    class ViewProviderCustom:
        ...
    
        def getIcon(self):
            return ":/icons/my_icon.svg"
    

A raw [XPM icon](https://en.wikipedia.org/wiki/X_PixMap), which is essentially
ASCII art.

    
    
    import MyModule_rc.py
    
    class ViewProviderCustom:
        ...
    
        def getIcon(self):
            return """
                   /* XPM */
                   static char *Some_icon_xpm[] = {
                   /* columns rows colors chars-per-pixel */
                   "16 16 3 1 ",
                   "  c None",
                   ". c #D71414",
                   "+ c #AA1919",
                   /* pixels */
                   "                ",
                   "  +          +  ",
                   " +.+        +.+ ",
                   "  +.+      +.+  ",
                   "   +        +   ",
                   "      ++++      ",
                   "     +....+     ",
                   "     +...++     ",
                   "     +..+++     ",
                   "     +.++.+     ",
                   "      ++++      ",
                   "   +        +   ",
                   "  +.+      +.+  ",
                   " +.+        +.+ ",
                   "  +          +  ",
                   "                "
                   };
                   """
    

See various examples in [Custom icon in tree view](/Custom_icon_in_tree_view
"Custom icon in tree view").

Expand[![](/images/thumb/8/8f/Power_user_hub.png/24px-
Power_user_hub.png)](/index.php?title=File:Power_user_hub.png&filetimestamp=20200511213015&)
[Power user documentation](/Power_users_hub "Power users hub")

  * **FreeCAD scripting:** [Python](/Python "Python"), [Introduction to Python](/Introduction_to_Python "Introduction to Python"), [Python scripting tutorial](/Python_scripting_tutorial "Python scripting tutorial"), [FreeCAD Scripting Basics](/FreeCAD_Scripting_Basics "FreeCAD Scripting Basics")

* * *

  * **Modules:** [Builtin modules](/Builtin_modules "Builtin modules"), [Units](/Units "Units"), [Quantity](/Quantity "Quantity")
  * **Workbenches:** [Workbench creation](/Workbench_creation "Workbench creation"), [Gui Commands](/Gui_Command "Gui Command"), [Commands](/Command "Command"), [Installing more workbenches](/Installing_more_workbenches "Installing more workbenches")
  * **Meshes and Parts:** [Mesh Scripting](/Mesh_Scripting "Mesh Scripting"), [Topological data scripting](/Topological_data_scripting "Topological data scripting"), [Mesh to Part](/Mesh_to_Part "Mesh to Part"), [PythonOCC](/PythonOCC "PythonOCC")

* * *

  * **Parametric objects:** [Scripted objects](/Scripted_objects "Scripted objects"), Viewproviders ([Custom icon in tree view](/Custom_icon_in_tree_view "Custom icon in tree view"))
  * **Scenegraph:** [Coin (Inventor) scenegraph](/Scenegraph "Scenegraph"), [Pivy](/Pivy "Pivy")
  * **Graphical interface:** [Interface creation](/Interface_creation "Interface creation"), [Interface creation completely in Python](/Dialog_creation "Dialog creation") ([1](/Dialog_creation_with_various_widgets "Dialog creation with various widgets"), [2](/Dialog_creation_reading_and_writing_files "Dialog creation reading and writing files"), [3](/Dialog_creation_setting_colors "Dialog creation setting colors"), [4](/Dialog_creation_image_and_animated_GIF "Dialog creation image and animated GIF"), [5](/PySide_usage_snippets "PySide usage snippets")), [PySide](/PySide "PySide"), PySide examples [beginner](/PySide_Beginner_Examples "PySide Beginner Examples"), [intermediate](/PySide_Intermediate_Examples "PySide Intermediate Examples"), [advanced](/PySide_Advanced_Examples "PySide Advanced Examples")
  * **Macros:** [Macros](/Macros "Macros"), [How to install macros](/How_to_install_macros "How to install macros")
  * **Embedding:** [Embedding FreeCAD](/Embedding_FreeCAD "Embedding FreeCAD"), [Embedding FreeCADGui](/Embedding_FreeCADGui "Embedding FreeCADGui")

* * *

  * **Other:** [Expressions](/Expressions "Expressions"), [Code snippets](/Code_snippets "Code snippets"), [Line drawing function](/Line_drawing_function "Line drawing function"), [FreeCAD vector math library](/FreeCAD_vector_math_library "FreeCAD vector math library") (deprecated)

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

