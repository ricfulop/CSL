---
url: https://wiki.freecad.org/Scripted_objects_migration
title: Scripted objects migration
scraped_at: 2025-09-08 16:46:31
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction
  * 2 Old object and new object Toggle Old object and new object subsection
    * 2.1 Old object
    * 2.2 New object
  * 3 Method 1. Migration by redirecting the class Toggle Method 1. Migration by redirecting the class subsection
    * 3.1 Advantages and disadvantages
  * 4 Method 2. Migration when restoring the document Toggle Method 2. Migration when restoring the document subsection
    * 4.1 Advantages and disadvantages
  * 5 Method 3. Migration when restoring the document, manually handling the properties Toggle Method 3. Migration when restoring the document, manually handling the properties subsection
    * 5.1 Advantages and disadvantages
  * 6 Addendum A. Creating the properties only if they do not already exist Toggle Addendum A. Creating the properties only if they do not already exist subsection
    * 6.1 Advantages and disadvantages
  * 7 Addendum B. Migrating different versions of the old object Toggle Addendum B. Migrating different versions of the old object subsection
    * 7.1 Advantages and disadvantages
  * 8 Addendum B2. Using internal class attributes instead of properties
  * 9 Addendum C. Method 3 without removing old properties that are named the same Toggle Addendum C. Method 3 without removing old properties that are named the same subsection
    * 9.1 Advantages and disadvantages
  * 10 Summary
  * 11 Links

# Scripted objects migration

  * [Page](/Scripted_objects_migration "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Scripted_objects_migration&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Scripted_objects_migration)
  * [Edit](/index.php?title=Scripted_objects_migration&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Scripted_objects_migration&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Scripted_objects_migration.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Scripted_objects_migration&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Scripted_objects_migration)
  * [Edit](/index.php?title=Scripted_objects_migration&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Scripted_objects_migration&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Scripted_objects_migration&action=history)

General

  * [What links here](/Special:WhatLinksHere/Scripted_objects_migration "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Scripted_objects_migration "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Scripted_objects_migration&oldid=1602823 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Scripted_objects_migration&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Scripted_objects_migration&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Scripted+objects+migration&action=page&filter=&language=en)This is the
approved revision of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Scripted+objects+migration&language=&task=view "Start translation for this language")
  * [Deutsch](/Scripted_objects_migration/de "Migration geskripteter Objekte \(65% translated\)")
  * English
  * [français](/Scripted_objects_migration/fr "Migration d'objets créés par script \(100% translated\)")
  * [italiano](/Scripted_objects_migration/it "Migrazione di oggetti creati con script \(3% translated\)")
  * [polski](/Scripted_objects_migration/pl "Obiekty tworzone skryptami, migracja \(100% translated\)")
  * [русский](/Scripted_objects_migration/ru "Scripted objects migration/ru \(0% translated\)")

## Introduction

[Scripted objects](/Scripted_objects "Scripted objects") are rebuilt every
time a [FCStd document](/File_Format_FCStd "File Format FCStd") is opened. To
do this the document keeps a reference to the module and Python class that
were used to create the object, along with its properties.

    
    
    <Document SchemaVersion="4" ProgramVersion="0.19R20959 (Git)" FileVersion="1">
        ...
        <Properties Count="15" TransientCount="3">
        ...
        </Properties>
        <Objects Count="1" Dependencies="1">
            <ObjectDeps Name="Custom" Count="0"/>
            <Object type="Part::FeaturePython" name="Custom" id="2715" Touched="1" />
        </Objects>
        <ObjectData Count="1">
            <Object name="Custom">
                <Properties Count="9" TransientCount="0">
                    ...
                    <Property name="Proxy" type="App::PropertyPythonObject" status="1">
                        <Python value="eyJUeXBlIjogIkN1c3RvbSJ9" encoded="yes" module="old_module" class="OldObject"/>
                    </Property>
                    ...
                </Properties>
            </Object>
        </ObjectData>
    </Document>
    

Particularly focus on this part:

    
    
    ...
                    <Property name="Proxy" type="App::PropertyPythonObject" status="1">
                        <Python value="eyJUeXBlIjogIkN1c3RvbSJ9" encoded="yes" module="old_module" class="OldObject"/>
                    </Property>
                    ...
    

If the value of `module=` or `class=` is not found on the installed system,
the object will fail to load correctly. This means that once an object is
created using a particular class, the module should no longer be moved or
renamed because if this is done, previously saved objects will break.

