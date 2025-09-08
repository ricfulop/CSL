---
url: https://wiki.freecad.org/Exposing_C%2B%2B_to_Python
title: Exposing C%2B%2B to Python
scraped_at: 2025-09-08 16:46:33
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 How to expose c++ functionality to Python Toggle How to expose c++ functionality to Python subsection
    * 1.1 Further Elaboration
    * 1.2 Related Links

# Exposing Cplusplus to Python

  * [Page](/Exposing_Cplusplus_to_Python "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Exposing_Cplusplus_to_Python&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Exposing_Cplusplus_to_Python)
  * [Edit](/index.php?title=Exposing_Cplusplus_to_Python&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Exposing_Cplusplus_to_Python&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Exposing_Cplusplus_to_Python.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Exposing_Cplusplus_to_Python&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Exposing_Cplusplus_to_Python)
  * [Edit](/index.php?title=Exposing_Cplusplus_to_Python&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Exposing_Cplusplus_to_Python&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Exposing_Cplusplus_to_Python&action=history)

General

  * [What links here](/Special:WhatLinksHere/Exposing_Cplusplus_to_Python "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Exposing_Cplusplus_to_Python "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Exposing_Cplusplus_to_Python&oldid=1188867 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Exposing_Cplusplus_to_Python&action=info "More information about this page")

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Exposing_Cplusplus_to_Python&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Exposing+Cplusplus+to+Python&action=page&filter=&language=en)(Redirected from
[Exposing C++ to
Python](/index.php?title=Exposing_C%2B%2B_to_Python&redirect=no "Exposing C++
to Python"))  
  
This is the approved revision of this page, as well as being the most recent.

This documentation is not finished. Please help and contribute documentation.

[GuiCommand model](/GuiCommand_model "GuiCommand model") explains how commands
should be documented. Browse
[Category:UnfinishedDocu](/Category:UnfinishedDocu "Category:UnfinishedDocu")
to see more incomplete pages like this one. See [Category:Command
Reference](/Category:Command_Reference "Category:Command Reference") for all
commands.

See [WikiPages](/WikiPages "WikiPages") to learn about editing the wiki pages,
and go to [Help FreeCAD](/Help_FreeCAD "Help FreeCAD") to learn about other
ways in which you can contribute.

This documentation is a stub and needs more work, perhaps a written example +
links to commits demonstrating in the commit history

## How to expose c++ functionality to Python

It becomes necessary at times to expand the FreeCAD API further by exposing
functions that are available in the source code in c++ to the python. In so
doing, providing an ability to trigger deep internal functionality with Python
in real-time instead of needing to compile.

Below is an explanation of how one can achieve this.

The basic structure of a program to expose functionality to Python is
something like this:

  * get the `Py` object parameters and convert them to c++ variables using `PyArg_ParseTuple()`,
  * use various `c++` routines from **OpenCascade** and/or **FreeCAD** to produce the desired result,
  * convert the `c++` result into `Py` object using routines like `PyLong_AsLong()`, `Py::asObject()`, etc,
  * return the `Py` object.

### Further Elaboration

There are two source files required to implement a new Python binding.
Assuming we wanted to expose some methods from
[`FreeCAD/src/Mod/Part/TopoShape.cpp`](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Part/TopoShape.cpp),
we would need to make:

  * `TopoShapePy.xml` \- definitions of the functions for be exposed in XML format. This file is used to generate header files for our next file...
  * `TopoShapePyImp.cpp` \- the actual C++ code that bridges from Python to C++.

These 2 files need to be added to **`../Mod/yourModule/App/CMakeLists.txt`**.
See
[`FreeCAD/src/Mod/Part/App/CMakeLists.txt`](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Part/App/AppPartPy.cpp)
for an example.

You can extend the Python version of your module by adding to
**`../Mod/yourModule/App/AppmyModulePy.cpp`** (see
[`FreeCAD/src/Mod/Part/AppPartPy.cpp`](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Part/App/AppPartPy.cpp)).
The additions are accessed in Python by "`import myModule`".

Note:

  1. `xxxxxPyImp` routines return a `PyObject*` pointer (see `TopoShapePyImp.cpp`)
  2. `AppmyModulePy.cpp` routines return a `Py::Object` (see [`FreeCAD/src/Mod/Part/AppPartPy.cpp`](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Part/App/AppPartPy.cpp)).

### Related Links

  * Source: <https://forum.freecadweb.org/viewtopic.php?p=314796#p314617>
  * [Forum discussion: Adding Commands in Python to C++ Workbench](https://forum.freecadweb.org/viewtopic.php?p=560639#p560639)
  * Another forum thread: [https://forum.freecadweb.org/viewtopic.php?f=10&t=70750](https://forum.freecadweb.org/viewtopic.php?f=10&t=70750)
  * [Workbench creation](/Workbench_creation "Workbench creation")

