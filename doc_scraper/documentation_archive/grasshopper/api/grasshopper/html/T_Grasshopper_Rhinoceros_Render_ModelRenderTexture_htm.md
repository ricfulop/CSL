---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Rhinoceros_Render_ModelRenderTexture.htm
scraped_at: 2025-09-08T16:24:45.436388
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Rhinoceros.Render](../html/N_Grasshopper_Rhinoceros_Render.htm
"Grasshopper.Rhinoceros.Render")

[ModelRenderTexture
Class](../html/T_Grasshopper_Rhinoceros_Render_ModelRenderTexture.htm
"ModelRenderTexture Class")

[ModelRenderTexture Constructor
](../html/Overload_Grasshopper_Rhinoceros_Render_ModelRenderTexture__ctor.htm
"ModelRenderTexture Constructor ")

[ModelRenderTexture
Properties](../html/Properties_T_Grasshopper_Rhinoceros_Render_ModelRenderTexture.htm
"ModelRenderTexture Properties")

[ModelRenderTexture
Methods](../html/Methods_T_Grasshopper_Rhinoceros_Render_ModelRenderTexture.htm
"ModelRenderTexture Methods")

[ModelRenderTexture Type
Conversions](../html/Operators_T_Grasshopper_Rhinoceros_Render_ModelRenderTexture.htm
"ModelRenderTexture Type Conversions")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# ModelRenderTexture Class  
  
---  
  
Represents a Rhino render texture. Wraps the functionality of the
RenderTexture type.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.RhinocerosModelData](T_Grasshopper_Rhinoceros_ModelData.htm)  
[Grasshopper.RhinocerosModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm)  
[Grasshopper.Rhinoceros.RenderModelRenderContent](T_Grasshopper_Rhinoceros_Render_ModelRenderContent.htm)  
Grasshopper.Rhinoceros.RenderModelRenderTexture  

**Namespace:**
[Grasshopper.Rhinoceros.Render](N_Grasshopper_Rhinoceros_Render.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class ModelRenderTexture : ModelRenderContent, 
    	IGH_BakeAwareData
    
    
    Public NotInheritable Class ModelRenderTexture
    	Inherits ModelRenderContent
    	Implements IGH_BakeAwareData

The ModelRenderTexture type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[ModelRenderTexture](M_Grasshopper_Rhinoceros_Render_ModelRenderTexture__ctor.htm)|
Initializes a new instance of the ModelRenderTexture class  
![Public method](../icons/pubmethod.gif)|
[ModelRenderTexture(ModelRenderTextureAttributes)](M_Grasshopper_Rhinoceros_Render_ModelRenderTexture__ctor_1.htm)|
Initializes a new instance of the ModelRenderTexture class  
![Public method](../icons/pubmethod.gif)|
[ModelRenderTexture(Guid)](M_Grasshopper_Rhinoceros_Render_ModelRenderTexture__ctor_3.htm)|
Initializes a new instance of the ModelRenderTexture class  
![Public method](../icons/pubmethod.gif)|
[ModelRenderTexture(RenderTexture)](M_Grasshopper_Rhinoceros_Render_ModelRenderTexture__ctor_2.htm)|
Initializes a new instance of the ModelRenderTexture class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
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
[Tags](P_Grasshopper_Rhinoceros_ModelContent_Tags.htm)|  (Inherited from
[ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Public property](../icons/pubproperty.gif)|
[TypeName](P_Grasshopper_Rhinoceros_Render_ModelRenderTexture_TypeName.htm)|
(Overrides
[ModelRenderContentTypeName](P_Grasshopper_Rhinoceros_Render_ModelRenderContent_TypeName.htm).)  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Cast](M_Grasshopper_Rhinoceros_Render_ModelRenderTexture_Cast.htm)|  
![Public method](../icons/pubmethod.gif)|
[CastToT(T)](M_Grasshopper_Rhinoceros_ModelContent_CastTo__1.htm)|  (Inherited
from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToT(T)](M_Grasshopper_Rhinoceros_ModelData_CastTo__1.htm)|  (Inherited
from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToT(T)](M_Grasshopper_Rhinoceros_Render_ModelRenderTexture_CastTo__1.htm)|
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
[ToAttributes](M_Grasshopper_Rhinoceros_Render_ModelRenderTexture_ToAttributes.htm)|  
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
member](../icons/static.gif)| [(ModelRenderTextureAttributes to
ModelRenderTexture)](M_Grasshopper_Rhinoceros_Render_ModelRenderTexture_op_Implicit.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [(ColorRGBA to
ModelRenderTexture)](M_Grasshopper_Rhinoceros_Render_ModelRenderTexture_op_Implicit_1.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [(RenderTexture to
ModelRenderTexture)](M_Grasshopper_Rhinoceros_Render_ModelRenderTexture_op_Implicit_2.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [(String to
ModelRenderTexture)](M_Grasshopper_Rhinoceros_Render_ModelRenderTexture_op_Implicit_3.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros.Render Namespace](N_Grasshopper_Rhinoceros_Render.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

