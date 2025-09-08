---
url: https://developer.rhino3d.com/samples/rhinocommon/add-sphere/
scraped_at: 2025-09-08T15:44:35.374529
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

Add Sphere

Demonstrates how to create a sphere from a center point and radius.

C# VB.NET Python

    
    
    partial class Examples
    {
      public static Rhino.Commands.Result AddSphere(Rhino.RhinoDoc doc)
      {
        Rhino.Geometry.Point3d center = new Rhino.Geometry.Point3d(0, 0, 0);
        const double radius = 5.0;
        Rhino.Geometry.Sphere sphere = new Rhino.Geometry.Sphere(center, radius);
        if( doc.Objects.AddSphere(sphere) != Guid.Empty )
        {
          doc.Views.Redraw();
          return Rhino.Commands.Result.Success;
        }
        return Rhino.Commands.Result.Failure;
      }
    }
    
    
    
    Partial Friend Class Examples
      Public Shared Function AddSphere(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Dim center As New Rhino.Geometry.Point3d(0, 0, 0)
    	Const radius As Double = 5.0
    	Dim sphere As New Rhino.Geometry.Sphere(center, radius)
    	If doc.Objects.AddSphere(sphere) <> Guid.Empty Then
    	  doc.Views.Redraw()
    	  Return Rhino.Commands.Result.Success
    	End If
    	Return Rhino.Commands.Result.Failure
      End Function
    End Class
    
    
    
    import Rhino
    import scriptcontext
    import System.Guid
    
    def AddSphere():
        center = Rhino.Geometry.Point3d(0, 0, 0)
        radius = 5.0
        sphere = Rhino.Geometry.Sphere(center, radius)
        if scriptcontext.doc.Objects.AddSphere(sphere)!=System.Guid.Empty:
            scriptcontext.doc.Views.Redraw()
            return Rhino.Commands.Result.Success
        return Rhino.Commands.Result.Failure
    
    
    if __name__ == "__main__":
        AddSphere()
    

  

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

