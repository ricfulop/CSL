---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_PingDocumentEventArgs.htm
scraped_at: 2025-09-08T16:17:30.583847
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_PingDocumentEventArgs
Class](../html/T_Grasshopper_Kernel_GH_PingDocumentEventArgs.htm
"GH_PingDocumentEventArgs Class")

[GH_PingDocumentEventArgs Constructor
](../html/M_Grasshopper_Kernel_GH_PingDocumentEventArgs__ctor.htm
"GH_PingDocumentEventArgs Constructor ")

[GH_PingDocumentEventArgs
Properties](../html/Properties_T_Grasshopper_Kernel_GH_PingDocumentEventArgs.htm
"GH_PingDocumentEventArgs Properties")

[GH_PingDocumentEventArgs
Fields](../html/Fields_T_Grasshopper_Kernel_GH_PingDocumentEventArgs.htm
"GH_PingDocumentEventArgs Fields")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_PingDocumentEventArgs Class  
  
---  
  
Event arguments passed during PingDocument events.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[SystemEventArgs](https://docs.microsoft.com/dotnet/api/system.eventargs)  
Grasshopper.KernelGH_PingDocumentEventArgs  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_PingDocumentEventArgs : EventArgs
    
    
    Public Class GH_PingDocumentEventArgs
    	Inherits EventArgs

The GH_PingDocumentEventArgs type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_PingDocumentEventArgs](M_Grasshopper_Kernel_GH_PingDocumentEventArgs__ctor.htm)|
Initializes a new instance of the GH_PingDocumentEventArgs class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Document](P_Grasshopper_Kernel_GH_PingDocumentEventArgs_Document.htm)|  If
you're a GH_Document that owns this object, you must fill out this field. This
is the **only** way for objects to know which document they belong to.  
Top

![](../icons/SectionExpanded.png)Fields

| Name| Description  
---|---|---  
![Protected field](../icons/protfield.gif)|
[m_document](F_Grasshopper_Kernel_GH_PingDocumentEventArgs_m_document.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