However, a valid reason for moving or renaming the module or class is to
improve the structure and maintainability of the original code, for example,
when restructuring an entire workbench. In this case there are various
strategies to migrate old objects to using a new class. This is done in order
to retain backwards compatibility, when outright breaking of old documents
must be avoided.

## Old object and new object

### Old object

An old object is defined in a module which is at the root of the workbench.

    
    
    # old_module.py
    class OldObject:
        def __init__(self, obj):
            obj.addProperty("App::PropertyLength", "Length")
            obj.addProperty("App::PropertyArea", "Area")
            obj.Length = 15
            obj.Area = 300
            obj.Proxy = self
            self.Type = "Custom"
    
        def execute(self, obj):
            pass
    

An object can be created using this class, and it can be saved to
my_document.FCstd. If no particular [viewprovider](/Viewprovider
"Viewprovider") is assigned to the new object, its proxy class is simply set
to a value different from `None`, in this case, to `1`.

    
    
    import FreeCAD as App
    import old_module
    
    doc = App.newDocument()
    doc.FileName = "my_document.FCStd"
    
    obj = doc.addObject("Part::FeaturePython", "Custom")
    old_module.OldObject(obj)
    
    if App.GuiUp:
        obj.ViewObject.Proxy = 1
    
    doc.recompute()
    doc.save()
    

[Python console](/Python_console "Python console") session with the basic
properties omitted.

    
    
    >>> obj = App.ActiveDocument.Custom
    >>> print(obj.PropertiesList)
    ['Area', ..., ..., ..., 'Length', ..., ..., ..., ...]
    >>> print(obj.Proxy)
    <old_module.OldObject object at 0x7efc3c51c390>
    

### New object

Now we consider that the workbench is restructured, so that classes aren't
just at the root directory, but instead are inside an objects directory.
Complex workbenches that have many different types of objects should be
structured in directories including objects, [viewproviders](/Viewprovider
"Viewprovider"), [Gui Commands](/Command "Command"), [task panel](/Task_panel
"Task panel") interfaces, etc.

    
    
    # objects/new_module.py
    class NewObject:
        def __init__(self, obj):
            obj.addProperty("App::PropertyLength", "Length")
            obj.addProperty("App::PropertyArea", "GeneralArea")
            obj.addProperty("App::PropertyInteger", "Divisions")
            obj.Length = 30
            obj.GeneralArea = 600
            obj.Divisions = 4
            obj.Proxy = self
            self.Type = "Custom"
    
        def execute(self, obj):
            pass
    

This new class will refer to the same type of object, but both the module name
as well as the class name have been renamed. Moreover, the properties also
have changed; one property has been renamed, and a completely new property has
been added.

If we create a new object with this new module we will have the following
console session.

    
    
    >>> obj2 = App.ActiveDocument.Custom2
    >>> print(obj2.PropertiesList)
    ['Divisions', ..., 'GeneralArea', ..., ..., 'Length', ..., ..., ..., ...]
    >>> print(obj2.Proxy)
    <objects.new_module.NewObject object at 0x7efc1cf68c50>
    

## Method 1. Migration by redirecting the class

We will migrate the older object by redirecting the old class. The original
class is deleted, and the name of the class is simply redirected to point to
the new class.

    
    
    # old_module.py
    import objects.new_module as new_module
    
    OldObject = new_module.NewObject
    

Any document that tries to load `old_module.OldObject` will be redirected to
load `objects.new_module.NewObject` instead.

If we open the document, and inspect the properties of the object in the
[Python console](/Python_console "Python console") we will see that the older
properties are conserved, but the object has a new Proxy class.

    
    
    >>> obj = App.ActiveDocument.Custom
    >>> print(obj.PropertiesList)
    ['Area', ..., ..., ..., 'Length', ..., ..., ..., ...]
    >>> print(obj.Proxy)
    <objects.new_module.NewObject object at 0x7f099700b2b0>
    

However, in this case we don't see the new properties of the new class. The
reason is simply that the older object didn't have these properties. When
`old_module.OldObject` was redirected to `objects.new_module.NewObject`, only
the proxy class changed, but previous information was retained.

Now, if the document is saved and opened again, it will automatically look for
`objects.new_module.NewObject`, and it will not require `old_module.OldObject`
any more. The old_module.py file may be removed permanently from the system as
long as all older objects have been migrated to the new module. If the old
module is removed but an object hasn't been migrated, the [report
view](/Report_view "Report view") will show a message like this when opening a
document containing such object.

    
    
    <class 'ModuleNotFoundError'>: No module named 'old_module'
    

