---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_DocFilePathEventArgs.htm
scraped_at: 2025-09-08T16:16:05.198555
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_DocFilePathEventArgs
Class](../html/T_Grasshopper_Kernel_GH_DocFilePathEventArgs.htm
"GH_DocFilePathEventArgs Class")

[GH_DocFilePathEventArgs Constructor
](../html/M_Grasshopper_Kernel_GH_DocFilePathEventArgs__ctor.htm
"GH_DocFilePathEventArgs Constructor ")

[GH_DocFilePathEventArgs
Properties](../html/Properties_T_Grasshopper_Kernel_GH_DocFilePathEventArgs.htm
"GH_DocFilePathEventArgs Properties")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_DocFilePathEventArgs Class  
  
---  
  
These arguments are passed along with FilePathChanged events on GH_Document.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[SystemEventArgs](https://docs.microsoft.com/dotnet/api/system.eventargs)  
Grasshopper.KernelGH_DocFilePathEventArgs  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_DocFilePathEventArgs : EventArgs
    
    
    Public Class GH_DocFilePathEventArgs
    	Inherits EventArgs

The GH_DocFilePathEventArgs type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_DocFilePathEventArgs](M_Grasshopper_Kernel_GH_DocFilePathEventArgs__ctor.htm)|
Create a new instance of the GH_DocFilePathEventArgs class.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Document](P_Grasshopper_Kernel_GH_DocFilePathEventArgs_Document.htm)|  Gets
the document that raised this event.  
![Public property](../icons/pubproperty.gif)|
[NewFilePath](P_Grasshopper_Kernel_GH_DocFilePathEventArgs_NewFilePath.htm)|
Gets the new filepath, the one currently assigned to this document.  
![Public property](../icons/pubproperty.gif)|
[OldFilePath](P_Grasshopper_Kernel_GH_DocFilePathEventArgs_OldFilePath.htm)|
Gets the old filepath, prior to the change that triggered this event.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

