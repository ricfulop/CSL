---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Rhinoceros_Display_ModelPageViewport_Attributes.htm
scraped_at: 2025-09-08T16:23:23.099481
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Rhinoceros.Display](../html/N_Grasshopper_Rhinoceros_Display.htm
"Grasshopper.Rhinoceros.Display")

[ModelPageViewport.Attributes
Class](../html/T_Grasshopper_Rhinoceros_Display_ModelPageViewport_Attributes.htm
"ModelPageViewport.Attributes Class")

[ModelPageViewport.Attributes Constructor
](../html/M_Grasshopper_Rhinoceros_Display_ModelPageViewport_Attributes__ctor.htm
"ModelPageViewport.Attributes Constructor ")

[Attributes
Properties](../html/Properties_T_Grasshopper_Rhinoceros_Display_ModelPageViewport_Attributes.htm
"Attributes Properties")

[Attributes
Methods](../html/Methods_T_Grasshopper_Rhinoceros_Display_ModelPageViewport_Attributes.htm
"Attributes Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# ModelPageViewportAttributes Class  
  
---  
  
![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.RhinocerosModelDataAttributes](T_Grasshopper_Rhinoceros_ModelData_Attributes.htm)  
[Grasshopper.RhinocerosModelContentAttributes](T_Grasshopper_Rhinoceros_ModelContent_Attributes.htm)  
[Grasshopper.Rhinoceros.DisplayModelViewportAttributes](T_Grasshopper_Rhinoceros_Display_ModelViewport_Attributes.htm)  
Grasshopper.Rhinoceros.DisplayModelPageViewportAttributes  

**Namespace:**
[Grasshopper.Rhinoceros.Display](N_Grasshopper_Rhinoceros_Display.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class Attributes : ModelViewportAttributes, 
    	IEquatable<ModelPageViewportAttributes>
    
    
    Public NotInheritable Class Attributes
    	Inherits ModelViewportAttributes
    	Implements IEquatable(Of ModelPageViewportAttributes)

The ModelPageViewportAttributes type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[ModelPageViewportAttributes](M_Grasshopper_Rhinoceros_Display_ModelPageViewport_Attributes__ctor.htm)|
Initializes a new instance of the ModelPageViewportAttributes class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[DisplayMode](P_Grasshopper_Rhinoceros_Display_ModelViewport_Attributes_DisplayMode.htm)|
(Inherited from
[ModelViewportAttributes](T_Grasshopper_Rhinoceros_Display_ModelViewport_Attributes.htm).)  
![Public property](../icons/pubproperty.gif)|
[Name](P_Grasshopper_Rhinoceros_ModelContent_Attributes_Name.htm)|  The last
component of the element Path.  (Inherited from
[ModelContentAttributes](T_Grasshopper_Rhinoceros_ModelContent_Attributes.htm).)  
![Public property](../icons/pubproperty.gif)|
[Notes](P_Grasshopper_Rhinoceros_ModelContent_Attributes_Notes.htm)|
(Inherited from
[ModelContentAttributes](T_Grasshopper_Rhinoceros_ModelContent_Attributes.htm).)  
![Public property](../icons/pubproperty.gif)|
[PageNumber](P_Grasshopper_Rhinoceros_Display_ModelPageViewport_Attributes_PageNumber.htm)|  
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
[UserText](P_Grasshopper_Rhinoceros_Display_ModelViewport_Attributes_UserText.htm)|
(Inherited from
[ModelViewportAttributes](T_Grasshopper_Rhinoceros_Display_ModelViewport_Attributes.htm).)  
![Public property](../icons/pubproperty.gif)|
[View](P_Grasshopper_Rhinoceros_Display_ModelViewport_Attributes_View.htm)|
(Inherited from
[ModelViewportAttributes](T_Grasshopper_Rhinoceros_Display_ModelViewport_Attributes.htm).)  
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
[ToDetails](M_Grasshopper_Rhinoceros_Display_ModelPageViewport_Attributes_ToDetails.htm)|
(Overrides
[ModelViewportAttributesToDetails](M_Grasshopper_Rhinoceros_Display_ModelViewport_Attributes_ToDetails.htm).)  
![Public method](../icons/pubmethod.gif)|
[ToModelData](M_Grasshopper_Rhinoceros_Display_ModelPageViewport_Attributes_ToModelData.htm)|
(Overrides
[ModelViewportAttributesToModelData](M_Grasshopper_Rhinoceros_Display_ModelViewport_Attributes_ToModelData.htm).)  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Rhinoceros_ModelContent_Attributes_ToString.htm)|
(Inherited from
[ModelContentAttributes](T_Grasshopper_Rhinoceros_ModelContent_Attributes.htm).)  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros.Display
Namespace](N_Grasshopper_Rhinoceros_Display.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

