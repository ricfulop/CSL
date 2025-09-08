---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_GH_AsynchFileData.htm
scraped_at: 2025-09-08T16:12:13.215796
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH_AsynchFileData Class](../html/T_Grasshopper_GUI_GH_AsynchFileData.htm
"GH_AsynchFileData Class")

[GH_AsynchFileData Constructor
](../html/M_Grasshopper_GUI_GH_AsynchFileData__ctor.htm "GH_AsynchFileData
Constructor ")

[GH_AsynchFileData
Properties](../html/Properties_T_Grasshopper_GUI_GH_AsynchFileData.htm
"GH_AsynchFileData Properties")

[GH_AsynchFileData
Methods](../html/Methods_T_Grasshopper_GUI_GH_AsynchFileData.htm
"GH_AsynchFileData Methods")

[GH_AsynchFileData
Fields](../html/Fields_T_Grasshopper_GUI_GH_AsynchFileData.htm
"GH_AsynchFileData Fields")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_AsynchFileData Class  
  
---  
  
This class provides asynchronous methods to keep tabs on a file.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.GUIGH_AsynchFileData  

**Namespace:** [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_AsynchFileData : IDisposable
    
    
    Public Class GH_AsynchFileData
    	Implements IDisposable

The GH_AsynchFileData type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_AsynchFileData](M_Grasshopper_GUI_GH_AsynchFileData__ctor.htm)|
Asynchronous constructor. File properties will be loaded asychronously.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Callback](P_Grasshopper_GUI_GH_AsynchFileData_Callback.htm)|  Gets or sets
the callback delegate to be used when properties are updated.  
![Public property](../icons/pubproperty.gif)|
[FileCreated](P_Grasshopper_GUI_GH_AsynchFileData_FileCreated.htm)|  Gets the
date at which the file was created.  
![Public property](../icons/pubproperty.gif)|
[FileExists](P_Grasshopper_GUI_GH_AsynchFileData_FileExists.htm)|  Gets
whether the file exists. Note that this property returns false if
DataExists=False, regardless of whether the file exists.  
![Public property](../icons/pubproperty.gif)|
[FileLastChanged](P_Grasshopper_GUI_GH_AsynchFileData_FileLastChanged.htm)|
Gets the date at which the file was last changed.  
![Public property](../icons/pubproperty.gif)|
[FileSize](P_Grasshopper_GUI_GH_AsynchFileData_FileSize.htm)|  Gets the size
of the file.  
![Public property](../icons/pubproperty.gif)|
[FileThumbnail](P_Grasshopper_GUI_GH_AsynchFileData_FileThumbnail.htm)|  Gets
the thumbnail bitmap associated with the file.  
![Public property](../icons/pubproperty.gif)|
[HarvestThumbnail](P_Grasshopper_GUI_GH_AsynchFileData_HarvestThumbnail.htm)|
Gets or sets whether the thumbnail ought to be parsed. At the moment this only
makes sense for GH/GHX files.  
![Public property](../icons/pubproperty.gif)|
[IsFileData](P_Grasshopper_GUI_GH_AsynchFileData_IsFileData.htm)|  Gets
whether the data has been retrieved at least once.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[Dispose](M_Grasshopper_GUI_GH_AsynchFileData_Dispose.htm)| Releases all
resources used by the GH_AsynchFileData  
![Public method](../icons/pubmethod.gif)|
[UpdateProperties](M_Grasshopper_GUI_GH_AsynchFileData_UpdateProperties.htm)|
Updates all file properties on the thread on which this method is called.  
Top

![](../icons/SectionExpanded.png)Fields

| Name| Description  
---|---|---  
![Public field](../icons/pubfield.gif)|
[FilePath](F_Grasshopper_GUI_GH_AsynchFileData_FilePath.htm)|  Gets the
location this instance is watching.  
![Public field](../icons/pubfield.gif)|
[IsLocal](F_Grasshopper_GUI_GH_AsynchFileData_IsLocal.htm)|  Gets whether
Grasshopper thinks the file it is watching is on a local machine.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

