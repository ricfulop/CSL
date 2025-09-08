---
url: https://wiki.freecad.org/Profiling
title: Profiling
scraped_at: 2025-09-08 16:43:02
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Description
  * 2 Resources

# Profiling

  * [Page](/Profiling "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Profiling&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Profiling)
  * [Edit](/index.php?title=Profiling&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Profiling&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Profiling.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Profiling&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Profiling)
  * [Edit](/index.php?title=Profiling&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Profiling&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Profiling&action=history)

General

  * [What links here](/Special:WhatLinksHere/Profiling "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Profiling "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Profiling&oldid=1602814 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Profiling&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Profiling&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Profiling&action=page&filter=&language=en)This is the approved revision of
this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Profiling&language=&task=view "Start translation for this language")
  * [Deutsch](/Profiling/de "Profilieren \(88% translated\)")
  * English
  * [français](/Profiling/fr "Profilage \(100% translated\)")
  * [italiano](/Profiling/it "Profilazione \(100% translated\)")
  * [polski](/Profiling/pl "Profilowanie kodu \(100% translated\)")
  * [русский](/Profiling/ru "Профилирование \(25% translated\)")

## Description

Profiling the code of FreeCAD helps find bottlenecks in the algorithms used to
create or manipulate objects.

To profile [Python](/Python "Python") code use the standard `cProfile` module
to define start and end points to profile in the code.

    
    
    import cProfile
    pr = cProfile.Profile()
    pr.enable()
    
    # --------------------------------------
    # Lines of code that you want to profile
    # --------------------------------------
    
    pr.disable()
    pr.dump_stats("/tmp/profile.cprof")
    

Then install and use `pyprof2calltree` to convert the profile output into
cachegrind input.

    
    
    pyprof2calltree -i /tmp/profile.cprof -o /tmp/callgrind.out
    

Then visualize this information with `kcachegrind` for Linux or `qcachegrind`
for Windows.

    
    
    kcachegrind /tmp/callgrind.out
    

## Resources

  * [The Python profilers](https://docs.python.org/3/library/profile.html), `cProfile` and `python`.
  * [pyprof2calltree](https://pypi.org/project/pyprof2calltree/) at PyPI; [pyprof2calltree](https://github.com/pwaller/pyprof2calltree/) repository.
  * [FreeCAD's Python profiling tutorial](https://forum.freecad.org/viewtopic.php?f=10&t=44785).

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

