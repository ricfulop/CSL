---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_State.htm
scraped_at: 2025-09-08T16:17:58.721696
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_State Class](../html/T_Grasshopper_Kernel_GH_State.htm "GH_State Class")

[GH_State Constructor ](../html/Overload_Grasshopper_Kernel_GH_State__ctor.htm
"GH_State Constructor ")

[GH_State Properties](../html/Properties_T_Grasshopper_Kernel_GH_State.htm
"GH_State Properties")

[GH_State Methods](../html/Methods_T_Grasshopper_Kernel_GH_State.htm "GH_State
Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_State Class  
  
---  
  
Represents a single recorded document state. A state contains values for an
arbitrary set of objects inside the document.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.KernelGH_State  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_State : GH_ISerializable
    
    
    Public Class GH_State
    	Implements GH_ISerializable

The GH_State type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_State](M_Grasshopper_Kernel_GH_State__ctor.htm)| Initializes a new
instance of the GH_State class  
![Public method](../icons/pubmethod.gif)|
[GH_State(GH_State)](M_Grasshopper_Kernel_GH_State__ctor_1.htm)| Initializes a
new instance of the GH_State class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[DataGuid](P_Grasshopper_Kernel_GH_State_Data.htm)|  Gets the state data
stored under the specified ID  
![Public property](../icons/pubproperty.gif)|
[DataInt32](P_Grasshopper_Kernel_GH_State_Data_1.htm)|  Gets the state data
stored under the specified index  
![Public property](../icons/pubproperty.gif)|
[LastModified](P_Grasshopper_Kernel_GH_State_LastModified.htm)|  Gets the date
at which this state was last modified.  
![Public property](../icons/pubproperty.gif)|
[Name](P_Grasshopper_Kernel_GH_State_Name.htm)|  Gets or sets the name of this
state.  
![Public property](../icons/pubproperty.gif)|
[StateCount](P_Grasshopper_Kernel_GH_State_StateCount.htm)|  Gets the number
of items stored in the state database.  
![Public property](../icons/pubproperty.gif)|
[StateData](P_Grasshopper_Kernel_GH_State_StateData.htm)|  Gets a pointer to
the internal database of states.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[AddStateObject](M_Grasshopper_Kernel_GH_State_AddStateObject.htm)|  Append a
new object to the database.  
![Public method](../icons/pubmethod.gif)|
[ClearStates](M_Grasshopper_Kernel_GH_State_ClearStates.htm)|  Removes all
items from the state database.  
![Public method](../icons/pubmethod.gif)|
[CreateStateFromDocument](M_Grasshopper_Kernel_GH_State_CreateStateFromDocument.htm)|
Creates a state database from a document.  
![Public method](../icons/pubmethod.gif)|
[Read](M_Grasshopper_Kernel_GH_State_Read.htm)|  
![Public method](../icons/pubmethod.gif)|
[RemoveStateObject](M_Grasshopper_Kernel_GH_State_RemoveStateObject.htm)|
Remove an object from the database.  
![Public method](../icons/pubmethod.gif)|
[Write](M_Grasshopper_Kernel_GH_State_Write.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

