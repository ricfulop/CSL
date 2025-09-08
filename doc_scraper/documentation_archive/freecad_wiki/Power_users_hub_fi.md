---
url: https://wiki.freecad.org/Power_users_hub/fi
title: Power users hub/fi
scraped_at: 2025-09-08 16:46:05
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Customizing FreeCAD
  * 2 Scripting in FreeCAD Toggle Scripting in FreeCAD subsection
    * 2.1 General
    * 2.2 Modules
      * 2.2.1 Working with Meshes
      * 2.2.2 Working with Parts
      * 2.2.3 Accessing the Coin scenegraph
    * 2.3 Controlling the Qt interface
    * 2.4 Working with parametric objects
    * 2.5 Examples
  * 3 API Functions
  * 4 Advanced modification
  * 5 Python tutorials
  * 6 Community projects

# Power users hub

  * [Page](/Power_users_hub/fi "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Power_users_hub/fi&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

suomi

  * [Read](/Power_users_hub/fi)
  * [Translate](/index.php?title=Special:Translate&group=page-Power+users+hub&action=page&filter=&language=fi "Edit this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Power_users_hub/fi&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Power_users_hub/fi)
  * [Translate](/index.php?title=Special:Translate&group=page-Power+users+hub&action=page&filter=&language=fi "Edit this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Power_users_hub/fi&action=history)

General

  * [What links here](/Special:WhatLinksHere/Power_users_hub/fi "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Power_users_hub/fi "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Power_users_hub/fi&oldid=1605655 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Power_users_hub/fi&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Power_users_hub%2Ffi&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Power+users+hub&action=page&filter=&language=en)This is the approved revision
of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Power+users+hub&language=&task=view "Start translation for this language")
  * [Bahasa Indonesia](/Power_users_hub/id "Power users hub \(3% translated\)")
  * [Deutsch](/Power_users_hub/de "Hauptanwenderzentrum \(100% translated\)")
  * [English](/Power_users_hub "Power users hub \(100% translated\)")
  * [Türkçe](/Power_users_hub/tr "Uzman kullanıcı merkezi \(8% translated\)")
  * [español](/Power_users_hub/es "Centro usuarios avanzados \(86% translated\)")
  * [français](/Power_users_hub/fr "Documentation pour utilisateurs expérimentés \(100% translated\)")
  * [hrvatski](/Power_users_hub/hr "Napredno korisničko okruženje \(3% translated\)")
  * [italiano](/Power_users_hub/it "Hub degli utenti esperti \(100% translated\)")
  * [polski](/Power_users_hub/pl "Centrum Power użytkowników \(100% translated\)")
  * [português](/Power_users_hub/pt "Power users hub \(65% translated\)")
  * [português do Brasil](/Power_users_hub/pt-br "Documentação para usuários avançados \(24% translated\)")
  * [română](/Power_users_hub/ro "=Hub ul pentru utilizatorii avansați= \(27% translated\)")
  * suomi
  * [svenska](/Power_users_hub/sv "Power users hub \(22% translated\)")
  * [čeština](/Power_users_hub/cs "Centrum pokročilého uživatele \(22% translated\)")
  * [русский](/Power_users_hub/ru "Центр опытных пользователей \(84% translated\)")
  * [中文（中国大陆）](/Power_users_hub/zh-cn "发烧友中心 \(27% translated\)")
  * [中文（臺灣）](/Power_users_hub/zh-tw "進階用戶區 \(11% translated\)")
  * [日本語](/Power_users_hub/ja "パワーユーザー向けハブ \(3% translated\)")
  * [한국어](/Power_users_hub/ko "Power users hub/ko \(19% translated\)")

[![](/images/thumb/8/8f/Power_user_hub.png/64px-
Power_user_hub.png)](/index.php?title=File:Power_user_hub.png&filetimestamp=20200511213015&)

* * *

This is the place to come if you are an experienced user and want to learn
more about customizing and extending FreeCAD.

FreeCAD is extensible by [Python](/Python "Python") code that is run directly
in the [Python console](/Python_console "Python console"), or that is loaded
from modules at startup. This means that you can modify FreeCAD without
needing to recompile the program. For example, you can:

  * **Create and modify geometry** : you can create a new object type, either from scratch or by adapting an existing type.
  * **Create custom tools and commands** : add your own set of tools that run your code.
  * **Modify the interface** : create toolbars to put your tools, create special windows, panels, or interfaces for interacting with your tools.
  * **Modify the scenegraph representation** : FreeCAD has separate processes for building up the geometry and displaying that geometry on screen. You have full access to the way the scene contents are displayed on screen, therefore you can modify that representation, interact with it, or add custom behaviour to it. You can also add custom screen widgets, like information, draggers, anchors or temporary entities.

If you'd like to contribute content to these pages, request a wiki account
with editor permissions [in the
forum](https://forum.freecad.org/viewtopic.php?f=21&t=6830), and read the
[WikiPages](/WikiPages "WikiPages") for the general guidelines that you should
follow. For other ways to contribute with the project, see the [Help
FreeCAD](/Help_FreeCAD "Help FreeCAD") page.

## Customizing FreeCAD

  * [Interface Customization](/Interface_Customization "Interface Customization"): Starting with the beginning: Toolbars and shortcuts
  * [Working with Macros](/Macros "Macros"): Easily record often repeated tasks or Python code
  * [Macros recipes](/Macros_recipes "Macros recipes")
  * [Customize Toolbars](/Customize_Toolbars "Customize Toolbars")
  * [Installing more workbenches](/Installing_more_workbenches "Installing more workbenches")

## Scripting in FreeCAD

### General

  * [Scripting and Macros](/Scripting_and_macros "Scripting and macros") \- A list of relevant wiki pages
  * [Introduction to Python](/Introduction_to_Python "Introduction to Python") \- See also other Python tutorials at the bottom of this page
  * [FreeCAD scripting tutorial](/Python_scripting_tutorial "Python scripting tutorial") \- A general look at Python scripting in FreeCAD
  * [FreeCAD Scripting Basics](/FreeCAD_Scripting_Basics "FreeCAD Scripting Basics"): Well, the basics
  * [FreeCAD Manual - Section Python Scripting](/Manual:A_gentle_introduction "Manual:A gentle introduction"): Multi-chapter introduction to Python Scripting in FreeCAD
  * [Gui Command](/Gui_Command "Gui Command"): Adding custom commands to the GUI
  * Using mixed [Units](/Units "Units") in FreeCAD
  * [Profiling](/Profiling "Profiling") the Python code
  * [Debugging](/Debugging#Python_Debugging "Debugging") the Python code
  * [Python Development Environment](/Python_Development_Environment "Python Development Environment") \- A simplistic development environment for Python within FreeCAD

### Modules

The functionality of FreeCAD is separated in Modules which deal with special
data types and applications. FreeCAD has built-in modules and Extension
Modules (plug-ins). Once plugin modules are installed, they become availible
to you as easily as the built-in modules. The modules described below are the
default modules, includeed in every FreeCAD installation.

  * The [Builtin modules](/Builtin_modules "Builtin modules") are the principal FreeCAD modules. They contain tools for manipulating general FreeCAD configurations, documents and their contents.
  * [Workbench creation](/Workbench_creation "Workbench creation") shows you how to create your own workbench

#### Working with Meshes

  * [Mesh Scripting](/Mesh_Scripting "Mesh Scripting"): How to interact with the [Mesh Workbench](/Mesh_Workbench "Mesh Workbench")

#### Working with Parts

  * [The Part Workbench](/Part_Workbench "Part Workbench"): How [Open CASCADE Technology](https://en.wikipedia.org/wiki/Open_CASCADE) tools and structure is used in FreeCAD
  * [Topological data scripting](/Topological_data_scripting "Topological data scripting"): How to interact with the Part Module
  * [PythonOCC](/PythonOCC "PythonOCC"): How to unleash the whole Open CASCADE power
  * [Mesh to Part](/Mesh_to_Part "Mesh to Part"): Converting between object types

#### Accessing the Coin scenegraph

  * [The Coin/Inventor scenegraph](/Scenegraph "Scenegraph"): How the FreeCAD scene representation works
  * [Pivy](/Pivy "Pivy"): How to access and modify the scenegraph

### Controlling the Qt interface

  * [PySide](/PySide "PySide"): How to access the interface, and modify its contents
  * [Using the FreeCAD GUI](/Embedding_FreeCADGui "Embedding FreeCADGui") in another Qt application with PyQt

### Working with parametric objects

  * [Scripted objects](/Scripted_objects "Scripted objects"): how to make 100% Python-scripted objects. 
    * [Scripted objects with attachment](/Scripted_objects_with_attachment "Scripted objects with attachment"): how to make scripted objects attachable to other objects.
    * [Scripted objects saving attributes](/Scripted_objects_saving_attributes "Scripted objects saving attributes"): how to save and restore attributes of the proxy class with `dumps` and `loads`.
    * [Scripted objects migration](/Scripted_objects_migration "Scripted objects migration"): how to migrate old scripted objects to a new class.

### Examples

  * [Code snippets](/Code_snippets "Code snippets") : A collection of pieces of FreeCAD Python code, to serve as ingredients in your scripts...
  * [Line drawing function](/Line_drawing_function "Line drawing function"): How to build a simple tool to draw lines
  * [Dialog creation](/Dialog_creation "Dialog creation"): How to construct dialogs with Qt designer, and use them in FreeCAD
  * [Embedding FreeCAD](/Embedding_FreeCAD "Embedding FreeCAD"): How to import FreeCAD as a Python module in other applications
  * The [Draft Workbench](/Draft_Workbench "Draft Workbench") adds basic 2d drawing functions to freecad. It is written entirely in Python, so it can be a good example if you want to write your own modules.
  * [FreeCAD vector math library](/FreeCAD_vector_math_library "FreeCAD vector math library") : A couple of handy functions to manipulate FreeCAD vectors. This library is also included in the Draft module.

## API Functions

The complete API documentation of FreeCAD is located at
<https://freecad.org/api/> . It contains both C++ and Python APIs, and is not
totally well formatted yet, which can be confusing when looking for python-
only code. An easier to browse version can be found [here](/Category:API
"Category:API"). Note that it can be incomplete, since it is updated manually.
For more accurate information, browse the modules directly from FreeCAD's
Python console.

Related: [Exposing C++ to Python](/Exposing_C%2B%2B_to_Python "Exposing C++ to
Python")

## Advanced modification

  * [Start up and Configuration](/Start_up_and_Configuration "Start up and Configuration"): Startup and command line options
  * [Installing on Windows](/Installing_on_Windows "Installing on Windows"): Using the windows installer
  * [Compiling FreeCAD on Windows](/Compile_on_Windows "Compile on Windows") and [Compiling FreeCAD on Linux](/Compile_on_Linux "Compile on Linux")
  * [Branding](/Branding "Branding"): Simple modifications you can do to the source code to change some aspects of FreeCAD
  * [Extra python modules](/Extra_python_modules "Extra python modules") : Extend the FreeCAD python interpreter with these powerful modules!

## Python tutorials

These are good generic tutorials, not specific to FreeCAD, that might interest
you if you are totally new to python.

**Python**

  * [Official python tutorial](https://docs.python.org/3/tutorial/index.html) \- A very complete tutorial for discovering python
  * [Non-programmer tutorial for python](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3) \- an excellent wikibook
  * [Python for newbies](http://npt.cc.rsu.ru/user/wanderer/ODP/Python_for_Newbies.htm) \- one big tutorial covering all the basics

**PySide** \- How to create and manage FreeCAD's Qt UI interface from python

  * [PySide tutorial](http://zetcode.com/gui/pysidetutorial/) : A platform-agnostic tutorial showing the usage of PySide with examples
  * [PySide/PyQt tutorial](http://www.pythoncentral.io/series/python-pyside-pyqt-tutorial/) : A easy to read tutorial that covers PySide and PyQt with examples
  * [PySide documentation](http://qt-project.org/wiki/PySideDocumentation) : from the Qt Project (the people who wrote it all)
  * [Using QtCreator in PySide](http://qt-project.org/wiki/QtCreator_and_PySide) : also from the Qt Project
  * [PySide reference](http://srinikom.github.io/pyside-docs/index.html) : endless detail on the minutiae of PySide and Qt, a reliable reference source
  * [PySide code snippets](http://nullege.com/codes/search?cq=PySide) : a searchable database of PySide code snippets

The following two references are PyQt specific (not PySide) but may offer some
information of use:

  * [Basic PyQt tutorial](http://www.cs.usfca.edu/~afedosov/qttut/) : A simple and short linux-based tutorial that will explain how to work with PyQt and Qt Designer
  * [Programming Qt applications in python](http://vizzzion.org/?id=pyqt) : A more in-depth tutorial covering all the process of working with qt and python

**Pivy** \- How to interact with FreeCAD's 3D scenes

  * [Pivy - Embedding a Dynamic Scripting Language into a Scene Graph Library](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.108.947&rep=rep1&type=pdf) : Thesis that explains Pivy in detail
  * [High Level 3D Graphics Programming in Python](http://ftp.ntua.gr/mirror/python/pycon/dc2004/papers/47/) : Pivy example from Pycon 2004
  * [Introducing Pivy into studierstube](https://www.semanticscholar.org/paper/Integrating-Pivy-into-Studierstube-4.2-Gruber/08c9a89c8326c87f81c2d83428029fbfb6c2ae64) [(Mirror)](https://www.researchgate.net/publication/228737136_Integrating_Pivy_into_Studierstube_42) : A paper that is not really a tutorial, but that illustrates well how Pivy works (requires an academic account)

## Community projects

On the [Community portal](/FreeCAD_Community_Portal "FreeCAD Community
Portal"), you can find other FreeCAD-based projects run by the FreeCAD users
community. If you are starting a new FreeCAD project, be sure to list it
there! We also have a page with things you can do if you would like to [Help
FreeCAD](/Help_FreeCAD "Help FreeCAD").

  

Expand[![](/images/thumb/8/8f/Power_user_hub.png/24px-
Power_user_hub.png)](/index.php?title=File:Power_user_hub.png&filetimestamp=20200511213015&)
Power user documentation

  * **FreeCAD scripting:** [Python](/index.php?title=Python/fi&action=edit&redlink=1 "Python/fi \(page does not exist\)"), [Introduction to Python](/index.php?title=Introduction_to_Python/fi&action=edit&redlink=1 "Introduction to Python/fi \(page does not exist\)"), [Python scripting tutorial](/index.php?title=Python_scripting_tutorial/fi&action=edit&redlink=1 "Python scripting tutorial/fi \(page does not exist\)"), [FreeCAD Scripting Basics](/index.php?title=FreeCAD_Scripting_Basics/fi&action=edit&redlink=1 "FreeCAD Scripting Basics/fi \(page does not exist\)")

* * *

  * **Modules:** [Builtin modules](/index.php?title=Builtin_modules/fi&action=edit&redlink=1 "Builtin modules/fi \(page does not exist\)"), [Units](/index.php?title=Units/fi&action=edit&redlink=1 "Units/fi \(page does not exist\)"), [Quantity](/index.php?title=Quantity/fi&action=edit&redlink=1 "Quantity/fi \(page does not exist\)")
  * **Workbenches:** [Workbench creation](/index.php?title=Workbench_creation/fi&action=edit&redlink=1 "Workbench creation/fi \(page does not exist\)"), [Gui Commands](/index.php?title=Gui_Command/fi&action=edit&redlink=1 "Gui Command/fi \(page does not exist\)"), [Commands](/index.php?title=Command/fi&action=edit&redlink=1 "Command/fi \(page does not exist\)"), [Installing more workbenches](/index.php?title=Installing_more_workbenches/fi&action=edit&redlink=1 "Installing more workbenches/fi \(page does not exist\)")
  * **Meshes and Parts:** [Mesh Scripting](/index.php?title=Mesh_Scripting/fi&action=edit&redlink=1 "Mesh Scripting/fi \(page does not exist\)"), [Topological data scripting](/index.php?title=Topological_data_scripting/fi&action=edit&redlink=1 "Topological data scripting/fi \(page does not exist\)"), [Mesh to Part](/index.php?title=Mesh_to_Part/fi&action=edit&redlink=1 "Mesh to Part/fi \(page does not exist\)"), [PythonOCC](/index.php?title=PythonOCC/fi&action=edit&redlink=1 "PythonOCC/fi \(page does not exist\)")

* * *

  * **Parametric objects:** [Scripted objects](/Scripted_objects/fi "Scripted objects/fi"), [Viewproviders](/index.php?title=Viewprovider/fi&action=edit&redlink=1 "Viewprovider/fi \(page does not exist\)") ([Custom icon in tree view](/index.php?title=Custom_icon_in_tree_view/fi&action=edit&redlink=1 "Custom icon in tree view/fi \(page does not exist\)"))
  * **Scenegraph:** [Coin (Inventor) scenegraph](/index.php?title=Scenegraph/fi&action=edit&redlink=1 "Scenegraph/fi \(page does not exist\)"), [Pivy](/index.php?title=Pivy/fi&action=edit&redlink=1 "Pivy/fi \(page does not exist\)")
  * **Graphical interface:** [Interface creation](/index.php?title=Interface_creation/fi&action=edit&redlink=1 "Interface creation/fi \(page does not exist\)"), [Interface creation completely in Python](/index.php?title=Dialog_creation/fi&action=edit&redlink=1 "Dialog creation/fi \(page does not exist\)") ([1](/index.php?title=Dialog_creation_with_various_widgets/fi&action=edit&redlink=1 "Dialog creation with various widgets/fi \(page does not exist\)"), [2](/index.php?title=Dialog_creation_reading_and_writing_files/fi&action=edit&redlink=1 "Dialog creation reading and writing files/fi \(page does not exist\)"), [3](/index.php?title=Dialog_creation_setting_colors/fi&action=edit&redlink=1 "Dialog creation setting colors/fi \(page does not exist\)"), [4](/index.php?title=Dialog_creation_image_and_animated_GIF/fi&action=edit&redlink=1 "Dialog creation image and animated GIF/fi \(page does not exist\)"), [5](/index.php?title=PySide_usage_snippets/fi&action=edit&redlink=1 "PySide usage snippets/fi \(page does not exist\)")), [PySide](/index.php?title=PySide/fi&action=edit&redlink=1 "PySide/fi \(page does not exist\)"), PySide examples [beginner](/index.php?title=PySide_Beginner_Examples/fi&action=edit&redlink=1 "PySide Beginner Examples/fi \(page does not exist\)"), [intermediate](/index.php?title=PySide_Intermediate_Examples/fi&action=edit&redlink=1 "PySide Intermediate Examples/fi \(page does not exist\)"), [advanced](/index.php?title=PySide_Advanced_Examples/fi&action=edit&redlink=1 "PySide Advanced Examples/fi \(page does not exist\)")
  * **Macros:** [Macros](/index.php?title=Macros/fi&action=edit&redlink=1 "Macros/fi \(page does not exist\)"), [How to install macros](/index.php?title=How_to_install_macros/fi&action=edit&redlink=1 "How to install macros/fi \(page does not exist\)")
  * **Embedding:** [Embedding FreeCAD](/index.php?title=Embedding_FreeCAD/fi&action=edit&redlink=1 "Embedding FreeCAD/fi \(page does not exist\)"), [Embedding FreeCADGui](/index.php?title=Embedding_FreeCADGui/fi&action=edit&redlink=1 "Embedding FreeCADGui/fi \(page does not exist\)")

* * *

  * **Other:** [Expressions](/index.php?title=Expressions/fi&action=edit&redlink=1 "Expressions/fi \(page does not exist\)"), [Code snippets](/index.php?title=Code_snippets/fi&action=edit&redlink=1 "Code snippets/fi \(page does not exist\)"), [Line drawing function](/index.php?title=Line_drawing_function/fi&action=edit&redlink=1 "Line drawing function/fi \(page does not exist\)"), [FreeCAD vector math library](/index.php?title=FreeCAD_vector_math_library/fi&action=edit&redlink=1 "FreeCAD vector math library/fi \(page does not exist\)") (deprecated)

* * *

  * **Hubs:** [User hub](/User_hub/fi "User hub/fi"), Power users hub, [Developer hub](/index.php?title=Developer_hub/fi&action=edit&redlink=1 "Developer hub/fi \(page does not exist\)")

