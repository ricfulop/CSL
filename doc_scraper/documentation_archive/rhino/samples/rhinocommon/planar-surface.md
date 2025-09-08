---
url: https://developer.rhino3d.com/samples/rhinocommon/planar-surface/
scraped_at: 2025-09-08T15:46:31.871433
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

Planar Surface

Demonstrates how to create a planar surface from a rectangle.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result PlanarSurface(RhinoDoc doc)
      {
        Point3d[] corners;
        var rc = Rhino.Input.RhinoGet.GetRectangle(out corners);
        if (rc != Result.Success)
          return rc;
    
        var plane = new Plane(corners[0], corners[1], corners[2]);
    
        var plane_surface = new PlaneSurface(plane,
          new Interval(0, corners[0].DistanceTo(corners[1])),
          new Interval(0, corners[1].DistanceTo(corners[2])));
    
        doc.Objects.Add(plane_surface);
        doc.Views.Redraw();
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function PlanarSurface(ByVal doc As RhinoDoc) As Result
    	Dim corners() As Point3d = Nothing
    	Dim rc = Rhino.Input.RhinoGet.GetRectangle(corners)
    	If rc IsNot Result.Success Then
    	  Return rc
    	End If
    
    	Dim plane = New Plane(corners(0), corners(1), corners(2))
    
    	Dim plane_surface = New PlaneSurface(plane, New Interval(0, corners(0).DistanceTo(corners(1))), New Interval(0, corners(1).DistanceTo(corners(2))))
    
    	doc.Objects.Add(plane_surface)
    	doc.Views.Redraw()
    	Return Result.Success
      End Function
    End Class
    
    
    
    import Rhino;
    import rhinoscriptsyntax as rs
    
    def RunCommand():
        rc, corners = Rhino.Input.RhinoGet.GetRectangle()
        if rc != Rhino.Commands.Result.Success:
            return rc
    
        plane = Rhino.Geometry.Plane(corners[0], corners[1], corners[2])
        u_dir = rs.Distance(corners[0], corners[1])
        v_dir = rs.Distance(corners[1], corners[2])
        rs.AddPlaneSurface(plane, u_dir, v_dir)
    
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

