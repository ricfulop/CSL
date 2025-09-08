---
url: https://wiki.freecad.org/Scripted_objects_saving_attributes
title: Scripted objects saving attributes
scraped_at: 2025-09-08 16:46:25
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction
  * 2 Saving all attributes
  * 3 Saving specific attributes
  * 4 Usage Toggle Usage subsection
    * 4.1 Identifying the type
    * 4.2 Migrating the object
  * 5 Links

# Scripted objects saving attributes

  * [Page](/Scripted_objects_saving_attributes "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Scripted_objects_saving_attributes&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Scripted_objects_saving_attributes)
  * [Edit](/index.php?title=Scripted_objects_saving_attributes&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Scripted_objects_saving_attributes&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Scripted_objects_saving_attributes.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Scripted_objects_saving_attributes&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Scripted_objects_saving_attributes)
  * [Edit](/index.php?title=Scripted_objects_saving_attributes&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Scripted_objects_saving_attributes&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Scripted_objects_saving_attributes&action=history)

General

  * [What links here](/Special:WhatLinksHere/Scripted_objects_saving_attributes "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Scripted_objects_saving_attributes "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Scripted_objects_saving_attributes&oldid=1601836 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Scripted_objects_saving_attributes&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Scripted_objects_saving_attributes&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Scripted+objects+saving+attributes&action=page&filter=&language=en)This is the
approved revision of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Scripted+objects+saving+attributes&language=&task=view "Start translation for this language")
  * [Deutsch](/Scripted_objects_saving_attributes/de "Gescriptete Objekte die Attribute speichern \(42% translated\)")
  * English
  * [français](/Scripted_objects_saving_attributes/fr "Sauvegarde des attributs des objets scripts \(100% translated\)")
  * [italiano](/Scripted_objects_saving_attributes/it "Oggetti creati con script che salvano gli attributi \(12% translated\)")
  * [polski](/Scripted_objects_saving_attributes/pl "Obiekty tworzone skryptami, zapis atrybutów \(100% translated\)")
  * [русский](/Scripted_objects_saving_attributes/ru "Scripted objects saving attributes/ru \(4% translated\)")

## Introduction

[Scripted objects](/Scripted_objects "Scripted objects") are rebuilt every
time a [FCStd document](/File_Format_FCStd "File Format FCStd") is opened. To
do this the document keeps a reference to the module and Python class that
were used to create the object, along with its properties.

Attributes of the class used to create the object can also be saved, that is,
"serialized". This can be further controlled by the `dumps` and `loads`
methods of the class.

## Saving all attributes

By default, attributes saved in an object class are those from the `__dict__`
dictionary of the class.

    
    
    # various_states.py
    class VariousStates:
        def __init__(self, obj):
            obj.addProperty("App::PropertyLength", "Length")
            obj.addProperty("App::PropertyArea", "Area")
            obj.Length = 15
            obj.Area = 300
            obj.Proxy = self
    
            Type = dict()
            Type["Version"] = "Custom"
            Type["Release"] = "production"
            self.Type = Type
            self.Type = "Custom"
            self.ver = "0.18"
            self.color = (0, 0, 1)
            self.width = 2.5
    
        def execute(self, obj):
            pass
    

An object can be created using this class, and it can be saved to
my_document.FCstd. If no particular [viewprovider](/Viewprovider
"Viewprovider") is assigned to the new object, its proxy class is simply set
to a value different from `None`, in this case, to `1`.

    
    
    import FreeCAD as App
    import various_states
    
    doc = App.newDocument()
    doc.FileName = "my_document.FCStd"
    
    obj = doc.addObject("Part::FeaturePython", "Custom")
    various_states.VariousStates(obj)
    
    if App.GuiUp:
        obj.ViewObject.Proxy = 1
    
    doc.recompute()
    doc.save()
    

When we re-open the file we can inspect the dictionary of the object's class.

    
    
    >>> obj = App.ActiveDocument.Custom
    >>> print(obj.Proxy)
    <various_states.VariousStates object at 0x7f0a899bde10>
    >>> print(obj.Proxy.__dict__)
    {'Type': {'Version': 'Custom', 'Release': 'production'}, 'ver': '0.18', 'color': [0, 0, 1], 'width': 2.5}
    

We see that all attributes that start with `self` in the class were saved.
These can be of different types, including string, list, float, and
dictionary. The original tuple for `self.color` was converted to a list, but
otherwise all attributes were loaded the same.

