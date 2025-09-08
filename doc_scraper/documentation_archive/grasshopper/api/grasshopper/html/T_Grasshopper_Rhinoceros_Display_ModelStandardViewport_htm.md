---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Rhinoceros_Display_ModelStandardViewport.htm
scraped_at: 2025-09-08T16:23:24.099591
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Rhinoceros.Display](../html/N_Grasshopper_Rhinoceros_Display.htm
"Grasshopper.Rhinoceros.Display")

[ModelStandardViewport
Class](../html/T_Grasshopper_Rhinoceros_Display_ModelStandardViewport.htm
"ModelStandardViewport Class")

[ModelStandardViewport Constructor
](../html/Overload_Grasshopper_Rhinoceros_Display_ModelStandardViewport__ctor.htm
"ModelStandardViewport Constructor ")

[ModelStandardViewport
Properties](../html/Properties_T_Grasshopper_Rhinoceros_Display_ModelStandardViewport.htm
"ModelStandardViewport Properties")

[ModelStandardViewport
Methods](../html/Methods_T_Grasshopper_Rhinoceros_Display_ModelStandardViewport.htm
"ModelStandardViewport Methods")

[ModelStandardViewport Type
Conversions](../html/Operators_T_Grasshopper_Rhinoceros_Display_ModelStandardViewport.htm
"ModelStandardViewport Type Conversions")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# ModelStandardViewport Class  
  
---  
  
Represents a Rhino standard modeling viewport. Wraps the main viewport of a
modeling RhinoView instance.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.RhinocerosModelData](T_Grasshopper_Rhinoceros_ModelData.htm)  
[Grasshopper.RhinocerosModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm)  
[Grasshopper.Rhinoceros.DisplayModelViewport](T_Grasshopper_Rhinoceros_Display_ModelViewport.htm)  
Grasshopper.Rhinoceros.DisplayModelStandardViewport  

