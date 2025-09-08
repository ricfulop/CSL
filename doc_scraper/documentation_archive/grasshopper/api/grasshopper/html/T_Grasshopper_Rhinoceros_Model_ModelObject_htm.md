---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Rhinoceros_Model_ModelObject.htm
scraped_at: 2025-09-08T16:24:18.320072
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Rhinoceros.Model](../html/N_Grasshopper_Rhinoceros_Model.htm
"Grasshopper.Rhinoceros.Model")

[ModelObject Class](../html/T_Grasshopper_Rhinoceros_Model_ModelObject.htm
"ModelObject Class")

[ModelObject Constructor
](../html/Overload_Grasshopper_Rhinoceros_Model_ModelObject__ctor.htm
"ModelObject Constructor ")

[ModelObject
Properties](../html/Properties_T_Grasshopper_Rhinoceros_Model_ModelObject.htm
"ModelObject Properties")

[ModelObject
Methods](../html/Methods_T_Grasshopper_Rhinoceros_Model_ModelObject.htm
"ModelObject Methods")

[ModelObject Type
Conversions](../html/Operators_T_Grasshopper_Rhinoceros_Model_ModelObject.htm
"ModelObject Type Conversions")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# ModelObject Class  
  
---  
  
Represents a Rhino model object. Wraps the functionality of the RhinoObject
type.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.RhinocerosModelData](T_Grasshopper_Rhinoceros_ModelData.htm)  
[Grasshopper.RhinocerosModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm)  
[Grasshopper.RhinocerosModelComponentContent](T_Grasshopper_Rhinoceros_ModelComponentContent.htm)  
Grasshopper.Rhinoceros.ModelModelObject  

