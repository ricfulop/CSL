---
url: https://wiki.freecad.org/Start_up_and_Configuration
title: Start up and Configuration
scraped_at: 2025-09-08 16:44:51
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Overview
  * 2 Starting FreeCAD from the Command line Toggle Starting FreeCAD from the Command line subsection
    * 2.1 Using command line options without a command line shell
    * 2.2 Command line options
    * 2.3 Response and config files
    * 2.4 Hidden options
    * 2.5 Running FreeCAD without GUI (headless)
    * 2.6 Running modules, macros and scripts
  * 3 Environment variables Toggle Environment variables subsection
    * 3.1 HOME
    * 3.2 TMPDIR
    * 3.3 Libraries
  * 4 Configuration set Toggle Configuration set subsection
    * 4.1 User related information
    * 4.2 Command line arguments
    * 4.3 System related
    * 4.4 Build related information
    * 4.5 Branding related
    * 4.6 Querying the configuration
  * 5 Starting FreeCAD from the desktop Toggle Starting FreeCAD from the desktop subsection
    * 5.1 Linux: Creating an additional start option
  * 6 Starting FreeCAD from a portable USB medium

# Start up and Configuration

  * [Page](/Start_up_and_Configuration "View the content page \[ctrl-option-c\]")
  * [Discussion](/Talk:Start_up_and_Configuration "Discussion about the content page \[ctrl-option-t\]")

English

  * [Read](/Start_up_and_Configuration)
  * [Edit](/index.php?title=Start_up_and_Configuration&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Start_up_and_Configuration&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Start_up_and_Configuration.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Start_up_and_Configuration&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Start_up_and_Configuration)
  * [Edit](/index.php?title=Start_up_and_Configuration&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Start_up_and_Configuration&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Start_up_and_Configuration&action=history)

General

  * [What links here](/Special:WhatLinksHere/Start_up_and_Configuration "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Start_up_and_Configuration "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Start_up_and_Configuration&oldid=1624560 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Start_up_and_Configuration&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Start_up_and_Configuration&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Start+up+and+Configuration&action=page&filter=&language=en)This is the
approved revision of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Start+up+and+Configuration&language=&task=view "Start translation for this language")
  * [Deutsch](/Start_up_and_Configuration/de "Programmstart und Konfiguration \(100% translated\)")
  * English
  * [Türkçe](/Start_up_and_Configuration/tr "Start up and Configuration \(1% translated\)")
  * [español](/Start_up_and_Configuration/es "Puesta en marcha y Configuración \(23% translated\)")
  * [français](/Start_up_and_Configuration/fr "Démarrage et configuration \(100% translated\)")
  * [italiano](/Start_up_and_Configuration/it "Avvio e Configurazione \(93% translated\)")
  * [polski](/Start_up_and_Configuration/pl "Uruchomienie i konfiguracja \(100% translated\)")
  * [português do Brasil](/Start_up_and_Configuration/pt-br "Inicialização e configuração \(5% translated\)")
  * [română](/Start_up_and_Configuration/ro "Start up and Configuration \(20% translated\)")
  * [svenska](/Start_up_and_Configuration/sv "Start up and Configuration \(19% translated\)")
  * [čeština](/Start_up_and_Configuration/cs "Start up and Configuration \(1% translated\)")
  * [русский](/Start_up_and_Configuration/ru "Запуск и Конфигурирование \(34% translated\)")
  * [日本語](/Start_up_and_Configuration/ja "起動方法と設定 \(1% translated\)")
  * [한국어](/Start_up_and_Configuration/ko "시작 및 구성설정 \(18% translated\)")

![](/images/6/6f/Arrow-left.svg) [Import Export
Preferences](/Import_Export_Preferences "Import Export Preferences")

