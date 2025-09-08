---
url: https://wiki.freecad.org/Scripts
title: Scripts
scraped_at: 2025-09-08 16:43:15
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction
  * 2 Getting started
  * 3 Something more
  * 4 Placement

# Scripts

  * [Page](/Scripts "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Scripts&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Scripts)
  * [Edit](/index.php?title=Scripts&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Scripts&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Scripts.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Scripts&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Scripts)
  * [Edit](/index.php?title=Scripts&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Scripts&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Scripts&action=history)

General

  * [What links here](/Special:WhatLinksHere/Scripts "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Scripts "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Scripts&oldid=1461200 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Scripts&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Scripts&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Scripts&action=page&filter=&language=en)This is the approved revision of this
page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Scripts&language=&task=view "Start translation for this language")
  * [Deutsch](/Scripts/de "Skripte \(100% translated\)")
  * English
  * [français](/Scripts/fr "Scripts \(100% translated\)")
  * [italiano](/Scripts/it "Script \(100% translated\)")
  * [polski](/Scripts/pl "Tworzenie skryptów \(100% translated\)")
  * [português do Brasil](/Scripts/pt-br "Scripts \(6% translated\)")
  * [русский](/Scripts/ru "Скрипты \(4% translated\)")
  * [한국어](/Scripts/ko "스크립트 \(17% translated\)")

![](/images/6/6f/Arrow-left.svg) [Macros](/Macros "Macros")