**Namespace:**
[Grasshopper.Rhinoceros.Model](N_Grasshopper_Rhinoceros_Model.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class ModelObject : ModelComponentContent, 
    	IGH_BakeAwareData, IGH_PreviewData, IGH_PreviewMeshData, IGH_RenderAwareData
    
    
    Public NotInheritable Class ModelObject
    	Inherits ModelComponentContent
    	Implements IGH_BakeAwareData, IGH_PreviewData, IGH_PreviewMeshData, IGH_RenderAwareData

The ModelObject type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[ModelObject](M_Grasshopper_Rhinoceros_Model_ModelObject__ctor.htm)|
Initializes a new instance of the ModelObject class  
![Public method](../icons/pubmethod.gif)|
[ModelObject(ModelObjectAttributes)](M_Grasshopper_Rhinoceros_Model_ModelObject__ctor_1.htm)|
Initializes a new instance of the ModelObject class  
![Public method](../icons/pubmethod.gif)|
[ModelObject(Guid)](M_Grasshopper_Rhinoceros_Model_ModelObject__ctor_5.htm)|
Initializes a new instance of the ModelObject class  
![Public method](../icons/pubmethod.gif)|
[ModelObject(RhinoObject)](M_Grasshopper_Rhinoceros_Model_ModelObject__ctor_2.htm)|
Initializes a new instance of the ModelObject class  
![Public method](../icons/pubmethod.gif)| [ModelObject(RhinoDoc,
ObjectAttributes)](M_Grasshopper_Rhinoceros_Model_ModelObject__ctor_3.htm)|
Initializes a new instance of the ModelObject class  
![Public method](../icons/pubmethod.gif)| [ModelObject(RhinoDoc,
ObjectAttributes,
GeometryBase)](M_Grasshopper_Rhinoceros_Model_ModelObject__ctor_4.htm)|
Initializes a new instance of the ModelObject class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Display](P_Grasshopper_Rhinoceros_Model_ModelObject_Display.htm)|  
![Public property](../icons/pubproperty.gif)|
[Drafting](P_Grasshopper_Rhinoceros_Model_ModelObject_Drafting.htm)|  
![Public property](../icons/pubproperty.gif)|
[Id](P_Grasshopper_Rhinoceros_ModelContent_Id.htm)|  (Inherited from
[ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsValid](P_Grasshopper_Rhinoceros_Model_ModelObject_IsValid.htm)|  (Overrides
[ModelContentIsValid](P_Grasshopper_Rhinoceros_ModelContent_IsValid.htm).)  
![Public property](../icons/pubproperty.gif)|
[Layer](P_Grasshopper_Rhinoceros_Model_ModelObject_Layer.htm)|  
![Public property](../icons/pubproperty.gif)|
[Name](P_Grasshopper_Rhinoceros_ModelContent_Name.htm)|  (Inherited from
[ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Public property](../icons/pubproperty.gif)|
[Notes](P_Grasshopper_Rhinoceros_ModelContent_Notes.htm)|  (Inherited from
[ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Public property](../icons/pubproperty.gif)|
[ObjectType](P_Grasshopper_Rhinoceros_Model_ModelObject_ObjectType.htm)|  
![Public property](../icons/pubproperty.gif)|
[Parent](P_Grasshopper_Rhinoceros_ModelContent_Parent.htm)|  (Inherited from
[ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Public property](../icons/pubproperty.gif)|
[Path](P_Grasshopper_Rhinoceros_ModelContent_Path.htm)|  (Inherited from
[ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Public property](../icons/pubproperty.gif)|
[Render](P_Grasshopper_Rhinoceros_Model_ModelObject_Render.htm)|  
![Public property](../icons/pubproperty.gif)|
[Tags](P_Grasshopper_Rhinoceros_ModelContent_Tags.htm)|  (Inherited from
[ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Public property](../icons/pubproperty.gif)|
[TypeName](P_Grasshopper_Rhinoceros_Model_ModelObject_TypeName.htm)|
(Overrides ModelData.TypeName.)  
![Public property](../icons/pubproperty.gif)|
[Url](P_Grasshopper_Rhinoceros_Model_ModelObject_Url.htm)|  
![Public property](../icons/pubproperty.gif)|
[UserText](P_Grasshopper_Rhinoceros_ModelComponentContent_UserText.htm)|
(Inherited from
[ModelComponentContent](T_Grasshopper_Rhinoceros_ModelComponentContent.htm).)  
![Public property](../icons/pubproperty.gif)|
[Visibility](P_Grasshopper_Rhinoceros_Model_ModelObject_Visibility.htm)|  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Cast](M_Grasshopper_Rhinoceros_Model_ModelObject_Cast.htm)|  
![Public method](../icons/pubmethod.gif)|
[CastToT(T)](M_Grasshopper_Rhinoceros_Model_ModelObject_CastTo__1.htm)|
(Overrides
[ModelContentCastToT(T)](M_Grasshopper_Rhinoceros_ModelContent_CastTo__1.htm).)  
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
[GetBoundingBox](M_Grasshopper_Rhinoceros_Model_ModelObject_GetBoundingBox.htm)|  
![Public method](../icons/pubmethod.gif)|
[GetHashCode](M_Grasshopper_Rhinoceros_ModelContent_GetHashCode.htm)|
(Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Public method](../icons/pubmethod.gif)|
[ToAttributes](M_Grasshopper_Rhinoceros_Model_ModelObject_ToAttributes.htm)|  
![Public method](../icons/pubmethod.gif)|
[ToDetails](M_Grasshopper_Rhinoceros_ModelData_ToDetails.htm)|  (Inherited
from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).)  
![Public method](../icons/pubmethod.gif)|
[TooltipString](M_Grasshopper_Rhinoceros_Model_ModelObject_TooltipString.htm)|
(Overrides
[ModelContentTooltipString](M_Grasshopper_Rhinoceros_ModelContent_TooltipString.htm).)  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Rhinoceros_Model_ModelObject_ToString.htm)|
(Overrides
[ModelContentToString](M_Grasshopper_Rhinoceros_ModelContent_ToString.htm).)  
Top

![](../icons/SectionExpanded.png)Operators

| Name| Description  
---|---|---  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [(ModelObjectAttributes to
ModelObject)](M_Grasshopper_Rhinoceros_Model_ModelObject_op_Implicit.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [(RhinoObject to
ModelObject)](M_Grasshopper_Rhinoceros_Model_ModelObject_op_Implicit_1.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros.Model Namespace](N_Grasshopper_Rhinoceros_Model.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

