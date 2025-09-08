---
url: https://developer.rhino3d.com/samples/rhinocommon/add-leader/
scraped_at: 2025-09-08T15:45:38.650417
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

Add Leader

Demonstrates how to add a leaders to your Rhino model from an array of points.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result Leader(RhinoDoc doc)
      {
        var points = new Point3d[]
        {
          new Point3d(1, 1, 0),
          new Point3d(5, 1, 0),
          new Point3d(5, 5, 0),
          new Point3d(9, 5, 0)
        };
    
        var xy_plane = Plane.WorldXY;
    
        var points2d = new List<Point2d>();
        foreach (var point3d in points)
        {
          double x, y;
          if (xy_plane.ClosestParameter(point3d, out x, out y))
          {
            var point2d = new Point2d(x, y);
            if (points2d.Count < 1 || point2d.DistanceTo(points2d.Last<Point2d>()) > RhinoMath.SqrtEpsilon)
              points2d.Add(point2d);
          }
        }
    
        doc.Objects.AddLeader(xy_plane, points2d);
        doc.Views.Redraw();
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function Leader(ByVal doc As RhinoDoc) As Result
    	Dim points = New Point3d() {
    		New Point3d(1, 1, 0),
    		New Point3d(5, 1, 0),
    		New Point3d(5, 5, 0),
    		New Point3d(9, 5, 0)
    	}
    
    	Dim xy_plane = Plane.WorldXY
    
    	Dim points2d = New List(Of Point2d)()
    	For Each point3d In points
    	  Dim x As Double = Nothing, y As Double = Nothing
    	  If xy_plane.ClosestParameter(point3d, x, y) Then
    		Dim point2d = New Point2d(x, y)
    		If points2d.Count < 1 OrElse point2d.DistanceTo(points2d.Last()) > RhinoMath.SqrtEpsilon Then
    		  points2d.Add(point2d)
    		End If
    	  End If
    	Next point3d
    
    	doc.Objects.AddLeader(xy_plane, points2d)
    	doc.Views.Redraw()
    	Return Result.Success
      End Function
    End Class
    
    
    
    import rhinoscriptsyntax as rs
    
    def RunCommand():
        points = [(1,1,0), (5,1,0), (5,5,0), (9,5,0)]
        rs.AddLeader(points)
    
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

