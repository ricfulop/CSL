---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_SettingsServer.htm
scraped_at: 2025-09-08T16:17:51.667090
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_SettingsServer Class](../html/T_Grasshopper_Kernel_GH_SettingsServer.htm
"GH_SettingsServer Class")

[GH_SettingsServer Constructor
](../html/Overload_Grasshopper_Kernel_GH_SettingsServer__ctor.htm
"GH_SettingsServer Constructor ")

[GH_SettingsServer
Properties](../html/Properties_T_Grasshopper_Kernel_GH_SettingsServer.htm
"GH_SettingsServer Properties")

[GH_SettingsServer
Methods](../html/Methods_T_Grasshopper_Kernel_GH_SettingsServer.htm
"GH_SettingsServer Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_SettingsServer Class  
  
---  
  
A single instance of this class is maintained at module level under the
accessor "Settings".

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.KernelGH_SettingsServer  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class GH_SettingsServer : GH_ISerializable
    
    
    Public NotInheritable Class GH_SettingsServer
    	Implements GH_ISerializable

The GH_SettingsServer type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_SettingsServer(String)](M_Grasshopper_Kernel_GH_SettingsServer__ctor.htm)|
Create a new instance of the GH_SettingsServer class. The server will be
associated with a settings xml file in the %ApplicationData%\Grasshopper\
directory. If a file with the same name already exists, its settings will be
automatically loaded.  
![Public method](../icons/pubmethod.gif)| [GH_SettingsServer(String,
Boolean)](M_Grasshopper_Kernel_GH_SettingsServer__ctor_1.htm)|  Create a new
instance of the GH_SettingsServer class. The server will be associated with a
settings xml file in the %ApplicationData%\Grasshopper\ directory.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Count](P_Grasshopper_Kernel_GH_SettingsServer_Count.htm)|  Gets the total
number of settings stored in this database.  
![Public property](../icons/pubproperty.gif)|
[DatabaseName](P_Grasshopper_Kernel_GH_SettingsServer_DatabaseName.htm)|  Gets
the name of this settings database.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[Clear](M_Grasshopper_Kernel_GH_SettingsServer_Clear.htm)|  Destroy all
settings.  
![Public method](../icons/pubmethod.gif)|
[ConstainsEntry](M_Grasshopper_Kernel_GH_SettingsServer_ConstainsEntry.htm)|
Tests to see if a given entry is stored in this settings database.  
![Public method](../icons/pubmethod.gif)|
[DeleteValue](M_Grasshopper_Kernel_GH_SettingsServer_DeleteValue.htm)|  
![Public method](../icons/pubmethod.gif)|
[EntryNames](M_Grasshopper_Kernel_GH_SettingsServer_EntryNames.htm)|  Gets a
list of all the entry names in this settings.  
![Public method](../icons/pubmethod.gif)|
[EntryType](M_Grasshopper_Kernel_GH_SettingsServer_EntryType.htm)|  Gets the
type of a specific entry.  
![Public method](../icons/pubmethod.gif)| [GetValue(String,
Boolean)](M_Grasshopper_Kernel_GH_SettingsServer_GetValue.htm)|  
![Public method](../icons/pubmethod.gif)| [GetValue(String,
Byte)](M_Grasshopper_Kernel_GH_SettingsServer_GetValue_1.htm)|  
![Public method](../icons/pubmethod.gif)| [GetValue(String,
DateTime)](M_Grasshopper_Kernel_GH_SettingsServer_GetValue_2.htm)|  
![Public method](../icons/pubmethod.gif)| [GetValue(String,
Double)](M_Grasshopper_Kernel_GH_SettingsServer_GetValue_3.htm)|  
![Public method](../icons/pubmethod.gif)| [GetValue(String,
Color)](M_Grasshopper_Kernel_GH_SettingsServer_GetValue_4.htm)|  
![Public method](../icons/pubmethod.gif)| [GetValue(String,
Point)](M_Grasshopper_Kernel_GH_SettingsServer_GetValue_5.htm)|  
![Public method](../icons/pubmethod.gif)| [GetValue(String,
Rectangle)](M_Grasshopper_Kernel_GH_SettingsServer_GetValue_6.htm)|  
![Public method](../icons/pubmethod.gif)| [GetValue(String,
Size)](M_Grasshopper_Kernel_GH_SettingsServer_GetValue_7.htm)|  
![Public method](../icons/pubmethod.gif)| [GetValue(String,
Int32)](M_Grasshopper_Kernel_GH_SettingsServer_GetValue_8.htm)|  
![Public method](../icons/pubmethod.gif)| [GetValue(String,
String)](M_Grasshopper_Kernel_GH_SettingsServer_GetValue_9.htm)|  
![Public method](../icons/pubmethod.gif)|
[Read](M_Grasshopper_Kernel_GH_SettingsServer_Read.htm)|  Low-level
deserializer.  
![Public method](../icons/pubmethod.gif)|
[SetValue(String)](M_Grasshopper_Kernel_GH_SettingsServer_SetValue.htm)|  
![Public method](../icons/pubmethod.gif)| [SetValue(String,
Boolean)](M_Grasshopper_Kernel_GH_SettingsServer_SetValue_1.htm)|  
![Public method](../icons/pubmethod.gif)| [SetValue(String,
Byte)](M_Grasshopper_Kernel_GH_SettingsServer_SetValue_2.htm)|  
![Public method](../icons/pubmethod.gif)| [SetValue(String,
DateTime)](M_Grasshopper_Kernel_GH_SettingsServer_SetValue_3.htm)|  
![Public method](../icons/pubmethod.gif)| [SetValue(String,
Double)](M_Grasshopper_Kernel_GH_SettingsServer_SetValue_4.htm)|  
![Public method](../icons/pubmethod.gif)| [SetValue(String,
Color)](M_Grasshopper_Kernel_GH_SettingsServer_SetValue_5.htm)|  
![Public method](../icons/pubmethod.gif)| [SetValue(String,
Point)](M_Grasshopper_Kernel_GH_SettingsServer_SetValue_6.htm)|  
![Public method](../icons/pubmethod.gif)| [SetValue(String,
Rectangle)](M_Grasshopper_Kernel_GH_SettingsServer_SetValue_7.htm)|  
![Public method](../icons/pubmethod.gif)| [SetValue(String,
Size)](M_Grasshopper_Kernel_GH_SettingsServer_SetValue_8.htm)|  
![Public method](../icons/pubmethod.gif)| [SetValue(String,
Int32)](M_Grasshopper_Kernel_GH_SettingsServer_SetValue_9.htm)|  
![Public method](../icons/pubmethod.gif)| [SetValue(String,
String)](M_Grasshopper_Kernel_GH_SettingsServer_SetValue_10.htm)|  
![Public method](../icons/pubmethod.gif)|
[ShowSettingsBrowser](M_Grasshopper_Kernel_GH_SettingsServer_ShowSettingsBrowser.htm)|  
![Public method](../icons/pubmethod.gif)|
[Write](M_Grasshopper_Kernel_GH_SettingsServer_Write.htm)|  Low-level
serializer.  
![Public method](../icons/pubmethod.gif)|
[WritePersistentSettings](M_Grasshopper_Kernel_GH_SettingsServer_WritePersistentSettings.htm)|
Store all settings in the xml file now. You _must_ call this function if you
want the current settings to persist between sessions.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

