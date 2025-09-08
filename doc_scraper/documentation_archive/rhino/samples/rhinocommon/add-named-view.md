---
url: https://developer.rhino3d.com/samples/rhinocommon/add-named-view/
scraped_at: 2025-09-08T15:44:30.243939
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

Add Named View

Demonstrates how to add a named view to a Rhino model from a user-specified
view and camera location.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result AddNamedView(Rhino.RhinoDoc doc)
      {
        Rhino.Display.RhinoView view;
        Rhino.Commands.Result rc = Rhino.Input.RhinoGet.GetView("Select view to adjust", out view);
        if (rc != Rhino.Commands.Result.Success)
          return rc;
    
        Rhino.Geometry.Point3d location;
        rc = Rhino.Input.RhinoGet.GetPoint("Camera Location", false, out location);
        if (rc != Rhino.Commands.Result.Success)
          return rc;
    
        Rhino.Input.Custom.GetPoint gp = new Rhino.Input.Custom.GetPoint();
        gp.SetCommandPrompt("Look At Location");
        gp.DrawLineFromPoint(location, false);
        gp.Get();
        if (gp.CommandResult() != Rhino.Commands.Result.Success)
          return gp.CommandResult();
        Rhino.Geometry.Point3d lookat = gp.Point();
    
        string name = view.ActiveViewport.Name;
        rc = Rhino.Input.RhinoGet.GetString("Name", true, ref name);
        if (rc != Rhino.Commands.Result.Success)
          return rc;
    
        Rhino.Display.RhinoViewport vp = view.ActiveViewport;
        // save the current viewport projection
        vp.PushViewProjection();
        vp.CameraUp = Rhino.Geometry.Vector3d.ZAxis;
        vp.SetCameraLocation(location, false);
        vp.SetCameraDirection(lookat - location, true);
        vp.Name = name;
    
        doc.NamedViews.Add(name, vp.Id);
        view.Redraw();
        return Rhino.Commands.Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function AddNamedView(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Dim view As Rhino.Display.RhinoView = Nothing
    	Dim rc As Rhino.Commands.Result = Rhino.Input.RhinoGet.GetView("Select view to adjust", view)
    	If rc IsNot Rhino.Commands.Result.Success Then
    	  Return rc
    	End If
    
    	Dim location As Rhino.Geometry.Point3d = Nothing
    	rc = Rhino.Input.RhinoGet.GetPoint("Camera Location", False, location)
    	If rc IsNot Rhino.Commands.Result.Success Then
    	  Return rc
    	End If
    
    	Dim gp As New Rhino.Input.Custom.GetPoint()
    	gp.SetCommandPrompt("Look At Location")
    	gp.DrawLineFromPoint(location, False)
    	gp.Get()
    	If gp.CommandResult() <> Rhino.Commands.Result.Success Then
    	  Return gp.CommandResult()
    	End If
    	Dim lookat As Rhino.Geometry.Point3d = gp.Point()
    
    	Dim name As String = view.ActiveViewport.Name
    	rc = Rhino.Input.RhinoGet.GetString("Name", True, name)
    	If rc IsNot Rhino.Commands.Result.Success Then
    	  Return rc
    	End If
    
    	Dim vp As Rhino.Display.RhinoViewport = view.ActiveViewport
    	' save the current viewport projection
    	vp.PushViewProjection()
    	vp.CameraUp = Rhino.Geometry.Vector3d.ZAxis
    	vp.SetCameraLocation(location, False)
    	vp.SetCameraDirection(lookat - location, True)
    	vp.Name = name
    
    	doc.NamedViews.Add(name, vp.Id)
    	view.Redraw()
    	Return Rhino.Commands.Result.Success
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    import System.Guid
    
    def AddNamedView():
        rc, view = Rhino.Input.RhinoGet.GetView("Select view to adjust")
        if rc!=Rhino.Commands.Result.Success: return rc
    
        rc, location = Rhino.Input.RhinoGet.GetPoint("Camera Location", False)
        if rc!=Rhino.Commands.Result.Success: return rc
    
        gp = Rhino.Input.Custom.GetPoint()
        gp.SetCommandPrompt("Look At Location")
        gp.DrawLineFromPoint(location, False)
        gp.Get()
        if gp.CommandResult()!=Rhino.Commands.Result.Success:
            return gp.CommandResult()
        lookat = gp.Point()
    
        name = view.ActiveViewport.Name
        rc, name = Rhino.Input.RhinoGet.GetString("Name", True, name)
        if rc!=Rhino.Commands.Result.Success: return rc
    
        vp = view.ActiveViewport
        # save the current viewport projection
        vp.PushViewProjection()
        vp.CameraUp = Rhino.Geometry.Vector3d.ZAxis
        vp.SetCameraLocation(location, False)
        vp.SetCameraDirection(lookat - location, True)
        vp.Name = name
    
        scriptcontext.doc.NamedViews.Add(name, vp.Id)
        view.Redraw()
        return Rhino.Commands.Result.Success
    
    if __name__=="__main__":
        AddNamedView()
    

  

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

