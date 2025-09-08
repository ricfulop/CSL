---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Rhinoceros_Render_ModelRenderContent.htm
scraped_at: 2025-09-08T16:24:35.389632
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Rhinoceros.Render](../html/N_Grasshopper_Rhinoceros_Render.htm
"Grasshopper.Rhinoceros.Render")

[ModelRenderContent
Class](../html/T_Grasshopper_Rhinoceros_Render_ModelRenderContent.htm
"ModelRenderContent Class")

[ModelRenderContent
Properties](../html/Properties_T_Grasshopper_Rhinoceros_Render_ModelRenderContent.htm
"ModelRenderContent Properties")

[ModelRenderContent
Methods](../html/Methods_T_Grasshopper_Rhinoceros_Render_ModelRenderContent.htm
"ModelRenderContent Methods")

[ModelRenderContent
Fields](../html/Fields_T_Grasshopper_Rhinoceros_Render_ModelRenderContent.htm
"ModelRenderContent Fields")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# ModelRenderContent Class  
  
---  
  
Represents a Rhino render content. Wraps the functionality of the
RenderContent type.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.RhinocerosModelData](T_Grasshopper_Rhinoceros_ModelData.htm)  
[Grasshopper.RhinocerosModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm)  
Grasshopper.Rhinoceros.RenderModelRenderContent  
[Grasshopper.Rhinoceros.RenderModelRenderEnvironment](T_Grasshopper_Rhinoceros_Render_ModelRenderEnvironment.htm)  
[Grasshopper.Rhinoceros.RenderModelRenderMaterial](T_Grasshopper_Rhinoceros_Render_ModelRenderMaterial.htm)  
[Grasshopper.Rhinoceros.RenderModelRenderTexture](T_Grasshopper_Rhinoceros_Render_ModelRenderTexture.htm)  

**Namespace:**
[Grasshopper.Rhinoceros.Render](N_Grasshopper_Rhinoceros_Render.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public abstract class ModelRenderContent : ModelContent
    
    
    Public MustInherit Class ModelRenderContent
    	Inherits ModelContent

The ModelRenderContent type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Protected property](../icons/protproperty.gif)|
[Attribs](P_Grasshopper_Rhinoceros_Render_ModelRenderContent_Attribs.htm)|  
![Protected property](../icons/protproperty.gif)|
[DefaultAttributes](P_Grasshopper_Rhinoceros_ModelData_DefaultAttributes.htm)|
(Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).)  
![Public property](../icons/pubproperty.gif)|
[Id](P_Grasshopper_Rhinoceros_ModelContent_Id.htm)|  (Inherited from
[ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Protected property](../icons/protproperty.gif)|
[IsReferencedData](P_Grasshopper_Rhinoceros_ModelContent_IsReferencedData.htm)|
(Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Protected property](../icons/protproperty.gif)|
[IsReferencedDataLoaded](P_Grasshopper_Rhinoceros_ModelContent_IsReferencedDataLoaded.htm)|
(Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsValid](P_Grasshopper_Rhinoceros_ModelContent_IsValid.htm)|  (Inherited from
[ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Protected property](../icons/protproperty.gif)|
[IsValidWhyNot](P_Grasshopper_Rhinoceros_ModelContent_IsValidWhyNot.htm)|
(Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
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
[Tags](P_Grasshopper_Rhinoceros_ModelContent_Tags.htm)|  (Inherited from
[ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Protected property](../icons/protproperty.gif)|
[TypeDescription](P_Grasshopper_Rhinoceros_ModelData_TypeDescription.htm)|
(Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).)  
![Public property](../icons/pubproperty.gif)|
[TypeName](P_Grasshopper_Rhinoceros_Render_ModelRenderContent_TypeName.htm)|
(Overrides ModelData.TypeName.)  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Protected method](../icons/protmethod.gif)|
[AsFrozen](M_Grasshopper_Rhinoceros_ModelContent_AsFrozen.htm)|  Try to obtain
a dereferenced snapshot of itself.  (Inherited from
[ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
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
![Protected method](../icons/protmethod.gif)|
[InternaliseData](M_Grasshopper_Rhinoceros_ModelContent_InternaliseData.htm)|
(Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Protected method](../icons/protmethod.gif)|
[LoadReferencedData](M_Grasshopper_Rhinoceros_ModelContent_LoadReferencedData.htm)|
(Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Protected method](../icons/protmethod.gif)|
[Read](M_Grasshopper_Rhinoceros_ModelContent_Read.htm)|  (Inherited from
[ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Protected method](../icons/protmethod.gif)|
[RuntimeId](M_Grasshopper_Rhinoceros_ModelContent_RuntimeId.htm)|  (Inherited
from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Public method](../icons/pubmethod.gif)|
[ToAttributes](M_Grasshopper_Rhinoceros_Render_ModelRenderContent_ToAttributes.htm)|  
![Public method](../icons/pubmethod.gif)|
[ToDetails](M_Grasshopper_Rhinoceros_ModelData_ToDetails.htm)|  (Inherited
from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).)  
![Public method](../icons/pubmethod.gif)|
[TooltipString](M_Grasshopper_Rhinoceros_ModelContent_TooltipString.htm)|
(Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Rhinoceros_ModelContent_ToString.htm)|  (Inherited
from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Protected method](../icons/protmethod.gif)|
[UnloadReferencedData](M_Grasshopper_Rhinoceros_ModelContent_UnloadReferencedData.htm)|
(Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Protected method](../icons/protmethod.gif)|
[Write](M_Grasshopper_Rhinoceros_ModelContent_Write.htm)|  (Inherited from
[ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
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

[Grasshopper.Rhinoceros.Render Namespace](N_Grasshopper_Rhinoceros_Render.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

