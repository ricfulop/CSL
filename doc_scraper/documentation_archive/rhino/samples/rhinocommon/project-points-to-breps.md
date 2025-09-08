---
url: https://developer.rhino3d.com/samples/rhinocommon/project-points-to-breps/
scraped_at: 2025-09-08T15:46:32.908439
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

Project Points to Breps

Demonstrates how to project points to Brep objects.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result ProjectPointsToBreps(RhinoDoc doc)
      {
        var gs = new GetObject();
        gs.SetCommandPrompt("select surface");
        gs.GeometryFilter = ObjectType.Surface | ObjectType.PolysrfFilter;
        gs.DisablePreSelect();
        gs.SubObjectSelect = false;
        gs.Get();
        if (gs.CommandResult() != Result.Success)
          return gs.CommandResult();
        var brep = gs.Object(0).Brep();
        if (brep == null)
          return Result.Failure;
    
        var points = Intersection.ProjectPointsToBreps(
                     new List<Brep> {brep}, // brep on which to project
                     new List<Point3d> {new Point3d(0, 0, 0), new Point3d(3,0,3), new Point3d(-2,0,-2)}, // some random points to project
                     new Vector3d(0, 1, 0), // project on Y axis
                     doc.ModelAbsoluteTolerance);
    
        if (points != null && points.Length > 0)
        {
          foreach (var point in points)
          {
            doc.Objects.AddPoint(point);
          }
        }
        doc.Views.Redraw();
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function ProjectPointsToBreps(ByVal doc As RhinoDoc) As Result
    	Dim gs = New GetObject()
    	gs.SetCommandPrompt("select surface")
    	gs.GeometryFilter = ObjectType.Surface Or ObjectType.PolysrfFilter
    	gs.DisablePreSelect()
    	gs.SubObjectSelect = False
    	gs.Get()
    	If gs.CommandResult() <> Result.Success Then
    	  Return gs.CommandResult()
    	End If
    	Dim brep = gs.Object(0).Brep()
    	If brep Is Nothing Then
    	  Return Result.Failure
    	End If
    
    	Dim points = Intersection.ProjectPointsToBreps(New List(Of Brep) _
    	    From {brep}, New List(Of Point3d)
    	    From {New Point3d(0, 0, 0), New Point3d(3,0,3), New Point3d(-2,0,-2)}, New Vector3d(0, 1, 0), doc.ModelAbsoluteTolerance) ' project on Y axis -  some random points to project -  brep on which to project
    
    	If points IsNot Nothing AndAlso points.Length > 0 Then
    	  For Each point In points
    		doc.Objects.AddPoint(point)
    	  Next point
    	End If
    	doc.Views.Redraw()
    	Return Result.Success
      End Function
    End Class
    
    
    
    import rhinoscriptsyntax as rs
    from scriptcontext import *
    from Rhino.Geometry import *
    
    def RunCommand():
        srfid = rs.GetObject("select surface", rs.filter.surface | rs.filter.polysurface)
        if not srfid: return
        brep = rs.coercebrep(srfid)
        if not brep: return
    
        pts = Intersect.Intersection.ProjectPointsToBreps(
            [brep], # brep on which to project
            [Point3d(0, 0, 0), Point3d(3,0,3), Point3d(-2,0,-2)], # points to project
            Vector3d(0, 1, 0), # project on Y axis
            doc.ModelAbsoluteTolerance)
    
        if pts != None and pts.Length > 0:
            for pt in pts:
                doc.Objects.AddPoint(pt)
    
        doc.Views.Redraw()
    
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