[Introduction to Python](/Introduction_to_Python "Introduction to Python")
![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

![](/images/0/06/Freecad.svg) Tutorial  
---  
Topic  
Scripting  
Level  
Base  
Time to complete  
Authors  
onekk Carlo  
FreeCAD version  
0.19  
Example files  
See also  
_None_  
  
  
  
## Introduction

With Scripting we mean create topological objects using FreeCAD's Python
interpreter. FreeCAD could be used as a "very good" replacement of OpenSCAD,
mainly because it has a real Python interpreter, that means that it has a real
programming language on board, almost everything you could do with the GUI, is
doable with a Python Script.

Sadly information about scripting in the documentation, and even in this wiki
are scattered around and lacks of "writing" uniformity and most of them are
explained in a too technical manner.

## Getting started

The first obstacle in an easy way to scripting is that there is no direct way
to access the FreeCAD internal Python editor through a menu item or a icon on
the toolbar area, but knowing that FreeCAD opens a file with a `.py` extension
in the internal Python editor, the most simple trick is create in your
favorite text editor and then open it with the usual command **File → Open**.

To make the things in a polite way, the file has to be written with some
order, FreeCAD Python editor have a good "Syntax Highlighting" that lacks in
many simple editors like Windows Notepad or some basic Linux editors, so it is
sufficient to write these few lines:

    
    
    """filename.py
    
       A short description of what the script does
    
    """
    

Save them with a meaningfull name with `.py` extension and load the resulting
file in FreeCAD, with the said **File → Open** command.

A minimal example of what is necessary to have in a script is shown in this
portion of code that you could be use as a template for almost any future
script:

    
    
    """filename.py
    
       First FreeCAD Script
    
    """
    
    import FreeCAD
    from FreeCAD import Placement, Rotation, Vector
    import FreeCADGui
    
    DOC_NAME = "Wiki_Example"
    DOC = FreeCAD.newDocument(DOC_NAME)
    FreeCAD.setActiveDocument(DOC.Name)
    
    ROT0 = Rotation(0, 0, 0)
    VEC0 = Vector(0, 0, 0)
    
    # Helper function
    
    def set_view():
        """Rearrange View."""
        if not FreeCAD.GuiUp:
            return
        doc = FreeCADGui.ActiveDocument
        if doc is None:
            return
        view = doc.ActiveView
        if view is None:
            return
        # Check if the view is a 3D view:
        if not hasattr(view, "getSceneGraph"):
            return
        view.viewAxometric()
        view.fitAll()
    

Some tricks are incorporated in the above code:

  * `import FreeCAD` This line import FreeCAD in the FreeCAD Python interpreter, it may seem a redundant thing, but it isn't.
  * `from FreeCAD import Placement, Rotation, Vector` **Placement** **Rotation** and **Vector** are widely used in FreeCAD scripting, import them in this manner will save you to invoke them with `FreeCAD.Vector` or `FreeCAD.Placement` instead of `Vector` or `Placement`, this will save many keystrokes and make codelines much smaller.

Let's start with a small script that does a very small job, but display the
power of this approach.

    
    
    # Script functions
    
    def my_box(name, len, wid, hei):
        """Create a box."""
        obj_b = DOC.addObject("Part::Box", name)
        obj_b.Length = len
        obj_b.Width = wid
        obj_b.Height = hei
    
        DOC.recompute()
    
        return obj_b
    
    # objects definition
    
    obj = my_box("test_cube", 5, 5, 5)
    
    set_view()
    

Write above lines of code after `# Script functions` and press the green arrow
in the **Macro toolbar**.

You will see some magic things, a new document is open named "Wiki_example"
and you will see in the 3d view a [Cube](/Part_Box "Part Box"), like the one
in the image below.

[![](/images/thumb/0/0d/Cubo.png/300px-
Cubo.png)](/index.php?title=File:Cubo.png&filetimestamp=20200302133620&)Test
cube

## Something more

Not that amazing? Yes, but we have to start somewhere, we can do the same
thing with a [Cylinder](/Part_Cylinder "Part Cylinder"), add these lines of
code after the `my_box()` function and before the line: `# objects
definition`.

    
    
    def my_cyl(name, ang, rad, hei):
        """Create a Cylinder."""
        obj = DOC.addObject("Part::Cylinder", name)
        obj.Angle = ang
        obj.Radius = rad
        obj.Height = hei
    
        DOC.recompute()
    
        return obj
    

Even here nothing too exciting. But please note some peculiarities:

  * The absence of the usual reference to the `App.`, present in many Documentation code snippets, is deliberate, this code could be used even invoking FreeCAD as a module in an external Python interpreter, the thing is not easily doable with an AppImage, but with some care it could be done. Plus in the standard Python motto that "better explicit than implicit" `App.` is explaining in a very "poor" way where the things are from.
  * Note the use of the "constant" name assigned to the active Document in `DOC = FreeCAD.activeDocument()`; activeDocument is not a "constant" in a strict sense, but in a "semantical" way is our "active Document", that for our use is a proper "constant" so the Python convention to use the "ALL CAPS" name for "constants", not to mention that `DOC` is much shorten than `FreeCAD.activeDocument()`.
  * Every function returns a geometry, this will be clear in the continuation of the page.
  * Geometry didn't have the `Placement` property, when using the simple geometries to make more complex geometry, managing `Placement` is a awkward thing.

Now what to do with this geometries?

Let's introduce boolean operations. As a starter example put these lines after
`my_cyl`, this create a function for a **Fusion** also know as **Union**
operation:

    
    
    def fuse_obj(name, obj_0, obj_1):
        """Fuse two objects."""
        obj = DOC.addObject("Part::Fuse", name)
        obj.Base = obj_0
        obj.Tool = obj_1
        obj.Refine = True
        DOC.recompute()
    
        return obj
    

Nothing exceptional also here, note however the uniformity in function coding;
This approach is more linear than those seen around other tutorial on
scripting, this "linearity" help greatly in readability and also with cut-
copy-paste operations.

Let's use the geometries, delete lines below the code section starting with `#
objects definition`, and insert the following lines:

    
    
    # objects definition
    
    obj = my_box("test_cube", 5, 5, 5)
    
    obj1 = my_cyl("test_cyl", 360, 2, 10)
    
    fuse_obj("Fusion", obj, obj1)
    
    set_view()
    

Launch the script with the green arrow and we will see in the 3D view
something like:

[![](/images/thumb/c/c7/Cucil.png/300px-
Cucil.png)](/index.php?title=File:Cucil.png&filetimestamp=20200302140515&)Cube
and cylinder

## Placement

Placement Concept is relatively complex, see [Aeroplane Tutorial](/Aeroplane
"Aeroplane") for a more deep explanation.

We usually are in need of placing geometries respect each other, when building
complex object this is a recurring task, the most common way is to use the
geometry `Placement` property.

FreeCAD offer a wide choice of ways to set this property, one is more tailored
to another depending the knowledge and the background of the user, but the
more plain writing is explained in the cited Tutorial, it use a peculiar
definition of the `Rotation` portion of `Placement`, quite easy to learn.

    
    
    FreeCAD.Placement(Vector(0, 0, 0), FreeCAD.Rotation(10, 20, 30), Vector(0, 0, 0))
    

But over other consideration, one thing is crucial, geometry **reference
point** , in other words the point from which the object is modeled by
FreeCAD, as described in this table, copied from [Placement](/Placement
"Placement"):

Object | Reference Point   
---|---  
Part.Box | left (minx), front (miny), bottom (minz) vertex   
Part.Sphere | center of the sphere   
Part.Cylinder | center of the bottom face   
Part.Cone | center of bottom face (or apex if bottom radius is 0)   
Part.Torus | center of the torus   
Features derived from Sketches | the Feature inherits the Position of the underlying Sketch. Sketches always start with Position = (0, 0, 0). This position corresponds to the origin in the sketch.   
  
This information has to be kept in mind especially when we have to apply a
rotation.

Some examples may help, delete the `my_box` function and all lines after the
`my_cyl` function, and add the code below after the `my_cyl` function:

    
    
    def my_sphere(name, rad):
        """Create a Sphere."""
        obj = DOC.addObject("Part::Sphere", name)
        obj.Radius = rad
    
        DOC.recompute()
    
        return obj
    
    def my_box2(name, len, wid, hei, cent=False, off_z=0):
        """Create a box with an optional z offset."""
        obj_b = DOC.addObject("Part::Box", name)
        obj_b.Length = len
        obj_b.Width = wid
        obj_b.Height = hei
    
        if cent is True:
            pos = Vector(len * -0.5, wid * -0.5, off_z)
        else:
            pos = Vector(0, 0, off_z)
    
        obj_b.Placement = Placement(pos, ROT0, VEC0)
    
        DOC.recompute()
    
        return obj_b
    
    def mfuse_obj(name, objs):
        """Fuse multiple objects."""
        obj = DOC.addObject("Part::MultiFuse", name)
        obj.Shapes = objs
        obj.Refine = True
        DOC.recompute()
    
        return obj
    
    def airplane():
        """Create an airplane shaped solid."""
        fuselage_length = 30
        fuselage_diameter = 5
        wing_span = fuselage_length * 1.75
        wing_width = 7.5
        wing_thickness = 1.5
        tail_height = fuselage_diameter * 3.0
        tail_position = fuselage_length * 0.70
        tail_offset = tail_position - (wing_width * 0.5)
    
        obj1 = my_cyl("main_body", 360, fuselage_diameter, fuselage_length)
    
        obj2 = my_box2("wings", wing_span, wing_thickness, wing_width, True, tail_offset)
    
        obj3 = my_sphere("nose", fuselage_diameter)
        obj3.Placement = Placement(Vector(0, 0, fuselage_length), ROT0, VEC0)
    
        obj4 = my_box2("tail", wing_thickness, tail_height, wing_width, False, 0)
        obj4.Placement = Placement(Vector(0, tail_height * -1, 0), ROT0, VEC0)
    
        objs = (obj1, obj2, obj3, obj4)
    
        obj = mfuse_obj("airplane", objs)
        obj.Placement = Placement(VEC0, Rotation(0, 0, -90), Vector(0, 0, tail_position))
    
        DOC.recompute()
    
        return obj
    
    # objects definition
    
    airplane()
    
    set_view()
    

Let's explain something in the code:

  * We have used a function to define a sphere, using the most easy definition, using only the radius.
  * We have introduced a second writing for the **Union** or **Fusion** , using multiple objects, not more distant from the usual **Part::Fuse** it uses **Part:Multifuse**. We only use one property `Shapes`. We have passed a **tuple** as arguments, but it accepts also a **list**.
  * We have defined a complex object **airplane** , but we have done it in a **"parametric"** way, defining some parameters and deriving other parameters, through some calculation, based on the main parameters.
  * We have used some Placement `Placement` poperties around in the function and before returning the final geometries we have used a `Rotation` property with the _Yaw-Pitch-Roll_ writing. Note the last `Vector(0, 0, tail_position)`, that define a **center of rotation** of the whole geometry.

[![](/images/thumb/a/af/Aereo.png/300px-Aereo.png)](/index.php?title=File:Aereo.png&filetimestamp=20200302152032&)Airplane example | [![](/images/thumb/c/cb/Aereo2.png/300px-Aereo2.png)](/index.php?title=File:Aereo2.png&filetimestamp=20200302155137&)Airplane rotated |  [![](/images/4/4a/Aereo-prop.png)](/index.php?title=File:Aereo-prop.png&filetimestamp=20200302161352&)Placement property  
---|---|---  
  
It can be easily noted that **airplane** geometry rotate around his
"barycenter" or "center of gravity", that I've fixed at wing center, a place
that is relatively "natural", but could be placed wherever you want.

The first `Vector(0, 0, 0)` is the Translation vector, not used here, but if
you substitute `airplane()` with these lines:

    
    
    obj_f = airplane()
    
    print(obj_F.Placement)
    

You will see in the Report window this text:

    
    
    Placement [Pos=(0, -21, 21), Yaw-Pitch-Roll=(0, 0, -90)]
    

What has happened?

FreeCAD has translated the `Vector(0, 0, 0), FreeCAD.Rotation(0, 0, -90),
Vector(0, 0, tail_position)` in other words our `Placement` definition that
specifies three components, **Translation** , **Rotation** and **center of
rotation** in the "internal" values of only two components, **Translation**
and **Rotation**.

you can easily visualize the value of `tail_position` using a print statement
in the `airplane()` function and see that it is:

    
    
    tail_position = 21.0
    

in other words the **rotation center** of the geometry is at `Vector(0, 0,
21)`, but this rotation center is not shown in the GUI, it could be entered as
a `Placement` value, it could not be easily retrieved.

This is the meaning of the word "awkward" that I've used to define `Placement`
property.

  
This is the complete code example with a decent script docstring following
[Google docstrings convention](https://www.sphinx-
doc.org/en/master/usage/extensions/example_google.html#example-google):

    
    
    """Sample code.
    
    Filename:
       airplane.py
    
    Author:
        Dormeletti Carlo (onekk)
    
    Version:
        1.0
    
    License:
        Creative Commons Attribution 3.0
    
    Summary:
        This is sample code written for a FreeCAD Wiki page.
        It creates an airplane shaped solid using standard "Part WB" shapes.
    
    """
    
    import FreeCAD
    from FreeCAD import Placement, Rotation, Vector
    import FreeCADGui
    
    DOC_NAME = "Wiki_Example"
    DOC = FreeCAD.newDocument(DOC_NAME)
    FreeCAD.setActiveDocument(DOC.Name)
    
    ROT0 = Rotation(0, 0, 0)
    VEC0 = Vector(0, 0, 0)
    
    # Helper function
    
    def set_view():
        """Rearrange View."""
        if not FreeCAD.GuiUp:
            return
        doc = FreeCADGui.ActiveDocument
        if doc is None:
            return
        view = doc.ActiveView
        if view is None:
            return
        # Check if the view is a 3D view:
        if not hasattr(view, "getSceneGraph"):
            return
        view.viewAxometric()
        view.fitAll()
    
    # Script functions
    
    def my_cyl(name, ang, rad, hei):
        """Create a Cylinder."""
        obj = DOC.addObject("Part::Cylinder", name)
        obj.Angle = ang
        obj.Radius = rad
        obj.Height = hei
    
        DOC.recompute()
    
        return obj
    
    def my_sphere(name, rad):
        """Create a Sphere."""
        obj = DOC.addObject("Part::Sphere", name)
        obj.Radius = rad
    
        DOC.recompute()
    
        return obj
    
    def my_box2(name, len, wid, hei, cent=False, off_z=0):
        """Create a box with an optional z offset."""
        obj_b = DOC.addObject("Part::Box", name)
        obj_b.Length = len
        obj_b.Width = wid
        obj_b.Height = hei
    
        if cent is True:
            pos = Vector(len * -0.5, wid * -0.5, off_z)
        else:
            pos = Vector(0, 0, off_z)
    
        obj_b.Placement = Placement(pos, ROT0, VEC0)
    
        DOC.recompute()
    
        return obj_b
    
    def mfuse_obj(name, objs):
        """Fuse multiple objects."""
        obj = DOC.addObject("Part::MultiFuse", name)
        obj.Shapes = objs
        obj.Refine = True
        DOC.recompute()
    
        return obj
    
    def airplane():
        """Create an airplane shaped solid."""
        fuselage_length = 30
        fuselage_diameter = 5
        wing_span = fuselage_length * 1.75
        wing_width = 7.5
        wing_thickness = 1.5
        tail_height = fuselage_diameter * 3.0
        tail_position = fuselage_length * 0.70
        tail_offset = tail_position - (wing_width * 0.5)
    
        obj1 = my_cyl("main_body", 360, fuselage_diameter, fuselage_length)
    
        obj2 = my_box2("wings", wing_span, wing_thickness, wing_width, True, tail_offset)
    
        obj3 = my_sphere("nose", fuselage_diameter)
        obj3.Placement = Placement(Vector(0, 0, fuselage_length), ROT0, VEC0)
    
        obj4 = my_box2("tail", wing_thickness, tail_height, wing_width, False, 0)
        obj4.Placement = Placement(Vector(0, tail_height * -1, 0), ROT0, VEC0)
    
        objs = (obj1, obj2, obj3, obj4)
    
        obj = mfuse_obj("airplane", objs)
        obj.Placement = Placement(VEC0, Rotation(0, 0, -90), Vector(0, 0, tail_position))
    
        DOC.recompute()
    
        return obj
    
    # objects definition
    
    airplane()
    
    set_view()
    

  

![](/images/6/6f/Arrow-left.svg) [Macros](/Macros "Macros")

[Introduction to Python](/Introduction_to_Python "Introduction to Python")
![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

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

