---
url: https://wiki.freecad.org/Extra_python_modules
title: Extra python modules
scraped_at: 2025-09-08 16:46:35
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Overview
  * 2 PySide Toggle PySide subsection
    * 2.1 Installation
      * 2.1.1 Linux
      * 2.1.2 Windows
      * 2.1.3 MacOS
    * 2.2 Usage
    * 2.3 Additional documentation
  * 3 Pivy Toggle Pivy subsection
    * 3.1 Installation
      * 3.1.1 Prerequisites
      * 3.1.2 Debian & Ubuntu
      * 3.1.3 Other Linux distributions
      * 3.1.4 MacOS
      * 3.1.5 Windows
    * 3.2 Usage
    * 3.3 Additonal Documentation
  * 4 pyCollada Toggle pyCollada subsection
    * 4.1 Installation
      * 4.1.1 Linux
      * 4.1.2 Linux AppImages and Snaps
      * 4.1.3 Windows
      * 4.1.4 MacOS
  * 5 IfcOpenShell Toggle IfcOpenShell subsection
    * 5.1 Installation
      * 5.1.1 Linux
      * 5.1.2 Windows and macOS
    * 5.2 Links
  * 6 LazyLoader Toggle LazyLoader subsection
    * 6.1 Installation
    * 6.2 Usage
    * 6.3 Links

# Extra python modules

  * [Page](/Extra_python_modules "View the content page \[ctrl-option-c\]")
  * [Discussion](/Talk:Extra_python_modules "Discussion about the content page \[ctrl-option-t\]")

English

  * [Read](/Extra_python_modules)
  * [Edit](/index.php?title=Extra_python_modules&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Extra_python_modules&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Extra_python_modules.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Extra_python_modules&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Extra_python_modules)
  * [Edit](/index.php?title=Extra_python_modules&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Extra_python_modules&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Extra_python_modules&action=history)

General

  * [What links here](/Special:WhatLinksHere/Extra_python_modules "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Extra_python_modules "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Extra_python_modules&oldid=1605008 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Extra_python_modules&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Extra_python_modules&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Extra+python+modules&action=page&filter=&language=en)This is the approved
revision of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Extra+python+modules&language=&task=view "Start translation for this language")
  * [Deutsch](/Extra_python_modules/de "Zusätzliche Python Module \(98% translated\)")
  * English
  * [Türkçe](/Extra_python_modules/tr "Extra python modules \(1% translated\)")
  * [español](/Extra_python_modules/es "Módulos extra de python \(42% translated\)")
  * [français](/Extra_python_modules/fr "Modules Python supplémentaires \(100% translated\)")
  * [italiano](/Extra_python_modules/it "Moduli Python aggiuntivi \(100% translated\)")
  * [polski](/Extra_python_modules/pl "Dodatkowe moduły Python \(100% translated\)")
  * [português do Brasil](/Extra_python_modules/pt-br "Módulos python extras \(3% translated\)")
  * [română](/Extra_python_modules/ro "Module suplimentare de python \(45% translated\)")
  * [svenska](/Extra_python_modules/sv "Extra python modules \(24% translated\)")
  * [čeština](/Extra_python_modules/cs "Extra python modules \(1% translated\)")
  * [русский](/Extra_python_modules/ru "Дополнительные python модули \(20% translated\)")
  * [日本語](/Extra_python_modules/ja "外部Pythonモジュールの追加 \(1% translated\)")

![](/images/6/6f/Arrow-left.svg) [Workbench creation](/Workbench_creation
"Workbench creation")

