---
url: https://developer.rhino3d.com/samples/rhinocommon/brep-from-curve-bounding-box/
scraped_at: 2025-09-08T15:45:05.572337
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

Brep from Curve Bounding Box

Demonstrates how to create a valid Brep from a curve's bounding box.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Result BrepFromCurveBBox(RhinoDoc doc)
      {
        Rhino.DocObjects.ObjRef objref;
        var rc = RhinoGet.GetOneObject("Select Curve", false, ObjectType.Curve, out objref);
        if( rc != Result.Success )
          return rc;
        var curve = objref.Curve();
    
        var view = doc.Views.ActiveView;
        var plane = view.ActiveViewport.ConstructionPlane();
        // Create a construction plane aligned bounding box
        var bbox = curve.GetBoundingBox(plane);
    
        if (bbox.IsDegenerate(doc.ModelAbsoluteTolerance) > 0) {
          RhinoApp.WriteLine("the curve's bounding box is degenerate (flat) in at least one direction so a box cannot be created.");
          return Result.Failure;
        }
        var brep = Brep.CreateFromBox(bbox);
        doc.Objects.AddBrep(brep);
        doc.Views.Redraw();
        return Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function BrepFromCurveBBox(ByVal doc As RhinoDoc) As Result
    	Dim objref As Rhino.DocObjects.ObjRef = Nothing
    	Dim rc = RhinoGet.GetOneObject("Select Curve", False, ObjectType.Curve, objref)
    	If rc IsNot Result.Success Then
    	  Return rc
    	End If
    	Dim curve = objref.Curve()
    
    	Dim view = doc.Views.ActiveView
    	Dim plane = view.ActiveViewport.ConstructionPlane()
    	' Create a construction plane aligned bounding box
    	Dim bbox = curve.GetBoundingBox(plane)
    
    	If bbox.IsDegenerate(doc.ModelAbsoluteTolerance) > 0 Then
    	  RhinoApp.WriteLine("the curve's bounding box is degenerate (flat) in at least one direction so a box cannot be created.")
    	  Return Result.Failure
    	End If
    	Dim brep = Brep.CreateFromBox(bbox)
    	doc.Objects.AddBrep(brep)
    	doc.Views.Redraw()
    	Return Result.Success
      End Function
    End Class
    
    
    
    import Rhino
    from Rhino.Geometry import *
    from Rhino.Commands import Result
    from Rhino.Input import RhinoGet
    from Rhino.DocObjects import ObjectType
    import rhinoscriptsyntax as rs
    from scriptcontext import doc
    
    def RunCommand():
        rc, objRef = RhinoGet.GetOneObject("Select curve", False, ObjectType.Curve)
        if rc != Result.Success:
            return rc
        curve = objRef.Curve()
        if None == curve:
            return Result.Failure
    
        view = doc.Views.ActiveView
        plane = view.ActiveViewport.ConstructionPlane()
        # Create a construction plane aligned bounding box
        bbox = curve.GetBoundingBox(plane)
    
        if bbox.IsDegenerate(doc.ModelAbsoluteTolerance) > 0:
            print "the curve's bounding box is degenerate (flat) in at least one direction so a box cannot be created."
            return Result.Failure
    
        brep = Brep.CreateFromBox(bbox)
        doc.Objects.AddBrep(brep)
        doc.Views.Redraw()
    
        return Result.Success
    
    if __name__ == "__main__":
        print RunCommand()
    

  

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

