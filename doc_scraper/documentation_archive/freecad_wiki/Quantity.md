---
url: https://wiki.freecad.org/Quantity
title: Quantity
scraped_at: 2025-09-08 16:42:36
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 General Toggle General subsection
    * 1.1 Supported units
  * 2 Internal representation
  * 3 Units calculator
  * 4 InputField
  * 5 Python scripting Toggle Python scripting subsection
    * 5.1 Unit
    * 5.2 Quantity
    * 5.3 User facing values
    * 5.4 Precision
  * 6 Appendix Toggle Appendix subsection
    * 6.1 Parser supported units

# Quantity

  * [Page](/Quantity "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Quantity&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Quantity)
  * [Edit](/index.php?title=Quantity&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Quantity&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Quantity.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Quantity&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Quantity)
  * [Edit](/index.php?title=Quantity&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Quantity&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Quantity&action=history)

General

  * [What links here](/Special:WhatLinksHere/Quantity "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Quantity "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Quantity&oldid=1612850 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Quantity&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Quantity&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Quantity&action=page&filter=&language=en)This is the approved revision of this
page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Quantity&language=&task=view "Start translation for this language")
  * [Deutsch](/Quantity/de "Größe \(59% translated\)")
  * English
  * [français](/Quantity/fr "Quantity \(100% translated\)")
  * [italiano](/Quantity/it "Quantity \(57% translated\)")
  * [polski](/Quantity/pl "Ilość \(3% translated\)")
  * [čeština](/Quantity/cs "Veličina \(16% translated\)")
  * [русский](/Quantity/ru "Количество \(8% translated\)")

The quantity is a combination of a floating point number and a unit. It is
used throughout all of FreeCAD to handle parameters and all other kind of
input/output.

## General