**Namespace:**
[Grasshopper.Rhinoceros.Display](N_Grasshopper_Rhinoceros_Display.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class ModelStandardViewport : ModelViewport
    
    
    Public NotInheritable Class ModelStandardViewport
    	Inherits ModelViewport

The ModelStandardViewport type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[ModelStandardViewport](M_Grasshopper_Rhinoceros_Display_ModelStandardViewport__ctor.htm)|
Initializes a new instance of the ModelStandardViewport class  
![Public method](../icons/pubmethod.gif)|
[ModelStandardViewport(ModelStandardViewportAttributes)](M_Grasshopper_Rhinoceros_Display_ModelStandardViewport__ctor_1.htm)|
Initializes a new instance of the ModelStandardViewport class  
![Public method](../icons/pubmethod.gif)|
[ModelStandardViewport(Guid)](M_Grasshopper_Rhinoceros_Display_ModelStandardViewport__ctor_3.htm)|
Initializes a new instance of the ModelStandardViewport class  
![Public method](../icons/pubmethod.gif)|
[ModelStandardViewport(RhinoViewport)](M_Grasshopper_Rhinoceros_Display_ModelStandardViewport__ctor_2.htm)|
Initializes a new instance of the ModelStandardViewport class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[DisplayMode](P_Grasshopper_Rhinoceros_Display_ModelViewport_DisplayMode.htm)|
(Inherited from
[ModelViewport](T_Grasshopper_Rhinoceros_Display_ModelViewport.htm).)  
![Public property](../icons/pubproperty.gif)|
[Id](P_Grasshopper_Rhinoceros_ModelContent_Id.htm)|  (Inherited from
[ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsValid](P_Grasshopper_Rhinoceros_ModelContent_IsValid.htm)|  (Inherited from
[ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Public property](../icons/pubproperty.gif)|
[Name](P_Grasshopper_Rhinoceros_ModelContent_Name.htm)|  (Inherited from
[ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Public property](../icons/pubproperty.gif)|
[Notes](P_Grasshopper_Rhinoceros_ModelContent_Notes.htm)|  (Inherited from
[ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Public property](../icons/pubproperty.gif)|
[Parent](P_Grasshopper_Rhinoceros_ModelContent_Parent.htm)|  (Inherited from
[ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Public property](../icons/pubproperty.gif)|
[Path](P_Grasshopper_Rhinoceros_ModelContent_Path.htm)|  (Inherited from
[ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Public property](../icons/pubproperty.gif)|
[Space](P_Grasshopper_Rhinoceros_Display_ModelStandardViewport_Space.htm)|
(Overrides
[ModelViewportSpace](P_Grasshopper_Rhinoceros_Display_ModelViewport_Space.htm).)  
![Public property](../icons/pubproperty.gif)|
[Tags](P_Grasshopper_Rhinoceros_ModelContent_Tags.htm)|  (Inherited from
[ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Public property](../icons/pubproperty.gif)|
[ViewportType](P_Grasshopper_Rhinoceros_Display_ModelStandardViewport_ViewportType.htm)|
(Overrides
[ModelViewportViewportType](P_Grasshopper_Rhinoceros_Display_ModelViewport_ViewportType.htm).)  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Cast](M_Grasshopper_Rhinoceros_Display_ModelStandardViewport_Cast.htm)|  
![Public method](../icons/pubmethod.gif)|
[CastToT(T)](M_Grasshopper_Rhinoceros_Display_ModelStandardViewport_CastTo__1.htm)|
(Overrides
[ModelViewportCastToT(T)](M_Grasshopper_Rhinoceros_Display_ModelViewport_CastTo__1.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToT(T)](M_Grasshopper_Rhinoceros_Display_ModelViewport_CastTo__1.htm)|
(Inherited from
[ModelViewport](T_Grasshopper_Rhinoceros_Display_ModelViewport.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToT(T)](M_Grasshopper_Rhinoceros_ModelContent_CastTo__1.htm)|  (Inherited
from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToT(T)](M_Grasshopper_Rhinoceros_ModelData_CastTo__1.htm)|  (Inherited
from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).)  
![Public method](../icons/pubmethod.gif)|
[Equals(ModelContent)](M_Grasshopper_Rhinoceros_ModelContent_Equals.htm)|
(Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Public method](../icons/pubmethod.gif)|
[Equals(ModelData)](M_Grasshopper_Rhinoceros_ModelData_Equals.htm)|
(Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).)  
![Public method](../icons/pubmethod.gif)|
[Equals(Object)](M_Grasshopper_Rhinoceros_ModelContent_Equals_1.htm)|
(Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Public method](../icons/pubmethod.gif)|
[GetHashCode](M_Grasshopper_Rhinoceros_ModelContent_GetHashCode.htm)|
(Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Public method](../icons/pubmethod.gif)|
[ToAttributes](M_Grasshopper_Rhinoceros_Display_ModelStandardViewport_ToAttributes.htm)|  
![Public method](../icons/pubmethod.gif)|
[ToDetails](M_Grasshopper_Rhinoceros_ModelData_ToDetails.htm)|  (Inherited
from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).)  
![Public method](../icons/pubmethod.gif)|
[TooltipString](M_Grasshopper_Rhinoceros_ModelContent_TooltipString.htm)|
(Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Rhinoceros_ModelContent_ToString.htm)|  (Inherited
from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
Top

![](../icons/SectionExpanded.png)Operators

| Name| Description  
---|---|---  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [(ModelStandardViewportAttributes to
ModelStandardViewport)](M_Grasshopper_Rhinoceros_Display_ModelStandardViewport_op_Implicit.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [(RhinoViewport to
ModelStandardViewport)](M_Grasshopper_Rhinoceros_Display_ModelStandardViewport_op_Implicit_1.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros.Display
Namespace](N_Grasshopper_Rhinoceros_Display.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

