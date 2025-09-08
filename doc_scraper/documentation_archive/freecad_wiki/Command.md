---
url: https://wiki.freecad.org/Command
title: Command
scraped_at: 2025-09-08 16:46:38
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction
  * 2 Background
  * 3 Commands defined in C++
  * 4 Commands defined in Python
  * 5 Examples

# Command

  * [Page](/Command "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Command&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Command)
  * [Edit](/index.php?title=Command&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Command&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Command.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Command&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Command)
  * [Edit](/index.php?title=Command&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Command&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Command&action=history)

General

  * [What links here](/Special:WhatLinksHere/Command "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Command "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Command&oldid=1130156 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Command&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Command&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Command&action=page&filter=&language=en)This is the approved revision of this
page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Command&language=&task=view "Start translation for this language")
  * [Deutsch](/Command/de "Befehl \(100% translated\)")
  * English
  * [Türkçe](/Command/tr "Komutlar \(14% translated\)")
  * [español](/Command/es "Command \(7% translated\)")
  * [français](/Command/fr "Les commandes \(100% translated\)")
  * [italiano](/Command/it "Comando \(100% translated\)")
  * [polski](/Command/pl "Polecenia \(100% translated\)")
  * [português do Brasil](/Command/pt-br "Comandos \(14% translated\)")
  * [română](/Command/ro "Comanda \(14% translated\)")
  * [русский](/Command/ru "Команда \(93% translated\)")
  * [中文（中国大陆）](/Command/zh-cn "命令 \(14% translated\)")

## Introduction

A command is what is being executed when you press a toolbar button or type a
keyboard shortcut. It can be a very simple action, like changing the zoom
level of the [3D view](/3D_view "3D view") or rotating the point of view, or a
complex system that will open dialog boxes and wait for the user to perform
specific tasks.

Each FreeCAD command has a unique name, that appears in the [:Category:Command
Reference](/Category:Command_Reference "Category:Command Reference") page.
Commands can be launched by a toolbar button, a menu item, or from a
[python](/Python "Python") script or the [Python console](/Python_console
"Python console"), by running:

    
    
    FreeCADGui.runCommand("my_Command_Name")
    

## Background

FreeCAD commands are defined per workbench. Workbenches will normally add
their command definitions at FreeCAD init time, so the command exists and is
available as soon as FreeCAD is started, no matter if the corresponding
workbench has been activated yet or not. In some cases however, the workbench
author might have decided to not overload/burden the FreeCAD startup process
and therefore loaded the command definitions only at workbench init. In those
cases, the command will only be available after the workbench has been
activated (you have switched to it at least once with the workbench selector).

As most of them require user interaction, FreeCAD commands are only available
in GUI-mode, and not in console mode. However, for convenience, most FreeCAD
commands will either have a corresponding python function (like `Part.makeBox`
or `Draft.makeLine`), or will execute code that is very easy to replicate in a
python script and/or [macro](/Macros "Macros").

Commands can be defined either in C++ or in Python.

## Commands defined in C++

Example of a C++ command definition, usually defined following the structure
Mod/ModuleName/Gui/Command.cpp.

    
    
    DEF_STD_CMD_A(StdCmdMyCommand);
    
    StdCmdMyCommand::StdCmdMyCommand()
      : Command("Std_My_Command")
    {
        sGroup        = QT_TR_NOOP("File");
        sMenuText     = QT_TR_NOOP("My Command");
        sToolTipText  = QT_TR_NOOP("Runs my command in the active document");
        sWhatsThis    = "Std_MyCommand";
        sStatusTip    = QT_TR_NOOP("Runs my command in the active document");
        sPixmap       = "MyCommand.svg";
        sAccel        = "Ctrl+A";
    }
    
    void StdCmdExport::activated(int iMsg)
    {
        // place here the code to be executed when the command is ran
    }
    
    bool StdCmdMyCommand::isActive(void)
    {
        // here you have a chance to return true or false depending if your command must be shown as active or inactive (greyed).
    }
    
    // the command must be "registered" in FreeCAD's command system
    CommandManager &rcCmdMgr = Application::Instance->commandManager();
    rcCmdMgr.addCommand(new StdCmdMyCommand());
    

## Commands defined in Python

Example of a Python command definition, it can be placed in a directory like
Mod/ModuleName/tools/commands.py.

    
    
    from PySide.QtCore import QT_TRANSLATE_NOOP
    
    
    class MyCommand:
        """Explanation of the command."""
    
        def __init__(self):
            """Initialize variables for the command that must exist at all times."""
            pass
    
        def GetResources(self):
            """Return a dictionary with data that will be used by the button or menu item."""
            return {'Pixmap': 'MyCommand.svg',
                    'Accel': "Ctrl+A",
                    'MenuText': QT_TRANSLATE_NOOP("My_Command", "My Command"),
                    'ToolTip': QT_TRANSLATE_NOOP("My_Command", "Runs my command in the active document")}
    
        def Activated(self):
            """Run the following code when the command is activated (button press)."""
            print("Activated")
    
        def IsActive(self):
            """Return True when the command should be active or False when it should be disabled (greyed)."""
            return True
    
    # The command must be "registered" with a unique name by calling its class.
    FreeCADGui.addCommand('My_Command', MyCommand())
    

## Examples

See [Line drawing function](/Line_drawing_function "Line drawing function").

Expand[![](/images/thumb/8/8f/Power_user_hub.png/24px-
Power_user_hub.png)](/index.php?title=File:Power_user_hub.png&filetimestamp=20200511213015&)
[Power user documentation](/Power_users_hub "Power users hub")

  * **FreeCAD scripting:** [Python](/Python "Python"), [Introduction to Python](/Introduction_to_Python "Introduction to Python"), [Python scripting tutorial](/Python_scripting_tutorial "Python scripting tutorial"), [FreeCAD Scripting Basics](/FreeCAD_Scripting_Basics "FreeCAD Scripting Basics")

* * *

  * **Modules:** [Builtin modules](/Builtin_modules "Builtin modules"), [Units](/Units "Units"), [Quantity](/Quantity "Quantity")
  * **Workbenches:** [Workbench creation](/Workbench_creation "Workbench creation"), [Gui Commands](/Gui_Command "Gui Command"), Commands, [Installing more workbenches](/Installing_more_workbenches "Installing more workbenches")
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

