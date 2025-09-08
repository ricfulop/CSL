---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Types_IGH_ReferencedData.htm
scraped_at: 2025-09-08T16:21:47.683783
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm
"Grasshopper.Kernel.Types")

[IGH_ReferencedData
Interface](../html/T_Grasshopper_Kernel_Types_IGH_ReferencedData.htm
"IGH_ReferencedData Interface")

[IGH_ReferencedData
Properties](../html/Properties_T_Grasshopper_Kernel_Types_IGH_ReferencedData.htm
"IGH_ReferencedData Properties")

[IGH_ReferencedData
Methods](../html/Methods_T_Grasshopper_Kernel_Types_IGH_ReferencedData.htm
"IGH_ReferencedData Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# IGH_ReferencedData Interface  
  
---  
  
**Namespace:** [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public interface IGH_ReferencedData : IGH_Goo
    
    
    Public Interface IGH_ReferencedData
    	Inherits IGH_Goo

The IGH_ReferencedData type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[IsReferencedData](P_Grasshopper_Kernel_Types_IGH_ReferencedData_IsReferencedData.htm)|  
![Public property](../icons/pubproperty.gif)|
[IsReferencedDataLoaded](P_Grasshopper_Kernel_Types_IGH_ReferencedData_IsReferencedDataLoaded.htm)|  
![Public property](../icons/pubproperty.gif)|
[IsValid](P_Grasshopper_Kernel_Types_IGH_Goo_IsValid.htm)|  Gets a value
indicating whether or not the current value is valid.  (Inherited from
[IGH_Goo](T_Grasshopper_Kernel_Types_IGH_Goo.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsValidWhyNot](P_Grasshopper_Kernel_Types_IGH_Goo_IsValidWhyNot.htm)|  Gets a
string describing the state of "invalidness". If the instance _is_ valid, then
this property should return Nothing or String.Empty.  (Inherited from
[IGH_Goo](T_Grasshopper_Kernel_Types_IGH_Goo.htm).)  
![Public property](../icons/pubproperty.gif)|
[TypeDescription](P_Grasshopper_Kernel_Types_IGH_Goo_TypeDescription.htm)|
Gets a description of the type of the implementation.  (Inherited from
[IGH_Goo](T_Grasshopper_Kernel_Types_IGH_Goo.htm).)  
![Public property](../icons/pubproperty.gif)|
[TypeName](P_Grasshopper_Kernel_Types_IGH_Goo_TypeName.htm)|  Gets the name of
the type of the implementation.  (Inherited from
[IGH_Goo](T_Grasshopper_Kernel_Types_IGH_Goo.htm).)  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[CastFrom](M_Grasshopper_Kernel_Types_IGH_Goo_CastFrom.htm)|  Attempt a cast
from generic object  (Inherited from
[IGH_Goo](T_Grasshopper_Kernel_Types_IGH_Goo.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToT](M_Grasshopper_Kernel_Types_IGH_Goo_CastTo__1.htm)|  Attempt a cast
to type T  (Inherited from [IGH_Goo](T_Grasshopper_Kernel_Types_IGH_Goo.htm).)  
![Public method](../icons/pubmethod.gif)|
[Duplicate](M_Grasshopper_Kernel_Types_IGH_Goo_Duplicate.htm)|  Make a
complete duplicate of this instance. No shallow copies.  (Inherited from
[IGH_Goo](T_Grasshopper_Kernel_Types_IGH_Goo.htm).)  
![Public method](../icons/pubmethod.gif)|
[EmitProxy](M_Grasshopper_Kernel_Types_IGH_Goo_EmitProxy.htm)|  Create a new
proxy for this instance. Return Null if this class does not support proxies.
(Inherited from [IGH_Goo](T_Grasshopper_Kernel_Types_IGH_Goo.htm).)  
![Public method](../icons/pubmethod.gif)|
[LoadReferencedData](M_Grasshopper_Kernel_Types_IGH_ReferencedData_LoadReferencedData.htm)|  
![Public method](../icons/pubmethod.gif)|
[ScriptVariable](M_Grasshopper_Kernel_Types_IGH_Goo_ScriptVariable.htm)|  This
function will be called when the local IGH_Goo instance disapears into a user
Script. This would be an excellent place to cast your IGH_Goo type to a simple
data type.  (Inherited from
[IGH_Goo](T_Grasshopper_Kernel_Types_IGH_Goo.htm).)  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Kernel_Types_IGH_Goo_ToString.htm)|  Creates a string
description of the current instance value  (Inherited from
[IGH_Goo](T_Grasshopper_Kernel_Types_IGH_Goo.htm).)  
![Public method](../icons/pubmethod.gif)|
[UnloadReferencedData](M_Grasshopper_Kernel_Types_IGH_ReferencedData_UnloadReferencedData.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

