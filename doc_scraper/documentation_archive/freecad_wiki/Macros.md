---
url: https://wiki.freecad.org/Macros
title: Macros
scraped_at: 2025-09-08 16:41:49
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction
  * 2 How it works
  * 3 Example
  * 4 Customizing
  * 5 Creating macros without recording
  * 6 Macro repositories
  * 7 Additional information
  * 8 Tutorials

# Macros

  * [Page](/Macros "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Macros&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Macros)
  * [Edit](/index.php?title=Macros&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Macros&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Macros.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Macros&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Macros)
  * [Edit](/index.php?title=Macros&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Macros&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Macros&action=history)

General

  * [What links here](/Special:WhatLinksHere/Macros "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Macros "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Macros&oldid=1638047 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Macros&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Macros&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Macros&action=page&filter=&language=en)This is the approved revision of this
page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Macros&language=&task=view "Start translation for this language")
  * [Bahasa Indonesia](/Macros/id "Macros \(7% translated\)")
  * [Deutsch](/Macros/de "Makros \(100% translated\)")
  * English
  * [Türkçe](/Macros/tr "Macros \(4% translated\)")
  * [español](/Macros/es "Macros \(61% translated\)")
  * [français](/Macros/fr "Macros \(100% translated\)")
  * [italiano](/Macros/it "Macro \(100% translated\)")
  * [polski](/Macros/pl "Makrodefinicje \(100% translated\)")
  * [português](/Macros/pt "Macros \(7% translated\)")
  * [português do Brasil](/Macros/pt-br "Macros \(4% translated\)")
  * [română](/Macros/ro "Macro comenzi \(7% translated\)")
  * [svenska](/Macros/sv "Macros \(7% translated\)")
  * [čeština](/Macros/cs "Makra \(11% translated\)")
  * [български](/Macros/bg "Macros/bg \(0% translated\)")
  * [русский](/Macros/ru "Макросы \(71% translated\)")
  * [中文（中国大陆）](/Macros/zh-cn "宏 \(14% translated\)")
  * [日本語](/Macros/ja "Macros/マクロ \(7% translated\)")
  * [한국어](/Macros/ko "매크로 \(100% translated\)")

![](/images/6/6f/Arrow-left.svg) [Scripting and macros](/Scripting_and_macros
"Scripting and macros")

