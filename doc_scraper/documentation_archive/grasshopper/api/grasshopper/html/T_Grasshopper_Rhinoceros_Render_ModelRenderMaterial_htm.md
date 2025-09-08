---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Rhinoceros_Render_ModelRenderMaterial.htm
scraped_at: 2025-09-08T16:24:39.436070
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Rhinoceros.Render](../html/N_Grasshopper_Rhinoceros_Render.htm
"Grasshopper.Rhinoceros.Render")

[ModelRenderMaterial
Class](../html/T_Grasshopper_Rhinoceros_Render_ModelRenderMaterial.htm
"ModelRenderMaterial Class")

[ModelRenderMaterial Constructor
](../html/Overload_Grasshopper_Rhinoceros_Render_ModelRenderMaterial__ctor.htm
"ModelRenderMaterial Constructor ")

[ModelRenderMaterial
Properties](../html/Properties_T_Grasshopper_Rhinoceros_Render_ModelRenderMaterial.htm
"ModelRenderMaterial Properties")

[ModelRenderMaterial
Methods](../html/Methods_T_Grasshopper_Rhinoceros_Render_ModelRenderMaterial.htm
"ModelRenderMaterial Methods")

[ModelRenderMaterial Type
Conversions](../html/Operators_T_Grasshopper_Rhinoceros_Render_ModelRenderMaterial.htm
"ModelRenderMaterial Type Conversions")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# ModelRenderMaterial Class  
  
---  
  
Represents a Rhino render material. Wraps the functionality of the
RenderMaterial type.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.RhinocerosModelData](T_Grasshopper_Rhinoceros_ModelData.htm)  
[Grasshopper.RhinocerosModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm)  
[Grasshopper.Rhinoceros.RenderModelRenderContent](T_Grasshopper_Rhinoceros_Render_ModelRenderContent.htm)  
Grasshopper.Rhinoceros.RenderModelRenderMaterial  

**Namespace:**
[Grasshopper.Rhinoceros.Render](N_Grasshopper_Rhinoceros_Render.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class ModelRenderMaterial : ModelRenderContent, 
    	IGH_BakeAwareData
    
    
    Public NotInheritable Class ModelRenderMaterial
    	Inherits ModelRenderContent
    	Implements IGH_BakeAwareData

The ModelRenderMaterial type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[ModelRenderMaterial](M_Grasshopper_Rhinoceros_Render_ModelRenderMaterial__ctor.htm)|
Initializes a new instance of the ModelRenderMaterial class  
![Public method](../icons/pubmethod.gif)|
[ModelRenderMaterial(ModelRenderMaterialAttributes)](M_Grasshopper_Rhinoceros_Render_ModelRenderMaterial__ctor_1.htm)|
Initializes a new instance of the ModelRenderMaterial class  
![Public method](../icons/pubmethod.gif)|
[ModelRenderMaterial(Guid)](M_Grasshopper_Rhinoceros_Render_ModelRenderMaterial__ctor_4.htm)|
Initializes a new instance of the ModelRenderMaterial class  
![Public method](../icons/pubmethod.gif)|
[ModelRenderMaterial(Material)](M_Grasshopper_Rhinoceros_Render_ModelRenderMaterial__ctor_2.htm)|
Initializes a new instance of the ModelRenderMaterial class  
![Public method](../icons/pubmethod.gif)|
[ModelRenderMaterial(RenderMaterial)](M_Grasshopper_Rhinoceros_Render_ModelRenderMaterial__ctor_3.htm)|
Initializes a new instance of the ModelRenderMaterial class  
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
[Name](P_Grasshopper_Rhinoceros_Render_ModelRenderMaterial_Name.htm)|
(Overrides
[ModelContentName](P_Grasshopper_Rhinoceros_ModelContent_Name.htm).)  
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
[TypeName](P_Grasshopper_Rhinoceros_Render_ModelRenderMaterial_TypeName.htm)|
(Overrides
[ModelRenderContentTypeName](P_Grasshopper_Rhinoceros_Render_ModelRenderContent_TypeName.htm).)  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[Unset](P_Grasshopper_Rhinoceros_Render_ModelRenderMaterial_Unset.htm)|  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Cast](M_Grasshopper_Rhinoceros_Render_ModelRenderMaterial_Cast.htm)|  
![Public method](../icons/pubmethod.gif)|
[CastToT(T)](M_Grasshopper_Rhinoceros_ModelContent_CastTo__1.htm)|  (Inherited
from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToT(T)](M_Grasshopper_Rhinoceros_ModelData_CastTo__1.htm)|  (Inherited
from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToT(T)](M_Grasshopper_Rhinoceros_Render_ModelRenderMaterial_CastTo__1.htm)|
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
[ToAttributes](M_Grasshopper_Rhinoceros_Render_ModelRenderMaterial_ToAttributes.htm)|  
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
member](../icons/static.gif)| [(ModelRenderMaterialAttributes to
ModelRenderMaterial)](M_Grasshopper_Rhinoceros_Render_ModelRenderMaterial_op_Implicit.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [(ColorRGBA to
ModelRenderMaterial)](M_Grasshopper_Rhinoceros_Render_ModelRenderMaterial_op_Implicit_1.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [(Material to
ModelRenderMaterial)](M_Grasshopper_Rhinoceros_Render_ModelRenderMaterial_op_Implicit_2.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [(RenderMaterial to
ModelRenderMaterial)](M_Grasshopper_Rhinoceros_Render_ModelRenderMaterial_op_Implicit_3.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [(String to
ModelRenderMaterial)](M_Grasshopper_Rhinoceros_Render_ModelRenderMaterial_op_Implicit_4.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros.Render Namespace](N_Grasshopper_Rhinoceros_Render.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

