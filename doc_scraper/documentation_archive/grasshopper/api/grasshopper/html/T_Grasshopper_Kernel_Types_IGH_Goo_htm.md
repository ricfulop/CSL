---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Types_IGH_Goo.htm
scraped_at: 2025-09-08T16:21:45.674215
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm
"Grasshopper.Kernel.Types")

[IGH_Goo Interface](../html/T_Grasshopper_Kernel_Types_IGH_Goo.htm "IGH_Goo
Interface")

[IGH_Goo Properties](../html/Properties_T_Grasshopper_Kernel_Types_IGH_Goo.htm
"IGH_Goo Properties")

[IGH_Goo Methods](../html/Methods_T_Grasshopper_Kernel_Types_IGH_Goo.htm
"IGH_Goo Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# IGH_Goo Interface  
  
---  
  
Base interface for all Data inside Grasshopper. Every parameter must implement
a type of Goo.

**Namespace:** [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public interface IGH_Goo : GH_ISerializable
    
    
    Public Interface IGH_Goo
    	Inherits GH_ISerializable

The IGH_Goo type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[IsValid](P_Grasshopper_Kernel_Types_IGH_Goo_IsValid.htm)|  Gets a value
indicating whether or not the current value is valid.  
![Public property](../icons/pubproperty.gif)|
[IsValidWhyNot](P_Grasshopper_Kernel_Types_IGH_Goo_IsValidWhyNot.htm)|  Gets a
string describing the state of "invalidness". If the instance _is_ valid, then
this property should return Nothing or String.Empty.  
![Public property](../icons/pubproperty.gif)|
[TypeDescription](P_Grasshopper_Kernel_Types_IGH_Goo_TypeDescription.htm)|
Gets a description of the type of the implementation.  
![Public property](../icons/pubproperty.gif)|
[TypeName](P_Grasshopper_Kernel_Types_IGH_Goo_TypeName.htm)|  Gets the name of
the type of the implementation.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[CastFrom](M_Grasshopper_Kernel_Types_IGH_Goo_CastFrom.htm)|  Attempt a cast
from generic object  
![Public method](../icons/pubmethod.gif)|
[CastToT](M_Grasshopper_Kernel_Types_IGH_Goo_CastTo__1.htm)|  Attempt a cast
to type T  
![Public method](../icons/pubmethod.gif)|
[Duplicate](M_Grasshopper_Kernel_Types_IGH_Goo_Duplicate.htm)|  Make a
complete duplicate of this instance. No shallow copies.  
![Public method](../icons/pubmethod.gif)|
[EmitProxy](M_Grasshopper_Kernel_Types_IGH_Goo_EmitProxy.htm)|  Create a new
proxy for this instance. Return Null if this class does not support proxies.  
![Public method](../icons/pubmethod.gif)|
[Read](M_GH_IO_GH_ISerializable_Read.htm)|  This method is called whenever the
instance is required to deserialize itself.  (Inherited from
[GH_ISerializable](T_GH_IO_GH_ISerializable.htm).)  
![Public method](../icons/pubmethod.gif)|
[ScriptVariable](M_Grasshopper_Kernel_Types_IGH_Goo_ScriptVariable.htm)|  This
function will be called when the local IGH_Goo instance disapears into a user
Script. This would be an excellent place to cast your IGH_Goo type to a simple
data type.  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Kernel_Types_IGH_Goo_ToString.htm)|  Creates a string
description of the current instance value  
![Public method](../icons/pubmethod.gif)|
[Write](M_GH_IO_GH_ISerializable_Write.htm)|  This method is called whenever
the instance is required to serialize itself.  (Inherited from
[GH_ISerializable](T_GH_IO_GH_ISerializable.htm).)  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

