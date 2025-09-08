---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Attributes_GH_LinkedParamAttributes.htm
scraped_at: 2025-09-08T16:18:54.955544
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Attributes](../html/N_Grasshopper_Kernel_Attributes.htm
"Grasshopper.Kernel.Attributes")

[GH_LinkedParamAttributes
Class](../html/T_Grasshopper_Kernel_Attributes_GH_LinkedParamAttributes.htm
"GH_LinkedParamAttributes Class")

[GH_LinkedParamAttributes Constructor
](../html/M_Grasshopper_Kernel_Attributes_GH_LinkedParamAttributes__ctor.htm
"GH_LinkedParamAttributes Constructor ")

[GH_LinkedParamAttributes
Properties](../html/Properties_T_Grasshopper_Kernel_Attributes_GH_LinkedParamAttributes.htm
"GH_LinkedParamAttributes Properties")

[GH_LinkedParamAttributes
Methods](../html/Methods_T_Grasshopper_Kernel_Attributes_GH_LinkedParamAttributes.htm
"GH_LinkedParamAttributes Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_LinkedParamAttributes Class  
  
---  
  
These Attributes are assigned to parameters that are part of a GH_Component.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.KernelGH_Attributes](T_Grasshopper_Kernel_GH_Attributes_1.htm)[IGH_Param](T_Grasshopper_Kernel_IGH_Param.htm)  
Grasshopper.Kernel.AttributesGH_LinkedParamAttributes  