In a CAD or CAE system it is very important to keep track of the unit of a
value. Lots of trouble can arise when mixing up units or calculating results
in different systems of units. One famous disaster is the [crash of the Mars
Climate
Orbiter](https://en.wikipedia.org/wiki/Mars_Climate_Orbiter#Cause_of_failure)
due to a unit mix-up. Even in the same system of units the units come in lots
of different flavours always tailored to the field of use. Simple examples are
e.g. velocity in km/h (cars), m/s (robotics) or mm/minute (milling). A CAD
system has to keep track of units reliably. Also it has to do calculations
with them and check on the right unit for special parameters.

For that reason the FreeCAD Quantity framework was created. It includes all
the code and objects to deal with units, unit calculations, user input,
conversion to other systems of units and the pretty output of units and
values. In the long run no parameter in FreeCAD should be just a number.

### Supported units

The FreeCAD input parser supports a bunch of units and systems of units.
FreeCAD supports the Greek letter 'µ' for micro but also accepts 'u' as a
replacement. A complete list of all supported units can be [found
here](/Expressions#Units "Expressions").

The detailed specifications you will find in the code:

  * [Quantity lexer](https://github.com/FreeCAD/FreeCAD/blob/main/src/Base/QuantityLexer.c)
  * [Quantity definitions](https://github.com/FreeCAD/FreeCAD/blob/main/src/Base/Quantity.cpp#l167)

## Internal representation

All physical units can be expressed as a combination of the seven [SI-
Units](https://en.wikipedia.org/wiki/International_System_of_Units):

[![](/images/thumb/4/4b/SI-Derived-Units.jpg/750px-SI-Derived-
Units.jpg)](/index.php?title=File:SI-Derived-
Units.jpg&filetimestamp=20131108155709&)

An easy way to express a unit is an integer array of size 7 (number of base
units) that defines what the unit is. The signature of the 7 base units are:

  * LENGTH: [1,0,0,0,0,0,0]
  * MASS: [0,1,0,0,0,0,0]
  * TIME: [0,0,1,0,0,0,0]
  * ELECTRIC CURRENT: [0,0,0,1,0,0,0]
  * THERMODYNAMIC TEMPERATURE: [0,0,0,0,1,0,0]
  * AMOUNT OF SUBSTANCE: [0,0,0,0,0,1,0]
  * LUMINOUS INTENSITY: [0,0,0,0,0,0,1]

Using these seven units we are then able to express all derived units defined
in [Guide for the Use of the International System of Units
(SI)](http://physics.nist.gov/cuu/pdf/sp811.pdf) and create new ones as needed
such as for instance:

  * MASS DENSITY: [-3,1,0,0,0,0,0]
  * AREA: [0,2,0,0,0,0,0]

Since angle is physically dimensionless, but nevertheless important to a CAD
system we add one more virtual unit for Angle. This makes a vector of 8 in the
FreeCAD unit signature.

## Units calculator

Often you are in need of converting values from one system of units to
another. For example you have old parameter tables with wired units. In these
cases FreeCAD offers a conversion tool called Units-Calculator which helps in
translating units.

Its description in detail is here: [Std_UnitsCalculator](/Std_UnitsCalculator
"Std UnitsCalculator")

## InputField

The InputField is a QLineEdit derived Qt widget to handle all kinds of user
interaction with quantities and parameters. It features the following
properties:

  * parsing arbitrary value/unit input
  * checking on the right unit (if given) and give the user feedback
  * special context menu for operations on quantities/values
  * history management (save the last used values)
  * save often needed values as shortcut in context menu
  * selecting values with mouse wheel and arrow keys (tbd)
  * selecting with middle mouse button and mouse move (tbd)
  * Python integration for usage in Python only dialogs (tbd)

The UnitsCalculator uses the InputField already.

Code:

  * [InputField.h](https://github.com/FreeCAD/FreeCAD/blob/main/src/Gui/InputField.h)
  * [InputField.cpp](https://github.com/FreeCAD/FreeCAD/blob/main/src/Gui/InputField.cpp)

## Python scripting

The Unit and Quantity system in FreeCAD is (as nearly everything) fully
accessibly via Python.

### Unit

The Unit class represents the fingerprint of any physical unit. As described
in the Basics section a vector of eight numbers is used to represent this
fingerprint. The Unit class allows the handling and calculation based on this
information.

    
    
    from FreeCAD import Units
    
    # creating a unit with certain signature
    Units.Unit(0,1)      # Mass     (kg)
    Units.Unit(1)        # Length   (mm)
    Units.Unit(-1,1,-2)  # Pressure (kg/mm*s^2)
    
    # using predefined constants
    Units.Unit(Units.Length)
    Units.Unit(Units.Mass)
    Units.Unit(Units.Pressure)
    
    # parsing unit out of a string
    Units.Unit('kg/(m*s^2)')    # Pressure
    Units.Unit('Pa')            # the same as combined unit Pascale
    Units.Unit('J')             # Joule (work,energy) mm^2*kg/(s^2)
    
    # you can use units from all supported systems of units
    Units.Unit('psi')           # imperial pressure
    Units.Unit('lb')            # imperial  mass
    Units.Unit('ft^2')          # imperial area
    
    # comparing units
    Units.Unit(0,1) == Unit(Units.Mass)
    
    # getting type of unit
    Units.Unit('kg/(m*s^2)').Type == 'Pressure'
    
    # calculating
    Units.Unit('kg') * Units.Unit('m^-1*s^-2') == Units.Unit('kg/(m*s^2)')
    

The unit is mainly used to describe a certain type of unit for a parameter.
Therefore a special property type in FreeCAD can pass a unit to check and
ensure the right unit. A unit and a float value is called quantity.

### Quantity

    
    
    from FreeCAD import Units
    
    # to create a quantity you need a value (float) and a unit
    Units.Quantity(1.0,Units.Unit(0,1))     # Mass       1.0 kg
    Units.Quantity(1.0,Units.Unit(1))       # Length    1.0 mm
    Units.Quantity(1.0,Units.Unit(-1,1,-2)) # Pressure  1.0 kg/mm*s^2
    Units.Quantity(1.0,Units.Pressure)      # Pressure  1.0 kg/mm*s^2
    
    # you can directly give a signature
    Units.Quantity(1.0,0,1)     # Mass       1.0 kg
    Units.Quantity(1.0,1)       # Length    1.0 mm
    Units.Quantity(1.0,-1,1,-2) # Pressure  1.0 kg/mm*s^2
    
    # parsing quantities out of a string
    Units.Quantity('1.0 kg/(m*s^2)') # Pressure
    Units.Quantity('1.0 Pa')         # the same as combined Unit Pascale
    Units.Quantity('1.0 J')          # Joule (Work,Energy) mm^2*kg/(s^2)
    
    # You can use a point or comma as float delimiter
    Units.Quantity('1,0 m')
    Units.Quantity('1.0 m')
    
    # you can use units from all supported systems of units
    Units.Quantity('1.0 psi')  # imperial pressure
    Units.Quantity('1.0 lb')   # imperial mass
    Units.Quantity('1.0 ft^2') # imperial area
    
    # the quantity parser can do calculations too
    Units.Quantity('360/5 deg')        # splitting circle 
    Units.Quantity('1/16 in')          # fractions
    Units.Quantity('5.3*6.3 m^2')      # calculating an area
    Units.Quantity('1/(log(2.3)/sin(pi)*3.4)+1.8e-3 m')
    Units.Quantity('1ft 3in')          # imperial style
    
    # and for sure calculation and comparison
    Units.Quantity('1 Pa') * Units.Quantity(2.0) == Units.Quantity('2 Pa')
    Units.Quantity('1 m') * Units.Quantity('2 m') == Units.Quantity('2 m^2')
    Units.Quantity('1 m') * Units.Quantity('2 ft') + Units.Quantity('2 mm^2')
    Units.Quantity('1 m') > Units.Quantity('2 ft')
    
    # accessing the components
    Units.Quantity('1 m').Value # get the number (always internal system (mm/kg/s))
    Units.Quantity('1 m').Unit  # get the unit
    Units.Quantity('1 m') == Units.Quantity( Units.Quantity('1 m').Value , Units.Quantity('1 m').Unit)
    
    # translating the value into other units than the internal system (mm/kg/s)
    Units.Quantity('1 km/h').getValueAs('m/s')                  # translate value
    Units.Quantity('1 m').getValueAs(2.45,1)                    # translation value and unit signature
    Units.Quantity('1 kPa').getValueAs(Units.Pascal)            # predefined standard units 
    Units.Quantity('1 MPa').getValueAs(Units.Quantity('N/m^2')) # a quantity
    

### User facing values

Normally in scripts you can use Quantity for all kinds of calculations and
checking, but there comes the time you have to output information to the user.
You could use getValueAs() to force a certain unit, but normally the user sets
his preferred unit-schema in the preferences. This unit-schema does all the
translations to the representation the user likes to see. At the moment there
are three schemes implemented:

  * 1: Internal (mm/kg/s)
  * 2: MKS (m/kg/s)
  * 3: US customary (in/lb)

There can be easily additional schemas implemented in the future...

The Quantity class has two options to use the actual schema translation:

    
    
    from FreeCAD import Units
    
    # Use the translated string:
    Units.Quantity('1m').UserString           # '1000 mm' in 1; '1 m' in 2; and '1.09361 yr' in 3
    

This does the job if you only need a string. But sometimes you need more
control, e.g. if you want to have a dialog button which dials up and down.
Then you need more information about the translation output. Therefore the
getUserPreferred() method of quantity is used:

    
    
    Units.Quantity('22 m').getUserPreferred() # gets a tuple:('22 m', 1000.0, 'm')
    Units.Quantity('2  m').getUserPreferred() # Tuple: ('2000 mm', 1.0, 'mm')
    

Here you get more information using a tuple (three items). You get the string
as before, plus the factor of the value and the raw string with only the unit
chosen by the translation schema. With this information you can implement a
much richer user interaction.

The code of the schema translation can be found here:

  * [Internal](https://github.com/FreeCAD/FreeCAD/blob/main/src/Base/UnitsSchemaInternal.cpp)
  * [MKS](https://github.com/FreeCAD/FreeCAD/blob/main/src/Base/UnitsSchemaMKS.cpp)
  * [Imperial](https://github.com/FreeCAD/FreeCAD/blob/main/src/Base/UnitsSchemaImperial1.cpp)

### Precision

The precision of quantities is within FreeCAD dialogs the number of decimals
specified [in the preferences](/Preferences_Editor#Units "Preferences
Editor"). To use this settings for your script (for example in dialogs), you
can get it with this code:

    
    
    import FreeCAD
    
    params = App.ParamGet("User parameter:BaseApp/Preferences/Units")
    params.GetInt('Decimals') # returns an int
    

## Appendix

### Parser supported units

Although all physical units can be described with the seven SI units, most of
the units used in technical areas are common combined units (like Pa = N/m^2
Pascal ). Therefore the units parser in FreeCAD supports lot of SI and
Imperial combined units. These units are defined in src/Base/QuantityParser.l
file and can be further expanded in the future.

    
    
    from FreeCAD import Units
    
     "nm"  = Units.Quantity(1.0e-6    ,Units.Unit(1));         // nano meter
     "µm"  = Units.Quantity(1.0e-3    ,Units.Unit(1));         // micro meter
     "mm"  = Units.Quantity(1.0       ,Units.Unit(1));         // milli meter
     "cm"  = Units.Quantity(10.0      ,Units.Unit(1));         // centi meter
     "dm"  = Units.Quantity(100.0     ,Units.Unit(1));         // deci meter
     "m"   = Units.Quantity(1.0e3     ,Units.Unit(1));         // meter
     "km"  = Units.Quantity(1.0e6     ,Units.Unit(1));         // kilo meter
     "l"   = Units.Quantity(1000000.0 ,Units.Unit(3));         // liter dm^3
                                                      
     "µg"  = Units.Quantity(1.0e-9    ,Units.Unit(0,1));       // micro gram
     "mg"  = Units.Quantity(1.0e-6    ,Units.Unit(0,1));       // milli gram
     "g"   = Units.Quantity(1.0e-3    ,Units.Unit(0,1));       // gram
     "kg"  = Units.Quantity(1.0       ,Units.Unit(0,1));       // kilo gram
     "t"   = Units.Quantity(1000.0    ,Units.Unit(0,1));       // ton
                                                      
     "s"   = Units.Quantity(1.0       ,Units.Unit(0,0,1));     // second (internal standard time)
     "min" = Units.Quantity(60.0      ,Units.Unit(0,0,1));     // minute
     "h"   = Units.Quantity(3600.0    ,Units.Unit(0,0,1));     // hour  
                                                      
     "A"   = Units.Quantity(1.0       ,Units.Unit(0,0,0,1));   // Ampere (internal standard electric current)
     "mA"  = Units.Quantity(0.001     ,Units.Unit(0,0,0,1));   // milli Ampere         
     "kA"  = Units.Quantity(1000.0    ,Units.Unit(0,0,0,1));   // kilo Ampere         
     "MA"  = Units.Quantity(1.0e6     ,Units.Unit(0,0,0,1));   // Mega Ampere         
                                                      
     "K"   = Units.Quantity(1.0       ,Units.Unit(0,0,0,0,1)); // Kelvin (internal standard thermodynamic temperature)
     "mK"  = Units.Quantity(0.001     ,Units.Unit(0,0,0,0,1)); // Kelvin         
     "µK"  = Units.Quantity(0.000001  ,Units.Unit(0,0,0,0,1)); // Kelvin         
    
     "mol" = Units.Quantity(1.0       ,Units.Unit(0,0,0,0,0,1)); // Mole (internal standard amount of substance)        
    
     "cd"  = Units.Quantity(1.0       ,Units.Unit(0,0,0,0,0,0,1)); // Candela (internal standard luminous intensity)        
    
     "deg" = Units.Quantity(1.0         ,Units.Unit(0,0,0,0,0,0,0,1)); // degree (internal standard angle)
     "rad" = Units.Quantity(180/M_PI    ,Units.Unit(0,0,0,0,0,0,0,1)); // radian         
     "gon" = Units.Quantity(360.0/400.0 ,Units.Unit(0,0,0,0,0,0,0,1)); // gon         
    
     "in"  = Units.Quantity(25.4        ,Units.Unit(1));       // inch
     "\""  = Units.Quantity(25.4        ,Units.Unit(1));       // inch
     "fo"  = Units.Quantity(304.8       ,Units.Unit(1));       // foot
     "'"   = Units.Quantity(304.8       ,Units.Unit(1));       // foot
     "th"  = Units.Quantity(0.0254      ,Units.Unit(1));       // thou
     "yd"  = Units.Quantity(914.4       ,Units.Unit(1));       // yard
    
     "lb"  = Units.Quantity(0.45359237   ,Units.Unit(0,1));    // pound
     "oz"  = Units.Quantity(0.0283495231 ,Units.Unit(0,1));    // ounce
     "st"  = Units.Quantity(6.35029318   ,Units.Unit(0,1));    // Stone
     "cwt" = Units.Quantity(50.80234544  ,Units.Unit(0,1));    // hundredweights
    

Expand[![](/images/thumb/8/8f/Power_user_hub.png/24px-
Power_user_hub.png)](/index.php?title=File:Power_user_hub.png&filetimestamp=20200511213015&)
[Power user documentation](/Power_users_hub "Power users hub")

  * **FreeCAD scripting:** [Python](/Python "Python"), [Introduction to Python](/Introduction_to_Python "Introduction to Python"), [Python scripting tutorial](/Python_scripting_tutorial "Python scripting tutorial"), [FreeCAD Scripting Basics](/FreeCAD_Scripting_Basics "FreeCAD Scripting Basics")

* * *

  * **Modules:** [Builtin modules](/Builtin_modules "Builtin modules"), [Units](/Units "Units"), Quantity
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

