---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Rhinoceros_ModelComponentContent_Attributes.htm
scraped_at: 2025-09-08T16:22:32.871514
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Rhinoceros](../html/N_Grasshopper_Rhinoceros.htm
"Grasshopper.Rhinoceros")

[ModelComponentContent.Attributes
Class](../html/T_Grasshopper_Rhinoceros_ModelComponentContent_Attributes.htm
"ModelComponentContent.Attributes Class")

[ModelComponentContent.Attributes Constructor
](../html/M_Grasshopper_Rhinoceros_ModelComponentContent_Attributes__ctor.htm
"ModelComponentContent.Attributes Constructor ")

[Attributes
Properties](../html/Properties_T_Grasshopper_Rhinoceros_ModelComponentContent_Attributes.htm
"Attributes Properties")

[Attributes
Methods](../html/Methods_T_Grasshopper_Rhinoceros_ModelComponentContent_Attributes.htm
"Attributes Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# ModelComponentContentAttributes Class  
  
---  
  
![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.RhinocerosModelDataAttributes](T_Grasshopper_Rhinoceros_ModelData_Attributes.htm)  
[Grasshopper.RhinocerosModelContentAttributes](T_Grasshopper_Rhinoceros_ModelContent_Attributes.htm)  
Grasshopper.RhinocerosModelComponentContentAttributes  
More...

**Namespace:** [Grasshopper.Rhinoceros](N_Grasshopper_Rhinoceros.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public abstract class Attributes : ModelContentAttributes, 
    	IEquatable<ModelComponentContentAttributes>
    
    
    Public MustInherit Class Attributes
    	Inherits ModelContentAttributes
    	Implements IEquatable(Of ModelComponentContentAttributes)

The ModelComponentContentAttributes type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Protected method](../icons/protmethod.gif)|
[ModelComponentContentAttributes](M_Grasshopper_Rhinoceros_ModelComponentContent_Attributes__ctor.htm)|
Initializes a new instance of the ModelComponentContentAttributes class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
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
[UserText](P_Grasshopper_Rhinoceros_ModelComponentContent_Attributes_UserText.htm)|  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Protected method](../icons/protmethod.gif)|
[AsFrozen](M_Grasshopper_Rhinoceros_ModelContent_Attributes_AsFrozen.htm)|
(Inherited from
[ModelContentAttributes](T_Grasshopper_Rhinoceros_ModelContent_Attributes.htm).)  
![Public method](../icons/pubmethod.gif)|
[Clone](M_Grasshopper_Rhinoceros_ModelData_Attributes_Clone.htm)|  (Inherited
from
[ModelDataAttributes](T_Grasshopper_Rhinoceros_ModelData_Attributes.htm).)  
![Public method](../icons/pubmethod.gif)|
[Equals(Object)](M_Grasshopper_Rhinoceros_ModelContent_Attributes_Equals.htm)|
(Inherited from
[ModelContentAttributes](T_Grasshopper_Rhinoceros_ModelContent_Attributes.htm).)  
![Protected method](../icons/protmethod.gif)| [Equals(Object,
IEqualityComparer)](M_Grasshopper_Rhinoceros_ModelComponentContent_Attributes_Equals.htm)|
(Overrides [ModelContentAttributesEquals(Object,
IEqualityComparer)](M_Grasshopper_Rhinoceros_ModelContent_Attributes_Equals_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[GetHashCode](M_Grasshopper_Rhinoceros_ModelContent_Attributes_GetHashCode.htm)|
(Inherited from
[ModelContentAttributes](T_Grasshopper_Rhinoceros_ModelContent_Attributes.htm).)  
![Protected method](../icons/protmethod.gif)|
[GetHashCode(IEqualityComparer)](M_Grasshopper_Rhinoceros_ModelComponentContent_Attributes_GetHashCode.htm)|
(Overrides
[ModelContentAttributesGetHashCode(IEqualityComparer)](M_Grasshopper_Rhinoceros_ModelContent_Attributes_GetHashCode_1.htm).)  
![Protected method](../icons/protmethod.gif)|
[IsValidContentName](M_Grasshopper_Rhinoceros_ModelContent_Attributes_IsValidContentName.htm)|
(Inherited from
[ModelContentAttributes](T_Grasshopper_Rhinoceros_ModelContent_Attributes.htm).)  
![Protected method](../icons/protmethod.gif)|
[Read](M_Grasshopper_Rhinoceros_ModelContent_Attributes_Read.htm)|  (Inherited
from
[ModelContentAttributes](T_Grasshopper_Rhinoceros_ModelContent_Attributes.htm).)  
![Protected method](../icons/protmethod.gif)|
[ReadData](M_Grasshopper_Rhinoceros_ModelComponentContent_Attributes_ReadData.htm)|
(Overrides
[ModelContentAttributesReadData(GH_IReader)](M_Grasshopper_Rhinoceros_ModelContent_Attributes_ReadData.htm).)  
![Protected method](../icons/protmethod.gif)|
[SubClone](M_Grasshopper_Rhinoceros_ModelData_Attributes_SubClone.htm)|
(Inherited from
[ModelDataAttributes](T_Grasshopper_Rhinoceros_ModelData_Attributes.htm).)  
![Public method](../icons/pubmethod.gif)|
[ToDetails](M_Grasshopper_Rhinoceros_ModelComponentContent_Attributes_ToDetails.htm)|
(Overrides
[ModelDataAttributesToDetails](M_Grasshopper_Rhinoceros_ModelData_Attributes_ToDetails.htm).)  
![Public method](../icons/pubmethod.gif)|
[ToModelData](M_Grasshopper_Rhinoceros_ModelData_Attributes_ToModelData.htm)|
(Inherited from
[ModelDataAttributes](T_Grasshopper_Rhinoceros_ModelData_Attributes.htm).)  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Rhinoceros_ModelContent_Attributes_ToString.htm)|
(Inherited from
[ModelContentAttributes](T_Grasshopper_Rhinoceros_ModelContent_Attributes.htm).)  
![Protected method](../icons/protmethod.gif)|
[Write](M_Grasshopper_Rhinoceros_ModelContent_Attributes_Write.htm)|
(Inherited from
[ModelContentAttributes](T_Grasshopper_Rhinoceros_ModelContent_Attributes.htm).)  
![Protected method](../icons/protmethod.gif)|
[WriteData](M_Grasshopper_Rhinoceros_ModelComponentContent_Attributes_WriteData.htm)|
(Overrides
[ModelContentAttributesWriteData(GH_IWriter)](M_Grasshopper_Rhinoceros_ModelContent_Attributes_WriteData.htm).)  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros Namespace](N_Grasshopper_Rhinoceros.htm)

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.RhinocerosModelDataAttributes](T_Grasshopper_Rhinoceros_ModelData_Attributes.htm)  
[Grasshopper.RhinocerosModelContentAttributes](T_Grasshopper_Rhinoceros_ModelContent_Attributes.htm)  
Grasshopper.RhinocerosModelComponentContentAttributes  
[Grasshopper.Rhinoceros.AnnotationsModelAnnotationStyleAttributes](T_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_Attributes.htm)  
[Grasshopper.Rhinoceros.DraftingModelHatchPatternAttributes](T_Grasshopper_Rhinoceros_Drafting_ModelHatchPattern_Attributes.htm)  
[Grasshopper.Rhinoceros.DraftingModelLinetypeAttributes](T_Grasshopper_Rhinoceros_Drafting_ModelLinetype_Attributes.htm)  
[Grasshopper.Rhinoceros.ModelModelInstanceDefinitionAttributes](T_Grasshopper_Rhinoceros_Model_ModelInstanceDefinition_Attributes.htm)  
[Grasshopper.Rhinoceros.ModelModelLayerAttributes](T_Grasshopper_Rhinoceros_Model_ModelLayer_Attributes.htm)  
[Grasshopper.Rhinoceros.ModelModelObjectAttributes](T_Grasshopper_Rhinoceros_Model_ModelObject_Attributes.htm)  

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

