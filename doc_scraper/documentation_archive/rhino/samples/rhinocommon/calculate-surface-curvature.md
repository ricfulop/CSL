---
url: https://developer.rhino3d.com/samples/rhinocommon/calculate-surface-curvature/
scraped_at: 2025-09-08T15:45:44.693467
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

Calculate Surface Curvature

Demonstrates how to calculate the principle curvature at a user-specified
point on a surface.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result PrincipalCurvature(RhinoDoc doc)
      {
        ObjRef obj_ref;
        var rc = RhinoGet.GetOneObject("Select surface for curvature measurement", true,
          ObjectType.Surface, out obj_ref);
        if (rc != Result.Success)
          return rc;
        var surface = obj_ref.Surface();
    
        var gp = new Rhino.Input.Custom.GetPoint();
        gp.SetCommandPrompt("Select point on surface for curvature measurement");
        gp.Constrain(surface, false);
        gp.Get();
        if (gp.CommandResult() != Result.Success)
          return gp.CommandResult();
        var point_on_surface = gp.Point();
    
        double u, v;
        if (!surface.ClosestPoint(point_on_surface, out u, out v))
          return Result.Failure;
    
        var surface_curvature = surface.CurvatureAt(u, v);
        if (surface_curvature == null)
          return Result.Failure;
    
        RhinoApp.WriteLine("Surface curvature evaluation at parameter: ({0}, {1})", u, v);
    
        RhinoApp.WriteLine("  3-D Point: ({0}, {1}, {2})",
          surface_curvature.Point.X,
          surface_curvature.Point.Y,
          surface_curvature.Point.Z);
    
        RhinoApp.WriteLine("  3-D Normal: ({0}, {1}, {2})",
          surface_curvature.Normal.X,
          surface_curvature.Normal.Y,
          surface_curvature.Normal.Z);
    
        RhinoApp.WriteLine(string.Format("  Maximum principal curvature: {0} ({1}, {2}, {3})",
          surface_curvature.Kappa(0),
          surface_curvature.Direction(0).X,
          surface_curvature.Direction(0).Y,
          surface_curvature.Direction(0).Z));
    
        RhinoApp.WriteLine(string.Format("  Minimum principal curvature: {0} ({1}, {2}, {3})",
          surface_curvature.Kappa(1),
          surface_curvature.Direction(1).X,
          surface_curvature.Direction(1).Y,
          surface_curvature.Direction(1).Z));
    
        RhinoApp.WriteLine("  Gaussian curvature: {0}", surface_curvature.Gaussian);
        RhinoApp.WriteLine("  Mean curvature: {0}", surface_curvature.Mean);
    
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function PrincipalCurvature(ByVal doc As RhinoDoc) As Result
    	Dim obj_ref As ObjRef = Nothing
    	Dim rc = RhinoGet.GetOneObject("Select surface for curvature measurement", True, ObjectType.Surface, obj_ref)
    	If rc IsNot Result.Success Then
    	  Return rc
    	End If
    	Dim surface = obj_ref.Surface()
    
    	Dim gp = New Rhino.Input.Custom.GetPoint()
    	gp.SetCommandPrompt("Select point on surface for curvature measurement")
    	gp.Constrain(surface, False)
    	gp.Get()
    	If gp.CommandResult() <> Result.Success Then
    	  Return gp.CommandResult()
    	End If
    	Dim point_on_surface = gp.Point()
    
    	Dim u As Double = Nothing, v As Double = Nothing
    	If Not surface.ClosestPoint(point_on_surface, u, v) Then
    	  Return Result.Failure
    	End If
    
    	Dim surface_curvature = surface.CurvatureAt(u, v)
    	If surface_curvature Is Nothing Then
    	  Return Result.Failure
    	End If
    
    	RhinoApp.WriteLine("Surface curvature evaluation at parameter: ({0}, {1})", u, v)
    
    	RhinoApp.WriteLine("  3-D Point: ({0}, {1}, {2})", surface_curvature.Point.X, surface_curvature.Point.Y, surface_curvature.Point.Z)
    
    	RhinoApp.WriteLine("  3-D Normal: ({0}, {1}, {2})", surface_curvature.Normal.X, surface_curvature.Normal.Y, surface_curvature.Normal.Z)
    
    	RhinoApp.WriteLine(String.Format("  Maximum principal curvature: {0} ({1}, {2}, {3})", surface_curvature.Kappa(0), surface_curvature.Direction(0).X, surface_curvature.Direction(0).Y, surface_curvature.Direction(0).Z))
    
    	RhinoApp.WriteLine(String.Format("  Minimum principal curvature: {0} ({1}, {2}, {3})", surface_curvature.Kappa(1), surface_curvature.Direction(1).X, surface_curvature.Direction(1).Y, surface_curvature.Direction(1).Z))
    
    	RhinoApp.WriteLine("  Gaussian curvature: {0}", surface_curvature.Gaussian)
    	RhinoApp.WriteLine("  Mean curvature: {0}", surface_curvature.Mean)
    
    	Return Result.Success
      End Function
    End Class
    
    
    
    import rhinoscriptsyntax as rs
    
    surface_id,_,_,_,_,_ = rs.GetSurfaceObject("Select surface for curvature measurement")
    point = rs.GetPointOnSurface(surface_id, "Select point on surface for curvature measurement")
    u,v = rs.SurfaceClosestPoint(surface_id, point)
    
    #point, normal, kappa_u, direction_u, kappa_v, direction_v, gaussian, mean =
    surface_curvature = rs.SurfaceCurvature(surface_id, (u,v))
    
    point, normal, kappa_u, direction_u, kappa_v, direction_v, gaussian, mean = surface_curvature
    
    print "Surface curvature evaluation at parameter: ({0}, {1})".format(u,v)
    
    print "  3-D Point: ({0}, {1}, {2})".format(point.X, point.Y, point.Z)
    
    print "  3-D Normal: ({0}, {1}, {2})".format(normal.X, normal.Y, normal.Z)
    
    print "  Maximum principal curvature: {0} ({1}, {2}, {3})".format(kappa_u, direction_u.X, direction_u.Y, direction_u.Z)
    
    print "  Minimum principal curvature: {0} ({1}, {2}, {3})".format(kappa_v, direction_v.X, direction_v.Y, direction_v.Z)
    
    print "  Gaussian curvature: {0}".format(gaussian)
    print "  Mean curvature: {0}".format(mean)
    

  

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