[Scripts](/Scripts "Scripts") ![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

## Introduction

Macros are a convenient way to reproduce complex actions in FreeCAD. You
simply record actions as you do them, then save those actions under a name,
and replay them whenever you want. Since macros are in reality a list of
[Python](/Python "Python") commands, you can also edit them, and create very
complex scripts.

While Python scripts normally have the `.py` extension, FreeCAD macros should
have the `.FCMacro` extension. A collection of macros written by experienced
users is found in the [macros recipes](/Macros_recipes "Macros recipes") page.

See the [Power users hub](/Power_users_hub "Power users hub") to learn more
about the [Python](/Python "Python") programming language, and about writing
macros. In particular, you should start with these pages:

  * [Introduction to Python](/Introduction_to_Python "Introduction to Python")
  * [Python scripting tutorial](/Python_scripting_tutorial "Python scripting tutorial")
  * [FreeCAD Scripting Basics](/FreeCAD_Scripting_Basics "FreeCAD Scripting Basics")

## How it works

Enable the console output in the menu **Edit → Preferences → Python → Macro →
Show scripts commands in python console**. You will see that in FreeCAD, every
action you do, such as pressing a button, outputs a Python command. Those
commands are what can be recorded in a macro. The main tool for making macros
is the macros toolbar:
[![](/images/0/09/Macros_toolbar.jpg)](/index.php?title=File:Macros_toolbar.jpg&filetimestamp=20090726225614&).
On it you have 4 buttons: Record, stop recording, edit and play the current
macro.

It is very simple to use: Press the record button, you will be asked to give a
name to your macro, then perform some actions. When you are done, click the
stop recording button, and your actions will be saved. You can now access the
macro dialog with the edit button.

[![](/images/8/84/Macros.png)](/index.php?title=File:Macros.png&filetimestamp=20241110085825&)

Macro dialog, listing the macros available in the system

There you can manage your macros, delete, edit, duplicate, install or create
new ones from scratch. If you edit a macro, it will be opened in an editor
window where you can make changes to its code. New macros can be installed
using the Addons... button, which links to the [Addon Manager](/Std_AddonMgr
"Std AddonMgr").

## Example

Press the record button, give a name, let's say "cylinder 10x10", then, in the
[Part Workbench](/Part_Workbench "Part Workbench"), create a cylinder with
radius = 10 and height = 10. Then, press the "stop recording" button. In the
edit macros dialog, you can see the python code that has been recorded, and,
if you want, make alterations to it. To execute your macro, simply press the
execute button on the toolbar while your macro is in the editor. You macro is
always saved to disk, so any change you make, or any new macro you create,
will always be available next time you start FreeCAD.

## Customizing

Of course it is not practical to load a macro in the editor in order to use
it. FreeCAD provides much better ways to use your macro, such as assigning a
keyboard shortcut to it or putting an entry in the menu. Once your macro is
created, all this can be done via the **Tools → Customize** menu.

[![](/images/b/ba/Macros_config.jpg)](/index.php?title=File:Macros_config.jpg&filetimestamp=20090727004641&)

This way you can make your macro become a real tool, just like any standard
FreeCAD tool. This, added to the power of python scripting within FreeCAD,
makes it possible to easily add your own tools to the interface.

See [Customize Toolbars](/Customize_Toolbars "Customize Toolbars") for a more
detailed description.

## Creating macros without recording

You can also directly copy/paste python code into a macro, without recording
GUI action. Simply create a new macro, edit it, and paste your code. You can
then save your macro the same way as you save a FreeCAD document. Next time
you start FreeCAD, the macro will appear under the "Installed Macros" item of
the Macro menu.

See [How to install macros](/How_to_install_macros "How to install macros")
for a more detailed description.

## Macro repositories

There are two main places for macros. The first one is the official peer-
reviewed macro repository on [GitHub](https://github.com/FreeCAD/FreeCAD-
macros). The second one is the [Macros recipes](/Macros_recipes "Macros
recipes") page from which you can pick some useful macros to add to your
FreeCAD installation. Macros from both repositories can be installed via the
[Addon Manager](/Std_AddonMgr "Std AddonMgr") directly from FreeCAD.

## Additional information

  * [Automatically run macro at startup](/Macro_at_Startup "Macro at Startup")
  * [Installing more workbenches](/Installing_more_workbenches "Installing more workbenches")

## Tutorials

You can manually install extensions, however, it is much simpler to just use
the [Addon Manager](/Std_AddonMgr "Std AddonMgr").

  * [How to install macros](/How_to_install_macros "How to install macros")
  * [How to install additional workbenches](/How_to_install_additional_workbenches "How to install additional workbenches")

  

![](/images/6/6f/Arrow-left.svg) [Scripting and macros](/Scripting_and_macros
"Scripting and macros")

[Scripts](/Scripts "Scripts") ![](/images/a/af/Arrow-right.svg)

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
  * **Macros:** Macros, [How to install macros](/How_to_install_macros "How to install macros")
  * **Embedding:** [Embedding FreeCAD](/Embedding_FreeCAD "Embedding FreeCAD"), [Embedding FreeCADGui](/Embedding_FreeCADGui "Embedding FreeCADGui")

* * *

  * **Other:** [Expressions](/Expressions "Expressions"), [Code snippets](/Code_snippets "Code snippets"), [Line drawing function](/Line_drawing_function "Line drawing function"), [FreeCAD vector math library](/FreeCAD_vector_math_library "FreeCAD vector math library") (deprecated)

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

