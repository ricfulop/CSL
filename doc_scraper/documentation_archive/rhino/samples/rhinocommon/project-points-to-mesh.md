---
url: https://developer.rhino3d.com/samples/rhinocommon/project-points-to-mesh/
scraped_at: 2025-09-08T15:46:33.891354
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

Project Points to Mesh

Demonstrates how to project points to a mesh.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result ProjectPointsToMeshesEx(RhinoDoc doc)
      {
        ObjRef obj_ref;
        var rc = RhinoGet.GetOneObject("mesh", false, ObjectType.Mesh, out obj_ref);
        if (rc != Result.Success) return rc;
        var mesh = obj_ref.Mesh();
    
        ObjRef[] obj_ref_pts;
        rc = RhinoGet.GetMultipleObjects("points", false, ObjectType.Point, out obj_ref_pts);
        if (rc != Result.Success) return rc;
        var points = new List<Point3d>();
        foreach (var obj_ref_pt in obj_ref_pts)
        {
          var pt = obj_ref_pt.Point().Location;
          points.Add(pt);
        }
    
        int[] indices;
        var prj_points = Intersection.ProjectPointsToMeshesEx(new[] {mesh}, points, new Vector3d(0, 1, 0), 0, out indices);
        foreach (var prj_pt in prj_points) doc.Objects.AddPoint(prj_pt);
        doc.Views.Redraw();
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function ProjectPointsToMeshesEx(ByVal doc As RhinoDoc) As Result
    	Dim obj_ref As ObjRef = Nothing
    	Dim rc = RhinoGet.GetOneObject("mesh", False, ObjectType.Mesh, obj_ref)
    	If rc IsNot Result.Success Then
    		Return rc
    	End If
    	Dim mesh = obj_ref.Mesh()
    
    	Dim obj_ref_pts() As ObjRef = Nothing
    	rc = RhinoGet.GetMultipleObjects("points", False, ObjectType.Point, obj_ref_pts)
    	If rc IsNot Result.Success Then
    		Return rc
    	End If
    	Dim points = New List(Of Point3d)()
    	For Each obj_ref_pt In obj_ref_pts
    	  Dim pt = obj_ref_pt.Point().Location
    	  points.Add(pt)
    	Next obj_ref_pt
    
    	Dim indices() As Integer = Nothing
    	Dim prj_points = Intersection.ProjectPointsToMeshesEx( {mesh}, points, New Vector3d(0, 1, 0), 0, indices)
    	For Each prj_pt In prj_points
    		doc.Objects.AddPoint(prj_pt)
    	Next prj_pt
    	doc.Views.Redraw()
    	Return Result.Success
      End Function
    End Class
    
    
    
    from System.Collections.Generic import *
    from Rhino import *
    from Rhino.Commands import *
    from Rhino.Geometry import *
    from Rhino.Geometry.Intersect import *
    from Rhino.Input import *
    from Rhino.DocObjects import *
    from scriptcontext import doc
    
    def RunCommand():
        rc, obj_ref = RhinoGet.GetOneObject("mesh", False, ObjectType.Mesh)
        if rc != Result.Success: return rc
        mesh = obj_ref.Mesh()
    
        rc, obj_ref_pts = RhinoGet.GetMultipleObjects("points", False, ObjectType.Point)
        if rc != Result.Success: return rc
        points = []
        for obj_ref_pt in obj_ref_pts:
            pt = obj_ref_pt.Point().Location
            points.append(pt)
    
        prj_points, indices = Intersection.ProjectPointsToMeshesEx({mesh}, points, Vector3d(0, 1, 0), 0)
        for prj_pt in prj_points:
            doc.Objects.AddPoint(prj_pt)
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

