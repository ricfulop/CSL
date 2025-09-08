---
url: https://wiki.freecad.org/Compile_on_Linux
title: Compile on Linux
scraped_at: 2025-09-08 16:45:13
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Overview
  * 2 Getting the source Toggle Getting the source subsection
    * 2.1 Git
  * 3 Getting the dependencies Toggle Getting the dependencies subsection
    * 3.1 Debian and Ubuntu
      * 3.1.1 Python 3 and Qt6
      * 3.1.2 Python 3 and Qt5
      * 3.1.3 OpenCascade kernel
      * 3.1.4 Optional packages
      * 3.1.5 Single command for Python 3 and Qt5
    * 3.2 Raspberry Pi
    * 3.3 Fedora
      * 3.3.1 Fedora40
      * 3.3.2 Fedora38/39
    * 3.4 Gentoo
    * 3.5 openSUSE
      * 3.5.1 Tumbleweed
      * 3.5.2 Leap
    * 3.6 Arch Linux
    * 3.7 Older and non-conventional distributions
    * 3.8 Pivy
    * 3.9 Debug symbols
  * 4 Compile FreeCAD Toggle Compile FreeCAD subsection
    * 4.1 Building
    * 4.2 Resolving cmake issues
    * 4.3 Compiling against GNU libc 2.34 and later
    * 4.4 How to repair your source code directory
    * 4.5 Configuration
      * 4.5.1 For a Debug build
      * 4.5.2 For a Release build
      * 4.5.3 Building against Python 3 and Qt5
      * 4.5.4 Building for a specific Python version
      * 4.5.5 Building with Qt Creator against Python 3 and Qt5
      * 4.5.6 Qt designer plugin
      * 4.5.7 External or internal Pivy
      * 4.5.8 Doxygen documentation
    * 4.6 Additional documentation
    * 4.7 Making a debian package
      * 4.7.1 *.deb package with checkinstall
  * 5 Updating the source code
  * 6 Uninstalling the source code
  * 7 Troubleshooting Toggle Troubleshooting subsection
    * 7.1 For 64 bit systems
  * 8 Automatic build scripts Toggle Automatic build scripts subsection
    * 8.1 Ubuntu
    * 8.2 openSUSE
    * 8.3 Debian Squeeze
    * 8.4 Fedora 27/28/29
    * 8.5 Arch using AUR

# Compile on Linux

  * [Page](/Compile_on_Linux "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Compile_on_Linux&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Compile_on_Linux)
  * [Edit](/index.php?title=Compile_on_Linux&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Compile_on_Linux&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Compile_on_Linux.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Compile_on_Linux&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Compile_on_Linux)
  * [Edit](/index.php?title=Compile_on_Linux&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Compile_on_Linux&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Compile_on_Linux&action=history)

General

  * [What links here](/Special:WhatLinksHere/Compile_on_Linux "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Compile_on_Linux "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Compile_on_Linux&oldid=1639179 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Compile_on_Linux&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Compile_on_Linux&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Compile+on+Linux&action=page&filter=&language=en)This is the approved revision
of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Compile+on+Linux&language=&task=view "Start translation for this language")
  * [Deutsch](/Compile_on_Linux/de "Kompilieren unter Linux \(90% translated\)")
  * English
  * [español](/Compile_on_Linux/es "Compilar en Linux \(66% translated\)")
  * [français](/Compile_on_Linux/fr "Compiler sous Linux \(100% translated\)")
  * [italiano](/Compile_on_Linux/it "Compilazione in Linux \(95% translated\)")
  * [polski](/Compile_on_Linux/pl "Kompilacja w systemie Linux \(100% translated\)")
  * [português](/Compile_on_Linux/pt "Compile on Linux/pt \(0% translated\)")
  * [português do Brasil](/Compile_on_Linux/pt-br "Compilar no Linux \(74% translated\)")
  * [română](/Compile_on_Linux/ro "Compile on Linux/ro \(0% translated\)")
  * [čeština](/Compile_on_Linux/cs "Compile on Linux/cs \(0% translated\)")
  * [български](/Compile_on_Linux/bg "Compile on Linux/bg \(0% translated\)")
  * [русский](/Compile_on_Linux/ru "Компиляция в Linux \(66% translated\)")
  * [日本語](/Compile_on_Linux/ja "Linuxでのコンパイル \(0% translated\)")
  * [한국어](/Compile_on_Linux/ko "Compile on Linux/ko \(0% translated\)")

![](/images/6/6f/Arrow-left.svg) [Compile on Windows](/Compile_on_Windows
"Compile on Windows")

