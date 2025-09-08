---
url: https://wiki.freecad.org/Source_documentation
title: Source documentation
scraped_at: 2025-09-08 16:45:24
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Overview
  * 2 Build source documentation Toggle Build source documentation subsection
    * 2.1 Complete documentation
    * 2.2 Reduced documentation
  * 3 Other versions
  * 4 Integrate Coin3D documentation
  * 5 Using Doxygen

# Source documentation

  * [Page](/Source_documentation "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Source_documentation&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Source_documentation)
  * [Edit](/index.php?title=Source_documentation&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Source_documentation&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Source_documentation.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Source_documentation&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Source_documentation)
  * [Edit](/index.php?title=Source_documentation&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Source_documentation&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Source_documentation&action=history)

General

  * [What links here](/Special:WhatLinksHere/Source_documentation "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Source_documentation "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Source_documentation&oldid=1597895 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Source_documentation&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Source_documentation&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Source+documentation&action=page&filter=&language=en)This is the approved
revision of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Source+documentation&language=&task=view "Start translation for this language")
  * [Deutsch](/Source_documentation/de "Quellendokumentation \(100% translated\)")
  * English
  * [Türkçe](/Source_documentation/tr "Source documentation \(3% translated\)")
  * [español](/Source_documentation/es "Documentación de Fuente \(77% translated\)")
  * [français](/Source_documentation/fr "Documentation du code source \(100% translated\)")
  * [hrvatski](/Source_documentation/hr "Dokumentacija Izvora \(3% translated\)")
  * [italiano](/Source_documentation/it "Documentazione del codice sorgente \(100% translated\)")
  * [polski](/Source_documentation/pl "Dokumentacja dla źródeł \(100% translated\)")
  * [português do Brasil](/Source_documentation/pt-br "Documentação do código-fonte \(74% translated\)")
  * [română](/Source_documentation/ro "Documentație \(3% translated\)")
  * [svenska](/Source_documentation/sv "Source documentation \(3% translated\)")
  * [русский](/Source_documentation/ru "Source documentation \(23% translated\)")
  * [中文（中国大陆）](/Source_documentation/zh-cn "Source documentation/zh-cn \(0% translated\)")
  * [日本語](/Source_documentation/ja "Source documentation/ja \(0% translated\)")

![](/images/6/6f/Arrow-left.svg) [Extra python modules](/Extra_python_modules
"Extra python modules")

