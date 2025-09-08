---
url: https://wiki.freecad.org/Debugging#Python_Debugging
title: Debugging
scraped_at: 2025-09-08 16:43:00
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Test First
  * 2 Command Line
  * 3 Generating a Backtrace Toggle Generating a Backtrace subsection
    * 3.1 For Linux
    * 3.2 For macOS
  * 4 List Libraries Loaded by FreeCAD
  * 5 Python Debugging Toggle Python Debugging subsection
    * 5.1 winpdb
    * 5.2 Visual Studio Code (VS Code)
    * 5.3 With LiClipse and AppImage
    * 5.4 Pyzo
  * 6 Debugging OpenCasCade

# Debugging

  * [Page](/Debugging "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Debugging&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Debugging)
  * [Edit](/index.php?title=Debugging&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Debugging&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Debugging.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Debugging&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Debugging)
  * [Edit](/index.php?title=Debugging&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Debugging&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Debugging&action=history)

General

  * [What links here](/Special:WhatLinksHere/Debugging "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Debugging "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Debugging&oldid=1601389#Python_Debugging "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Debugging&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Debugging&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Debugging&action=page&filter=&language=en)This is the approved revision of
this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Debugging&language=&task=view "Start translation for this language")
  * [Deutsch](/Debugging/de "Fehlerdiagnose \(95% translated\)")
  * English
  * [Türkçe](/Debugging/tr "Debugging \(1% translated\)")
  * [español](/Debugging/es "Debugging \(29% translated\)")
  * [français](/Debugging/fr "Débogage \(100% translated\)")
  * [hrvatski](/Debugging/hr "Debugging \(3% translated\)")
  * [italiano](/Debugging/it "Debugging - Individuare gli errori \(100% translated\)")
  * [polski](/Debugging/pl "Debugowanie \(100% translated\)")
  * [português](/Debugging/pt "Debugging/pt \(0% translated\)")
  * [português do Brasil](/Debugging/pt-br "Depuração \(1% translated\)")
  * [română](/Debugging/ro "Depanare \(21% translated\)")
  * [svenska](/Debugging/sv "Debugging \(1% translated\)")
  * [čeština](/Debugging/cs "Debugging/cs \(0% translated\)")
  * [български](/Debugging/bg "Debugging \(1% translated\)")
  * [русский](/Debugging/ru "Отладка \(14% translated\)")
  * [中文](/Debugging/zh "Debugging/zh \(0% translated\)")
  * [中文（中国大陆）](/Debugging/zh-cn "调试 \(21% translated\)")
  * [中文（臺灣）](/Debugging/zh-tw "Debugging/zh-tw \(1% translated\)")
  * [日本語](/Debugging/ja "FreeCADのデバッグ \(1% translated\)")

![](/images/6/6f/Arrow-left.svg) [Tracker](/Tracker "Tracker")

[Testing](/Testing "Testing") ![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

## Test First

Before you go through the pain of debugging use the [Test framework](/Testing
"Testing") to check if the standard tests work properly. If they do not run
complete there is possibly a broken installation.

## Command Line

The _debugging_ of FreeCAD is supported by a few internal mechanisms. The
command line version of FreeCAD provides some options for debugging support.

These are the currently recognized options in FreeCAD 0.19:

Generic options:

    
    
     -v [ --version ]          Prints version string
     -h [ --help ]             Prints help message
     -c [ --console ]          Starts in console mode
     --response-file arg       Can be specified with '@name', too
     --dump-config             Dumps configuration
     --get-config arg          Prints the value of the requested configuration key
    

Configuration:

    
    
     -l [ --write-log ]        Writes a log file to:
                               $HOME/.local/share/FreeCAD/FreeCAD.log (Linux)
                               $HOME/Library/Application\ Support/FreeCAD/FreeCAD.log (macOS)
                               %APPDATA%\FreeCAD\FreeCAD.log (Windows)
     --log-file arg            Unlike to --write-log this allows to log to an 
                               arbitrary file
     -u [ --user-cfg ] arg     User config file to load/save user settings
     -s [ --system-cfg ] arg   System config file to load/save system settings
     -t [ --run-test ] arg     Test case - or 0 for all
     -M [ --module-path ] arg  Additional module paths
     -P [ --python-path ] arg  Additional Python paths
     --single-instance         Allow to run a single instance of the application
    

## Generating a Backtrace

If you are running a version of FreeCAD from the bleeding edge of the
development curve, it may "crash". You can help solve such problems by
providing the developers with a "backtrace". To do this, you need to be
running a "debug build" of the software. "Debug build" is a parameter that is
set at compile time, so you'll either need to compile FreeCAD yourself, or
obtain a pre-compiled "debug" version.

### For Linux

Expand

Linux Debugging →

Prerequisites:

  * software package gdb installed
  * a debug build of FreeCAD (at this time only available by [building from source](/Compile_on_Linux#For_a_Debug_build "Compile on Linux"))
  * a FreeCAD model that causes a crash

Steps: Enter the following in your terminal window:

Find FreeCAD binary on your system:

    
    
    $ whereis freecad
    freecad: /usr/local/freecad <--- for example
    
    $ cd /usr/local/freecad/bin
    $ gdb FreeCAD
    

GNUdebugger will output some initializing information. The (gdb) shows
GNUDebugger is running in the terminal, now input:

    
    
    (gdb) handle SIG33 noprint nostop
    (gdb) run
    

FreeCAD will now start up. Perform the steps that cause FreeCAD to crash or
freeze, then enter in the terminal window:

    
    
    (gdb) bt
    

This will generate a lengthy listing of exactly what the program was doing
when it crashed or froze. Include this with your problem report.

    
    
    (gdb) bt full
    

Print the values of the local variables also. This can be combined with a
number to limit the number of frames shown.

### For macOS

Expand

macOS Debugging →

Prerequisites:

  * software package lldb installed
  * a debug build of FreeCAD
  * a FreeCAD model that causes a crash

Steps: Enter the following in your terminal window:

    
    
    $ cd FreeCAD/bin
    $ lldb FreeCAD
    

LLDB will output some initializing information. The (lldb) shows the debugger
is running in the terminal, now input:

    
    
    (lldb) run
    

FreeCAD will now start up. Perform the steps that cause FreeCAD to crash or
freeze, then enter in the terminal window:

    
    
    (lldb) bt
    

This will generate a lengthy listing of exactly what the program was doing
when it crashed or froze. Include this with your problem report.

## List Libraries Loaded by FreeCAD

(Applicable to Linux and macOS)

Sometimes it's helpful to understand what libraries FreeCAD is loading,
specifically if there are multiple libraries being loaded of the same name but
different versions (version collision). In order to see which libraries are
loaded by FreeCAD when it crashes you should open a terminal and run it in the
debugger. In a second terminal window, find out the process id of FreeCAD:

`ps -A | grep FreeCAD`

Use the returned id and pass it to `lsof`:

` lsof -p process_id`

This prints a long list of loaded resources. So for example, if trying to
ascertain if more than one Coin3d library versions is loaded, scroll through
the list or search directly for Coin in the output:

`lsof -p process_id | grep Coin`

## Python Debugging

For a more modern approach to debugging Python, see these posts:

  * [Debugging macros with VS 2017](https://forum.freecad.org/viewtopic.php?f=22&t=28901)
  * [Python workbenches debugging](https://forum.freecad.org/viewtopic.php?f=10&t=35383)
  * [python3.dll, Qt5Windgets.dll, Qt5Gui.dll and Qt5Core.dll not found](https://forum.freecad.org/viewtopic.php?f=4&t=40251)

### winpdb

Expand

winpdb Debugging →

Here is an example of using _Winpdb_ inside FreeCAD:

We need the Python debugger: _Winpdb_. If you do not have it installed, on
Ubuntu/Debian install it with:

    
    
    sudo apt-get install winpdb
    

Now lets setup the debugger.

  1. Start _Winpdb_.
  2. Set the debugger password to "test": Go to menu _File_ → _Password" and set the password._

Now we will run a test Python script in FreeCAD step by step.

  1. Run winpdb and set the password (e.g. test)
  2. Create a Python file with this content

    
    
    import rpdb2
    rpdb2.start_embedded_debugger("test")
    import FreeCAD
    import Part
    import Draft
    print "hello"
    print "hello"
    import Draft
    points=[FreeCAD.Vector(-3.0,-1.0,0.0),FreeCAD.Vector(-2.0,0.0,0.0)]
    Draft.makeWire(points,closed=False,face=False,support=None)
    

  1. Start FreeCAD and load the above file into FreeCAD
  2. Press F6 to execute it
  3. Now FreeCAD will become unresponsive because the Python debugger is waiting
  4. Switch to the Windpdb GUI and click on "Attach". After a few seconds an item "<Input>" appears where you have to double-click
  5. Now the currently executed script appears in Winpdb.
  6. Set a break at the last line and press F5
  7. Now press F7 to step into the Python code of Draft.makeWire

### Visual Studio Code (VS Code)

Expand

VS Code Debugging →

Prerequisites:

  * The ptvsd package needs to be installed in a Python 3 outside of FreeCAD, then the module must be copied to FreeCAD's Python library folder.

    
    
    # In a cmd window that has a path to you local Python 3:
    pip install ptvsd
    # Then if your Python is installed in C:\Users\<userid>\AppData\Local\Programs\Python\Python37
    # and your FreeCAD is installed in C:\freecad\bin
    xcopy "C:\Users\<userid>\AppData\Local\Programs\Python\Python37\Lib\site-packages\ptvsd" "C:\freecad\bin\Lib\site-packages\ptvsd"
    

[pypi page](https://pypi.org/project/ptvsd/)

[Visual Studio Code documentation for remote
debugging](https://code.visualstudio.com/docs/python/debugging#_remote-
debugging)

Steps:

  * Add following code at the beginning of your script

    
    
    import ptvsd
    print("Waiting for debugger attach")
    # 5678 is the default attach port in the VS Code debug configurations
    ptvsd.enable_attach(address=('localhost', 5678), redirect_output=True)
    ptvsd.wait_for_attach()
    

  * Add a debug configuration in Visual Studio Code **Debug → Add Configurations…**.
  * The config should look like this:

    
    
        "configurations": [
            {
                "name": "Python: Attacher",
                "type": "python",
                "request": "attach",
                "port": 5678,
                "host": "localhost",
                "pathMappings": [
                    {
                        "localRoot": "${workspaceFolder}",
                        "remoteRoot": "."
                    }
                ]
            },
    

  * In VS Code add a breakpoint anywhere you want.
  * Launch the script in FreeCAD. FreeCAD freeze waiting for attachment.
  * In VS Code start debugging using created configuration. You should see variables in debugger area.
  * When setting breakpoints, VS Code will complain about not finding the .py file opened in the VS Code editor. 
    * Change "remoteRoot": "." to "remoteRoot": "<directory of file>" 
      * For example, if the Python file resides in _/home/FC_myscripts/myscript.py_
      * Change to: "remoteRoot": "/home/FC_myscripts"
    * If you're just debugging FreeCAD macros from the FreeCAD macro folder, and that folder is "C:/Users/<userid>/AppData/Roaming/FreeCAD/Macro", then use: 
      * "localRoot": "C:/Users/<userid>/AppData/Roaming/FreeCAD/Macro",
      * "remoteRoot": "C:/Users/<userid>/AppData/Roaming/FreeCAD/Macro"
  * If your macro can't find ptvsd despite having installed it somewhere precede 'import ptvsd' with

    
    
    from sys import path
    sys.path.append('/path/to/site-packages')
    

Where the path is to the directory where ptvsd was installed.

  * On the left bottom edge of VSCode you can choose the Python executable - it's best to make this the version packaged with FreeCAD.

In the Mac package it is
/Applications/FreeCAD.App/Contents/Resources/bin/python.

You can locate it on your system by typing

    
    
    import sys
    print(sys.executable)
    

into FreeCAD's Python console.

### With LiClipse and AppImage

Expand

LiClipse Debugging →

  * Extract AppImage.

    
    
    > ./your location/FreeCAD_xxx.AppImage --appimage-extract
    > cd squashfs-root/
    

  * The sqashfs-root location is where the debugger later on is hooked up to.

  * Make sure you can start a FreeCAD session from within the squashfs-root location.

    
    
    squashfs-root> ./usr/bin/freecadcmd
    

  * Should start up a FreeCAD commandline session.

  * Install [LiClipse](https://www.liclipse.com/). 
    * Comes ready with pydev and has installers for all platforms.
    * For linux it is just to extract (to any location) and run.

  * Configure liclipse for debugging. 
    * Right-click pydev icon (upper right corner) and choose customize. 
      * Activate "PyDev Debug" (through checkbox, or it might be needed to go to tab "Action Set Availability" and activate there first).
      * In the pydev menu you can now choose "start debug server".
    * Use menu window/open perspective/other > debug. 
      * Right-click debug icon (upper right corner) and choose customize.
      * Checking "Debug" brings the debugging navigation tools to the toolbar.
    * Open preferences through menu window/preferences. 
      * In PyDev/Interpreters add "new Interpreter by browsing".
      * The added interpreter should be: `your loc/squashfs-root/usr/bin/python`.
      * If you are only using this for fc, you can add AddOn workbench folders as well, or do that in a pydev-project later on.

  * Find path to `pydevd.py` in your liclipse installation. 
    * Something along the lines of: `your location/liclipse/plugins/org.python.pydev.xx/pysrc`.
  * Create a regular pydev-project in liclipse. 
    * Import external sources, for example a macro that you want to debug, or an external workbench.
    * In that macro (or workbench .py file) add the code lines:

    
    
    
    import sys; sys.path.append("path ending with /pysrc")
    import pydevd; pydevd.settrace()
    

    

  * This is where the execution will halt when the macro is run.

  * Start the liclipse debug server (menu pydev).

  * Start FreeCAD.

    
    
    squashfs-root> ./usr/bin/freecad
    

  * Run the macro (or any other file with a `pydevd.settrace()` trigger) from within freecad, as you would normally do.

  * Happy debugging.

  * The use of LiClipse for remote debugging, and the steps described here related to liclipse, should work on any platform. The parts related to AppImage is for linux only.

### Pyzo

See the [main article about Pyzo](/Pyzo "Pyzo").

## Debugging OpenCasCade

For developers needing to dig deeper in to the OpenCasCade kernel, user
@abdullah has created a
[thread](https://forum.freecad.org/viewtopic.php?f=10&t=47017) orientation
discussing how to do so.

  

![](/images/6/6f/Arrow-left.svg) [Tracker](/Tracker "Tracker")

[Testing](/Testing "Testing") ![](/images/a/af/Arrow-right.svg)

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

