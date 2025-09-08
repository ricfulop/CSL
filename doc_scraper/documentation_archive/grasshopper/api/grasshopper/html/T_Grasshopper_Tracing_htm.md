---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Tracing.htm
scraped_at: 2025-09-08T16:11:49.105622
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper](../html/N_Grasshopper.htm "Grasshopper")

[Tracing Class](../html/T_Grasshopper_Tracing.htm "Tracing Class")

[Tracing Methods](../html/Methods_T_Grasshopper_Tracing.htm "Tracing Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# Tracing Class  
  
---  
  
Class that provides useful static methods for debugging, tracing and
messaging.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
GrasshopperTracing  

**Namespace:** [Grasshopper](N_Grasshopper.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class Tracing
    
    
    Public NotInheritable Class Tracing

The Tracing type exposes the following members.

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Assert(Guid)](M_Grasshopper_Tracing_Assert.htm)|  Display a typical ASSERT
dialog with stack information.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Assert(Guid, Exception)](M_Grasshopper_Tracing_Assert_1.htm)|  Display a
typical assert dialog with stack information.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Assert(Guid, String)](M_Grasshopper_Tracing_Assert_2.htm)|  Display a typical
assert dialog with stack information.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Assert(Guid, String, Exception)](M_Grasshopper_Tracing_Assert_3.htm)|
Display a typical assert dialog with stack information.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[DebugLogAddEntry](M_Grasshopper_Tracing_DebugLogAddEntry.htm)|  Add a message
to the debug log. If the debug log doesn't exist yet, it will be created. This
function will only work if the Grasshopper window exists. This method is
threadsafe.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[DebugLogBeginBlock](M_Grasshopper_Tracing_DebugLogBeginBlock.htm)|  Start a
new block in the debug data. You _must_ end all your own blocks. This function
will only work if the Grasshopper window exists. This method is threadsafe.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[DebugLogEndBlock](M_Grasshopper_Tracing_DebugLogEndBlock.htm)|  Start a new
block in the debug data. You _must_ end all your own blocks. This function
will only work if the Grasshopper window exists. This method is threadsafe.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper Namespace](N_Grasshopper.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