[Contributors](/Contributors "Contributors") ![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

## Overview

The FreeCAD source code is commented to allow automatic programming
documentation generation using [Doxygen](/Doxygen "Doxygen"), a popular source
code documentation system. Doxygen can document both the C++ and Python parts
of FreeCAD, resulting in HTML pages with hyperlinks to each documented
function and class.

The documentation is hosted online at the [FreeCAD API
website](https://freecad.github.io/SourceDoc/). Please note that this
documentation may not always be up to date; if you need more details, download
FreeCAD's latest source code and compile the documentation yourself. If you
have pressing questions about the code please ask in the developer section of
the [FreeCAD forum](https://forum.freecad.org/index.php).

Compiling the API documentation follows the same general steps as compiling
the FreeCAD executable, as indicated in the [Compile on
Linux](/Compile_on_Linux "Compile on Linux") page.

[![](/images/7/7a/FreeCAD_documentation_compilation_workflow.svg)](/index.php?title=File:FreeCAD_documentation_compilation_workflow.svg&filetimestamp=20190720052653&)

General workflow to compile FreeCAD's programming documentation. The Doxygen
and Graphviz packages must be in the system, as well as the FreeCAD source
code itself. CMake configures the system so that with a single make
instruction the documentation for the the entire project is compiled into many
HTML files with diagrams.

## Build source documentation

### Complete documentation

If you have Doxygen installed, it is very easy to build the documentation.
Also install [Graphviz](https://www.graphviz.org/) to be able to produce
diagrams showing the relationships between different classes and libraries in
the FreeCAD code. Graphviz is also used by FreeCAD's [dependency
graph](/Std_DependencyGraph "Std DependencyGraph") to show the relationships
between different objects.

    
    
    sudo apt install doxygen graphviz
    

Then follow the same steps you would do to compile FreeCAD, as described on
the [compile on Linux](/Compile_on_Linux "Compile on Linux") page, and
summarized here for convenience.

  * Get the source code of FreeCAD and place it in its own directory `freecad-source`.
  * Create another directory `freecad-build` in which you will compile FreeCAD and its documentation.
  * Configure the sources with `cmake`, making sure you indicate the source directory, and specify the required options for your build.
  * Trigger the creation of the documentation using `make`.

    
    
    git clone https://github.com/FreeCAD/FreeCAD.git freecad-source
    mkdir freecad-build
    cd freecad-build
    cmake -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 ../freecad-source
    

While you are inside the build directory issue the following instruction to
create only the documentation.

    
    
    make -j$(nproc --ignore=2) DevDoc
    

As mentioned in [compiling (speeding up)](/Compiling_\(Speeding_up\)
"Compiling \(Speeding up\)"), the `-j` option sets the number of CPU cores
used for compilation. The resulting documentation files will appear in the
directory

    
    
    freecad-build/doc/SourceDocu/html/
    

The point of entrance to the documentation is the `index.html` file, which you
can open with a web browser:

    
    
    xdg-open freecad-build/doc/SourceDocu/html/index.html
    

The `DevDoc` target will generate a significant amount of data, around 5 GB of
new files, particularly due to the diagrams created by Graphviz.

### Reduced documentation

The complete documentation uses around 3Gb of disk space. An alternative,
smaller version of the documentation which takes only around 600 MB can be
generated with a different target. This is the version displayed on the
[FreeCAD API website](https://freecad.github.io/SourceDoc/).

    
    
    make -j$(nproc --ignore=2) WebDoc
    

The documentation on the [FreeCAD API
website](https://freecad.github.io/SourceDoc/) is produced automatically from
<https://github.com/FreeCAD/SourceDoc>. Anyone can rebuild it and submit a
pull request:

  * Fork the repo at <https://github.com/FreeCAD/SourceDoc>
  * on your machine: clone the FreeCAD code (if you haven't yet), create a build dir for the doc, and clone the above SourceDoc repo inside. That SourceDoc will be updated when you rebuild the doc, and you'll be able to commit & push the results afterwards:

    
    
    git clone https://github.com/FreeCAD/FreeCAD
    cd FreeCAD
    mkdir build
    cd build
    mkdir -p doc/SourceDocu/html
    cd doc/SourceDocu/html
    git clone your-fork-url
    cd ../../..
    cmake -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 ..
    make WebDoc
    cd doc/SourceDocu/html
    git commit
    git push
    

  * Go to your fork online, and create a pull request.

## Other versions

[FreeCAD 0.19 development](https://iesensor.com/FreeCADDoc/0.19/)
documentation built by
[qingfeng.xia](https://forum.freecad.org/viewtopic.php?t=12613).

## Integrate Coin3D documentation

On Unix systems it is possible to link Coin3D source documentation with
FreeCAD's. This allows for easier navigation and complete inheritance diagrams
for Coin derived classes.

  * Install the `libcoin-doc`, `libcoin80-doc`, or similarly named package.
  * Unpack the archive `coin.tar.gz` located in `/usr/share/doc/libcoin-doc/html`; the files may be already unpacked in your system.
  * Generate again the source documentation.

If you don't install the documentation package for Coin, the links will be
generated to access the online documentation at
[BitBucket](https://coin3d.bitbucket.io/Coin/). This will happen if a Doxygen
tag file can be downloaded at configure time with `wget`.

## Using Doxygen

See the [Doxygen](/Doxygen "Doxygen") page for an extensive explanation on how
to comment C++ and Python source code so that it can be processed by Doxygen
to automatically create the documentation.

Essentially, a comment block, starting with `/**` or `///` for C++, or `##`
for Python, needs to appear before every class or function definition, so that
it is picked up by Doxygen. Many [special commands](/Doxygen#Doxygen_markup
"Doxygen"), which start with `\` or `@`, can be used to define parts of the
code and format the output. [Markdown syntax](/Doxygen#Markdown_support
"Doxygen") is also understood within the comment block, which makes it
convenient to emphasize certain parts of the documentation.

    
    
    /**
     * Returns the name of the workbench object.
     */
    std::string name() const;
    
    /**
     * Set the name to the workbench object.
     */
    void setName(const std::string&);
    
    /// remove the added TaskWatcher
    void removeTaskWatcher(void);
    

  

![](/images/6/6f/Arrow-left.svg) [Extra python modules](/Extra_python_modules
"Extra python modules")

[Contributors](/Contributors "Contributors") ![](/images/a/af/Arrow-right.svg)

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

