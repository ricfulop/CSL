---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Rhinoceros_Render_ModelRenderSun.htm
scraped_at: 2025-09-08T16:24:43.437756
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Rhinoceros.Render](../html/N_Grasshopper_Rhinoceros_Render.htm
"Grasshopper.Rhinoceros.Render")

[ModelRenderSun
Class](../html/T_Grasshopper_Rhinoceros_Render_ModelRenderSun.htm
"ModelRenderSun Class")

[ModelRenderSun Constructor
](../html/M_Grasshopper_Rhinoceros_Render_ModelRenderSun__ctor.htm
"ModelRenderSun Constructor ")

[ModelRenderSun
Properties](../html/Properties_T_Grasshopper_Rhinoceros_Render_ModelRenderSun.htm
"ModelRenderSun Properties")

[ModelRenderSun
Methods](../html/Methods_T_Grasshopper_Rhinoceros_Render_ModelRenderSun.htm
"ModelRenderSun Methods")

[ModelRenderSun Type
Conversions](../html/Operators_T_Grasshopper_Rhinoceros_Render_ModelRenderSun.htm
"ModelRenderSun Type Conversions")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# ModelRenderSun Class  
  
---  
  
Represents a Rhino sun. Wraps the functionality of the Sun type.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.RhinocerosModelData](T_Grasshopper_Rhinoceros_ModelData.htm)  
[Grasshopper.RhinocerosModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm)  
Grasshopper.Rhinoceros.RenderModelRenderSun  

**Namespace:**
[Grasshopper.Rhinoceros.Render](N_Grasshopper_Rhinoceros_Render.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class ModelRenderSun : ModelContent, 
    	IGH_PreviewData
    
    
    Public NotInheritable Class ModelRenderSun
    	Inherits ModelContent
    	Implements IGH_PreviewData

The ModelRenderSun type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[ModelRenderSun](M_Grasshopper_Rhinoceros_Render_ModelRenderSun__ctor.htm)|
Initializes a new instance of the ModelRenderSun class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Altitude](P_Grasshopper_Rhinoceros_Render_ModelRenderSun_Altitude.htm)|  
![Public property](../icons/pubproperty.gif)|
[Azimuth](P_Grasshopper_Rhinoceros_Render_ModelRenderSun_Azimuth.htm)|  
![Public property](../icons/pubproperty.gif)|
[DateTime](P_Grasshopper_Rhinoceros_Render_ModelRenderSun_DateTime.htm)|  
![Public property](../icons/pubproperty.gif)|
[DaylightSavingEnabled](P_Grasshopper_Rhinoceros_Render_ModelRenderSun_DaylightSavingEnabled.htm)|  
![Public property](../icons/pubproperty.gif)|
[DaylightSavingMinutes](P_Grasshopper_Rhinoceros_Render_ModelRenderSun_DaylightSavingMinutes.htm)|  
![Public property](../icons/pubproperty.gif)|
[Direction](P_Grasshopper_Rhinoceros_Render_ModelRenderSun_Direction.htm)|  
![Public property](../icons/pubproperty.gif)|
[Enabled](P_Grasshopper_Rhinoceros_Render_ModelRenderSun_Enabled.htm)|  
![Public property](../icons/pubproperty.gif)|
[Id](P_Grasshopper_Rhinoceros_ModelContent_Id.htm)|  (Inherited from
[ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Public property](../icons/pubproperty.gif)|
[Intensity](P_Grasshopper_Rhinoceros_Render_ModelRenderSun_Intensity.htm)|  
![Public property](../icons/pubproperty.gif)|
[IsValid](P_Grasshopper_Rhinoceros_ModelContent_IsValid.htm)|  (Inherited from
[ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Public property](../icons/pubproperty.gif)|
[Latitude](P_Grasshopper_Rhinoceros_Render_ModelRenderSun_Latitude.htm)|  
![Public property](../icons/pubproperty.gif)|
[Longitude](P_Grasshopper_Rhinoceros_Render_ModelRenderSun_Longitude.htm)|  
![Public property](../icons/pubproperty.gif)|
[Manual](P_Grasshopper_Rhinoceros_Render_ModelRenderSun_Manual.htm)|  
![Public property](../icons/pubproperty.gif)|
[Name](P_Grasshopper_Rhinoceros_ModelContent_Name.htm)|  (Inherited from
[ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Public property](../icons/pubproperty.gif)|
[North](P_Grasshopper_Rhinoceros_Render_ModelRenderSun_North.htm)|  
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
[Tags](P_Grasshopper_Rhinoceros_ModelContent_Tags.htm)|  (Inherited from
[ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Public property](../icons/pubproperty.gif)|
[TimeZone](P_Grasshopper_Rhinoceros_Render_ModelRenderSun_TimeZone.htm)|  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Cast](M_Grasshopper_Rhinoceros_Render_ModelRenderSun_Cast.htm)|  
![Public method](../icons/pubmethod.gif)|
[CastToT(T)](M_Grasshopper_Rhinoceros_ModelContent_CastTo__1.htm)|  (Inherited
from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToT(T)](M_Grasshopper_Rhinoceros_ModelData_CastTo__1.htm)|  (Inherited
from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToT(T)](M_Grasshopper_Rhinoceros_Render_ModelRenderSun_CastTo__1.htm)|
(Overrides
[ModelContentCastToT(T)](M_Grasshopper_Rhinoceros_ModelContent_CastTo__1.htm).)  
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
[ToAttributes](M_Grasshopper_Rhinoceros_Render_ModelRenderSun_ToAttributes.htm)|  
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
member](../icons/static.gif)| [(ModelRenderSunAttributes to
ModelRenderSun)](M_Grasshopper_Rhinoceros_Render_ModelRenderSun_op_Implicit.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros.Render Namespace](N_Grasshopper_Rhinoceros_Render.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

