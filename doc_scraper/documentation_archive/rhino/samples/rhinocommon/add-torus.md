---
url: https://developer.rhino3d.com/samples/rhinocommon/add-torus/
scraped_at: 2025-09-08T15:44:37.400903
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

Add Torus

Demonstrates how to construct a torus from a set of radii and a plane.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result AddTorus(Rhino.RhinoDoc doc)
      {
        const double major_radius = 4.0;
        const double minor_radius = 2.0;
    
        Rhino.Geometry.Plane plane = Rhino.Geometry.Plane.WorldXY;
        Rhino.Geometry.Torus torus = new Rhino.Geometry.Torus(plane, major_radius, minor_radius);
        Rhino.Geometry.RevSurface revsrf = torus.ToRevSurface();
        if (doc.Objects.AddSurface(revsrf) != Guid.Empty)
        {
          doc.Views.Redraw();
          return Rhino.Commands.Result.Success;
        }
        return Rhino.Commands.Result.Failure;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function AddTorus(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Const major_radius As Double = 4.0
    	Const minor_radius As Double = 2.0
    
    	Dim plane As Rhino.Geometry.Plane = Rhino.Geometry.Plane.WorldXY
    	Dim torus As New Rhino.Geometry.Torus(plane, major_radius, minor_radius)
    	Dim revsrf As Rhino.Geometry.RevSurface = torus.ToRevSurface()
    	If doc.Objects.AddSurface(revsrf) <> Guid.Empty Then
    	  doc.Views.Redraw()
    	  Return Rhino.Commands.Result.Success
    	End If
    	Return Rhino.Commands.Result.Failure
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    import System.Guid
    
    def AddTorus():
        major_radius = 4.0
        minor_radius = 2.0
    
        plane = Rhino.Geometry.Plane.WorldXY
        torus = Rhino.Geometry.Torus(plane, major_radius, minor_radius)
        revsrf = torus.ToRevSurface()
    
        if scriptcontext.doc.Objects.AddSurface(revsrf)!=System.Guid.Empty:
            scriptcontext.doc.Views.Redraw()
            return Rhino.Commands.Result.Success
        return Rhino.Commands.Result.Failure
    
    
    if __name__=="__main__":
        AddTorus()
    

  

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

