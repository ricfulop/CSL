---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_FontServer.htm
scraped_at: 2025-09-08T16:16:49.385743
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_FontServer Class](../html/T_Grasshopper_Kernel_GH_FontServer.htm
"GH_FontServer Class")

[GH_FontServer
Properties](../html/Properties_T_Grasshopper_Kernel_GH_FontServer.htm
"GH_FontServer Properties")

[GH_FontServer Methods](../html/Methods_T_Grasshopper_Kernel_GH_FontServer.htm
"GH_FontServer Methods")

[GH_FontServer Events](../html/Events_T_Grasshopper_Kernel_GH_FontServer.htm
"GH_FontServer Events")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_FontServer Class  
  
---  
  
Maintains a collection of standard fonts and mays to measure them.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.KernelGH_FontServer  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class GH_FontServer
    
    
    Public NotInheritable Class GH_FontServer

The GH_FontServer type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[Console](P_Grasshopper_Kernel_GH_FontServer_Console.htm)|
FontFamily.GenericMonospace, 10pt, regular  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[ConsoleAdjusted](P_Grasshopper_Kernel_GH_FontServer_ConsoleAdjusted.htm)|
FontFamily.GenericMonospace, 10pt, regular, adjusted to counter UI scaling.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[ConsoleSmall](P_Grasshopper_Kernel_GH_FontServer_ConsoleSmall.htm)|
FontFamily.GenericMonospace, 8pt, regular  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[ConsoleSmallAdjusted](P_Grasshopper_Kernel_GH_FontServer_ConsoleSmallAdjusted.htm)|
FontFamily.GenericMonospace, 8pt, regular, adjusted to counter UI scaling.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[FamilyConsole](P_Grasshopper_Kernel_GH_FontServer_FamilyConsole.htm)|  Gets
or sets the FontFamily used for monospaced fonts in Grasshopper.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[FamilyScript](P_Grasshopper_Kernel_GH_FontServer_FamilyScript.htm)|  Gets or
sets the FontFamily used for scripted fonts in Grasshopper.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[FamilyStandard](P_Grasshopper_Kernel_GH_FontServer_FamilyStandard.htm)|  Gets
or sets the FontFamily used for standard fonts in Grasshopper.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[Large](P_Grasshopper_Kernel_GH_FontServer_Large.htm)|
SystemFonts.CaptionFont, 10pt, bold  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[LargeAdjusted](P_Grasshopper_Kernel_GH_FontServer_LargeAdjusted.htm)|
SystemFonts.CaptionFont, 10pt, bold, adjusted for logical pixel size.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[Script](P_Grasshopper_Kernel_GH_FontServer_Script.htm)|
FontFamily.GenericSansSerif, 10pt, italic  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[ScriptSmall](P_Grasshopper_Kernel_GH_FontServer_ScriptSmall.htm)|
FontFamily.GenericSansSerif, 8pt, italic  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[Small](P_Grasshopper_Kernel_GH_FontServer_Small.htm)|
SystemFonts.CaptionFont, 6pt, regular  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[Standard](P_Grasshopper_Kernel_GH_FontServer_Standard.htm)|
SystemFonts.CaptionFont, 8pt, regular  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[StandardAdjusted](P_Grasshopper_Kernel_GH_FontServer_StandardAdjusted.htm)|
SystemFonts.CaptionFont, 8pt, regular, adjusted for logical pixel size.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[StandardBold](P_Grasshopper_Kernel_GH_FontServer_StandardBold.htm)|
SystemFonts.CaptionFont, 8pt, bold  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[StandardItalic](P_Grasshopper_Kernel_GH_FontServer_StandardItalic.htm)|
SystemFonts.CaptionFont, 8pt, italic  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[FontToString](M_Grasshopper_Kernel_GH_FontServer_FontToString.htm)|  Convert
a font to a string.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[MeasureString(String,
Font)](M_Grasshopper_Kernel_GH_FontServer_MeasureString.htm)|  Measure the
size of a string  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[MeasureString(String, Font,
SizeF)](M_Grasshopper_Kernel_GH_FontServer_MeasureString_1.htm)|  Measure the
size of a string  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[MeasureString(String, Font,
Single)](M_Grasshopper_Kernel_GH_FontServer_MeasureString_2.htm)|  Measure the
size of a string  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[NewFont(Font, FontStyle)](M_Grasshopper_Kernel_GH_FontServer_NewFont.htm)|
Safe font constructor.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[NewFont(Font, Single)](M_Grasshopper_Kernel_GH_FontServer_NewFont_1.htm)|
Safe font constructor.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[NewFont(FontFamily,
Single)](M_Grasshopper_Kernel_GH_FontServer_NewFont_3.htm)|  Safe font
constructor.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[NewFont(Font, Single,
FontStyle)](M_Grasshopper_Kernel_GH_FontServer_NewFont_2.htm)|  Safe font
constructor.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[NewFont(FontFamily, Single,
FontStyle)](M_Grasshopper_Kernel_GH_FontServer_NewFont_4.htm)|  Safe font
constructor.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[NewFont(String, Single,
FontStyle)](M_Grasshopper_Kernel_GH_FontServer_NewFont_5.htm)|  High level
function for Font creation. We've ran into loads of trouble in the past with
missing Fonts. _Never_ create a font directly via GDI+, _always_ use this
method.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[StringToFont](M_Grasshopper_Kernel_GH_FontServer_StringToFont.htm)|  Convert
a font description string back into a font.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[StringWidth(IEnumerableString,
Font)](M_Grasshopper_Kernel_GH_FontServer_StringWidth.htm)|  Measure the
maximum width of a collection of strings  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[StringWidth(String,
Font)](M_Grasshopper_Kernel_GH_FontServer_StringWidth_1.htm)|  Measure the
width of a string in pixels  
Top

![](../icons/SectionExpanded.png)Events

| Name| Description  
---|---|---  
![Public event](../icons/pubevent.gif)![Static member](../icons/static.gif)|
[ConsoleFamilyChanged](E_Grasshopper_Kernel_GH_FontServer_ConsoleFamilyChanged.htm)|
Raised whenever the MonospacedFamily is changed.  
![Public event](../icons/pubevent.gif)![Static member](../icons/static.gif)|
[ScriptFamilyChanged](E_Grasshopper_Kernel_GH_FontServer_ScriptFamilyChanged.htm)|
Raised whenever the ScriptFamily is changed.  
![Public event](../icons/pubevent.gif)![Static member](../icons/static.gif)|
[StandardFamilyChanged](E_Grasshopper_Kernel_GH_FontServer_StandardFamilyChanged.htm)|
Raised whenever the StandardFamily is changed.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

