---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle.htm
scraped_at: 2025-09-08T16:23:03.017250
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Rhinoceros.Annotations](../html/N_Grasshopper_Rhinoceros_Annotations.htm
"Grasshopper.Rhinoceros.Annotations")

[ModelAnnotationStyle
Class](../html/T_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle.htm
"ModelAnnotationStyle Class")

[ModelAnnotationStyle Constructor
](../html/Overload_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle__ctor.htm
"ModelAnnotationStyle Constructor ")

[ModelAnnotationStyle
Properties](../html/Properties_T_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle.htm
"ModelAnnotationStyle Properties")

[ModelAnnotationStyle
Methods](../html/Methods_T_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle.htm
"ModelAnnotationStyle Methods")

[ModelAnnotationStyle Type
Conversions](../html/Operators_T_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle.htm
"ModelAnnotationStyle Type Conversions")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# ModelAnnotationStyle Class  
  
---  
  
Represents a Rhino model annotation style. Wraps the functionality of the
DimensionStyle type.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.RhinocerosModelData](T_Grasshopper_Rhinoceros_ModelData.htm)  
[Grasshopper.RhinocerosModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm)  
[Grasshopper.RhinocerosModelComponentContent](T_Grasshopper_Rhinoceros_ModelComponentContent.htm)  
Grasshopper.Rhinoceros.AnnotationsModelAnnotationStyle  

**Namespace:**
[Grasshopper.Rhinoceros.Annotations](N_Grasshopper_Rhinoceros_Annotations.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class ModelAnnotationStyle : ModelComponentContent, 
    	IGH_BakeAwareData
    
    
    Public NotInheritable Class ModelAnnotationStyle
    	Inherits ModelComponentContent
    	Implements IGH_BakeAwareData

The ModelAnnotationStyle type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[ModelAnnotationStyle](M_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle__ctor.htm)|
Initializes a new instance of the ModelAnnotationStyle class  
![Public method](../icons/pubmethod.gif)|
[ModelAnnotationStyle(ModelAnnotationStyleAttributes)](M_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle__ctor_1.htm)|
Initializes a new instance of the ModelAnnotationStyle class  
![Public method](../icons/pubmethod.gif)|
[ModelAnnotationStyle(DimensionStyle)](M_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle__ctor_2.htm)|
Initializes a new instance of the ModelAnnotationStyle class  
![Public method](../icons/pubmethod.gif)|
[ModelAnnotationStyle(Guid)](M_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle__ctor_3.htm)|
Initializes a new instance of the ModelAnnotationStyle class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[ArrowSettings](P_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_ArrowSettings.htm)|  
![Public property](../icons/pubproperty.gif)|
[DimensionScale](P_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_DimensionScale.htm)|  
![Public property](../icons/pubproperty.gif)|
[DimensionSettings](P_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_DimensionSettings.htm)|  
![Public property](../icons/pubproperty.gif)|
[Id](P_Grasshopper_Rhinoceros_ModelContent_Id.htm)|  (Inherited from
[ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsValid](P_Grasshopper_Rhinoceros_ModelContent_IsValid.htm)|  (Inherited from
[ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Public property](../icons/pubproperty.gif)|
[LeaderSettings](P_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_LeaderSettings.htm)|  
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
[TextSettings](P_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_TextSettings.htm)|  
![Public property](../icons/pubproperty.gif)|
[ToleranceSettings](P_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_ToleranceSettings.htm)|  
![Public property](../icons/pubproperty.gif)|
[UnitsSettings](P_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_UnitsSettings.htm)|  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[Unset](P_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_Unset.htm)|  
![Public property](../icons/pubproperty.gif)|
[UserText](P_Grasshopper_Rhinoceros_ModelComponentContent_UserText.htm)|
(Inherited from
[ModelComponentContent](T_Grasshopper_Rhinoceros_ModelComponentContent.htm).)  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Cast](M_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_Cast.htm)|  
![Public method](../icons/pubmethod.gif)|
[CastToT(T)](M_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_CastTo__1.htm)|
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
[GetHashCode](M_Grasshopper_Rhinoceros_ModelContent_GetHashCode.htm)|
(Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Public method](../icons/pubmethod.gif)|
[ToAttributes](M_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_ToAttributes.htm)|  
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
member](../icons/static.gif)| [(ModelAnnotationStyleAttributes to
ModelAnnotationStyle)](M_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_op_Implicit.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [(DimensionStyle to
ModelAnnotationStyle)](M_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_op_Implicit_1.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [(String to
ModelAnnotationStyle)](M_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_op_Implicit_2.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros.Annotations
Namespace](N_Grasshopper_Rhinoceros_Annotations.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

