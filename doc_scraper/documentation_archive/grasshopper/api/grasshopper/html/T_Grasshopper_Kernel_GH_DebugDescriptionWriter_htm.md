---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_DebugDescriptionWriter.htm
scraped_at: 2025-09-08T16:16:01.167508
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_DebugDescriptionWriter
Class](../html/T_Grasshopper_Kernel_GH_DebugDescriptionWriter.htm
"GH_DebugDescriptionWriter Class")

[GH_DebugDescriptionWriter Constructor
](../html/M_Grasshopper_Kernel_GH_DebugDescriptionWriter__ctor.htm
"GH_DebugDescriptionWriter Constructor ")

[GH_DebugDescriptionWriter
Properties](../html/Properties_T_Grasshopper_Kernel_GH_DebugDescriptionWriter.htm
"GH_DebugDescriptionWriter Properties")

[GH_DebugDescriptionWriter
Methods](../html/Methods_T_Grasshopper_Kernel_GH_DebugDescriptionWriter.htm
"GH_DebugDescriptionWriter Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_DebugDescriptionWriter Class  
  
---  
  
Writer object used to create debug logs.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.KernelGH_DebugDescriptionWriter  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_DebugDescriptionWriter
    
    
    Public Class GH_DebugDescriptionWriter

The GH_DebugDescriptionWriter type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_DebugDescriptionWriter](M_Grasshopper_Kernel_GH_DebugDescriptionWriter__ctor.htm)|
Initializes a new instance of the GH_DebugDescriptionWriter class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Depth](P_Grasshopper_Kernel_GH_DebugDescriptionWriter_Depth.htm)|  Gets the
depth of the current writer. Depth is represented by whitespace in front of
each line.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[CloseBlock](M_Grasshopper_Kernel_GH_DebugDescriptionWriter_CloseBlock.htm)|
Close the current block and decrease the depth by 1.  
![Public method](../icons/pubmethod.gif)|
[CreateBlock](M_Grasshopper_Kernel_GH_DebugDescriptionWriter_CreateBlock.htm)|
Begin a new block. This will increase the depth by 1. You _must_ call
CloseBlock() if you call this function.  
![Public method](../icons/pubmethod.gif)|
[CreateLog](M_Grasshopper_Kernel_GH_DebugDescriptionWriter_CreateLog.htm)|
Get a single string that represents the entire log so far.  
![Public method](../icons/pubmethod.gif)|
[WriteLine](M_Grasshopper_Kernel_GH_DebugDescriptionWriter_WriteLine.htm)|
Write a new blank line to the log.  
![Public method](../icons/pubmethod.gif)|
[WriteLine(String)](M_Grasshopper_Kernel_GH_DebugDescriptionWriter_WriteLine_1.htm)|
Write a new line to the log.  
![Public method](../icons/pubmethod.gif)| [WriteLine(String,
Object)](M_Grasshopper_Kernel_GH_DebugDescriptionWriter_WriteLine_2.htm)|
Write a new formatted line to the log.  
![Public method](../icons/pubmethod.gif)|
[WriteLogToFile](M_Grasshopper_Kernel_GH_DebugDescriptionWriter_WriteLogToFile.htm)|
Write the log to a text file.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

