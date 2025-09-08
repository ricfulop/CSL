---
url: https://developer.rhino3d.com/samples/rhinocommon/pick-point/
scraped_at: 2025-09-08T15:44:52.475183
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

Pick Point

Demonstrates how to pick and select a point object.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result PickPoint(RhinoDoc doc)
      {
        // this creates a point where the mouse is clicked.
        var gp = new GetPoint();
        gp.SetCommandPrompt("Click for new point");
        gp.Get();
        if (gp.CommandResult() != Result.Success)
          return gp.CommandResult();
        var point3d = gp.Point();
        doc.Objects.AddPoint(point3d);
        doc.Views.Redraw();
    
        // selects a point that already exists
        ObjRef obj_ref;
        var rc = RhinoGet.GetOneObject("Select point", false, ObjectType.Point, out obj_ref);
        if (rc != Result.Success)
          return rc;
        var point = obj_ref.Point();
        RhinoApp.WriteLine("Point: x:{0}, y:{1}, z:{2}",
          point.Location.X,
          point.Location.Y,
          point.Location.Z);
        doc.Objects.UnselectAll();
    
        // selects multiple points that already exist
        ObjRef[] obj_refs;
        rc = RhinoGet.GetMultipleObjects("Select point", false, ObjectType.Point, out obj_refs);
        if (rc != Result.Success)
          return rc;
        foreach (var o_ref in obj_refs)
        {
          point = o_ref.Point();
          RhinoApp.WriteLine("Point: x:{0}, y:{1}, z:{2}",
            point.Location.X,
            point.Location.Y,
            point.Location.Z);
        }
        doc.Objects.UnselectAll();
    
        // also selects a point that already exists.
        // Used when RhinoGet doesn't provide enough control
        var go = new GetObject();
        go.SetCommandPrompt("Select point");
        go.GeometryFilter = ObjectType.Point;
        go.GetMultiple(1, 0);
        if (go.CommandResult() != Result.Success)
          return go.CommandResult();
        foreach (var o_ref in  go.Objects())
        {
          point = o_ref.Point();
          if (point != null)
            RhinoApp.WriteLine("Point: x:{0}, y:{1}, z:{2}",
              point.Location.X,
              point.Location.Y,
              point.Location.Z);
        }
    
        doc.Views.Redraw();
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function PickPoint(ByVal doc As RhinoDoc) As Result
    	' this creates a point where the mouse is clicked.
    	Dim gp = New GetPoint()
    	gp.SetCommandPrompt("Click for new point")
    	gp.Get()
    	If gp.CommandResult() <> Result.Success Then
    	  Return gp.CommandResult()
    	End If
    	Dim point3d = gp.Point()
    	doc.Objects.AddPoint(point3d)
    	doc.Views.Redraw()
    
    	' selects a point that already exists
    	Dim obj_ref As ObjRef = Nothing
    	Dim rc = RhinoGet.GetOneObject("Select point", False, ObjectType.Point, obj_ref)
    	If rc IsNot Result.Success Then
    	  Return rc
    	End If
    	Dim point = obj_ref.Point()
    	RhinoApp.WriteLine("Point: x:{0}, y:{1}, z:{2}", point.Location.X, point.Location.Y, point.Location.Z)
    	doc.Objects.UnselectAll()
    
    	' selects multiple points that already exist
    	Dim obj_refs() As ObjRef = Nothing
    	rc = RhinoGet.GetMultipleObjects("Select point", False, ObjectType.Point, obj_refs)
    	If rc IsNot Result.Success Then
    	  Return rc
    	End If
    	For Each o_ref In obj_refs
    	  point = o_ref.Point()
    	  RhinoApp.WriteLine("Point: x:{0}, y:{1}, z:{2}", point.Location.X, point.Location.Y, point.Location.Z)
    	Next o_ref
    	doc.Objects.UnselectAll()
    
    	' also selects a point that already exists.
    	' Used when RhinoGet doesn't provide enough control
    	Dim go = New GetObject()
    	go.SetCommandPrompt("Select point")
    	go.GeometryFilter = ObjectType.Point
    	go.GetMultiple(1, 0)
    	If go.CommandResult() <> Result.Success Then
    	  Return go.CommandResult()
    	End If
    	For Each o_ref In go.Objects()
    	  point = o_ref.Point()
    	  If point IsNot Nothing Then
    		RhinoApp.WriteLine("Point: x:{0}, y:{1}, z:{2}", point.Location.X, point.Location.Y, point.Location.Z)
    	  End If
    	Next o_ref
    
    	doc.Views.Redraw()
    	Return Result.Success
      End Function
    End Class
    
    
    
    from Rhino import *
    from Rhino.DocObjects import *
    from Rhino.Commands import *
    from Rhino.Input import *
    from Rhino.Input.Custom import *
    from scriptcontext import doc
    import rhinoscriptsyntax as rs
    
    def RunCommand():
        # creates a point where the mouse is clicked
        # using RhinoCommon
        gp = GetPoint()
        gp.SetCommandPrompt("Click for point")
        gp.Get()
        if gp.CommandResult() != Result.Success:
            return gp.CommandResult()
        point3d = gp.Point()
        doc.Objects.AddPoint(point3d)
        doc.Views.Redraw()
    
        # creates a point where the mouse is clicked
        # using the RhinoScript syntax
        point3d = rs.GetPoint("Click for point")
        if point3d == None: return Result.Nothing
        rs.AddPoint(point3d)
        doc.Objects.AddPoint(point3d)
    
    
        # selects a point that already exists
        # using RhinoCommon
        rc, obj_ref = RhinoGet.GetOneObject("Select point", False, ObjectType.Point)
        if rc != Result.Success:
            return rc
        point = obj_ref.Point()
        RhinoApp.WriteLine("Point: x:{0}, y:{1}, z:{2}", point.Location.X, point.Location.Y, point.Location.Z)
        doc.Objects.UnselectAll()
    
        # also selects a point that already exists
        # using RhinoCommon
        # Used when RhinoGet doesn't provide enough control
        go = GetObject()
        go.SetCommandPrompt("Select point")
        go.GeometryFilter = ObjectType.Point
        go.GetMultiple(1, 0)
        if go.CommandResult() != Result.Success:
            return go.CommandResult()
        for o_ref in  go.Objects():
            point = o_ref.Point()
            if point != None:
                RhinoApp.WriteLine("Point: x:{0}, y:{1}, z:{2}", point.Location.X, point.Location.Y, point.Location.Z)
        doc.Objects.UnselectAll()
    
        # selects a point that already exists
        # using RhinoScript syntax
        point_id = rs.GetObject("Select point", rs.filter.point)
        if point_id == None: return Result.Nothing
        print "point id: {0}".format(point_id)
        rs.UnselectAllObjects()
    
        # selects multiple points that already exist
        rc, obj_refs = RhinoGet.GetMultipleObjects("Select point", False, ObjectType.Point)
        if rc != Result.Success:
            return rc
        for o_ref in obj_refs:
            point = o_ref.Point()
            RhinoApp.WriteLine("Point: x:{0}, y:{1}, z:{2}", point.Location.X, point.Location.Y, point.Location.Z)
        doc.Objects.UnselectAll()
    
        # selects multiple poins that already exists
        # using the RhinoScript syntax
        point_ids = rs.GetObjects("Select point", rs.filter.point)
        for p_id in point_ids:
            print "point id: {0}".format(p_id)
    
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

