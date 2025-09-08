---
url: https://wiki.freecad.org/How_to_install_macros
title: How to install macros
scraped_at: 2025-09-08 16:47:09
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Description
  * 2 The Macro menu and toolbar Toggle The Macro menu and toolbar subsection
    * 2.1 Toolbar
    * 2.2 Menu
  * 3 Macros directory Toggle Macros directory subsection
    * 3.1 Default directory
    * 3.2 Configuring the user directory
  * 4 Installing macros Toggle Installing macros subsection
    * 4.1 Automatic method
    * 4.2 Manual method 1. Copy the code to the macro editor
    * 4.3 Manual method 2. Add a macro file from a compressed .zip file
  * 5 Execute a macro in command line
  * 6 Errors in macros Toggle Errors in macros subsection
    * 6.1 Indentation errors
      * 6.1.1 Example 1
      * 6.1.2 Example 2
      * 6.1.3 Example 3
      * 6.1.4 Example 4
      * 6.1.5 Good code
    * 6.2 No text output from macros
      * 6.2.1 Printing information
      * 6.2.2 Enabling the report view
      * 6.2.3 Enabling the print() command

# How to install macros

  * [Page](/How_to_install_macros "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:How_to_install_macros&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/How_to_install_macros)
  * [Edit](/index.php?title=How_to_install_macros&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=How_to_install_macros&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/How_to_install_macros.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=How_to_install_macros&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/How_to_install_macros)
  * [Edit](/index.php?title=How_to_install_macros&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=How_to_install_macros&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=How_to_install_macros&action=history)

General

  * [What links here](/Special:WhatLinksHere/How_to_install_macros "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/How_to_install_macros "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=How_to_install_macros&oldid=1604470 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=How_to_install_macros&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=How_to_install_macros&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
How+to+install+macros&action=page&filter=&language=en)This is the approved
revision of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-How+to+install+macros&language=&task=view "Start translation for this language")
  * [Deutsch](/How_to_install_macros/de "Wie man Makros installiert \(100% translated\)")
  * English
  * [Türkçe](/How_to_install_macros/tr "How to install macros/tr \(1% translated\)")
  * [español](/How_to_install_macros/es "How to install macros/es \(0% translated\)")
  * [français](/How_to_install_macros/fr "Comment installer des macros \(100% translated\)")
  * [hrvatski](/How_to_install_macros/hr "How to install macros/hr \(1% translated\)")
  * [italiano](/How_to_install_macros/it "Come installare le macro \(100% translated\)")
  * [polski](/How_to_install_macros/pl "Jak zainstalować makrodefinicje \(100% translated\)")
  * [português do Brasil](/How_to_install_macros/pt-br "Como instalar macros \(1% translated\)")
  * [română](/How_to_install_macros/ro "Cum se instalează macrocomenzile \(2% translated\)")
  * [svenska](/How_to_install_macros/sv "Macro Install HowTo \(0% translated\)")
  * [čeština](/How_to_install_macros/cs "How to install macros/cs \(0% translated\)")
  * [русский](/How_to_install_macros/ru "Как установить макросы \(10% translated\)")
  * [日本語](/How_to_install_macros/ja "マクロのインストール方法 \(1% translated\)")
  * [한국어](/How_to_install_macros/ko "매크로 설치방법 \(57% translated\)")

![](/images/0/06/Freecad.svg) Tutorial  
---  
Topic  
Programming  
Level  
Medium programmer  
Time to complete  
15 minutes  
Authors  
[Mario52](/User:Mario52 "User:Mario52")  
FreeCAD version  
All  
Example files  
_None_  
See also  
_None_  
  
  
  
## Description

Since v0.17 it is easy to add macros by using the [Addon
Manager](/Std_AddonMgr "Std AddonMgr"). A regular user doesn't need to do more
than use this tool. Keep reading for more information regarding installation
of [macros](/Macros "Macros").

Macros are sequences of commands which are used to perform a complex drawing
operation. Macros are [Python](/Python "Python") scripts, which means they are
text files that can be written and edited with a text editor.

While Python scripts normally have the `.py` extension, FreeCAD macros should
have the `.FCMacro` extension. A collection of macros written by experienced
users is found in the [macros recipes](/Macros_recipes "Macros recipes") page.

