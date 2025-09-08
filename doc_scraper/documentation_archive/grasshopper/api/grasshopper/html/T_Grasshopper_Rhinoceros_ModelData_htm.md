---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Rhinoceros_ModelData.htm
scraped_at: 2025-09-08T16:22:37.884755
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Rhinoceros](../html/N_Grasshopper_Rhinoceros.htm
"Grasshopper.Rhinoceros")

[ModelData Class](../html/T_Grasshopper_Rhinoceros_ModelData.htm "ModelData
Class")

[ModelData
Properties](../html/Properties_T_Grasshopper_Rhinoceros_ModelData.htm
"ModelData Properties")

[ModelData Methods](../html/Methods_T_Grasshopper_Rhinoceros_ModelData.htm
"ModelData Methods")

[ModelData Fields](../html/Fields_T_Grasshopper_Rhinoceros_ModelData.htm
"ModelData Fields")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# ModelData Class  
  
---  
  
Represents a Rhino model chunk of data.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.RhinocerosModelData  
More...

**Namespace:** [Grasshopper.Rhinoceros](N_Grasshopper_Rhinoceros.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public abstract class ModelData : IGH_ModelData, 
    	ICloneable, IComparable, IEquatable<ModelData>, IStructuralEquatable
    
    
    Public MustInherit Class ModelData
    	Implements IGH_ModelData, ICloneable, IComparable, IEquatable(Of ModelData), 
    	IStructuralEquatable

The ModelData type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Protected property](../icons/protproperty.gif)|
[Attribs](P_Grasshopper_Rhinoceros_ModelData_Attribs.htm)|  
![Protected property](../icons/protproperty.gif)|
[DefaultAttributes](P_Grasshopper_Rhinoceros_ModelData_DefaultAttributes.htm)|  
![Protected property](../icons/protproperty.gif)|
[IsValidWhyNot](P_Grasshopper_Rhinoceros_ModelData_IsValidWhyNot.htm)|  
![Protected property](../icons/protproperty.gif)|
[TypeDescription](P_Grasshopper_Rhinoceros_ModelData_TypeDescription.htm)|  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Protected method](../icons/protmethod.gif)![Static
member](../icons/static.gif)| [CastA,
T](M_Grasshopper_Rhinoceros_ModelData_Cast__2.htm)|  
![Public method](../icons/pubmethod.gif)|
[CastToT](M_Grasshopper_Rhinoceros_ModelData_CastTo__1.htm)|  
![Public method](../icons/pubmethod.gif)|
[Equals(ModelData)](M_Grasshopper_Rhinoceros_ModelData_Equals.htm)|  
![Public method](../icons/pubmethod.gif)|
[Equals(Object)](M_Grasshopper_Rhinoceros_ModelData_Equals_1.htm)|  (Overrides
[ObjectEquals(Object)](https://docs.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)).)  
![Public method](../icons/pubmethod.gif)|
[GetHashCode](M_Grasshopper_Rhinoceros_ModelData_GetHashCode.htm)|  (Overrides
[ObjectGetHashCode](https://docs.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode).)  
![Protected method](../icons/protmethod.gif)|
[Read](M_Grasshopper_Rhinoceros_ModelData_Read.htm)|  
![Public method](../icons/pubmethod.gif)|
[ToAttributes](M_Grasshopper_Rhinoceros_ModelData_ToAttributes.htm)|  
![Public method](../icons/pubmethod.gif)|
[ToDetails](M_Grasshopper_Rhinoceros_ModelData_ToDetails.htm)|  
![Public method](../icons/pubmethod.gif)|
[TooltipString](M_Grasshopper_Rhinoceros_ModelData_TooltipString.htm)|  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Rhinoceros_ModelData_ToString.htm)|  (Overrides
[ObjectToString](https://docs.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring).)  
![Protected method](../icons/protmethod.gif)|
[Write](M_Grasshopper_Rhinoceros_ModelData_Write.htm)|  
Top

![](../icons/SectionExpanded.png)Fields

| Name| Description  
---|---|---  
![Protected field](../icons/protfield.gif)|
[Serial](F_Grasshopper_Rhinoceros_ModelData_Serial.htm)|  
Top

![](../icons/SectionExpanded.png)Remarks

This type is the base type of a family of immutable types.

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros Namespace](N_Grasshopper_Rhinoceros.htm)

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.RhinocerosModelData  
[Grasshopper.Rhinoceros.AnnotationsAnnotationArrow](T_Grasshopper_Rhinoceros_Annotations_AnnotationArrow.htm)  
[Grasshopper.Rhinoceros.AnnotationsAnnotationArrowSettings](T_Grasshopper_Rhinoceros_Annotations_AnnotationArrowSettings.htm)  
[Grasshopper.Rhinoceros.AnnotationsAnnotationDimensionSettings](T_Grasshopper_Rhinoceros_Annotations_AnnotationDimensionSettings.htm)  
[Grasshopper.Rhinoceros.AnnotationsAnnotationLeaderSettings](T_Grasshopper_Rhinoceros_Annotations_AnnotationLeaderSettings.htm)  
[Grasshopper.Rhinoceros.AnnotationsAnnotationTextSettings](T_Grasshopper_Rhinoceros_Annotations_AnnotationTextSettings.htm)  
[Grasshopper.Rhinoceros.AnnotationsAnnotationToleranceSettings](T_Grasshopper_Rhinoceros_Annotations_AnnotationToleranceSettings.htm)  
[Grasshopper.Rhinoceros.AnnotationsAnnotationUnitsSettings](T_Grasshopper_Rhinoceros_Annotations_AnnotationUnitsSettings.htm)  
[Grasshopper.RhinocerosModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm)  

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

