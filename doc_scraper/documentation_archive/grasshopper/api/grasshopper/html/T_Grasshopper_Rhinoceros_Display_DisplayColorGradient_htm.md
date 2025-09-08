---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Rhinoceros_Display_DisplayColorGradient.htm
scraped_at: 2025-09-08T16:23:16.054759
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Rhinoceros.Display](../html/N_Grasshopper_Rhinoceros_Display.htm
"Grasshopper.Rhinoceros.Display")

[DisplayColorGradient
Class](../html/T_Grasshopper_Rhinoceros_Display_DisplayColorGradient.htm
"DisplayColorGradient Class")

[DisplayColorGradient Constructor
](../html/Overload_Grasshopper_Rhinoceros_Display_DisplayColorGradient__ctor.htm
"DisplayColorGradient Constructor ")

[DisplayColorGradient
Properties](../html/Properties_T_Grasshopper_Rhinoceros_Display_DisplayColorGradient.htm
"DisplayColorGradient Properties")

[DisplayColorGradient
Methods](../html/Methods_T_Grasshopper_Rhinoceros_Display_DisplayColorGradient.htm
"DisplayColorGradient Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# DisplayColorGradient Class  
  
---  
  
Represents a gradient colour stop. Wraps the functionality of the
ColorGradient type.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.Kernel.TypesGH_Goo](T_Grasshopper_Kernel_Types_GH_Goo_1.htm)ColorGradient  
Grasshopper.Rhinoceros.DisplayDisplayColorGradient  

**Namespace:**
[Grasshopper.Rhinoceros.Display](N_Grasshopper_Rhinoceros_Display.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class DisplayColorGradient : GH_Goo<ColorGradient>, 
    	IGH_PreviewData
    
    
    Public NotInheritable Class DisplayColorGradient
    	Inherits GH_Goo(Of ColorGradient)
    	Implements IGH_PreviewData

The DisplayColorGradient type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[DisplayColorGradient](M_Grasshopper_Rhinoceros_Display_DisplayColorGradient__ctor.htm)|
Blank constructor  
![Public method](../icons/pubmethod.gif)|
[DisplayColorGradient(ColorGradient)](M_Grasshopper_Rhinoceros_Display_DisplayColorGradient__ctor_2.htm)|
Initializes a new instance of the DisplayColorGradient class  
![Public method](../icons/pubmethod.gif)|
[DisplayColorGradient(DisplayColorGradient)](M_Grasshopper_Rhinoceros_Display_DisplayColorGradient__ctor_1.htm)|
Initializes a new instance of the DisplayColorGradient class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[ClippingBox](P_Grasshopper_Rhinoceros_Display_DisplayColorGradient_ClippingBox.htm)|  
![Public property](../icons/pubproperty.gif)|
[IsValid](P_Grasshopper_Rhinoceros_Display_DisplayColorGradient_IsValid.htm)|
Gets the validity of this instance.  (Overrides
[GH_GooTIsValid](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValid.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsValidWhyNot](P_Grasshopper_Rhinoceros_Display_DisplayColorGradient_IsValidWhyNot.htm)|
Gets a string describing the state of "invalidness". If the instance _is_
valid, then this property should return Nothing or String.Empty.  (Overrides
[GH_GooTIsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValidWhyNot.htm).)  
![Public property](../icons/pubproperty.gif)|
[TypeDescription](P_Grasshopper_Rhinoceros_Display_DisplayColorGradient_TypeDescription.htm)|
(Overrides
[GH_GooTTypeDescription](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeDescription.htm).)  
![Public property](../icons/pubproperty.gif)|
[TypeName](P_Grasshopper_Rhinoceros_Display_DisplayColorGradient_TypeName.htm)|
(Overrides
[GH_GooTTypeName](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeName.htm).)  
![Public property](../icons/pubproperty.gif)|
[Value](P_Grasshopper_Kernel_Types_GH_Goo_1_Value.htm)|  Gets or sets the
internal data.  (Inherited from
[GH_GooT](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).)  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[CastFrom](M_Grasshopper_Rhinoceros_Display_DisplayColorGradient_CastFrom.htm)|
(Overrides
[GH_GooTCastFrom(Object)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastFrom.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToQ(Q)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm)|  Attempt a
cast to type Q.  (Inherited from
[GH_GooT](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToT(T)](M_Grasshopper_Rhinoceros_Display_DisplayColorGradient_CastTo__1.htm)|
(Overrides
[GH_GooTCastToQ(Q)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm).)  
![Public method](../icons/pubmethod.gif)|
[DrawViewportMeshes](M_Grasshopper_Rhinoceros_Display_DisplayColorGradient_DrawViewportMeshes.htm)|  
![Public method](../icons/pubmethod.gif)|
[DrawViewportWires](M_Grasshopper_Rhinoceros_Display_DisplayColorGradient_DrawViewportWires.htm)|  
![Public method](../icons/pubmethod.gif)|
[Duplicate](M_Grasshopper_Rhinoceros_Display_DisplayColorGradient_Duplicate.htm)|
(Overrides
[GH_GooTDuplicate](M_Grasshopper_Kernel_Types_GH_Goo_1_Duplicate.htm).)  
![Public method](../icons/pubmethod.gif)|
[DuplicateColourGradient](M_Grasshopper_Rhinoceros_Display_DisplayColorGradient_DuplicateColourGradient.htm)|  
![Public method](../icons/pubmethod.gif)|
[EmitProxy](M_Grasshopper_Kernel_Types_GH_Goo_1_EmitProxy.htm)|  Create a new
proxy for this instance. Return Null if this class does not support proxies.
(Inherited from [GH_GooT](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[Read](M_Grasshopper_Rhinoceros_Display_DisplayColorGradient_Read.htm)|
(Overrides
[GH_GooTRead(GH_IReader)](M_Grasshopper_Kernel_Types_GH_Goo_1_Read.htm).)  
![Public method](../icons/pubmethod.gif)|
[ScriptVariable](M_Grasshopper_Kernel_Types_GH_Goo_1_ScriptVariable.htm)|
This function will be called when the local IGH_Goo instance disappears into a
user Script. This would be an excellent place to cast your IGH_Goo type to a
simple data type.  (Inherited from
[GH_GooT](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Rhinoceros_Display_DisplayColorGradient_ToString.htm)|
(Overrides
[GH_GooTToString](M_Grasshopper_Kernel_Types_GH_Goo_1_ToString.htm).)  
![Public method](../icons/pubmethod.gif)|
[Write](M_Grasshopper_Rhinoceros_Display_DisplayColorGradient_Write.htm)|
(Overrides
[GH_GooTWrite(GH_IWriter)](M_Grasshopper_Kernel_Types_GH_Goo_1_Write.htm).)  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros.Display
Namespace](N_Grasshopper_Rhinoceros_Display.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

