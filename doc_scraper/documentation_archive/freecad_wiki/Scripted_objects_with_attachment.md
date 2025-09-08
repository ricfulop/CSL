---
url: https://wiki.freecad.org/Scripted_objects_with_attachment
title: Scripted objects with attachment
scraped_at: 2025-09-08 16:46:23
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction
  * 2 Making Scripted Objects Attachable Toggle Making Scripted Objects Attachable subsection
    * 2.1 Add Attach Extension
    * 2.2 Update Position Based on Attached Object
  * 3 Full and Complete Minimal Example
  * 4 References
  * 5 Tested With the Following FreeCAD Version

# Scripted objects with attachment

  * [Page](/Scripted_objects_with_attachment "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Scripted_objects_with_attachment&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Scripted_objects_with_attachment)
  * [Edit](/index.php?title=Scripted_objects_with_attachment&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Scripted_objects_with_attachment&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Scripted_objects_with_attachment.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Scripted_objects_with_attachment&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Scripted_objects_with_attachment)
  * [Edit](/index.php?title=Scripted_objects_with_attachment&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Scripted_objects_with_attachment&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Scripted_objects_with_attachment&action=history)

General

  * [What links here](/Special:WhatLinksHere/Scripted_objects_with_attachment "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Scripted_objects_with_attachment "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Scripted_objects_with_attachment&oldid=1602824 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Scripted_objects_with_attachment&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Scripted_objects_with_attachment&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Scripted+objects+with+attachment&action=page&filter=&language=en)This is the
approved revision of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Scripted+objects+with+attachment&language=&task=view "Start translation for this language")
  * [Deutsch](/Scripted_objects_with_attachment/de "Geskriptete Objekte mit Anhang \(95% translated\)")
  * English
  * [français](/Scripted_objects_with_attachment/fr "Objets créés par script avec ancrage \(100% translated\)")
  * [italiano](/Scripted_objects_with_attachment/it "Oggetti creati da script con parti associate \(11% translated\)")
  * [polski](/Scripted_objects_with_attachment/pl "Obiekty tworzone skryptami, z dołączeniem \(100% translated\)")
  * [русский](/Scripted_objects_with_attachment/ru "Scripted objects with attachment/ru \(0% translated\)")

## Introduction

The purpose of this page is to show a minimal example of [Part
EditAttachment](/Part_EditAttachment "Part EditAttachment") feature using
[Scripted objects](/Scripted_objects "Scripted objects") in Python.

See full and complete minimal example below.

The following GIF demonstrates attaching our custom box to a cylinder, and
automatically updating it's position when the cylinder's position changes.

[![](/images/b/b7/Box-attached-to-cylinder-
demo.gif)](/index.php?title=File:Box-attached-to-cylinder-
demo.gif&filetimestamp=20200505231024&)

**NOTE:** The box is our custom scripted object, and the cylinder is a regular
FreeCAD object generated from the Part workbench.

## Making Scripted Objects Attachable

### Add Attach Extension

First, we need to add the `Part::AttachExtensionPython` extension to our
`Part::FeaturePython` oject in the constructor, or `__init__` method, of our
custom scripted object.

    
    
    class Box():
        """Custom Scripted Box Object"""
    
        def __init__(self, obj):
            self.Type = 'Box'
    
            obj.Proxy = self
            
            ... custom properties
    
            # Needed to make this object "attachable"
            obj.addExtension('Part::AttachExtensionPython')
    

Without adding this code, we'll see the following warning dialog when
attaching our custom scripted object to another object.

[![](/images/4/4d/Part-attachment-warning-
dialog.png)](/index.php?title=File:Part-attachment-warning-
dialog.png&filetimestamp=20200505230856&)

### Update Position Based on Attached Object

Then, in the `execute` method of our custom scripted object, we need to call
the `positionBySupport` on our `Part::FeaturePython` object.

    
    
    class Box:
        
        ...
    
        def execute(self, obj):
            obj.positionBySupport()
            
            # Assign a Shape to obj
            obj.Shape = Part.makeBox(...)
    

Without calling `positionBySupport`, our custom scripted object won't update
it's position when the position of the attached-to object changes.

## Full and Complete Minimal Example

    
    
    import FreeCAD as App
    import Part
    
    
    class Box():
        """
        Simple Custom Box Object
        See Also:
            https://wiki.freecad.org/FeaturePython_Objects
        """
    
        def __init__(self, obj):
            """
            Constructor
            Arguments
            ---------
            - obj: an existing document object or an object created with FreeCAD.Document.addObject('Part::FeaturePython', '{name}').
            """
    
            self.Type = 'Box'
    
            obj.Proxy = self
            obj.addProperty('App::PropertyLength', 'Length',
                            'Dimensions', 'Box length').Length = 10.0
            obj.addProperty('App::PropertyLength', 'Width',
                            'Dimensions', 'Box width').Width = 10.0
            obj.addProperty('App::PropertyLength', 'Height',
                            'Dimensions', 'Box height').Height = 10.0
    
            # Needed to make this object "attachable",
            # or able to attach parameterically to other objects
            obj.addExtension('Part::AttachExtensionPython')
    
        def execute(self, obj):
            """
            Called on document recompute
            """
            # Needed to update position when attached-to object changes position.
            # Reposition object based on Support, MapMode and MapPathParameter properties.
            # Returns True if attachment calculation was successful, False if object is not attached and Placement wasn't updated,
            obj.positionBySupport()
    
            obj.Shape = Part.makeBox(obj.Length, obj.Width, obj.Height)
    
    
    def create_box(obj_name, document):
        """
        Create a Box.
        """
        obj = document.addObject('Part::FeaturePython', obj_name)
        Box(obj)
        obj.ViewObject.Proxy = 0  # Mandatory unless ViewProvider is coded
        return obj
    
    
    document = App.ActiveDocument
    if document is None:
        document = App.newDocument('Part Attachment Example')
    
    box = create_box('CustomBox', document)
    document.recompute()
    