See [Introduction to Python](/Introduction_to_Python "Introduction to Python")
to learn about the Python programming language, and then [Python scripting
tutorial](/Python_scripting_tutorial "Python scripting tutorial") and [FreeCAD
Scripting Basics](/FreeCAD_Scripting_Basics "FreeCAD Scripting Basics") to
learn about writing macros.

Here is a video on [installing FreeCAD macros in
Ubuntu](https://wiki.opensourceecology.org/wiki/Installing_Macros_in_FreeCAD).

## The Macro menu and toolbar

### Toolbar

  * [![](/images/1/14/Std_DlgMacroRecord.svg)](/index.php?title=File:Std_DlgMacroRecord.svg&filetimestamp=20240704212317&) [Macro recording...](/Std_DlgMacroRecord "Std DlgMacroRecord")
  * [![](/images/f/f1/Std_MacroStopRecord.svg)](/index.php?title=File:Std_MacroStopRecord.svg&filetimestamp=20240704212620&) [Stop macro recording](/Std_MacroStopRecord "Std MacroStopRecord")
  * [![](/images/b/b2/Std_DlgMacroExecute.svg)](/index.php?title=File:Std_DlgMacroExecute.svg&filetimestamp=20240704212406&) [Macros...](/Std_DlgMacroExecute "Std DlgMacroExecute")
  * [![](/images/f/f7/Std_DlgMacroExecuteDirect.svg)](/index.php?title=File:Std_DlgMacroExecuteDirect.svg&filetimestamp=20240704212444&) [Execute macro](/Std_DlgMacroExecuteDirect "Std DlgMacroExecuteDirect")

### Menu

Besides the tools in the toolbar, the following functions are also available
in the **Macro** menu.

  * [Attach to remote debugger](/Std_MacroAttachDebugger "Std MacroAttachDebugger")
  * [![](/images/4/4f/Std_MacroStartDebug.svg)](/index.php?title=File:Std_MacroStartDebug.svg&filetimestamp=20240704212534&) [Debug macro](/Std_MacroStartDebug "Std MacroStartDebug")
  * [![](/images/a/a0/Std_MacroStopDebug.svg)](/index.php?title=File:Std_MacroStopDebug.svg&filetimestamp=20240704212549&) [Stop debugging](/Std_MacroStopDebug "Std MacroStopDebug")
  * [Step over](/Std_MacroStepOver "Std MacroStepOver")
  * [Step into](/Std_MacroStepInto "Std MacroStepInto")
  * [Toggle breakpoint](/Std_ToggleBreakpoint "Std ToggleBreakpoint")

## Macros directory

Expand

Macros are created in a specific folder under the user's FreeCAD directory.
This directory can be configured in the [Execute macro
dialog](/Std_DlgMacroExecute "Std DlgMacroExecute"), or in the [Preferences
Editor](/Preferences_Editor "Preferences Editor"), through the menu **Edit →
Preferences → Python → Macro → Macro recording settings**.

Downloaded macros should also be placed in this directory.

### Default directory

Macros can be simply copied into

    
    
    $ROOT_DIR/
    

where `$ROOT_DIR` is a top level directory searched by FreeCAD on startup.

The `$ROOT_DIR` could be a system wide directory, in which case the macro is
installed for all users.

  * On Linux it is usually `/usr/share/freecad/`
  * On Windows it is usually `C:\Program Files\FreeCAD\`
  * On Mac OSX it is usually `/Applications/FreeCAD/`

The `$ROOT_DIR` could be a particular user's directory.

  * On Linux it is usually `/home/username/.local/share/FreeCAD/` (0.20 and above) or `/home/username/.FreeCAD/` (0.19 and below).
  * On Windows it is usually `C:\Users\username\AppData\FreeCAD\`
  * On Mac OSX it is usually `/Users/username/Library/Preferences/FreeCAD/`

### Configuring the user directory

1\. Open the menu **Macro
→[![](/images/b/b2/Std_DlgMacroExecute.svg)](/index.php?title=File:Std_DlgMacroExecute.svg&filetimestamp=20240704212406&)
[Macros...](/Std_DlgMacroExecute "Std DlgMacroExecute")** to open the [Execute
macro dialog](/Std_DlgMacroExecute "Std DlgMacroExecute").

[![](/images/5/56/Dxf_Importer_Install_01.png)](/index.php?title=File:Dxf_Importer_Install_01.png&filetimestamp=20141219175606&)

Opening the Execute macro dialog

2\. Set the appropriate `User macros location`.

  * Linux: usually `/home/username/.local/share/FreeCAD/` (0.20 and above) or `/home/username/.FreeCAD/` (0.19 and below)
  * Windows: usually `C:\Users\username\AppData\Roaming\FreeCAD\`
  * MacOS: usually `/Users/username/Library/Preferences/FreeCAD/`

[![](/images/c/c2/Dxf_Importer_Install_02.png)](/index.php?title=File:Dxf_Importer_Install_02.png&filetimestamp=20141219175658&)

Setting of the macros directory

3\. Navigate to that directory in your computer.

  * Linux: paste the address into your file manager, "Nautilus" or other. You may have to press Ctrl+H to make the hidden directory `.FreeCAD/` visible.
  * Windows: paste the address into your "File explorer" and confirm.
  * MacOS: locate the folder in the "Finder" or paste the address into a "File explorer"; remember the `file:///` prefix in the "File explorer" for a file on disk.

[![](/images/4/49/Dxf_Importer_Install_03.png)](/index.php?title=File:Dxf_Importer_Install_03.png&filetimestamp=20141219175733&)

Accessing the macros directory in the operating system

4\. Add macro files to this directory.

  * Linux: leave the file manager open, and bookmark the location for faster access.
  * Windows: leave open the file explorer.
  * MacOS: either leave a "Finder" window open, or bookmark the location in your "File explorer", or set up an "Alias" to point to it, or drag the folder into the "SideBar" of the "Finder" so it is there to use from other programs such as text editors.

[![](/images/2/2f/Dxf_Importer_Install_04.png)](/index.php?title=File:Dxf_Importer_Install_04.png&filetimestamp=20141219175807&)

Macros directory

## Installing macros

Expand

### Automatic method

Starting with FreeCAD 0.17, use the [Addon Manager](/Std_AddonMgr "Std
AddonMgr") in **Tools → Addon manager** to install a macro that has been
included in the [FreeCAD-macros](https://github.com/FreeCAD/FreeCAD-macros)
repository.

In past versions of FreeCAD you could use two automated ways to install macros
and other addons:

  * [addons_installer.FCMacro](https://github.com/FreeCAD/FreeCAD-addons): itself a macro, this was the precursor to the Addon Manager, and is hosted in the [FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons) repository. You don't need to use this tool in new installations of FreeCAD.
  * [freecad-pluginloader](https://github.com/microelly2/freecad-pluginloader): also a macro, it could be used to install new components to FreeCAD. It is no longer developed.

The recommended way to install addons, that is, [external
workbenches](/External_workbenches "External workbenches") and macros, is the
[Addon Manager](/Std_AddonMgr "Std AddonMgr"). However, you can still add
macros to your system with the manual methods described in the following
sections; this is useful if you are developing and testing your own code.

Expand

### Manual method 1. Copy the code to the macro editor

For macros that are relatively small, 300 lines or less, the code can be
copied and pasted directly into the FreeCAD macro editor.

We will use
[![](/images/4/4e/Part_Prism_Apothem.svg)](/index.php?title=File:Part_Prism_Apothem.svg&filetimestamp=20141024202313&)
[Macro Apothem Based Prism GUI](/Macro_Apothem_Based_Prism_GUI "Macro Apothem
Based Prism GUI") as an example.

1\. Go to the macro wiki page, which should be listed in [Macros
recipes](/Macros_recipes "Macros recipes").

If there is a custom icon download it; click on it with the right mouse button
and select `Save image as...`; place the icon in the macros directory. This
icon can be used as a shortcut for the macro in a [custom
toolbar](/Customize_Toolbars "Customize Toolbars"). The default icon is
[![](/images/thumb/2/2c/Text-x-python.png/24px-Text-x-
python.png)](/index.php?title=File:Text-x-
python.png&filetimestamp=20121224162851&).

[![](/images/6/60/Macro_Install_HowTo_28.png)](/index.php?title=File:Macro_Install_HowTo_28.png&filetimestamp=20141228201928&)

Downloading the icon from the macro page

2\. In the macro page, select the code inside the _Script_ or _Macro_
sections, and copy it.

3\. In FreeCAD, open the menu **Macro
→[![](/images/b/b2/Std_DlgMacroExecute.svg)](/index.php?title=File:Std_DlgMacroExecute.svg&filetimestamp=20240704212406&)
[Macros...](/Std_DlgMacroExecute "Std DlgMacroExecute")** to open the [Execute
macro dialog](/Std_DlgMacroExecute "Std DlgMacroExecute").

[![](/images/5/56/Dxf_Importer_Install_01.png)](/index.php?title=File:Dxf_Importer_Install_01.png&filetimestamp=20141219175606&)

Opening the Execute macro dialog

4\. Click Create.

[![](/images/c/c0/Macro_Install_HowTo_17.png)](/index.php?title=File:Macro_Install_HowTo_17.png&filetimestamp=20141227210134&)

Creating a new macro

5\. Enter the macro name, here `Macro_Apothem_Based_Prism_GUI`, and press OK.

[![](/images/9/9b/Macro_Install_HowTo_18.png)](/index.php?title=File:Macro_Install_HowTo_18.png&filetimestamp=20141227210220&)

Entering the macro name

6\. The macro editor opens, showing the full path of the new macro.

[![](/images/6/62/Macro_Install_HowTo_19.png)](/index.php?title=File:Macro_Install_HowTo_19.png&filetimestamp=20141227210254&)

The macro editor

7\. Paste the code in the editor window, and then click the cross on the tab
to close the window.

[![](/images/9/9c/Macro_Install_HowTo_20.png)](/index.php?title=File:Macro_Install_HowTo_20.png&filetimestamp=20141227210331&)

Closing the macro editor

8\. A window appears asking for confirmation to save the code; click on Yes.
You can also use Ctrl+S to save the file.

Restart FreeCAD to correctly register the new macro.

[![](/images/7/7f/Macro_Install_HowTo_27.png)](/index.php?title=File:Macro_Install_HowTo_27.png&filetimestamp=20141227215236&)

Asking for confirmation to save the code

9\. Open the menu again, **Macro
→[![](/images/b/b2/Std_DlgMacroExecute.svg)](/index.php?title=File:Std_DlgMacroExecute.svg&filetimestamp=20240704212406&)
[Macros...](/Std_DlgMacroExecute "Std DlgMacroExecute")**, select the new
macro and press Execute.

[![](/images/b/b9/Macro_Install_HowTo_21.png)](/index.php?title=File:Macro_Install_HowTo_21.png&filetimestamp=20141227210402&)

Selecting the macro to run it

10\. The macro now runs. Fill in the fields with your values and click the OK
button.

[![](/images/4/45/Macro_Install_HowTo_22.png)](/index.php?title=File:Macro_Install_HowTo_22.png&filetimestamp=20141227210448&)

The macro in action; fill in the information and press OK when ready

11\. This macro should return an error if no document is active; other macros
open a new document if none exists.

Create a new document with **File
→[![](/images/d/d4/Std_New.svg)](/index.php?title=File:Std_New.svg&filetimestamp=20240528091658&)
[New](/Std_New "Std New")**, and then repeat the previous steps to execute the
macro.

[![](/images/0/0d/Macro_Install_HowTo_23.png)](/index.php?title=File:Macro_Install_HowTo_23.png&filetimestamp=20141227210813&)

The macro returning an error if no document is active

12\. Once an active document is available, the macro runs and creates an
object.

[![](/images/2/24/Macro_Install_HowTo_24.png)](/index.php?title=File:Macro_Install_HowTo_24.png&filetimestamp=20141227210525&)

Object created by the macro

13\. You can open the macro in the editor again to run it or modify it. Go to
**Macro
→[![](/images/b/b2/Std_DlgMacroExecute.svg)](/index.php?title=File:Std_DlgMacroExecute.svg&filetimestamp=20240704212406&)
[Macros...](/Std_DlgMacroExecute "Std DlgMacroExecute")**, select the macro
and press Edit.

[![](/images/5/52/Macro_Install_HowTo_25.png)](/index.php?title=File:Macro_Install_HowTo_25.png&filetimestamp=20141227210606&)

Opening the macro in the editor

14\. The macro can now be run with **Macro
→[![](/images/f/f7/Std_DlgMacroExecuteDirect.svg)](/index.php?title=File:Std_DlgMacroExecuteDirect.svg&filetimestamp=20240704212444&)
[Execute macro](/Std_DlgMacroExecuteDirect "Std DlgMacroExecuteDirect")**, or
by clicking on the
[![](/images/f/f7/Std_DlgMacroExecuteDirect.svg)](/index.php?title=File:Std_DlgMacroExecuteDirect.svg&filetimestamp=20240704212444&)
[Std DlgMacroExecuteDirect](/Std_DlgMacroExecuteDirect "Std
DlgMacroExecuteDirect") button in the toolbar.

[![](/images/6/64/Macro_Install_HowTo_26.png)](/index.php?title=File:Macro_Install_HowTo_26.png&filetimestamp=20141227210650&)

Running the macro that is loaded in the editor

Expand

### Manual method 2. Add a macro file from a compressed .zip file

Some macros are too big that it's inconvenient to copy and paste them into the
macro editor, or they cannot be hosted in the wiki. In this case, the code may
be hosted somewhere else, in a Github repository, or in the [FreeCAD
forum](https://forum.freecad.org). The code may also be compressed into a
`.zip` file, tarball `.tar.xz`, or other type of archive if it contains
several files. If the code is distributed in this way, the archive should be
extracted and the files placed in the macros directory.

We will use [![](/images/thumb/2/2c/Text-x-python.png/24px-Text-x-
python.png)](/index.php?title=File:Text-x-
python.png&filetimestamp=20121224162851&) [Macro screw
maker](/Macro_screw_maker1_2 "Macro screw maker1 2") as an example.

1\. Download the compressed code from the forum, [Screw
Maker](https://forum.freecad.org/viewtopic.php?f=22&t=6558#p52887).

You need to use a decompressor to get the internal files.

  * For Windows you can use an application like [7-zip](http://www.7-zip.org/) or [L-Zarc](http://www.kanmandet.dk/?p=37) or [quickzip](http://www.quickzip.org/quickzip51.html).
  * For Linux you can use a command from the terminal

    
    
    unzip your_file.zip -d your_directory
    

2\. Download the compressed archive with the macro code to a local folder.

[![](/images/9/99/Macro_Install_HowTo_01.png)](/index.php?title=File:Macro_Install_HowTo_01.png&filetimestamp=20141229131247&)

Downloading the compressed archive to a local directory

3\. Decompress the file in the folder.

[![](/images/5/55/Macro_Install_HowTo_02.png)](/index.php?title=File:Macro_Install_HowTo_02.png&filetimestamp=20141229131446&)

Decompressing the file in the folder

4\. The decompressor creates a new directory with the unpacked files.

[![](/images/4/45/Macro_Install_HowTo_03.png)](/index.php?title=File:Macro_Install_HowTo_03.png&filetimestamp=20141229131622&)

New directory created after unpacking the archive

5\. Go inside the new directory, and copy or cut the macro file.

[![](/images/d/d0/Macro_Install_HowTo_04.png)](/index.php?title=File:Macro_Install_HowTo_04.png&filetimestamp=20141229131743&)

Entering the newly created directory with the decompressed macro file

6\. Go to the macro directory and paste the file there.

[![](/images/c/ce/Macro_Install_HowTo_05.png)](/index.php?title=File:Macro_Install_HowTo_05.png&filetimestamp=20141229131847&)

Placing the macro file in the macro directory

7\. In FreeCAD, open the menu **Macro
→[![](/images/b/b2/Std_DlgMacroExecute.svg)](/index.php?title=File:Std_DlgMacroExecute.svg&filetimestamp=20240704212406&)
[Macros...](/Std_DlgMacroExecute "Std DlgMacroExecute")** to open the [Execute
macro dialog](/Std_DlgMacroExecute "Std DlgMacroExecute").

[![](/images/2/2d/Macro_Install_HowTo_06.png)](/index.php?title=File:Macro_Install_HowTo_06.png&filetimestamp=20141226224922&)

Opening the Execute macro dialog

8\. Select the new macro and press Execute.

[![](/images/7/75/Macro_Install_HowTo_07.png)](/index.php?title=File:Macro_Install_HowTo_07.png&filetimestamp=20141229132111&)

Selecting the macro to run it

9\. The macro now runs. Select the desired options, and click the Create
button.

[![](/images/thumb/2/2d/Macro_Install_HowTo_08.png/640px-
Macro_Install_HowTo_08.png)](/index.php?title=File:Macro_Install_HowTo_08.png&filetimestamp=20141229132212&)

The macro in action; select the desired options, and press Create when ready

[![](/images/2/27/Macro_Install_HowTo_30.png)](/index.php?title=File:Macro_Install_HowTo_30.png&filetimestamp=20141229132424&)

Object created by the macro

## Execute a macro in command line

Expand

Command line execute a macro (.FCMacro or .py)

on Windows

    
    
    "C:\Program Files\FreeCAD\bin\FreeCAD.exe" "C:\Users\userName\AppData\Roaming\FreeCAD\Mod\WorkFeature\start_WF.FCMacro"
    

on Linux

    
    
    todo
    

## Errors in macros

Expand

### Indentation errors

The white space at the beginning of the lines (indentation) in the
[Python](/Python "Python") programming language is very important, and an
integral part of the code. An inappropriate space may cause the code to not
run or present errors.

This section describes some errors that may be encountered when copying and
pasting, and writing macro code.

A typical indentation error looks like this:

    
    
    <unknown exception traceback><type 'exceptions.IndentationError'>: ('expected an indented block', ('C:/Users/d/AppData/Roaming/FreeCAD/Macro_Apothem_Based_Prism_GUI.FCMacro', 21, 3, 'def priSm(self):\n'))
    

#### Example 1

If the code lacks any indentation, the code won't work. Class (`class`) and
function definitions (`def()`), as well as control structures (`if`, `while`,
`for`) should be followed by a block of indented code.

This error is possible if the user doesn't copy the code correctly, and all
spaces are accidentally removed.

[![](/images/1/13/Macro_Install_HowTo_09.png)](/index.php?title=File:Macro_Install_HowTo_09.png&filetimestamp=20141226225324&)

Python code that lacks any indentation; it will cause an error when it's run

Indentation problem fixed.

[![](/images/9/96/Macro_Install_HowTo_10.png)](/index.php?title=File:Macro_Install_HowTo_10.png&filetimestamp=20141226225354&)

Python code with the correct indentation

If the code is selected, all lines should be highlighted all the way to the
left edge, indicating that the lines are aligned.

[![](/images/9/97/Macro_Install_HowTo_11.png)](/index.php?title=File:Macro_Install_HowTo_11.png&filetimestamp=20141226225506&)

Python code highlighted, showing that all lines start at the left edge

#### Example 2

If an additional space is introduced at the beginning of all lines, the Python
interpreter will fail and complain about unnecessary indentation. In this
case, all lines need the initial space removed.

[![](/images/7/79/Macro_Install_HowTo_12.png)](/index.php?title=File:Macro_Install_HowTo_12.png&filetimestamp=20141226225544&)

Python code with additional space on each line

#### Example 3

Here the code has been copied from a forum thread by using the Select all
button. Apparently the selection is good.

[![](/images/e/eb/Macro_Install_HowTo_14.png)](/index.php?title=File:Macro_Install_HowTo_14.png&filetimestamp=20141227174746&)

Python code copied from a forum

However, when the selection is pasted into the macro editor, undesirable
indentation seems to appear.

[![](/images/d/d3/Macro_Install_HowTo_15.png)](/index.php?title=File:Macro_Install_HowTo_15.png&filetimestamp=20141227174909&)

Python code copied from a forum into the macro editor; unnecessary indentation
is added

In this case, the initial spaces need to be removed. This can be done with a
specialized text editor to quickly decrease the indentation of the lines.

In Windows, [Notepad++](http://notepad-plus-plus.org/) can perform selection
with Alt \+ Mouse dragging, and then use **Edit → Indent → Decrease the
indentation**.

[![](/images/c/c3/Macro_Install_HowTo_16.png)](/index.php?title=File:Macro_Install_HowTo_16.png&filetimestamp=20141227174942&)

Python code with the correct indentation

#### Example 4

Here the selection also selects the line numbers in the code example. If this
selection is pasted into the macro editor, it won't work. All line numbers
need to be removed, and the spaces adjusted so that the Python code has the
proper indentation.

[![](/images/8/8b/Macro_Install_HowTo_29.png)](/index.php?title=File:Macro_Install_HowTo_29.png&filetimestamp=20141228213928&)

Selection that also selects the line numbers; if this code is pasted into the
macro editor, it won't work

#### Good code

[![](/images/7/7e/Macro_Install_HowTo_13.png)](/index.php?title=File:Macro_Install_HowTo_13.png&filetimestamp=20141226225701&)

Python code with the correct indentation

Expand

### No text output from macros

Macros may output information to the report view to detail what the code is
doing when it is running.

If no information is displayed, make sure the report view and [Python](/Python
"Python") console are visible, and that the output is directed tot he report
view.

#### Printing information

FreeCAD macros have two methods to print information to the report view.

The FreeCAD functions

    
    
    FreeCAD.Console.PrintMessage("Hello World! \n")
    FreeCAD.Console.PrintError("Hello World! \n")
    FreeCAD.Console.PrintWarning("Hello World! \n")
    

The simple Python function

    
    
    print("Hello World!")
    

#### Enabling the report view

To see the information displayed in the console you should:

1\. Go to the menu **View → Panels**.

[![](/images/0/0d/Macro_Install_HowTo_31.png)](/index.php?title=File:Macro_Install_HowTo_31.png&filetimestamp=20150117184246&)
[![](/images/7/7f/Macro_Install_HowTo_32.png)](/index.php?title=File:Macro_Install_HowTo_32.png&filetimestamp=20150117184350&)

Making the panels visible in the menu View → Panels

2\. Enable the `Report view` and the `Python console`.

[![](/images/e/e9/Macro_Install_HowTo_33.png)](/index.php?title=File:Macro_Install_HowTo_33.png&filetimestamp=20150117184421&)

Enabling the report view and the Python console

3\. The panels are now visible, and commands like
`FreeCAD.Console.PrintMessage()` now print information that appears in the
`Report view`.

[![](/images/b/b2/Macro_Install_HowTo_34.png)](/index.php?title=File:Macro_Install_HowTo_34.png&filetimestamp=20150117184454&)

FreeCAD main window with the Report view and the Python console

#### Enabling the `print()` command

FreeCAD may need to be configured so the `print()` function of
[Python](/Python "Python") redirects its output correctly to the report view.

1\. Go into the [Preferences Editor](/Preferences_Editor "Preferences Editor")
with the menu **Edit → Preferences**.

[![](/images/9/92/Macro_Install_HowTo_35.png)](/index.php?title=File:Macro_Install_HowTo_35.png&filetimestamp=20150117184526&)

Going into the preferences editor

2\. Go to **Python** section, and then **Output window → Python interpreter**.

[![](/images/f/f7/Macro_Install_HowTo_36.png)](/index.php?title=File:Macro_Install_HowTo_36.png&filetimestamp=20150117184558&)

Output window preferences

3\. Check both boxes:

  * [![](/images/thumb/8/82/Case_a_cocher_O.png/16px-Case_a_cocher_O.png)](/index.php?title=File:Case_a_cocher_O.png&filetimestamp=20121227153120&) Redirect internal Python output to report view

  * [![](/images/thumb/8/82/Case_a_cocher_O.png/16px-Case_a_cocher_O.png)](/index.php?title=File:Case_a_cocher_O.png&filetimestamp=20121227153120&) Redirect internal Python errors to report view

and then press the OK button.

[![](/images/f/f7/Macro_Install_HowTo_37.png)](/index.php?title=File:Macro_Install_HowTo_37.png&filetimestamp=20150117192904&)

Redirecting the Python output to the report view

[![](/images/c/cb/Macro_Install_HowTo_38.png)](/index.php?title=File:Macro_Install_HowTo_38.png&filetimestamp=20150117184628&)

Python commands printing information to the report view

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
  * **Macros:** [Macros](/Macros "Macros"), How to install macros
  * **Embedding:** [Embedding FreeCAD](/Embedding_FreeCAD "Embedding FreeCAD"), [Embedding FreeCADGui](/Embedding_FreeCADGui "Embedding FreeCADGui")

* * *

  * **Other:** [Expressions](/Expressions "Expressions"), [Code snippets](/Code_snippets "Code snippets"), [Line drawing function](/Line_drawing_function "Line drawing function"), [FreeCAD vector math library](/FreeCAD_vector_math_library "FreeCAD vector math library") (deprecated)

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

