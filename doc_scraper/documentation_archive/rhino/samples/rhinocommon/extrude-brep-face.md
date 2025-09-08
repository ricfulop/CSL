---
url: https://developer.rhino3d.com/samples/rhinocommon/extrude-brep-face/
scraped_at: 2025-09-08T15:46:10.774619
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

Extrude Brep Face

Demonstrates how to extrude the Brep face from a user-specified surface.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result ExtrudeBrepFace(Rhino.RhinoDoc doc)
      {
        Rhino.Input.Custom.GetObject go0 = new Rhino.Input.Custom.GetObject();
        go0.SetCommandPrompt("Select surface to extrude");
        go0.GeometryFilter = Rhino.DocObjects.ObjectType.Surface;
        go0.SubObjectSelect = true;
        go0.Get();
        if (go0.CommandResult() != Rhino.Commands.Result.Success)
          return go0.CommandResult();
    
        Rhino.Geometry.BrepFace face = go0.Object(0).Face();
        if (null == face)
          return Rhino.Commands.Result.Failure;
    
        Rhino.Input.Custom.GetObject go1 = new Rhino.Input.Custom.GetObject();
        go1.SetCommandPrompt("Select path curve");
        go1.GeometryFilter = Rhino.DocObjects.ObjectType.Curve;
        go1.SubObjectSelect = true;
        go1.DeselectAllBeforePostSelect = false;
        go1.Get();
        if (go1.CommandResult() != Rhino.Commands.Result.Success)
          return go1.CommandResult();
    
        Rhino.Geometry.Curve curve = go1.Object(0).Curve();
        if (null == curve)
          return Rhino.Commands.Result.Failure;
    
        Rhino.Geometry.Brep brep = face.CreateExtrusion(curve, true);
        if (null != brep)
        {
          doc.Objects.Add(brep);
          doc.Views.Redraw();
        }
    
        return Rhino.Commands.Result.Success;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function ExtrudeBrepFace(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Dim go0 As New Rhino.Input.Custom.GetObject()
    	go0.SetCommandPrompt("Select surface to extrude")
    	go0.GeometryFilter = Rhino.DocObjects.ObjectType.Surface
    	go0.SubObjectSelect = True
    	go0.Get()
    	If go0.CommandResult() <> Rhino.Commands.Result.Success Then
    	  Return go0.CommandResult()
    	End If
    
    	Dim face As Rhino.Geometry.BrepFace = go0.Object(0).Face()
    	If Nothing Is face Then
    	  Return Rhino.Commands.Result.Failure
    	End If
    
    	Dim go1 As New Rhino.Input.Custom.GetObject()
    	go1.SetCommandPrompt("Select path curve")
    	go1.GeometryFilter = Rhino.DocObjects.ObjectType.Curve
    	go1.SubObjectSelect = True
    	go1.DeselectAllBeforePostSelect = False
    	go1.Get()
    	If go1.CommandResult() <> Rhino.Commands.Result.Success Then
    	  Return go1.CommandResult()
    	End If
    
    	Dim curve As Rhino.Geometry.Curve = go1.Object(0).Curve()
    	If Nothing Is curve Then
    	  Return Rhino.Commands.Result.Failure
    	End If
    
    	Dim brep As Rhino.Geometry.Brep = face.CreateExtrusion(curve, True)
    	If Nothing IsNot brep Then
    	  doc.Objects.Add(brep)
    	  doc.Views.Redraw()
    	End If
    
    	Return Rhino.Commands.Result.Success
      End Function
    End Class
    
    
    
    # No Python sample available
    

  

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