If it is not realistically possible to migrate all older objects, say, because
the old module was used in a workbench for many years, then old_module.py must
be kept as long as it's deemed necessary to give users the opportunity to
migrate their objects.

### Advantages and disadvantages

**Advantages**

  * [![](/images/d/d4/Edit_OK.svg)](/index.php?title=File:Edit_OK.svg&filetimestamp=20240704192428&) This is the simplest method that just requires redirecting an old class to a new class.
  * [![](/images/d/d4/Edit_OK.svg)](/index.php?title=File:Edit_OK.svg&filetimestamp=20240704192428&) Old properties are conserved as long as the new class doesn't override them.
  * [![](/images/d/d4/Edit_OK.svg)](/index.php?title=File:Edit_OK.svg&filetimestamp=20240704192428&) This is good if the old class and the new class have the same properties (handle the same type of data) but only their module or class name is different.

**Disadvantages**

  * [![](/images/f/f6/Edit_Cancel.svg)](/index.php?title=File:Edit_Cancel.svg&filetimestamp=20240704192407&) The new class keeps the old properties of the object, which is not always desired.
  * [![](/images/f/f6/Edit_Cancel.svg)](/index.php?title=File:Edit_Cancel.svg&filetimestamp=20240704192407&) New properties or renamed properties aren't handled, so the object will load but it may not show the correct behavior of the new class.
  * [![](/images/f/f6/Edit_Cancel.svg)](/index.php?title=File:Edit_Cancel.svg&filetimestamp=20240704192407&) The old module may have to be kept indefinitely to migrate all old objects created in the past.

## Method 2. Migration when restoring the document

We will migrate the older object by modifying the old class. The majority of
the original class is deleted, and instead the `onDocumentRestored` method is
implemented. When this method exists, it will run when the document tries to
restore an object that uses the class, so this is the opportunity that we have
to assign a new class, manipulate the information, or print messages.

In this case, we assume that we have also defined a new
[viewprovider](/Viewprovider "Viewprovider") in the module viewp/new_view.py.
If we don't want to migrate this class, we may omit everything after the
`App.GuiUp` check.

    
    
    # old_module.py
    import FreeCAD as App
    import objects.new_module as new_module
    import viewp.new_view as new_view
    _wrn = App.Console.PrintWarning
    
    class OldObject:
        def onDocumentRestored(self, obj):
            new_module.NewObject(obj)
            _wrn("New proxy class used\n")
    
            if App.GuiUp:
                new_view.ViewProviderNew(obj.ViewObject)
                _wrn("New viewprovider class used\n")
    

A more complex example checks first that the proxy class is of the type that
we are looking for, and only proceeds with the migration if it's the right
type.

    
    
    class OldObject:
        def onDocumentRestored(self, obj):
            if hasattr(obj, "Proxy") and obj.Proxy.Type == "Custom":
                _module = str(obj.Proxy.__class__)
                _module = _module.lstrip("<class '").rstrip("'>")
    
                if _module == "old_module.OldObject":
                    self._migrate(obj)
    
        def _migrate(self, obj):
            _wrn("New proxy class used\n")
            new_module.NewObject(obj)
    
            if App.GuiUp:
                new_view.ViewProviderNew(obj.ViewObject)
                _wrn("New viewprovider class used\n")
    

Assuming that we already changed the old module in this way, if we open a
document with an old object, we will see the messages mentioning the use of
the new classes.

