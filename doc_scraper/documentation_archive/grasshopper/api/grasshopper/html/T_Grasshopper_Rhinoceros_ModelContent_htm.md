---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Rhinoceros_ModelContent.htm
scraped_at: 2025-09-08T16:22:33.877351
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Rhinoceros](../html/N_Grasshopper_Rhinoceros.htm
"Grasshopper.Rhinoceros")

[ModelContent Class](../html/T_Grasshopper_Rhinoceros_ModelContent.htm
"ModelContent Class")

[ModelContent
Properties](../html/Properties_T_Grasshopper_Rhinoceros_ModelContent.htm
"ModelContent Properties")

[ModelContent
Methods](../html/Methods_T_Grasshopper_Rhinoceros_ModelContent.htm
"ModelContent Methods")

[ModelContent Fields](../html/Fields_T_Grasshopper_Rhinoceros_ModelContent.htm
"ModelContent Fields")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# ModelContent Class  
  
---  
  
Represents a Rhino model element.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.RhinocerosModelData](T_Grasshopper_Rhinoceros_ModelData.htm)  
Grasshopper.RhinocerosModelContent  
More...

**Namespace:** [Grasshopper.Rhinoceros](N_Grasshopper_Rhinoceros.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public abstract class ModelContent : ModelData, 
    	IGH_ModelContentData, IEquatable<ModelContent>
    
    
    Public MustInherit Class ModelContent
    	Inherits ModelData
    	Implements IGH_ModelContentData, IEquatable(Of ModelContent)

The ModelContent type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Protected property](../icons/protproperty.gif)|
[Attribs](P_Grasshopper_Rhinoceros_ModelContent_Attribs.htm)|  
![Protected property](../icons/protproperty.gif)|
[DefaultAttributes](P_Grasshopper_Rhinoceros_ModelData_DefaultAttributes.htm)|
(Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).)  
![Public property](../icons/pubproperty.gif)|
[Id](P_Grasshopper_Rhinoceros_ModelContent_Id.htm)|  
![Protected property](../icons/protproperty.gif)|
[IsReferencedData](P_Grasshopper_Rhinoceros_ModelContent_IsReferencedData.htm)|  
![Protected property](../icons/protproperty.gif)|
[IsReferencedDataLoaded](P_Grasshopper_Rhinoceros_ModelContent_IsReferencedDataLoaded.htm)|  
![Public property](../icons/pubproperty.gif)|
[IsValid](P_Grasshopper_Rhinoceros_ModelContent_IsValid.htm)|  (Overrides
ModelData.IsValid.)  
![Protected property](../icons/protproperty.gif)|
[IsValidWhyNot](P_Grasshopper_Rhinoceros_ModelContent_IsValidWhyNot.htm)|
(Overrides
[ModelDataIsValidWhyNot](P_Grasshopper_Rhinoceros_ModelData_IsValidWhyNot.htm).)  
![Public property](../icons/pubproperty.gif)|
[Name](P_Grasshopper_Rhinoceros_ModelContent_Name.htm)|  
![Public property](../icons/pubproperty.gif)|
[Notes](P_Grasshopper_Rhinoceros_ModelContent_Notes.htm)|  
![Public property](../icons/pubproperty.gif)|
[Parent](P_Grasshopper_Rhinoceros_ModelContent_Parent.htm)|  
![Public property](../icons/pubproperty.gif)|
[Path](P_Grasshopper_Rhinoceros_ModelContent_Path.htm)|  
![Public property](../icons/pubproperty.gif)|
[Tags](P_Grasshopper_Rhinoceros_ModelContent_Tags.htm)|  
![Protected property](../icons/protproperty.gif)|
[TypeDescription](P_Grasshopper_Rhinoceros_ModelData_TypeDescription.htm)|
(Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).)  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Protected method](../icons/protmethod.gif)|
[AsFrozen](M_Grasshopper_Rhinoceros_ModelContent_AsFrozen.htm)|  Try to obtain
a dereferenced snapshot of itself.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Cast(Object)](M_Grasshopper_Rhinoceros_ModelContent_Cast.htm)|  
![Protected method](../icons/protmethod.gif)![Static
member](../icons/static.gif)| [CastA,
T(Object)](M_Grasshopper_Rhinoceros_ModelContent_Cast__2.htm)|  
![Public method](../icons/pubmethod.gif)|
[CastToT(T)](M_Grasshopper_Rhinoceros_ModelContent_CastTo__1.htm)|  (Overrides
[ModelDataCastToT(T)](M_Grasshopper_Rhinoceros_ModelData_CastTo__1.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToT(T)](M_Grasshopper_Rhinoceros_ModelData_CastTo__1.htm)|  (Inherited
from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).)  
![Public method](../icons/pubmethod.gif)|
[Equals(ModelContent)](M_Grasshopper_Rhinoceros_ModelContent_Equals.htm)|  
![Public method](../icons/pubmethod.gif)|
[Equals(ModelData)](M_Grasshopper_Rhinoceros_ModelData_Equals.htm)|
(Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).)  
![Public method](../icons/pubmethod.gif)|
[Equals(Object)](M_Grasshopper_Rhinoceros_ModelContent_Equals_1.htm)|
(Overrides
[ModelDataEquals(Object)](M_Grasshopper_Rhinoceros_ModelData_Equals_1.htm).)  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[FromId](M_Grasshopper_Rhinoceros_ModelContent_FromId.htm)|  
![Public method](../icons/pubmethod.gif)|
[GetHashCode](M_Grasshopper_Rhinoceros_ModelContent_GetHashCode.htm)|
(Overrides
[ModelDataGetHashCode](M_Grasshopper_Rhinoceros_ModelData_GetHashCode.htm).)  
![Protected method](../icons/protmethod.gif)|
[InternaliseData](M_Grasshopper_Rhinoceros_ModelContent_InternaliseData.htm)|  
![Protected method](../icons/protmethod.gif)|
[LoadReferencedData](M_Grasshopper_Rhinoceros_ModelContent_LoadReferencedData.htm)|  
![Protected method](../icons/protmethod.gif)|
[Read](M_Grasshopper_Rhinoceros_ModelContent_Read.htm)|  (Overrides
[ModelDataRead(GH_IReader)](M_Grasshopper_Rhinoceros_ModelData_Read.htm).)  
![Protected method](../icons/protmethod.gif)|
[RuntimeId](M_Grasshopper_Rhinoceros_ModelContent_RuntimeId.htm)|  
![Public method](../icons/pubmethod.gif)|
[ToAttributes](M_Grasshopper_Rhinoceros_ModelContent_ToAttributes.htm)|  
![Public method](../icons/pubmethod.gif)|
[ToDetails](M_Grasshopper_Rhinoceros_ModelData_ToDetails.htm)|  (Inherited
from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).)  
![Public method](../icons/pubmethod.gif)|
[TooltipString](M_Grasshopper_Rhinoceros_ModelContent_TooltipString.htm)|
(Overrides
[ModelDataTooltipString](M_Grasshopper_Rhinoceros_ModelData_TooltipString.htm).)  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Rhinoceros_ModelContent_ToString.htm)|  (Overrides
[ModelDataToString](M_Grasshopper_Rhinoceros_ModelData_ToString.htm).)  
![Protected method](../icons/protmethod.gif)|
[UnloadReferencedData](M_Grasshopper_Rhinoceros_ModelContent_UnloadReferencedData.htm)|  
![Protected method](../icons/protmethod.gif)|
[Write](M_Grasshopper_Rhinoceros_ModelContent_Write.htm)|  (Overrides
[ModelDataWrite(GH_IWriter)](M_Grasshopper_Rhinoceros_ModelData_Write.htm).)  
Top

