---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Types_IGH_GooProxy.htm
scraped_at: 2025-09-08T16:21:46.670745
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm
"Grasshopper.Kernel.Types")

[IGH_GooProxy Interface](../html/T_Grasshopper_Kernel_Types_IGH_GooProxy.htm
"IGH_GooProxy Interface")

[IGH_GooProxy
Properties](../html/Properties_T_Grasshopper_Kernel_Types_IGH_GooProxy.htm
"IGH_GooProxy Properties")

[IGH_GooProxy
Methods](../html/Methods_T_Grasshopper_Kernel_Types_IGH_GooProxy.htm
"IGH_GooProxy Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# IGH_GooProxy Interface  
  
---  
  
Base interface for all type proxies.

**Namespace:** [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public interface IGH_GooProxy
    
    
    Public Interface IGH_GooProxy

The IGH_GooProxy type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[IsParsable](P_Grasshopper_Kernel_Types_IGH_GooProxy_IsParsable.htm)|  Gets a
value indicating whether or not the type can be instantiated from a String.  
![Public property](../icons/pubproperty.gif)|
[ProxyOwner](P_Grasshopper_Kernel_Types_IGH_GooProxy_ProxyOwner.htm)|  Gets
the piece of Grasshopper data that spawned this proxy.  
![Public property](../icons/pubproperty.gif)|
[UserString](P_Grasshopper_Kernel_Types_IGH_GooProxy_UserString.htm)|  Gets or
sets the user-defined string that describes this proxy. This only really makes
sense if the Proxy is Parsable.  
![Public property](../icons/pubproperty.gif)|
[Valid](P_Grasshopper_Kernel_Types_IGH_GooProxy_Valid.htm)|  Gets a value
indicating whether this proxy represents valid data.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[Construct](M_Grasshopper_Kernel_Types_IGH_GooProxy_Construct.htm)|  This
method will be called when a new instance of this type is constructed. It
allows implementers to supply a customized UI to be shown during construction.
This method should never throw exceptions.  
![Public method](../icons/pubmethod.gif)|
[FormatInstance](M_Grasshopper_Kernel_Types_IGH_GooProxy_FormatInstance.htm)|
Returns a String description of the current value.  
![Public method](../icons/pubmethod.gif)|
[FromString](M_Grasshopper_Kernel_Types_IGH_GooProxy_FromString.htm)|  If
IsParsable(), then attempts to convert the string to a generic type value  
![Public method](../icons/pubmethod.gif)|
[MutateString](M_Grasshopper_Kernel_Types_IGH_GooProxy_MutateString.htm)|
Munge a string to remove obvious errors on account of the user.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

