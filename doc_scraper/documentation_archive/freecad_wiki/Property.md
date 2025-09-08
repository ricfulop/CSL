---
url: https://wiki.freecad.org/Property
title: Property
scraped_at: 2025-09-08 16:42:47
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction
  * 2 All property types
  * 3 Scripting
  * 4 Source code

# Property

  * [Page](/Property "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Property&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Property)
  * [Edit](/index.php?title=Property&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Property&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Property.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Property&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Property)
  * [Edit](/index.php?title=Property&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Property&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Property&action=history)

General

  * [What links here](/Special:WhatLinksHere/Property "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Property "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Property&oldid=1597855 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Property&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Property&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Property&action=page&filter=&language=en)This is the approved revision of this
page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Property&language=&task=view "Start translation for this language")
  * [Bahasa Indonesia](/Property/id "Property \(5% translated\)")
  * [Deutsch](/Property/de "Objekteigenschaften \(79% translated\)")
  * English
  * [Türkçe](/Property/tr "Özellikler \(5% translated\)")
  * [español](/Property/es "Property \(100% translated\)")
  * [français](/Property/fr "Propriétés des objets \(100% translated\)")
  * [italiano](/Property/it "Proprietà degli oggetti \(100% translated\)")
  * [polski](/Property/pl "Właściwości \(100% translated\)")
  * [português](/Property/pt "Property \(5% translated\)")
  * [português do Brasil](/Property/pt-br "Propriedade \(26% translated\)")
  * [română](/Property/ro "Proprietăți \(5% translated\)")
  * [suomi](/Property/fi "Property \(5% translated\)")
  * [svenska](/Property/sv "Property \(5% translated\)")
  * [čeština](/Property/cs "Vlastnosti \(5% translated\)")
  * [русский](/Property/ru "Свойства \(11% translated\)")
  * [中文](/Property/zh "Property/zh \(0% translated\)")
  * [中文（中国大陆）](/Property/zh-cn "Property/zh-cn \(0% translated\)")
  * [日本語](/Property/ja "Property/プロパティ \(11% translated\)")

## Introduction