## Saving specific attributes

We can define a class similar to the first one, that implements specific
attributes to save.

    
    
    # various_states.py
    class CustomStates:
        def __init__(self, obj):
            obj.addProperty("App::PropertyLength", "Length")
            obj.addProperty("App::PropertyArea", "Area")
            obj.Length = 15
            obj.Area = 300
            obj.Proxy = self
    
            Type = dict()
            Type["Version"] = "Custom"
            Type["Release"] = "production"
            self.Type = Type
            self.ver = "0.18"
            self.color = (0, 0, 1)
            self.width = 2.5
    
        def execute(self, obj):
            pass
    
        def dumps(self):
            return self.color, self.width
    
        def loads(self, state):
            self.color = state[0]
            self.width = state[1]
    

The return value of `dumps` is the object that will be serialized. This can be
a single value, or a tuple of values. When the object is restored, the class
calls the `loads` method, passing the `state` variable with the serialized
content. In this case `state` is a tuple that is unpacked into the respective
variables to reconstruct the "state" that original existed.

    
    
    state = (self.color, self.width)
    state = ((0, 0, 1), 2.5)
    

We can create an object with this class, and save the document, just like in
the previous example. When we re-open the file we can inspect the dictionary
of the object's class.

    
    
    >>> obj2 = App.ActiveDocument.Custom2
    >>> print(obj2.Proxy)
    <various_states.CustomStates object at 0x7fb399496630>
    >>> print(obj2.Proxy.__dict__)
    {'color': [0, 0, 1], 'width': 2.5}
    

The original tuple for `self.color` was converted to a list, but otherwise the
information was recovered fine. Instead of restoring all attributes like in
the previous case, only the attributes that we specified in `dumps` and
`loads` were restored.

## Usage

### Identifying the type

Normally, [scripted objects](/Scripted_objects "Scripted objects") should use
[properties](/Property "Property") to store information, as these are
automatically restored when the document is opened.

However, sometimes the class restore internal information which is not
intended to be modified, but which is helpful to inspect.

For example, most objects of the [Draft Workbench](/Draft_Workbench "Draft
Workbench") set up a `Type` attribute that can be used to determine the type
of object that is under use.

    
    
    class DraftObject:
        def __init__(self, obj, _type):
            self.Type = _type
    
        def dumps(self):
            return self.Type
    
        def loads(self, state):
            if state:
                self.Type = state
    

All objects have a `TypeId` property, but for [scripted
objects](/Scripted_objects "Scripted objects") this property is not useful, as
it always refers to the parent C++ class, for example,
[`Part::Part2DObjectPython`](/Part_Part2DObject "Part Part2DObject") or
[`Part::FeaturePython`](/Part_Feature "Part Feature"). Therefore, having this
additional `Proxy.Type` attribute in the class is useful to treat each object
in a particular way.

### Migrating the object

Version information can be stored inside the class in order to verify the
origin of an object.

    
    
    class CustomObject:
        def __init__(self, obj, _type):
            self.Type = _type
            self.version = "0.18"
    
        def dumps(self):
            return self.Type, self.version
    
        def loads(self, state):
            if state:
                self.Type = state[0]
                self.version = state[1]
    

If the structure of the class changes, that is, if its properties or methods
change, are renamed, or are removed, we could test the version attribute in
order to migrate the older object to a new set of properties or to a new
class. This can be done by implementing the `onDocumentRestored` method, as
explained in [Scripted objects migration](/Scripted_objects_migration
"Scripted objects migration").

    
    
    class CustomObject:
        def onDocumentRestored(self, obj):
            if hasattr(obj.Proxy, "version") and obj.Proxy.version:
                if obj.Proxy.version == "0.18":
                    self.migrate_from_018(obj)
    
        def migrate_from_018(self, obj):
            ...
    

## Links

  * [Scripted objects](/Scripted_objects "Scripted objects")
  * [Scripted objects migration](/Scripted_objects_migration "Scripted objects migration")
  * [FreeCAD Forum Discussion: Scripted Object Serialization: json or pickle?](https://forum.freecadweb.org/viewtopic.php?f=10&t=49120)

  * [obj.Proxy.Type is a dict, not a string](https://forum.freecadweb.org/viewtopic.php?f=18&t=44009), explanation of `dumps` and `loads` in the forum.
  * [The Pickle module](https://docs.python.org/3/library/pickle.html#object.__getstate__) in the Python documentation.

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

