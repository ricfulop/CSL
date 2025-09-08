---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Types_GH_Mesh_GH_MeshProxy.htm
scraped_at: 2025-09-08T16:21:06.494826
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm
"Grasshopper.Kernel.Types")

[GH_Mesh.GH_MeshProxy
Class](../html/T_Grasshopper_Kernel_Types_GH_Mesh_GH_MeshProxy.htm
"GH_Mesh.GH_MeshProxy Class")

[GH_Mesh.GH_MeshProxy Constructor
](../html/M_Grasshopper_Kernel_Types_GH_Mesh_GH_MeshProxy__ctor.htm
"GH_Mesh.GH_MeshProxy Constructor ")

[GH_MeshProxy
Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_Mesh_GH_MeshProxy.htm
"GH_MeshProxy Properties")

[GH_MeshProxy
Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_Mesh_GH_MeshProxy.htm
"GH_MeshProxy Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_MeshGH_MeshProxy Class  
  
---  
  
![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.Kernel.TypesGH_GooProxy](T_Grasshopper_Kernel_Types_GH_GooProxy_1.htm)[GH_Mesh](T_Grasshopper_Kernel_Types_GH_Mesh.htm)  
Grasshopper.Kernel.TypesGH_MeshGH_MeshProxy  

**Namespace:** [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_MeshProxy : GH_GooProxy<GH_Mesh>
    
    
    Public Class GH_MeshProxy
    	Inherits GH_GooProxy(Of GH_Mesh)

The GH_MeshGH_MeshProxy type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_MeshGH_MeshProxy](M_Grasshopper_Kernel_Types_GH_Mesh_GH_MeshProxy__ctor.htm)|
Initializes a new instance of the GH_MeshGH_MeshProxy class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Area](P_Grasshopper_Kernel_Types_GH_Mesh_GH_MeshProxy_Area.htm)|  
![Public property](../icons/pubproperty.gif)|
[EdgeCount](P_Grasshopper_Kernel_Types_GH_Mesh_GH_MeshProxy_EdgeCount.htm)|  
![Public property](../icons/pubproperty.gif)|
[FaceCount](P_Grasshopper_Kernel_Types_GH_Mesh_GH_MeshProxy_FaceCount.htm)|  
![Public property](../icons/pubproperty.gif)|
[Manifold](P_Grasshopper_Kernel_Types_GH_Mesh_GH_MeshProxy_Manifold.htm)|  
![Public property](../icons/pubproperty.gif)|
[ObjectID](P_Grasshopper_Kernel_Types_GH_Mesh_GH_MeshProxy_ObjectID.htm)|  
![Public property](../icons/pubproperty.gif)|
[Solid](P_Grasshopper_Kernel_Types_GH_Mesh_GH_MeshProxy_Solid.htm)|  
![Public property](../icons/pubproperty.gif)|
[TypeDescription](P_Grasshopper_Kernel_Types_GH_GooProxy_1_TypeDescription.htm)|
(Inherited from [GH_GooProxyT](T_Grasshopper_Kernel_Types_GH_GooProxy_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[TypeName](P_Grasshopper_Kernel_Types_GH_GooProxy_1_TypeName.htm)|  (Inherited
from [GH_GooProxyT](T_Grasshopper_Kernel_Types_GH_GooProxy_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[Valid](P_Grasshopper_Kernel_Types_GH_GooProxy_1_Valid.htm)|  Gets a value
indicating whether this proxy represents valid data.  (Inherited from
[GH_GooProxyT](T_Grasshopper_Kernel_Types_GH_GooProxy_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[VertexCount](P_Grasshopper_Kernel_Types_GH_Mesh_GH_MeshProxy_VertexCount.htm)|  
![Public property](../icons/pubproperty.gif)|
[Volume](P_Grasshopper_Kernel_Types_GH_Mesh_GH_MeshProxy_Volume.htm)|  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[Construct](M_Grasshopper_Kernel_Types_GH_Mesh_GH_MeshProxy_Construct.htm)|
(Overrides
[GH_GooProxyTConstruct](M_Grasshopper_Kernel_Types_GH_GooProxy_1_Construct.htm).)  
![Public method](../icons/pubmethod.gif)|
[FormatInstance](M_Grasshopper_Kernel_Types_GH_GooProxy_1_FormatInstance.htm)|
Returns a String description of the current value.  (Inherited from
[GH_GooProxyT](T_Grasshopper_Kernel_Types_GH_GooProxy_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[FromString](M_Grasshopper_Kernel_Types_GH_GooProxy_1_FromString.htm)|  If
IsParsable(), then attempts to convert the string to a generic type value
(Inherited from [GH_GooProxyT](T_Grasshopper_Kernel_Types_GH_GooProxy_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[MutateString](M_Grasshopper_Kernel_Types_GH_GooProxy_1_MutateString.htm)|
Munge a string to remove obvious errors on account of the user.  (Inherited
from [GH_GooProxyT](T_Grasshopper_Kernel_Types_GH_GooProxy_1.htm).)  
![Protected method](../icons/protmethod.gif)|
[NumberToString](M_Grasshopper_Kernel_Types_GH_GooProxy_1_NumberToString.htm)|
(Inherited from [GH_GooProxyT](T_Grasshopper_Kernel_Types_GH_GooProxy_1.htm).)  
![Protected method](../icons/protmethod.gif)|
[StringToNumber](M_Grasshopper_Kernel_Types_GH_GooProxy_1_StringToNumber.htm)|
(Inherited from [GH_GooProxyT](T_Grasshopper_Kernel_Types_GH_GooProxy_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Kernel_Types_GH_GooProxy_1_ToString.htm)|  (Inherited
from [GH_GooProxyT](T_Grasshopper_Kernel_Types_GH_GooProxy_1.htm).)  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