**Namespace:**
[Grasshopper.Kernel.Attributes](N_Grasshopper_Kernel_Attributes.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_LinkedParamAttributes : GH_Attributes<IGH_Param>
    
    
    Public Class GH_LinkedParamAttributes
    	Inherits GH_Attributes(Of IGH_Param)

The GH_LinkedParamAttributes type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_LinkedParamAttributes](M_Grasshopper_Kernel_Attributes_GH_LinkedParamAttributes__ctor.htm)|
Initializes a new instance of the GH_LinkedParamAttributes class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[AllowMessageBalloon](P_Grasshopper_Kernel_GH_Attributes_1_AllowMessageBalloon.htm)|
Gets a value indicating whether these attributes allow warning and error
balloons to be drawn on top of them.  (Inherited from
[GH_AttributesT](T_Grasshopper_Kernel_GH_Attributes_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[Bounds](P_Grasshopper_Kernel_GH_Attributes_1_Bounds.htm)|  Gets the rectangle
that contains the active content of the attributes. Typically the Contents
determine the active area for menus, tooltips etc. Attributes are not supposed
to draw objects beyond the Bounds.  (Inherited from
[GH_AttributesT](T_Grasshopper_Kernel_GH_Attributes_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[DocObject](P_Grasshopper_Kernel_GH_Attributes_1_DocObject.htm)|  Gets the
owner object of these attributes.  (Inherited from
[GH_AttributesT](T_Grasshopper_Kernel_GH_Attributes_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[GetTopLevel](P_Grasshopper_Kernel_GH_Attributes_1_GetTopLevel.htm)|  Gets the
top-level attributes of the attribute stack these attributes belong to.
(Inherited from [GH_AttributesT](T_Grasshopper_Kernel_GH_Attributes_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[HasInputGrip](P_Grasshopper_Kernel_Attributes_GH_LinkedParamAttributes_HasInputGrip.htm)|
(Overrides
[GH_AttributesTHasInputGrip](P_Grasshopper_Kernel_GH_Attributes_1_HasInputGrip.htm).)  
![Public property](../icons/pubproperty.gif)|
[HasOutputGrip](P_Grasshopper_Kernel_Attributes_GH_LinkedParamAttributes_HasOutputGrip.htm)|
(Overrides
[GH_AttributesTHasOutputGrip](P_Grasshopper_Kernel_GH_Attributes_1_HasOutputGrip.htm).)  
![Public property](../icons/pubproperty.gif)|
[InputGrip](P_Grasshopper_Kernel_GH_Attributes_1_InputGrip.htm)|  Gets the
input grip location for these attributes. If HasInputGrip equals False, this
point is meaningless.  (Inherited from
[GH_AttributesT](T_Grasshopper_Kernel_GH_Attributes_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[InstanceGuid](P_Grasshopper_Kernel_GH_Attributes_1_InstanceGuid.htm)|  Gets
the instance ID of the document object that owns these attributes.  (Inherited
from [GH_AttributesT](T_Grasshopper_Kernel_GH_Attributes_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsTopLevel](P_Grasshopper_Kernel_GH_Attributes_1_IsTopLevel.htm)|  Gets
whether these attributes are top_level (i.e. no Parent attributes)  (Inherited
from [GH_AttributesT](T_Grasshopper_Kernel_GH_Attributes_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[OutputGrip](P_Grasshopper_Kernel_GH_Attributes_1_OutputGrip.htm)|  Gets the
output grip location for these attributes. If HasOutputGrip equals False, this
point is meaningless.  (Inherited from
[GH_AttributesT](T_Grasshopper_Kernel_GH_Attributes_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[Owner](P_Grasshopper_Kernel_GH_Attributes_1_Owner.htm)|  Gets the type-safe
owner object of these attributes. This property is identical to the DocObject
property.  (Inherited from
[GH_AttributesT](T_Grasshopper_Kernel_GH_Attributes_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[Parent](P_Grasshopper_Kernel_GH_Attributes_1_Parent.htm)|  Gets or sets the
parent attributes. Top level attributes do not have parents.  (Inherited from
[GH_AttributesT](T_Grasshopper_Kernel_GH_Attributes_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[PathName](P_Grasshopper_Kernel_GH_Attributes_1_PathName.htm)|  Get a
description of the location of these attributes within the local attribute
stack.  (Inherited from
[GH_AttributesT](T_Grasshopper_Kernel_GH_Attributes_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[Pivot](P_Grasshopper_Kernel_GH_Attributes_1_Pivot.htm)|  Gets or sets the
pivot for these attributes. The pivot controls the general placement of the
attributes. If you want to move the attributes, change the pivot location.
(Inherited from [GH_AttributesT](T_Grasshopper_Kernel_GH_Attributes_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[Selected](P_Grasshopper_Kernel_GH_Attributes_1_Selected.htm)|  Gets or sets
the selected state of the top-level attributes.  (Inherited from
[GH_AttributesT](T_Grasshopper_Kernel_GH_Attributes_1.htm).)  
![Public property](../icons/pubproperty.gif)|
[TooltipEnabled](P_Grasshopper_Kernel_GH_Attributes_1_TooltipEnabled.htm)|
Gets the tooltip enabled value. If False, no further tooltip functions will be
called.  (Inherited from
[GH_AttributesT](T_Grasshopper_Kernel_GH_Attributes_1.htm).)  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[AppendToAttributeTree](M_Grasshopper_Kernel_GH_Attributes_1_AppendToAttributeTree.htm)|
Recursively append these attributes and all child attributes to the attribute
list.  (Inherited from
[GH_AttributesT](T_Grasshopper_Kernel_GH_Attributes_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[ExpireLayout](M_Grasshopper_Kernel_GH_Attributes_1_ExpireLayout.htm)|
Expires the entire layout of the attributes. When overridden, implementer
_must_ place a call to the base class ExpireLayout().  (Inherited from
[GH_AttributesT](T_Grasshopper_Kernel_GH_Attributes_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[InvalidateCanvas](M_Grasshopper_Kernel_GH_Attributes_1_InvalidateCanvas.htm)|
If the mouse location should cause a canvas invalidation then return true. You
only need to override this function if you draw objects that are dependant on
cursor positions outside the bounds of the attributes.  (Inherited from
[GH_AttributesT](T_Grasshopper_Kernel_GH_Attributes_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[IsMenuRegion](M_Grasshopper_Kernel_GH_Attributes_1_IsMenuRegion.htm)|
Determines whether a point is available for context menu popups. By default,
IsMenuRegion calls IsPickRegion(PointF).  (Inherited from
[GH_AttributesT](T_Grasshopper_Kernel_GH_Attributes_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[IsPickRegion(PointF)](M_Grasshopper_Kernel_GH_Attributes_1_IsPickRegion.htm)|
Determines whether a point is within the pickable region for this object. By
default, any point inside the Bounds is treated as pickable.  (Inherited from
[GH_AttributesT](T_Grasshopper_Kernel_GH_Attributes_1.htm).)  
![Public method](../icons/pubmethod.gif)| [IsPickRegion(RectangleF,
GH_PickBox)](M_Grasshopper_Kernel_GH_Attributes_1_IsPickRegion_1.htm)|
Determines whether a rectangle is a valid pick region for this object. By
default, the picking rectangle is intersected with the Bounds rectangle.
(Inherited from [GH_AttributesT](T_Grasshopper_Kernel_GH_Attributes_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[IsTooltipRegion](M_Grasshopper_Kernel_GH_Attributes_1_IsTooltipRegion.htm)|
Determines whether a point is available for tooltip popups. By default,
IsMenuRegion calls IsTooltipRegion(PointF).  (Inherited from
[GH_AttributesT](T_Grasshopper_Kernel_GH_Attributes_1.htm).)  
![Protected method](../icons/protmethod.gif)|
[Layout](M_Grasshopper_Kernel_Attributes_GH_LinkedParamAttributes_Layout.htm)|
(Overrides
[GH_AttributesTLayout](M_Grasshopper_Kernel_GH_Attributes_1_Layout.htm).)  
![Public method](../icons/pubmethod.gif)|
[NewInstanceGuid](M_Grasshopper_Kernel_GH_Attributes_1_NewInstanceGuid.htm)|
Generate a new instance GUID for the owner object.  (Inherited from
[GH_AttributesT](T_Grasshopper_Kernel_GH_Attributes_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[NewInstanceGuid(Guid)](M_Grasshopper_Kernel_GH_Attributes_1_NewInstanceGuid_1.htm)|
Generate a new instance GUID for the owner object. Do not use this overload
unless you're > 1.95m and called David.  (Inherited from
[GH_AttributesT](T_Grasshopper_Kernel_GH_Attributes_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[PerformLayout](M_Grasshopper_Kernel_GH_Attributes_1_PerformLayout.htm)|
Recompute the layout for these attributes. This function is automatically
called during Drawing operations, so you typically don't have to.  (Inherited
from [GH_AttributesT](T_Grasshopper_Kernel_GH_Attributes_1.htm).)  
![Protected method](../icons/protmethod.gif)|
[PrepareForRender](M_Grasshopper_Kernel_GH_Attributes_1_PrepareForRender.htm)|
This method will always be called exactly once prior to Render(). This would
be a good place to make sure all the necessary GUI data is up and running.
(Inherited from [GH_AttributesT](T_Grasshopper_Kernel_GH_Attributes_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[Read](M_Grasshopper_Kernel_GH_Attributes_1_Read.htm)|  (Inherited from
[GH_AttributesT](T_Grasshopper_Kernel_GH_Attributes_1.htm).)  
![Protected method](../icons/protmethod.gif)|
[Render](M_Grasshopper_Kernel_Attributes_GH_LinkedParamAttributes_Render.htm)|
(Overrides [GH_AttributesTRender(GH_Canvas, Graphics,
GH_CanvasChannel)](M_Grasshopper_Kernel_GH_Attributes_1_Render.htm).)  
![Protected method](../icons/protmethod.gif)| [RenderIncomingWires(GH_Painter,
IEnumerableIGH_Param,
GH_ParamWireDisplay)](M_Grasshopper_Kernel_GH_Attributes_1_RenderIncomingWires.htm)|
Utility function for derived classes. This method draws all the wires going
into the left side of the attributes.  (Inherited from
[GH_AttributesT](T_Grasshopper_Kernel_GH_Attributes_1.htm).)  
![Protected method](../icons/protmethod.gif)| [RenderIncomingWires(GH_Painter,
IEnumerableIGH_Param,
IEnumerablePen)](M_Grasshopper_Kernel_GH_Attributes_1_RenderIncomingWires_1.htm)|
Utility function for derived classes. This method draws all the wires going
into the left side of the attributes.  (Inherited from
[GH_AttributesT](T_Grasshopper_Kernel_GH_Attributes_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[RenderToCanvas](M_Grasshopper_Kernel_GH_Attributes_1_RenderToCanvas.htm)|
Render these attributes into a Canvas control. This function places calls to
PrepareForRender() and Render(), you should override those.  (Inherited from
[GH_AttributesT](T_Grasshopper_Kernel_GH_Attributes_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[RespondToKeyDown](M_Grasshopper_Kernel_GH_Attributes_1_RespondToKeyDown.htm)|
(Inherited from [GH_AttributesT](T_Grasshopper_Kernel_GH_Attributes_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[RespondToKeyUp](M_Grasshopper_Kernel_GH_Attributes_1_RespondToKeyUp.htm)|
(Inherited from [GH_AttributesT](T_Grasshopper_Kernel_GH_Attributes_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[RespondToMouseDoubleClick](M_Grasshopper_Kernel_GH_Attributes_1_RespondToMouseDoubleClick.htm)|
(Inherited from [GH_AttributesT](T_Grasshopper_Kernel_GH_Attributes_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[RespondToMouseDown](M_Grasshopper_Kernel_GH_Attributes_1_RespondToMouseDown.htm)|
(Inherited from [GH_AttributesT](T_Grasshopper_Kernel_GH_Attributes_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[RespondToMouseMove](M_Grasshopper_Kernel_GH_Attributes_1_RespondToMouseMove.htm)|
(Inherited from [GH_AttributesT](T_Grasshopper_Kernel_GH_Attributes_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[RespondToMouseUp](M_Grasshopper_Kernel_GH_Attributes_1_RespondToMouseUp.htm)|
(Inherited from [GH_AttributesT](T_Grasshopper_Kernel_GH_Attributes_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[SetupTooltip](M_Grasshopper_Kernel_Attributes_GH_LinkedParamAttributes_SetupTooltip.htm)|
(Overrides [GH_AttributesTSetupTooltip(PointF,
GH_TooltipDisplayEventArgs)](M_Grasshopper_Kernel_GH_Attributes_1_SetupTooltip.htm).)  
![Public method](../icons/pubmethod.gif)|
[Write](M_Grasshopper_Kernel_GH_Attributes_1_Write.htm)|  (Inherited from
[GH_AttributesT](T_Grasshopper_Kernel_GH_Attributes_1.htm).)  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Attributes Namespace](N_Grasshopper_Kernel_Attributes.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

