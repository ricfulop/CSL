---
url: https://developer.rhino3d.com/samples/rhinocommon/create-contour-curves/
scraped_at: 2025-09-08T15:45:08.520196
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

Create Contour Curves

Demonstrates how to create contour curves on user-specified objects.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result ContourCurves(RhinoDoc doc)
      {
        var filter = ObjectType.Surface | ObjectType.PolysrfFilter | ObjectType.Mesh;
        ObjRef[] obj_refs;
        var rc = RhinoGet.GetMultipleObjects("Select objects to contour", false, filter, out obj_refs);
        if (rc != Result.Success)
          return rc;
    
        var gp = new GetPoint();
        gp.SetCommandPrompt("Contour plane base point");
        gp.Get();
        if (gp.CommandResult() != Result.Success)
          return gp.CommandResult();
        var base_point = gp.Point();
    
        gp.DrawLineFromPoint(base_point, true);
        gp.SetCommandPrompt("Direction perpendicular to contour planes");
        gp.Get();
        if (gp.CommandResult() != Result.Success)
          return gp.CommandResult();
        var end_point = gp.Point();
    
        if (base_point.DistanceTo(end_point) < RhinoMath.ZeroTolerance)
          return Result.Nothing;
    
        double distance = 1.0;
        rc = RhinoGet.GetNumber("Distance between contours", false, ref distance);
        if (rc != Result.Success)
          return rc;
    
        var interval = Math.Abs(distance);
    
        Curve[] curves = null;
        foreach (var obj_ref in obj_refs)
        {
          var geometry = obj_ref.Geometry();
          if (geometry == null)
            return Result.Failure;
    
          if (geometry is Brep)
          {
            curves = Brep.CreateContourCurves(geometry as Brep, base_point, end_point, interval);
          }
          else
          {
            curves = Mesh.CreateContourCurves(geometry as Mesh, base_point, end_point, interval);
          }
    
          foreach (var curve in curves)
          {
            var curve_object_id = doc.Objects.AddCurve(curve);
            doc.Objects.Select(curve_object_id);
          }
        }
    
        if (curves != null)
          doc.Views.Redraw();
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function ContourCurves(ByVal doc As RhinoDoc) As Result
    	Dim filter = ObjectType.Surface Or ObjectType.PolysrfFilter Or ObjectType.Mesh
    	Dim obj_refs() As ObjRef = Nothing
    	Dim rc = RhinoGet.GetMultipleObjects("Select objects to contour", False, filter, obj_refs)
    	If rc IsNot Result.Success Then
    	  Return rc
    	End If
    
    	Dim gp = New GetPoint()
    	gp.SetCommandPrompt("Contour plane base point")
    	gp.Get()
    	If gp.CommandResult() <> Result.Success Then
    	  Return gp.CommandResult()
    	End If
    	Dim base_point = gp.Point()
    
    	gp.DrawLineFromPoint(base_point, True)
    	gp.SetCommandPrompt("Direction perpendicular to contour planes")
    	gp.Get()
    	If gp.CommandResult() <> Result.Success Then
    	  Return gp.CommandResult()
    	End If
    	Dim end_point = gp.Point()
    
    	If base_point.DistanceTo(end_point) < RhinoMath.ZeroTolerance Then
    	  Return Result.Nothing
    	End If
    
    	Dim distance As Double = 1.0
    	rc = RhinoGet.GetNumber("Distance between contours", False, distance)
    	If rc IsNot Result.Success Then
    	  Return rc
    	End If
    
    	Dim interval = Math.Abs(distance)
    
    	Dim curves() As Curve = Nothing
    	For Each obj_ref In obj_refs
    	  Dim geometry = obj_ref.Geometry()
    	  If geometry Is Nothing Then
    		Return Result.Failure
    	  End If
    
    	  If TypeOf geometry Is Brep Then
    		curves = Brep.CreateContourCurves(TryCast(geometry, Brep), base_point, end_point, interval)
    	  Else
    		curves = Mesh.CreateContourCurves(TryCast(geometry, Mesh), base_point, end_point, interval)
    	  End If
    
    	  For Each curve In curves
    		Dim curve_object_id = doc.Objects.AddCurve(curve)
    		doc.Objects.Select(curve_object_id)
    	  Next curve
    	Next obj_ref
    
    	If curves IsNot Nothing Then
    	  doc.Views.Redraw()
    	End If
    	Return Result.Success
      End Function
    End Class
    
    
    
    from System import *
    from Rhino import *
    from Rhino.DocObjects import *
    from Rhino.Geometry import *
    from Rhino.Input import *
    from Rhino.Input.Custom import *
    from Rhino.Commands import *
    from scriptcontext import doc
    
    def RunCommand():
        filter = ObjectType.Surface | ObjectType.PolysrfFilter | ObjectType.Mesh
        rc, obj_refs = RhinoGet.GetMultipleObjects("Select objects to contour", False, filter)
        if rc != Result.Success:
            return rc
    
        gp = GetPoint()
        gp.SetCommandPrompt("Contour plane base point")
        gp.Get()
        if gp.CommandResult() != Result.Success:
            return gp.CommandResult()
        base_point = gp.Point()
    
        gp.DrawLineFromPoint(base_point, True)
        gp.SetCommandPrompt("Direction perpendicular to contour planes")
        gp.Get()
        if gp.CommandResult() != Result.Success:
            return gp.CommandResult()
        end_point = gp.Point()
    
        if base_point.DistanceTo(end_point) < RhinoMath.ZeroTolerance:
            return Result.Nothing
    
        distance = 1.0
        rc, distance = RhinoGet.GetNumber("Distance between contours", False, distance)
        if rc != Result.Success:
            return rc
    
        interval = Math.Abs(distance)
    
        for obj_ref in obj_refs:
            geometry = obj_ref.Geometry()
            if geometry == None:
                return Result.Failure
    
            if type(geometry) == Brep:
                curves = Brep.CreateContourCurves(geometry, base_point, end_point, interval)
            else:
                curves = Mesh.CreateContourCurves(geometry, base_point, end_point, interval)
    
            for curve in curves:
                curve_object_id = doc.Objects.AddCurve(curve)
                doc.Objects.Select(curve_object_id)
    
        if curves != None:
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

