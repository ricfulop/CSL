---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Rhinoceros_ModelValue.htm
scraped_at: 2025-09-08T16:22:45.922295
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Rhinoceros](../html/N_Grasshopper_Rhinoceros.htm
"Grasshopper.Rhinoceros")

[ModelValue Class](../html/T_Grasshopper_Rhinoceros_ModelValue.htm "ModelValue
Class")

[ModelValue
Properties](../html/Properties_T_Grasshopper_Rhinoceros_ModelValue.htm
"ModelValue Properties")

[ModelValue Methods](../html/Methods_T_Grasshopper_Rhinoceros_ModelValue.htm
"ModelValue Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# ModelValue Class  
  
---  
  
Represents a value in a Rhino model.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.RhinocerosModelValue  
More...

**Namespace:** [Grasshopper.Rhinoceros](N_Grasshopper_Rhinoceros.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public abstract class ModelValue : IGH_ModelData, 
    	ICloneable, IEquatable<ModelValue>
    
    
    Public MustInherit Class ModelValue
    	Implements IGH_ModelData, ICloneable, IEquatable(Of ModelValue)

The ModelValue type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Protected property](../icons/protproperty.gif)|
[IsValidWhyNot](P_Grasshopper_Rhinoceros_ModelValue_IsValidWhyNot.htm)|  
![Protected property](../icons/protproperty.gif)|
[TypeDescription](P_Grasshopper_Rhinoceros_ModelValue_TypeDescription.htm)|  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[CastToT](M_Grasshopper_Rhinoceros_ModelValue_CastTo__1.htm)|  
![Protected method](../icons/protmethod.gif)|
[Clone](M_Grasshopper_Rhinoceros_ModelValue_Clone.htm)|  
![Public method](../icons/pubmethod.gif)|
[Equals(ModelValue)](M_Grasshopper_Rhinoceros_ModelValue_Equals.htm)|  
![Public method](../icons/pubmethod.gif)|
[Equals(Object)](M_Grasshopper_Rhinoceros_ModelValue_Equals_1.htm)|
(Overrides
[ObjectEquals(Object)](https://docs.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)).)  
![Public method](../icons/pubmethod.gif)|
[GetHashCode](M_Grasshopper_Rhinoceros_ModelValue_GetHashCode.htm)|
(Overrides
[ObjectGetHashCode](https://docs.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode).)  
![Protected method](../icons/protmethod.gif)|
[Read](M_Grasshopper_Rhinoceros_ModelValue_Read.htm)|  
![Protected method](../icons/protmethod.gif)![Static
member](../icons/static.gif)|
[ReadValueT](M_Grasshopper_Rhinoceros_ModelValue_ReadValue__1.htm)|  
![Protected method](../icons/protmethod.gif)|
[ScriptVariable](M_Grasshopper_Rhinoceros_ModelValue_ScriptVariable.htm)|  
![Public method](../icons/pubmethod.gif)|
[TooltipString](M_Grasshopper_Rhinoceros_ModelValue_TooltipString.htm)|  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Rhinoceros_ModelValue_ToString.htm)|  (Overrides
[ObjectToString](https://docs.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring).)  
![Protected method](../icons/protmethod.gif)|
[Write](M_Grasshopper_Rhinoceros_ModelValue_Write.htm)|  
![Protected method](../icons/protmethod.gif)![Static
member](../icons/static.gif)|
[WriteValueT](M_Grasshopper_Rhinoceros_ModelValue_WriteValue__1.htm)|  
Top

![](../icons/SectionExpanded.png)Remarks

This type is the base type of a family of immutable types.

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros Namespace](N_Grasshopper_Rhinoceros.htm)

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.RhinocerosModelValue  
[Grasshopper.Rhinoceros.DisplayObjectDisplay](T_Grasshopper_Rhinoceros_Display_ObjectDisplay.htm)  
[Grasshopper.Rhinoceros.DisplayObjectDisplayColor](T_Grasshopper_Rhinoceros_Display_ObjectDisplayColor.htm)  
[Grasshopper.Rhinoceros.DisplayObjectVisibility](T_Grasshopper_Rhinoceros_Display_ObjectVisibility.htm)  
[Grasshopper.Rhinoceros.DraftingModelHatchLine](T_Grasshopper_Rhinoceros_Drafting_ModelHatchLine.htm)  
[Grasshopper.Rhinoceros.DraftingObjectDrafting](T_Grasshopper_Rhinoceros_Drafting_ObjectDrafting.htm)  
[Grasshopper.Rhinoceros.DraftingObjectDraftingColor](T_Grasshopper_Rhinoceros_Drafting_ObjectDraftingColor.htm)  
[Grasshopper.Rhinoceros.DraftingObjectDraftingLinetype](T_Grasshopper_Rhinoceros_Drafting_ObjectDraftingLinetype.htm)  
[Grasshopper.Rhinoceros.DraftingObjectDraftingLineWidth](T_Grasshopper_Rhinoceros_Drafting_ObjectDraftingLineWidth.htm)  
[Grasshopper.RhinocerosModelMeshingParameters](T_Grasshopper_Rhinoceros_ModelMeshingParameters.htm)  
[Grasshopper.RhinocerosModelUnitSystem](T_Grasshopper_Rhinoceros_ModelUnitSystem.htm)  
[Grasshopper.Rhinoceros.RenderObjectRender](T_Grasshopper_Rhinoceros_Render_ObjectRender.htm)  
[Grasshopper.Rhinoceros.RenderObjectRenderMaterial](T_Grasshopper_Rhinoceros_Render_ObjectRenderMaterial.htm)  

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

