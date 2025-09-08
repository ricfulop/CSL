---
url: https://developer.rhino3d.com/samples/rhinocommon/add-radial-dimension/
scraped_at: 2025-09-08T15:45:39.676909
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

Add Radial Dimension

Demonstrates how to add radial dimensions to a selected curve.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result AddRadialDimension(Rhino.RhinoDoc doc)
      {
        ObjRef obj_ref;
        var rc = RhinoGet.GetOneObject("Select curve for radius dimension",
          true, ObjectType.Curve, out obj_ref);
        if (rc != Result.Success)
          return rc;
        double curve_parameter;
        var curve = obj_ref.CurveParameter(out curve_parameter);
        if (curve == null)
          return Result.Failure;
    
        if (curve.IsLinear() || curve.IsPolyline())
        {
          RhinoApp.WriteLine("Curve must be non-linear.");
          return Result.Nothing;
        }
    
        // in this example just deal with planar curves
        if (!curve.IsPlanar())
        {
          RhinoApp.WriteLine("Curve must be planar.");
          return Result.Nothing;
        }
    
        var point_on_curve = curve.PointAt(curve_parameter);
        var curvature_vector = curve.CurvatureAt(curve_parameter);
        var len = curvature_vector.Length;
        if (len < RhinoMath.SqrtEpsilon)
        {
          RhinoApp.WriteLine("Curve is almost linear and therefore has no curvature.");
          return Result.Nothing;
        }
    
        var center = point_on_curve + (curvature_vector/(len*len));
        Plane plane;
        curve.TryGetPlane(out plane);
        var radial_dimension =
          new RadialDimension(center, point_on_curve, plane.XAxis, plane.Normal, 5.0);
        doc.Objects.AddRadialDimension(radial_dimension);
        doc.Views.Redraw();
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function AddRadialDimension(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Dim obj_ref As ObjRef = Nothing
    	Dim rc = RhinoGet.GetOneObject("Select curve for radius dimension", True, ObjectType.Curve, obj_ref)
    	If rc IsNot Result.Success Then
    	  Return rc
    	End If
    	Dim curve_parameter As Double = Nothing
    	Dim curve = obj_ref.CurveParameter(curve_parameter)
    	If curve Is Nothing Then
    	  Return Result.Failure
    	End If
    
    	If curve.IsLinear() OrElse curve.IsPolyline() Then
    	  RhinoApp.WriteLine("Curve must be non-linear.")
    	  Return Result.Nothing
    	End If
    
    	' in this example just deal with planar curves
    	If Not curve.IsPlanar() Then
    	  RhinoApp.WriteLine("Curve must be planar.")
    	  Return Result.Nothing
    	End If
    
    	Dim point_on_curve = curve.PointAt(curve_parameter)
    	Dim curvature_vector = curve.CurvatureAt(curve_parameter)
    	Dim len = curvature_vector.Length
    	If len < RhinoMath.SqrtEpsilon Then
    	  RhinoApp.WriteLine("Curve is almost linear and therefore has no curvature.")
    	  Return Result.Nothing
    	End If
    
    	Dim center = point_on_curve + (curvature_vector/(len*len))
    	Dim plane As Plane = Nothing
    	curve.TryGetPlane(plane)
    	Dim radial_dimension = New RadialDimension(center, point_on_curve, plane.XAxis, plane.Normal, 5.0)
    	doc.Objects.AddRadialDimension(radial_dimension)
    	doc.Views.Redraw()
    	Return Result.Success
      End Function
    End Class
    
    
    
    from Rhino import *
    from Rhino.DocObjects import *
    from Rhino.Commands import *
    from Rhino.Geometry import *
    from Rhino.Input import *
    from scriptcontext import doc
    
    def RunCommand():
        rc, obj_ref = RhinoGet.GetOneObject("Select curve for radius dimension", True, ObjectType.Curve)
        if rc != Result.Success:
            return rc
        curve, curve_parameter = obj_ref.CurveParameter()
        if curve == None:
            return Result.Failure
    
        if curve.IsLinear() or curve.IsPolyline():
            print "Curve must be non-linear."
            return Result.Nothing
    
        # in this example just deal with planar curves
        if not curve.IsPlanar():
            print "Curve must be planar."
            return Result.Nothing
    
        point_on_curve = curve.PointAt(curve_parameter)
        curvature_vector = curve.CurvatureAt(curve_parameter)
        len = curvature_vector.Length
        if len < RhinoMath.SqrtEpsilon:
            print "Curve is almost linear and therefore has no curvature."
            return Result.Nothing
    
        center = point_on_curve + (curvature_vector/(len*len))
        _, plane = curve.TryGetPlane()
        radial_dimension = RadialDimension(center, point_on_curve, plane.XAxis, plane.Normal, 5.0)
        doc.Objects.AddRadialDimension(radial_dimension)
        doc.Views.Redraw()
        return Result.Success
    
    if __name__=="__main__":
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

