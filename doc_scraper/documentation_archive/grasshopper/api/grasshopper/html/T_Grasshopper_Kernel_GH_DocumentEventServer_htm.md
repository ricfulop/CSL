---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_DocumentEventServer.htm
scraped_at: 2025-09-08T16:16:27.285251
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_DocumentEventServer
Class](../html/T_Grasshopper_Kernel_GH_DocumentEventServer.htm
"GH_DocumentEventServer Class")

[GH_DocumentEventServer Constructor
](../html/M_Grasshopper_Kernel_GH_DocumentEventServer__ctor.htm
"GH_DocumentEventServer Constructor ")

[GH_DocumentEventServer
Properties](../html/Properties_T_Grasshopper_Kernel_GH_DocumentEventServer.htm
"GH_DocumentEventServer Properties")

[GH_DocumentEventServer
Methods](../html/Methods_T_Grasshopper_Kernel_GH_DocumentEventServer.htm
"GH_DocumentEventServer Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_DocumentEventServer Class  
  
---  
  
RhinoCommon only event server.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.KernelGH_DocumentEventServer  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_DocumentEventServer : IGH_DebugDescription
    
    
    Public Class GH_DocumentEventServer
    	Implements IGH_DebugDescription

The GH_DocumentEventServer type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_DocumentEventServer](M_Grasshopper_Kernel_GH_DocumentEventServer__ctor.htm)|
Create and register a new event server.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Enabled](P_Grasshopper_Kernel_GH_DocumentEventServer_Enabled.htm)|  Gets or
sets the enabled state flag for this event watcher.  
![Public property](../icons/pubproperty.gif)|
[GuidTableRefCount](P_Grasshopper_Kernel_GH_DocumentEventServer_GuidTableRefCount.htm)|
Gets the number of stored ids in the Guid Table.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[AppendToDebugLog](M_Grasshopper_Kernel_GH_DocumentEventServer_AppendToDebugLog.htm)|  
![Public method](../icons/pubmethod.gif)|
[ClearGuidTable](M_Grasshopper_Kernel_GH_DocumentEventServer_ClearGuidTable.htm)|
Clear the entire ID table.  
![Public method](../icons/pubmethod.gif)|
[CreateGuidTable](M_Grasshopper_Kernel_GH_DocumentEventServer_CreateGuidTable.htm)|
Create the entire ID table from scratch.  
![Public method](../icons/pubmethod.gif)|
[EnsureGuidTable](M_Grasshopper_Kernel_GH_DocumentEventServer_EnsureGuidTable.htm)|
Create the entire ID table if it doesn't exist yet.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

