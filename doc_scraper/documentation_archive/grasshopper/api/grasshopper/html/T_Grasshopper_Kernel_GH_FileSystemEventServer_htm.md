---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_FileSystemEventServer.htm
scraped_at: 2025-09-08T16:16:42.335565
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_FileSystemEventServer
Class](../html/T_Grasshopper_Kernel_GH_FileSystemEventServer.htm
"GH_FileSystemEventServer Class")

[GH_FileSystemEventServer
Properties](../html/Properties_T_Grasshopper_Kernel_GH_FileSystemEventServer.htm
"GH_FileSystemEventServer Properties")

[GH_FileSystemEventServer
Methods](../html/Methods_T_Grasshopper_Kernel_GH_FileSystemEventServer.htm
"GH_FileSystemEventServer Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_FileSystemEventServer Class  
  
---  
  
Provides a easy-to-use way to keep tabs on files.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.KernelGH_FileSystemEventServer  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class GH_FileSystemEventServer
    
    
    Public NotInheritable Class GH_FileSystemEventServer

The GH_FileSystemEventServer type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[AllPaths](P_Grasshopper_Kernel_GH_FileSystemEventServer_AllPaths.htm)|  Gets
a list of all the paths currently under surveillance.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[AddWatcher](M_Grasshopper_Kernel_GH_FileSystemEventServer_AddWatcher.htm)|
Add a new file watcher instance.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[RemoveWatcher(Object)](M_Grasshopper_Kernel_GH_FileSystemEventServer_RemoveWatcher.htm)|
Remove all watchers that are linked to a specific object.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[RemoveWatcher(Object,
String)](M_Grasshopper_Kernel_GH_FileSystemEventServer_RemoveWatcher_1.htm)|
Remove all watchers that are linked to a specific object and a specific file
path.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

