---
url: https://developer.rhino3d.com/samples/rhinocommon/is-planar-surface-in-plane/
scraped_at: 2025-09-08T15:46:19.853545
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

Is Planar Surface in Plane

Demonstrates how to determine if a user-selected surface is in plane.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result IsPlanarSurfaceInPlane(RhinoDoc doc)
      {
        ObjRef obj_ref;
        var rc = RhinoGet.GetOneObject("select surface", true, ObjectType.Surface, out obj_ref);
        if (rc != Result.Success)
          return rc;
        var surface = obj_ref.Surface();
    
        Point3d[] corners;
        rc = RhinoGet.GetRectangle(out corners);
        if (rc != Result.Success)
          return rc;
    
        var plane = new Plane(corners[0], corners[1], corners[2]);
    
        var is_or_isnt = " not ";
        if (IsSurfaceInPlane(surface, plane, doc.ModelAbsoluteTolerance))
          is_or_isnt = "";
    
        RhinoApp.WriteLine("Surface is{0} in plane.", is_or_isnt);
        return Result.Success;
      }
    
      private static bool IsSurfaceInPlane(Surface surface, Plane plane, double tolerance)
      {
        if (!surface.IsPlanar(tolerance))
          return false;
    
        var bbox = surface.GetBoundingBox(true);
        return bbox.GetCorners().All(c => System.Math.Abs(plane.DistanceTo(c)) <= tolerance);
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function IsPlanarSurfaceInPlane(ByVal doc As RhinoDoc) As Result
    	Dim obj_ref As ObjRef = Nothing
    	Dim rc = RhinoGet.GetOneObject("select surface", True, ObjectType.Surface, obj_ref)
    	If rc IsNot Result.Success Then
    	  Return rc
    	End If
    	Dim surface = obj_ref.Surface()
    
    	Dim corners() As Point3d = Nothing
    	rc = RhinoGet.GetRectangle(corners)
    	If rc IsNot Result.Success Then
    	  Return rc
    	End If
    
    	Dim plane = New Plane(corners(0), corners(1), corners(2))
    
    	Dim is_or_isnt = " not "
    	If IsSurfaceInPlane(surface, plane, doc.ModelAbsoluteTolerance) Then
    	  is_or_isnt = ""
    	End If
    
    	RhinoApp.WriteLine("Surface is{0} in plane.", is_or_isnt)
    	Return Result.Success
      End Function
    
      Private Shared Function IsSurfaceInPlane(ByVal surface As Surface, ByVal plane As Plane, ByVal tolerance As Double) As Boolean
    	If Not surface.IsPlanar(tolerance) Then
    	  Return False
    	End If
    
    	Dim bbox = surface.GetBoundingBox(True)
    	Return bbox.GetCorners().All(Function(c) System.Math.Abs(plane.DistanceTo(c)) <= tolerance)
      End Function
    End Class
    
    
    
    import Rhino
    from Rhino.Geometry import *
    import rhinoscriptsyntax as rs
    from scriptcontext import doc
    import math
    
    def RunCommand():
        surface_id = rs.GetSurfaceObject()[0]
        if surface_id == None:
            return
        surface = rs.coercesurface(surface_id)
    
        corners = rs.GetRectangle()
        if corners == None:
            return
    
        plane = Plane(corners[0], corners[1], corners[2])
    
        is_or_isnt = "" if IsSurfaceInPlane(surface, plane, doc.ModelAbsoluteTolerance) else " not "
        print "Surface is{0} in plane.".format(is_or_isnt)
    
    def IsSurfaceInPlane(surface, plane, tolerance):
        if not surface.IsPlanar(tolerance):
            return False
    
        bbox = surface.GetBoundingBox(True)
        rc = True
        for corner in bbox.GetCorners():
            if math.fabs(plane.DistanceTo(corner)) > tolerance:
                rc = False
                break
    
        return rc
    
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

