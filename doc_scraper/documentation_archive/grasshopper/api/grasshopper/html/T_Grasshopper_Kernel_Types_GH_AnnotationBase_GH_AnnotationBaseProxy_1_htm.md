---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Types_GH_AnnotationBase_GH_AnnotationBaseProxy_1.htm
scraped_at: 2025-09-08T16:20:16.296366
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm
"Grasshopper.Kernel.Types")

[GH_AnnotationBase.GH_AnnotationBaseProxy(T)
Class](../html/T_Grasshopper_Kernel_Types_GH_AnnotationBase_GH_AnnotationBaseProxy_1.htm
"GH_AnnotationBase.GH_AnnotationBaseProxy\(T\) Class")

[GH_AnnotationBase.GH_AnnotationBaseProxy(T) Constructor
](../html/M_Grasshopper_Kernel_Types_GH_AnnotationBase_GH_AnnotationBaseProxy_1__ctor.htm
"GH_AnnotationBase.GH_AnnotationBaseProxy\(T\) Constructor ")

[GH_AnnotationBaseProxy(T)
Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_AnnotationBase_GH_AnnotationBaseProxy_1.htm
"GH_AnnotationBaseProxy\(T\) Properties")

[GH_AnnotationBaseProxy(T)
Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_AnnotationBase_GH_AnnotationBaseProxy_1.htm
"GH_AnnotationBaseProxy\(T\) Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_AnnotationBaseGH_AnnotationBaseProxyT Class  
  
---  
  
![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.Kernel.TypesGH_GooProxy](T_Grasshopper_Kernel_Types_GH_GooProxy_1.htm)T  
Grasshopper.Kernel.TypesGH_AnnotationBaseGH_AnnotationBaseProxyT  
[Grasshopper.Kernel.TypesGH_DimensionGH_DimensionProxy](T_Grasshopper_Kernel_Types_GH_Dimension_GH_DimensionProxy.htm)  

**Namespace:** [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_AnnotationBaseProxy<T> : GH_GooProxy<T>
    where T : GH_AnnotationBase
    
    
    
    Public Class GH_AnnotationBaseProxy(Of T As GH_AnnotationBase)
    	Inherits GH_GooProxy(Of T)

#### Type Parameters

T

    

The GH_AnnotationBaseGH_AnnotationBaseProxyT type exposes the following
members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_AnnotationBaseGH_AnnotationBaseProxyT](M_Grasshopper_Kernel_Types_GH_AnnotationBase_GH_AnnotationBaseProxy_1__ctor.htm)|
Initializes a new instance of the GH_AnnotationBaseGH_AnnotationBaseProxyT
class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[AnnotationType](P_Grasshopper_Kernel_Types_GH_AnnotationBase_GH_AnnotationBaseProxy_1_AnnotationType.htm)|  
![Public property](../icons/pubproperty.gif)|
[ObjectID](P_Grasshopper_Kernel_Types_GH_AnnotationBase_GH_AnnotationBaseProxy_1_ObjectID.htm)|  
![Public property](../icons/pubproperty.gif)|
[PlainText](P_Grasshopper_Kernel_Types_GH_AnnotationBase_GH_AnnotationBaseProxy_1_PlainText.htm)|  
![Public property](../icons/pubproperty.gif)|
[Style](P_Grasshopper_Kernel_Types_GH_AnnotationBase_GH_AnnotationBaseProxy_1_Style.htm)|  
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