## References

  * [Part EditAttachment](/Part_EditAttachment "Part EditAttachment")
  * [FreeCAD Forum - Parametric attachment of scripted object](https://forum.freecad.org/viewtopic.php?f=22&t=24794)
  * [FreeCAD Forum - Port attachment to be an extension](https://forum.freecad.org/viewtopic.php?f=10&t=18978&start=10)
  * [GitHub - freecad-part-attachment-python-example](https://github.com/gbroques/freecad-part-attachment-python-example)

## Tested With the Following FreeCAD Version

Tested with the following FreeCAD version information:

    
    
    OS: Ubuntu 18.04.3 LTS
    Word size of OS: 64-bit
    Word size of FreeCAD: 64-bit
    Version: 0.18.16146 (Git) AppImage
    Build type: Release
    Branch: (HEAD detached at 0.18.4)
    Hash: 980bf9060e28555fecd9e3462f68ca74007b70f8
    Python version: 3.6.7
    Qt version: 5.6.2
    Coin version: 4.0.0a
    OCC version: 7.3.0
    Locale: English/UnitedStates (en_US)
    

Note: For FreeCAD 0.19 this tutorial needs a minor update:

  * The second argument of the`addExtension` method got deprecated.
  * For details see [https://forum.freecad.org/viewtopic.php?f=10&t=54370](https://forum.freecad.org/viewtopic.php?f=10&t=54370)

Expand[![](/images/thumb/8/8f/Power_user_hub.png/24px-
Power_user_hub.png)](/index.php?title=File:Power_user_hub.png&filetimestamp=20200511213015&)
[Power user documentation](/Power_users_hub "Power users hub")

  * **FreeCAD scripting:** [Python](/Python "Python"), [Introduction to Python](/Introduction_to_Python "Introduction to Python"), [Python scripting tutorial](/Python_scripting_tutorial "Python scripting tutorial"), [FreeCAD Scripting Basics](/FreeCAD_Scripting_Basics "FreeCAD Scripting Basics")

* * *

  * **Modules:** [Builtin modules](/Builtin_modules "Builtin modules"), [Units](/Units "Units"), [Quantity](/Quantity "Quantity")
  * **Workbenches:** [Workbench creation](/Workbench_creation "Workbench creation"), [Gui Commands](/Gui_Command "Gui Command"), [Commands](/Command "Command"), [Installing more workbenches](/Installing_more_workbenches "Installing more workbenches")
  * **Meshes and Parts:** [Mesh Scripting](/Mesh_Scripting "Mesh Scripting"), [Topological data scripting](/Topological_data_scripting "Topological data scripting"), [Mesh to Part](/Mesh_to_Part "Mesh to Part"), [PythonOCC](/PythonOCC "PythonOCC")

* * *

  * **Parametric objects:** [Scripted objects](/Scripted_objects "Scripted objects"), [Viewproviders](/Viewprovider "Viewprovider") ([Custom icon in tree view](/Custom_icon_in_tree_view "Custom icon in tree view"))
  * **Scenegraph:** [Coin (Inventor) scenegraph](/Scenegraph "Scenegraph"), [Pivy](/Pivy "Pivy")
  * **Graphical interface:** [Interface creation](/Interface_creation "Interface creation"), [Interface creation completely in Python](/Dialog_creation "Dialog creation") ([1](/Dialog_creation_with_various_widgets "Dialog creation with various widgets"), [2](/Dialog_creation_reading_and_writing_files "Dialog creation reading and writing files"), [3](/Dialog_creation_setting_colors "Dialog creation setting colors"), [4](/Dialog_creation_image_and_animated_GIF "Dialog creation image and animated GIF"), [5](/PySide_usage_snippets "PySide usage snippets")), [PySide](/PySide "PySide"), PySide examples [beginner](/PySide_Beginner_Examples "PySide Beginner Examples"), [intermediate](/PySide_Intermediate_Examples "PySide Intermediate Examples"), [advanced](/PySide_Advanced_Examples "PySide Advanced Examples")
  * **Macros:** [Macros](/Macros "Macros"), [How to install macros](/How_to_install_macros "How to install macros")
  * **Embedding:** [Embedding FreeCAD](/Embedding_FreeCAD "Embedding FreeCAD"), [Embedding FreeCADGui](/Embedding_FreeCADGui "Embedding FreeCADGui")

* * *

  * **Other:** [Expressions](/Expressions "Expressions"), [Code snippets](/Code_snippets "Code snippets"), [Line drawing function](/Line_drawing_function "Line drawing function"), [FreeCAD vector math library](/FreeCAD_vector_math_library "FreeCAD vector math library") (deprecated)

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

