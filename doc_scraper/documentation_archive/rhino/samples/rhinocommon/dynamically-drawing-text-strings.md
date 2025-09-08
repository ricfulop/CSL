---
url: https://developer.rhino3d.com/samples/rhinocommon/dynamically-drawing-text-strings/
scraped_at: 2025-09-08T15:46:04.775336
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

Dynamically Drawing Text Strings

Demonstrates how to dynamically draw text strings relative to a given screen
to world transform.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result DrawString(RhinoDoc doc)
      {
        var gp = new GetDrawStringPoint();
        gp.SetCommandPrompt("Point");
        gp.Get();
        return gp.CommandResult();
      }
    }
    
    public class GetDrawStringPoint : GetPoint
    {
      protected override void OnDynamicDraw(GetPointDrawEventArgs e)
      {
        base.OnDynamicDraw(e);
        var xform = e.Viewport.GetTransform(CoordinateSystem.World, CoordinateSystem.Screen);
        var current_point = e.CurrentPoint;
        current_point.Transform(xform);
        var screen_point = new Point2d(current_point.X, current_point.Y);
        var msg = string.Format("screen {0:F}, {1:F}", current_point.X, current_point.Y);
        e.Display.Draw2dText(msg, System.Drawing.Color.Blue, screen_point, false);
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function DrawString(ByVal doc As RhinoDoc) As Result
    	Dim gp = New GetDrawStringPoint()
    	gp.SetCommandPrompt("Point")
    	gp.Get()
    	Return gp.CommandResult()
      End Function
    End Class
    
    Public Class GetDrawStringPoint
    	Inherits GetPoint
    
      Protected Overrides Sub OnDynamicDraw(ByVal e As GetPointDrawEventArgs)
    	MyBase.OnDynamicDraw(e)
    	Dim xform = e.Viewport.GetTransform(CoordinateSystem.World, CoordinateSystem.Screen)
    	Dim current_point = e.CurrentPoint
    	current_point.Transform(xform)
    	Dim screen_point = New Point2d(current_point.X, current_point.Y)
    	Dim msg = String.Format("screen {0:F}, {1:F}", current_point.X, current_point.Y)
    	e.Display.Draw2dText(msg, System.Drawing.Color.Blue, screen_point, False)
      End Sub
    End Class
    
    
    
    from Rhino import *
    from Rhino.DocObjects import *
    from Rhino.Geometry import *
    from Rhino.Commands import *
    from Rhino.Input.Custom import *
    from System.Drawing import Color
    
    def RunCommand():
        gp = GetDrawStringPoint()
        gp.SetCommandPrompt("Point")
        gp.Get()
        return gp.CommandResult()
    
    class GetDrawStringPoint(GetPoint):
        def OnDynamicDraw(self, e):
            xform = e.Viewport.GetTransform(CoordinateSystem.World, CoordinateSystem.Screen)
    
            current_point = e.CurrentPoint
            current_point.Transform(xform)
            screen_point = Point2d(current_point.X, current_point.Y)
    
            msg = "screen {0}, {1}".format(screen_point.X, screen_point.Y)
            e.Display.Draw2dText(msg, Color.Blue, screen_point, False)
    
    if __name__ == "__main__":
        RunCommand()
    

  

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

