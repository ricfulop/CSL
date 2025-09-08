---
url: https://wiki.freecad.org/Units
title: Units
scraped_at: 2025-09-08 16:42:32
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Examples
  * 2 Supported units
  * 3 See Also

# Units

  * [Page](/Units "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Units&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Units)
  * [Edit](/index.php?title=Units&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Units&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Units.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Units&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Units)
  * [Edit](/index.php?title=Units&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Units&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Units&action=history)

General

  * [What links here](/Special:WhatLinksHere/Units "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Units "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Units&oldid=1605964 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Units&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Units&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Units&action=page&filter=&language=en)This is the approved revision of this
page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Units&language=&task=view "Start translation for this language")
  * [Deutsch](/Units/de "Einheiten \(100% translated\)")
  * English
  * [español](/Units/es "Units \(29% translated\)")
  * [français](/Units/fr "Unités \(100% translated\)")
  * [italiano](/Units/it "Le unità di misura \(100% translated\)")
  * [polski](/Units/pl "Jednostki \(100% translated\)")
  * [português do Brasil](/Units/pt-br "Units \(14% translated\)")
  * [română](/Units/ro "Units/ro \(14% translated\)")
  * [svenska](/Units/sv "Units \(14% translated\)")
  * [čeština](/Units/cs "Units \(14% translated\)")
  * [русский](/Units/ru "Единицы Измерения \(100% translated\)")

Some reading about units:

  * [Metrology](http://en.wikipedia.org/wiki/Metrology)
  * [SI system](http://en.wikipedia.org/wiki/International_System_of_Units)
  * [Imperial units](http://en.wikipedia.org/wiki/Imperial_units)
  * [SI derived units](http://en.wikipedia.org/wiki/SI_derived_unit)
  * [angle units](http://en.wikipedia.org/wiki/Degree_%28angle%29)
  * [unit implemented in OCC](https://github.com/3drepo/occt/blob/master/src/UnitsAPI/Units.dat)

## Examples

    
    
    # -- some examples of the FreeCAD unit translation system --
    # make a shortcut for the examples
    pq = FreeCAD.Units.parseQuantity
    
    # 10 meters in internal numbers
    pq('10 m')
    
    # doing math
    pq('3/8 in')
    
    # combined stuff
    pq('100 km/h')
    
    # transfer to other units
    pq('100 km/h') / pq('m/s')
    
    # derived units (Ohm)
    pq('m^2*kg*s^-3*A^-2')
    
    # or
    pq('(m^2*kg)/(A^2*s^3)')
    
    # angles 
    pq('2*pi rad') # full circle
    
    # as gon
    pq('2*pi rad') / pq('gon')
    
    # more imperial
    pq('1ft (3+7/16)in')
    
    # or 
    pq('1\' (3+7/16)"') # the ' we have to escape because of python
    
    # trigonometry
    pq('sin(pi)')
    
    # Using translated units as parameters, this command will create a 50.8mm x 20mm x 10mm box
    b = Part.makeBox(pq('2in'), pq('2m')/100, 10)
    

## Supported units

A complete list of all supported units can be [found here](/Expressions#Units
"Expressions").

## See Also

  * The [Expressions](/Expressions#Units "Expressions") page for a list of all known units.
  * The documentation of [Quantity](/Quantity "Quantity").
  * The [Std UnitsCalculator](/Std_UnitsCalculator "Std UnitsCalculator") tool.

  

Expand[![](/images/thumb/8/8f/Power_user_hub.png/24px-
Power_user_hub.png)](/index.php?title=File:Power_user_hub.png&filetimestamp=20200511213015&)
[Power user documentation](/Power_users_hub "Power users hub")

  * **FreeCAD scripting:** [Python](/Python "Python"), [Introduction to Python](/Introduction_to_Python "Introduction to Python"), [Python scripting tutorial](/Python_scripting_tutorial "Python scripting tutorial"), [FreeCAD Scripting Basics](/FreeCAD_Scripting_Basics "FreeCAD Scripting Basics")

* * *

  * **Modules:** [Builtin modules](/Builtin_modules "Builtin modules"), Units, [Quantity](/Quantity "Quantity")
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

