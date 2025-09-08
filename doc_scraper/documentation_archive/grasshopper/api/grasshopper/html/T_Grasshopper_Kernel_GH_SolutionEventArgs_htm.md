---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_SolutionEventArgs.htm
scraped_at: 2025-09-08T16:17:53.664652
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_SolutionEventArgs
Class](../html/T_Grasshopper_Kernel_GH_SolutionEventArgs.htm
"GH_SolutionEventArgs Class")

[GH_SolutionEventArgs
Properties](../html/Properties_T_Grasshopper_Kernel_GH_SolutionEventArgs.htm
"GH_SolutionEventArgs Properties")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_SolutionEventArgs Class  
  
---  
  
Event arguments used for Document Solution events.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[SystemEventArgs](https://docs.microsoft.com/dotnet/api/system.eventargs)  
Grasshopper.KernelGH_SolutionEventArgs  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_SolutionEventArgs : EventArgs
    
    
    Public Class GH_SolutionEventArgs
    	Inherits EventArgs

The GH_SolutionEventArgs type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Document](P_Grasshopper_Kernel_GH_SolutionEventArgs_Document.htm)|  Gets the
document that raised the event, should be the same as the "sender" parameter
in the event handler.  
![Public property](../icons/pubproperty.gif)|
[Duration](P_Grasshopper_Kernel_GH_SolutionEventArgs_Duration.htm)|  Gets the
duration for this solution. The duration is a more accurate measure than
EndTime-StartTime.  
![Public property](../icons/pubproperty.gif)|
[StartTime](P_Grasshopper_Kernel_GH_SolutionEventArgs_StartTime.htm)|  Gets
the time when the current solution began.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