[Scripting and macros](/Scripting_and_macros "Scripting and macros")
![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

In FreeCAD version 0.20 the default location of the program's configuration,
data and cache files was changed for Linux.  
See [Release notes 0.20](/Release_notes_0.20#Core "Release notes 0.20") for
more information. This page has not yet been updated accordingly.

## Overview

This page shows the different ways to start FreeCAD and the most important
configuration features.

## Starting FreeCAD from the Command line

FreeCAD can be started normally by double-clicking on its desktop icon or
selecting it from the start menu, but it can also be started directly from the
command line. This allows you to change some of the default startup options.

### Using command line options without a command line shell

  * On Ubuntu you can create a desktop icon and edit its properties. Add the command line options separated by spaces behind the program name in the "Command" field.
  * On Windows create a shortcut and edit the properties. Add the command line options separated by spaces to "Target" field.

### Command line options

The command line options are subject to frequent changes.Therefore, it is a
good idea to check the current options by typing:

    
    
    FreeCAD --help
    

From the response you can read the possible parameters. For FreeCAD version
1.0 they are:

    
    
     Usage: FreeCAD [options] File1 File2 ...
     
     Allowed options:
     
     Generic options:
       -v [ --version ]          Prints version string
       --verbose                 Prints verbose version string
       -h [ --help ]             Prints help message
       -c [ --console ]          Starts in console mode
       --response-file arg       Can be specified with '@name', too
       --dump-config             Dumps configuration
       --get-config arg          Prints the value of the requested configuration key
       --set-config arg          Sets the value of a configuration key
       --keep-deprecated-paths   If set then config files are kept on the old 
                                 location
     
     Configuration:
       -l [ --write-log ]        Writes FreeCAD.log to the user directory.
       --log-file arg            Unlike --write-log this allows logging to an 
                                 arbitrary file
       -u [ --user-cfg ] arg     User config file to load/save user settings
       -s [ --system-cfg ] arg   System config file to load/save system settings
       -t [ --run-test ] arg     Run a given test case (use 0 (zero) to run all 
                                 tests). If no argument is provided then return list
                                 of all available tests.
       -r [ --run-open ] arg     Run a given test case (use 0 (zero) to run all 
                                 tests). If no argument is provided then return list
                                 of all available tests.  Keeps UI open after 
                                 test(s) complete.
       -M [ --module-path ] arg  Additional module paths
       -P [ --python-path ] arg  Additional python paths
       --single-instance         Allow to run a single instance of the application
       --safe-mode               Force enable safe mode
       --pass arg                Ignores the following arguments and pass them 
                                 through to be used by a script
    

In the following table, selected options are described in more detail:

Long option | Corresponding config var name | Synopsis   
---|---|---  
`--user-cfg <filename>` | UserParameter | Filename or relative path that ends with a filename. Defaults to `user.cfg`.   
`--module-path <dir>` | Prepends to AdditionalModulePaths | Directory that contains modules. This option can be given repeatedly to specify multiple directories.   
`--get-config <config-var-name>` | most | Outputs the requested value in a popup dialog. Exits upon confirmation with OK. Cannot be used repeatedly. If an unknown/illegal variable name is used, the response is empty. The `--console` flag is not honored.   
  
Options can written in two forms: `--long-option arg` and `--long-option=arg`.

### Response and config files

FreeCAD can read some of these options from a config file. This file must be
in the bin path and must be named FreeCAD.cfg. Be aware that options specified
in the command line override the config file!

Some operating systems have a very low limit of characters on the command
line. The common way to work around those limitations is using response files.
A response file is just a configuration file which uses the same syntax as the
command line. If the command line specifies a response file, it's loaded and
parsed in addition to the command line:

    
    
    FreeCAD @ResponseFile.txt 
    

or:

    
    
    FreeCAD --response-file=ResponseFile.txt
    

or:

    
    
    FreeCAD --response-file ResponseFile.txt
    

### Hidden options

There are a couple of options not visible to the user. These options are e.g.
the X-Window parameters parsed by the Windows system:

  * _-display_ \- Sets the X display (default is $DISPLAY).
  * _-geometry_ \- Sets the client geometry of the first window that is shown.
  * _-fn_ or _-font_ \- Defines the application font. The font should be specified using an X logical font description.
  * _-bg_ or _-background_ \- Sets the default background color and an application palette (light and dark shades are calculated).
  * _-fg_ or _-foreground_ \- Sets the default foreground color.
  * _-btn_ or _-button_ \- Sets the default button color.
  * _-name_ \- Sets the application name.
  * _-title_ \- Sets the application title.
  * _-visual_ \- Forces the application to use a TrueColor visual on an 8-bit display.
  * _-ncols_ \- Limits the number of colors allocated in the color cube on an 8-bit display, if the application is using the QApplication::ManyColor color specification. If count is 216 then a 6x6x6 color cube is used (i.e. 6 levels of red, 6 of green, and 6 of blue); for other values, a cube approximately proportional to a 2x3x1 cube is used.
  * _-cmap_ \- Causes the application to install a private color map on an 8-bit display.

### Running FreeCAD without GUI (headless)

FreeCAD is usually built with two executables: a GUI-capable one called
FreeCAD or freecad, and a headless one, called FreeCADCmd or freecadcmd.
FreeCAD can be used in console mode using the `--console` switch (which is the
default behavior of FreeCADCmd):

    
    
    FreeCAD --console
    

In console mode, no graphical user interface will be displayed, and you will
be presented with a Python interpreter prompt: `>>>`. From that prompt, you
have the same functionality as the Python interpreter that runs inside the
FreeCAD GUI, and access to all modules and plugins of FreeCAD, except the
FreeCADGui module. Be aware that modules that depend on FreeCADGui might also
be unavailable.

To read more about console or headless mode, refer to [Headless
FreeCAD](/Headless_FreeCAD "Headless FreeCAD").

### Running modules, macros and scripts

File type | System | Command line example   
---|---|---  
Module | Windows | `"C:\Program Files\FreeCAD\bin\FreeCAD.exe" -M "C:\FreeCAD\Mod\Draft"`  
| Linux | `FreeCAD_0.19 -M ~/.FreeCAD/Mod/Draft`  
| Linux (AppImage) | `path/to/FreeCADXXX.AppImage -M ~/.FreeCAD/Mod/Draft`  
.FCMacro or .py | Windows | `"C:\Program Files\FreeCAD\bin\FreeCAD.exe" "C:\Users\userName\AppData\Roaming\FreeCAD\Mod\WorkFeature\start_WF.FCMacro"`  
| Linux | `FreeCAD_0.19 ~/.FreeCAD/Mod/WorkFeature/start_WF.FCMacro`  
| Linux (AppImage) | `path/to/FreeCADXXX.AppImage ~/.FreeCAD/Mod/WorkFeature/start_WF.FCMacro`  
  
See [Macro at Startup](/Macro_at_Startup "Macro at Startup") on how to set up
a macro to automatically run at FreeCAD startup.

## Environment variables

FreeCAD supports the following environment variables, which can be used to
configure directories: [introduced in 0.19](/Release_notes_0.19 "Release notes
0.19")

Environment variable | Corresponding config var name | Synopsis   
---|---|---  
`FREECAD_USER_HOME` | UserHomePath | FreeCAD's "base" directory for keeping local user data.   
`FREECAD_USER_DATA` | UserAppData | If not set, defaults to `FREECAD_USER_HOME/.FreeCAD`, but only if `FREECAD_USER_HOME` is set.   
`FREECAD_USER_TEMP` | AppTempPath | If not set, defaults to `FREECAD_USER_HOME/temp`, but only if `FREECAD_USER_HOME` is set.   
  
If the specified path does not exist, the setting is ignored!

The above environment variables are meant to be used to realize a _portable_
FreeCAD environment. For an example how environment variables can be used from
the command line on Linux refer to the [notes for Linux users on the downloads
page](/Download#Notes_for_GNU.2FLinux_users "Download").

### `HOME`

FreeCAD uses [Qt](/Third_Party_Libraries#Qt "Third Party Libraries"), which
does honor the `HOME` environmental variable. Thus, setting `HOME` can be used
to specify the base directory of Qt-related configuration files
(`.config/FreeCAD/FreeCAD.conf`).

FreeCad itself does not honor the `HOME` environmental variable (because it
determines the user's home directory from a lower-level system API). Use
`FREECAD_USER_HOME` for this pupose.

### `TMPDIR`

The default temporary directory is /tmp/. The `TMPDIR` environmental variable
can be used to override the default. (_Editor: precedence?_).

### Libraries

Some libraries need to call system environment variables. Sometimes when there
is a problem with a FreeCAD installation, it is because some environment
variable is absent or incorrect. Therefore, some important variables get
duplicated in the Config and saved in the log file.

**Python**

  * PYTHONPATH
  * PYTHONHOME
  * TCL_LIBRARY
  * TCLLIBPATH

**OpenCascade**

  * CSF_MDTVFontDirectory
  * CSF_MDTVTexturesDirectory
  * CSF_UnitsDefinition
  * CSF_UnitsLexicon
  * CSF_StandardDefaults
  * CSF_PluginDefaults
  * CSF_LANGUAGE
  * CSF_SHMessage
  * CSF_XCAFDefaults
  * CSF_GraphicShr
  * CSF_IGESDefaults
  * CSF_STEPDefaults

## Configuration set

On every startup FreeCAD examines its surrounding and the command line
parameters. It builds up a **configuration set** which holds the essence of
the runtime information. This information is later used to determine the place
where to save user data or log files. It is also very important for debugging
analyses. Therefore it is saved in the log file.

To quickly find the location of the configuration files (e.g. to delete them
and therefore reset FreeCAD to "factory settings") on your machine, run the
following command in the [Python console](/Python_console "Python console") in
FreeCAD:

    
    
    App.getUserConfigDir()
    

### User related information

Config var name | Synopsis | Example Windows | Example Linux   
---|---|---|---  
UserAppData | Path where FreeCAD stores User Related application data. | C:\Users\username\AppData\Roaming\FreeCAD

* * *

 _Short path :_ %APPDATA%\FreeCAD | /home/username/.local/share/FreeCAD

* * *

 _Short path :_ ~/.local/share/FreeCAD  
UserParameter | File where FreeCAD stores User Related application data. | C:\Users\username\AppData\Roaming\FreeCAD\user.cfg

* * *

 _Short path :_ %APPDATA%\FreeCAD\user.cfg | /home/username/.config/FreeCAD/user.cfg

* * *

 _Short path :_ ~/.config/FreeCAD/user.cfg or $HOME/.config/FreeCAD/user.cfg  
SystemParameter | File where FreeCAD stores Application Related data. | C:\Users\username\AppData\Roaming\FreeCAD\system.cfg

* * *

 _Short path :_ %APPDATA%\FreeCAD\system.cfg | /home/username/.config/FreeCAD/system.cfg

* * *

 _Short path :_ ~/.config/FreeCAD/system.cfg or
$HOME/.config/FreeCAD/system.cfg  
UserHomePath | Home path of the current user | C:\Users\username

* * *

 _Short path :_ %USERPROFILE% | /home/username

* * *

 _Short path :_ ~  
  
Note: For Linux distributions, an additional configuration file that relates
to [Qt](/Third_Party_Tools#Qt-Toolkit "Third Party Tools") may exist at path
/home/username/.config/FreeCAD/FreeCAD.conf.

### Command line arguments

Config var name | Synopsis | Example   
---|---|---  
LoggingFile | 1 if the logging is switched on | 1   
LoggingFileName | File name where the log is placed | C:\Users\username\AppData\Roaming\FreeCAD\FreeCAD.log  
RunMode | This indicates how the main loop will work. **"Script"** means that the given script is called and then exit. **"Cmd"** runs the command line interpreter. **"Internal"** runs an internal script. **"Gui"** enters the Gui event loop. **"Module"** loads a given python module. | "Cmd"   
FileName | Meaning depends on the RunMode |   
ScriptFileName | Meaning depends on the RunMode |   
Verbose | Verbosity level of FreeCAD | "" or "strict"   
OpenFileCount | Holds the number of files opened through command line arguments | "12"   
AdditionalModulePaths | Holds the additional Module paths given in the cmd line | "extraModules/"   
  
### System related

Config var name | Synopsis | Example Windows | Example Linux   
---|---|---|---  
AppHomePath | Path where FreeCAD is installed | c:/Progam Files/FreeCAD_0.19 | /user/local/FreeCAD_0.19  
PythonSearchPath | Holds a list of paths which python search modules. This is at startup can change during execution |  |   
AppTempPath | Path of the temporary directory. Can be given with `TMPDIR` environment variable, or with the [![](/images/0/0e/Std_DlgParameter.svg)](/index.php?title=File:Std_DlgParameter.svg&filetimestamp=20240528121001&) [Parameter Editor](/Std_DlgParameter "Std DlgParameter"): **Tools → Edit parameters... → BaseApp → Preferences → General → TempPath** |  | /tmp/ (default)   
  
### Build related information

The table below shows the available information about the Build version. Most
of it comes from the Subversion repository. This stuff is needed to exactly
rebuild a version!

Config var name | Synopsis | Example   
---|---|---  
BuildVersionMajor | Major Version number of the Build. Defined in src/Build/Version.h.in | 0   
BuildVersionMinor | Minor Version number of the Build. Defined in src/Build/Version.h.in | 7   
BuildRevision | SVN Repository Revision number of the src in the Build. Generated by SVN | 356   
BuildRevisionRange | Range of different changes | 123-356   
BuildRepositoryURL | Repository URL | <https://free-cad.svn.sourceforge.net/svnroot/free-cad/trunk/src>  
BuildRevisionDate | Date of the above Revision | 2007/02/03 22:21:18   
BuildScrClean | Indicates if the source was changed after checkout | Src modified   
BuildScrMixed |  | Src not mixed   
  
### Branding related

These Config entries are related to the branding mechanism of FreeCAD. See
[Branding](/Branding "Branding") for more details.

Config var name | Synopsis | Example   
---|---|---  
ExeName | Name of the build Executable file. Can differ from FreeCAD if a different main.cpp is used. | FreeCAD.exe  
ExeVersion | Over all Version shows up at start time | "0.19"   
AppIcon | Icon which is used for the Executable, shows in Application MainWindow. | "FCIcon"   
ConsoleBanner | Banner which is prompted in console mode |   
SplashPicture | Name of the Icon used for the Splash Screen | "FreeCADSplasher"   
SplashAlignment | Alignment of the Text in the Splash dialog | "Bottom" or "Left"   
SplashTextColor | Color of the splasher Text | "#000000"   
StartWorkbench | Name of the Workbench which get started automatically after Startup | "Part Design"   
HiddenDockWindow | List of dockwindows (separated by a semicolon) which will be disabled | "Property editor"   
  
### Querying the configuration

**From FreeCAD's Python console**

Entries of the configuration set can be queried with the **config var name**
(see tables above) from the [Python console](/Python_console "Python
console"). For example:

    
    
     >>> FreeCAD.ConfigGet("ExeVersion")
     '0.19'
    

If the name is not found, an empty string is returned.

**From command line**

Use the `--get-config <config-var-name>` option to query a single name. Not
all names are supported. For example:

    
    
     FreeCAD --get-config ExeVersion
    

Use the `--dump-config` option to get a list of names and their values. Not
all names are supported.

**From FreeCAD console**

Start FreeCAD in console mode with `--console` and query with Python code. For
example:

    
    
     $ FreeCAD --console
     [FreeCAD Console mode <Use Ctrl-D (i.e. EOF) to exit.>]
     >>> FreeCAD.ConfigGet("ExeVersion")
     '0.19'
     >>> exit()
    

For Linux (bash shell) you can modify the following command line to suit your
needs:

    
    
     $ FreeCAD --console <<EOF
     print( "FREECAD_USER_HOME: " + ( "not set" if ( os.environ.get('FREECAD_USER_HOME') is None ) else os.environ.get('FREECAD_USER_HOME') ) )
     print( "UserHomePath: " + FreeCAD.ConfigGet("UserHomePath") )
     exit()
     EOF
    

## Starting FreeCAD from the desktop

### Linux: Creating an additional start option

The following assumes that your desktop is configured such that you can launch
FreeCAD from it. Depending on your Linux distribution and desktop environment,
you may have to adapt the following steps:

  1. Copy the freedesktop entry file for FreeCAD from /usr/share/applications/freecad.desktop to ~/.local/share/applications.
  2. Change the name from freecad.desktop to something else (e.g. MyFreeCADConfig.desktop).
  3. Open the file with a text editor and change how FreeCAD is invoked by modifying the line starting with `Exec`.
  4. As a result, an additional entry in your start menu/application launcher is available. This way, you can have multiple FreeCAD entries with various launch options.

## Starting FreeCAD from a portable USB medium

**Windows**

Put the FreeCAD executable, FreeCAD.exe, on the USB medium. Create a batch
file, FreeCAD.bat, and put it into the same directory as FreeCAD.exe. Inside
the batch file write:

    
    
    set CURRENTDIR=%cd%
    set FREECAD_USER_HOME=%CURRENTDIR%
    start FreeCAD.exe -u FreeCAD/user.cfg -s FreeCAD/system.cfg --write-log
    

Or with `FREECAD_USER_DATA`
([see](https://forum.freecad.org/viewtopic.php?f=12&t=54784&start=60#p474759)):

    
    
    set CURRENTDIR="%cd%"
    set FREECAD_USER_DATA=%CURRENTDIR%/..
    start FreeCAD.exe -u %FREECAD_USER_DATA%/user.cfg -s %FREECAD_USER_DATA%/system.cfg
    

With the batch in the root of the USB medium:

    
    
    set CURRENTDIR=%cd%
    set FREECAD_USER_DATA=%CURRENTDIR%FreeCAD\
    start %cd%FreeCAD\bin\FreeCAD.exe -u %FREECAD_USER_DATA%user.cfg -s %FREECAD_USER_DATA%system.cfg
    

Now double-click the batch file to start FreeCAD.
([see](https://forum.freecad.org/viewtopic.php?f=4&t=49028))

  

![](/images/6/6f/Arrow-left.svg) [Import Export
Preferences](/Import_Export_Preferences "Import Export Preferences")

[Scripting and macros](/Scripting_and_macros "Scripting and macros")
![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

Expand[![](/images/thumb/9/94/User_hub.png/24px-
User_hub.png)](/index.php?title=File:User_hub.png&filetimestamp=20190221145008&)
[User documentation](/User_hub "User hub")

  * **[Getting started](/Getting_started "Getting started")**
  * **Installation:** [Download](/Download "Download"), [Windows](/Installing_on_Windows "Installing on Windows"), [Linux](/Installing_on_Linux "Installing on Linux"), [Mac](/Installing_on_Mac "Installing on Mac"), [Additional components](/Installing_additional_components "Installing additional components"), [Docker](/Compile_on_Docker "Compile on Docker"), [AppImage](/AppImage "AppImage"), [Ubuntu Snap](/Ubuntu_Snap "Ubuntu Snap")
  * **Basics:** [About FreeCAD](/About_FreeCAD "About FreeCAD"), [Interface](/Interface "Interface"), [Mouse navigation](/Mouse_navigation "Mouse navigation"), [Selection methods](/Selection_methods "Selection methods"), [Object name](/Object_name "Object name"), [Preferences](/Preferences_Editor "Preferences Editor"), [Workbenches](/Workbenches "Workbenches"), [Document structure](/Document_structure "Document structure"), [Properties](/Property "Property"), [Help FreeCAD](/Help_FreeCAD "Help FreeCAD"), [Donate](/Donate "Donate")

* * *

  * **Help:** [Tutorials](/Tutorials "Tutorials"), [Video tutorials](/Video_tutorials "Video tutorials")
  * **[Workbenches](/Workbenches "Workbenches"):** [Std Base](/Std_Base "Std Base"), [Assembly](/Assembly_Workbench "Assembly Workbench"), [BIM](/BIM_Workbench "BIM Workbench"), [CAM](/CAM_Workbench "CAM Workbench"), [Draft](/Draft_Workbench "Draft Workbench"), [FEM](/FEM_Workbench "FEM Workbench"), [Inspection](/Inspection_Workbench "Inspection Workbench"), [Material](/Material_Workbench "Material Workbench"), [Mesh](/Mesh_Workbench "Mesh Workbench"), [OpenSCAD](/OpenSCAD_Workbench "OpenSCAD Workbench"), [Part](/Part_Workbench "Part Workbench"), [PartDesign](/PartDesign_Workbench "PartDesign Workbench"), [Points](/Points_Workbench "Points Workbench"), [Reverse Engineering](/Reverse_Engineering_Workbench "Reverse Engineering Workbench"), [Robot](/Robot_Workbench "Robot Workbench"), [Sketcher](/Sketcher_Workbench "Sketcher Workbench"), [Spreadsheet](/Spreadsheet_Workbench "Spreadsheet Workbench"), [Surface](/Surface_Workbench "Surface Workbench"), [TechDraw](/TechDraw_Workbench "TechDraw Workbench"), [Test Framework](/Testing "Testing")

* * *

  * **[Addons](/Addon "Addon"):** [Addon Manager](/Std_AddonMgr "Std AddonMgr"), [External workbenches](/External_workbenches "External workbenches"), [Scripting and macros](/Scripting_and_macros "Scripting and macros")

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

