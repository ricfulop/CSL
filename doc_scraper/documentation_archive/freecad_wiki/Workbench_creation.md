---
url: https://wiki.freecad.org/Workbench_creation
title: Workbench creation
scraped_at: 2025-09-08 16:41:54
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction
  * 2 The workbench structure Toggle The workbench structure subsection
    * 2.1 C++ workbench structure
    * 2.2 The Init.py file
    * 2.3 Python workbenches
      * 2.3.1 Preferences
      * 2.3.2 Distribution
    * 2.4 C++ workbenches
      * 2.4.1 Preferences
      * 2.4.2 Distribution
  * 3 FreeCAD commands Toggle FreeCAD commands subsection
    * 3.1 Python command definition
    * 3.2 C++ command definition
  * 4 "Compiling" your resource file
  * 5 Related

# Workbench creation

  * [Page](/Workbench_creation "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Workbench_creation&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Workbench_creation)
  * [Edit](/index.php?title=Workbench_creation&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Workbench_creation&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Workbench_creation.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Workbench_creation&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Workbench_creation)
  * [Edit](/index.php?title=Workbench_creation&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Workbench_creation&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Workbench_creation&action=history)

General

  * [What links here](/Special:WhatLinksHere/Workbench_creation "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Workbench_creation "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Workbench_creation&oldid=1601638 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Workbench_creation&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Workbench_creation&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Workbench+creation&action=page&filter=&language=en)This is the approved
revision of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Workbench+creation&language=&task=view "Start translation for this language")
  * [Deutsch](/Workbench_creation/de "Erstellung von Arbeitsbereichen \(100% translated\)")
  * English
  * [español](/Workbench_creation/es "Workbench creation/es \(2% translated\)")
  * [français](/Workbench_creation/fr "Création d'atelier \(100% translated\)")
  * [italiano](/Workbench_creation/it "Creare un Ambiente di lavoro \(100% translated\)")
  * [polski](/Workbench_creation/pl "Tworzenie środowiska pracy \(100% translated\)")
  * [português do Brasil](/Workbench_creation/pt-br "Criação de bancadas de trabalho \(27% translated\)")
  * [română](/Workbench_creation/ro "Workbench creation/ro \(2% translated\)")
  * [русский](/Workbench_creation/ru "Разработка верстака \(100% translated\)")
  * [中文（中国大陆）](/Workbench_creation/zh-cn "工作台的创建 \(100% translated\)")
  * [中文（繁體）](/Workbench_creation/zh-hant "Workbench creation/zh-hant \(0% translated\)")
  * [中文（臺灣）](/Workbench_creation/zh-tw "建立Workbench \(10% translated\)")
  * [日本語](/Workbench_creation/ja "ワークベンチの追加 \(2% translated\)")
  * [한국어](/Workbench_creation/ko "작업대 만들기 \(12% translated\)")

![](/images/6/6f/Arrow-left.svg) [Localisation](/Localisation "Localisation")