![](../icons/SectionExpanded.png)Fields

| Name| Description  
---|---|---  
![Protected field](../icons/protfield.gif)|
[Serial](F_Grasshopper_Rhinoceros_ModelData_Serial.htm)|  (Inherited from
[ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).)  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros Namespace](N_Grasshopper_Rhinoceros.htm)

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.RhinocerosModelData](T_Grasshopper_Rhinoceros_ModelData.htm)  
Grasshopper.RhinocerosModelContent  
[Grasshopper.Rhinoceros.DisplayModelDisplayMode](T_Grasshopper_Rhinoceros_Display_ModelDisplayMode.htm)  
[Grasshopper.Rhinoceros.DisplayModelNamedView](T_Grasshopper_Rhinoceros_Display_ModelNamedView.htm)  
[Grasshopper.Rhinoceros.DisplayModelViewport](T_Grasshopper_Rhinoceros_Display_ModelViewport.htm)  
[Grasshopper.Rhinoceros.ModelModelEarthAnchorPoint](T_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint.htm)  
[Grasshopper.RhinocerosModelComponentContent](T_Grasshopper_Rhinoceros_ModelComponentContent.htm)  
[Grasshopper.Rhinoceros.RenderModelRenderContent](T_Grasshopper_Rhinoceros_Render_ModelRenderContent.htm)  
[Grasshopper.Rhinoceros.RenderModelRenderSkylight](T_Grasshopper_Rhinoceros_Render_ModelRenderSkylight.htm)  
[Grasshopper.Rhinoceros.RenderModelRenderSun](T_Grasshopper_Rhinoceros_Render_ModelRenderSun.htm)  

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

