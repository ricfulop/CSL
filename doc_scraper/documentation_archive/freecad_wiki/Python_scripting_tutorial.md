---
url: https://wiki.freecad.org/Python_scripting_tutorial
title: Python scripting tutorial
scraped_at: 2025-09-08 16:41:19
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction
  * 2 Writing Python code
  * 3 Exploring FreeCAD
  * 4 Vectors and placements
  * 5 App and Gui
  * 6 Modules
  * 7 Mesh module
  * 8 Part module
  * 9 Draft module
  * 10 Interface
  * 11 Macros
  * 12 External scripts

# Python scripting tutorial

  * [Page](/Python_scripting_tutorial "View the content page \[ctrl-option-c\]")
  * [Discussion](/Talk:Python_scripting_tutorial "Discussion about the content page \[ctrl-option-t\]")

English

  * [Read](/Python_scripting_tutorial)
  * [Edit](/index.php?title=Python_scripting_tutorial&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Python_scripting_tutorial&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Python_scripting_tutorial.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Python_scripting_tutorial&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Python_scripting_tutorial)
  * [Edit](/index.php?title=Python_scripting_tutorial&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Python_scripting_tutorial&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Python_scripting_tutorial&action=history)

General

  * [What links here](/Special:WhatLinksHere/Python_scripting_tutorial "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Python_scripting_tutorial "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Python_scripting_tutorial&oldid=1296875 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Python_scripting_tutorial&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Python_scripting_tutorial&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Python+scripting+tutorial&action=page&filter=&language=en)This is the approved
revision of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Python+scripting+tutorial&language=&task=view "Start translation for this language")
  * [Bahasa Indonesia](/Python_scripting_tutorial/id "Python scripting tutorial \(1% translated\)")
  * [Deutsch](/Python_scripting_tutorial/de "Anleitung Skripterstellung mit Python \(100% translated\)")
  * English
  * [Türkçe](/Python_scripting_tutorial/tr "Python betik kılavuzu \(3% translated\)")
  * [español](/Python_scripting_tutorial/es "Python Tutorial de guionización \(80% translated\)")
  * [français](/Python_scripting_tutorial/fr "Tutoriel sur les scripts Python \(100% translated\)")
  * [italiano](/Python_scripting_tutorial/it "Guida agli Script Python \(100% translated\)")
  * [polski](/Python_scripting_tutorial/pl "Poradnik: Tworzenie skryptów Python \(100% translated\)")
  * [português](/Python_scripting_tutorial/pt "Tutoriais de programação Python \(1% translated\)")
  * [português do Brasil](/Python_scripting_tutorial/pt-br "Tutorial de script em Python \(10% translated\)")
  * [română](/Python_scripting_tutorial/ro "Tutorial de programare Python \(14% translated\)")
  * [čeština](/Python_scripting_tutorial/cs "Python scripting tutorial/cs \(0% translated\)")
  * [русский](/Python_scripting_tutorial/ru "Руководство по скриптам Python \(72% translated\)")
  * [中文（中国大陆）](/Python_scripting_tutorial/zh-cn "Python脚本教程 \(16% translated\)")
  * [日本語](/Python_scripting_tutorial/ja "Pythonスクリプトのチュートリアル \(35% translated\)")
  * [한국어](/Python_scripting_tutorial/ko "파이썬 스크립트 자습서 \(12% translated\)")

![](/images/6/6f/Arrow-left.svg) [Introduction to
Python](/Introduction_to_Python "Introduction to Python")

