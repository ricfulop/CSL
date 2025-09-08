---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_ConnectivityDiagram.htm
scraped_at: 2025-09-08T16:15:53.138846
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_ConnectivityDiagram
Class](../html/T_Grasshopper_Kernel_GH_ConnectivityDiagram.htm
"GH_ConnectivityDiagram Class")

[GH_ConnectivityDiagram Constructor
](../html/Overload_Grasshopper_Kernel_GH_ConnectivityDiagram__ctor.htm
"GH_ConnectivityDiagram Constructor ")

[GH_ConnectivityDiagram
Properties](../html/Properties_T_Grasshopper_Kernel_GH_ConnectivityDiagram.htm
"GH_ConnectivityDiagram Properties")

[GH_ConnectivityDiagram
Methods](../html/Methods_T_Grasshopper_Kernel_GH_ConnectivityDiagram.htm
"GH_ConnectivityDiagram Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_ConnectivityDiagram Class  
  
---  
  
Represents a complete connectivity diagram (topology) of a GH_Document. A
connectivity diagram is basically an undirected network of all the wires in a
document.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.KernelGH_ConnectivityDiagram  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_ConnectivityDiagram
    
    
    Public Class GH_ConnectivityDiagram

The GH_ConnectivityDiagram type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_ConnectivityDiagram(GH_ConnectivityDiagram)](M_Grasshopper_Kernel_GH_ConnectivityDiagram__ctor.htm)|
Create a duplicate of another Connectivity Diagram.  
![Public method](../icons/pubmethod.gif)|
[GH_ConnectivityDiagram(GH_Document)](M_Grasshopper_Kernel_GH_ConnectivityDiagram__ctor_1.htm)|
Create a new Connectivity Diagram from a GH_Document.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Node](P_Grasshopper_Kernel_GH_ConnectivityDiagram_Node.htm)|  Get the
connectivity node with the specified ID.  
![Public property](../icons/pubproperty.gif)|
[NodeCount](P_Grasshopper_Kernel_GH_ConnectivityDiagram_NodeCount.htm)|  Gets
the number of connectivity nodes in this diagram.  
![Public property](../icons/pubproperty.gif)|
[Nodes](P_Grasshopper_Kernel_GH_ConnectivityDiagram_Nodes.htm)|  Gets a proxy
for all the Nodes in this diagram.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[ContainsID](M_Grasshopper_Kernel_GH_ConnectivityDiagram_ContainsID.htm)|
Test the diagram for a given Node ID.  
![Public method](../icons/pubmethod.gif)|
[GetAllInputs](M_Grasshopper_Kernel_GH_ConnectivityDiagram_GetAllInputs.htm)|
Get all the Nodes that are part of the specified node input.  
![Public method](../icons/pubmethod.gif)|
[GetAllOutputs](M_Grasshopper_Kernel_GH_ConnectivityDiagram_GetAllOutputs.htm)|
Get all the Nodes that are part of the specified node output.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

