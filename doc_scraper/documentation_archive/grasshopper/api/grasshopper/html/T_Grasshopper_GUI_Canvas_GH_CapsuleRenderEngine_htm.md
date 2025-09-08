---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine.htm
scraped_at: 2025-09-08T16:14:35.852898
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm
"Grasshopper.GUI.Canvas")

[GH_CapsuleRenderEngine
Class](../html/T_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine.htm
"GH_CapsuleRenderEngine Class")

[GH_CapsuleRenderEngine
Methods](../html/Methods_T_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine.htm
"GH_CapsuleRenderEngine Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_CapsuleRenderEngine Class  
  
---  
  
Provides basic Render methods for capsule display. You typically don't need
this class, just use the Render() overloads on GH_Capsule directly.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.GUI.CanvasGH_CapsuleRenderEngine  

**Namespace:** [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_CapsuleRenderEngine
    
    
    Public Class GH_CapsuleRenderEngine

The GH_CapsuleRenderEngine type exposes the following members.

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateHighlightBar(Rectangle, Int32,
Int32)](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_CreateHighlightBar.htm)|
Static (Shared in VB) method for creating Grasshopper Capsule highlight fills.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateHighlightBar(Rectangle, Int32, Int32,
Int32)](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_CreateHighlightBar_2.htm)|
Static (Shared in VB) method for creating Grasshopper Capsule highlight fills.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateHighlightBar(Rectangle, Int32, Int32, Boolean,
Boolean)](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_CreateHighlightBar_1.htm)|
Static (Shared in VB) method for creating Grasshopper Capsule highlight fills.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateHighlightBar(Rectangle, Int32, Int32, Int32, Boolean,
Boolean)](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_CreateHighlightBar_3.htm)|
Static (Shared in VB) method for creating Grasshopper Capsule highlight fills.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateJaggedRectangle](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_CreateJaggedRectangle.htm)|
Static (Shared in VB) method for creating rectangles with rounded corners.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateRoundedRectangle(Rectangle,
Int32)](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_CreateRoundedRectangle.htm)|
Static (Shared in VB) method for creating rectangles with rounded corners.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateRoundedRectangle(RectangleF,
Single)](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_CreateRoundedRectangle_2.htm)|
Static (Shared in VB) method for creating rectangles with rounded corners.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateRoundedRectangle(Rectangle, Int32, Int32, Int32,
Int32)](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_CreateRoundedRectangle_1.htm)|
Static (Shared in VB) method for creating rectangles with rounded corners.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateRoundedRectangle(RectangleF, Single, Single, Single,
Single)](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_CreateRoundedRectangle_3.htm)|
Static (Shared in VB) method for creating rectangles with rounded corners.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[GetImpliedPalette](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_GetImpliedPalette.htm)|
Static (Shared in VB) method for solving which palette is the default given a
specific object's properties. Default palettes are either GH_Palette.Normal,
GH_Palette.Warning or GH_Palette.Error depending on the objects' runtime
message level.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[GetImpliedStyle(GH_Palette,
IGH_Attributes)](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_GetImpliedStyle.htm)|
Static (Shared in VB) method for solving which palette style is implied by the
properties.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[GetImpliedStyle(GH_Palette, Boolean, Boolean,
Boolean)](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_GetImpliedStyle_1.htm)|
Static (Shared in VB) method for solving which palette style is implied by the
properties.  
![Public method](../icons/pubmethod.gif)|
[RenderAlphaFill](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderAlphaFill.htm)|
Render a standard transparancy background hatch. This is only needed when the
capsule background colour is not fully opaque. This is usually the second
stage in a capsule rendering, right after the Grips are drawn.  
![Public method](../icons/pubmethod.gif)|
[RenderBackground](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderBackground.htm)|
Render a default capsule background fill. This is usually the third stage in a
capsule rendering.  
![Public method](../icons/pubmethod.gif)|
[RenderBackground_Alternative](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderBackground_Alternative.htm)|
Render a custom capsule background fill. This is usually the third stage in a
capsule rendering.  
![Public method](../icons/pubmethod.gif)|
[RenderBoundaryDots](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderBoundaryDots.htm)|
Render a collection of boundary dots along the top edge of the capsule.  
![Public method](../icons/pubmethod.gif)|
[RenderGrips](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderGrips.htm)|
Render all the grips associates with the capsule. Grips are not drawn if the
zoom level is less than 50%. This is usually the first stage in a Capsule
rendering.  
![Public method](../icons/pubmethod.gif)|
[RenderGrips_Alternative](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderGrips_Alternative.htm)|
Render all the grips associates with the capsule as semi-circles. This is
needed if the capsule background is not fully opaque. Grips are not drawn if
the zoom level is less than 50%. This is usually the first stage in a Capsule
rendering.  
![Public method](../icons/pubmethod.gif)|
[RenderHighlight](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderHighlight.htm)|
Render a highlight bar. This is highly zoom-dependant. Highlight rendering is
usually the fourth stage in a Capsule Rendering, after the background but
prior to the edges.  
![Public method](../icons/pubmethod.gif)| [RenderIcon(Graphics, Image, Int32,
Int32)](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderIcon_1.htm)|
Render an image icon centered into the box. If the content box has been
defined the icon will be centered there, otherwise the outline box will be
used.  
![Public method](../icons/pubmethod.gif)| [RenderIcon(Graphics, Image,
RectangleF, Int32,
Int32)](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderIcon.htm)|
Render an image icon centered into the box. If the content box has been
defined the icon will be centered there, otherwise the outline box will be
used.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[RenderInputGrip](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderInputGrip.htm)|
Static (Shared in VB) method to render a default input grip.  
![Public method](../icons/pubmethod.gif)|
[RenderMessage](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderMessage.htm)|
Render a text message underneath the capsule.  
![Public method](../icons/pubmethod.gif)|
[RenderOutlines](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderOutlines.htm)|
Render default capsule outlines. If the zoom factor is less than 50% the inner
outline is not drawn. This is usually the fifth stage in a Capsule rendering.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[RenderOutputGrip](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderOutputGrip.htm)|
Static (Shared in VB) method to render a default output grip.  
![Public method](../icons/pubmethod.gif)|
[RenderText](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderText.htm)|
Render the capsule text. This is usually the sixth and final stage in a
capsule rendering.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

