---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_Attributes.htm
scraped_at: 2025-09-08T16:23:04.016285
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Rhinoceros.Annotations](../html/N_Grasshopper_Rhinoceros_Annotations.htm
"Grasshopper.Rhinoceros.Annotations")

[ModelAnnotationStyle.Attributes
Class](../html/T_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_Attributes.htm
"ModelAnnotationStyle.Attributes Class")

[ModelAnnotationStyle.Attributes Constructor
](../html/M_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_Attributes__ctor.htm
"ModelAnnotationStyle.Attributes Constructor ")

[Attributes
Properties](../html/Properties_T_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_Attributes.htm
"Attributes Properties")

[Attributes
Methods](../html/Methods_T_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_Attributes.htm
"Attributes Methods")

[Attributes Type
Conversions](../html/Operators_T_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_Attributes.htm
"Attributes Type Conversions")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# ModelAnnotationStyleAttributes Class  
  
---  
  
![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.RhinocerosModelDataAttributes](T_Grasshopper_Rhinoceros_ModelData_Attributes.htm)  
[Grasshopper.RhinocerosModelContentAttributes](T_Grasshopper_Rhinoceros_ModelContent_Attributes.htm)  
[Grasshopper.RhinocerosModelComponentContentAttributes](T_Grasshopper_Rhinoceros_ModelComponentContent_Attributes.htm)  
Grasshopper.Rhinoceros.AnnotationsModelAnnotationStyleAttributes  

**Namespace:**
[Grasshopper.Rhinoceros.Annotations](N_Grasshopper_Rhinoceros_Annotations.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class Attributes : ModelComponentContentAttributes, 
    	IEquatable<ModelAnnotationStyleAttributes>
    
    
    Public NotInheritable Class Attributes
    	Inherits ModelComponentContentAttributes
    	Implements IEquatable(Of ModelAnnotationStyleAttributes)

The ModelAnnotationStyleAttributes type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[ModelAnnotationStyleAttributes](M_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_Attributes__ctor.htm)|
Initializes a new instance of the ModelAnnotationStyleAttributes class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[ArrowSettings](P_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_Attributes_ArrowSettings.htm)|  
![Public property](../icons/pubproperty.gif)|
[DimensionScale](P_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_Attributes_DimensionScale.htm)|  
![Public property](../icons/pubproperty.gif)|
[DimensionSettings](P_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_Attributes_DimensionSettings.htm)|  
![Public property](../icons/pubproperty.gif)|
[LeaderSettings](P_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_Attributes_LeaderSettings.htm)|  
![Public property](../icons/pubproperty.gif)|
[Name](P_Grasshopper_Rhinoceros_ModelContent_Attributes_Name.htm)|  The last
component of the element Path.  (Inherited from
[ModelContentAttributes](T_Grasshopper_Rhinoceros_ModelContent_Attributes.htm).)  
![Public property](../icons/pubproperty.gif)|
[Notes](P_Grasshopper_Rhinoceros_ModelContent_Attributes_Notes.htm)|
(Inherited from
[ModelContentAttributes](T_Grasshopper_Rhinoceros_ModelContent_Attributes.htm).)  
![Public property](../icons/pubproperty.gif)|
[Parent](P_Grasshopper_Rhinoceros_ModelContent_Attributes_Parent.htm)|  Path
of the parent element in 'Root::Parent' format if nested.  (Inherited from
[ModelContentAttributes](T_Grasshopper_Rhinoceros_ModelContent_Attributes.htm).)  
![Public property](../icons/pubproperty.gif)|
[Path](P_Grasshopper_Rhinoceros_ModelContent_Attributes_Path.htm)|  Full
content path in 'Root::Parent::Name' format if is nested.  (Inherited from
[ModelContentAttributes](T_Grasshopper_Rhinoceros_ModelContent_Attributes.htm).)  
![Public property](../icons/pubproperty.gif)|
[Tags](P_Grasshopper_Rhinoceros_ModelContent_Attributes_Tags.htm)|  (Inherited
from
[ModelContentAttributes](T_Grasshopper_Rhinoceros_ModelContent_Attributes.htm).)  
![Public property](../icons/pubproperty.gif)|
[TextSettings](P_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_Attributes_TextSettings.htm)|  
![Public property](../icons/pubproperty.gif)|
[ToleranceSettings](P_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_Attributes_ToleranceSettings.htm)|  
![Public property](../icons/pubproperty.gif)|
[UnitsSettings](P_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_Attributes_UnitsSettings.htm)|  
![Public property](../icons/pubproperty.gif)|
[UserText](P_Grasshopper_Rhinoceros_ModelComponentContent_Attributes_UserText.htm)|
(Inherited from
[ModelComponentContentAttributes](T_Grasshopper_Rhinoceros_ModelComponentContent_Attributes.htm).)  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[Clone](M_Grasshopper_Rhinoceros_ModelData_Attributes_Clone.htm)|  (Inherited
from
[ModelDataAttributes](T_Grasshopper_Rhinoceros_ModelData_Attributes.htm).)  
![Public method](../icons/pubmethod.gif)|
[Equals(Object)](M_Grasshopper_Rhinoceros_ModelContent_Attributes_Equals.htm)|
(Inherited from
[ModelContentAttributes](T_Grasshopper_Rhinoceros_ModelContent_Attributes.htm).)  
![Public method](../icons/pubmethod.gif)|
[GetHashCode](M_Grasshopper_Rhinoceros_ModelContent_Attributes_GetHashCode.htm)|
(Inherited from
[ModelContentAttributes](T_Grasshopper_Rhinoceros_ModelContent_Attributes.htm).)  
![Public method](../icons/pubmethod.gif)|
[ToDetails](M_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_Attributes_ToDetails.htm)|
(Overrides
[ModelComponentContentAttributesToDetails](M_Grasshopper_Rhinoceros_ModelComponentContent_Attributes_ToDetails.htm).)  
![Public method](../icons/pubmethod.gif)|
[ToModelData](M_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_Attributes_ToModelData.htm)|
(Overrides
[ModelDataAttributesToModelData](M_Grasshopper_Rhinoceros_ModelData_Attributes_ToModelData.htm).)  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Rhinoceros_ModelContent_Attributes_ToString.htm)|
(Inherited from
[ModelContentAttributes](T_Grasshopper_Rhinoceros_ModelContent_Attributes.htm).)  
Top

![](../icons/SectionExpanded.png)Operators

| Name| Description  
---|---|---  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [(String to
ModelAnnotationStyleAttributes)](M_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_Attributes_op_Implicit.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros.Annotations
Namespace](N_Grasshopper_Rhinoceros_Annotations.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

