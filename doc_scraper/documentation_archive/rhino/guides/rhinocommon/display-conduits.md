---
url: https://developer.rhino3d.com/guides/rhinocommon/display-conduits/
scraped_at: 2025-09-08T15:36:46.883550
title: Untitled
---

[RhinoDeveloper®](/)

[design, model, present, analyze, realize...](/)

[![Rhino Logo](https://developer.rhino3d.com/images/rhinodevlogo.png)](/)

__

[Guides](https://developer.rhino3d.com/guides)
[Samples](https://developer.rhino3d.com/samples)
[API](https://developer.rhino3d.com/api)
[Videos](https://developer.rhino3d.com/videos)
[Community](https://discourse.mcneel.com/c/rhino-developer) [my account
](https://www.rhino3d.com/my-account/ "Manage your account, licenses, and
teams")

[Display Conduits](https://developer.rhino3d.com/guides/rhinocommon/display-
conduits/)

  * Conduit Concept
  * Implementation
  * Warning

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoCommon
Guides](https://developer.rhino3d.com/en/guides/rhinocommon/) /

Display Conduits

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

Rhino lets you define your own display conduits, which provide access to many
levels of the display pipeline. They are a bit tricky. This guide cover the
concepts and basics of using display conduits.

## Conduit Concept

The DisplayPipeline in Rhino is a big and complicated class and we do not
recommend you derive your own pipeline. Instead, we’ve exposed something
called a conduit for easy access. The pipeline itself is structured like this
(except in reality there are many more channels):

![Rhino Display Pipeline](https://developer.rhino3d.com/images/display-
conduits-01.png)

At one end is the Rhino model, a collection of 3D geometry and data. At the
other end is the image we want to display on the screen, a collection of 2D
pixels. To get from model to image, the pipeline has to process a lot of
information. These steps have been put into channels. When you implement a new
conduit, you have to implement at least one of these channels, like so:

![Rhino Display Conduit](https://developer.rhino3d.com/images/display-
conduits-02.png)

Note that the pipeline itself is not bound to the channels. It just executes
its code and raises events during specific phases of drawing. During the
drawing of a single frame the events are raised in the following order. You
hook into the pipeline by extending DisplayConduit and overriding the event
handlers that have the same name as the pipeline events:

  1. _ObjectCulling_ : Create a list of all the objects to draw.
  2. _CalculateBoundingBox_ : Determine the extent of the entire scene. Override this function to increase the bounding box of scene so it includes the geometry that you plan to draw.
  3. _CalculateBoundingBoxZoomExtents_ : If you want to participate in the Zoom Extents command with your display conduit, then you need to override ZoomExtentsBoundingBox. Typically you could just call your CalculateBoundingBox override, but you may also want to spend a little more time here and compute a tighter bounding box for your conduit geometry.
  4. _PreDrawObjects_ : Called before objects are drawn. Depth writing and testing are on. Here you could set up the object’s display attributes.
  5. _PreDrawObject_ : Called before every object in the scene is drawn.
  6. _PostDrawObjects_ : Called after all non-highlighted objects are drawn. Depth writing and testing are still turned on. If you want to draw without depth writing and testing, see DrawForeground. Here you draw stuff on top of all the objects, like selection wireframes.
  7. _DrawForeground_ : Called after all non-highlighted objects are drawn and PostDrawObjects called. Depth writing and testing are turned _off_. If you want to draw with depth writing and testing, see PostDrawObjects. For example, here you could draw objects like the little axis-system in the lower left corner of viewports.
  8. _DrawOverlay_ : If Rhino is in a feedback mode, the draw overlay call lets temporary geometry be drawn on top of everything in the scene. This is similar to the dynamic draw routine that occurs with custom get point.

You hook into the pipeline by extending DisplayConduit and overriding the key
event handlers which have the same name as the pipeline events.

## Implementation

In the above image, the conduit overrode two event handlers;
`CalculateBoundingBox` and `PostDrawObjects`. In RhinoCommon this conduit
would look like:

    
    
    class MyConduit : Rhino.Display.DisplayConduit
    {
      protected override void CalculateBoundingBox(CalculateBoundingBoxEventArgs e)
      {
        base.CalculateBoundingBox(e);
        // ..
      }
    
      protected override void PostDrawObjects(DrawEventArgs e)
      {
        base.PreDrawObjects(e);
        // ..
      }
    }
    

By default, conduits are not enabled but it is easily done by setting the
Enabled property of the DisplayConduit to true:

    
    
    var conduit = new MyConduit();
    conduit.Enabled = true;
    

Once our conduit is constructed and enabled, the overriden methods will be
called whenever the Rhino pipeline raises the event for which our overridden
method is registered. In our case, this method will always be called once with
the `CalculateBoundingBox` and the `PostDrawObjects` events have been raised
(the events have the same name as the overridden methods). Here’s a simple
example:

    
    
    class MyConduit : Rhino.Display.DisplayConduit
    {
      protected override void CalculateBoundingBox(CalculateBoundingBoxEventArgs e)
      {
        base.CalculateBoundingBox(e);
        var bbox = new BoundingBox();
        bbox.Union(new Point3d(0, 0, 0));
        e.IncludeBoundingBox(bbox);
      }
    
      protected override void PreDrawObjects(DrawEventArgs e)
      {
        base.PreDrawObjects(e);
        e.Display.DrawPoint(new Point3d(0, 0, 0));
      }
    }
    

The code above simply draws a single point at the world origin. Since a point
is 3D geometry, it is subject to z-depth clipping. This means that if the
point resides outside the z-buffer region, it will not be visible (it will get
_clipped_). By default, the clipping planes are set up to encompass the
bounding box of the entire Rhino model. If you are drawing stuff which is
potentially outside this box, you should override `CalculateBoundingBox` to
make sure your objects are not clipped.

Let’s take a look at a more complex drawing routine:

    
    
    protected override void CalculateBoundingBox(CalculateBoundingBoxEventArgs e)
    {
      base.CalculateBoundingBox(e);
      var bbox = new BoundingBox();
      bbox.Union(e.Display.Viewport.ConstructionPlane().Origin);
      e.IncludeBoundingBox(bbox);
    }
    
    protected override void PreDrawObjects(DrawEventArgs e)
    {
      base.PreDrawObjects(e);
    
      var cPlane = e.Display.Viewport.ConstructionPlane();
      var xColor = Rhino.ApplicationSettings.AppearanceSettings.GridXAxisLineColor;
      var yColor = Rhino.ApplicationSettings.AppearanceSettings.GridYAxisLineColor;
      var zColor = Rhino.ApplicationSettings.AppearanceSettings.GridZAxisLineColor;
    
      e.Display.EnableDepthWriting(false);
      e.Display.EnableDepthTesting(false);
    
      e.Display.DrawPoint(cPlane.Origin, System.Drawing.Color.White);
      e.Display.DrawArrow(new Line(cPlane.Origin, new Vector3d(cPlane.XAxis) * 10.0), xColor);
      e.Display.DrawArrow(new Line(cPlane.Origin, new Vector3d(cPlane.YAxis) * 10.0), yColor);
      e.Display.DrawArrow(new Line(cPlane.Origin, new Vector3d(cPlane.ZAxis) * 10.0), zColor);
    
      e.Display.EnableDepthWriting(false);
      e.Display.EnableDepthTesting(false);
    }
    

This piece of code draws a colored, c-plane axis system on top of all objects.
Because we disable DepthWriting and Testing before drawing my points and
arrows, my objects are not obscured by the existing geometry (which was drawn
in a channel previous to `PostDrawObjects`):

![Resulting Frame](https://developer.rhino3d.com/images/display-
conduits-03.png)

## Warning

Another thing to realize is that there can be many other active conduits
present as well. There is no way of telling which one will be called first. It
is important to consider how your display conduits will interact with other
conduits potentially called within the pipeline by other developers. Do not
write display conduit code that intentionally disrupts other conduits.

![Many Conduits](https://developer.rhino3d.com/images/display-conduits-04.png)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinocommon/display-
conduits/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinocommon/display-
conduits/index.md) [ Admin](https://developer.rhino3d.com/admin)

[Find a Reseller](https://www.rhino3d.com/sales)

[Shop online](https://www.rhino3d.com/store) or find a
[Reseller](https://www.rhino3d.com/sales)

[Find a Reseller](https://www.rhino3d.com/sales)

[Privacy Policy](https://www.rhino3d.com/privacy) •
[About](https://www.rhino3d.com/mcneel/about) • [Contact
Us](https://www.rhino3d.com/mcneel/contact) • [
Language](https://www.rhino3d.com/language "Change to a different region or
language")

[Copyright © 1993-2025 Robert McNeel & Associates. All Rights
Reserved.](https://www.rhino3d.com/mcneel/about)

[](https://www.facebook.com/McNeelRhinoceros/)
[](https://twitter.com/bobmcneel) [](https://www.linkedin.com/groups/75313/)
[](https://www.youtube.com/user/RhinoGuide/videos) [](https://vimeo.com/rhino)
[![Blogger
icon](https://developer.rhino3d.com/images/blogger.svg)](http://blog.rhino3d.com/)
[![Food4Rhino](https://developer.rhino3d.com/images/f4r_icon_01.svg)](https://www.food4rhino.com)

