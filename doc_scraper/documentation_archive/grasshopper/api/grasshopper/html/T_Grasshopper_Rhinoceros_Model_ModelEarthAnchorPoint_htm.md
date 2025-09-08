---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint.htm
scraped_at: 2025-09-08T16:24:12.304968
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Rhinoceros.Model](../html/N_Grasshopper_Rhinoceros_Model.htm
"Grasshopper.Rhinoceros.Model")

[ModelEarthAnchorPoint
Class](../html/T_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint.htm
"ModelEarthAnchorPoint Class")

[ModelEarthAnchorPoint Constructor
](../html/Overload_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint__ctor.htm
"ModelEarthAnchorPoint Constructor ")

[ModelEarthAnchorPoint
Properties](../html/Properties_T_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint.htm
"ModelEarthAnchorPoint Properties")

[ModelEarthAnchorPoint
Methods](../html/Methods_T_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint.htm
"ModelEarthAnchorPoint Methods")

[ModelEarthAnchorPoint Type
Conversions](../html/Operators_T_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint.htm
"ModelEarthAnchorPoint Type Conversions")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# ModelEarthAnchorPoint Class  
  
---  
  
Represents a Rhino Earth anchor point. Wraps the functionality of the
EarthAnchorPoint type.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.RhinocerosModelData](T_Grasshopper_Rhinoceros_ModelData.htm)  
[Grasshopper.RhinocerosModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm)  
Grasshopper.Rhinoceros.ModelModelEarthAnchorPoint  

**Namespace:**
[Grasshopper.Rhinoceros.Model](N_Grasshopper_Rhinoceros_Model.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class ModelEarthAnchorPoint : ModelContent, 
    	IGH_BakeAwareData
    
    
    Public NotInheritable Class ModelEarthAnchorPoint
    	Inherits ModelContent
    	Implements IGH_BakeAwareData

The ModelEarthAnchorPoint type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[ModelEarthAnchorPoint](M_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint__ctor.htm)|
Initializes a new instance of the ModelEarthAnchorPoint class  
![Public method](../icons/pubmethod.gif)|
[ModelEarthAnchorPoint(ModelEarthAnchorPointAttributes)](M_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint__ctor_1.htm)|
Initializes a new instance of the ModelEarthAnchorPoint class  
![Public method](../icons/pubmethod.gif)|
[ModelEarthAnchorPoint(EarthAnchorPoint)](M_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint__ctor_2.htm)|
Initializes a new instance of the ModelEarthAnchorPoint class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Elevation](P_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint_Elevation.htm)|
Gets a point elevation on earth, in meters.  
![Public property](../icons/pubproperty.gif)|
[ElevationCoordinateSystem](P_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint_ElevationCoordinateSystem.htm)|
Gets the value indicating the zero level convention relating to a location on
Earth  
![Public property](../icons/pubproperty.gif)|
[Id](P_Grasshopper_Rhinoceros_ModelContent_Id.htm)|  (Inherited from
[ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsValid](P_Grasshopper_Rhinoceros_ModelContent_IsValid.htm)|  (Inherited from
[ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Public property](../icons/pubproperty.gif)|
[Latitude](P_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint_Latitude.htm)|
Gets a point latitude on earth, in degrees. [-90, +90]  
![Public property](../icons/pubproperty.gif)|
[Longitude](P_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint_Longitude.htm)|
Gets a point longitude on earth, in degrees. [-180, +180]  
![Public property](../icons/pubproperty.gif)|
[ModelCompass](P_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint_ModelCompass.htm)|
Gets the corresponding compass plane in model coordinates  
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
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Cast](M_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint_Cast.htm)|  
![Public method](../icons/pubmethod.gif)|
[CastToT(T)](M_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint_CastTo__1.htm)|
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
[ToAttributes](M_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint_ToAttributes.htm)|  
![Public method](../icons/pubmethod.gif)|
[ToDetails](M_Grasshopper_Rhinoceros_ModelData_ToDetails.htm)|  (Inherited
from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).)  
![Public method](../icons/pubmethod.gif)|
[TooltipString](M_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint_TooltipString.htm)|
(Overrides
[ModelContentTooltipString](M_Grasshopper_Rhinoceros_ModelContent_TooltipString.htm).)  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint_ToString.htm)|
(Overrides
[ModelContentToString](M_Grasshopper_Rhinoceros_ModelContent_ToString.htm).)  
Top

![](../icons/SectionExpanded.png)Operators

| Name| Description  
---|---|---  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [(ModelEarthAnchorPointAttributes to
ModelEarthAnchorPoint)](M_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint_op_Implicit.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [(EarthAnchorPoint to
ModelEarthAnchorPoint)](M_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint_op_Implicit_1.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros.Model Namespace](N_Grasshopper_Rhinoceros_Model.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

