---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Rhinoceros_Display_ModelView.htm
scraped_at: 2025-09-08T16:23:26.102020
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Rhinoceros.Display](../html/N_Grasshopper_Rhinoceros_Display.htm
"Grasshopper.Rhinoceros.Display")

[ModelView Class](../html/T_Grasshopper_Rhinoceros_Display_ModelView.htm
"ModelView Class")

[ModelView Constructor
](../html/Overload_Grasshopper_Rhinoceros_Display_ModelView__ctor.htm
"ModelView Constructor ")

[ModelView
Properties](../html/Properties_T_Grasshopper_Rhinoceros_Display_ModelView.htm
"ModelView Properties")

[ModelView
Methods](../html/Methods_T_Grasshopper_Rhinoceros_Display_ModelView.htm
"ModelView Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# ModelView Class  
  
---  
  
Represents a 3D view frustum. Wraps the functionality of the ViewportInfo
type.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.Rhinoceros.DisplayModelView  

**Namespace:**
[Grasshopper.Rhinoceros.Display](N_Grasshopper_Rhinoceros_Display.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class ModelView : IGH_GeometricGoo, 
    	IEquatable<ModelView>, IGH_PreviewData, IGH_BakeAwareData
    
    
    Public NotInheritable Class ModelView
    	Implements IGH_GeometricGoo, IEquatable(Of ModelView), 
    	IGH_PreviewData, IGH_BakeAwareData

The ModelView type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[ModelView](M_Grasshopper_Rhinoceros_Display_ModelView__ctor.htm)| Initializes
a new instance of the ModelView class  
![Public method](../icons/pubmethod.gif)|
[ModelView(Guid)](M_Grasshopper_Rhinoceros_Display_ModelView__ctor_7.htm)|
Create a new referenced view that references a RhinoView or NamedView object
with the specified ref_guid.  
![Public method](../icons/pubmethod.gif)|
[ModelView(ModelView)](M_Grasshopper_Rhinoceros_Display_ModelView__ctor_1.htm)|
Initializes a new instance of the ModelView class  
![Public method](../icons/pubmethod.gif)|
[ModelView(RhinoView)](M_Grasshopper_Rhinoceros_Display_ModelView__ctor_2.htm)|
Initializes a new instance of the ModelView class  
![Public method](../icons/pubmethod.gif)|
[ModelView(RhinoViewport)](M_Grasshopper_Rhinoceros_Display_ModelView__ctor_3.htm)|
Initializes a new instance of the ModelView class  
![Public method](../icons/pubmethod.gif)|
[ModelView(ViewInfo)](M_Grasshopper_Rhinoceros_Display_ModelView__ctor_4.htm)|
Initializes a new instance of the ModelView class  
![Public method](../icons/pubmethod.gif)|
[ModelView(ViewportInfo)](M_Grasshopper_Rhinoceros_Display_ModelView__ctor_5.htm)|
Initializes a new instance of the ModelView class  
![Public method](../icons/pubmethod.gif)| [ModelView(ViewportInfo,
String)](M_Grasshopper_Rhinoceros_Display_ModelView__ctor_6.htm)| Initializes
a new instance of the ModelView class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[IsValid](P_Grasshopper_Rhinoceros_Display_ModelView_IsValid.htm)|  
![Public property](../icons/pubproperty.gif)|
[Title](P_Grasshopper_Rhinoceros_Display_ModelView_Title.htm)|  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Cast](M_Grasshopper_Rhinoceros_Display_ModelView_Cast.htm)|  
![Protected method](../icons/protmethod.gif)|
[CastToQ](M_Grasshopper_Rhinoceros_Display_ModelView_CastTo__1.htm)|  
![Public method](../icons/pubmethod.gif)|
[Equals(ModelView)](M_Grasshopper_Rhinoceros_Display_ModelView_Equals.htm)|  
![Public method](../icons/pubmethod.gif)|
[Equals(Object)](M_Grasshopper_Rhinoceros_Display_ModelView_Equals_1.htm)|
(Overrides
[ObjectEquals(Object)](https://docs.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)).)  
![Public method](../icons/pubmethod.gif)|
[GetBoundingBox](M_Grasshopper_Rhinoceros_Display_ModelView_GetBoundingBox.htm)|  
![Public method](../icons/pubmethod.gif)|
[GetHashCode](M_Grasshopper_Rhinoceros_Display_ModelView_GetHashCode.htm)|
(Overrides
[ObjectGetHashCode](https://docs.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode).)  
![Public method](../icons/pubmethod.gif)|
[Morph](M_Grasshopper_Rhinoceros_Display_ModelView_Morph.htm)|  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Rhinoceros_Display_ModelView_ToString.htm)|
(Overrides
[ObjectToString](https://docs.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring).)  
![Public method](../icons/pubmethod.gif)|
[ToViewportInfo](M_Grasshopper_Rhinoceros_Display_ModelView_ToViewportInfo.htm)|  
![Public method](../icons/pubmethod.gif)|
[Transform](M_Grasshopper_Rhinoceros_Display_ModelView_Transform.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros.Display
Namespace](N_Grasshopper_Rhinoceros_Display.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

