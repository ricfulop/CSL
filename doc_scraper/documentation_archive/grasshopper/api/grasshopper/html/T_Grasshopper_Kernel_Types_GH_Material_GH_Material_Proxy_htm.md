---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Types_GH_Material_GH_Material_Proxy.htm
scraped_at: 2025-09-08T16:21:02.495196
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm
"Grasshopper.Kernel.Types")

[GH_Material.GH_Material_Proxy
Class](../html/T_Grasshopper_Kernel_Types_GH_Material_GH_Material_Proxy.htm
"GH_Material.GH_Material_Proxy Class")

[GH_Material.GH_Material_Proxy Constructor
](../html/M_Grasshopper_Kernel_Types_GH_Material_GH_Material_Proxy__ctor.htm
"GH_Material.GH_Material_Proxy Constructor ")

[GH_Material_Proxy
Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_Material_GH_Material_Proxy.htm
"GH_Material_Proxy Properties")

[GH_Material_Proxy
Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_Material_GH_Material_Proxy.htm
"GH_Material_Proxy Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_MaterialGH_Material_Proxy Class  
  
---  
  
![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.Kernel.TypesGH_GooProxy](T_Grasshopper_Kernel_Types_GH_GooProxy_1.htm)[GH_Material](T_Grasshopper_Kernel_Types_GH_Material.htm)  
Grasshopper.Kernel.TypesGH_MaterialGH_Material_Proxy  

**Namespace:** [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_Material_Proxy : GH_GooProxy<GH_Material>
    
    
    Public Class GH_Material_Proxy
    	Inherits GH_GooProxy(Of GH_Material)

The GH_MaterialGH_Material_Proxy type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_MaterialGH_Material_Proxy](M_Grasshopper_Kernel_Types_GH_Material_GH_Material_Proxy__ctor.htm)|
Initializes a new instance of the GH_MaterialGH_Material_Proxy class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Diffuse](P_Grasshopper_Kernel_Types_GH_Material_GH_Material_Proxy_Diffuse.htm)|  
![Public property](../icons/pubproperty.gif)|
[Emission](P_Grasshopper_Kernel_Types_GH_Material_GH_Material_Proxy_Emission.htm)|  
![Public property](../icons/pubproperty.gif)|
[IsRDKMaterial](P_Grasshopper_Kernel_Types_GH_Material_GH_Material_Proxy_IsRDKMaterial.htm)|  
![Public property](../icons/pubproperty.gif)|
[Shine](P_Grasshopper_Kernel_Types_GH_Material_GH_Material_Proxy_Shine.htm)|  
![Public property](../icons/pubproperty.gif)|
[Specular](P_Grasshopper_Kernel_Types_GH_Material_GH_Material_Proxy_Specular.htm)|  
![Public property](../icons/pubproperty.gif)|
[Transparency](P_Grasshopper_Kernel_Types_GH_Material_GH_Material_Proxy_Transparency.htm)|  
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
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[Construct](M_Grasshopper_Kernel_Types_GH_GooProxy_1_Construct.htm)|  Override
this method to supply a custom UI during proxy construction.  (Inherited from
[GH_GooProxyT](T_Grasshopper_Kernel_Types_GH_GooProxy_1.htm).)  
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

