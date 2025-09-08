---
url: https://wiki.freecad.org/Compile_on_Windows
title: Compile on Windows
scraped_at: 2025-09-08 16:45:08
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Prerequisites Toggle Prerequisites subsection
    * 1.1 Required
    * 1.2 Optional programs
    * 1.3 Source code
      * 1.3.1 Using a frontend
      * 1.3.2 Using the command line
    * 1.4 Compiler
    * 1.5 Optional system path configuration
  * 2 Configuration Toggle Configuration subsection
    * 2.1 CMake
    * 2.2 Options for the build process
  * 3 Building FreeCAD Toggle Building FreeCAD subsection
    * 3.1 Building from cmd.exe command line
    * 3.2 Building with Visual Studio 15 (2017) or newer
      * 3.2.1 Release Build
      * 3.2.2 Debug Build
      * 3.2.3 Video Resource
    * 3.3 Building with Qt Creator (outdated)
      * 3.3.1 Installation and configuration of Qt Creator
      * 3.3.2 Import project and building
    * 3.4 Command line build
  * 4 Running and installing FreeCAD Toggle Running and installing FreeCAD subsection
    * 4.1 Troubleshooting
  * 5 Updating the build Toggle Updating the build subsection
    * 5.1 Updating the source code
      * 5.1.1 Using a frontend
      * 5.1.2 Using the command line
    * 5.2 Recompilation
  * 6 Updating the LibPack
  * 7 Tools Toggle Tools subsection
    * 7.1 Qt Designer plugin
      * 7.1.1 Compilation
      * 7.1.2 Installation
    * 7.2 Thumbnail Provider
      * 7.2.1 Installation
      * 7.2.2 Compilation
  * 8 Compiling Open Cascade
  * 9 Compiling Netgen
  * 10 References

# Compile on Windows

  * [Page](/Compile_on_Windows "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Compile_on_Windows&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Compile_on_Windows)
  * [Edit](/index.php?title=Compile_on_Windows&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Compile_on_Windows&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Compile_on_Windows.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Compile_on_Windows&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Compile_on_Windows)
  * [Edit](/index.php?title=Compile_on_Windows&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Compile_on_Windows&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Compile_on_Windows&action=history)

General

  * [What links here](/Special:WhatLinksHere/Compile_on_Windows "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Compile_on_Windows "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Compile_on_Windows&oldid=1638170 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Compile_on_Windows&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Compile_on_Windows&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Compile+on+Windows&action=page&filter=&language=en)This is the approved
revision of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Compile+on+Windows&language=&task=view "Start translation for this language")
  * [Deutsch](/Compile_on_Windows/de "Kompilieren unter Windows \(91% translated\)")
  * English
  * [Türkçe](/Compile_on_Windows/tr "CompileOnWindows \(0% translated\)")
  * [español](/Compile_on_Windows/es "Compilar en Windows \(12% translated\)")
  * [français](/Compile_on_Windows/fr "Compiler sous Windows \(100% translated\)")
  * [hrvatski](/Compile_on_Windows/hr "KompilirajNaWindowsima \(0% translated\)")
  * [italiano](/Compile_on_Windows/it "Compilazione in Windows \(93% translated\)")
  * [polski](/Compile_on_Windows/pl "Kompilacja w systemie Windows \(100% translated\)")
  * [português](/Compile_on_Windows/pt "CompileOnWindows \(0% translated\)")
  * [português do Brasil](/Compile_on_Windows/pt-br "Compilar no Windows \(92% translated\)")
  * [română](/Compile_on_Windows/ro "CompileOnWindows \(12% translated\)")
  * [svenska](/Compile_on_Windows/sv "CompileOnWindows \(0% translated\)")
  * [čeština](/Compile_on_Windows/cs "CompileOnWindows \(0% translated\)")
  * [русский](/Compile_on_Windows/ru "Компиляция в Windows \(56% translated\)")
  * [中文（中国大陆）](/Compile_on_Windows/zh-cn "Windows 编译指南 \(72% translated\)")
  * [日本語](/Compile_on_Windows/ja "Windowsでのコンパイル \(1% translated\)")

![](/images/6/6f/Arrow-left.svg) [License](/License "License")