[Compile on macOS](/Compile_on_MacOS "Compile on MacOS")
![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

There is an experimental FreeCAD Docker container that is being tested for
FreeCAD development. Read more about it at [Compile on
Docker](/Compile_on_Docker "Compile on Docker")

## Overview

Building FreeCAD on recent Linux distributions basically involves three steps:

  1. Getting the FreeCAD source code.
  2. Getting the dependencies of FreeCAD.
  3. Compiling FreeCAD

Below, you'll find detailed explanations of the whole process, some build
scripts, and particularities you might encounter. If you find anything wrong
or out of date in the text below (Linux distributions change often), or if you
use a distribution which is not listed, discuss the issue in the
[forum](https://forum.freecad.org/index.php), and help us correct it.

[![](/images/e/ed/FreeCAD_source_compilation_workflow.svg)](/index.php?title=File:FreeCAD_source_compilation_workflow.svg&filetimestamp=20200225195107&)

General workflow to compile FreeCAD from source. The third party dependencies
must be in the system, as well as the FreeCAD source code itself. CMake
configures the system so that with a single make instruction the entire
project is compiled.

## Getting the source

### Git

The best way to get the code is to clone the read-only [Git
repository](https://github.com/FreeCAD/FreeCAD) using the `git` program. It
can be easily installed on most Linux distributions.

For instance, on Debian related distributions, Git can be installed via the
following command:

    
    
    sudo apt install git
    

The following command will place a copy of the latest version of the FreeCAD
source code in a new directory called `freecad-source`.

    
    
    git clone --recurse-submodules https://github.com/FreeCAD/FreeCAD.git freecad-source
    

For more information on using Git and contributing code to the project, see
[Source code management](/Source_code_management "Source code management").

## Getting the dependencies

To compile FreeCAD you have to install the requisite dependencies mentioned in
[Third Party Libraries](/Third_Party_Libraries "Third Party Libraries"); the
packages that contain these dependencies are listed below for different Linux
distributions. Please note that the names and availability of the libraries
will depend on your particular distribution; if your distribution is old, some
packages may be unavailable or have a different name. In this case, look in
the older and non-conventional distributions section below.

Once you have all the dependencies installed, proceed to compile FreeCAD.

Please note that FreeCAD's source code is around 500 MB in size; it may be
three times as big if you clone the Git repository with its entire
modification history. Getting all dependencies may require downloading 500 MB
or more of new files; when these files are unpacked they may require 1500 MB
or more in space. Also beware that the compilation process may generate up to
1500 MB of additional files as the system copies and modifies the entire
source code. Therefore, be sure you have enough free space in your hard drive,
at least 4 GB, when attempting compilation.

Expand

### Debian and Ubuntu

On Debian-based systems (Debian, Ubuntu, Mint, etc.) it is quite easy to get
all needed dependencies installed. Most of the libraries are available via
`apt` or the Synaptic package manager.

If you already installed FreeCAD from the official repositories, you can
install its build dependencies with this single line of code in a terminal:

    
    
    sudo apt build-dep freecad
    

Alternatively, replace `freecad` with `freecad-daily` to install the build
dependencies for the main development branch. You'll need to have the
[freecad-stable/freecad-daily
PPAs](/Installing_on_Linux#Development_PPA_\(Daily\) "Installing on Linux")
added to your software sources.

However, if the version of FreeCAD in the repositories is old, the
dependencies may be the wrong ones to compile a recent version of FreeCAD.
Therefore, please verify that you have installed the following packages.

These packages are essential for any sort of compilation to succeed:

  * `build-essential`, installs the C and C++ compilers, the C development libraries, and the `make` program.
  * `cmake`, essential tool to configure the source of FreeCAD. You may also wish to install `cmake-gui` and `cmake-curses-gui` for a graphical option.
  * `libtool`, essential tools to produce shared libraries.
  * `lsb-release`, the standard base reporting utility is normally already installed in a Debian system, and allows you to programmatically distinguish between a pure Debian installation or a variant, such as Ubuntu or Linux Mint. Do not remove this package, as many other system packages may depend on it.

Compilation of FreeCAD uses the Python language, and it's also used at runtime
as a scripting language. If you are using a Debian based distribution the
Python interpreter is normally already installed.

  * `python3`
  * `swig`, the tool that creates interfaces between C++ code and Python.

The Boost libraries need to be installed:

  * `libboost-dev`
  * `libboost-date-time-dev`
  * `libboost-filesystem-dev`
  * `libboost-graph-dev`
  * `libboost-iostreams-dev`
  * `libboost-program-options-dev`
  * `libboost-python-dev`
  * `libboost-regex-dev`
  * `libboost-serialization-dev`
  * `libboost-thread-dev`

The Coin libraries need to be installed:

  * `libcoin-dev`, for Debian Buster, Ubuntu 19.04 and newer, as well as for Ubuntu 18.04/18.10 with the [freecad-stable/freecad-daily PPAs](/Installing_on_Linux#Development_PPA_\(Daily\) "Installing on Linux") added to your software sources.

Several libraries that deal with mathematics, triangulated surfaces, sorting,
meshes, computer vision, cartographic projections, 3D visualization, Point
Cloud Libraries, the X11 Window system, XML parsing, and Zip file reading:

  * `libeigen3-dev`
  * `libgts-bin`
  * `libgts-dev`
  * `libkdtree++-dev`
  * `libmedc-dev`
  * `libopencv-dev` or `libcv-dev`
  * `libproj-dev`
  * `libvtk9-dev`, `libvtk8-dev`, `libvtk7-dev` or `libvtk6-dev`
  * `libx11-dev`
  * `libxerces-c-dev`
  * `libyaml-cpp-dev`
  * `libzipios++-dev`
  * `libpcl-dev`

  

#### Python 3 and Qt6

To compile FreeCAD for Debian Trixie install the following dependencies.

  * `pybind11-dev`
  * `qt6-base-dev`
  * `qt6-svg-dev`
  * `qt6-tools-dev`
  * `qt6-webengine-dev`
  * `libpyside6-dev`
  * `libshiboken6-dev`
  * `pyside6-tools`
  * `pyqt6-dev-tools`
  * `python3-dev`
  * `python3-matplotlib`
  * `python3-packaging`
  * `python3-pivy`
  * `python3-ply`
  * `python3-pyside6.qtcore`
  * `python3-pyside6.qtgui`
  * `python3-pyside6.qtnetwork`
  * `python3-pyside6.qtsvg`
  * `python3-pyside6.qtwebchannel`
  * `python3-pyside6.qtwebenginecore`
  * `python3-pyside6.qtwebenginequick`
  * `python3-pyside6.qtwebenginewidgets`
  * `python3-pyside6.qtwidgets`

#### Python 3 and Qt5

To compile FreeCAD for Debian Buster, Ubuntu 19.04 and newer, as well as
Ubuntu 18.04/18.10 with the [freecad-stable/freecad-daily
PPAs](/Installing_on_Linux#Development_PPA_\(Daily\) "Installing on Linux")
added to your software sources, install the following dependencies.

  * `qtbase5-dev`
  * `qttools5-dev`
  * `qt5-default` (if compiling 0.20 on a machine that still has Qt4)
  * `libqt5opengl5-dev`
  * `libqt5svg5-dev`
  * `qtwebengine5-dev`
  * `libqt5xmlpatterns5-dev`
  * `libqt5x11extras5-dev`
  * `libpyside2-dev`
  * `libshiboken2-dev`
  * `pyside2-tools`
  * `pyqt5-dev-tools`
  * `python3-dev`
  * `python3-matplotlib`
  * `python3-packaging`
  * `python3-pivy`
  * `python3-ply`
  * `python3-pyside2.qtcore`
  * `python3-pyside2.qtgui`
  * `python3-pyside2.qtsvg`
  * `python3-pyside2.qtwidgets`
  * `python3-pyside2.qtnetwork`
  * `python3-pyside2.qtwebengine`
  * `python3-pyside2.qtwebenginecore`
  * `python3-pyside2.qtwebenginewidgets`
  * `python3-pyside2.qtwebchannel`
  * `python3-pyside2uic` (not required on Ubuntu 20.04 and later)

#### OpenCascade kernel

The OpenCascade kernel is the core graphics library to create 3D shapes. It
exists in an official version OCCT, and a community version OCE. The community
version is no longer recommended, as it's outdated.

For Debian Buster and Ubuntu 18.10 and newer, as well as Ubuntu 18.04 with the
[freecad-stable/freecad-daily
PPAs](/Installing_on_Linux#Development_PPA_\(Daily\) "Installing on Linux")
added to your software sources, install the official packages.

  * `libocct*-dev`
    * `libocct-data-exchange-dev`
    * `libocct-draw-dev`
    * `libocct-foundation-dev`
    * `libocct-modeling-algorithms-dev`
    * `libocct-modeling-data-dev`
    * `libocct-ocaf-dev`
    * `libocct-visualization-dev`
  * `occt-draw`

For Debian Jessie, Stretch, Ubuntu 16.04 and newer, install the community
edition packages.

  * `liboce*-dev`
    * `liboce-foundation-dev`
    * `liboce-modeling-dev`
    * `liboce-ocaf-dev`
    * `liboce-ocaf-lite-dev`
    * `liboce-visualization-dev`
  * `oce-draw`

You may install the libraries individually, or using asterisk expansion.
Change `occ` for `oce` if you want to install the community libraries.

    
    
    sudo apt install libocct*-dev
    

#### Optional packages

Optionally you can also install these extra packages:

  * `libsimage-dev`, to make Coin support additional image file formats.
  * `doxygen` and `libcoin-doc` (or `libcoin80-doc` for older systems), if you intend to generate source code documentation.
  * `libspnav-dev`, for [3D input devices](/3D_input_devices "3D input devices") support, like the 3Dconnexion "Space Navigator" or "Space Pilot".
  * `checkinstall`, if you intend to register your installed files into your system's package manager, so you can uninstall it later.

#### Single command for Python 3 and Qt5

Requires Pyside2 available in Debian buster and the [freecad-stable/freecad-
daily PPAs](/Installing_on_Linux#Official_Ubuntu_repository "Installing on
Linux").

    
    
    sudo apt install cmake cmake-gui libboost-date-time-dev libboost-dev libboost-filesystem-dev libboost-graph-dev libboost-iostreams-dev libboost-program-options-dev libboost-python-dev libboost-regex-dev libboost-serialization-dev libboost-thread-dev libcoin-dev libeigen3-dev libgts-bin libgts-dev libkdtree++-dev libmedc-dev libocct-data-exchange-dev libocct-ocaf-dev libocct-visualization-dev libopencv-dev libproj-dev libpyside2-dev libqt5opengl5-dev libqt5svg5-dev qtwebengine5-dev libqt5x11extras5-dev libqt5xmlpatterns5-dev libshiboken2-dev libspnav-dev libvtk7-dev libx11-dev libxerces-c-dev libzipios++-dev occt-draw pyside2-tools python3-dev python3-matplotlib python3-packaging python3-pivy python3-ply python3-pyside2.qtcore python3-pyside2.qtgui python3-pyside2.qtsvg python3-pyside2.qtwidgets python3-pyside2.qtnetwork python3-pyside2.qtwebengine python3-pyside2.qtwebenginecore python3-pyside2.qtwebenginewidgets python3-pyside2.qtwebchannel python3-markdown python3-git python3-pyside2uic qtbase5-dev qttools5-dev swig libyaml-cpp-dev
    

NOTE: On some versions of Ubuntu and some versions of Qt, you will get an
error that python3-pyside2uic cannot be found -- on those systems you can
safely omit it. On Ubuntu 20.04 you will need to add `pyqt5-dev-tools`. More
information can be found in [this forum
discussion](https://forum.freecad.org/viewtopic.php?t=51324).

Expand

    
    
    sudo apt install cmake debhelper dh-exec dh-python libboost-date-time-dev libboost-dev libboost-filesystem-dev libboost-graph-dev libboost-iostreams-dev libboost-program-options-dev libboost-python-dev libboost-regex-dev libboost-serialization-dev libboost-thread-dev libcoin80-dev libeigen3-dev libgts-bin libgts-dev libkdtree++-dev libmedc-dev libocct-data-exchange-dev libocct-ocaf-dev libocct-visualization-dev libopencv-dev libproj-dev libpyside-dev libqt4-dev libqt4-opengl-dev libqtwebkit-dev libshiboken-dev libspnav-dev libvtk6-dev libx11-dev libxerces-c-dev libzipios++-dev lsb-release occt-draw pyside-tools python-dev python-matplotlib python-pivy python-ply swig
    

  
Ubuntu 16.04 users please see also the compilation discussion in the forum:
[Compile on Linux (Kubuntu): CMake can't find
VTK](https://forum.freecad.org/viewtopic.php?f=4&t=16292).

Expand

### Raspberry Pi

Follow the same steps as in Debian and Ubuntu.

There are problems reported when trying to compile in Raspberry PI OS 32-bit
with Python 3 and Qt5, but the combination Python 3 and Qt4 seems to work for
older versions of FreeCAD (with minor issues).

For newer versions of FreeCAD (>= 0.20) the compilation with Py3/Qt5 is
successful if the operating system installed is Raspberry Pi OS 64-bit or
Ubuntu 20.04.

Due to different issues with Qt, in Ubuntu 20.04 the normal PySide tools won't
be found.

    
    
    E: Unable to locate package python3-pyside2uic
    

In this case, we can install the packages from PyQt and create symbolic links
to the needed tools.

    
    
    sudo apt-get install pyqt5-dev
    sudo apt-get install pyqt5-dev-tools
    cd /usr/bin/
    ln -s pyrcc5 pyside2-rcc
    ln -s pyuic5 pyside2-uic
    

Now compilation may proceed.

    
    
    cd build/
    cmake ../ -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 -DUSE_PYBIND11=ON
    make -j2
    

The `-j` option to `make` should not be more than 3 because the Raspberry Pi
has limited memory. It will take several hours to compile, so it is better to
do it overnight.

More information, [FreeCAD and Raspberry Pi
4](https://forum.freecad.org/viewtopic.php?f=42&t=37458&start=160#p396652).

Expand

### Fedora

There is a bug in opencascade cmake files which results in cmake failing to
find the opencascade libraries on Fedora. This can easily be fixed by making
one minor change to the top level cmake file of opencascade installed on
Fedora. Details here: <https://bugzilla.redhat.com/show_bug.cgi?id=2083568>.

Near the top of the file OpenCASCADEConfig.cmake, change the following line to
use `REAL_PATH()`. This fixes a bug triggered by the use of a symlink from
`/lib` to `/usr/lib` of Fedora, which cmake script fails to handle correctly.
This is due to making narrow assumptions about where the include files are
usually found on Linux and not testing for a valid result.

This file is usually installed in
/usr/lib64/cmake/opencascade/OpenCASCADEConfig.cmake.

    
    
    get_filename_component (OpenCASCADE_INSTALL_PREFIX "${OpenCASCADE_INSTALL_PREFIX}" PATH)
    

change this to:

    
    
    file (REAL_PATH ${OpenCASCADE_INSTALL_PREFIX} OpenCASCADE_INSTALL_PREFIX)
    

This trivial change needs to be made inside the build directory once cmake has
been run and failed. Re-running cmake will then correctly detect the OCCT
libraries in the normal way.

#### Fedora40

Fedora allows concurrent installation of Qt5 and Qt6 libraries. Adding the Qt6
libraries relevant to FreeCAD can be done using dnf:

    
    
    dnf install python3-shiboken6 python3-shiboken6-devel python3-pyside6 python3-pyside6-devel\
     pyside6-tools qt6-qtsvg qt6-qtsvg-devel qt6-qttools-devel python3-pyqt6-devel
    

**BEWARE:** A new feature, PCL, was introduced in March 2025. This requires
two additional packages: pcl and pcl-devel. However, it fails to build on
Fedora when using Qt6 libraries. Add the following to the cmake command line
to disable this code.

    
    
    -DFREECAD_USE_PCL=Off
    

Some remote Google code for automatic testing of coding practice is now
included by default. If you do not want to include this external code, which
is subject to change without notice, use the cmake option:

    
    
    -DENABLE_DEVELOPER_TESTS=Off
    

The following cmake command should be suitable for Fedora 40 with Qt6:

    
    
    cmake -DCMAKE_BUILD_TYPE=Release -DFREECAD_QT_VERSION=6 -Wno-dev -DENABLE_DEVELOPER_TESTS=Off -DFREECAD_USE_PCL=Off  ../FreeCAD
    

Adjust the final directory to point to the FreeCAD source code directory.

#### Fedora38/39

Now install Python 3.11. This includes a notable change in how Python
initializes when running a program. As a result FreeCAD fails to find
OpenCamLib, meaning [3D Surface](/CAM_Surface "CAM Surface") and
[Waterline](/CAM_Waterline "CAM Waterline") are not available in the [CAM
Workbench](/CAM_Workbench "CAM Workbench"). This was fixed in the master
branch on 20th Mar 2024 ([Pull request
#13059](https://github.com/FreeCAD/FreeCAD/pull/13059)).

You need the following packages:

  * `gcc-c++` (or possibly another C++ compiler?)
  * `cmake`
  * `doxygen`
  * `swig`
  * `gettext`
  * `dos2unix`
  * `desktop-file-utils`
  * `libXmu-devel`
  * `freeimage-devel`
  * `mesa-libGLU-devel`
  * `opencascade-devel`
  * `openmpi-devel`
  * `python3`
  * `python3-devel`
  * `python3-pyside2`
  * `python3-pyside2-devel`
  * `pyside2-tools`
  * `boost-devel`
  * `tbb-devel`
  * `eigen3-devel`
  * `qt-devel`
  * `qt5-qtwebengine-devel`
  * `qt5-qtxmlpatterns`
  * `qt5-qtxmlpatterns-devel`
  * `qt5-qtsvg-devel`
  * `qt5-qttools-static`
  * `ode-devel`
  * `xerces-c`
  * `xerces-c-devel`
  * `opencv-devel`
  * `smesh-devel`
  * `Coin3`
  * `Coin3-devel`
  * `yaml-cpp`

(April 2021, Coin4 and Coin4-devel are available) (if coin2 is the latest
available for your version of Fedora, use packages from
<http://www.zultron.com/rpm-repo/>)

  * `SoQt-devel`
  * `freetype`
  * `freetype-devel`
  * `vtk`
  * `vtk-devel`
  * `med`
  * `med-devel`

And optionally:

  * `libspnav-devel` (for 3Dconnexion devices support like the Space Navigator or Space Pilot)
  * `python3-pivy` (<https://bugzilla.redhat.com/show_bug.cgi?id=458975> Pivy is not mandatory but needed for the Draft Workbench)
  * `python3-markdown` (for the Addon Manager to display native markdown)
  * `python3-GitPython` (for the Addon Manager to use git to checkout and update workbenches and macros)

To install all dependencies at once (tested on fedora 36 and 37):

    
    
    sudo dnf install gcc-c++ cmake doxygen swig gettext dos2unix desktop-file-utils libXmu-devel freeimage-devel mesa-libGLU-devel opencascade-devel openmpi-devel python3 python3-devel python3-pyside2 python3-pyside2-devel pyside2-tools boost-devel tbb-devel eigen3-devel qt-devel qt5-qtwebengine-devel qt5-qtxmlpatterns qt5-qtxmlpatterns-devel qt5-qtsvg-devel qt5-qttools-static ode-devel xerces-c xerces-c-devel opencv-devel smesh-devel Coin3 Coin3-devel SoQt-devel freetype freetype-devel vtk vtk-devel med med-devel libspnav-devel python3-pivy python3-markdown python3-GitPython yaml-cpp
    

Expand

### Gentoo

Easiest way to check which packages are needed to compile FreeCAD is to check
via portage:

`emerge -pv freecad`

This should give a nice list of extra packages that you need installed on your
system.

If FreeCAD is not available on portage, it is available on the [waebbl
overlay](https://github.com/waebbl/waebbl-gentoo). The issue tracker on the
waebbl overlay Github may help guide through some issues you may come across.
The overlay provides `freecad-9999`, which you can choose to compile, or
simply use to get the dependencies.

`layman -a waebbl`

Expand

### openSUSE

#### Tumbleweed

The following commands will install the packages required for building FreeCAD
with Qt5 and Python 3.

    
    
    zypper in --no-recommends -t pattern devel_C_C++ devel_qt5
    
    zypper in libqt5-qtbase-devel libqt5-qtsvg-devel libqt5-qttools-devel boost-devel swig libboost_program_options-devel libboost_mpi_python3-devel libboost_system-devel libboost_program_options-devel libboost_regex-devel libboost_python3-devel libboost_thread-devel libboost_system-devel libboost_headers-devel libboost_graph-devel python3 python3-devel python3-matplotlib python3-matplotlib-qt5 python3-pyside2 python3-pyside2-devel python3-pivy gcc gcc-fortran cmake occt-devel libXi-devel opencv-devel libxerces-c-devel Coin-devel SoQt-devel freetype2-devel eigen3-devel libode6 vtk-devel libmed-devel hdf5-openmpi-devel openmpi2-devel netgen-devel freeglut-devel libspnav-devel f2c doxygen dos2unix glew-devel yaml-cpp
    

The following command will install Qt Creator and the GNU Project Debugger.

    
    
    zypper in libqt5-creator gdb
    

If any packages are missing, then you can check the Tumbleweed
["FreeCAD.spec"](https://build.opensuse.org/package/view_file/openSUSE:Factory/FreeCAD/FreeCAD.spec)
file on the [Open Build
Service](https://build.opensuse.org/package/show/openSUSE:Factory/FreeCAD).

Also, check to see if there are any patches you need to apply (such as
[0001-find-openmpi2-include-
files.patch](https://build.opensuse.org/package/view_file/openSUSE:Factory/FreeCAD/0001-find-
openmpi2-include-files.patch)).

#### Leap

If there is a difference between the available packages on Tumbleweed and
Leap, then you can read the Leap
["FreeCAD.spec"](https://build.opensuse.org/package/view_file/openSUSE:Leap:15.0/FreeCAD/FreeCAD.spec)
file on the [Open Build Service](https://build.opensuse.org/) to determine the
required packages.

See [piano_jonas unofficial "Compile On openSUSE"
guide](https://forum.freecad.org/viewtopic.php?f=4&t=49726).

Expand

### Arch Linux

You will need the following libraries from the official repositories:

  * `boost`
  * `cmake`
  * `coin`
  * `curl`
  * `desktop-file-utils`
  * `eigen`
  * `gcc-fortran`
  * `git`
  * `glew`
  * `hicolor-icon-theme`
  * `jsoncpp`
  * `libspnav`
  * `med`
  * `nlohmann-json`
  * `opencascade`
  * `pybind11`
  * `pyside2-tools`
  * `pyside2`
  * `python-matplotlib`
  * `python-netcdf4`
  * `python-packaging`
  * `python-pivy`
  * `qt5-svg`
  * `qt5-tools`
  * `qt5-webengine`
  * `shared-mime-info`
  * `shiboken2`
  * `swig`
  * `utf8cpp`
  * `verdict`
  * `xerces-c`
  * `yaml-cpp`

    
    
    sudo pacman -S --needed --asdeps boost cmake coin curl desktop-file-utils eigen gcc-fortran git glew hicolor-icon-theme jsoncpp libspnav med nlohmann-json opencascade pybind11 python-matplotlib python-netcdf4 python-packaging python-pivy qt5-svg qt5-tools qt5-webengine shared-mime-info swig utf8cpp xerces-c yaml-cpp
    

FreeCAD currently uses QT5. This requires packages which have been moved from
the official repositories to the AUR. These packages will be compiled by
source and may take a long time depending on the available hardware.

    
    
    yay -S --needed --asdeps pyside2 pyside2-tools shiboken2
    

Expand

### Older and non-conventional distributions

On other distributions, we have very few feedback from users, so it might be
harder to find the required packages.

Try first locating the required libraries mentioned in [third party
libraries](/Third_Party_Libraries "Third Party Libraries") in your package
manager. Beware that some of them might have a slightly different package
name; search for `name`, but also `libname`, `name-dev`, `name-devel`, and
similar. If that is not possible try compiling those libraries yourself.

FreeCAD requires the GNU g++ compiler version equal or above 3.0.0, as FreeCAD
is mostly written in C++. During the compilation some Python scripts are
executed, so the Python interpreter has to work properly. To avoid any linker
problems it is also a good idea to have the library paths in the
`LD_LIBRARY_PATH` variable or in the `ld.so.conf` file. This is already done
in modern Linux distributions, but may need to be set in older ones.

### Pivy

[Pivy](/Pivy "Pivy") (Python wrappers to Coin3d) is not needed to build
FreeCAD or to start it, but it is needed as a runtime dependency by the [Draft
Workbench](/Draft_Workbench "Draft Workbench"). If you are not going to use
this workbench, you won't need Pivy. However, do notice that the Draft
Workbench is used internally by other workbenches, like the
[BIM](/BIM_Workbench "BIM Workbench"), so Pivy needs to be installed to use
these workbenches as well.

By November 2015 the obsolete version of Pivy included with the FreeCAD source
code will no longer compile on many systems. This isn't a big problem as
normally you should get Pivy from your distribution's package manager; if you
cannot find Pivy, you may have to compile it yourself, see [Pivy compilation
instructions](/Extra_python_modules#Pivy "Extra python modules").

### Debug symbols

In order to troubleshoot crashes in FreeCAD, it is useful to have the debug
symbols of important dependency libraries such as Qt. For this, try installing
the dependency packages that end with `-dbg`, `-dbgsym`, `-debuginfo` or
similar, depending on your Linux distribution.

For Ubuntu, you may have to enable special repositories to be able to see and
install these debug packages with the package manager. See [Debug Symbol
Packages](https://wiki.ubuntu.com/Debug_Symbol_Packages) for more information.

## Compile FreeCAD

Building FreeCAD 0.20 requires at least Python3.6 and Qt 5.9.

FreeCAD uses CMake as its main build system, as it's available on all major
operating systems. Compiling with CMake is usually very simple and happens in
two steps.

  1. CMake checks that every needed program and library is present on your system, and generates a `Makefile` that is configured for the second step. FreeCAD has several configuration options to choose from, but it comes with sensible defaults. Some alternatives are detailed below.
  2. The compilation itself, which is done with the program `make`, which generates the FreeCAD executables.

Since FreeCAD is a large application, compiling the entire source code can
take anywhere from 10 minutes to one hour, depending on your CPU and the
number of CPU cores used for compilation.

### Building

To build simply create a build directory, `build`. Then from this build
directory point `cmake` to the right source folder. You can use `cmake-gui` or
`ccmake` instead of `cmake` in the instructions below as well. Once `cmake`
finishes configuring the environment, use `make` to start the actual
compilation.

    
    
    # from your freecad-source folder:
    mkdir build
    cd build
    cmake ../
    make -j$(nproc --ignore=2)
    

The `-j` option of `make` controls how many jobs (files) are compiled in
parallel. The `nproc` program prints the number of CPU cores in your system;
by using it together with the `-j` option you can choose to process as many
files as you have cores, in order to speed up overall compilation of the
program. In the example above, it will use all cores in your system except
two; this will keep your computer responsive for other uses while compilation
proceeds in the background. The FreeCAD executable will eventually appear in
the `build/bin` directory. See also [Compiling (speeding
up)](/Compiling_\(Speeding_up\) "Compiling \(Speeding up\)") to improve
compilation speed.

### Resolving cmake issues

If you have done a build before and get stuck on a dependency that is not
recognized or can't seem to be resolved, try the following:

  * Delete the contents of the build directory before running cmake again. FreeCAD is a rapidly moving target, you may be tripping over cached cmake information that points at an older version than the new repository head can use. Clearing the cache may allow cmake to recover and recognize the version you actually need.

  * If cmake complains about missing a specific file, use a tool such as "apt-file search", or its equivalent in other package systems, to discover what package that file belongs to and install it. Bear in mind that you are likely to need the -dev version of the package that carries header or config files files required for FreeCAD to use the package.

### Compiling against GNU libc 2.34 and later

GNU libc 2.34 introduces a change to the library that can cause builds on some
Linux systems to fail with an error like:

    
    
    No rule to make target '/usr/lib/x86_64-linux-gnu/libdl.so
    

To resolve this, a symbolic link must be manually created from the (now empty)
system-installed libdl.so.* to the location your compiler says it is looking
for the file. For example (if the actual installed copy of libdl.so on your
system is /usr/lib/x86_64-linux-gnu/libdl.so.2):

    
    
    sudo ln -s /usr/lib/x86_64-linux-gnu/libdl.so.2 /usr/lib/x86_64-linux-gnu/libdl.so
    

Adapt the command for the structure of your system by searching for libdl.so*
and linking it to the appropriate location.

### How to repair your source code directory

If you accidentally performed a compilation inside the source code directory,
or added strange files, and would like to restore the contents to only the
original source code, you can perform the following steps.

    
    
    > .gitignore
    git clean -df
    git reset --hard HEAD
    

The first line clears the `.gitignore` file. This ensures that the following
clean and reset commands will affect everything in the directory and will not
ignore items matching the expressions in `.gitignore`. The second line deletes
all files and directories that are not tracked by the git repository; then the
last command will reset any changes to tracked files, including the first
command which cleared the `.gitignore` file.

If you do not clear the source directory, subsequent runs of `cmake` may not
capture new options to the system if the code changes.

### Configuration

By passing different options to `cmake`, you can change how FreeCAD is
compiled. The syntax is as follows.

    
    
    cmake -D <var>:<type>=<value> $SOURCE_DIR
    

Where `$SOURCE_DIR` is the directory that contains the source code. The
`<type>` may be omitted in most cases. The space after the `-D` option may
also be omitted.

For example, to avoid building the [FEM Workbench](/FEM_Workbench "FEM
Workbench"):

    
    
    cmake -D BUILD_FEM:BOOL=OFF ../
    cmake -DBUILD_FEM=OFF ../
    

All possible variables are listed in the `InitializeFreeCADBuildOptions.cmake`
file, located in the `cMake/FreeCAD_Helpers` directory. In this file, search
for the word `option` to get to the variables that can be set, and see their
default values.

    
    
    # ==============================================================================
    # =================   All the options for the build process    =================
    # ==============================================================================
    
    option(BUILD_FORCE_DIRECTORY "The build directory must be different to the source directory." OFF)
    option(BUILD_GUI "Build FreeCAD Gui. Otherwise you have only the command line and the Python import module." ON)
    option(FREECAD_USE_EXTERNAL_ZIPIOS "Use system installed zipios++ instead of the bundled." OFF)
    option(FREECAD_USE_EXTERNAL_SMESH "Use system installed smesh instead of the bundled." OFF)
    ...
    

Alternatively, use the command `cmake -LH` to list the current configuration,
and thus all variables that can be changed. You may also install and use
`cmake-gui` to launch a graphical interface showing all the variables that can
be modified. In the next sections we list some of the more relevant options
that you may want to use.

#### For a Debug build

Create a `Debug` build to troubleshoot crashes in FreeCAD. Beware that with
this build the [Sketcher](/Sketcher_Workbench "Sketcher Workbench") becomes
very slow with complex sketches.

    
    
    cmake -DPYTHON_EXECUTABLE=/usr/bin/python3 -DCMAKE_BUILD_TYPE=Debug ../
    

#### For a Release build

Create a `Release` build to test code that doesn't crash. A `Release` build
will run much faster than a `Debug` build.

    
    
    cmake -DPYTHON_EXECUTABLE=/usr/bin/python3 -DCMAKE_BUILD_TYPE=Release ../
    

#### Building against Python 3 and Qt5

FreeCAD is moving to Qt6 and will soon end support for Qt5 and
FREECAD_QT_VERSION set to "5".

For 0.20 and 0.21_dev:

    
    
    cmake ../
    

Note that when switching between 0.20 and the 0.21_dev builds, it may be
necessary to delete CMakeCache.txt prior to running cmake.

#### Building for a specific Python version

If the default `python` executable on your system isn't desirable, you can
choose another Python version by giving the path to a specific executable to
`cmake`:

    
    
    cmake -DPYTHON_EXECUTABLE=/usr/bin/python3 ../
    

If that doesn't work, you may have to define additional variables pointing to
the desired Python libraries and include directories:

    
    
    cmake -DPYTHON_EXECUTABLE=/usr/bin/python3.6 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python3.6m \
        -DPYTHON_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython3.6m.so \
        -DPYTHON_PACKAGES_PATH=/usr/lib/python3.6/site-packages/ \
        ../
    

It is possible to have several independent versions of Python in the same
system, so the locations and version numbers of your Python files will depend
on your particular Linux distribution. Use `python3 -V` to display the version
of Python that you are using currently; only the first two numbers are
necessary; for example, if the result is `Python 3.6.8`, you need to specify
the directories that relate to the 3.6 version. If you don't know the right
directories, try searching for them with the `locate` command.

    
    
    locate python3.6
    

You may use `python3 -m site` in a terminal to determine the `site-packages`
directory, or `dist-packages` for Debian systems.

Some components of FreeCAD, such as PySide, try to autodetect the most recent
Python version installed on your system, which might fail if it is different
from what you entered above. Adding the following cMake option might solve the
issue:

    
    
    -DPython3_FIND_STRATEGY=LOCATION
    

#### Building with Qt Creator against Python 3 and Qt5

1\. Launch Qt Creator.

2\. Click on **Open Project**.

3\. Navigate to the directory where the source code is, `freecad-source/`, and
choose the topmost `CMakeLists.txt` file.

4\. By selecting the file, it will automatically run `cmake` on it, but it may
fail if the appropriate options aren't correctly set.

5\. Go to **Projects → Build & Run → Imported Kit → Build → Build Settings →
CMake**. Set the appropriate build directory, `build/`.

6\. Set the appropriate variables in the Key-Value dialog, of types `String`
and `Bool`.

    
    
    PYTHON_EXECUTABLE=/usr/bin/python3
    

7\. If the variables do not load the project correctly, you may have to go to
**Projects → Manage Kits → Kits → Default (or Imported Kit or similar) → CMake
Configuration**. Then press Change, and add the appropriate configuration as
described above. You may have to add more variables about the Python paths, if
the system Python is not found.

    
    
    PYTHON_EXECUTABLE:STRING=/usr/bin/python3.7
    PYTHON_INCLUDE_DIR:STRING=/usr/include/python3.7m
    PYTHON_LIBRARY:STRING=/usr/lib/x86_64-linux-gnu/libpython3.7m.so
    PYTHON_PACKAGES_PATH:STRING=/usr/lib/python3.7/site-packages
    

7.1. Press Apply, then OK.

7.2. Make sure the rest of the options are correctly set, for example, **Qt
version** should be a present version installed in the system, like `Qt 5.9.5
in PATH (qt5)`.

Press Apply, then OK to close the configuration.

The `cmake` program should run automatically again, and it should fill the
entire Key-Value dialog with all the variables that can be configured.

8\. Go to **Projects → Build & Run → Imported Kit → Run → Run Settings → Run →
Run Configuration** and choose `FreeCADMain` to compile the graphical version
of FreeCAD, or `FreeCADMainCMD` to compile only the command line version.

9\. Finally, go to the menu **Build → Build Project "FreeCAD"**. If this is a
new compilation, it should take several minutes, inclusive hours, depending on
the number of processors that you have available.

#### Qt designer plugin

If you want to develop Qt code for FreeCAD, you'll need the Qt Designer plugin
that provides all custom widgets of FreeCAD.

Go into an auxiliary directory of the source code, then run `qmake` with the
indicated project file to create a `Makefile`; then run `make` to compile the
plugin.

    
    
    cd freecad-source/src/Tools/plugins/widget
    qmake plugin.pro
    make
    

If you are compiling for Qt5, make sure the `qmake` binary is the one for this
version, so that the resulting `Makefile` contains the necessary information
for Qt5.

    
    
    cd freecad-source/src/Tools/plugins/widget
    $QT_DIR/bin/qmake plugin.pro
    make
    

where `$QT_DIR` is the directory that stores Qt binary libraries, for example,
`/usr/lib/x86_64-linux-gnu/qt5`.

The library created is `libFreeCAD_widgets.so`, which needs to be copied to
`$QT_DIR/plugins/designer`.

    
    
    sudo cp libFreeCAD_widgets.so $QT_DIR/plugins/designer
    

#### External or internal Pivy

Previously, a version of Pivy was included in the source code of FreeCAD
(internal). If you wanted to use your system's copy of Pivy (external), you
needed to use `-DFREECAD_USE_EXTERNAL_PIVY=1`.

Using external Pivy became the default during development of FreeCAD 0.16,
therefore this option does not need to be set manually anymore.

#### Doxygen documentation

If you have Doxygen installed you can build the source code documentation. See
[source documentation](/Source_documentation "Source documentation") for
instructions.

### Additional documentation

The source code of FreeCAD is very extensive, and with CMake it's possible to
configure many options. Learning to use CMake fully may be useful to choose
the right options for your particular needs.

  * [CMake Reference Documentation](https://cmake.org/documentation/) by Kitware.
  * [How to Build a CMake-Based Project](https://preshing.com/20170511/how-to-build-a-cmake-based-project/) (blog) by Preshing on programming.
  * [Learn CMake's Scripting Language in 15 Minutes](https://preshing.com/20170522/learn-cmakes-scripting-language-in-15-minutes/) (blog) by Preshing on programming.

### Making a debian package

If you plan to build a Debian package out of the sources you need to install
certain packages first:

    
    
    sudo apt install dh-make devscripts lintian
    

Go to the FreeCAD directory and call

    
    
    debuild
    

Once the package is built, you can use `lintian` to check if the package
contains errors

    
    
    lintian freecad-package.deb
    

#### *.deb package with checkinstall

The Debian script `checkinstall` allows to create a *.deb package that can be
installed and removed with the standard `dpkg` commands. It may need to be
installed first (on Ubuntu use `sudo apt install checkinstall`). It's
interactive and asks for the required information providing helpful defaults.
During the process the package is installed and a *.deb file and a backup
archive are created.

It's a good idea to define a name and a short description for the package. The
name must be entered to uninstall it again and the desription will be listed
by `dpkg -l`. The default name "build" is not very informative.

Example:

    
    
    cd freecad-source/build
    cmake ..
    make
    sudo checkinstall                                  # e.g. name=freecad-test1
    

The result is a *.deb file in the build folder. `checkinstall` will install
the build by default. This is how you can install or uninstall it:

    
    
    cd freecad-source/build
    ls | grep freecad
            freecad-test1_20220814-1_amd64.deb
    sudo dpkg -i freecad-test1_20220814-1_amd64.deb   # install
    dkpg -l | grep freecad                            # find by name
    sudo dpkg -r freecad-test1                        # uninstall by name
    

## Updating the source code

The CMake system allows you to intelligently update the source code, and only
recompile what has changed, making subsequent compilations faster.

Move to the location where the FreeCAD source code was first downloaded, and
pull the new code:

    
    
    cd freecad-source
    git pull
    

Then move into the build directory where the code was compiled initially, and
run `cmake` specifying the present directory (denoted by a dot); then trigger
the re-compilation with `make`.

    
    
    cd build
    cmake ../
    make -j$(nproc --ignore=2)
    

## Uninstalling the source code

In case the compiled source code was installed with `sudo make install` (for
Debian) the files were copied to the /usr/local folder into several
subfolders. For uninstallation the file install_manifest.txt can be used. It
has been created into the build folder during compilation and contains all
installed files. As long as this file exists, the installation can be
uninstalled.

    
    
    cd freecad-source/build
    xargs sudo rm < install_manifest.txt
    

## Troubleshooting

### For 64 bit systems

When building FreeCAD for 64-bit there is a known issue with the OpenCASCADE
(OCCT) 64-bit package. To get FreeCAD running properly you might need to run
the `configure` script and set additional `CXXFLAGS`:

    
    
    ./configure CXXFLAGS="-D_OCC64"
    

For Debian based systems this option is not needed when using the pre-built
OpenCASCADE packages because these ones set the proper `CXXFLAGS` internally.

## Automatic build scripts

Here is all what you need for a complete build of FreeCAD. It's a one-script-
approach and works on a freshly installed Linux distribution. The commands
will ask for the root password for installation of packages and new online
repositories. These scripts should run on 32 and 64 bit versions. They are
written for different versions, but are also likely to run on a later version
with or without major changes.

If you have such a script for your preferred distribution, please discuss it
on the [FreeCAD
forum](https://forum.freecad.org/viewforum.php?f=21&sid=e3c22dca9da076fefb56b1d5c5fb3134)
so we can incorporate it.

Expand

### Ubuntu

These scripts provide a reliable way to install the correct set of
dependencies required to build and run FreeCAD on Ubuntu. They make use of the
Ubuntu personal package archives (PPA), and should work on any version of
Ubuntu targeted by the PPA. The [freecad-
daily](https://launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-
daily) PPA targets recent versions of Ubuntu, while the [freecad-
stable](https://launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-
stable) PPA targets officially supported versions of Ubuntu.

This script installs the daily compiled snapshot of FreeCAD and its
dependencies. It adds the daily repository, gets the dependencies to build
this version, and installs the required packages. Afterwards it proceeds to
pull the source code into a particular directory, creates a build directory
and changes into it, configures the compilation environment with `cmake`, and
finally builds the entire program with `make`. Save the script to a file, make
it executable, and run it, but don't use `sudo`; superuser privileges will be
asked only for selected commands.

    
    
    #!/bin/sh
    sudo add-apt-repository --enable-source ppa:freecad-maintainers/freecad-daily && sudo apt-get update
    sudo apt-get build-dep freecad-daily
    sudo apt-get install freecad-daily
    
    git clone --recurse-submodules https://github.com/FreeCAD/FreeCAD.git freecad-source
    mkdir freecad-source/build
    cd freecad-source/build
    cmake -DPYTHON_EXECUTABLE=/usr/bin/python3 -DFREECAD_USE_PYBIND11=ON ../
    make -j$(nproc --ignore=2)
    

If you wish, you can uninstall the pre-compiled version of FreeCAD (`freecad-
daily`) while leaving the dependencies in place, however, leaving this package
installed will allow the package manager to keep its dependencies up to date
as well; this is mostly useful if you intend to follow the development of
FreeCAD, and constantly update and compile the sources from the Git
repository.

The previous script assumes that you want to compile the latest version of
FreeCAD, so you are using the "daily" repository to get the dependencies.
However, you can instead get the build dependencies of the "stable" version
for your current Ubuntu release. If this is the case, replace the top part of
the previous script with the following instructions. For Ubuntu 12.04, omit
`--enable-source` from the command.

    
    
    #!/bin/sh
    sudo add-apt-repository --enable-source ppa:freecad-maintainers/freecad-stable && sudo apt-get update
    sudo apt-get build-dep freecad
    sudo apt-get install libqt5xmlpatterns5-dev   # Needed for 0.20; should go away on next packaging update 
    sudo apt-get install freecad
    

Once you install the `freecad` package from the `freecad-stable` repository,
it will supersede the FreeCAD executable that is available from the Universe
Ubuntu repository. The executable will be named simply `freecad`, and not
`freecad-stable`.

Expand

### openSUSE

No external repositories are needed to compile FreeCAD. However, there is an
incompatability with python3-devel which needs to be removed. FreeCAD can be
compiled from GIT

    
    
    # install needed packages for development
    sudo zypper install gcc cmake OpenCASCADE-devel libXerces-c-devel \
    python-devel libqt4-devel python-qt4 Coin-devel SoQt-devel boost-devel \
    libode-devel libQtWebKit-devel libeigen3-devel gcc-fortran git swig
     
    # create new dir, and go into it
    mkdir FreeCAD-Compiled 
    cd FreeCAD-Compiled
     
    # get the source
    git clone --recurse-submodules https://github.com/FreeCAD/FreeCAD.git free-cad
     
    # Now you will have a subfolder in this location called free-cad. It contains the source
     
    # make another dir for compilation, and go into it
    mkdir FreeCAD-Build1
    cd FreeCAD-Build1 
     
    # build configuration 
    cmake ../free-cad
     
    # build FreeCAD
    make
     
    # test FreeCAD
    cd bin
    ./FreeCAD -t 0
    

Since you are using git, next time you wish to compile you do not have to
clone everything, just pull from git and compile once more

    
    
    # go into free-cad dir created earlier
    cd free-cad
     
    # pull
    git pull
     
    # get back to previous dir
    cd ..
     
    # Now repeat last few steps from before.
     
    # make another dir for compilation, and go into it
    mkdir FreeCAD-Build2
    cd FreeCAD-Build2
     
    # build configuration 
    cmake ../free-cad
     
    # build FreeCAD
    # Note: to speed up build use all CPU cores: make -j$(nproc)
    make
     
    # test FreeCAD
    cd bin
    ./FreeCAD -t 0
    

Expand

### Debian Squeeze

    
    
    # get the needed tools and libs
    sudo apt-get install build-essential python libcoin60-dev libsoqt4-dev \
    libxerces-c2-dev libboost-dev libboost-date-time-dev libboost-filesystem-dev \
    libboost-graph-dev libboost-iostreams-dev libboost-program-options-dev \
    libboost-serialization-dev libboost-signals-dev libboost-regex-dev \
    libqt4-dev qt4-dev-tools python2.5-dev \
    libsimage-dev libopencascade-dev \
    libsoqt4-dev libode-dev subversion cmake libeigen2-dev python-pivy \
    libtool autotools-dev automake gfortran
     
    # checkout the latest source
    git clone --recurse-submodules https://github.com/FreeCAD/FreeCAD.git freecad
     
    # go to source dir
    cd freecad
     
    # build configuration 
    cmake .
     
    # build FreeCAD
    # Note: to speed up build use all CPU cores: make -j$(nproc)
    make
     
    # test FreeCAD
    cd bin
    ./FreeCAD -t 0
    

Expand

### Fedora 27/28/29

Posted by user
[[PrzemoF](https://forum.freecad.org/memberlist.php?mode=viewprofile&u=3666)]
in the forum.

    
    
    #!/bin/bash
    
    ARCH=$(arch)
    
    MAIN_DIR=FreeCAD
    BUILD_DIR=build
    
    #FEDORA_VERSION=27
    #FEDORA_VERSION=28
    FEDORA_VERSION=29
    
    PACKAGES="gcc cmake gcc-c++ boost-devel zlib-devel swig eigen3 qt-devel \
    shiboken shiboken-devel pyside-tools python-pyside python-pyside-devel xerces-c \
    xerces-c-devel OCE-devel smesh graphviz python-pivy python-matplotlib tbb-devel \
     freeimage-devel Coin3 Coin3-devel med-devel vtk-devel"
    
    FEDORA_29_PACKAGES="boost-python2 boost-python3 boost-python2-devel boost-python3-devel"
    
    if [ "$FEDORA_VERSION" = "29" ]; then
        PACKAGES="$PACKAGES $FEDORA_29_PACKAGES"
    fi
    
    echo "Installing packages required to build FreeCAD"
    sudo dnf -y install $PACKAGES
    cd ~
    mkdir $MAIN_DIR || { echo "~/$MAIN_DIR already exist. Quitting.."; exit; }
    cd $MAIN_DIR
    git clone --recurse-submodules https://github.com/FreeCAD/FreeCAD.git
    mkdir $BUILD_DIR || { echo "~/$BUILD_DIR already exist. Quitting.."; exit; }
    cd $BUILD_DIR
    cmake ../FreeCAD 
    make -j$(nproc)
    

Expand

### Arch using AUR

[Arch User Repository (AUR)](https://aur.archlinux.org/) is a collection user
made recipes to build packages which are not officially supported by
distribution maintainers / community. They are usually safe. You can see who
maintain the package and for how long he did. It is recommended to check
construction files. Also non open source software are available in this area
even if maintained by the official owning company.

Prerequisite : git

Steps :

  1. Open a terminal. Optionally create a directory eg. ` mkdir git`. Optionally change directory eg. `cd git`.
  2. Clone the AUR repository : `git clone <https://aur.archlinux.org/freecad-git.git>`
  3. Enter AUR repository folder : `cd freecad-git`
  4. Compile using [Arch makepkg](https://wiki.archlinux.org/index.php/Makepkg) : `makepkg -s`. The -s or --syncdeps flag will also install required dependencies.
  5. Install created package : `makepkg --install` or double click on the pkgname-pkgver.pkg.tar.xz inside your file browser.

To update FreeCAD to latest build just repeat from step 3. Update AUR
repository when there is some breaking change in the recipe or new features
using `git checkout -f` inside the folder.

  

![](/images/6/6f/Arrow-left.svg) [Compile on Windows](/Compile_on_Windows
"Compile on Windows")

[Compile on macOS](/Compile_on_MacOS "Compile on MacOS")
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

