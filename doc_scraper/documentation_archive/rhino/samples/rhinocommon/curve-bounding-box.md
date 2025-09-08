---
url: https://developer.rhino3d.com/samples/rhinocommon/curve-bounding-box/
scraped_at: 2025-09-08T15:45:09.415676
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

Curve Bounding Box

Demonstrates how to create a curve bounding box (world and plane oriented).

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result CurveBoundingBox(Rhino.RhinoDoc doc)
      {
        // Select a curve object
        Rhino.DocObjects.ObjRef rhObject;
        var rc = Rhino.Input.RhinoGet.GetOneObject("Select curve", false, Rhino.DocObjects.ObjectType.Curve, out rhObject);
        if (rc != Rhino.Commands.Result.Success)
          return rc;
    
        // Validate selection
        var curve = rhObject.Curve();
        if (curve == null)
          return Rhino.Commands.Result.Failure;
    
        // Get the active view's construction plane
        var view = doc.Views.ActiveView;
        if (view == null)
          return Rhino.Commands.Result.Failure;
        var plane = view.ActiveViewport.ConstructionPlane();
    
        // Compute the tight bounding box of the curve in world coordinates
        var bbox = curve.GetBoundingBox(true);
        if (!bbox.IsValid)
          return Rhino.Commands.Result.Failure;
    
        // Print the min and max box coordinates in world coordinates
        Rhino.RhinoApp.WriteLine("World min: {0}", bbox.Min);
        Rhino.RhinoApp.WriteLine("World max: {0}", bbox.Max);
    
        // Compute the tight bounding box of the curve based on the
        // active view's construction plane
        bbox = curve.GetBoundingBox(plane);
    
        // Print the min and max box coordinates in cplane coordinates
        Rhino.RhinoApp.WriteLine("CPlane min: {0}", bbox.Min);
        Rhino.RhinoApp.WriteLine("CPlane max: {0}", bbox.Max);
        return Rhino.Commands.Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function CurveBoundingBox(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	' Select a curve object
    	Dim rhObject As Rhino.DocObjects.ObjRef = Nothing
    	Dim rc = Rhino.Input.RhinoGet.GetOneObject("Select curve", False, Rhino.DocObjects.ObjectType.Curve, rhObject)
    	If rc IsNot Rhino.Commands.Result.Success Then
    	  Return rc
    	End If
    
    	' Validate selection
    	Dim curve = rhObject.Curve()
    	If curve Is Nothing Then
    	  Return Rhino.Commands.Result.Failure
    	End If
    
    	' Get the active view's construction plane
    	Dim view = doc.Views.ActiveView
    	If view Is Nothing Then
    	  Return Rhino.Commands.Result.Failure
    	End If
    	Dim plane = view.ActiveViewport.ConstructionPlane()
    
    	' Compute the tight bounding box of the curve in world coordinates
    	Dim bbox = curve.GetBoundingBox(True)
    	If Not bbox.IsValid Then
    	  Return Rhino.Commands.Result.Failure
    	End If
    
    	' Print the min and max box coordinates in world coordinates
    	Rhino.RhinoApp.WriteLine("World min: {0}", bbox.Min)
    	Rhino.RhinoApp.WriteLine("World max: {0}", bbox.Max)
    
    	' Compute the tight bounding box of the curve based on the
    	' active view's construction plane
    	bbox = curve.GetBoundingBox(plane)
    
    	' Print the min and max box coordinates in cplane coordinates
    	Rhino.RhinoApp.WriteLine("CPlane min: {0}", bbox.Min)
    	Rhino.RhinoApp.WriteLine("CPlane max: {0}", bbox.Max)
    	Return Rhino.Commands.Result.Success
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    
    def CurveBoundingBox():
        # Select a curve object
        rc, rhobject = Rhino.Input.RhinoGet.GetOneObject("Select curve", False, Rhino.DocObjects.ObjectType.Curve)
        if rc!=Rhino.Commands.Result.Success: return
    
        # Validate selection
        curve = rhobject.Curve()
        if not curve: return
    
        ## Get the active view's construction plane
        view = scriptcontext.doc.Views.ActiveView
        if not view: return
        plane = view.ActiveViewport.ConstructionPlane()
    
        # Compute the tight bounding box of the curve in world coordinates
        bbox = curve.GetBoundingBox(True)
        if not bbox.IsValid: return
    
        # Print the min and max box coordinates in world coordinates
        print "World min:", bbox.Min
        print "World max:", bbox.Max
    
        # Compute the tight bounding box of the curve based on the
        # active view's construction plane
        bbox = curve.GetBoundingBox(plane)
    
        # Print the min and max box coordinates in cplane coordinates
        print "CPlane min:", bbox.Min
        print "CPlane max:", bbox.Max
    
    if __name__=="__main__":
        CurveBoundingBox()
    

  

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

