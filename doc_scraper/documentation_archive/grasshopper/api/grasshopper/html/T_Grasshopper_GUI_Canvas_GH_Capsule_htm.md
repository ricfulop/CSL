---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_GUI_Canvas_GH_Capsule.htm
scraped_at: 2025-09-08T16:14:34.879180
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm
"Grasshopper.GUI.Canvas")

[GH_Capsule Class](../html/T_Grasshopper_GUI_Canvas_GH_Capsule.htm "GH_Capsule
Class")

[GH_Capsule
Properties](../html/Properties_T_Grasshopper_GUI_Canvas_GH_Capsule.htm
"GH_Capsule Properties")

[GH_Capsule Methods](../html/Methods_T_Grasshopper_GUI_Canvas_GH_Capsule.htm
"GH_Capsule Methods")

[GH_Capsule Fields](../html/Fields_T_Grasshopper_GUI_Canvas_GH_Capsule.htm
"GH_Capsule Fields")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_Capsule Class  
  
---  
  
Class used to draw standard Grasshopper interface boxes.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.GUI.CanvasGH_Capsule  

**Namespace:** [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_Capsule : IDisposable
    
    
    Public Class GH_Capsule
    	Implements IDisposable

The GH_Capsule type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Box](P_Grasshopper_GUI_Canvas_GH_Capsule_Box.htm)|  Gets the outline box for
this Capsule.  
![Public property](../icons/pubproperty.gif)|
[Box_Content](P_Grasshopper_GUI_Canvas_GH_Capsule_Box_Content.htm)|  Gets the
content box for this Capsule. Text and icons are drawn inside this box.  
![Public property](../icons/pubproperty.gif)|
[Font](P_Grasshopper_GUI_Canvas_GH_Capsule_Font.htm)|  Gets or sets the Font
to use for text rendering.  
![Public property](../icons/pubproperty.gif)|
[Highlight](P_Grasshopper_GUI_Canvas_GH_Capsule_Highlight.htm)|  Gets the
highlight size for this Capsule. Zero or negative means there is no highlight.  
![Public property](../icons/pubproperty.gif)|
[HighlightShape](P_Grasshopper_GUI_Canvas_GH_Capsule_HighlightShape.htm)|
Gets the graphics path that describes the highlight bar shape of the capsule.  
![Public property](../icons/pubproperty.gif)|
[InputGrips](P_Grasshopper_GUI_Canvas_GH_Capsule_InputGrips.htm)|  Gets the
list of locally defined input grip locations.  
![Public property](../icons/pubproperty.gif)|
[JaggedLeft](P_Grasshopper_GUI_Canvas_GH_Capsule_JaggedLeft.htm)|  Gets
whether the left edge of this capsule is jagged.  
![Public property](../icons/pubproperty.gif)|
[JaggedRight](P_Grasshopper_GUI_Canvas_GH_Capsule_JaggedRight.htm)|  Gets
whether the right edge of this capsule is jagged.  
![Public property](../icons/pubproperty.gif)|
[MaxRadius](P_Grasshopper_GUI_Canvas_GH_Capsule_MaxRadius.htm)|  Gets the
largest radius defined for this capsule.  
![Public property](../icons/pubproperty.gif)|
[OutlineShape](P_Grasshopper_GUI_Canvas_GH_Capsule_OutlineShape.htm)|  Gets
the graphics path that describes the outer edge of the capsule.  
![Public property](../icons/pubproperty.gif)|
[OutputGrips](P_Grasshopper_GUI_Canvas_GH_Capsule_OutputGrips.htm)|  Gets the
list of locally defined output grip locations.  
![Public property](../icons/pubproperty.gif)|
[Palette](P_Grasshopper_GUI_Canvas_GH_Capsule_Palette.htm)|  Gets or sets the
palette for this Capsule.  
![Public property](../icons/pubproperty.gif)|
[Radius](P_Grasshopper_GUI_Canvas_GH_Capsule_Radius.htm)|  Gets the radius of
the rounded corners of this Capsule.  
![Public property](../icons/pubproperty.gif)|
[RenderEngine](P_Grasshopper_GUI_Canvas_GH_Capsule_RenderEngine.htm)|  Gets
the RenderEngine associated with this capsule. You typically don't need to go
this far, just use one of the Render() overloads on GH_Capsule directly.  
![Public property](../icons/pubproperty.gif)|
[Text](P_Grasshopper_GUI_Canvas_GH_Capsule_Text.htm)|  Gets or sets the text
to render in the content box.  
![Public property](../icons/pubproperty.gif)|
[TextOrientation](P_Grasshopper_GUI_Canvas_GH_Capsule_TextOrientation.htm)|
Gets or sets the orientation of the text within the content box.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[AddInputGrip(Point)](M_Grasshopper_GUI_Canvas_GH_Capsule_AddInputGrip.htm)|
Add an input grip to this UI Box.  
![Public method](../icons/pubmethod.gif)|
[AddInputGrip(PointF)](M_Grasshopper_GUI_Canvas_GH_Capsule_AddInputGrip_1.htm)|
Add an input grip to this UI Box.  
![Public method](../icons/pubmethod.gif)|
[AddInputGrip(Single)](M_Grasshopper_GUI_Canvas_GH_Capsule_AddInputGrip_2.htm)|
Add an input grip to this UI Box. This is the recommended overload.  
![Public method](../icons/pubmethod.gif)| [AddInputGrip(Single,
Single)](M_Grasshopper_GUI_Canvas_GH_Capsule_AddInputGrip_3.htm)|  Add an
input grip to this UI Box.  
![Public method](../icons/pubmethod.gif)|
[AddOutputGrip(Point)](M_Grasshopper_GUI_Canvas_GH_Capsule_AddOutputGrip.htm)|
Add an output grip to this UI Box.  
![Public method](../icons/pubmethod.gif)|
[AddOutputGrip(PointF)](M_Grasshopper_GUI_Canvas_GH_Capsule_AddOutputGrip_1.htm)|
Add an output grip to this UI Box.  
![Public method](../icons/pubmethod.gif)|
[AddOutputGrip(Single)](M_Grasshopper_GUI_Canvas_GH_Capsule_AddOutputGrip_2.htm)|
Add an output grip to this UI Box. This is the recommended overload.  
![Public method](../icons/pubmethod.gif)| [AddOutputGrip(Single,
Single)](M_Grasshopper_GUI_Canvas_GH_Capsule_AddOutputGrip_3.htm)|  Add an
output grip to this UI Box.  
![Public method](../icons/pubmethod.gif)|
[Contains](M_Grasshopper_GUI_Canvas_GH_Capsule_Contains.htm)|  Test a point
for capsule containment.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateCapsule(Rectangle,
GH_Palette)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateCapsule.htm)|  Create a
new blank capsule with default radius and highlight dimensions.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateCapsule(RectangleF,
GH_Palette)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateCapsule_3.htm)|  Create
a new blank capsule with default radius and highlight dimensions.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateCapsule(Rectangle, GH_Palette, Int32,
Int32)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateCapsule_1.htm)|  Create a
new blank capsule.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateCapsule(Rectangle, GH_Palette, Int32,
Int32)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateCapsule_2.htm)|  Create a
new blank capsule.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateCapsule(RectangleF, GH_Palette, Int32,
Int32)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateCapsule_4.htm)|  Create a
new blank capsule.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateCapsule(RectangleF, GH_Palette, Int32,
Int32)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateCapsule_5.htm)|  Create a
new blank capsule.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateTextCapsule(Rectangle, Rectangle, GH_Palette,
String)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateTextCapsule.htm)|  Create a
new capsule with content text.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateTextCapsule(RectangleF, RectangleF, GH_Palette,
String)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateTextCapsule_9.htm)|  Create
a new capsule with content text.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateTextCapsule(Rectangle, Rectangle, GH_Palette, String,
Font)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateTextCapsule_1.htm)|  Create a
new capsule with content text.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateTextCapsule(RectangleF, RectangleF, GH_Palette, String,
Font)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateTextCapsule_10.htm)|  Create
a new capsule with content text.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateTextCapsule(Rectangle, Rectangle, GH_Palette, String, Font,
GH_Orientation)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateTextCapsule_2.htm)|
Create a new capsule with content text.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateTextCapsule(Rectangle, Rectangle, GH_Palette, String, Int32,
Int32)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateTextCapsule_7.htm)|  Create
a new capsule with content text.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateTextCapsule(Rectangle, Rectangle, GH_Palette, String, Int32,
Int32)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateTextCapsule_8.htm)|  Create
a new capsule with content text.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateTextCapsule(RectangleF, RectangleF, GH_Palette, String, Font,
GH_Orientation)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateTextCapsule_11.htm)|
Create a new capsule with content text.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateTextCapsule(RectangleF, RectangleF, GH_Palette, String, Int32,
Int32)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateTextCapsule_16.htm)|  Create
a new capsule with content text.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateTextCapsule(RectangleF, RectangleF, GH_Palette, String, Int32,
Int32)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateTextCapsule_17.htm)|  Create
a new capsule with content text.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateTextCapsule(Rectangle, Rectangle, GH_Palette, String, Font, Int32,
Int32)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateTextCapsule_5.htm)|  Create
a new capsule with content text.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateTextCapsule(Rectangle, Rectangle, GH_Palette, String, Font, Int32,
Int32)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateTextCapsule_6.htm)|  Create
a new capsule with content text.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateTextCapsule(RectangleF, RectangleF, GH_Palette, String, Font, Int32,
Int32)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateTextCapsule_14.htm)|  Create
a new capsule with content text.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateTextCapsule(RectangleF, RectangleF, GH_Palette, String, Font, Int32,
Int32)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateTextCapsule_15.htm)|  Create
a new capsule with content text.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateTextCapsule(Rectangle, Rectangle, GH_Palette, String, Font,
GH_Orientation, Int32,
Int32)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateTextCapsule_3.htm)|  Create
a new capsule with content text.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateTextCapsule(Rectangle, Rectangle, GH_Palette, String, Font,
GH_Orientation, Int32,
Int32)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateTextCapsule_4.htm)|  Create
a new capsule with content text.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateTextCapsule(RectangleF, RectangleF, GH_Palette, String, Font,
GH_Orientation, Int32,
Int32)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateTextCapsule_12.htm)|  Create
a new capsule with content text.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateTextCapsule(RectangleF, RectangleF, GH_Palette, String, Font,
GH_Orientation, Int32,
Int32)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateTextCapsule_13.htm)|  Create
a new capsule with content text.  
![Public method](../icons/pubmethod.gif)|
[Dispose](M_Grasshopper_GUI_Canvas_GH_Capsule_Dispose.htm)| Releases all
resources used by the GH_Capsule  
![Protected method](../icons/protmethod.gif)|
[Dispose(Boolean)](M_Grasshopper_GUI_Canvas_GH_Capsule_Dispose_1.htm)|
Releases the unmanaged resources used by the GH_Capsule and optionally
releases the managed resources  
![Public method](../icons/pubmethod.gif)| [Render(Graphics,
GH_PaletteStyle)](M_Grasshopper_GUI_Canvas_GH_Capsule_Render.htm)|  Have this
capsule draw itself onto a Graphics surface with a custom Style override.  
![Public method](../icons/pubmethod.gif)| [Render(Graphics,
Color)](M_Grasshopper_GUI_Canvas_GH_Capsule_Render_2.htm)|  Have this capsule
draw itself onto a Graphics surface with a custom colour override.  
![Public method](../icons/pubmethod.gif)| [Render(Graphics, Image,
GH_PaletteStyle)](M_Grasshopper_GUI_Canvas_GH_Capsule_Render_3.htm)|  Have
this capsule draw itself onto a Graphics surface with a custom Style override.  
![Public method](../icons/pubmethod.gif)| [Render(Graphics, Image,
Color)](M_Grasshopper_GUI_Canvas_GH_Capsule_Render_5.htm)|  Have this capsule
draw itself onto a Graphics surface with a custom colour override.  
![Public method](../icons/pubmethod.gif)| [Render(Graphics, Boolean, Boolean,
Boolean)](M_Grasshopper_GUI_Canvas_GH_Capsule_Render_1.htm)|  Render the
capsule onto a graphics context.  
![Public method](../icons/pubmethod.gif)| [Render(Graphics, Image, Boolean,
Boolean, Boolean)](M_Grasshopper_GUI_Canvas_GH_Capsule_Render_4.htm)|  Render
the capsule onto a graphics context.  
![Public method](../icons/pubmethod.gif)|
[SetJaggedEdges](M_Grasshopper_GUI_Canvas_GH_Capsule_SetJaggedEdges.htm)|
Assign left and right jagged edges.  
Top

![](../icons/SectionExpanded.png)Fields

| Name| Description  
---|---|---  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[DefaultHighlight](F_Grasshopper_GUI_Canvas_GH_Capsule_DefaultHighlight.htm)|
The default size (in pixel units) of the highlight bar.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[DefaultRadius](F_Grasshopper_GUI_Canvas_GH_Capsule_DefaultRadius.htm)|  The
default radius (in pixel units) of the rounded corners.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

