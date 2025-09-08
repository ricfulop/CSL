---
url: https://developer.rhino3d.com/samples/rhinocommon/intersect-line-and-circle/
scraped_at: 2025-09-08T15:46:18.856512
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

Intersecting Line and Circle

Demonstrates how to find the intersection point(s) of a circle and a line.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result IntersectLineCircle(RhinoDoc doc)
      {
        Circle circle;
        var rc = RhinoGet.GetCircle(out circle);
        if (rc != Result.Success)
          return rc;
        doc.Objects.AddCircle(circle);
        doc.Views.Redraw();
    
        Line line;
        rc = RhinoGet.GetLine(out line);
        if (rc != Result.Success)
          return rc;
        doc.Objects.AddLine(line);
        doc.Views.Redraw();
    
        double t1, t2;
        Point3d point1, point2;
        var line_circle_intersect = Intersection.LineCircle(line, circle, out t1, out point1, out t2, out point2);
        string msg = "";
        switch (line_circle_intersect) {
          case LineCircleIntersection.None:
            msg = "line does not intersect circle";
            break;
          case LineCircleIntersection.Single:
            msg = string.Format("line intersects circle at point ({0})", point1);
            doc.Objects.AddPoint(point1);
            break;
          case LineCircleIntersection.Multiple:
            msg = string.Format("line intersects circle at points ({0}) and ({1})",
              point1, point2);
            doc.Objects.AddPoint(point1);
            doc.Objects.AddPoint(point2);
            break;
        }
        RhinoApp.WriteLine(msg);
        doc.Views.Redraw();
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function IntersectLineCircle(ByVal doc As RhinoDoc) As Result
    	Dim circle As Circle = Nothing
    	Dim rc = RhinoGet.GetCircle(circle)
    	If rc IsNot Result.Success Then
    	  Return rc
    	End If
    	doc.Objects.AddCircle(circle)
    	doc.Views.Redraw()
    
    	Dim line As Line = Nothing
    	rc = RhinoGet.GetLine(line)
    	If rc IsNot Result.Success Then
    	  Return rc
    	End If
    	doc.Objects.AddLine(line)
    	doc.Views.Redraw()
    
    	Dim t1 As Double = Nothing, t2 As Double = Nothing
    	Dim point1 As Point3d = Nothing, point2 As Point3d = Nothing
    	Dim line_circle_intersect = Intersection.LineCircle(line, circle, t1, point1, t2, point2)
    	Dim msg As String = ""
    	Select Case line_circle_intersect
    	  Case LineCircleIntersection.None
    		msg = "line does not intersect circle"
    	  Case LineCircleIntersection.Single
    		msg = String.Format("line intersects circle at point ({0})", point1)
    		doc.Objects.AddPoint(point1)
    	  Case LineCircleIntersection.Multiple
    		msg = String.Format("line intersects circle at points ({0}) and ({1})", point1, point2)
    		doc.Objects.AddPoint(point1)
    		doc.Objects.AddPoint(point2)
    	End Select
    	RhinoApp.WriteLine(msg)
    	doc.Views.Redraw()
    	Return Result.Success
      End Function
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