A property is a piece of information like a number or a text string that is
attached to a FreeCAD document or an object in a document. Public properties
can be viewed and modified in the [Property editor](/Property_editor "Property
editor").

Properties play a very important role in FreeCAD. As objects in FreeCAD are
"parametric", this means that their behavior is defined by their properties,
and how these properties are used as input for their class methods. See also
[FeaturePython Custom Properties](/FeaturePython_Custom_Properties
"FeaturePython Custom Properties") and [PropertyLink: InList and
OutList](/PropertyLink:_InList_and_OutList "PropertyLink: InList and OutList")

## All property types

Custom [scripted objects](/Scripted_objects "Scripted objects") can use any of
the property types defined in the base system:

Name | Unit (if any) | Remark   
---|---|---  
Acceleration | m/s^2   
AmountOfSubstance | mol   
Angle | °   
Area | m^2   
Bool |   
BoolList |   
Color |   
ColorList |   
CurrentDensity | A/m^2 | [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")  
Density | kg/m^3   
Direction |   
DissipationRate | m^2/s^3 | [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")  
Distance | m   
DynamicViscosity | Pa*s | [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")  
ElectricalCapacitance | F | [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")  
ElectricalConductance | S | [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")  
ElectricalConductivity | S/m | [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")  
ElectricalInductance | H | [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")  
ElectricalResistance | Ohm | [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")  
ElectricCharge | C | [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")  
ElectricCurrent | A | [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")  
ElectricPotential | V | [introduced in 0.20](/Release_notes_0.20 "Release notes 0.20")  
Enumeration |   
ExpressionEngine |   
File |   
FileIncluded |   
Float |   
FloatConstraint |   
FloatList |   
Font |   
Force | N   
Frequency | Hz   
HeatFlux | W/m^2 | [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")  
Integer |   
IntegerConstraint |   
IntegerList |   
IntegerSet |   
InverseArea | 1/m^2 | [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")  
InverseLength | 1/m | [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")  
InverseVolume | 1/m^3 | [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")  
KinematicViscosity | m^2/s | [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")  
Length | m   
Link |   
LinkChild |   
LinkGlobal |   
LinkHidden |   
LinkList |   
LinkListChild |   
LinkListGlobal |   
LinkListHidden |   
LinkSub |   
LinkSubChild |   
LinkSubGlobal |   
LinkSubHidden |   
LinkSubList |   
LinkSubListChild |   
LinkSubListGlobal |   
LinkSubListHidden |   
LuminousIntensity | cd | [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")  
MagneticFieldStrength | A/m | [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")  
MagneticFlux | Wb or V*s | [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")  
MagneticFluxDensity | T | [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")  
Magnetization | A/m | [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")  
Map |   
Mass | kg | [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")  
Material |   
MaterialList |   
Matrix |   
PartShape |  | a Part property, is accessed as  
`Part::PropertyPartShape`  
Path |   
Percent |   
PersistentObject |   
Placement |   
PlacementLink |   
PlacementList |   
Position |   
Power | W | [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")  
Precision |   
Pressure | Pa   
PythonObject |   
Quantity |   
QuantityConstraint |   
Rotation |   
ShearModulus | Pa | [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")  
SpecificEnergy | m^2/s^2 or J/kg | [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")  
SpecificHeat | J/kg/K | [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")  
Speed | m/s   
Stiffness | m/s^2   
Stress | Pa | [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")  
String |   
StringList |   
Temperature | K | [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")  
ThermalConductivity | W/m/K | [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")  
ThermalExpansionCoefficient | 1/K | [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")  
ThermalTransferCoefficient | W/m^2/K | [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")  
Time | s | [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")  
UltimateTensileStrength | Pa | [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")  
UUID |   
VacuumPermittivity | s^4*A^2 / (m^3*kg)   
Vector |   
VectorDistance |   
VectorList |   
Velocity | m/s | [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")  
Volume | l or m^3   
VolumeFlowRate | l/s or m^3/s | [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")  
VolumetricThermalExpansionCoefficient | 1/K | [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")  
Work | J | [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")  
XLink |   
XLinkList |   
XLinkSub |   
XLinkSubList |   
YieldStrength | Pa | [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")  
YoungsModulus | Pa | [introduced in 0.21](/Release_notes_0.21 "Release notes 0.21")  
  
Internally, the property name is prefixed with `App::Property`:

    
    
    App::PropertyBool
    App::PropertyFloat
    App::PropertyFloatList
    ...
    

Remember that these are property _types_. A single object may have many
properties of the same type, but with different names.

For example:

    
    
    obj.addProperty("App::PropertyFloat", "Length")
    obj.addProperty("App::PropertyFloat", "Width")
    obj.addProperty("App::PropertyFloat", "Height")
    

This indicates an object with three properties of type "Float", named
"Length", "Width", and "Height", respectively.

## Scripting

_See also:_ [FreeCAD scripting basics](/FreeCAD_Scripting_Basics "FreeCAD
Scripting Basics")

A [scripted object](/Scripted_objects "Scripted objects") is created first,
and then properties are assigned.

    
    
    obj = App.ActiveDocument.addObject("Part::Feature", "CustomObject")
    
    obj.addProperty("App::PropertyFloat", "Velocity", "Parameter", "Body speed")
    obj.addProperty("App::PropertyBool", "VelocityEnabled", "Parameter", "Enable body speed")
    

In general, _Data_ properties are assigned by using the object's
`addProperty()` method. On the other hand, _View_ properties are normally
provided automatically by the parent object from which the scripted object is
derived.

For example:

  * Deriving from `App::FeaturePython` provides only 4 _View_ properties: "Display Mode", "On Top When Selected", "Show In Tree", and "Visibility".
  * Deriving from `Part::Feature` provides 17 _View_ properties: the previous four, plus "Angular Deflection", "Bounding Box", "Deviation", "Draw Style", "Lighting", "Line Color", "Line Width", "Point Color", "Point Size", "Selectable", "Selection Style", "Shape Color", and "Transparency".

Nevertheless, _View_ properties can also be assigned using the view provider
object's `addProperty()` method.

    
    
    obj.ViewObject.addProperty("App::PropertyBool", "SuperVisibility", "Base", "Make the object glow")
    

## Source code

In the source code, properties are located in various src/App/Property* files.

They are imported and initialized in
`[src/App/Application.cpp](https://github.com/FreeCAD/FreeCAD/blob/9c27f1078e5ec516fe882aac1a27f5c6c6174554/src/App/Application.cpp#L1681-L1758)`.

    
    
    #include "Property.h"
    #include "PropertyContainer.h"
    #include "PropertyUnits.h"
    #include "PropertyFile.h"
    #include "PropertyLinks.h"
    #include "PropertyPythonObject.h"
    #include "PropertyExpressionEngine.h"
    

  

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

