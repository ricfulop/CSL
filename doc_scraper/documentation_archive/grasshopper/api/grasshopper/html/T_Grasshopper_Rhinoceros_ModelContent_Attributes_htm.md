---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Rhinoceros_ModelContent_Attributes.htm
scraped_at: 2025-09-08T16:22:34.875051
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Rhinoceros](../html/N_Grasshopper_Rhinoceros.htm
"Grasshopper.Rhinoceros")

[ModelContent.Attributes
Class](../html/T_Grasshopper_Rhinoceros_ModelContent_Attributes.htm
"ModelContent.Attributes Class")

[ModelContent.Attributes Constructor
](../html/M_Grasshopper_Rhinoceros_ModelContent_Attributes__ctor.htm
"ModelContent.Attributes Constructor ")

[Attributes
Properties](../html/Properties_T_Grasshopper_Rhinoceros_ModelContent_Attributes.htm
"Attributes Properties")

[Attributes
Methods](../html/Methods_T_Grasshopper_Rhinoceros_ModelContent_Attributes.htm
"Attributes Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# ModelContentAttributes Class  
  
---  
  
![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.RhinocerosModelDataAttributes](T_Grasshopper_Rhinoceros_ModelData_Attributes.htm)  
Grasshopper.RhinocerosModelContentAttributes  
More...

**Namespace:** [Grasshopper.Rhinoceros](N_Grasshopper_Rhinoceros.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public abstract class Attributes : ModelDataAttributes, 
    	IStructuralEquatable, IEquatable<ModelContentAttributes>
    
    
    Public MustInherit Class Attributes
    	Inherits ModelDataAttributes
    	Implements IStructuralEquatable, IEquatable(Of ModelContentAttributes)

The ModelContentAttributes type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Protected method](../icons/protmethod.gif)|
[ModelContentAttributes](M_Grasshopper_Rhinoceros_ModelContent_Attributes__ctor.htm)|
Initializes a new instance of the ModelContentAttributes class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Name](P_Grasshopper_Rhinoceros_ModelContent_Attributes_Name.htm)|  The last
component of the element Path.  
![Public property](../icons/pubproperty.gif)|
[Notes](P_Grasshopper_Rhinoceros_ModelContent_Attributes_Notes.htm)|  
![Public property](../icons/pubproperty.gif)|
[Parent](P_Grasshopper_Rhinoceros_ModelContent_Attributes_Parent.htm)|  Path
of the parent element in 'Root::Parent' format if nested.  
![Public property](../icons/pubproperty.gif)|
[Path](P_Grasshopper_Rhinoceros_ModelContent_Attributes_Path.htm)|  Full
content path in 'Root::Parent::Name' format if is nested.  
![Public property](../icons/pubproperty.gif)|
[Tags](P_Grasshopper_Rhinoceros_ModelContent_Attributes_Tags.htm)|  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Protected method](../icons/protmethod.gif)|
[AsFrozen](M_Grasshopper_Rhinoceros_ModelContent_Attributes_AsFrozen.htm)|  
![Public method](../icons/pubmethod.gif)|
[Clone](M_Grasshopper_Rhinoceros_ModelData_Attributes_Clone.htm)|  (Inherited
from
[ModelDataAttributes](T_Grasshopper_Rhinoceros_ModelData_Attributes.htm).)  
![Protected method](../icons/protmethod.gif)![Static
member](../icons/static.gif)|
[CloneOnWriteA](M_Grasshopper_Rhinoceros_ModelContent_Attributes_CloneOnWrite__1.htm)|  
![Public method](../icons/pubmethod.gif)|
[Equals(Object)](M_Grasshopper_Rhinoceros_ModelContent_Attributes_Equals.htm)|
(Overrides
[ObjectEquals(Object)](https://docs.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)).)  
![Protected method](../icons/protmethod.gif)| [Equals(Object,
IEqualityComparer)](M_Grasshopper_Rhinoceros_ModelContent_Attributes_Equals_1.htm)|  
![Public method](../icons/pubmethod.gif)|
[GetHashCode](M_Grasshopper_Rhinoceros_ModelContent_Attributes_GetHashCode.htm)|
(Overrides
[ObjectGetHashCode](https://docs.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode).)  
![Protected method](../icons/protmethod.gif)|
[GetHashCode(IEqualityComparer)](M_Grasshopper_Rhinoceros_ModelContent_Attributes_GetHashCode_1.htm)|  
![Protected method](../icons/protmethod.gif)|
[IsValidContentName](M_Grasshopper_Rhinoceros_ModelContent_Attributes_IsValidContentName.htm)|  
![Protected method](../icons/protmethod.gif)|
[Read](M_Grasshopper_Rhinoceros_ModelContent_Attributes_Read.htm)|  (Overrides
[ModelDataAttributesRead(GH_IReader)](M_Grasshopper_Rhinoceros_ModelData_Attributes_Read.htm).)  
![Protected method](../icons/protmethod.gif)|
[ReadData](M_Grasshopper_Rhinoceros_ModelContent_Attributes_ReadData.htm)|  
![Protected method](../icons/protmethod.gif)|
[SubClone](M_Grasshopper_Rhinoceros_ModelData_Attributes_SubClone.htm)|
(Inherited from
[ModelDataAttributes](T_Grasshopper_Rhinoceros_ModelData_Attributes.htm).)  
![Public method](../icons/pubmethod.gif)|
[ToDetails](M_Grasshopper_Rhinoceros_ModelData_Attributes_ToDetails.htm)|
(Inherited from
[ModelDataAttributes](T_Grasshopper_Rhinoceros_ModelData_Attributes.htm).)  
![Public method](../icons/pubmethod.gif)|
[ToModelData](M_Grasshopper_Rhinoceros_ModelData_Attributes_ToModelData.htm)|
(Inherited from
[ModelDataAttributes](T_Grasshopper_Rhinoceros_ModelData_Attributes.htm).)  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Rhinoceros_ModelContent_Attributes_ToString.htm)|
(Overrides
[ModelDataAttributesToString](M_Grasshopper_Rhinoceros_ModelData_Attributes_ToString.htm).)  
![Protected method](../icons/protmethod.gif)|
[Write](M_Grasshopper_Rhinoceros_ModelContent_Attributes_Write.htm)|
(Overrides
[ModelDataAttributesWrite(GH_IWriter)](M_Grasshopper_Rhinoceros_ModelData_Attributes_Write.htm).)  
![Protected method](../icons/protmethod.gif)|
[WriteData](M_Grasshopper_Rhinoceros_ModelContent_Attributes_WriteData.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros Namespace](N_Grasshopper_Rhinoceros.htm)

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.RhinocerosModelDataAttributes](T_Grasshopper_Rhinoceros_ModelData_Attributes.htm)  
Grasshopper.RhinocerosModelContentAttributes  
[Grasshopper.Rhinoceros.DisplayModelDisplayModeAttributes](T_Grasshopper_Rhinoceros_Display_ModelDisplayMode_Attributes.htm)  
[Grasshopper.Rhinoceros.DisplayModelNamedViewAttributes](T_Grasshopper_Rhinoceros_Display_ModelNamedView_Attributes.htm)  
[Grasshopper.Rhinoceros.DisplayModelViewportAttributes](T_Grasshopper_Rhinoceros_Display_ModelViewport_Attributes.htm)  
[Grasshopper.Rhinoceros.ModelModelEarthAnchorPointAttributes](T_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint_Attributes.htm)  
[Grasshopper.RhinocerosModelComponentContentAttributes](T_Grasshopper_Rhinoceros_ModelComponentContent_Attributes.htm)  
[Grasshopper.Rhinoceros.RenderModelRenderContentAttributes](T_Grasshopper_Rhinoceros_Render_ModelRenderContent_Attributes.htm)  
[Grasshopper.Rhinoceros.RenderModelRenderSkylightAttributes](T_Grasshopper_Rhinoceros_Render_ModelRenderSkylight_Attributes.htm)  
[Grasshopper.Rhinoceros.RenderModelRenderSunAttributes](T_Grasshopper_Rhinoceros_Render_ModelRenderSun_Attributes.htm)  

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

