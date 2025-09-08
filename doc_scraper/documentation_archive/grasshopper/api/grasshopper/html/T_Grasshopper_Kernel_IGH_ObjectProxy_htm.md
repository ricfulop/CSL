---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_IGH_ObjectProxy.htm
scraped_at: 2025-09-08T16:18:35.842207
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH_ObjectProxy Interface](../html/T_Grasshopper_Kernel_IGH_ObjectProxy.htm
"IGH_ObjectProxy Interface")

[IGH_ObjectProxy
Properties](../html/Properties_T_Grasshopper_Kernel_IGH_ObjectProxy.htm
"IGH_ObjectProxy Properties")

[IGH_ObjectProxy
Methods](../html/Methods_T_Grasshopper_Kernel_IGH_ObjectProxy.htm
"IGH_ObjectProxy Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# IGH_ObjectProxy Interface  
  
---  
  
Provides proxy data for all Grasshopper components and parameters.

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public interface IGH_ObjectProxy
    
    
    Public Interface IGH_ObjectProxy

The IGH_ObjectProxy type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Desc](P_Grasshopper_Kernel_IGH_ObjectProxy_Desc.htm)|  Gets the Instance
Description associated with this proxy.  
![Public property](../icons/pubproperty.gif)|
[Exposure](P_Grasshopper_Kernel_IGH_ObjectProxy_Exposure.htm)|  Gets or sets
the Exposure of the target object. Only set the exposure if you know what you
are doing.  
![Public property](../icons/pubproperty.gif)|
[Guid](P_Grasshopper_Kernel_IGH_ObjectProxy_Guid.htm)|  Gets the Guid of the
target object. In the case of Compiled Objects, the Guid represents the
ComponentID, in the case of User Objects, the Guid is a hash of the file path.  
![Public property](../icons/pubproperty.gif)|
[Icon](P_Grasshopper_Kernel_IGH_ObjectProxy_Icon.htm)|  Gets the icon for this
object.  
![Public property](../icons/pubproperty.gif)|
[Kind](P_Grasshopper_Kernel_IGH_ObjectProxy_Kind.htm)|  Gets the kind of the
Proxy target object.  
![Public property](../icons/pubproperty.gif)|
[LibraryGuid](P_Grasshopper_Kernel_IGH_ObjectProxy_LibraryGuid.htm)|  Gets the
ID of the library (GHA file) that defines this object.  
![Public property](../icons/pubproperty.gif)|
[Location](P_Grasshopper_Kernel_IGH_ObjectProxy_Location.htm)|  Gets the
location of the target object. If the proxy represents a Compiled Object, the
location refers to the file path of the assembly, in the case of User Objects,
the location refers to the object file.  
![Public property](../icons/pubproperty.gif)|
[Obsolete](P_Grasshopper_Kernel_IGH_ObjectProxy_Obsolete.htm)|  Gets whether
this proxy represents an obsolete object.  
![Public property](../icons/pubproperty.gif)|
[SDKCompliant](P_Grasshopper_Kernel_IGH_ObjectProxy_SDKCompliant.htm)|  Gets
whether this object is compliant with the current Rhino version.  
![Public property](../icons/pubproperty.gif)|
[Type](P_Grasshopper_Kernel_IGH_ObjectProxy_Type.htm)|  Gets the Type for the
target object. If the proxy references a User Object, the Type member will be
null.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[CreateInstance](M_Grasshopper_Kernel_IGH_ObjectProxy_CreateInstance.htm)|
Create a new instance from the target object.  
![Public method](../icons/pubmethod.gif)|
[DuplicateProxy](M_Grasshopper_Kernel_IGH_ObjectProxy_DuplicateProxy.htm)|
Create a duplicate of this proxy.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

