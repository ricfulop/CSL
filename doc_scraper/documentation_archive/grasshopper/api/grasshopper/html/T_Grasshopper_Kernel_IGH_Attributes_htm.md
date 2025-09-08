---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_IGH_Attributes.htm
scraped_at: 2025-09-08T16:18:13.769722
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH_Attributes Interface](../html/T_Grasshopper_Kernel_IGH_Attributes.htm
"IGH_Attributes Interface")

[IGH_Attributes
Properties](../html/Properties_T_Grasshopper_Kernel_IGH_Attributes.htm
"IGH_Attributes Properties")

[IGH_Attributes
Methods](../html/Methods_T_Grasshopper_Kernel_IGH_Attributes.htm
"IGH_Attributes Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# IGH_Attributes Interface  
  
---  
  
Base interface for all Attributes. Attributes are the visual portion of
GH_DocumentObjects. They handle display, mouse events, layout, context menus
etc. etc. You should consider inheriting from GH_Attributes or some other
abstract class instead of implementing this interface from scratch.

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public interface IGH_Attributes : GH_ISerializable, 
    	IGH_ResponsiveObject, IGH_TooltipAwareObject
    
    
    Public Interface IGH_Attributes
    	Inherits GH_ISerializable, IGH_ResponsiveObject, IGH_TooltipAwareObject

The IGH_Attributes type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[AllowMessageBalloon](P_Grasshopper_Kernel_IGH_Attributes_AllowMessageBalloon.htm)|
Gets a value indicating whether these attributes allow warning and error boxes
to be drawn on top of them.  
![Public property](../icons/pubproperty.gif)|
[Bounds](P_Grasshopper_Kernel_IGH_Attributes_Bounds.htm)|  Gets the rectangle
that contains the active content of the attributes. Typically the Contents
determine the active area for menus, tooltips etc. Attributes are not supposed
to draw objects beyond the Bounds.  
![Public property](../icons/pubproperty.gif)|
[DocObject](P_Grasshopper_Kernel_IGH_Attributes_DocObject.htm)|  Gets the
owner object of these attributes.  
![Public property](../icons/pubproperty.gif)|
[GetTopLevel](P_Grasshopper_Kernel_IGH_Attributes_GetTopLevel.htm)|  Gets the
top level attributes of these attributes.  
![Public property](../icons/pubproperty.gif)|
[HasInputGrip](P_Grasshopper_Kernel_IGH_Attributes_HasInputGrip.htm)|  Gets a
value indicating whether or not these attributes have an input grip.  
![Public property](../icons/pubproperty.gif)|
[HasOutputGrip](P_Grasshopper_Kernel_IGH_Attributes_HasOutputGrip.htm)|  Gets
a value indicating whether or not these attributes have an output grip.  
![Public property](../icons/pubproperty.gif)|
[InputGrip](P_Grasshopper_Kernel_IGH_Attributes_InputGrip.htm)|  Gets the
input grip location for these attributes. If HasInputGrip equals False, this
point is meaningless.  
![Public property](../icons/pubproperty.gif)|
[InstanceGuid](P_Grasshopper_Kernel_IGH_Attributes_InstanceGuid.htm)|  Gets
the instance ID for these attributes.  
![Public property](../icons/pubproperty.gif)|
[IsTopLevel](P_Grasshopper_Kernel_IGH_Attributes_IsTopLevel.htm)|  Gets
whether these attributes are top_level (i.e. no Parent attributes)  
![Public property](../icons/pubproperty.gif)|
[OutputGrip](P_Grasshopper_Kernel_IGH_Attributes_OutputGrip.htm)|  Gets the
output grip location for these attributes. If HasOutputGrip equals False, this
point is meaningless.  
![Public property](../icons/pubproperty.gif)|
[Parent](P_Grasshopper_Kernel_IGH_Attributes_Parent.htm)|  Gets or sets the
parent attributes. Top level attributes do not have parents.  
![Public property](../icons/pubproperty.gif)|
[PathName](P_Grasshopper_Kernel_IGH_Attributes_PathName.htm)|  Get a
description of the location of these attributes within the local attribute
tree.  
![Public property](../icons/pubproperty.gif)|
[Pivot](P_Grasshopper_Kernel_IGH_Attributes_Pivot.htm)|  Gets the pivot for
these attributes. The pivot controls the general placement of the attributes.
If you want to move the attributes, change the pivot location.  
![Public property](../icons/pubproperty.gif)|
[Selected](P_Grasshopper_Kernel_IGH_Attributes_Selected.htm)|  Gets or sets
the selected state of the top-level attributes.  
![Public property](../icons/pubproperty.gif)|
[TooltipEnabled](P_Grasshopper_GUI_Canvas_IGH_TooltipAwareObject_TooltipEnabled.htm)|
Gets the tooltip enabled value. If False, no further tooltip functions will be
called.  (Inherited from
[IGH_TooltipAwareObject](T_Grasshopper_GUI_Canvas_IGH_TooltipAwareObject.htm).)  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[AppendToAttributeTree](M_Grasshopper_Kernel_IGH_Attributes_AppendToAttributeTree.htm)|
Recursively append these attributes and all child attributes to the attribute
list.  
![Public method](../icons/pubmethod.gif)|
[ExpireLayout](M_Grasshopper_Kernel_IGH_Attributes_ExpireLayout.htm)|  Expires
the entire layout of the attributes. When overridden, implementer _must_ place
a call to the base class ExpireLayout().  
![Public method](../icons/pubmethod.gif)|
[InvalidateCanvas](M_Grasshopper_Kernel_IGH_Attributes_InvalidateCanvas.htm)|
If the mouse location should cause a canvas invalidation then return true. You
only need to override this function if you draw objects that are dependant on
cursor positions outside the bounds of the attributes.  
![Public method](../icons/pubmethod.gif)|
[IsMenuRegion](M_Grasshopper_Kernel_IGH_Attributes_IsMenuRegion.htm)|
Determines whether a point is available for context menu popups. By default,
IsMenuRegion calls IsPickRegion(PointF).  
![Public method](../icons/pubmethod.gif)|
[IsPickRegion(PointF)](M_Grasshopper_Kernel_IGH_Attributes_IsPickRegion.htm)|
Determines whether a point is within the pickable region for this object. By
default, any point inside the Bounds is treated as pickable.  
![Public method](../icons/pubmethod.gif)| [IsPickRegion(RectangleF,
GH_PickBox)](M_Grasshopper_Kernel_IGH_Attributes_IsPickRegion_1.htm)|
Determines whether a rectangle is a valid pick region for this object. By
default, the picking rectangle is intersected with the Bounds rectangle.  
![Public method](../icons/pubmethod.gif)|
[IsTooltipRegion](M_Grasshopper_GUI_Canvas_IGH_TooltipAwareObject_IsTooltipRegion.htm)|
Determine whether the specified pixel should result in a tooltip when the
cursor hovers over it.  (Inherited from
[IGH_TooltipAwareObject](T_Grasshopper_GUI_Canvas_IGH_TooltipAwareObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[NewInstanceGuid](M_Grasshopper_Kernel_IGH_Attributes_NewInstanceGuid.htm)|
Generate a new instance GUID for the owner object.  
![Public method](../icons/pubmethod.gif)|
[NewInstanceGuid(Guid)](M_Grasshopper_Kernel_IGH_Attributes_NewInstanceGuid_1.htm)|
Generate a new instance GUID for the owner object. Do not use this overload
unless you're > 1.95m and called David.  
![Public method](../icons/pubmethod.gif)|
[PerformLayout](M_Grasshopper_Kernel_IGH_Attributes_PerformLayout.htm)|
Recompute the layout for these attributes. This function is automatically
called during Drawing operations, so you typically don't have to.  
![Public method](../icons/pubmethod.gif)|
[Read](M_GH_IO_GH_ISerializable_Read.htm)|  This method is called whenever the
instance is required to deserialize itself.  (Inherited from
[GH_ISerializable](T_GH_IO_GH_ISerializable.htm).)  
![Public method](../icons/pubmethod.gif)|
[RenderToCanvas](M_Grasshopper_Kernel_IGH_Attributes_RenderToCanvas.htm)|
Render these attributes into a Canvas control.  
![Public method](../icons/pubmethod.gif)|
[RespondToKeyDown](M_Grasshopper_GUI_Canvas_IGH_ResponsiveObject_RespondToKeyDown.htm)|
(Inherited from
[IGH_ResponsiveObject](T_Grasshopper_GUI_Canvas_IGH_ResponsiveObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[RespondToKeyUp](M_Grasshopper_GUI_Canvas_IGH_ResponsiveObject_RespondToKeyUp.htm)|
(Inherited from
[IGH_ResponsiveObject](T_Grasshopper_GUI_Canvas_IGH_ResponsiveObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[RespondToMouseDoubleClick](M_Grasshopper_GUI_Canvas_IGH_ResponsiveObject_RespondToMouseDoubleClick.htm)|
This function will be called whenever the left button is double-clicked over
the canvas. If you are active, you will be the only object who gets called.
(Inherited from
[IGH_ResponsiveObject](T_Grasshopper_GUI_Canvas_IGH_ResponsiveObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[RespondToMouseDown](M_Grasshopper_GUI_Canvas_IGH_ResponsiveObject_RespondToMouseDown.htm)|
This function will be called whenever a mouse button is pressed over the
canvas. If you are active, you will be the only object who gets called. If you
are inactive, you might get called if nobody on top of you decides to become
active.  (Inherited from
[IGH_ResponsiveObject](T_Grasshopper_GUI_Canvas_IGH_ResponsiveObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[RespondToMouseMove](M_Grasshopper_GUI_Canvas_IGH_ResponsiveObject_RespondToMouseMove.htm)|
This function will be called when the mouse moves across the canvas. If you
are active, you will be the only object who gets called. If you are inactive,
you might get called if nobody on top of you decides to become active.
(Inherited from
[IGH_ResponsiveObject](T_Grasshopper_GUI_Canvas_IGH_ResponsiveObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[RespondToMouseUp](M_Grasshopper_GUI_Canvas_IGH_ResponsiveObject_RespondToMouseUp.htm)|
This function will be called whenever a mouse button is released over the
canvas. If you are active, you will be the only object who gets called. If you
are inactive, you will not be called at all for MouseUp events.  (Inherited
from
[IGH_ResponsiveObject](T_Grasshopper_GUI_Canvas_IGH_ResponsiveObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[SetupTooltip](M_Grasshopper_GUI_Canvas_IGH_TooltipAwareObject_SetupTooltip.htm)|
This function is called when a tooltip it about to be displayed.  (Inherited
from
[IGH_TooltipAwareObject](T_Grasshopper_GUI_Canvas_IGH_TooltipAwareObject.htm).)  
![Public method](../icons/pubmethod.gif)|
[Write](M_GH_IO_GH_ISerializable_Write.htm)|  This method is called whenever
the instance is required to serialize itself.  (Inherited from
[GH_ISerializable](T_GH_IO_GH_ISerializable.htm).)  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

