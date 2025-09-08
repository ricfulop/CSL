---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Rhinoceros_Model_ModelLayer.htm
scraped_at: 2025-09-08T16:24:16.339641
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Rhinoceros.Model](../html/N_Grasshopper_Rhinoceros_Model.htm
"Grasshopper.Rhinoceros.Model")

[ModelLayer Class](../html/T_Grasshopper_Rhinoceros_Model_ModelLayer.htm
"ModelLayer Class")

[ModelLayer Constructor
](../html/Overload_Grasshopper_Rhinoceros_Model_ModelLayer__ctor.htm
"ModelLayer Constructor ")

[ModelLayer
Properties](../html/Properties_T_Grasshopper_Rhinoceros_Model_ModelLayer.htm
"ModelLayer Properties")

[ModelLayer
Methods](../html/Methods_T_Grasshopper_Rhinoceros_Model_ModelLayer.htm
"ModelLayer Methods")

[ModelLayer Type
Conversions](../html/Operators_T_Grasshopper_Rhinoceros_Model_ModelLayer.htm
"ModelLayer Type Conversions")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# ModelLayer Class  
  
---  
  
Represents a Rhino model layer. Wraps the functionality of the Layer type.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.RhinocerosModelData](T_Grasshopper_Rhinoceros_ModelData.htm)  
[Grasshopper.RhinocerosModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm)  
[Grasshopper.RhinocerosModelComponentContent](T_Grasshopper_Rhinoceros_ModelComponentContent.htm)  
Grasshopper.Rhinoceros.ModelModelLayer  

**Namespace:**
[Grasshopper.Rhinoceros.Model](N_Grasshopper_Rhinoceros_Model.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class ModelLayer : ModelComponentContent, 
    	IGH_BakeAwareData
    
    
    Public NotInheritable Class ModelLayer
    	Inherits ModelComponentContent
    	Implements IGH_BakeAwareData

The ModelLayer type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[ModelLayer](M_Grasshopper_Rhinoceros_Model_ModelLayer__ctor.htm)| Initializes
a new instance of the ModelLayer class  
![Public method](../icons/pubmethod.gif)|
[ModelLayer(ModelLayerAttributes)](M_Grasshopper_Rhinoceros_Model_ModelLayer__ctor_1.htm)|
Initializes a new instance of the ModelLayer class  
![Public method](../icons/pubmethod.gif)|
[ModelLayer(Guid)](M_Grasshopper_Rhinoceros_Model_ModelLayer__ctor_3.htm)|
Initializes a new instance of the ModelLayer class  
![Public method](../icons/pubmethod.gif)|
[ModelLayer(Layer)](M_Grasshopper_Rhinoceros_Model_ModelLayer__ctor_2.htm)|
Initializes a new instance of the ModelLayer class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[DisplayColor](P_Grasshopper_Rhinoceros_Model_ModelLayer_DisplayColor.htm)|  
![Public property](../icons/pubproperty.gif)|
[DraftingColor](P_Grasshopper_Rhinoceros_Model_ModelLayer_DraftingColor.htm)|  
![Public property](../icons/pubproperty.gif)|
[Hidden](P_Grasshopper_Rhinoceros_Model_ModelLayer_Hidden.htm)|  
![Public property](../icons/pubproperty.gif)|
[HiddenOnModel](P_Grasshopper_Rhinoceros_Model_ModelLayer_HiddenOnModel.htm)|  
![Public property](../icons/pubproperty.gif)|
[HiddenOnNewDetail](P_Grasshopper_Rhinoceros_Model_ModelLayer_HiddenOnNewDetail.htm)|  
![Public property](../icons/pubproperty.gif)|
[Id](P_Grasshopper_Rhinoceros_ModelContent_Id.htm)|  (Inherited from
[ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsValid](P_Grasshopper_Rhinoceros_ModelContent_IsValid.htm)|  (Inherited from
[ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Public property](../icons/pubproperty.gif)|
[Linetype](P_Grasshopper_Rhinoceros_Model_ModelLayer_Linetype.htm)|  
![Public property](../icons/pubproperty.gif)|
[LineWeight](P_Grasshopper_Rhinoceros_Model_ModelLayer_LineWeight.htm)|  
![Public property](../icons/pubproperty.gif)|
[Locked](P_Grasshopper_Rhinoceros_Model_ModelLayer_Locked.htm)|  
![Public property](../icons/pubproperty.gif)|
[Material](P_Grasshopper_Rhinoceros_Model_ModelLayer_Material.htm)|  
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
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[Unset](P_Grasshopper_Rhinoceros_Model_ModelLayer_Unset.htm)|  
![Public property](../icons/pubproperty.gif)|
[UserText](P_Grasshopper_Rhinoceros_ModelComponentContent_UserText.htm)|
(Inherited from
[ModelComponentContent](T_Grasshopper_Rhinoceros_ModelComponentContent.htm).)  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Cast](M_Grasshopper_Rhinoceros_Model_ModelLayer_Cast.htm)|  
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
[ToAttributes](M_Grasshopper_Rhinoceros_Model_ModelLayer_ToAttributes.htm)|  
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
member](../icons/static.gif)| [(ModelLayerAttributes to
ModelLayer)](M_Grasshopper_Rhinoceros_Model_ModelLayer_op_Implicit.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [(Layer to
ModelLayer)](M_Grasshopper_Rhinoceros_Model_ModelLayer_op_Implicit_1.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [(String to
ModelLayer)](M_Grasshopper_Rhinoceros_Model_ModelLayer_op_Implicit_2.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros.Model Namespace](N_Grasshopper_Rhinoceros_Model.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

