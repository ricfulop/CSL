---
url: https://developer.rhino3d.com/samples/rhinocommon/divide-curve-by-segments/
scraped_at: 2025-09-08T15:45:11.531956
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

Divide Curve by Segments

Demonstrates how to divide a user-selected curve into length segments.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result DivideCurveBySegments(RhinoDoc doc)
      {
        const ObjectType filter = ObjectType.Curve;
        ObjRef objref;
        var rc = RhinoGet.GetOneObject("Select curve to divide", false, filter, out objref);
        if (rc != Result.Success || objref == null)
          return rc;
    
        var curve = objref.Curve();
        if (curve == null || curve.IsShort(RhinoMath.ZeroTolerance))
          return Result.Failure;
    
        var segment_count = 2;
        rc = RhinoGet.GetInteger("Divide curve into how many segments?", false, ref segment_count);
        if (rc != Result.Success)
          return rc;
    
        Point3d[] points;
        curve.DivideByCount(segment_count, true, out points);
        if (points == null)
          return Result.Failure;
    
        foreach (var point in points)
          doc.Objects.AddPoint(point);
    
        doc.Views.Redraw();
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function DivideCurveBySegments(ByVal doc As RhinoDoc) As Result
    	Const filter As ObjectType = ObjectType.Curve
    	Dim objref As ObjRef = Nothing
    	Dim rc = RhinoGet.GetOneObject("Select curve to divide", False, filter, objref)
    	If rc IsNot Result.Success OrElse objref Is Nothing Then
    	  Return rc
    	End If
    
    	Dim curve = objref.Curve()
    	If curve Is Nothing OrElse curve.IsShort(RhinoMath.ZeroTolerance) Then
    	  Return Result.Failure
    	End If
    
    	Dim segment_count = 2
    	rc = RhinoGet.GetInteger("Divide curve into how many segments?", False, segment_count)
    	If rc IsNot Result.Success Then
    	  Return rc
    	End If
    
    	Dim points() As Point3d = Nothing
    	curve.DivideByCount(segment_count, True, points)
    	If points Is Nothing Then
    	  Return Result.Failure
    	End If
    
    	For Each point In points
    	  doc.Objects.AddPoint(point)
    	Next point
    
    	doc.Views.Redraw()
    	Return Result.Success
      End Function
    End Class
    
    
    
    from Rhino.DocObjects import *
    from Rhino.Input import *
    from Rhino.Commands import *
    from Rhino.Geometry import *
    from Rhino import *
    from scriptcontext import doc
    
    def RunCommand():
        rc, objref = RhinoGet.GetOneObject("Select curve to divide", False, ObjectType.Curve)
        if rc != Result.Success or objref == None:
            return rc
    
        curve = objref.Curve()
        if curve == None or curve.IsShort(RhinoMath.ZeroTolerance):
            return Result.Failure
    
        segment_count = 2
        rc, segment_count = RhinoGet.GetInteger("Divide curve into how many segments?", False, segment_count)
        if rc != Result.Success:
            return rc
    
        curve_params = curve.DivideByCount(segment_count, True)
        if curve_params == None:
            return Result.Failure
    
        points = [curve.PointAt(t) for t in curve_params]
        for point in points:
            doc.Objects.AddPoint(point)
    
        doc.Views.Redraw()
        return Result.Success
    
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

