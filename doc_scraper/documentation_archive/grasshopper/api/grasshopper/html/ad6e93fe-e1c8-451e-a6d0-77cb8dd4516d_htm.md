---
url: https://developer.rhino3d.com/api/grasshopper/html/ad6e93fe-e1c8-451e-a6d0-77cb8dd4516d.htm
scraped_at: 2025-09-08T16:10:30.812616
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Examples](../html/d113a9f0-6e27-46df-8316-2079c44382ac.htm "Examples")

[Visual Basic .NET](../html/b883d0c0-4947-48bc-8e9e-492a6d6c2a06.htm "Visual
Basic .NET")

[Simple Component (VB)](../html/b883d0c0-4947-48bc-8e9e-492a6d6c2a06.htm
"Simple Component \(VB\)")

[Simple Mathematics (VB)](../html/2824c770-2673-49a3-8683-1a70bc0349cc.htm
"Simple Mathematics \(VB\)")

[Simple Geometry (VB)](../html/4306b177-1bf1-41bc-ac0e-2f6869d02365.htm
"Simple Geometry \(VB\)")

[Simple Data Types (VB)](../html/f9aa207f-3d19-414c-af01-1e5ad42a8cab.htm
"Simple Data Types \(VB\)")

[Simple Parameters (VB)](../html/0edd8dc9-32a7-40aa-b217-8e01e35e58bc.htm
"Simple Parameters \(VB\)")

[List Component (VB)](../html/4db493ec-0bb3-4b73-943a-fdff03863e1d.htm "List
Component \(VB\)")

[Extending the GUI (VB)](../html/99cd32c8-7c1f-4f9a-87ea-76b032de7f70.htm
"Extending the GUI \(VB\)")

[Custom Attributes (VB)](../html/ad6e93fe-e1c8-451e-a6d0-77cb8dd4516d.htm
"Custom Attributes \(VB\)")

[Custom Component Options
(VB)](../html/434018c0-6110-4478-bf2a-dcd099d8b8b2.htm "Custom Component
Options \(VB\)")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# Custom Attributes (VB)  
  
---  
  
  * Introduction
  * Grasshopper.Kernel.GH_Attributes
  * Layout
  * Render

This article contains a step-by-step walkthrough regarding custom object
display. Objects on the Grasshopper canvas consist of two parts. The most
important piece is the class that implements the
[IGH_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm) interface.
This interface provides the basic plumbing needed to make objects work within
a Grasshopper node network. The interface part of objects however is handled
separately. Every IGH_DocumentObject carries around an instance of a class
that implements the [IGH_Attributes](T_Grasshopper_Kernel_IGH_Attributes.htm)
interface (indeed, every IGH_DocumentObject knows how to create its own stand-
alone attributes) and it is this class that takes care of display, mouse
interactions, popup menus, tooltips and so forth.

In this article I'll explain how you can create your own attributes object.
Since it's not possible to have an IGH_Attributes instance work on its own, we
need an IGH_DocumentObject to tie it to. For this article we'll assume we have
a custom simple parameter (i.e. without persistent data) that holds integers.

VB

Copy

    
    
    Public Class MySimpleIntegerParameter
      Inherits GH_Param(Of Types.GH_Integer)
    
      Public Sub New()
        MyBase.New(New GH_InstanceDescription("Integer with stats", "Int(stats)", "Integer with basic statistics", "Params", "Primitive"))
      End Sub
    
      Public Overrides ReadOnly Property ComponentGuid() As System.Guid
        Get
          Return New Guid("{33D07726-8298-4104-9EBC-5398D8AD5420}")
        End Get
      End Property
    End Class

What we'll do is create a special attributes object for this parameter which
also displays the median and mean values of the collection of all integers. We
want to put this information below the parameter name, but inside the
parameter box. The first step here is to override the CreateAttributes() on
MySimpleIntegerParameter and assign a new instance of our (yet to be written)
attributes class:

VB

Copy

    
    
    Public Overrides Sub CreateAttributes()
      m_attributes = New MySimpleIntegerParameterAttributes(Me)
    End Sub

That's it, no more code is required inside the MySimpleIntegerParameter class.
This part at least is simple. If you _don't_ override the CreateAttributes()
method, then an instance of
[GH_FloatingParamAttributes](T_Grasshopper_Kernel_Attributes_GH_FloatingParamAttributes.htm)
will be created instead. If your parameter is to be attached to a component as
an input or output, then the component will assign an instance of
[GH_LinkedParamAttributes](T_Grasshopper_Kernel_Attributes_GH_LinkedParamAttributes.htm)
to the parameter and CreateAttributes() will never be called.

![](../icons/SectionExpanded.png)Grasshopper.Kernel.GH_Attributes

Although the [IGH_Attributes](T_Grasshopper_Kernel_IGH_Attributes.htm)
interface is required for custom attributes, it is usually a good idea to
derive from one of the abstract attribute classes already available.
[GH_AttributesT](T_Grasshopper_Kernel_GH_Attributes_1.htm) is the most basic
and obvious choice and it implements a large amount of methods with default
behaviour, saving you a lot of time and effort:

VB

Copy

    
    
    Public Class MySimpleIntegerParameterAttributes
      Inherits GH_Attributes(Of MySimpleIntegerParameter)
    
      Public Sub New(ByVal owner As MySimpleIntegerParameter)
        MyBase.New(owner)
      End Sub
    End Class

This is enough so far to make it work, eventhough all the logic is still
standard. We need to start overriding methods in
MySimpleIntegerParameterAttributes to suit our needs. But first some basic
information regarding the default behaviour.

GH_Attributes(Of T) assumes that the object that owns it is rectangular. This
is true for most objects in Grasshopper, but there are some notable exceptions
such as Pie-Graphs, Sketches and Scribbles. But this assumption (which holds
true in our case) allows GH_Attributes(Of T) to supply basic functionality for
a wide variety of methods.

All attributes have a property that defines the size of the object called
[Bounds](P_Grasshopper_Kernel_IGH_Attributes_Bounds.htm). Basically everything
that happens outside of the Bounds goes by unnoticed. Also, if the Bounds
rectangle is not visible within the canvas area, Grasshopper might decide to
not even bother calling any painting methods.

Because our parameter will be rectangular, we don't have to override any of
the picking logic, as the default implementation of
[IsPickRegion](Overload_Grasshopper_Kernel_GH_Attributes_1_IsPickRegion.htm),
[IsMenuRegion](M_Grasshopper_Kernel_GH_Attributes_1_IsMenuRegion.htm) and
[IsTooltipRegion](M_Grasshopper_Kernel_GH_Attributes_1_IsTooltipRegion.htm)
will already work.

![](../icons/SectionExpanded.png)Layout

We do however need to supply custom Layout logic. The width of our Attributes
depends on both the length of the NickName of the MySimpleIntegerParameter
that owns these attributes _and_ on the length of the statistics information
we want to include. The height of the parameter however is fixed, though
larger than the standard height for parameters in Grasshopper.

In order to supply custom layout logic, we need to override the
[Layout](M_Grasshopper_Kernel_GH_Attributes_1_Layout.htm) method. In this case
I measure the width of the NickName of the Owner object, and make sure the
parameter is never narrower than 80 pixels:

VB

Copy

    
    
    Protected Overrides Sub Layout()
      'Compute the width of the NickName of the owner (plus some extra padding), 
      'then make sure we have at least 80 pixels.
      Dim width As Int32 = GH_FontServer.StringWidth(Owner.NickName, GH_FontServer.Standard)
      width = Math.Max(width + 10, 80)
    
      'The height of our object is always 60 pixels
      Dim height As Int32 = 60
    
      'Assign the width and height to the Bounds property.
      'Also, make sure the Bounds are anchored to the Pivot
      Bounds = New RectangleF(Pivot, New SizeF(width, height))
    End Sub

The Pivot is a PointF structure that is changed when the object is dragged. It
is therefore important that you always 'anchor' the layout of some attributes
to the Pivot. If you fail to do so, your attributes will become undraggable.

There is a method you can override that will be called prior to the call to
[Layout](M_Grasshopper_Kernel_GH_Attributes_1_Layout.htm) which can be used to
destroy any cached data you might have that's to do with display. But note
that if you override
[ExpireLayout](M_Grasshopper_Kernel_GH_Attributes_1_ExpireLayout.htm) you
_must_ place a call to the base class method as well:

VB

Copy

    
    
    Public Overrides Sub ExpireLayout()
      MyBase.ExpireLayout()
    
      'Destroy any data you have that becomes 
      'invalid when the layout expires.
    End Sub

![](../icons/SectionExpanded.png)Render

Now that we have handled the layout, we need to override the display of the
parameter. There's two parts to doing so. You always have to override the
[Render](M_Grasshopper_Kernel_GH_Attributes_1_Render.htm) method, as this is
where the drawing takes place. Render is called a number of times as there are
several 'layers' or 'channels' to a single Grasshopper canvas. At first, the
background of the canvas is drawn. During this process attributes are not yet
involved. Then there will be four channels where IGH_Attributes will be
allowed to draw various shapes.

First the groups are drawn (as they are behind all other objects), but every
GH_Attributes.Render() method will be called once for the
[Groups](T_Grasshopper_GUI_Canvas_GH_CanvasChannel.htm) channel. Typically you
should not draw anything in the Groups channel.

Next up is the [Wires](T_Grasshopper_GUI_Canvas_GH_CanvasChannel.htm) channel
where all parameter connector wires are drawn. If your object has input
parameters or is a parameter, it is your responsibility to draw all wires
coming into your object. Wires going out the right side will be drawn by the
recipient objects.

Next the actual components and parameters themselves are drawn inside the
[Objects](T_Grasshopper_GUI_Canvas_GH_CanvasChannel.htm) channel. This is
typically the most work, though there are lots of classes that take care of
common tasks. The default visual style of components and parameter objects is
the shiny rectangle with rounded corners. You can use the
[GH_Capsule](T_Grasshopper_GUI_Canvas_GH_Capsule.htm) type to draw these
shapes with a minimum of fuss.

Ultimately there's an [Overlay](T_Grasshopper_GUI_Canvas_GH_CanvasChannel.htm)
channel which is rarely used but it allows you to draw shapes that need to be
on top of all other components and parameters. After this, there are still
more channels to do with canvas widgets, but IGH_Attributes are not involved
here.

Inside our implementation of the Render() method, we need to draw the wires
coming into the MySimpleIntegerParameter, then the parameter capsule, while
taking care to assign the correct colours (grey for normal, green for
selected, dark for disabled, orange for warnings and red for errors). Finally
we have to draw three lines of text on top of the capsule; the name of the
owner, the median integer and the mean integer. The important types involved
here are:

  * [GH_Canvas](T_Grasshopper_GUI_Canvas_GH_Canvas.htm)
  * [GH_Painter](T_Grasshopper_GUI_Canvas_GH_Painter.htm)
  * [GH_Palette](T_Grasshopper_GUI_Canvas_GH_Palette.htm)
  * [GH_RuntimeMessageLevel](T_Grasshopper_Kernel_GH_RuntimeMessageLevel.htm)
  * [GH_Capsule](T_Grasshopper_GUI_Canvas_GH_Capsule.htm)
  * [GH_FontServer](T_Grasshopper_Kernel_GH_FontServer.htm)

VB

Copy

    
    
    Protected Overrides Sub Render(ByVal canvas As GH_Canvas, ByVal graphics As Graphics, ByVal channel As GH_CanvasChannel)
      'Render all the wires that connect the Owner to all its Sources.
      If (channel = GH_CanvasChannel.Wires) Then
        RenderIncomingWires(canvas.Painter, Owner.Sources, Owner.WireDisplay)
        Return
      End If
    
      'Render the parameter capsule and any additional text on top of it.
      If (channel = GH_CanvasChannel.Objects) Then
        'Define the default palette.
        Dim palette As GH_Palette = GH_Palette.Normal
    
        'Adjust palette based on the Owner's worst case messaging level.
        Select Case Owner.RuntimeMessageLevel
          Case GH_RuntimeMessageLevel.Warning
            palette = GH_Palette.Warning
    
          Case GH_RuntimeMessageLevel.Error
            palette = GH_Palette.Error
        End Select
    
        'Create a new Capsule without text or icon.
        Dim capsule As GH_Capsule = GH_Capsule.CreateCapsule(Bounds, palette)
    
        'Render the capsule using the current Selection, Locked and Hidden states.
        'Integer parameters are always hidden since they cannot be drawn in the viewport.
        capsule.Render(graphics, Selected, Owner.Locked, True)
    
        'Always dispose of a GH_Capsule when you're done with it.
        capsule.Dispose()
        capsule = Nothing
    
        'Now it's time to draw the text on top of the capsule.
        'First we'll draw the Owner NickName using a standard font and a black brush.
        'We'll also align the NickName in the center of the Bounds.
        Dim format As New StringFormat()
        format.Alignment = StringAlignment.Center
        format.LineAlignment = StringAlignment.Center
        format.Trimming = StringTrimming.EllipsisCharacter
    
        'Our entire capsule is 60 pixels high, and we'll draw 
        'three lines of text, each 20 pixels high.
        Dim textRectangle As RectangleF = Bounds
        textRectangle.Height = 20
    
        'Draw the NickName in a Standard Grasshopper font.
        graphics.DrawString(Owner.NickName, GH_FontServer.Standard, Brushes.Black, textRectangle, format)
    
    
        'Now we need to draw the median and mean information.
        'Adjust the formatting and the layout rectangle.
        format.Alignment = StringAlignment.Near
        textRectangle.Inflate(-5, 0)
    
        textRectangle.Y += 20
        graphics.DrawString(String.Format("Median: {0}", Owner.MedianValue), _
                            GH_FontServer.StandardItalic, Brushes.Black, _
                            textRectangle, format)
    
        textRectangle.Y += 20
        graphics.DrawString(String.Format("Mean: {0:0.00}", Owner.MeanValue), _
                            GH_FontServer.StandardItalic, Brushes.Black, _
                            textRectangle, format)
    
        'Always dispose of any GDI+ object that implement IDisposable.
        format.Dispose()
      End If
    End Sub

Note that in this case I assume that MySimpleIntegerParameter has two
properties called MedianValue and MeanValue. I haven't written those, as they
are not within the scope of this topic.

If you have cached display objects (for whatever reason I don't want to hear),
a good place to ensure they are valid would be the
[PrepareForRender](M_Grasshopper_Kernel_GH_Attributes_1_PrepareForRender.htm)
method. It is called once (and only once) just before any calls to Render().
You do not need to call the overridden method as it is empty by default.

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