[Source documentation](/Source_documentation "Source documentation")
![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

## Overview

This page lists several additional Python modules or other pieces of software
that can be downloaded freely from the internet, and add functionality to your
FreeCAD installation.

## PySide

  * homepage (PySide): <http://qt-project.org/wiki/PySide>
  * license: LGPL
  * optional, but needed by several modules: Draft, BIM, Ship, Plot, OpenSCAD, Spreadsheet

PySide is required by several modules of FreeCAD to access FreeCAD's Qt
interface. It is already bundled in the windows verison of FreeCAD, and is
usually installed automatically by FreeCAD on Linux, when installing from
official repositories. If those modules (Draft, BIM, etc) are enabled after
FreeCAD is installed, it means PySide is already there, and you don't need to
do anything more.

**Note:** FreeCAD progressively moved away from PyQt after version 0.13, in
favour of [PySide](http://qt-project.org/wiki/PySide), which does exactly the
same job but has a license (LGPL) more compatible with FreeCAD.

### Installation

#### Linux

The simplest way to install PySide is through your distribution's package
manager. On Debian/Ubuntu systems, the package name is generally _python-
PySide_ , while on RPM-based systems it is named _pyside_. The necessary
dependencies (Qt and SIP) will be taken care of automatically.

#### Windows

The program can be downloaded from <http://qt-
project.org/wiki/Category:LanguageBindings::PySide::Downloads> . You'll need
to install the Qt and SIP libraries before installing PySide (to be
documented).

#### MacOS

PySide on Mac can be installed via homebrew or port. See [Install
dependencies](/Compile_on_MacOS#Install_Dependencies "Compile on MacOS") for
more information.

### Usage

Once it is installed, you can check that everything is working by typing in
FreeCAD Python console:

    
    
    import PySide
    

To access the FreeCAD interface, type:

    
    
    from PySide import QtCore,QtGui
    FreeCADWindow = FreeCADGui.getMainWindow()
    

Now you can start to explore the interface with the dir() command. You can add
new elements, like a custom widget, with commands like:

    
    
    FreeCADWindow.addDockWidget(QtCore.Qt.RghtDockWidgetArea,my_custom_widget)
    

Working with Unicode:

    
    
    text = text.encode('utf-8')
    

Working with QFileDialog and OpenFileName:

    
    
    path = FreeCAD.ConfigGet("AppHomePath")
    #path = FreeCAD.ConfigGet("UserAppData")
    OpenName, Filter = PySide.QtGui.QFileDialog.getOpenFileName(None, "Read a txt file", path, "*.txt")
    

Working with QFileDialog and SaveFileName:

    
    
    path = FreeCAD.ConfigGet("AppHomePath")
    #path = FreeCAD.ConfigGet("UserAppData")
    SaveName, Filter = PySide.QtGui.QFileDialog.getSaveFileName(None, "Save a file txt", path, "*.txt")
    

### Additional documentation

  * [Qt official documentation site](https://doc.qt.io/qt.html#qtforpython)

## Pivy

  * homepage: <https://www.coin3d.org/>
  * license: BSD
  * optional, but needed by several modules of FreeCAD: Draft, BIM

Pivy is a needed by several modules to access the 3D view of FreeCAD. On
windows, Pivy is already bundled inside the FreeCAD installer, and on Linux it
is usually automatically installed when you install FreeCAD from an official
repository. On macOS, unfortunately, you will need to compile pivy yourself.

### Installation

#### Prerequisites

I believe before compiling Pivy you will want to have Coin and SoQt installed.

I found for building on Mac it was sufficient to install the [Coin3 binary
package](http://www.coin3d.org/lib/plonesoftwarecenter_view). Attempting to
install coin from MacPorts was problematic: tried to add a lot of X Windows
packages and ultimately crashed with a script error.

For Fedora I found an RPM with Coin3.

SoQt compiled from [source](http://www.coin3d.org/lib/soqt/releases/1.5.0)
fine on Mac and Linux.

#### Debian & Ubuntu

Starting with Debian Squeeze and Ubuntu Lucid, pivy will be available directly
from the official repositories, saving us a lot of hassle. In the meantime,
you can either download one of the packages we made (for debian and ubuntu
karmic) availables on the [Download](/Download "Download") pages, or compile
it yourself.

The best way to compile pivy easily is to grab the debian source package for
pivy and make a package with debuild. It is the same source code from the
official pivy site, but the debian people made several bug-fixing additions.
It also compiles fine on ubuntu karmic:
<http://packages.debian.org/squeeze/python-pivy> download the .orig.gz and the
.diff.gz file, then unzip both, then apply the .diff to the source: go to the
unzipped pivy source folder, and apply the .diff patch:

    
    
    patch -p1 < ../pivy_0.5.0~svn765-2.diff
    

then

    
    
    debuild
    

to have pivy properly built into an official installable package. Then, just
install the package with gdebi.

#### Other Linux distributions

First get the latest sources from the [project's
repository](https://github.com/coin3d/pivy):

Information to be added.

As of March 2012, the latest version is Pivy-0.5.

Then you need a tool called SWIG to generate the C++ code for the Python
bindings. Pivy-0.5 reports that it has only been tested with SWIG 1.3.31,
1.3.33, 1.3.35, and 1.3.40. So you can download a source tarball for one of
these old versions from <http://www.swig.org>. Then unpack it and from a
command line do (as root):

    
    
    ./configure
    make
    make install (or checkinstall if you use it)
    

It takes just a few seconds to build.

Alternatively, you can try building with a more recent SWIG. As of March 2012,
a typical repository version is 2.0.4. Pivy has a minor compile problem with
SWIG 2.0.4 on macOS (see below) but seems to build fine on Fedora Core 15.

After that go to the pivy sources and call

    
    
    python setup.py build
    

which creates the source files. Note that build can produce thousands of
warnings, but hopefully there will be no errors.

This is probably obsolete, but you may run into a compiler error where a
'const char*' cannot be converted in a 'char*'. To fix that you just need to
write a 'const' before in the appropriate lines. There are six lines to fix.

After that, install by issuing (as root):

    
    
    python setup.py install (or checkinstall python setup.py install)
    

That's it, pivy is installed.

#### MacOS

These instructions may not be complete. Something close to this worked for OS
10.7 as of March 2012. I use MacPorts for repositories, but other options
should also work.

As for linux, get the latest source:

    
    
    hg clone http://hg.sim.no/Pivy/default Pivy
    

If you don't have hg, you can get it from MacPorts:

    
    
    port install mercurial
    

Then, as above you need SWIG. It should be a matter of:

    
    
    port install swig
    

I found I needed also:

    
    
    port install swig-python
    

As of March 2012, MacPorts SWIG is version 2.0.4. As noted above for linux,
you might be better off downloading an older version. SWIG 2.0.4 seems to have
a bug that stops Pivy building. See first message in this
[digest](https://sourceforge.net/mailarchive/message.php?msg_id=28114815)

This can be corrected by editing the 2 source locations to add dereferences:
*arg4, *arg5 in place of arg4, arg5. Now Pivy should build:

    
    
    python setup.py build
    sudo python setup.py install
    

#### Windows

Assuming you are using Visual Studio 2005 or later you should open a command
prompt with 'Visual Studio 2005 Command prompt' from the Tools menu. If the
Python interpreter is not yet in the system path do

    
    
    set PATH=path_to_python_3.x;%PATH%
    

To get pivy working you should get the latest sources from the project's
repository:

Information to be added.

Then you need a tool called SWIG to generate the C++ code for the Python
bindings. It is recommended to use version 1.3.25 of SWIG, not the latest
version, because at the moment pivy will only function correctly with 1.3.25.
Download the binaries for 1.3.25 from <http://www.swig.org>. Then unpack it
and from the command line add it to the system path

    
    
    set PATH=path_to_swig_1.3.25;%PATH%
    

and set COINDIR to the appropriate path

    
    
    set COINDIR=path_to_coin
    

On Windows the pivy config file expects SoWin instead of SoQt as default. I
didn't find an obvious way to build with SoQt, so I modified the file setup.py
directly. In line 200 just remove the part 'sowin': ('gui._sowin', 'sowin-
config', 'pivy.gui.') (do not remove the closing parenthesis).

After that go to the pivy sources and call

    
    
    python setup.py build
    

which creates the source files. You may run into a compiler error several
header files couldn't be found. In this case adjust the INCLUDE variable

    
    
    set INCLUDE=%INCLUDE%;path_to_coin_include_dir
    

and if the SoQt headers are not in the same place as the Coin headers also

    
    
    set INCLUDE=%INCLUDE%;path_to_soqt_include_dir
    

and finally the Qt headers

    
    
    set INCLUDE=%INCLUDE%;path_to_pyside\include\Qt
    

If you are using the Express Edition of Visual Studio you may get a Python
keyerror exception. In this case you have to modify a few things in
msvccompiler.py located in your Python installation.

Go to line 122 and replace the line

    
    
    vsbase = r"Software\Microsoft\VisualStudio\%0.1f" % version
    

with

    
    
    vsbase = r"Software\Microsoft\VCExpress\%0.1f" % version
    

Then retry again. If you get a second error like

    
    
    error: Python was built with Visual Studio 2003;...
    

you must also replace line 128

    
    
    self.set_macro("FrameworkSDKDir", net, "sdkinstallrootv1.1")
    

with

    
    
    self.set_macro("FrameworkSDKDir", net, "sdkinstallrootv2.0")
    

Retry once again. If you get again an error like

    
    
    error: Python was built with Visual Studio version 8.0, and extensions need to be built with the same version of the compiler, but it isn't installed.
    

then you should check the environment variables DISTUTILS_USE_SDK and MSSDK
with

    
    
    echo %DISTUTILS_USE_SDK%
    echo %MSSDK%
    

If not yet set then just set it e.g. to 1

    
    
    set DISTUTILS_USE_SDK=1
    set MSSDK=1
    

Now, you may run into a compiler error where a 'const char*' cannot be
converted in a 'char*'. To fix that you just need to write a 'const' before in
the appropriate lines. There are six lines to fix. After that copy the
generated pivy directory to a place where the Python interpreter in FreeCAD
can find it.

### Usage

To check if Pivy is correctly installed:

    
    
    import pivy
    

To have Pivy access the FreeCAD scenegraph do the following:

    
    
    from pivy import coin
    App.newDocument() # Open a document and a view
    view = Gui.ActiveDocument.ActiveView
    FCSceneGraph = view.getSceneGraph() # returns a pivy Python object that holds a SoSeparator, the main "container" of the Coin scenegraph
    FCSceneGraph.addChild(coin.SoCube()) # add a box to scene
    

You can now explore the FCSceneGraph with the dir() command.

### Additonal Documentation

Unfortunately documentation about pivy is still almost nonexistant on the net.
But you might find Coin documentation useful, since pivy simply translate Coin
functions, nodes and methods in Python, everything keeps the same name and
properties, keeping in mind the difference of syntax between C and Python:

  * <https://github.com/coin3d/coin/wiki/Documentation> \- Coin3D API Reference
  * <http://www-evasion.imag.fr/~Francois.Faure/doc/inventorMentor/sgi_html/index.html> \- The Inventor Mentor - The "bible" of Inventor scene description language.

You can also look at the Draft.py file in the FreeCAD Mod/Draft folder, since
it makes big use of pivy.

## pyCollada

  * homepage: <https://pycollada.github.io>
  * license: BSD
  * optional, needed to enable import and export of Collada (.DAE) files

pyCollada is a Python library that allow programs to read and write [Collada
(*.DAE)](https://en.wikipedia.org/wiki/COLLADA) files. When pyCollada is
installed on your system, FreeCAD will be able to handle importing and
exporting in the Collada file format.

### Installation

#### Linux

    
    
    sudo apt-get install python3-collada
    

You can check if pycollada was correctly installed by issuing in a Python
console:

    
    
    import collada
    

If it returns nothing (no error message), then all is OK

#### Linux AppImages and Snaps

Paste this code in the [Python console](/Python_console "Python console"):

    
    
    import addonmanager_utilities as utils
    import subprocess
    import os
    
    if hasattr(utils, "get_python_exe"):
        # For v0.21:
        python_exe = utils.get_python_exe()
    else:
        # For v0.22/v1.0:
        from freecad.utils import get_python_exe
    
    python_exe = get_python_exe()
    vendor_path = utils.get_pip_target_directory()
    if not os.path.exists(vendor_path):
        os.makedirs(vendor_path)
    
    subprocess.run(
        [
            python_exe,
            "-m",
            "pip",
            "install",
            "--disable-pip-version-check",
            "--target",
            vendor_path,
            "pycollada",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=120,
        check=True,
    )
    

#### Windows

On Windows since 0.15 pycollada is included in both the FreeCAD release and
developer builds so no additional steps are necessary.

#### MacOS

If you are using the Homebrew build of FreeCAD you can install pycollada into
your system Python using pip.

If you need to install pip:

    
    
    $ sudo easy_install pip
    

Install pycollada:

    
    
    $ sudo pip install pycollada
    

If you are using a binary version of FreeCAD, you can tell pip to install
pycollada into the site-packages inside FreeCAD.app:

    
    
    $ pip install --target="/Applications/FreeCAD.app/Contents/lib/python3.x/site-packages" pycollada
    

or after downloading the pycollada code

    
    
    $ export PYTHONPATH=/Applications/FreeCAD\ 0.16.6706.app/Contents/lib/python3.x/site-packages:$PYTHONPATH
    $ python setup.py install --prefix=/Applications/FreeCAD\ 0.2x.yyyy.app/Contents
    

## IfcOpenShell

  * homepage: <http://www.ifcopenshell.org>
  * license: LGPL
  * optional, needed to extend import abilities of IFC files

IFCOpenShell is a library currently in development, that allows to import (and
soon export) [Industry foundation Classes
(*.IFC)](https://en.wikipedia.org/wiki/Industry_Foundation_Classes) files. IFC
is an extension to the STEP format, and is becoming the standard in
[BIM](https://en.wikipedia.org/wiki/Building_information_modeling) workflows.
When ifcopenshell is correctly installed on your system, the FreeCAD [BIM
Workbench](/BIM_Workbench "BIM Workbench") will detect it and use it to import
IFC files, instead of its built-in rudimentary importer. Since ifcopenshell is
based on OpenCasCade, like FreeCAD, the quality of the import is very high,
producing high-quality solid geometry.

### Installation

#### Linux

Installation instructions can be found
[here](https://docs.ifcopenshell.org/ifcopenshell-python/installation.html).

You can check that ifcopenshell was correctly installed by issuing in a Python
console:

    
    
    import ifcopenshell
    

If it returns nothing (no error message), then all is OK

#### Windows and macOS

IfcOpenShell is included in both the FreeCAD release and developer builds so
no additional steps are necessary.

### Links

Tutorial [Import/Export IFC - compiling IfcOpenShell](/Import/Export_IFC_-
_compiling_IfcOpenShell "Import/Export IFC - compiling IfcOpenShell")

## LazyLoader

LazyLoader is a Python module that allows deferred loading, while still
importing at the top of the script. This is useful if you are importing
another module that is slow, and it is used several times throughout the
script. Using LazyLoader can improve workbench startup times, but the module
will still need to be loaded on first use.

### Installation

LazyLoader is included with FreeCAD v0.19

### Usage

You will need to import LazyLoader, then change the import of whatever module
you want to be deferred.

    
    
    from lazy_loader.lazy_loader import LazyLoader
    Part = LazyLoader('Part', globals(), 'Part')
    

The variable Part is how the module is named in your script. You can replicate
"import Part as P" by changing the variable.

    
    
    P = LazyLoader('Part', globals(), 'Part')
    

You can also import a module from a package.

    
    
    utils = LazyLoader('PathScripts', globals(), 'PathScripts.PathUtils')
    

You can't import individual functions, just entire modules.

### Links

  * Original source: <https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/util/lazy_loader.py>
  * Further explanation: <https://wil.yegelwel.com/lazily-importing-python-modules/>
  * Code within the FreeCAD source code: <https://github.com/FreeCAD/FreeCAD/tree/master/src/3rdParty/lazy_loader>
  * Forum discussion: [https://forum.freecad.org/viewtopic.php?f=10&t=45298](https://forum.freecad.org/viewtopic.php?f=10&t=45298)

  

![](/images/6/6f/Arrow-left.svg) [Workbench creation](/Workbench_creation
"Workbench creation")

[Source documentation](/Source_documentation "Source documentation")
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

