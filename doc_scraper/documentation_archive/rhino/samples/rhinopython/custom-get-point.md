---
url: https://developer.rhino3d.com/samples/rhinopython/custom-get-point/
scraped_at: 2025-09-08T15:47:04.883256
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

Custom Getpoint

A Rhino GetPoint that performs some custom dynamic drawing.

Python

    
    
    # A Rhino GetPoint that performs some custom dynamic drawing
    import Rhino
    import System.Drawing
    import scriptcontext
    
    def CustomArc3Point():
        # Color to use when drawing dynamic lines
        line_color = System.Drawing.Color.FromArgb(255,0,0)
        arc_color = System.Drawing.Color.FromArgb(150,0,50)
    
        rc, pt_start = Rhino.Input.RhinoGet.GetPoint("Start point of arc", False)
        if( rc!=Rhino.Commands.Result.Success ): return
        rc, pt_end = Rhino.Input.RhinoGet.GetPoint("End point of arc", False)
        if( rc!=Rhino.Commands.Result.Success ): return
    
        # This is a function that is called whenever the GetPoint's
        # DynamicDraw event occurs
        def GetPointDynamicDrawFunc( sender, args ):
            #draw a line from the first picked point to the current mouse point
            args.Display.DrawLine(pt_start, args.CurrentPoint, line_color, 2)
            #draw a line from the second picked point to the current mouse point
            args.Display.DrawLine(pt_end, args.CurrentPoint, line_color, 2)
            #draw an arc through these three points
            arc = Rhino.Geometry.Arc(pt_start, args.CurrentPoint, pt_end)
            args.Display.DrawArc(arc, arc_color, 1)
    
        # Create an instance of a GetPoint class and add a delegate
        # for the DynamicDraw event
        gp = Rhino.Input.Custom.GetPoint()
        gp.DynamicDraw += GetPointDynamicDrawFunc
        gp.Get()
        if( gp.CommandResult() == Rhino.Commands.Result.Success ):
            pt = gp.Point()
            arc = Rhino.Geometry.Arc(pt_start,pt,pt_end)
            scriptcontext.doc.Objects.AddArc(arc)
            scriptcontext.doc.Views.Redraw()
    
    
    if( __name__ == "__main__" ):
        CustomArc3Point()
    

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

