---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_StateServer.htm
scraped_at: 2025-09-08T16:17:59.702073
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_StateServer Class](../html/T_Grasshopper_Kernel_GH_StateServer.htm
"GH_StateServer Class")

[GH_StateServer Constructor
](../html/M_Grasshopper_Kernel_GH_StateServer__ctor.htm "GH_StateServer
Constructor ")

[GH_StateServer
Properties](../html/Properties_T_Grasshopper_Kernel_GH_StateServer.htm
"GH_StateServer Properties")

[GH_StateServer
Methods](../html/Methods_T_Grasshopper_Kernel_GH_StateServer.htm
"GH_StateServer Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_StateServer Class  
  
---  
  
Maintains all the recorded states for this document.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[System.Collections.GenericList](https://docs.microsoft.com/dotnet/api/system.collections.generic.list-1)[GH_State](T_Grasshopper_Kernel_GH_State.htm)  
Grasshopper.KernelGH_StateServer  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_StateServer : List<GH_State>, 
    	GH_ISerializable
    
    
    Public Class GH_StateServer
    	Inherits List(Of GH_State)
    	Implements GH_ISerializable

The GH_StateServer type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_StateServer](M_Grasshopper_Kernel_GH_StateServer__ctor.htm)| Initializes a
new instance of the GH_StateServer class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Names](P_Grasshopper_Kernel_GH_StateServer_Names.htm)|  Gets a list of all
the state names in this server.  
![Public property](../icons/pubproperty.gif)|
[Owner](P_Grasshopper_Kernel_GH_StateServer_Owner.htm)|  Gets the document
that owns this server.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[NewStateFromDocument](M_Grasshopper_Kernel_GH_StateServer_NewStateFromDocument.htm)|
Displays UI for new state creation. If the user aborts, then null is returned.
If the user successfully defines a new state, it is appended to this server.  
![Public method](../icons/pubmethod.gif)|
[Read](M_Grasshopper_Kernel_GH_StateServer_Read.htm)|  
![Public method](../icons/pubmethod.gif)|
[RemoveState](M_Grasshopper_Kernel_GH_StateServer_RemoveState.htm)|  Remove a
certain state. This method adds an undo record to the document.  
![Public method](../icons/pubmethod.gif)| [RestoreState(Int32, Int32,
Int32)](M_Grasshopper_Kernel_GH_StateServer_RestoreState_1.htm)|  Restore a
certain state.  
![Public method](../icons/pubmethod.gif)| [RestoreState(String, Int32,
Int32)](M_Grasshopper_Kernel_GH_StateServer_RestoreState_2.htm)|  Restore a
certain state.  
![Public method](../icons/pubmethod.gif)| [RestoreState(Int32, Boolean, Int32,
Int32)](M_Grasshopper_Kernel_GH_StateServer_RestoreState.htm)|  Restore a
certain state.  
![Public method](../icons/pubmethod.gif)|
[Write](M_Grasshopper_Kernel_GH_StateServer_Write.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