[Extra Python modules](/Extra_python_modules "Extra python modules")
![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

## Introduction

This page will show you how to add a new workbench to the FreeCAD interface.
[Workbenches](/Workbenches "Workbenches") are containers for FreeCAD commands.
They can be coded in Python, in C++, or in a mix of both, which has the
advantage to ally the speed of C++ to the flexibility of Python. In all cases,
though, your workbench will be launched by a set of two Python files. They can
be "internal" workbenches, included with FreeCAD's distribution, or "external"
workbenches, distributed via the [Addon Manager](/Std_AddonMgr "Std AddonMgr")
or installed manually by downloading from some online repository. Internal
workbenches may be coded in either C++, Python, or a combination of the two,
whereas external workbenches must be Python-only.

## The workbench structure

You need a folder, with any name you like, placed in the user Mod directory,
with an `Init.py` file, and, optionally an `InitGui.py` file. The `Init.py`
file is executed when FreeCAD starts, and the `InitGui.py` file is executed
immediately after, but only when FreeCAD starts in GUI mode. That's all it
needs for FreeCAD to find your workbench at startup and add it to its
interface.

The user Mod directory is a sub-directory of the user application data
directory (you can find the latter by typing `App.getUserAppDataDir()` in the
[Python console](/Python_console "Python console")):

  * On Linux it is usually /home/<username>/.local/share/FreeCAD/Mod/ (0.20 and above) or /home/<username>/.FreeCAD/Mod/ (0.19 and below).
  * On Windows it is %APPDATA%\FreeCAD\Mod\, which is usually C:\Users\<username>\Appdata\Roaming\FreeCAD\Mod\.
  * On macOS it is usually /Users/<username>/Library/Application Support/FreeCAD/Mod/.

The Mod directory should look like this:

    
    
    /Mod/
     +-- MyWorkbench/
         +-- Init.py
         +-- InitGui.py
    

Inside those files you can do whatever you want. Usually they are used like
this:

  * In the Init.py file you just add a couple of things used even when FreeCAD works in console mode, for example the file importers and exporters

  * In the InitGui.py file you usually define a workbench, which contains a name, an icon, and a series of FreeCAD commands (see below). That python file also defines functions that are executed when FreeCAD loads (you try to do as little as possible there, so you don't slow down the startup), another that gets executed when the workbench is activated (that's where you'll do most of the work), and a third one when the workbench is deactivated (so you can remove things if needed).

The structure and file content for a workbench described here is the classic
way of creating a new workbench. One can use a slight variation in the
structure of files when making a new Python workbench, that alternative way is
best described as a "namespaced workbench", opening up the possibility to use
pip to install the workbench. Both structures work, so it is more a question
of preference when creating a new workbench. The style and structure for
workbenches presented here are available in the global namespace of FreeCAD,
whereas for the alternative style and structure the workbench resides in a
dedicated namespace. For further readings on the topic see Related.

### C++ workbench structure

If you are going to code your workbench in python, you don't need to take
special care, and can simply place your other python files together with your
Init.py and InitGui.py files. When working with C++, however, you should take
greater care, and start with respecting one fundamental rule of FreeCAD: The
separation of your workbench between an App part (that can run in console
mode, without any GUI element), and a Gui part, which will only be loaded when
FreeCAD runs with its full GUI environment. So when developing a C++
workbench, you will actually most likely create two modules, an App and a Gui.
These two modules must of course be callable from python. Any FreeCAD module
(App or Gui) consists, at the very least, of a module init file. This is a
typical AppMyModuleGui.cpp file:

    
    
    extern "C" {
        void MyModuleGuiExport initMyModuleGui()  
        {
             if (!Gui::Application::Instance) {
                PyErr_SetString(PyExc_ImportError, "Cannot load Gui module in console application.");
                return;
            }
            try {
                // import other modules this one depends on
                Base::Interpreter().runString("import PartGui");
                // run some python code in the console
                Base::Interpreter().runString("print('welcome to my module!')");
            }
            catch(const Base::Exception& e) {
                PyErr_SetString(PyExc_ImportError, e.what());
                return;
            }
            (void) Py_InitModule("MyModuleGui", MyModuleGui_Import_methods);   /* mod name, table ptr */
            Base::Console().Log("Loading GUI of MyModule... done\n");
        
            // initializes the FreeCAD commands (in another cpp file)
            CreateMyModuleCommands();
        
            // initializes workbench and object definitions
            MyModuleGui::Workbench::init();
            MyModuleGui::ViewProviderSomeCustomObject::init();
        
             // add resources and reloads the translators
            loadMyModuleResource();
        }
    }
    

### The Init.py file

    
    
    """FreeCAD init script of XXX module"""
    
    # ***************************************************************************
    # *   Copyright (c) 2015 John Doe john@doe.com                              *   
    # *                                                                         *
    # *   This file is part of the FreeCAD CAx development system.              *
    # *                                                                         *
    # *   This program is free software; you can redistribute it and/or modify  *
    # *   it under the terms of the GNU Lesser General Public License (LGPL)    *
    # *   as published by the Free Software Foundation; either version 2 of     *
    # *   the License, or (at your option) any later version.                   *
    # *   for detail see the LICENSE text file.                                 *
    # *                                                                         *
    # *   FreeCAD is distributed in the hope that it will be useful,            *
    # *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
    # *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
    # *   GNU Lesser General Public License for more details.                   *
    # *                                                                         *
    # *   You should have received a copy of the GNU Library General Public     *
    # *   License along with FreeCAD; if not, write to the Free Software        *
    # *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
    # *   USA                                                                   *
    # *                                                                         *
    # ***************************************************************************/
    
    FreeCAD.addImportType("My own format (*.own)", "importOwn")
    FreeCAD.addExportType("My own format (*.own)", "exportOwn")
    print("I am executing some stuff here when FreeCAD starts!")
    

You can choose any license you like for your workbench, but be aware that if
you wish to see your workbench integrated into and distributed with the
FreeCAD source code at some point, it needs to be LGPL2+ like the example
above. See [License](/License "License").

The `FreeCAD.addImportType()` and `addEXportType()` functions allow you to
give the name and extension of a file type, and a Python module responsible
for its import. In the example above, an `importOwn.py` module will handle
`.own` files. See [Code snippets](/Code_snippets "Code snippets") for more
examples.

### Python workbenches

This is the InitGui.py file:

    
    
    class MyWorkbench (Workbench):
    
        MenuText = "My Workbench"
        ToolTip = "A description of my workbench"
        Icon = """paste here the contents of a 16x16 xpm icon"""
    
        def Initialize(self):
            """This function is executed when the workbench is first activated.
            It is executed once in a FreeCAD session followed by the Activated function.
            """
            import MyModuleA, MyModuleB # import here all the needed files that create your FreeCAD commands
            self.list = ["MyCommand1", "MyCommand2"] # a list of command names created in the line above
            self.appendToolbar("My Commands", self.list) # creates a new toolbar with your commands
            self.appendMenu("My New Menu", self.list) # creates a new menu
            self.appendMenu(["An existing Menu", "My submenu"], self.list) # appends a submenu to an existing menu
    
        def Activated(self):
            """This function is executed whenever the workbench is activated"""
            return
    
        def Deactivated(self):
            """This function is executed whenever the workbench is deactivated"""
            return
    
        def ContextMenu(self, recipient):
            """This function is executed whenever the user right-clicks on screen"""
            # "recipient" will be either "view" or "tree"
            self.appendContextMenu("My commands", self.list) # add commands to the context menu
    
        def GetClassName(self): 
            # This function is mandatory if this is a full Python workbench
            # This is not a template, the returned string should be exactly "Gui::PythonWorkbench"
            return "Gui::PythonWorkbench"
           
    Gui.addWorkbench(MyWorkbench())
    

Other than that, you can do anything you want: you could put your whole
workbench code inside the InitGui.py if you want, but it is usually more
convenient to place the different functions of your workbench in separate
files. So those files are smaller and easier to read. Then you import those
files into your InitGui.py file. You can organize those files the way you
want, a good example is one for each FreeCAD command you add.

#### Preferences

You can add a Preferences page for your Python workbench. The Preferences
pages look for a preference icon with a specific name in the Qt Resource
system. If your icon isn't in the resource system or doesn't have the correct
name, your icon won't appear on the Preferences page.

Adding your workbench icon:

  * the preferences icon needs to be named "preferences-" + "modulename" + ".svg" (all lowercase)
  * make a qrc file containing all icon names
  * in the main *.py directory, run pyside-rcc -o myResources.py myqrc.qrc
  * in InitGui.py, add import myResource(.py)
  * update your repository(git) with myResources.py and myqrc.qrc

You'll need to redo the steps if you add/change icons.

@kbwbe has created a nice script to compile resources for the A2Plus
workbench. See below.

Adding your preference page(s):

  * You need to compile the Qt designer plugin that allows you to add preference settings with [Qt Designer](/Compile_on_Linux#Qt_designer_plugin "Compile on Linux")
  * Create a blank widget in Qt Designer (no buttons or anything)
  * Design your preference page, any setting that must be saved (preferences) must be one of the Gui::Pref* widgets that were added by the plugin)
  * In any of those, make sure you fill the PrefName (the name of your preference value) and PrefPath (ex: Mod/MyWorkbenchName), which will save your value under BaseApp/Preferences/Mod/MyWorkbenchName
  * Save the ui file in your workbench, make sure it's handled by cmake
  * In your workbench, for ex. inside the InitGui file, inside the Initialize method (but any other place works too), add: FreeCADGui.addPreferencePage("/path/to/myUiFile.ui","MyGroup"), "MyGroup" being one of the preferences groups on the left. FreeCAD will automatically look for a "preferences-mygroup.svg" file in its known locations (which you can extend with FreeCADGui.addIconPath())
  * Make sure the addPreferencePage() method is called only once, otherwise your pref page will be added several times

#### Distribution

To distribute your Python workbench, you may either simply host the files in
some location and instruct your users to download them and place them in their
Mod directory manually, or you may host them in an online git repository
(GitHub, GitLab, Framagit, and Debian Salsa are currently supported locations)
and configure them for the [Addon Manager](/Std_AddonMgr "Std AddonMgr") to
install. Instructions for inclusion on FreeCAD's official Addons list can be
found on the [FreeCAD Addons GitHub
repository](https://github.com/FreeCAD/FreeCAD-addons/blob/master/README.md).
To use the Addon Manager, a [package.xml metadata file](/Package_Metadata
"Package Metadata") should be included, which instructs the Addon Manager how
to find your workbench's icon, and allows display of a description, version
number, etc. It can also be used to specify other workbenches or Python
packages that your Workbench either depends on, is blocked by, or is intended
to replace.

For a quick guide on how to create a basic package.xml file and add a
workbench to the [Addon Manager](/Std_AddonMgr "Std AddonMgr") see: [Add
Workbench to Addon Manager](/Add_Workbench_to_Addon_Manager "Add Workbench to
Addon Manager").

Optionally, you can include a separate metadata file describing your Python
dependencies. This may be either a file called metadata.txt describing your
workbench's external dependencies (on either other Addons, Workbenches, or
Python modules), or a
[requirements.txt](https://pip.pypa.io/en/latest/reference/requirements-file-
format/) describing your Python dependencies. Note that if using a
requirements.txt file, only the names of the specified packages are used for
dependency resolution: pip command options, include options and version
information are not supported by the Addon Manager. Users may manually run the
requirements file using pip if those features are required.

The format of the metadata.txt file is plain text, with three optional lines:

    
    
    workbenches=
    pylibs=
    optionalpylibs=
    

Each line should consist of a comma-separated list of items your Workbench
depends on. Workbenches may be either an internal FreeCAD Workbench, e.g.
"FEM", or an external Addon, for example "Curves". The required and optional
Python libraries should be specified with their canonical Python names, such
as you would use with `pip install`. For example:

    
    
    workbenches=FEM,Curves
    pylibs=ezdxf
    optionalpylibs=metadata,git
    

You may also include a script that is run when your package is uninstalled.
This is a file called "uninstall.py" located at the top level of your Addon.
It is executed when a user uninstalls your Addon using the Addon Manager. Use
it to clean up anything your Addon may have done to the users system that
should not persist when the Addon is gone (e.g. removing cache files, etc.).

To ensure that your addon is being read correctly by the Addon Manager, you
can enable a "developer mode" in which the Addon Manager examines all
available addons and ensures their metadata contains the required elements. To
enable this mode select: **Edit → Preferences... → Addon Manager → Addon
manager options → Addon developer mode** , see [Preferences
Editor](/Preferences_Editor#Addon_manager_options "Preferences Editor").

### C++ workbenches

If you are going to code your workbench in C++, you will probably want to code
the workbench definition itself in C++ too (although it is not necessary: you
could also code only the tools in C++, and leave the workbench definition in
Python). In that case, the InitGui.py file becomes very simple: It might
contain just one line:

    
    
    import MyModuleGui
    

where MyModule is your complete C++ workbench, including the commands and
workbench definition.

Coding C++ workbenches works in a pretty similar way. This is a typical
Workbench.cpp file to include in the Gui part of your module:

    
    
    namespace MyModuleGui {
        class MyModuleGuiExport Workbench : public Gui::StdWorkbench
        {
            TYPESYSTEM_HEADER();
    
        public:
            Workbench();
            virtual ~Workbench();
    
            virtual void activated();
            virtual void deactivated();
    
        protected:
            Gui::ToolBarItem* setupToolBars() const;
            Gui::MenuItem*    setupMenuBar() const;
        };
    }
    

#### Preferences

You can add a Preferences page for C++ workbenches too. The steps are similar
to those for Python.

#### Distribution

There are two options to distribute a C++ workbench, you can either host
precompiled versions for the different operating systems yourself, or you can
request for your code to be merged into the FreeCAD source code. As mentioned
above this requires a LGPL2+ license, and you must first present your
workbench to the community in the [FreeCAD forum](https://forum.freecad.org)
for review.

## FreeCAD commands

FreeCAD commands are the basic building block of the FreeCAD interface. They
can appear as a button on toolbars, and as a menu entry in menus. But it is
the same command. A command is a simple Python class, that must contain a
couple of predefined attributes and functions, that define the name of the
command, its icon, and what to do when the command is activated.

### Python command definition

    
    
    class My_Command_Class():
        """My new command"""
    
        def GetResources(self):
            return {"Pixmap"  : "My_Command_Icon", # the name of a svg file available in the resources
                    "Accel"   : "Shift+S", # a default shortcut (optional)
                    "MenuText": "My New Command",
                    "ToolTip" : "What my new command does"}
    
        def Activated(self):
            """Do something here"""
            return
    
        def IsActive(self):
            """Here you can define if the command must be active or not (greyed) if certain conditions
            are met or not. This function is optional."""
            return True
    
    FreeCADGui.addCommand("My_Command", My_Command_Class())
    

### C++ command definition

Similarly, you can code your commands in C++, typically in a Commands.cpp file
in your Gui module. This is a typical Commands.cpp file:

    
    
    DEF_STD_CMD_A(CmdMyCommand);
    
    CmdMyCommand::CmdMyCommand()
      :Command("My_Command")
    {
      sAppModule    = "MyModule";
      sGroup        = QT_TR_NOOP("MyModule");
      sMenuText     = QT_TR_NOOP("Runs my command...");
      sToolTipText  = QT_TR_NOOP("Describes what my command does");
      sWhatsThis    = QT_TR_NOOP("Describes what my command does");
      sStatusTip    = QT_TR_NOOP("Describes what my command does");
      sPixmap       = "some_svg_icon_from_my_resource";
    }
    
    void CmdMyCommand::activated(int iMsg)
    {
        openCommand("My Command");
        doCommand(Doc,"print('Hello, world!')");
        commitCommand();
        updateActive();
    }
    
    bool CmdMyCommand::isActive(void)
    {
      if( getActiveGuiDocument() )
        return true;
      else
        return false;
    }
    
    void CreateMyModuleCommands(void)
    {
        Gui::CommandManager &rcCmdMgr = Gui::Application::Instance->commandManager();
        rcCmdMgr.addCommand(new CmdMyCommand());
    }
    

## "Compiling" your resource file

compileA2pResources.py from the A2Plus workbench:

    
    
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    #***************************************************************************
    #*                                                                         *
    #*   Copyright (c) 2019 kbwbe                                              *
    #*                                                                         *
    #*   Portions of code based on hamish's assembly 2                         *
    #*                                                                         *
    #*   This program is free software; you can redistribute it and/or modify  *
    #*   it under the terms of the GNU Lesser General Public License (LGPL)    *
    #*   as published by the Free Software Foundation; either version 2 of     *
    #*   the License, or (at your option) any later version.                   *
    #*   for detail see the LICENSE text file.                                 *
    #*                                                                         *
    #*   This program is distributed in the hope that it will be useful,       *
    #*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
    #*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
    #*   GNU Library General Public License for more details.                  *
    #*                                                                         *
    #*   You should have received a copy of the GNU Library General Public     *
    #*   License along with this program; if not, write to the Free Software   *
    #*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
    #*   USA                                                                   *
    #*                                                                         *
    #***************************************************************************
    
    # This script compiles the A2plus icons for py2 and py3
    # For Linux only
    # Start this file in A2plus main directory
    # Make sure pyside-rcc is installed
    
    import os, glob
    
    qrc_filename = 'temp.qrc'
    if os.path.exists(qrc_filename):
        os.remove(qrc_filename)
    
    qrc = '''<RCC>
    \t<qresource prefix="/">'''
    for fn in glob.glob('./icons/*.svg'):
        qrc = qrc + '\n\t\t<file>%s</file>' % fn
    qrc = qrc + '''\n\t</qresource>
    </RCC>'''
    
    print(qrc)
    
    f = open(qrc_filename,'w')
    f.write(qrc)
    f.close()
    
    os.system(
        'pyside-rcc -o a2p_Resources2.py {}'.format(qrc_filename))
    os.system(
        'pyside-rcc -py3 -o a2p_Resources3.py {}'.format(qrc_filename))
    
    os.remove(qrc_filename)
    

## Related

  * [Translating an external workbench](/Translating_an_external_workbench "Translating an external workbench")
  * [Forum discussion: Namespaced Workbenches](https://forum.freecad.org/viewtopic.php?t=47460)
  * [freecad.workbench_starterkit](https://github.com/FreeCAD/freecad.workbench_starterkit)

  

![](/images/6/6f/Arrow-left.svg) [Localisation](/Localisation "Localisation")

[Extra Python modules](/Extra_python_modules "Extra python modules")
![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

Expand[![](/images/thumb/8/8f/Power_user_hub.png/24px-
Power_user_hub.png)](/index.php?title=File:Power_user_hub.png&filetimestamp=20200511213015&)
[Power user documentation](/Power_users_hub "Power users hub")

  * **FreeCAD scripting:** [Python](/Python "Python"), [Introduction to Python](/Introduction_to_Python "Introduction to Python"), [Python scripting tutorial](/Python_scripting_tutorial "Python scripting tutorial"), [FreeCAD Scripting Basics](/FreeCAD_Scripting_Basics "FreeCAD Scripting Basics")

* * *

  * **Modules:** [Builtin modules](/Builtin_modules "Builtin modules"), [Units](/Units "Units"), [Quantity](/Quantity "Quantity")
  * **Workbenches:** Workbench creation, [Gui Commands](/Gui_Command "Gui Command"), [Commands](/Command "Command"), [Installing more workbenches](/Installing_more_workbenches "Installing more workbenches")
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

