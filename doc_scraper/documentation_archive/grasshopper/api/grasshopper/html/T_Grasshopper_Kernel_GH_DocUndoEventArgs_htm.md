---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_DocUndoEventArgs.htm
scraped_at: 2025-09-08T16:16:38.340116
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_DocUndoEventArgs
Class](../html/T_Grasshopper_Kernel_GH_DocUndoEventArgs.htm
"GH_DocUndoEventArgs Class")

[GH_DocUndoEventArgs
Properties](../html/Properties_T_Grasshopper_Kernel_GH_DocUndoEventArgs.htm
"GH_DocUndoEventArgs Properties")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_DocUndoEventArgs Class  
  
---  
  
These arguments are passed along with UndoStateChanged events on GH_Document.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[SystemEventArgs](https://docs.microsoft.com/dotnet/api/system.eventargs)  
Grasshopper.KernelGH_DocUndoEventArgs  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_DocUndoEventArgs : EventArgs
    
    
    Public Class GH_DocUndoEventArgs
    	Inherits EventArgs

The GH_DocUndoEventArgs type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Document](P_Grasshopper_Kernel_GH_DocUndoEventArgs_Document.htm)|  Gets the
document that raised the event.  
![Public property](../icons/pubproperty.gif)|
[Operation](P_Grasshopper_Kernel_GH_DocUndoEventArgs_Operation.htm)|  Gets the
type of undo operation that caused this event.  
![Public property](../icons/pubproperty.gif)|
[Record](P_Grasshopper_Kernel_GH_DocUndoEventArgs_Record.htm)|  Gets the
UndoRecord pertaining to this event. Not every Event type has a single record
associated with it so be sure to test for null.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

