---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_ParamServerEventArgs.htm
scraped_at: 2025-09-08T16:17:22.517921
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_ParamServerEventArgs
Class](../html/T_Grasshopper_Kernel_GH_ParamServerEventArgs.htm
"GH_ParamServerEventArgs Class")

[GH_ParamServerEventArgs
Properties](../html/Properties_T_Grasshopper_Kernel_GH_ParamServerEventArgs.htm
"GH_ParamServerEventArgs Properties")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_ParamServerEventArgs Class  
  
---  
  
Arguments used in events for the GH_ComponentParamServer type.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[SystemEventArgs](https://docs.microsoft.com/dotnet/api/system.eventargs)  
Grasshopper.KernelGH_ParamServerEventArgs  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_ParamServerEventArgs : EventArgs
    
    
    Public Class GH_ParamServerEventArgs
    	Inherits EventArgs

The GH_ParamServerEventArgs type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[OriginalArguments](P_Grasshopper_Kernel_GH_ParamServerEventArgs_OriginalArguments.htm)|
Gets access to the original parameter event arguments.  
![Public property](../icons/pubproperty.gif)|
[Parameter](P_Grasshopper_Kernel_GH_ParamServerEventArgs_Parameter.htm)|  Gets
the parameter that caused the original event.  
![Public property](../icons/pubproperty.gif)|
[ParameterIndex](P_Grasshopper_Kernel_GH_ParamServerEventArgs_ParameterIndex.htm)|
Gets the index of the parameter that caused the original event.  
![Public property](../icons/pubproperty.gif)|
[ParameterSide](P_Grasshopper_Kernel_GH_ParamServerEventArgs_ParameterSide.htm)|
Gets the side of the parameter that caused the original event.  
![Public property](../icons/pubproperty.gif)|
[Server](P_Grasshopper_Kernel_GH_ParamServerEventArgs_Server.htm)|  Gets the
GH_ComponentParamServer object that raised the event.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

