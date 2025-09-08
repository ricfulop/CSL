---
url: https://developer.rhino3d.com/samples/rhinocommon/add-clipping-plane/
scraped_at: 2025-09-08T15:44:18.311315
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

Add Clipping Plane

Demonstrates how to add a clipping plane from an array or corner points.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result AddClippingPlane(Rhino.RhinoDoc doc)
      {
        // Define the corners of the clipping plane
        Rhino.Geometry.Point3d[] corners;
        Rhino.Commands.Result rc = Rhino.Input.RhinoGet.GetRectangle(out corners);
        if (rc != Rhino.Commands.Result.Success)
          return rc;
    
        // Get the active view
        Rhino.Display.RhinoView view = doc.Views.ActiveView;
        if (view == null)
          return Rhino.Commands.Result.Failure;
    
        Rhino.Geometry.Point3d p0 = corners[0];
        Rhino.Geometry.Point3d p1 = corners[1];
        Rhino.Geometry.Point3d p3 = corners[3];
    
        // Create a plane from the corner points
        Rhino.Geometry.Plane plane = new Rhino.Geometry.Plane(p0, p1, p3);
    
        // Add a clipping plane object to the document
        Guid id = doc.Objects.AddClippingPlane(plane, p0.DistanceTo(p1), p0.DistanceTo(p3), view.ActiveViewportID);
        if (id != Guid.Empty)
        {
          doc.Views.Redraw();
          return Rhino.Commands.Result.Success;
        }
        return Rhino.Commands.Result.Failure;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function AddClippingPlane(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	' Define the corners of the clipping plane
    	Dim corners() As Rhino.Geometry.Point3d = Nothing
    	Dim rc As Rhino.Commands.Result = Rhino.Input.RhinoGet.GetRectangle(corners)
    	If rc IsNot Rhino.Commands.Result.Success Then
    	  Return rc
    	End If
    
    	' Get the active view
    	Dim view As Rhino.Display.RhinoView = doc.Views.ActiveView
    	If view Is Nothing Then
    	  Return Rhino.Commands.Result.Failure
    	End If
    
    	Dim p0 As Rhino.Geometry.Point3d = corners(0)
    	Dim p1 As Rhino.Geometry.Point3d = corners(1)
    	Dim p3 As Rhino.Geometry.Point3d = corners(3)
    
    	' Create a plane from the corner points
    	Dim plane As New Rhino.Geometry.Plane(p0, p1, p3)
    
    	' Add a clipping plane object to the document
    	Dim id As Guid = doc.Objects.AddClippingPlane(plane, p0.DistanceTo(p1), p0.DistanceTo(p3), view.ActiveViewportID)
    	If id <> Guid.Empty Then
    	  doc.Views.Redraw()
    	  Return Rhino.Commands.Result.Success
    	End If
    	Return Rhino.Commands.Result.Failure
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    import System.Guid
    
    def AddClippingPlane():
        # Define the corners of the clipping plane
        rc, corners = Rhino.Input.RhinoGet.GetRectangle()
        if rc!=Rhino.Commands.Result.Success: return rc
    
        # Get the active view
        view = scriptcontext.doc.Views.ActiveView
        if view is None: return Rhino.Commands.Result.Failure
    
        p0, p1, p2, p3 = corners
        # Create a plane from the corner points
        plane = Rhino.Geometry.Plane(p0, p1, p3)
    
        # Add a clipping plane object to the document
        id = scriptcontext.doc.Objects.AddClippingPlane(plane, p0.DistanceTo(p1), p0.DistanceTo(p3), view.ActiveViewportID)
        if id!=System.Guid.Empty:
            scriptcontext.doc.Views.Redraw()
            return Rhino.Commands.Result.Success
        return Rhino.Commands.Result.Failure
    
    if __name__=="__main__":
        AddClippingPlane()
    

  

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