Inspecting the object from the [Python console](/Python_console "Python
console") we will see that the older properties are conserved, and in
addition, new properties were added together with the new Proxy class.

    
    
    >>> obj = App.ActiveDocument.Custom
    >>> print(obj.PropertiesList)
    ['Area', 'Divisions', ..., 'GeneralArea', ..., ..., 'Length', 'Length1', ..., ..., ..., ...]
    >>> print(obj.Proxy)
    <objects.new_module.NewObject object at 0x7fecb0ebd7b8>
    

The old properties were `Area` and `Length`; the new properties are
`Divisions`, `GeneralArea`, and `Length`. The migrated object retains the
original two properties, and gains three new properties. However, since the
new `Length` has the same name as the older property, the new property is
renamed with an incremental number. Presumably this is not what we want. We
can improve the situation by following the addendum 2.1 below.

Given that the classes are meant to handle the same type of object, we would
like a migration in which `Area` transforms into `GeneralArea`, and `Length`
is simply assigned to the new `Length`, and there are no duplicate properties.

### Advantages and disadvantages

**Advantages**

  * [![](/images/d/d4/Edit_OK.svg)](/index.php?title=File:Edit_OK.svg&filetimestamp=20240704192428&) This method allows us to check that the class that we are migrating is the right class, instead of simply redirecting to a newer class.
  * [![](/images/d/d4/Edit_OK.svg)](/index.php?title=File:Edit_OK.svg&filetimestamp=20240704192428&) Similar to method 1, old properties are kept as long as the new class doesn't override them.
  * [![](/images/d/d4/Edit_OK.svg)](/index.php?title=File:Edit_OK.svg&filetimestamp=20240704192428&) Unlike method 1, new properties are always added, however if they have the same name, they will be renamed.
  * [![](/images/d/d4/Edit_OK.svg)](/index.php?title=File:Edit_OK.svg&filetimestamp=20240704192428&) The migration is not immediate, we can still manipulate the information, or print messages while the object loads.

**Disadvantages**

  * [![](/images/f/f6/Edit_Cancel.svg)](/index.php?title=File:Edit_Cancel.svg&filetimestamp=20240704192407&) It is more verbose than method 1 because we need to implement the `onDocumentRestored` method to migrate the object.
  * [![](/images/f/f6/Edit_Cancel.svg)](/index.php?title=File:Edit_Cancel.svg&filetimestamp=20240704192407&) It always adds the new properties, so it may create duplicated properties in case the new properties have the same name as the old properties. This has to be handled manually.

## Method 3. Migration when restoring the document, manually handling the
properties

This is an extension of method 2. In the `onDocumentRestored` method we need
to save the values of the properties that we want, and then we can remove
these original properties. This is done so that when the new class is used, it
will assign the new properties without risking name collisions with the older
properties.

Like in method 2, if we want we can also add the piece of code that checks
that the Proxy class is the right one. In this example once more we assume
that we are using a custom [viewprovider](/Viewprovider "Viewprovider"), with
at least one custom property.

    
    
    # old_module.py
    import FreeCAD as App
    import objects.new_module as new_module
    import viewp.new_view as new_view
    _wrn = App.Console.PrintWarning
    
    class OldObject:
        def onDocumentRestored(self, obj):
            old = dict()
            old["Area"] = obj.Area
            old["Length"] = obj.Length
            obj.removeProperty("Area")
            obj.removeProperty("Length")
    
            new_module.NewObject(obj)
    
            obj.GeneralArea = 3 * old["Area"]
            obj.Length = old["Length"]
            _wrn("New proxy class used; properties migrated\n")
    
            if App.GuiUp:
                vobj = obj.ViewObject
                old = dict()
    
                old["LineScale"] = vobj.LineScale
                vobj.removeProperty("LineScale")
    
                new_view.ViewProviderNew(vobj)
    
                vobj.LineScale = 1.05 * old["LineScale"]
                _wrn("New viewprovider class used; view properties migrated\n")
    

We can see that the old values are stored in an auxiliary dictionary, then the
old properties are removed, then we add the new class, and finally we assign
the previously saved values to the new properties. In this moment we can
transform the saved values as necessary for the new class. For example, the
`GeneralArea` is set to 3 times the old `Area`, and the new `Length` simply
receives the value of the old `Length`. As we know how the old and new classes
are supposed to behave, we have the liberty of manipulating the data to
migrate the object as we want.

We can only remove properties that were added by [Python](/Python "Python")
classes when we built the [scripted object](/Scripted_objects "Scripted
objects"). Other attributes belong to the base C++ object and can't be
removed.

    
    
    >>> obj.removeProperty("Visibility")
    False
    

Assuming that we already changed the old module in this way, if we open a
document with an old object, we will see the messages mentioning the use of
the new classes. Inspecting the object from the [Python
console](/Python_console "Python console") we see that the older properties
are removed, and only the new properties exist.

    
    
    >>> obj = App.ActiveDocument.Custom
    >>> print(obj.PropertiesList)
    ['Divisions', ..., 'GeneralArea', ..., ..., 'Length', ..., ..., ..., ...]
    >>> print(obj.Proxy)
    <objects.new_module.NewObject object at 0x7efd456c9b00>
    

Since in the old class the `Divisions` property didn't exist, nothing was done
with it. It simply was created by the new `objects.new_module.NewObject`
class.

### Advantages and disadvantages

**Advantages**

  * [![](/images/d/d4/Edit_OK.svg)](/index.php?title=File:Edit_OK.svg&filetimestamp=20240704192428&) Similar to method 2, this method allows us to check that the class that we are migrating is the right class.
  * [![](/images/d/d4/Edit_OK.svg)](/index.php?title=File:Edit_OK.svg&filetimestamp=20240704192428&) We have complete control of what to do with the old properties. Typically they will be removed so that there is no name collision with new properties added. Thus we avoid duplicated properties.
  * [![](/images/d/d4/Edit_OK.svg)](/index.php?title=File:Edit_OK.svg&filetimestamp=20240704192428&) By saving the older values, we can manipulate the information in the restoring step as we want, and assign the corresponding values to the new properties.

**Disadvantages**

  * [![](/images/f/f6/Edit_Cancel.svg)](/index.php?title=File:Edit_Cancel.svg&filetimestamp=20240704192407&) This method is very verbose compared to the previous ones, because we must implement the `onDocumentRestored` method, and handle each of the properties individually (save value, delete property, re-assign value). This is problematic if the object that we want to migrate has many properties, or their values need to be transformed in very special ways.

## Addendum A. Creating the properties only if they do not already exist

One of the disadvantages of method 2 is that it will always try to add the new
properties. If the older properties have the same name as the new properties,
they will be duplicated with an incremental number, so `Length` will result in
`Length1`, then `Length2`, and so on. This makes method 2 an unrealistic
option in most cases, because the new class will only use one property anyway.

To improve this method, the new class can also be modified to only add the
properties if they don't already exist by the same name.

    
    
    # objects/new_module.py
    class NewObject:
        def __init__(self, obj):
            if not hasattr(obj, "Length"):
                obj.addProperty("App::PropertyLength", "Length")
                obj.Length = 30
            if not hasattr(obj, "GeneralArea"):
                obj.addProperty("App::PropertyArea", "GeneralArea")
                obj.GeneralArea = 600
            if not hasattr(obj, "Divisions"):
                obj.addProperty("App::PropertyInteger", "Divisions")
                obj.Divisions = 4
    
            obj.Proxy = self
            self.Type = "Custom"
    
        def execute(self, obj):
            pass
    

In this case, since `Length` already exists, it won't be added again;
`GeneralArea` and `Divisions` don't exist, so these will be added. And just
like before, `Area` will be retained because it is not explicitly removed,
although possibly it is no longer used in the new class.

    
    
    >>> obj = App.ActiveDocument.Custom
    >>> print(obj.PropertiesList)
    ['Area', 'Divisions', ..., 'GeneralArea', ..., ..., 'Length', ..., ..., ..., ...]
    >>> print(obj.Proxy)
    <objects.new_module.NewObject object at 0x7f036bd4c6a0>
    

The same can be done for the class of the [viewprovider](/Viewprovider
"Viewprovider").

By using this method 2 + A, the result is similar to method 1 in that the
object will retain all previous properties, but in addition it will gain the
new properties provided by the new class.

Method 3 does not need this addendum to the new class because the older
properties are explicitly removed, so there won't be any conflicts when
installing the new properties. Nevertheless, it is still a good practice that
every class adds its required properties only if these don't already exist.
This is helpful both in the case of creating new [scripted
objects](/Scripted_objects "Scripted objects") or in migrating them.

### Advantages and disadvantages

**Advantages**

  * [![](/images/d/d4/Edit_OK.svg)](/index.php?title=File:Edit_OK.svg&filetimestamp=20240704192428&) The object will retain all previous properties, but in addition it will gain new properties without repetition.

**Disadvantages**

  * [![](/images/f/f6/Edit_Cancel.svg)](/index.php?title=File:Edit_Cancel.svg&filetimestamp=20240704192407&) Like method 2, it still doesn't deal with renamed properties. The old properties should be manually removed.

## Addendum B. Migrating different versions of the old object

Method 3 is the most complex method because the properties are handled
individually. However, in this method we also have full flexibility in how we
manipulate the data, and this is an advantage if we want to do complex
operations.

If from the beginning we create a property that holds the version number of
our object, we can use this number in the future to perform specific migration
from that version to any other. We set the property to be read-only, so that
we cannot overwrite it in the [property editor](/Property_editor "Property
editor"), although it is still accessible from the [Python
console](/Python_console "Python console").

    
    
    # old_module.py
    class OldObject:
        def __init__(self, obj):
            obj.addProperty("App::PropertyLength", "Length")
            obj.addProperty("App::PropertyArea", "Area")
            obj.addProperty("App::PropertyString", "Version")
            obj.setEditorMode("Version", 1)
            obj.Length = 15
            obj.Area = 300
            obj.Version = "0.18"
            obj.Proxy = self
            self.Type = "Custom"
    
        def execute(self, obj):
            pass
    

Then, when we want to migrate the object, we implement the
`onDocumentRestored` method, and test for this version.

    
    
    # old_module.py
    import FreeCAD as App
    import objects.new_module as new_module
    _wrn = App.Console.PrintWarning
    
    class OldObject:
        def onDocumentRestored(self, obj):
            if hasattr(obj, "Version") and obj.Version:
                if obj.Version == "0.18":
                    _migrate_from_018(obj)
                elif obj.Version == "0.19":
                    _migrate_from_019(obj)
    
    def _migrate_from_018(obj):
        old = dict()
        old["Area"] = obj.Area
        old["Length"] = obj.Length
        obj.removeProperty("Area")
        obj.removeProperty("Length")
        obj.removeProperty("Version")
    
        new_module.NewObject(obj)
    
        obj.GeneralArea = 3 * old["Area"]
        obj.Length = old["Length"]
        obj.Version = "0.20"
        _wrn("New proxy class used; properties migrated\n")
    
    def _migrate_from_019(obj):
        ...
    

We don't save the `Version` value as we will set a new `Version` number when
doing the migration. As shown in the example, we can implement various
functions for each corresponding version of the object that we intend to
migrate. We omit the migration of the [viewprovider](/Viewprovider
"Viewprovider") properties but it follows the same pattern.

### Advantages and disadvantages

**Advantages**

  * [![](/images/d/d4/Edit_OK.svg)](/index.php?title=File:Edit_OK.svg&filetimestamp=20240704192428&) We have complete control of what to do with the old properties, and how to perform the migration.
  * [![](/images/d/d4/Edit_OK.svg)](/index.php?title=File:Edit_OK.svg&filetimestamp=20240704192428&) We can implement a particular method to migrate a particular version of the old object.

**Disadvantages**

  * [![](/images/f/f6/Edit_Cancel.svg)](/index.php?title=File:Edit_Cancel.svg&filetimestamp=20240704192407&) This method is very verbose because we must have a clear idea on how to handle each of the properties of each "version" that we want to migrate. If our object has many different versions created over the years, we may have to prepare a long list of methods to migrate them to the newest object.

## Addendum B2. Using internal class attributes instead of properties

Instead of using a [property](/Property "Property") of the object to hold the
version information, we can use an attribute of the class. In this way we
"hide" the version information, because properties are normally public, and
visible in the [property editor](/Property_editor "Property editor"), while
class attributes can only be manipulated from the [Python
console](/Python_console "Python console"). Class attributes can be saved and
restored as explained in [Scripted objects saving
attributes](/Scripted_objects_saving_attributes "Scripted objects saving
attributes").

    
    
    # old_module.py
    class OldObject:
        def __init__(self, obj):
            obj.addProperty("App::PropertyLength", "Length")
            obj.addProperty("App::PropertyArea", "Area")
            obj.Length = 15
            obj.Area = 300
            obj.Proxy = self
    
            self.Type = "Custom"
            self.ver = "0.18"
    
        def execute(self, obj):
            pass
    

This attribute is inspected by looking at the `Proxy` attribute.

    
    
    >>> obj = App.ActiveDocument.Custom
    >>> print(obj.Proxy.ver)
    0.18
    

Then the file is modified to migrate the object.

    
    
    # old_module.py
    import FreeCAD as App
    import objects.new_module as new_module
    _wrn = App.Console.PrintWarning
    
    class OldObject:
        def onDocumentRestored(self, obj):
            if hasattr(obj.Proxy, "ver") and obj.Proxy.ver:
                if obj.Proxy.ver == "0.18":
                    _migrate_from_018(obj)
    
    def _migrate_from_018(obj):
        old = dict()
        old["Area"] = obj.Area
        old["Length"] = obj.Length
        obj.removeProperty("Area")
        obj.removeProperty("Length")
    
        new_module.NewObject(obj)
    
        obj.GeneralArea = 3 * old["Area"]
        obj.Length = old["Length"]
        _wrn("New proxy class used; properties migrated\n")
    

When we install the new class, this new class should set the new value of the
version attribute, for example, `self.ver = "0.20"`.

## Addendum C. Method 3 without removing old properties that are named the
same

Like in Addendum A, we can write the new class to create properties only if
they aren't already present. Using method 3, we save the values of the older
properties, and subsequently delete the older properties. However, if the new
properties are named the same as the older ones, we don't need to delete the
older ones, we can just reuse the same property, as we know the property won't
be duplicated. If we are using Addendum B, we have a way to query the version
as well.

    
    
    # old_module.py
    import FreeCAD as App
    import objects.new_module as new_module
    _wrn = App.Console.PrintWarning
    
    class OldObject:
        def onDocumentRestored(self, obj):
            if hasattr(obj, "Version") and obj.Version:
                if obj.Version == "0.18":
                    _migrate_from_018(obj)
    
    def _migrate_from_018(obj):
        old = dict()
        old["Area"] = obj.Area
        obj.removeProperty("Area")
    
        new_module.NewObject(obj)
    
        obj.GeneralArea = 3 * old["Area"]
        obj.Version = "0.20"
        _wrn("New proxy class used; properties migrated\n")
    

As we see in the example, the old `Area` property is deleted and migrated to
the new `GeneralArea` property as usual. We do not need to delete `Length` nor
`Version` because in the new class they are still used with the same name, and
they won't be created again (addendum A). As we don't want to modify `Length`,
this property is not touched at all; it is migrated to the new class silently.
However, we do update `Version` to the new value. We omit the migration of the
[viewprovider](/Viewprovider "Viewprovider") properties but it follows the
same pattern.

This should work like method 3, meaning that the old properties are removed
and only the new properties remain in the new object. The only difference is
that we omit removing and recreating the properties that are named the same.
This process should work as long as the old [property](/Property "Property")
and the new [property](/Property "Property") have the same type (for example,
`App::PropertyLength` or `App::PropertyArea`), so the old property can pass
its value directly. However, if the new property has a different type than the
old property, then the old property should be removed, otherwise the old
property will completely overwrite the new property, which is probably not
what we want because the new class will be expecting the new type and not the
old type.

### Advantages and disadvantages

**Advantages**

  * [![](/images/d/d4/Edit_OK.svg)](/index.php?title=File:Edit_OK.svg&filetimestamp=20240704192428&) Like method 3, this method allows us complete control of the migration of the old information.
  * [![](/images/d/d4/Edit_OK.svg)](/index.php?title=File:Edit_OK.svg&filetimestamp=20240704192428&) We avoid writing code that removes and recreates properties that are named the same.

**Disadvantages**

  * [![](/images/f/f6/Edit_Cancel.svg)](/index.php?title=File:Edit_Cancel.svg&filetimestamp=20240704192407&) Like method 3, this method is still very verbose because we have to handle the properties carefully.
  * [![](/images/f/f6/Edit_Cancel.svg)](/index.php?title=File:Edit_Cancel.svg&filetimestamp=20240704192407&) If a new [property](/Property "Property") and an old [property](/Property "Property") share the same name, the new property will be overwritten, which may be undesired behavior, especially if the two properties have different types. In this case, removing the old property, and migrating its value manually is still necessary.

## Summary

Each of the methods has a recommended use:

  * Method 1. The module is moved or renamed but the properties are the same. Simple redirection of classes because the properties don't need to be modified at all.
  * Method 2+A. Simple migration scenarios. Display a message when the object is migrated from one class to another. The properties are of the same type and don't need to be modified at all.
  * Method 3, 3+A, or 3+B. Complex migration scenarios. Full control of the properties, deleting the old properties, and adding new properties. An identifier to know the version of the object is useful to choose the right function to perform the migration (Addendum B or B2).

Preferably avoid the following:

  * Method 2. The properties will be duplicated if the new class doesn't check for existing properties (Addendum A).
  * Method 3+C. Use only when the old properties and the new properties are of the same type. Otherwise use method 3 or 3+B to remove older properties, and handle them exactly as needed.

## Links

  * [Migrating and upgrading old scripted objects](https://forum.freecad.org/viewtopic.php?t=42948)
  * [Migrate old scripted objects](https://forum.freecad.org/viewtopic.php?f=18&t=46218)

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