[Compile on Linux](/Compile_on_Linux "Compile on Linux")
![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

This page explains step by step **how to compile FreeCAD 0.19 or newer on
Windows** using Microsoft's MSVC compiler. For information on using
MSYS2/MinGW see [Compile on MinGW](/Compile_on_MinGW "Compile on MinGW"). For
other platforms see [Compiling](/Compiling "Compiling").

## Prerequisites

Compiling FreeCAD on Windows requires several tools and libraries.

### Required

  * A compiler. FreeCAD is tested with Visual Studio (MSVC)—other compilers may work, but instructions for use are not included here. For more details, see the section Compiler below.

  * [Git](http://git-scm.com/) (There are also GUI frontends available for Git, see the next section.)

  * [CMake](https://cmake.org/download/) version 3.11.x or newer.   
_Hint:_ Choosing the option _Add CMake to the system PATH for all users_ when
installing CMake will make CMake accessible from the Windows command prompt,
which can be useful.

  * The [LibPack](https://github.com/FreeCAD/FreeCAD-LibPack). This is a single package containing all of the libraries necessary to compile FreeCAD on Windows. Download the version of the LibPack that corresponds to the version of FreeCAD you want to compile. To compile FreeCAD 0.20 download the [LibPack version 2.6](https://github.com/FreeCAD/FreeCAD-LibPack/releases/tag/2.6), for FreeCAD 0.19 download the [LibPack version 1.0](https://github.com/FreeCAD/FreeCAD-LibPack/releases/tag/1.0). Extract the LibPack to a convenient location. (If your computer does not recognize the .7z extension, you must install the program [7-zip](https://www.7-zip.org).)   
**Note** : It is highly recommended to compile FreeCAD with the compiler
version the LibPack is designed for. For example, you might run into problems
compiling FreeCAD 0.20 using MSVC 2017 because the LibPack is designed to be
built with MSVC 2019 or newer.  
To update your LibPack later, see the section Updating the LibPack.

### Optional programs

  * A GUI frontend for Git. There are several frontends available, see [this list](https://git-scm.com/downloads/guis). The main benefit of a frontend is that you don't have to learn the Git commands to get the source code of FreeCAD or to send patches to the GitHub repository of FreeCAD.

In the following we describe source code handling using the
[TortoiseGit](https://tortoisegit.org/) frontend. This frontend integrates
directly into Windows file explorer and has a large user community to get help
in case you have problems.

  * [NSIS](http://sourceforge.net/projects/nsis/) is used to generate the FreeCAD Windows installer.

### Source code

Now you can get the source code of FreeCAD:

#### Using a frontend

When using the [Git frontends](https://git-scm.com/downloads/guis)

TortoiseGit:

  1. Create a new folder where the source code will be downloaded.
  2. Right-click on this folder in the Windows file explorer and select **Git Clone** in the context menu.
  3. A dialog will appear.
  4. In it, enter the URL for the FreeCAD Git repository:  
_<https://github.com/FreeCAD/FreeCAD.git>_

  5. Click **OK**.

The latest source code will be downloaded from the FreeCAD Git repository and
the folder will be tracked by Git.

#### Using the command line

To create a local tracking branch and download the source code, open a
terminal (command prompt) and switch there to the directory you want the
source, then type:

    
    
    git clone --recurse-submodules https://github.com/FreeCAD/FreeCAD.git
    

### Compiler

The default (recommended) compiler is MS Visual Studio (MSVC). Though it may
be possible to use other compilers, for example gcc via Cygwin or MinGW, it is
not tested or covered here.

You can get a free version of MSVC (for individual usage) by downloading the
[_Community_ edition of MS Visual
Studio](https://visualstudio.microsoft.com/vs/community/).

For those who want to avoid installing the huge MSVC for the mere purpose of
having a compiler, see [CompileOnWindows - Reducing Disk
Footprint](/CompileOnWindows_-_Reducing_Disk_Footprint "CompileOnWindows -
Reducing Disk Footprint").

**Note:** Although the _Community_ edition of MSVC is free, to use the IDE for
more than a 30-day trial period you must create a Microsoft account. If you
will only compile using the command line, you don't need the IDE and thus no
Microsoft account.

As a free and OpenSource alternative IDE you can use
[KDevelop](https://www.kdevelop.org/download). You can use KDevelop to modify
and write C++ code but must use the command line to compile.

### Optional system path configuration

Optionally you can include the paths to some folders to the system PATH
variable. This is helpful if you want to access programs in these folders from
the command line/powershell or if you want special programs to be found by the
compiler or CMake. Besides this, adding folders to the PATH might be necessary
if you did not use the corresponding options when installing the program.

  * You can include the folder of your LibPack in your system PATH variable. This is useful if you plan to build multiple configurations/versions of FreeCAD.
  * If you did not use the option to add CMake to the PATH while installing it, add its installation folder to the PATH:  
_C:\Program Files\CMake\bin_

  * If you did not use the option to add TortoiseGit to the PATH while installing it, add its installation folder to the PATH:  
_C:\Program Files\TortoiseGit\bin_

To add folder paths to the PATH variable:

  1. In the Windows Start menu Right click on _Computer_ and choose _Properties_.
  2. In the appearing dialog click on _Advanced system settings_.
  3. Another dialog will open. Click there in the tab _Advanced_ on **Environment Variables**.
  4. Again another dialog will open. Select then the variable _Path_ and click on **Edit**.
  5. And again another dialog will open. Click there on **New** and add to path to the folder of Git or the LibPack.
  6. Finally press **OK** and close all dialogs by pressing **OK** as well.

## Configuration

Once you have all of the necessary tools, libraries, and FreeCAD source code,
you are ready to begin the configuration and compilation process. This process
will proceed in five steps:

  1. Run CMake once to examine your system and begin the configuration progress (this will report that it failed).
  2. Adjust necessary CMake settings to set the locations of the LibPack and enable Qt5.
  3. Re-run CMake to finalize the configuration (this time it should succeed).
  4. Use CMake to generate the Visual Studio build system.
  5. Use Visual Studio to build FreeCAD.

### CMake

First, configure the build environment using CMake:

  1. Open the CMake GUI
  2. Specify the source folder of FreeCAD.
  3. Specify a build folder. This can be **build** in the folder you cloned the repo because this path is ignored by git. Do not use the source folder. CMake will create this folder if it does not exist.
  4. Click **Configure**.
  5. In the dialog that appears specify the generator you want to use: in most cases you will use the defaults in this dialog. For the standard MS Visual Studio use _Visual Studio xx 2yyy_ where xx is the compiler version and 2yyy the year of its release. It is recommended to use the default option _Use default native compilers_.

**Note:** It is important to specify the correct bit variant. If you have the
64-bit variant of the LibPack you must also use the x64 compiler.

This will begin the configuration and _will fail_ because of missing settings.
This is normal, you have not yet specified the location of the LibPack.
However, there are other failures that might occur that require some further
action on your part.

If it fails with the message that Visual Studio could not be found, the CMake
support in MSVC is not yet installed. To do this:

  1. Open the MSVC IDE
  2. Use the menu Tools → Get Tools and Features
  3. In the _Workloads_ tab enable _Desktop development with C++_
  4. On the right side you should now see that the component _Visual C++ tools for CMake_ will be installed.
  5. Install it.

If there is no error about Visual Studio or Python, everything is fine, but
CMake does not yet know all necessary settings. Therefore now:

  1. Search in CMake for the variable **FREECAD_LIBPACK_DIR** and specify the location of the LibPack folder you downloaded earlier. Use forward slashes "/". Using backslashes "\" will cause CMake to fail.
  2. (_If building FreeCAD 0.19_) Search for the variable **BUILD_QT5** and enable this option.
  3. Click **Configure** again.
  4. (_If planning on running directly from the build folder such as for debugging_) Search for and enable the following options: 
     * **FREECAD_COPY_DEPEND_DIRS_TO_BUILD**
     * **FREECAD_COPY_LIBPACK_BIN_TO_BUILD**
     * **FREECAD_COPY_PLUGINS_BIN_TO_BUILD**
  5. Click **Configure** again.

There should now be no errors. If you continue to encounter errors that you
cannot diagnose, visit the [Install/Compile
forum](https://forum.freecad.org/viewforum.php?f=4) on the FreeCAD forum
website. If CMake proceeded correctly, click on **Generate**. After this is
done you can close CMake and start the compilation of FreeCAD using Visual
Studio. However, for the first compilation keep it open in case you want or
need to change some options for the build process.

### Options for the build process

The CMake build system gives you control over some aspects of the build
process. In particular, you can switch on and off some features or modules
using CMake variables.

Here is a description of some of these variables:

Variable name | Description | Default   
---|---|---  
BUILD_XXX | Build FreeCAD with the component XXX. If you don't want/need to compile e.g. the workbench _OpenSCAD_ , disable the variable _BUILD_OPENSCAD_. FreeCAD will then not have this workbench. **Note:** Some components are required for other components. If you for example uncheck _BUILD_ROBOT_ CMake will inform you that then the component _Path_ cannot be compiled correctly. Therefore check the CMake output after you changed a BUILD_XXX option!  | depends   
BUILD_ENABLE_CXX_STD | The version of the C++ language standard. **C++14** is the highest possible for FreeCAD 0.19 while at least **C++17** is required for FreeCAD 0.20. See also the note in the section Building with Visual Studio 15 (2017) and 16 (2019) | depends   
BUILD_DESIGNER_PLUGIN | To build the Qt Designer plugin, see this section below | OFF   
BUILD_FLAT_MESH | Necessary to have a build that includes the [CreateFlatMesh feature](/MeshPart_CreateFlatMesh "MeshPart CreateFlatMesh") | OFF   
CMAKE_INSTALL_PREFIX | The output folder when building the target _INSTALL_ , see also the section Running and installing FreeCAD | Windows default program installation folder   
FREECAD_COPY_DEPEND_DIRS_TO_BUILD | Copies depending libraries needed to execute the FreeCAD.exe to the build folder. See also the section Running and installing FreeCAD.  
**Note:** the options FREECAD_COPY_XXX only appear if the libraries were not already copied. If you only need to upgrade/change to another LibPack version, see the section Updating the LibPack. If you want to bring back the options for some reason, you need to delete all folders in your build folder, except for the LibPack folder. In CMake delete the cache and start as if you compile for the first time. | OFF   
FREECAD_COPY_LIBPACK_BIN_TO_BUILD | Copies the LibPack binaries needed to execute the FreeCAD.exe to the build folder. See also the section Running and installing FreeCAD. | OFF   
FREECAD_COPY_PLUGINS_BIN_TO_BUILD | Copies Qt's plugin files needed to execute the FreeCAD.exe to the build folder. See also the section Running and installing FreeCAD. | OFF   
FREECAD_LIBPACK_USE | Switch the usage of the FreeCAD LibPack on or off | ON   
FREECAD_LIBPACK_DIR | Directory where the LibPack is | FreeCAD's source code folder   
FREECAD_RELEASE_PDB | Create debug libraries (*.pdb) also for release builds. It doesn't affect the speed (like a real debug build would do) and can be very useful to locate crashes in FreeCAD code. In case FreeCAD crashes a _crash.dmp_ file will be created that can be loaded with MSVC and if you have the corresponding PDB files plus the source code of that version you can debug through the code. Without the PDB files it's not possible to debug the code and all what the debugger shows is the name of the DLL where the crash has occurred. | ON   
FREECAD_USE_MP_COMPILE_FLAG | Adds the /MP (multiprocessor) option to the Visual Studio projects, enabling speedups on multi-core CPUs. This can greatly accelerate builds on modern processors.  
**Note:** If you turn off **FREECAD_USE_PCH** , the compilation can quickly overload your heap space, even if you have 16 GB RAM. | ON   
FREECAD_USE_PCH | [Precompiles the headers](https://en.wikipedia.org/wiki/Precompiled_header) in order to save compilation time. | ON   
FREECAD_USE_PYBIND11 | Includes the [PyBind11](https://github.com/pybind/pybind11) library. Necessary to have a build that includes the [CreateFlatMesh feature](/MeshPart_CreateFlatMesh "MeshPart CreateFlatMesh").  
**Note:** after turning it on you might get a configuration error. Just configure again and the problem should go away. | OFF   
  
## Building FreeCAD

Depending on your compiler, the process for building FreeCAD will be slightly
different. In the following sections known workflows are described. If you are
building with Qt Creator, jump to Building with Qt Creator (outdated),
otherwise proceed directly:

### Building from cmd.exe command line

If you want build from the command line, CMake output will show you the proper
command to run (which depends on the configured release directory). But this
command will produce a _Debug_ build which does not work on Windows and
results in a Numpy import error in FreeCAD (which is a known issue but hard to
fix). You need to specify the _\--config Release_ option to force a _Release_
build:

    
    
    cmake --build E:/release --config Release
    

Please note that setting CMake variables like _CMAKE_BUILD_TYPE_ does not have
any effect, only specifying the _\--config_ option as shown above works.

Expand

### Building with Visual Studio 15 (2017) or newer

#### Release Build

  1. Start the Visual Studio IDE. This can either be done by pressing the button _Open Project_ in the CMake GUI or by double-clicking on the file _FreeCAD.sln_ that you find in your build folder.
  2. In the toolbar of the MSVC IDE assure that you use for the first compilation _Release_.
  3. There is a window called _Solution Explorer_. It lists all possible compilation targets. To start a full compilation, right-click on the target **ALL_BUILD** and then choose **Build**.

This will now take quite a long time.

To compile a ready-to use FreeCAD, compile the target _INSTALL_ , see the
section Running and installing FreeCAD.

If you don't get any errors you are done. **Congratulations!** You can exit
MSVC or keep it open.

**Important:** Since Visual Studio 17.4 you cannot use the code optimization
that is on by default for the target **SketcherGui**. If you do, angle
constraints will be misplaced in sketches. To fix this, right-click on this
target in the MSVC solution explorer and select the last entry **Properties**
in the context menu. In the appearing dialog go to C/C++ → Optimization and
there disable the setting **Optimization**. Finally build the target
**ALL_BUILD** again.

#### Debug Build

As prerequisite for the debug build, you need to do this:

  1. Copy the content of the LibPack folder _bind_ to the _bin_ folder of the FreeCAD build folder (overwrite the existing files).
  2. Copy the content of the LibPack folder _libd_ to the _lib_ folder of the FreeCAD build folder.

Now you can compile:

  1. Start the Visual Studio IDE. This can either be done by pressing the button _Open Project_ in the CMake GUI or by double-clicking on the file _FreeCAD.sln_ that you find in your build folder.
  2. In the toolbar of the MSVC IDE assure that you use for the first compilation _Debug_.
  3. There is a window called _Solution Explorer_. It lists all possible compilation targets. To start a full compilation, right-click on the target **ALL_BUILD** and then choose **Build** in the context menu.

This will now take quite a long time.

If there were no compilation errors, and if the **FREECAD_COPY_*** options
mentioned in the CMake Configuration step above were enabled, you can start
the debug build:

  1. Right-click on the target **FreeCADMain** and then choose **Set as Startup Project** in the context menu.
  2. Finally click in the toolbar on the button with the green triangle named **Local Windows Debugger**.

This will start the debug build of FreeCAD and you can use the MSVC IDE to
debug it.

#### Video Resource

An English language tutorial that begins with configuration in CMake Gui and
continues to the `Build` command in Visual Studio 16 2019 is available
unlisted on YouTube at [Tutorial: Build FreeCAD from source on Windows
10](https://youtu.be/s4pHvlDOSZQ).

Expand

### Building with Qt Creator (outdated)

#### Installation and configuration of Qt Creator

  * Download and install [Qt Creator](https://www.qt.io/offline-installers)
  * Tools → Options → Text Editor → Behavior tab: 
    * File Encodings → Default Encodings:
    * Set to: **ISO-8859-1 /...csISOLatin1** (Certain characters create errors/warnings with Qt Creator if left set to UTF-8. This seems to fix it.)
  * Tools → Options → Build & Run: 
    * CMake tab 
      * Fill Executable box with path to cmake.exe
    * Kits tab 
      * Name: MSVC 2008
      * Compiler: Microsoft Visual C++ Compiler 9.0 (x86)
      * Debugger: Auto detected...
      * Qt version: None
    * General tab 
      * Uncheck: Always build project before deploying it
      * Uncheck: Always deploy project before running it

#### Import project and building

  * File → Open File or Project
  * Open **CMakeLists.txt** which is in the top level of the source
  * This will start CMake
  * Choose build directory and click next
  * Set generator to **NMake Generator (MSVC 2008)**
  * Click Run CMake. Follow the instructions depicted above to configure CMake to your liking.

Now FreeCAD can be built

  * Build → Build All
  * This will take a long time...

Once complete, it can be run: There are 2 green triangles at the bottom left.
One is debug. The other is run. Pick whichever you want.

Expand

### Command line build

The steps how to compile from the command line depends on the compiler. For
MSVC 2017 the steps are:

  1. In Windows start menu go to **Visual Studio 2017 → Visual Studio Tools** and choose **Developer Command Prompt for VS 2017**
  2. Change to your build folder.
  3. Execute the command

    
    
    msbuild ALL_BUILD.vcxproj /p:Configuration=Release
    

or

    
    
    msbuild INSTALL.vcxproj /p:Configuration=Release
    

These steps can also be automaized. Here is for example a solution for MSVC
2017:

  1. Download the script [compile-FC.txt](https://forum.freecad.org/download/file.php?id=92135).
  2. Rename it to _compile-FC.bat_
  3. In Windows file explorer Shift+Right-click on your build folder and use from the context menu _Command prompt here_.
  4. Execute the command

    
    
    compile-FC install
    

Instead of calling **compile-FC** with the option _install_ you can also use
_debug_ or _release_ :

_debug_ \- compile FreeCAD in debug configuration

_release_ \- compile FreeCAD in release configuration

_install_ \- compile FreeCAD in release configuration and create an install
setup

## Running and installing FreeCAD

There are 2 methods to run the compiled FreeCAD:

_Method 1_ : You execute the FreeCAD.exe that you find in your build folder in
the subfolder _bin_

_Method 2_ : You build the target _INSTALL_

Method 2 is the simpler one because it automatically assures that all
libraries needed to run the FreeCAD.exe are in the correct folder. The
FreeCAD.exe and the libraries will be output in the folder you specified in
the CMake variable _CMAKE_INSTALL_PREFIX_.

For Method 1 you need to enable the **FREECAD_COPY_*** options mentioned in
the CMake Configuration step above.

### Troubleshooting

When running FreeCAD you may encounter missing DLLs when using certain
workbenches or features of workbenches. The error message in FreeCAD's console
will not tell you what DLL is missing. To find this out you must use an
external tool:

  * Download the latest release of the program **Dependencies** : <https://github.com/lucasg/Dependencies/releases> (choose the file _Dependencies_x64_Release.zip_)
  * In the FreeCAD [Python console](/Python_console "Python console") execute these commands:

    
    
    import os
    os.system(r"~\DependenciesGui.exe")
    

**Note** : Instead of the ~ you must specify the full path to the
_DependenciesGui.exe_ on your system.

  * Now drag in the *.pyd file of the workbench with which you get missing DLLs reported.

## Updating the build

FreeCAD is very actively developed. Therefore its source code changes almost
daily. New features are added and bugs are fixed. To benefit from these source
code changes, you must rebuild your FreeCAD. This is done in two steps:

  1. Updating the source code
  2. Recompilation

### Updating the source code

#### Using a frontend

When using the [Git
frontend](https://en.wikipedia.org/wiki/Comparison_of_Git_GUIs) TortoiseGit:

  1. Right-click on your FreeCAD source code folder in the Windows file explorer and select **Pull** in the context menu.
  2. A dialog will appear. Select there what development branch you want to get. **main** is the main branch. Therefore use this unless you want to compile a special new feature from a branch that has not yet been merged to _main_. (For more about Git branches, see [Git development process](/Source_code_management#Git_development_process "Source code management").)

Finally click **OK**.

#### Using the command line

Open a terminal (command prompt) and switch there to your source directory.
Then type:

    
    
    git pull https://github.com/FreeCAD/FreeCAD.git main
    

where _main_ the the name of the main development branch. If you want to get
code from another branch, use its name instead of _main_.

### Recompilation

  1. Open the MSVC IDE by double-clicking either on the file _FreeCAD.sln_ or on the file _ALL_BUILD.vcxproj_ in your build folder.
  2. Continue with step 2 from the section Building with Visual Studio 15 2017.

## Updating the LibPack

If a new major version of a third-party dependency like Open Cascade is
released, or if a third-party dependency has important bug fixes, a new
LibPack is released. You can find the latest version
[here](https://github.com/FreeCAD/FreeCAD-LibPack/releases/).

To update your LibPack the following recipe is best practice:

  1. Delete the _bin_ folder in your build folder.
  2. Switch to your local LibPack folder and delete everything there.
  3. Extract the content of the new LibPack ZIP file into the existing, but now empty, local LibPack folder.
  4. Open CMake and there press the button **Configure** and then the button **Generate**. This recreates the _bin_ folder you just deleted and also copies the new LibPack files into it.
  5. In CMake click the button **Open Project** and the MSVC IDE will open.
  6. In the MSVC IDE build the target _INSTALL_.

## Tools

In order to join the FreeCAD development you should compile and install the
following tools:

### Qt Designer plugin

FreeCAD uses [Qt](https://en.wikipedia.org/wiki/Qt_\(software\)) as toolkit
for its user interface. All dialogs are setup in UI-files that can be edited
using the program [Qt Designer](https://doc.qt.io/qt-5/qtdesigner-manual.html)
that is part of any Qt installation and also included in the LibPack. FreeCAD
has its own set of Qt widgets to provide special features like adding a unit
to input fields and to set preferences properties.

#### Compilation

The plugin cannot be loaded by the Qt Designer if it was compiled using
another Qt version than the one your Qt Designer/Qt Creator is based on.
Therefore the plugin must be compiled together with FreeCAD:

  * In the CMake options (see this section above) enable the option BUILD_DESIGNER_PLUGIN and reconfigure.
  * open MSVC and build the target **FreeCAD_widgets**

As result you will get the plugin file '_FreeCAD_widgets.dll_ in the folder  
 _~\src\Tools\plugins\widget\Release_

#### Installation

To install the plugin, copy the DLL either to:

  * If you use the LibPack: to the folder  
 _~\FreeCADLibs_2_8_x64_VC2019\plugins\designer_

  * If you have a full Qt installation: you can choose between the folder  
 _C:\Qt\5.15.2\msvc2019_64\plugins\designer_  
or  
 _C:\Qt\5.15.2\msvc2019_64\bin\designer_ (you must first create the _designer_
subfolder.)  
(adapt the paths to your installation!).

Finally (re)start Qt Designer and check its menu **Help → Plugins**. If the
plugin **FreeCAD_widgets.dll** is listed as being loaded, you can now design
and change FreeCAD's .ui files. If not, you must compile the DLL by yourself.

If you prefer using [Qt Creator](https://en.wikipedia.org/wiki/Qt_Creator)
instead of Qt Designer, the plugin file must be placed in this folder:  
_C:\Qt\Qt5.15.2\Tools\QtCreator\bin\plugins\designer_  
Then (re)start Qt Creator, switch to the mode **Design** and then check the
menu **Tools → Form Editor → About Qt Designer Plugins**. If the plugin
**FreeCAD_widgets.dll** is listed as being loaded, you can now design and
change FreeCAD's .ui files. If not, you must compile the DLL by yourself.

### Thumbnail Provider

FreeCAD has the feature to provide preview thumbnails for *.FCStd files. That
means that in the Windows file explorer *.FCStd files are shown with a
screenshot of the model it contains. To provide this feature, FreeCAD needs to
have the file **FCStdThumbnail.dll** installed to Windows.

#### Installation

The DLL is installed this way:

  1. Download [this ZIP file](https://forum.freecad.org/download/file.php?id=13404) and extract it.
  2. Open a Windows command prompt with administrator privileges (these privileges are a requirement).
  3. Change to the folder where the DLL is.
  4. Execute this command 
         
         regsvr32 FCStdThumbnail.dll
         

So check if it works, assure that in FreeCAD the preferences option **[Save
thumbnail into project file when saving document](/Preferences_Editor#Document
"Preferences Editor")** is enabled and save a model. Then view in Windows
Explorer the folder of the saved model using a symbol view. You should now see
a screenshot of the model in the folder view.

#### Compilation

To compile the FCStdThumbnail.dll

  1. Change to the FreeCAD source folder  
 _~\src\Tools\thumbs\ThumbnailProvider_

  2. Open the CMake GUI
  3. Specify there as source folder the one you are currently in.
  4. Use the same folder as build folder.
  5. Click **Configure**
  6. In the appearing dialog, specify the generator according to the one you want to use. For the standard MS Visual Studio use _Visual Studio xx 2yyy_ where xx is the compiler version and 2yyy the year of its release. It is recommended to use the default option _Use default native compilers_.  
**Note:** It is important to specify the correct bit variant. If you have the
64bit variant of LibPack you must also use the x64 compiler.

  7. Click on **Generate**.
  8. You should now have the file **ALL_BUILD.vcxproj** in the folder _~\src\Tools\thumbs\ThumbnailProvider_. Double-click on it and the MSVC IDE will open.
  9. In the toolbar of the MSVC IDE assure that you use the compilation target _Release_.
  10. There is a window called _Solution Explorer_. Right-click there on **ALL_BUILD** and then choose **Build**.
  11. As result you should now have a **FCStdThumbnail.dll** in the folder _~\src\Tools\thumbs\ThumbnailProvider\release_ that you can install as described above.

## Compiling Open Cascade

The LibPack comes with a version of [Open
Cascade](https://en.wikipedia.org/wiki/Open_Cascade) that is suitable for
general use. However, under some circumstances you may wish to compile against
an alternate version of Open Cascade, such as one of their official releases,
or a patched fork.

When compiling Open Cascade for FreeCAD note that there is no guarantee that
FreeCAD will work with all versions of Open Cascade. Note also that when you
are using the Netgen library, you must use the a NetGen version that it
approved to compile with the Open Cascade version you like to compile.

To compile:

  * First obtain the Open Cascade source code, either directly from [Open Cascade's git repository](https://github.com/Open-Cascade-SAS/OCCT) or by cloning someone else's fork, such as [the "blobfish" fork](https://gitlab.com/blobfish/occt) maintained by FreeCAD forum member [tanderson69](https://forum.freecad.org/memberlist.php?mode=viewprofile&u=208).

  * Then open the CMake GUI to configure the build system in a similar manner to building FreeCAD. These CMake options have to be set (or explicitly not set):

Variable name | Description | Default   
---|---|---  
3RDPARTY_DIR | The path to 3rdparty components. It is recommended to use the folder as input where your used LibPack is. Explicitly leave this field empty.  | empty   
3RDPARTY_DOXYGEN_EXECUTABLE | The path to the executable of the 3rdparty component [Doxygen](https://en.wikipedia.org/wiki/Doxygen). It is recommended to install Doxygen. CMake will then find it automatically.  | empty   
3RDPARTY_FREETYPE_DIR | The path to the necessary 3rdparty component [Freetype](https://en.wikipedia.org/wiki/FreeType). It is recommended to use the folder as input where your used LibPack is.  | empty   
3RDPARTY_RAPIDJSON_DIR | Only available if **USE_RAPIDJSON** is used. The path to the 3rdparty component [RapidJSON](https://rapidjson.org/). It is recommended NOT to use an existing LibPack folder as input. You can use the RapidJSOn folder from a LibPack, but copy it to a new folder and use this new folder as input.  | empty   
3RDPARTY_TCL_DIR | The path to the necessary 3rdparty component [TCL](https://en.wikipedia.org/wiki/Tcl). It is recommended NOT to use an existing LibPack folder as input. Take for example one of [these releases](https://github.com/teclab-at/tcltk/releases), extract it and take this as input folder for CMake.  | empty   
3RDPARTY_TK_DIR | The path to the necessary 3rdparty component [TK](https://en.wikipedia.org/wiki/Tk_\(software\)). It is recommended NOT to use an existing LibPack folder as input. Take for example one of [these releases](https://github.com/teclab-at/tcltk/releases), extract it and take this as input folder for CMake.  | empty   
3RDPARTY_VTK_DIR | Only available if **USE_VTK** is used. The path to the necessary 3rdparty component [VTK](https://en.wikipedia.org/wiki/VTK). It is recommended to use the folder as input where your used LibPack is. If you use another folder please assure that you don't use VTK 9.x or newer.  | empty   
BUILD_RELEASE_DISABLE_EXCEPTIONS | Disables exception handling for release builds. For FreeCAD you must set it to **OFF**.  | ON   
INSTALL_DIR | The output folder when building the target _INSTALL_. If the build was successful, take the files from this folder to update your LibPack.  | Windows default program installation folder   
INSTALL_DIR_BIN | The output subfolder for the DLL when building the target _INSTALL_. You must change it to **bin** | win64/vc14/bin   
INSTALL_DIR_LIB | The output subfolder for the .lib files when building the target _INSTALL_. You must change it to **lib** | win64/vc14/lib   
USE_RAPIDJSON | To compile Open Cascade with support for RapidJSON. Enabling this is mandatory in order to get support for the file format [glTF](https://en.wikipedia.org/wiki/Gltf).  | OFF   
USE_VTK | To compile Open Cascade with support for VTK. Enabling this is optimal. You can use this to build Open Cascade's VTK bridge.  | OFF   
  
  * Open the project in Visual Studio and first build the ALL_BUILD and then INSTALL targets in the **Release** mode.
  * Repeat building the two targets in the **Debug** mode.

To build FreeCAD using the self-compiled Open Cascade, you must do the
following:

  * Copy all folders from the INSTALL_DIR to your LibPack folder (overwrite the existing files)
  * Switch to the LibPack folder and go there to the subfolder _cmake_
  * Open there the file _OpenCASCADEDrawTargets.cmake_ with a text editor
  * Search there for absolute paths to your LibPack folder and remove them. So e.g. the absolute path  
 _D:/FreeCADLibs_12.5.4_x64_VC17/lib/freetype.lib_  
becomes just  
_freetype.lib_  

  * Do the same for the file _OpenCASCADEVisualizationTargets.cmake_

## Compiling Netgen

The LibPack comes with a version of [Netgen](https://ngsolve.org) that will
was tested to be build with the Open Cascade version of the LibPack. The
problem is that every new release of Netgen changes the API. Also every new
release of Open Cascade does the same. Therefore one cannot just easily change
the Netgen version.

However, you might build Netgen nevertheless. This is an easy task:

  * First obtain the Netgen source code, either directly from [Netgen 's git repository](https://github.com/NGSolve/netgen).
  * Then open the CMake GUI to configure the build system in a similar manner to building FreeCAD. These CMake options have to be set:

Variable name | Description | Default   
---|---|---  
CMAKE_INSTALL_PREFIX | The output folder when building the target _INSTALL_. If the build was successful, take the files from this folder to update your LibPack.  | C:/netgen   
OpenCasCade_DIR | The path to the CMake files of Open Cascade. If you built Open Cascade as described in the section Compiling Open Cascade you can use the subfolder _cmake_ of there folder you used as INSTALL_DIR. If not, use the subfolder _cmake_ of your LibPack. Note hereby that the LibPack must then already contain a proper Open Cascade build. Independent what folder you use, you must now also create there a subfolder _lib_ and copy in the files _freetype.lib_ and _freetyped.lib_ from your LibPack.  | empty   
USE_GUI | set it to **OFF** | ON   
USE_NATIVE_ARCH | set it to **OFF** ; this is only necessary important to support older CPU that don't have the [AVX2](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions) instruction set  | ON   
USE_OCC | set it to **ON** | OFF   
USE_PYTHON | set it to **OFF** | ON   
USE_SUPERBUILD | set it to **OFF** | ON   
ZLIB_INCLUDE_DIR | The path to the necessary 3rdparty component [zlib](https://en.wikipedia.org/wiki/Zlib). It is recommended to use the folder as input where your used LibPack is.  | empty   
ZLIB_LIBRARY_DEBUG | The path to the ZLib file _zlibd.lib_. It is located in the subfolder _lib_ of your LibPack folder.  | empty   
ZLIB_LIBRARY_RELEASE | The path to the ZLib file _zlib.lib_. It is located in the subfolder _lib_ of your LibPack folder.  | empty   
  
  * Additionally you need to add a new CMake entry:

name: _CMAKE_DEBUG_POSTFIX_ , type: _string_ , content: **_d**  
This assures that he file names of the debug libraries get another name than
the release libraries and can later not be accidentally exchanged.

  * Press the _Configure_ button in CMake to generate the *.cmake files.
  * Only necessary if older CPU should be supported that don't have the AVX2 instruction set: 
    * Search your Netgen build folder for the file _netgen-targets.cmake_ and open it with a text editor. Remove the setting _;/arch:AVX2_ in the Option INTERFACE_COMPILE_OPTIONS.
    * Press the _Configure_ button in CMake again.
  * Press the _Generate_ button in CMake.
  * Open the project in Visual Studio and first build the ALL_BUILD and then INSTALL targets in the **Release** mode.
  * Repeat building the two targets in the **Debug** mode.

To build FreeCAD using the self-compiled Netgen, you must do the following:

  * Copy all folders from the CMAKE_INSTALL_PREFIX to your LibPack folder (overwrite the existing files)

## References

See also

  * [Compiling - Speeding up](/Compiling_\(Speeding_up\) "Compiling \(Speeding up\)")

  

![](/images/6/6f/Arrow-left.svg) [License](/License "License")

[Compile on Linux](/Compile_on_Linux "Compile on Linux")
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