[FreeCAD Scripting Basics](/FreeCAD_Scripting_Basics "FreeCAD Scripting
Basics") ![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

## Introduction

[Python](https://en.wikipedia.org/wiki/Python_%28programming_language%29) is a
programming language that it relatively easy to learn and understand. It is
open-source and multi-platform, and can be used for many purposes: from simple
shell scripts to very complex programs. But its most widespread use is as a
scripting language embedded in other applications. That is how it is used
inside FreeCAD. From the [Python console](/Python_console "Python console"),
or from custom scripts, you can control FreeCAD and make it perform very
complex operations.

For example, from a Python script, you can:

  * Create new objects.
  * Modify existing objects.
  * Modify the 3D representation of those objects.
  * Modify the FreeCAD interface.

There are several ways to use Python in FreeCAD:

  * From the [FreeCAD Python interpreter](/FreeCAD_Scripting_Basics "FreeCAD Scripting Basics"), where you can issue commands in a "command line"-style interface.
  * From [macros](/Macros "Macros"), which are a convenient way to quickly add a missing tool to the FreeCAD interface.
  * From external scripts, which can used to create quite complex solutions, even entire [Workbenches](/Workbenches "Workbenches").

In this tutorial, we'll work on a couple of basic examples to get you started,
but there is much more [documentation about Python scripting](/Power_users_hub
"Power users hub") available on this wiki. If you are totally new to Python
and want to understand how it works, we also have a basic [introduction to
Python](/Introduction_to_Python "Introduction to Python").

Before proceeding with Python scripting, go to **Edit → Preferences → General
→ Report view** and check two boxes:

  * **Redirect internal Python output to report view**.
  * **Redirect internal Python errors to report view**.

Then go to **View → Panels** and check:

  * **Report view**.

## Writing Python code

There are two ways to write Python code in FreeCAD. In the [Python
console](/Python_console "Python console") (select **View → Panels → Python
console** from the menu) or in the [Macro editor](/Std_DlgMacroExecute "Std
DlgMacroExecute") (select **Macro → Macros...** from the menu). In the console
you write Python commands one by one, executing them by pressing Enter, while
macros can contain more complex code made up of several lines, executed only
when the macro is executed.

[![](/images/9/98/Screenshot_pythoninterpreter.jpg)](/index.php?title=File:Screenshot_pythoninterpreter.jpg&filetimestamp=20090202153113&)

The FreeCAD Python console

In this tutorial you can use both methods. You can copy-paste each line in the
Python console and then press Enter, or copy-paste the entire code in a new
Macro window.

Top

## Exploring FreeCAD

Let's start by creating a new empty document:

    
    
    doc = FreeCAD.newDocument()
    

If you type this in the FreeCAD Python console, you will notice that as soon
as you type `FreeCAD.` a window pops up, allowing to quickly autocomplete the
rest of your line. Even better, each entry in the autocomplete list has a
tooltip explaining what it does. This makes it easier to explore the available
functionality. Before choosing `newDocument`, have a look at the other
options.

[![](/images/f/f2/Screenshot_classbrowser.jpg)](/index.php?title=File:Screenshot_classbrowser.jpg&filetimestamp=20090202153040&)

The autocomplete mechanism of the FreeCAD Python console

Now our new document will be created. This is similar to pressing the
[![](/images/d/d4/Std_New.svg)](/index.php?title=File:Std_New.svg&filetimestamp=20240528091658&)
[New](/Std_New "Std New") button on the toolbar. In fact most buttons in
FreeCAD do nothing more than execute one or more lines of Python code. Even
better, you can set an option in **Edit → Preferences → Python → Macro** to
**Show script commands in python console**. This will print in the console all
Python code executed when you press buttons. Very useful for learning how to
reproduce actions in Python.

Now let's get back to our document and see what we can do with it:

    
    
    doc.
    

Explore the available options. Usually names that begin with a capital letter
are attributes, they contain a value, while names that begin with a lower case
letter are functions (also called methods), they "do something". Names that
begin with an underscore are usually there for the internal working of the
module, and you shouldn't care about them. Let's use one of the methods to add
a new object to our document:

    
    
    box = doc.addObject("Part::Box", "myBox")
    

Nothing happens. Why? Because FreeCAD is made for the big picture. One day, it
will work with hundreds of complex objects, all depending each other. Making a
small change somewhere could have a big impact; you may need to recalculate
the whole document which could take a long time. For that reason almost no
command updates the scene automatically. You must do it manually:

    
    
    doc.recompute()
    

Now our box appeared. Many of the buttons that add objects in FreeCAD actually
do two things: add the object, and recompute. If you turned on the **Show
script commands in python console** option above, try adding a sphere with the
GUI button; you'll see the two lines of Python code being executed one after
the other.

Now let's explore the contents of our box:

    
    
    box.
    

You'll immediately see a couple of very interesting things such as:

    
    
    box.Height
    

This will print the current height of our box. Now let's try to change that:

    
    
    box.Height = 5
    

If you select your box with the mouse, you'll see that in the [Property
editor](/Property_editor "Property editor"), on the **Data** tab, our
Data**Height** property appears. All properties of a FreeCAD object that
appear there (and also on the **View** tab, more about that later), are
directly accessible in Python too, by their names, like we did with the
Data**Height** property. Try changing the other dimensions of the box.

Top

## Vectors and placements

[Vectors](https://en.wikipedia.org/wiki/Euclidean_vector) are a very
fundamental concept in any 3D application. A vector is a list of 3 numbers (x,
y and z), describing a point or position in 3D space. Many things can be done
with vectors, such as additions, subtractions, projections and [much
more](https://en.wikipedia.org/wiki/Vector_space). In FreeCAD vectors work
like this:

    
    
    myvec = FreeCAD.Vector(2, 0, 0)
    myvec.x
    myvec.y
    othervec = FreeCAD.Vector(0, 3, 0)
    sumvec = myvec.add(othervec)
    

Another common feature of FreeCAD objects is their [placement](/Placement
"Placement"). Each object has a Data**Placement** property, which contains the
Data**Base** (position) and Data**Rotation** (orientation) of the object. It
is easy to manipulate, for example to move our object:

    
    
    box.Placement
    box.Placement.Base
    box.Placement.Base = sumvec
     
    otherpla = FreeCAD.Placement()
    box.Placement = otherpla
    

Now you must understand a couple of important concepts before we get further.

Top

## App and Gui

FreeCAD has been designed so that it can also be used without its user
interface, as a command-line application. Almost every object in FreeCAD
therefore consists of two parts: an `Object`, its "geometry" component, and a
`ViewObject`, its "visual" component. When you work in command-line mode, the
geometry part is present, but the visual part is disabled.

To illustrate the concept let's look at our cube object. The geometric
properties of the cube, such as its dimensions, position, etc. are stored in
the `Object`. While its visual properties, such as its color, line thickness,
etc. are stored in the `ViewObject`. This corresponds to the **Data** and
**View** tabs in the [Property editor](/Property_editor "Property editor").
The view object of an object is accessed like this:

    
    
    vo = box.ViewObject
    

Now you can also change the properties on the **View** tab:

    
    
    vo.Transparency = 80
    vo.hide()
    vo.show()
    

When you start FreeCAD, the Python console already loads two base modules:
`FreeCAD` and `FreeCADGui` (which can also be accessed by their shortcuts
`App` and `Gui`). They contain all kinds of generic functionality to work with
documents and their objects. To illustrate our concept, see that both
`FreeCAD` and `FreeCADGui` contain an `ActiveDocument` attribute, which is the
currently opened document. `FreeCAD.ActiveDocument` and
`FreeCADGui.ActiveDocument` are not the same object however. They are the two
components of a FreeCAD document, and they contain different attributes and
methods. For example, `FreeCADGui.ActiveDocument` contains `ActiveView`, which
is the currently opened [3D view](/3D_view "3D view").

Top

## Modules

The true power of FreeCAD lies in its faithful modules, with their respective
workbenches. The FreeCAD base application is more or less an empty container.
Without its modules it can do little more than create new, empty documents.
Each module not only adds new workbenches to the interface, but also new
Python commands and new object types. As a result several different, and even
totally incompatible, object types can coexist in the same document. The most
important modules in FreeCAD that we'll look at in this tutorial are:
[Part](/Part_Workbench "Part Workbench"), [Mesh](/Mesh_Workbench "Mesh
Workbench"), [Sketcher](/Sketcher_Workbench "Sketcher Workbench") and
[Draft](/Draft_Workbench "Draft Workbench").

[Sketcher](/Sketcher_Workbench "Sketcher Workbench") and
[Draft](/Draft_Workbench "Draft Workbench") both use the
[Part](/Part_Workbench "Part Workbench") module to create and handle their
geometry. While [Mesh](/Mesh_Workbench "Mesh Workbench") is totally
independent, and handles its own objects. More about that below.

You can check all the available base object types for the current document
like this:

    
    
    doc.supportedTypes()
    

The different FreeCAD modules are not automatically loaded in the Python
console. This is to avoid having a very slow startup. Modules are loaded only
when you need them. So, for example, to explore what's inside the Part module:

    
    
    import Part
    Part.
    

But we'll talk more about the Part module below.

Top

## Mesh module

[Meshes](https://en.wikipedia.org/wiki/Polygon_mesh) are a very simple kind of
3D object, used for example by
[Sketchup](https://en.wikipedia.org/wiki/SketchUp),
[Blender](https://en.wikipedia.org/wiki/Blender_\(software\)) and [3D Studio
Max](https://en.wikipedia.org/wiki/Autodesk_3ds_Max). They are composed of 3
elements: points (also called vertices), lines (also called edges) and faces.
In many applications, FreeCAD included, faces can have only 3 vertices. Of
course, nothing prevents you from having a bigger face made up of several
coplanar triangles.

Meshes are simple, but because they are simple you can easily have millions of
them in a single document. However, in FreeCAD they have less use and are
mostly there so you can import objects in mesh formats (.stl, .obj) from other
applications. The Mesh module was also used extensively as the main test
module in the first month of FreeCAD's life.

Mesh objects and FreeCAD objects are different things. You can see the FreeCAD
object as a container for a Mesh object (and as we'll see below, for Part
objects also). So in order to add a mesh object to FreeCAD, we must first
create a FreeCAD object and a Mesh object, then add the Mesh object to the
FreeCAD object:

    
    
    import Mesh
    mymesh = Mesh.createSphere()
    mymesh.Facets
    mymesh.Points
     
    meshobj = doc.addObject("Mesh::Feature", "MyMesh")
    meshobj.Mesh = mymesh
    doc.recompute()
    

This is a standard example that uses the `createSphere()` method to create a
sphere, but you can also create custom meshes from scratch by defining their
vertices and faces.

[Read more about mesh scripting...](/Mesh_Scripting "Mesh Scripting")

Top

## Part module

The [Part](/Part_Workbench "Part Workbench") module is the most powerful
module in the whole of FreeCAD. It allows you to create and manipulate
[BRep](https://en.wikipedia.org/wiki/Boundary_representation) objects. BREP
stands for "Boundary Representation". A BREP object is defined by surfaces
that enclose and define an inner volume. Unlike meshes, BREP objects can have
a wide variety of components from planar faces to very complex NURBS surfaces.

The Part module is based on the powerful
[OpenCasCade](https://en.wikipedia.org/wiki/Open_CASCADE_Technology) library,
which allows a wide range of complex operations to be performed on those
objects, such as boolean operations, filleting, lofts, etc.

The Part module works the same way as the Mesh module: You create a FreeCAD
object, a Part object, then add the Part object to the FreeCAD object:

    
    
    import Part
    myshape = Part.makeSphere(10)
    myshape.Volume
    myshape.Area
    
    shapeobj = doc.addObject("Part::Feature", "MyShape")
    shapeobj.Shape = myshape
    doc.recompute()
    

The Part module (like the Mesh module) also has a shortcut that automatically
creates a FreeCAD object and adds a shape to it, so you can shorten the last
three lines to:

    
    
    Part.show(myshape)
    

By exploring the contents of myshape, you will notice many interesting
subcomponents such as `Faces`, `Edges`, `Vertexes`, `Solids` and `Shells`, and
a wide range of geometry operations such as `cut` (subtraction), `common`
(intersection) or `fuse` (union). The [Topological data
scripting](/Topological_data_scripting "Topological data scripting") page
explains all that in detail.

[Read more about part scripting...](/Topological_data_scripting "Topological
data scripting")

Top

## Draft module

FreeCAD features many more modules, such as [Sketcher](/Sketcher_Workbench
"Sketcher Workbench") and [Draft](/Draft_Workbench "Draft Workbench"), that
also create Part objects. These modules add additional parameters to the
objects created, or even implement a whole new way to handle the Part geometry
in them. Our box example above is a perfect example of a parametric object.
All you need to define the box is to specify the parameters height, width and
length. Based on those, the object will automatically calculate its Part
shape. FreeCAD allows you to [create such objects in Python](/Scripted_objects
"Scripted objects").

The [Draft](/Draft_Workbench "Draft Workbench") module adds 2D parametric
object types (which are all Part objects) such as lines and circles, and also
provides some generic functions that not only work on Draft objects, but on
any Part object. To explore what is available, simply do:

    
    
    import Draft
    rec = Draft.makeRectangle(5, 2)
    mvec = FreeCAD.Vector(4, 4, 0)
    Draft.move(rec, mvec)
    Draft.move(box, mvec)
    

Top

## Interface

The FreeCAD user interface is made with
[Qt](https://en.wikipedia.org/wiki/Qt_\(software\)), a powerful graphical
interface system, responsible for drawing and handling all the controls,
menus, toolbars and buttons around the [3D view](/3D_view "3D view"). Qt
provides a module, [PySide](/PySide "PySide"), which allows Python to access
and modify Qt interfaces such as FreeCAD's. Let's try to fiddle with the Qt
interface and produce a simple dialog:

    
    
    from PySide import QtGui
    QtGui.QMessageBox.information(None, "Apollo program", "Houston, we have a problem")
    

Notice that the dialog that appears has the FreeCAD icon in its toolbar,
meaning that Qt knows that the order has been issued from inside the FreeCAD
application. It is possible to manipulate any part of the FreeCAD interface.

Qt is a very powerful interface system that allows you to do very complex
things. It also has some easy-to-use tools such as the Qt Designer with which
you can design dialogs graphically and then add them to the FreeCAD interface
with a few lines of Python code.

[Read more about PySide here...](/PySide "PySide")

Top

## Macros

Now that you have a good understanding of the basics, where are we going to
keep our Python scripts, and how are we going to launch them inside FreeCAD?
There is an easy mechanism for that, called [Macros](/Macros "Macros"). A
macro is a Python script that can be added to a toolbar and launched via a
mouse click. FreeCAD provides you with a simple text editor (**Macro →
Macros... → Create**) where you can write or paste scripts. Once the script is
done, use **Tools → Customize... → Macros** to define a button for it that can
be added to toolbars.

## External scripts

An alternative method for creating, saving, and running your own Python
scripts is to create them outside FreeCAD, using an editor of your choice (for
example, Vim). To run your Python script inside FreeCAD, be sure to save it
with the .py extension.

Then use **File → Open** to open your script. It will load into a new tab in
the [Main view area](/Main_view_area "Main view area"). You can run your
script by clicking the
[![](/images/f/f7/Std_DlgMacroExecuteDirect.svg)](/index.php?title=File:Std_DlgMacroExecuteDirect.svg&filetimestamp=20240704212444&)
[Execute macro](/Std_DlgMacroExecuteDirect "Std DlgMacroExecuteDirect")
button. Any errors or script output will be shown in the [Report
view](/Report_view "Report view").

When you make and save any modifications to your already-loaded script, a
dialog box will appear asking whether you want to reload the modified script
into FreeCAD.

You can continue to the [FreeCAD Scripting Basics](/FreeCAD_Scripting_Basics
"FreeCAD Scripting Basics") page, or you can access that page and other
relevant pages at the [Power users hub](/Power_users_hub "Power users hub").

Top

![](/images/6/6f/Arrow-left.svg) [Introduction to
Python](/Introduction_to_Python "Introduction to Python")

[FreeCAD Scripting Basics](/FreeCAD_Scripting_Basics "FreeCAD Scripting
Basics") ![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

Expand[![](/images/thumb/8/8f/Power_user_hub.png/24px-
Power_user_hub.png)](/index.php?title=File:Power_user_hub.png&filetimestamp=20200511213015&)
[Power user documentation](/Power_users_hub "Power users hub")

  * **FreeCAD scripting:** [Python](/Python "Python"), [Introduction to Python](/Introduction_to_Python "Introduction to Python"), Python scripting tutorial, [FreeCAD Scripting Basics](/FreeCAD_Scripting_Basics "FreeCAD Scripting Basics")

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

