---
url: https://wiki.freecad.org/Python
title: Python
scraped_at: 2025-09-08 16:41:15
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Description
  * 2 Readability
  * 3 Conventions
  * 4 Imports

# Python

  * [Page](/Python "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Python&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Python)
  * [Edit](/index.php?title=Python&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Python&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Python.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Python&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Python)
  * [Edit](/index.php?title=Python&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Python&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Python&action=history)

General

  * [What links here](/Special:WhatLinksHere/Python "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Python "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Python&oldid=1597856 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Python&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Python&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Python&action=page&filter=&language=en)This is the approved revision of this
page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Python&language=&task=view "Start translation for this language")
  * [Deutsch](/Python/de "Python \(100% translated\)")
  * English
  * [Türkçe](/Python/tr "Python \(80% translated\)")
  * [español](/Python/es "Python \(100% translated\)")
  * [français](/Python/fr "Python \(100% translated\)")
  * [italiano](/Python/it "Python \(100% translated\)")
  * [polski](/Python/pl "Środowisko Python \(5% translated\)")
  * [português do Brasil](/Python/pt-br "Python \(10% translated\)")
  * [română](/Python/ro "Python \(80% translated\)")
  * [русский](/Python/ru "Python \(100% translated\)")
  * [日本語](/Python/ja "Python \(55% translated\)")
  * [한국어](/Python/ko "파이썬 \(100% translated\)")

## Description

[Python](https://www.python.org) is a general purpose, high level programming
language that is very commonly used in large applications to automate some
tasks by creating scripts or [macros](/Macros "Macros").

In FreeCAD, Python code can be used to create various elements
programmatically, without needing to click on the graphical user interface.
Additionally, many tools and workbenches of FreeCAD are programmed in Python.

See [Introduction to Python](/Introduction_to_Python "Introduction to Python")
to learn about the Python programming language, and then [Python scripting
tutorial](/Python_scripting_tutorial "Python scripting tutorial") and [FreeCAD
Scripting Basics](/FreeCAD_Scripting_Basics "FreeCAD Scripting Basics") to
start scripting in FreeCAD.

## Readability

Readability of Python code is one of the most important aspects of this
language. Using a clear and consistent style within the Python community
facilitates contributions by different developers, as most experienced Python
programmers expect the code to be formatted in a certain way and to follow
certain rules. When writing Python code, it is advisable to follow [PEP8:
Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/) and
[PEP257: Docstring Conventions](https://www.python.org/dev/peps/pep-0257/).

These documents present explanations in a more user-friendly way:

  * [How to Write Beautiful Python Code With PEP 8](https://realpython.com/python-pep8/)
  * [Documenting Python Code: A Complete Guide](https://realpython.com/documenting-python-code/).

## Conventions

In this documentation, some conventions for Python examples should be
followed.

This is a typical function signature

    
    
    Wire = make_wire(pointslist, closed=False, placement=None, face=None, support=None)
    

  * Arguments with key-value pairs are optional, with the default value indicated in the signature. This means that the following calls are equivalent:

    
    
    Wire = make_wire(pointslist, False, None, None, None)
    Wire = make_wire(pointslist, False, None, None)
    Wire = make_wire(pointslist, False, None)
    Wire = make_wire(pointslist, False)
    Wire = make_wire(pointslist)
    

    In this example the first argument doesn't have a default value so it should always be included.

  * When the arguments are given with the explicit key, the optional arguments can be given in any order. This means that the following calls are equivalent:

    
    
    Wire = make_wire(pointslist, closed=False, placement=None, face=None)
    Wire = make_wire(pointslist, closed=False, face=None, placement=None)
    Wire = make_wire(pointslist, placement=None, closed=False, face=None)
    Wire = make_wire(pointslist, support=None, closed=False, placement=None, face=None)
    

  * Python's guidelines stress readability of code; in particular, parentheses should immediately follow the function name, and a space should follow a comma.

    
    
    p1 = Vector(0, 0, 0)
    p2 = Vector(1, 1, 0)
    p3 = Vector(2, 0, 0)
    Wire = make_wire([p1, p2, p3], closed=True)
    

  * If code needs to be broken over several lines, this should be done at a comma inside brackets or parentheses; the second line should be aligned with the previous one.

    
    
    a_list = [1, 2, 3,
              2, 4, 5]
    
    Wire = make_wire(pointslist,
                    False, None,
                    None, None)
    

  * Functions may return an object that can be used as the base of another drawing function.

    
    
    Wire = make_wire(pointslist, closed=True, face=True)
    Window = make_window(Wire, name="Big window")
    

## Imports

Python functions are stored in files called modules. Before using any function
in that module, the module must be included in the document with the `import`
instruction.

This creates prefixed functions, that is, `module.function()`. This system
prevents name clashes with functions that are named the same but that come
from different modules. For example, the two functions `Arch.make_window()`
and `myModule.make_window()` may coexist without problem.

Full examples should include the necessary imports and the prefixed functions.

    
    
    import FreeCAD as App
    import Draft
    
    p1 = App.Vector(0, 0, 0)
    p2 = App.Vector(1, 1, 0)
    p3 = App.Vector(2, 0, 0)
    Wire = Draft.make_wire([p1, p2, p3], closed=True)
    
    
    
    import FreeCAD as App
    import Draft
    import Arch
    
    p1 = App.Vector(0, 0, 0)
    p2 = App.Vector(1, 0, 0)
    p3 = App.Vector(1, 1, 0)
    p4 = App.Vector(0, 2, 0)
    pointslist = [p1, p2, p3, p4]
    
    Wire = Draft.make_wire(pointslist, closed=True, face=True)
    Structure = Arch.make_structure(Wire, name="Big pillar")
    

Expand[![](/images/thumb/8/8f/Power_user_hub.png/24px-
Power_user_hub.png)](/index.php?title=File:Power_user_hub.png&filetimestamp=20200511213015&)
[Power user documentation](/Power_users_hub "Power users hub")

  * **FreeCAD scripting:** Python, [Introduction to Python](/Introduction_to_Python "Introduction to Python"), [Python scripting tutorial](/Python_scripting_tutorial "Python scripting tutorial"), [FreeCAD Scripting Basics](/FreeCAD_Scripting_Basics "FreeCAD Scripting Basics")

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

