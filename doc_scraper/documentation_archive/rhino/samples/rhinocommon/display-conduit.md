---
url: https://developer.rhino3d.com/samples/rhinocommon/display-conduit/
scraped_at: 2025-09-08T15:45:57.715173
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

Display Conduit

Demonstrates a basic display conduit that draws a custom axis in the Rhino
viewport.

C# VB.NET Python

    
    
    partial class Examples
    {
      static MyConduit m_conduit;
      public static Result DisplayConduit(RhinoDoc doc)
      {
        // The following code lets you toggle the conduit on and off by repeatedly running the command
        if (m_conduit != null)
        {
          m_conduit.Enabled = false;
          m_conduit = null;
        }
        else
        {
          m_conduit = new MyConduit { Enabled = true };
        }
        doc.Views.Redraw();
        return Result.Success;
      }
    }
    
    class MyConduit : Rhino.Display.DisplayConduit
    {
      protected override void CalculateBoundingBox(CalculateBoundingBoxEventArgs e)
      {
        base.CalculateBoundingBox(e);
        e.BoundingBox.Union(e.Display.Viewport.ConstructionPlane().Origin);
      }
    
      protected override void PreDrawObjects(DrawEventArgs e)
      {
        base.PreDrawObjects(e);
    
        var c_plane = e.Display.Viewport.ConstructionPlane();
        var x_color = Rhino.ApplicationSettings.AppearanceSettings.GridXAxisLineColor;
        var y_color = Rhino.ApplicationSettings.AppearanceSettings.GridYAxisLineColor;
        var z_color = Rhino.ApplicationSettings.AppearanceSettings.GridZAxisLineColor;
    
        e.Display.PushDepthWriting(false);
        e.Display.PushDepthTesting(false);
    
        e.Display.DrawPoint(c_plane.Origin, System.Drawing.Color.White);
        e.Display.DrawArrow(new Line(c_plane.Origin, new Vector3d(c_plane.XAxis) * 10.0), x_color);
        e.Display.DrawArrow(new Line(c_plane.Origin, new Vector3d(c_plane.YAxis) * 10.0), y_color);
        e.Display.DrawArrow(new Line(c_plane.Origin, new Vector3d(c_plane.ZAxis) * 10.0), z_color);
    
        e.Display.PopDepthWriting();
        e.Display.PopDepthTesting();
      }
    }
    
    
    
    Partial Friend Class Examples
      Private Shared m_conduit As MyConduit
      Public Shared Function DisplayConduit(ByVal doc As RhinoDoc) As Result
    	' The following code lets you toggle the conduit on and off by repeatedly running the command
    	If m_conduit IsNot Nothing Then
    	  m_conduit.Enabled = False
    	  m_conduit = Nothing
    	Else
    	  m_conduit = New MyConduit With {.Enabled = True}
    	End If
    	doc.Views.Redraw()
    	Return Result.Success
      End Function
    End Class
    
    Friend Class MyConduit
    	Inherits Rhino.Display.DisplayConduit
    
      Protected Overrides Sub CalculateBoundingBox(ByVal e As CalculateBoundingBoxEventArgs)
    	MyBase.CalculateBoundingBox(e)
    	e.BoundingBox.Union(e.Display.Viewport.ConstructionPlane().Origin)
      End Sub
    
      Protected Overrides Sub PreDrawObjects(ByVal e As DrawEventArgs)
    	MyBase.PreDrawObjects(e)
    
    	Dim c_plane = e.Display.Viewport.ConstructionPlane()
    	Dim x_color = Rhino.ApplicationSettings.AppearanceSettings.GridXAxisLineColor
    	Dim y_color = Rhino.ApplicationSettings.AppearanceSettings.GridYAxisLineColor
    	Dim z_color = Rhino.ApplicationSettings.AppearanceSettings.GridZAxisLineColor
    
    	e.Display.PushDepthWriting(False)
    	e.Display.PushDepthTesting(False)
    
    	e.Display.DrawPoint(c_plane.Origin, System.Drawing.Color.White)
    	e.Display.DrawArrow(New Line(c_plane.Origin, New Vector3d(c_plane.XAxis) * 10.0), x_color)
    	e.Display.DrawArrow(New Line(c_plane.Origin, New Vector3d(c_plane.YAxis) * 10.0), y_color)
    	e.Display.DrawArrow(New Line(c_plane.Origin, New Vector3d(c_plane.ZAxis) * 10.0), z_color)
    
    	e.Display.PopDepthWriting()
    	e.Display.PopDepthTesting()
      End Sub
    End Class
    
    
    
    # No Python sample available
    

  

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

