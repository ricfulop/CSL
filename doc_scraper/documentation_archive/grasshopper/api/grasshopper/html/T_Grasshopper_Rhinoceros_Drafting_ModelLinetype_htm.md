---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Rhinoceros_Drafting_ModelLinetype.htm
scraped_at: 2025-09-08T16:23:51.218959
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Rhinoceros.Drafting](../html/N_Grasshopper_Rhinoceros_Drafting.htm
"Grasshopper.Rhinoceros.Drafting")

[ModelLinetype
Class](../html/T_Grasshopper_Rhinoceros_Drafting_ModelLinetype.htm
"ModelLinetype Class")

[ModelLinetype Constructor
](../html/Overload_Grasshopper_Rhinoceros_Drafting_ModelLinetype__ctor.htm
"ModelLinetype Constructor ")

[ModelLinetype
Properties](../html/Properties_T_Grasshopper_Rhinoceros_Drafting_ModelLinetype.htm
"ModelLinetype Properties")

[ModelLinetype
Methods](../html/Methods_T_Grasshopper_Rhinoceros_Drafting_ModelLinetype.htm
"ModelLinetype Methods")

[ModelLinetype Type
Conversions](../html/Operators_T_Grasshopper_Rhinoceros_Drafting_ModelLinetype.htm
"ModelLinetype Type Conversions")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# ModelLinetype Class  
  
---  
  
Represents a Rhino model linetype. Wraps the functionality of the Linetype
type.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.RhinocerosModelData](T_Grasshopper_Rhinoceros_ModelData.htm)  
[Grasshopper.RhinocerosModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm)  
[Grasshopper.RhinocerosModelComponentContent](T_Grasshopper_Rhinoceros_ModelComponentContent.htm)  
Grasshopper.Rhinoceros.DraftingModelLinetype  

**Namespace:**
[Grasshopper.Rhinoceros.Drafting](N_Grasshopper_Rhinoceros_Drafting.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class ModelLinetype : ModelComponentContent, 
    	IGH_BakeAwareData
    
    
    Public NotInheritable Class ModelLinetype
    	Inherits ModelComponentContent
    	Implements IGH_BakeAwareData

The ModelLinetype type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[ModelLinetype](M_Grasshopper_Rhinoceros_Drafting_ModelLinetype__ctor.htm)|
Initializes a new instance of the ModelLinetype class  
![Public method](../icons/pubmethod.gif)|
[ModelLinetype(ModelLinetypeAttributes)](M_Grasshopper_Rhinoceros_Drafting_ModelLinetype__ctor_1.htm)|
Initializes a new instance of the ModelLinetype class  
![Public method](../icons/pubmethod.gif)|
[ModelLinetype(Guid)](M_Grasshopper_Rhinoceros_Drafting_ModelLinetype__ctor_3.htm)|
Initializes a new instance of the ModelLinetype class  
![Public method](../icons/pubmethod.gif)|
[ModelLinetype(Linetype)](M_Grasshopper_Rhinoceros_Drafting_ModelLinetype__ctor_2.htm)|
Initializes a new instance of the ModelLinetype class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[CapStyle](P_Grasshopper_Rhinoceros_Drafting_ModelLinetype_CapStyle.htm)|  
![Public property](../icons/pubproperty.gif)|
[Id](P_Grasshopper_Rhinoceros_ModelContent_Id.htm)|  (Inherited from
[ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsValid](P_Grasshopper_Rhinoceros_ModelContent_IsValid.htm)|  (Inherited from
[ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Public property](../icons/pubproperty.gif)|
[JoinStyle](P_Grasshopper_Rhinoceros_Drafting_ModelLinetype_JoinStyle.htm)|  
![Public property](../icons/pubproperty.gif)|
[Name](P_Grasshopper_Rhinoceros_Drafting_ModelLinetype_Name.htm)|  (Overrides
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
[Segments](P_Grasshopper_Rhinoceros_Drafting_ModelLinetype_Segments.htm)|  
![Public property](../icons/pubproperty.gif)|
[Tags](P_Grasshopper_Rhinoceros_ModelContent_Tags.htm)|  (Inherited from
[ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Public property](../icons/pubproperty.gif)|
[TaperPoints](P_Grasshopper_Rhinoceros_Drafting_ModelLinetype_TaperPoints.htm)|  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[Unset](P_Grasshopper_Rhinoceros_Drafting_ModelLinetype_Unset.htm)|  
![Public property](../icons/pubproperty.gif)|
[UserText](P_Grasshopper_Rhinoceros_ModelComponentContent_UserText.htm)|
(Inherited from
[ModelComponentContent](T_Grasshopper_Rhinoceros_ModelComponentContent.htm).)  
![Public property](../icons/pubproperty.gif)|
[Width](P_Grasshopper_Rhinoceros_Drafting_ModelLinetype_Width.htm)|  
![Public property](../icons/pubproperty.gif)|
[WidthUnits](P_Grasshopper_Rhinoceros_Drafting_ModelLinetype_WidthUnits.htm)|  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Cast](M_Grasshopper_Rhinoceros_Drafting_ModelLinetype_Cast.htm)|  
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
[ToAttributes](M_Grasshopper_Rhinoceros_Drafting_ModelLinetype_ToAttributes.htm)|  
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
member](../icons/static.gif)| [(ModelLinetypeAttributes to
ModelLinetype)](M_Grasshopper_Rhinoceros_Drafting_ModelLinetype_op_Implicit.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [(Linetype to
ModelLinetype)](M_Grasshopper_Rhinoceros_Drafting_ModelLinetype_op_Implicit_1.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [(String to
ModelLinetype)](M_Grasshopper_Rhinoceros_Drafting_ModelLinetype_op_Implicit_2.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros.Drafting
Namespace](N_Grasshopper_Rhinoceros_Drafting.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

