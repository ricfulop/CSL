---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Rhinoceros_Display_ModelDisplayMode.htm
scraped_at: 2025-09-08T16:23:18.079953
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Rhinoceros.Display](../html/N_Grasshopper_Rhinoceros_Display.htm
"Grasshopper.Rhinoceros.Display")

[ModelDisplayMode
Class](../html/T_Grasshopper_Rhinoceros_Display_ModelDisplayMode.htm
"ModelDisplayMode Class")

[ModelDisplayMode Constructor
](../html/Overload_Grasshopper_Rhinoceros_Display_ModelDisplayMode__ctor.htm
"ModelDisplayMode Constructor ")

[ModelDisplayMode
Properties](../html/Properties_T_Grasshopper_Rhinoceros_Display_ModelDisplayMode.htm
"ModelDisplayMode Properties")

[ModelDisplayMode
Methods](../html/Methods_T_Grasshopper_Rhinoceros_Display_ModelDisplayMode.htm
"ModelDisplayMode Methods")

[ModelDisplayMode Type
Conversions](../html/Operators_T_Grasshopper_Rhinoceros_Display_ModelDisplayMode.htm
"ModelDisplayMode Type Conversions")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# ModelDisplayMode Class  
  
---  
  
Represents a Rhino display mode. Wraps the functionality of the
DisplayModeDescription type.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.RhinocerosModelData](T_Grasshopper_Rhinoceros_ModelData.htm)  
[Grasshopper.RhinocerosModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm)  
Grasshopper.Rhinoceros.DisplayModelDisplayMode  

**Namespace:**
[Grasshopper.Rhinoceros.Display](N_Grasshopper_Rhinoceros_Display.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class ModelDisplayMode : ModelContent, 
    	IGH_BakeAwareData
    
    
    Public NotInheritable Class ModelDisplayMode
    	Inherits ModelContent
    	Implements IGH_BakeAwareData

The ModelDisplayMode type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[ModelDisplayMode](M_Grasshopper_Rhinoceros_Display_ModelDisplayMode__ctor.htm)|
Initializes a new instance of the ModelDisplayMode class  
![Public method](../icons/pubmethod.gif)|
[ModelDisplayMode(ModelDisplayModeAttributes)](M_Grasshopper_Rhinoceros_Display_ModelDisplayMode__ctor_1.htm)|
Initializes a new instance of the ModelDisplayMode class  
![Public method](../icons/pubmethod.gif)|
[ModelDisplayMode(DisplayModeDescription)](M_Grasshopper_Rhinoceros_Display_ModelDisplayMode__ctor_2.htm)|
Initializes a new instance of the ModelDisplayMode class  
![Public method](../icons/pubmethod.gif)|
[ModelDisplayMode(Guid)](M_Grasshopper_Rhinoceros_Display_ModelDisplayMode__ctor_3.htm)|
Initializes a new instance of the ModelDisplayMode class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Id](P_Grasshopper_Rhinoceros_ModelContent_Id.htm)|  (Inherited from
[ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsValid](P_Grasshopper_Rhinoceros_ModelContent_IsValid.htm)|  (Inherited from
[ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).)  
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
[Unset](P_Grasshopper_Rhinoceros_Display_ModelDisplayMode_Unset.htm)|  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[Cast](M_Grasshopper_Rhinoceros_Display_ModelDisplayMode_Cast.htm)|  
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
[ToAttributes](M_Grasshopper_Rhinoceros_Display_ModelDisplayMode_ToAttributes.htm)|  
![Public method](../icons/pubmethod.gif)|
[ToDetails](M_Grasshopper_Rhinoceros_ModelData_ToDetails.htm)|  (Inherited
from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).)  
![Public method](../icons/pubmethod.gif)|
[TooltipString](M_Grasshopper_Rhinoceros_Display_ModelDisplayMode_TooltipString.htm)|
(Overrides
[ModelContentTooltipString](M_Grasshopper_Rhinoceros_ModelContent_TooltipString.htm).)  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Rhinoceros_Display_ModelDisplayMode_ToString.htm)|
(Overrides
[ModelContentToString](M_Grasshopper_Rhinoceros_ModelContent_ToString.htm).)  
Top

![](../icons/SectionExpanded.png)Operators

| Name| Description  
---|---|---  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [(ModelDisplayModeAttributes to
ModelDisplayMode)](M_Grasshopper_Rhinoceros_Display_ModelDisplayMode_op_Implicit.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [(DisplayModeDescription to
ModelDisplayMode)](M_Grasshopper_Rhinoceros_Display_ModelDisplayMode_op_Implicit_1.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [(Guid to
ModelDisplayMode)](M_Grasshopper_Rhinoceros_Display_ModelDisplayMode_op_Implicit_2.htm)|  
![Public operator](../icons/puboperator.gif)![Static
member](../icons/static.gif)| [(String to
ModelDisplayMode)](M_Grasshopper_Rhinoceros_Display_ModelDisplayMode_op_Implicit_3.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros.Display
Namespace](N_Grasshopper_Rhinoceros_Display.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

